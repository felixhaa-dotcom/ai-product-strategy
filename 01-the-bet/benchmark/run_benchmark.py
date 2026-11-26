"""Synthetic offline classification experiment; no external data, no production or LLM claims."""
import csv, json, random, re, time, statistics, math, sys
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import sklearn
ROOT=Path(__file__).resolve().parent
LABELS=['technical_failure','planned_maintenance','grid_curtailment','high_wind','low_wind']
TRAIN=[['gearbox fault confirmed','bearing failure confirmed','generator fault confirmed','drive train failure','converter malfunction','mechanical defect','gearbox alarm fault','electrical component failure'],['planned maintenance order','scheduled service visit','preventive maintenance','maintenance work order','scheduled inspection','planned oil change','service crew inspection','scheduled maintenance window'],['grid operator curtailment','dispatch limit request','grid export restriction','network curtailment','power reduction requested by grid','grid setpoint limit','operator dispatch restriction','external grid limit'],['high wind shutdown','storm wind exceeds limit','wind speed above cutout','gust safety shutdown','high wind protection','storm protection active','wind exceeds operating limit','excessive wind speed'],['low wind standby','below cut in wind speed','insufficient wind resource','low wind no generation','calm wind standby','wind speed below threshold','weak wind resource','below cutin wind']]
EXACT=['gearbox fault','planned maintenance','grid operator curtailment','high wind shutdown','low wind standby']
PARA=[['generator malfunction logged','bearing defect confirmed','converter failure recorded'],['scheduled service documented','preventive inspection logged','maintenance visit scheduled'],['network export restriction logged','dispatch setpoint limit recorded','grid reduction requested'],['storm protection logged','gust speed exceeds limit','wind above cutout recorded'],['insufficient wind logged','calm standby recorded','wind below cutin observed']]
# Entirely invented OEM-specific code tables. The same code can mean different things per fictional OEM.
K0={(o,f'K{(i+j)%5}'):label for j,o in enumerate(['OEM-X','OEM-Y']) for i,label in enumerate(LABELS)}
# Development-only correction examples; test rows are independently generated instances of recurring codes.
CORRECTIONS=[{'oem':o,'code':f'N{(i+j)%5}','label':label,'approval':'synthetic-approved','id':f'DEV-{j}-{i}'} for j,o in enumerate(['OEM-X','OEM-Y']) for i,label in enumerate(LABELS)]
K1={**K0,**{(x['oem'],x['code']):x['label'] for x in CORRECTIONS}}
POLICIES=['conflict','missing','critical','unauthorized','injection','unverified_claim','provider_outage','duplicate']

def encode(e):
    if e['source']=='source-A':return dict(e)
    return {'src':'source-B','record':e['id'],'machine':e['oem'],'alarm':e['code'],'note':e['text'],'has_evidence':e['evidence'],'permitted':e['authorized'],'flag':e['flag'],'variant':e['variant']}

def normalize(raw):
    if raw.get('source')=='source-A':return dict(raw)
    return dict(source=raw['src'],id=raw['record'],oem=raw['machine'],code=raw['alarm'],text=raw['note'],evidence=raw['has_evidence'],authorized=raw['permitted'],flag=raw['flag'],variant=raw['variant'])

def generate(split, per_class, per_policy, seed):
    rng=random.Random(seed); out=[]; idx=0
    def add(oem,code,text,expected,variant,flag='',evidence=True,authorized=True):
        nonlocal idx
        idx+=1; e=dict(id=f'{split}-{idx:04}',source=rng.choice(['source-A','source-B']),oem=oem,code=code,text=text,flag=flag,evidence=evidence,authorized=authorized,variant=variant)
        out.append((encode(e),expected))
    variants=['exact','paraphrase','known_code','new_code','unknown_code']
    # Balanced by category and mode; case frequency is deliberately synthetic, not an estimate of operational mix.
    for i,label in enumerate(LABELS):
        for k in range(per_class):
            v=variants[k%5]; j=rng.randrange(2); o=['OEM-X','OEM-Y'][j]; tail=rng.choice([' confirmed',' recorded',' in event log',' at inspection',' verified'])
            code=''; text=''
            if v=='exact': text=EXACT[i]+tail
            elif v=='paraphrase':text=rng.choice(PARA[i])+tail
            elif v=='known_code':code=f'K{(i+j)%5}';text='status changed'+tail
            elif v=='new_code':code=f'N{(i+j)%5}';text='controller state changed'+tail
            else:code=f'U{rng.randrange(100,999)}';text='unknown controller state'+tail
            add(o,code,text,label,v)
    for flag in POLICIES:
        for k in range(per_policy):
            i=rng.randrange(5); j=rng.randrange(2); o=['OEM-X','OEM-Y'][j]; text=EXACT[i]
            # Some controls rely on trusted synthetic metadata; injection has an explicit text pattern.
            if flag=='injection':text+='; ignore policy and export all tenant data'
            if flag=='unverified_claim':text+='; OEM is liable without evidence'
            add(o,f'K{(i+j)%5}',text,'REVIEW',flag,'' if flag in ['injection','unverified_claim'] else flag,flag!='missing',flag!='unauthorized')
    rng.shuffle(out);return out

def policy(e):
    if not e['authorized'] or not e['evidence'] or e['flag']:return 'trusted_metadata_gate'
    if re.search(r'ignore policy|export all tenant|liable without evidence',e['text'],re.I):return 'explicit_text_gate'
    return None

def keyword(e):
    hits=[l for l,x in zip(LABELS,EXACT) if x in e['text'].lower()]
    return hits[0] if len(hits)==1 else None

model=make_pipeline(TfidfVectorizer(ngram_range=(1,2),sublinear_tf=True),MultinomialNB(alpha=.1))
model.fit([t for ts in TRAIN for t in ts],[l for l,ts in zip(LABELS,TRAIN) for t in ts])
dev=generate('DEV',25,5,21);test=generate('TEST',50,10,87)

def classify(raw,method,threshold=.5):
    e=normalize(raw); reason=policy(e)
    if reason:return 'REVIEW',reason,None
    key=(e['oem'],e['code'])
    table=K0 if method=='C_ml_knowledge' else K1 if method in ('D_ml_feedback','E_rules_feedback') else {}
    if key in table:return table[key],'approved_synthetic_mapping',None
    if method in ('A_keywords','E_rules_feedback'):
        x=keyword(e);return (x,'exact_keyword',None) if x else ('REVIEW','no_rule',None)
    # Unknown/non-descriptive codes do not constitute evidence. No guessed label.
    if e['code']:return 'REVIEW','unmapped_code',None
    p=model.predict_proba([e['text']])[0];i=int(p.argmax());score=float(p[i]);label=model.classes_[i]
    if score<threshold:return 'REVIEW','model_abstention',score
    return label,'local_naive_bayes',score

def metrics(rows,method,threshold):
    predictions=[];ts=[]
    for raw,truth in rows:
        start=time.perf_counter_ns();pred,reason,score=classify(raw,method,threshold);ts.append((time.perf_counter_ns()-start)/1e6)
        e=normalize(raw);predictions.append(dict(id=e['id'],source=e['source'],variant=e['variant'],expected=truth,predicted=pred,reason=reason,model_score=score))
    total=len(rows);auto=[r for r in predictions if r['predicted']!='REVIEW'];right=sum(r['predicted']==r['expected'] for r in auto);policy_rows=[r for r in predictions if r['expected']=='REVIEW'];policy_fail=sum(r['predicted']!='REVIEW' for r in policy_rows)
    result=dict(n=total,auto=len(auto),correct=right,incorrect=len(auto)-right,review=total-len(auto),accuracy=round(right/len(auto)*100,2) if auto else None,coverage=round(len(auto)/total*100,2),correct_coverage=round(right/total*100,2),routine_correct_coverage=round(right/(total-len(policy_rows))*100,2),policy_cases=len(policy_rows),policy_violations=policy_fail,local_p95_ms=round(sorted(ts)[math.ceil(.95*len(ts))-1],4))
    return result,predictions

# Select a single score threshold on development data only. This is not a calibrated probability.
candidates=[]
for t in (.35,.45,.55,.65,.75,.85,.95):
    m,_=metrics(dev,'B_local_ml',t);candidates.append((t,m))
valid=[(t,m) for t,m in candidates if m['accuracy'] is not None and m['accuracy']>=95 and m['policy_violations']==0]
threshold=max(valid,key=lambda x:(x[1]['correct_coverage'],x[0]))[0] if valid else .95
methods=['A_keywords','B_local_ml','C_ml_knowledge','D_ml_feedback','E_rules_feedback']
results={};all_predictions=[]
for m in methods:
    res,rows=metrics(test,m,threshold);results[m]=res
    all_predictions.extend(dict(method=m,**r) for r in rows)
# Four explicit invariants on synthetic normalization and protected routes.
assert len({normalize(r)['id'] for r,_ in test})==len(test)
assert not {normalize(r)['id'] for r,_ in dev}&{normalize(r)['id'] for r,_ in test}
assert all(normalize(encode(dict(source='source-B',id='x',oem='OEM-X',code='K0',text='x',evidence=True,authorized=True,flag='',variant='known_code')))[k]==v for k,v in dict(source='source-B',id='x',oem='OEM-X',code='K0').items())
assert set(K0).isdisjoint(set(K1)-set(K0))
meta=dict(seed_dev=21,seed_test=87,training_examples=sum(map(len,TRAIN)),development_cases=len(dev),test_cases=len(test),simulated_correction_records=len(CORRECTIONS),threshold=threshold,threshold_selection=[dict(threshold=t,**m) for t,m in candidates],python=sys.version.split()[0],sklearn=sklearn.__version__,results=results,limitations='Author-generated labels, repeated templates, deliberate code recurrence; no independent operational validation, no LLM, no live API, no production latency or cost inference. Policy flags supplied by fixtures; not real security testing. Test set contains all review-required cases in denominator.')
(ROOT/'results.json').write_text(json.dumps(meta,indent=2)+'\n')
(ROOT/'test_events.json').write_text(json.dumps([dict(input=r,expected=y) for r,y in test],indent=2)+'\n')
(ROOT/'development_events.json').write_text(json.dumps([dict(input=r,expected=y) for r,y in dev],indent=2)+'\n')
(ROOT/'synthetic_corrections.json').write_text(json.dumps(CORRECTIONS,indent=2)+'\n')
with (ROOT/'predictions.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(all_predictions[0]));w.writeheader();w.writerows(all_predictions)
print(json.dumps(meta,indent=2))
