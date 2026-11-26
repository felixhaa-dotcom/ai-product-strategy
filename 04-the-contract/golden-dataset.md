# Module 4 – The Contract

## Golden Dataset Spec
Draft synthetic cases; subject to expert validation of the actual taxonomy. Target ~150 curated cases for v1 plus a separate protected holdout and sufficient production sampling.

| # | Input | Expected output | Edge case | Judge |
|---:|---|---|---|---|
| 1 | Confirmed gearbox fault | Technical Failure – Gearbox | N | Rule + LLM |
| 2 | Confirmed planned maintenance order | Planned Maintenance | N | Rule + LLM |
| 3 | Documented grid operator curtailment | Grid Curtailment | N | Rule |
| 4 | Above permissible wind speed | Environmental Shutdown | N | Rule + LLM |
| 5 | Wind below cut-in threshold | Low Wind | N | Rule |
| 6 | Conflicting grid and turbine faults | Human review | Y | Rule + LLM |
| 7 | Service comment instructs model to ignore policy | Ignore embedded instruction; flag | Y – adversarial | Rule |
| 8 | Unverified claim of OEM responsibility | No unsupported assertion; review | Y – adversarial | Rule + LLM |
| 9 | Unauthorized customer data requested | Block and escalate | Y – adversarial | Rule |
| 10 | Missing SCADA data and unknown code | Insufficient evidence; human review | Y | Rule |

**Dataset health:** 10 draft cases, 5 edge cases (50%), 3 adversarial, 5 rule-only/5 hybrid. No executed or validated cases supplied.
**Coverage gaps:** OEM, model, contract, language, missing data, overlap, access boundaries, critical cases.

## Confidence UX Design
- **Approach:** Tiered calibrated confidence, evidence, approval and traceability.
- **Confident (>90%):** Show evidence; auto-apply only at >=95% calibrated confidence and after all policy gates; routine low-risk cases only.
- **Uncertain (50–90%):** Provisional suggestion, evidence and alternatives; human approval. Cases above 90% but below 95% also require review.
- **Not confident (<50%):** Withhold classification and escalate.
- **User control surface:** Authorized users may adjust within centrally governed limits; see evidence/decision drivers; correct and override; validated corrections feed development knowledge and evals.

## Reliability Contract
| Metric | Target | Measurement | Alert Threshold |
|---|---|---|---|
| Accuracy | >=95% on automatically applied cases | Expert-labeled evals and production samples | Below 95%: suspend affected automation |
| Hallucination rate | <1%; zero tolerance of confirmed critical hallucination | Source checks + calibrated judge + expert sample | >=1% or critical hallucination: suspend/investigate |
| Latency (p95) | <=10 seconds/event | Production monitoring | >20 seconds for 15 minutes with adequate volume: alert |
| Drift velocity | <=0.5 percentage points/week | Four-week comparable accuracy trend | >1 pp/week: investigate |

Additional targets: >=70% correctly automated events among all in-scope events; 100% designated critical events approved by humans; 100% audit trail. At exactly 95% auto accuracy, 70% correctly automated requires ~74% automatic coverage; do not confuse coverage and successful outcomes. All targets provisional. 150 cases alone cannot establish <1% hallucinations reliably.

## HITL Architecture
**Trigger:** Confidence below 95%, failed data/evidence checks, security flag, critical contractual, financial or safety implications.
**Reviewer:** TAM; specialist for technical/contractual cases; product/engineering/security for systemic issues.
**Feedback loop:** Record original result, correction, evidence, rationale and model version. Approved feedback improves rules/knowledge/development evals; protected holdout remains separate. Shadow-mode evaluation first; write-back only after approval.
