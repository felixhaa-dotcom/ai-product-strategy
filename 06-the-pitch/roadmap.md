# Three-Horizon Roadmap & Board Pitch

**Version 4 update:** The original course-format working draft is preserved below for iteration history. The final V4 section and root [README](../README.md) supersede earlier status, cost sensitivities and assessment where they differ.


**Confidentiality and evidence:** Employer, actual suppliers, locations and internal names are withheld. All financial, portfolio and staffing figures are synthetic scenario assumptions. All proposed controls, metrics, competitor profiles and architecture are unverified unless explicitly stated. No operational data is included.


**Disclosure:** All portfolio, workload, cost, budget and staffing figures are synthetic illustrations, not actual company data or approved commitments.

## AI Evaluation
| Dimension | Assessment | Required evidence |
|---|---|---|
| Bet Validation | Plausible; synthetic planning estimates, not measured pilot | Time-and-motion baseline, representative pilot |
| Defensibility | Weak platform exposure (2/5) | Native feature fit/TCO, verified feedback reuse |
| Pricing Alignment | Internal value case preferable; external pricing hypothetical | Actual costs, marginal cost/realization, demand |
| Trust & Reliability | Defined targets, no execution evidence | Expert labels, holdout and shadow-mode results |
| Impact & Scale | Compounding not yet proven | Multi-OEM cohort, authorized reuse, unit-cost trends |
| Capability Gaps | Provider, APIs, owner and capacity unconfirmed | Technical scoping, approved providers, work allocation |

**Weakest claim revised:** Rather than committing to a proprietary AI product, fund a bounded validation of the best way to automate the workflow; buy native functionality if it meets requirements at lower risk-adjusted TCO. Never present capacity release as realized cash savings.

## Roadmap
Proposed backlog derived from M1–M5, not a Jira export. Start relative to funding approval. Review monthly.

### Horizon 1 — Now (0–4 weeks)
| Initiative | Component | Deliverable |
|---|---|---|
| Baseline and pilot cohort | Bet | Measured effort and event mix for 8–10 representative wind parks (proposed), at least two OEMs if feasible |
| Native feature and build/buy comparison | Moat | Feature fit and total cost comparison |
| Read-only workflow demo and API feasibility | Bet | Synthetic demo and approved test access |
| Define unit cost, full cost and realization | Margin | Finance-reviewed cost model |
| Curate initial gold cases and release gates | Contract | Expert-approved starter set, expansion plan |
| Data rights, owner, escalation and security approval | Guardrails | Documented scope and gate |

**Week-4 gate:** Stop or buy instead if native functionality meets quality, governance and lower risk-adjusted TCO; stop if data access, pilot staffing or approval cannot be secured. Release H2 only with credible economics and feasible design.

### Horizon 2 — Next (1–3 months)
| Initiative | Component | Hypothesis | Kill criteria (week 12 unless noted) |
|---|---|---|---|
| Shadow-mode event classification and comments | Bet | >=70% correct automation of all in-scope events and >=50% effort reduction | Stop/pivot if either threshold missed |
| Golden dataset, confidence calibration and HITL | Contract | >=95% accuracy on auto-eligible cases; no unresolved critical defects | No automated write-back if below target or any unresolved critical defect |
| Model routing and fallback | Margin | Full delivery cost supports payback <=12 months at Finance-approved realization assumptions | Stop scaling if economics fail |
| Correction capture and knowledge reuse | Moat | Feedback measurably improves held-out quality or correct coverage | Stop expansion of learning mechanism if no improvement in prespecified comparison |
| Provider swap and controls | Guardrails | Approved fallback or manual process; demonstrate switch <=48h before scale | Block scale if fallback/control readiness unproven |

### Horizon 3 — Bet (3–6 months)
| Initiative | Component | Experiment / prerequisite |
|---|---|---|
| Transfer to other OEMs/countries | Moat | Only after H2 gate; test local taxonomies and data rights |
| Reuse validated events in OEM reconciliation | Guardrails | Test incremental value separately; avoid double counting |
| Scale to a representative 100-park scenario | Margin | Conditional phased rollout after quality, adoption and Finance approval |
| External commercialization | Margin | Small discovery study only if internal fit proven |

### Unmapped / Deferred
Generic AI chatbot, general presentation/email tools, autonomous turbine control and autonomous trading are outside this product scope. No actual user-mapped backlog supplied; mapping disagreements not assessable.

## Board Pitch
**Thesis (1 sentence):**
Grow operational capacity through a reusable, governed knowledge workflow, starting with a bounded status categorization pilot; invest in shared intelligence only where it beats the best native or rules-based alternative.

**The case:**
**Why now:** The process is repetitive, a candidate for operational process improvement, and can be evaluated against existing manual work and operational data.
**What's defensible:** Approved operational knowledge, contractual rules, validated corrections and cross-platform workflows; not the model itself. Native functionality may be the right solution if better TCO.
**The economics:** Synthetic scenario (not company data): 100 illustrative wind parks, 2.0h to 0.5h per park/month; 1,800 hours/year capacity potential, €180,000 gross equivalent at €100/h. At 25% realization and illustrative €10,000/year OPEX, €35,000 annual net economic benefit. €32,000 proposed cap implies ~11.0 months simple steady-state payback. Not a cash-savings commitment; excludes ramp-up, discounting and unverified costs.

**The risks:**
**Trust:** Shadow mode first; >=95% auto accuracy, >=70% correctly automated outcomes, mandatory human review for critical cases, protected evaluation dataset and traceability.
**Scale:** Data rights, ownership, model portability, authorized feedback loop and operations readiness are release gates.
**Competitive:** Compare Vendor A/other native offerings before custom build; preserve knowledge and avoid duplicated investment.

**The ask:**
Audience: Renewable asset management leadership / internal funding review. Proposed 12-week validation with 40 person-days across existing teams (22 engineering, 8 TAM, 6 product, 4 security/QA; proposed not committed). Cap €32,000 at €100/hour and 8-hour day, subject to scoping. Release only 10 days (€8,000) for H1; conditional 30 days (€24,000) for H2 after week-4 gate. No production rollout or incremental hiring authorized by this ask. Incremental vendor/OPEX funding must be explicitly scoped before H2; stop or revise if total economics do not support the gate.

**Week-12 decision:** Scale only if success gates, governance approval and Finance-validated <=12-month payback are met; otherwise buy, narrow, pivot or stop.

### Coaching Notes
Opening: Our asset managers should spend less time categorizing routine events and more time improving asset performance.
60-second version: A limited pilot tests a real efficiency opportunity on 8–10 parks. We estimate up to 1,800 hours of annual capacity release in the illustrative portfolio under synthetic scenario assumptions, not booked savings. Approve €8,000 of initial effort, with further funding conditional on feasibility, alternatives and economics; quality and savings gates control rollout.
Hardest question: Why build if Vendor A already offers this? Answer: We don't commit to build. Compare native functionality first and choose the lowest risk-adjusted cost route that retains needed control and meets quality requirements.

## M1 Baseline vs. Now
**M1 baseline:** Build an AI status categorization tool for repetitive asset management work.

**Now:** Validate a provider-independent knowledge workflow, starting with categorization. Build only gaps where measured economics and reliability justify custom investment; prove reuse before extending to OEM reconciliation or analytics.

## V3 revised roadmap: dependency and decision gates
| Horizon | Priority / owner (role) | Deliverable and gate |
|---|---|---|
| H1: weeks 1–4 | Product + TAM | User evidence and time study, scoped event sample, strongest native/rules baseline; 5 usability tests. No build if native meets requirements more cheaply. |
| H1 | Data/architecture + security | Rights approval, canonical event schema, read-only adapter spike, risk/TCO comparison; <=10 days initial discovery budget. |
| H1 | Finance + product sponsor | Updated cash/economic-value ramp, pilot staffing, documented funding decision. If credible economics or data unavailable, stop. |
| H2: weeks 5–12 | Engineering + TAM + QA | Shadow pilot of best feasible path; >=95% auto accuracy, >=70% correct coverage, >=50% effort reduction; full review/rework measured; no critical violations. |
| H2 | Product + engineering | Correction reuse experiment: >=5pp lift in correct coverage at target accuracy OR >=10% less review time without quality degradation. If no lift, simplify to rules/native and stop custom learning. |
| H2 | Security + operations + Finance | Fallback drill, signed release gates, full delivery costs and ramp-aware <=12-month payback from approved rollout investment; otherwise narrow/pivot/buy/stop. |
| H3: months 3–6 | Sponsor + operations | Phased expansion only after H2; reuse experiment in OEM reconciliation >=20% effort reduction with non-inferior quality; no automatic approval of broad platform investment. |
| H3 | Product | Explore operational analytics only if reusable context produces additional value; commercialization discovery only, no revenue assumed. |

**Scope discipline:** First release remains classification/comments. Do not build a generic data lake, new monitoring platform, general agent framework, cross-tenant training or commercial product in the initial 40-day envelope. H2 scope and external costs must be re-estimated after H1. The 40 days are a planning cap for validation, not a production estimate. The demo and second source are synthetic. Owner roles need confirmation.

## AI Bet Evaluator: iteration record
First evaluation (V2, 8 lenses, assistant assessment, not course grade): 22/40 = 2.75/5. Biggest risk: duplicated incumbent functionality without incremental economic value. Revised strategy changes the unit of differentiation from a single feature to an independently governed knowledge workflow, retains build/buy discipline and adds concrete validation, architecture, reliability and governance gates.

| Lens | V2 | V3 provisional design | What improved | Evidence needed for 4/5 |
|---|---:|---:|---|---|
| Bet Validation | 3 | 3 | Defined users, tests and decision thresholds | Real interviews, representative time study, workflow demand |
| Capability Assessment | 2 | 3 | Canonical schema, adapter, gateway, release and fallback design | Approved sample, integration spike and committed resources |
| Impact Analysis | 3 | 3 | Alternatives, ramp-aware payback and sensitivities | Finance-reviewed baseline, real effort savings and costs |
| Defensibility Check | 2 | 3 | Cross-source knowledge and measurable reuse experiment | Native comparison and measured holdout lift |
| Pricing Alignment | 3 | 3 | Clear internal model; 10x sensitivity and full-cost scope | Observed cost-to-serve; willingness-to-pay for external option |
| Trust & Reliability | 3 | 4 | 20 designed cases, explicit metrics, sample sizing, fallback and release | Executed, expert-adjudicated evaluation and operational tests |
| Governance & Scale | 3 | 4 | Accountable roles, versioning, tenancy, scaling and shadow AI plan | Confirmed owners, approval, observed shadow AI and scale drill |
| Gap Identification | 3 | 4 | Named evidence gates and decisions for failed hypotheses | Closed priority gaps and revised evidence register |
| Total | 22/40 | 27/40 | 2.75 → 3.375/5 | 32/40 is a target, not a result |

Scoring reflects strategy design only; no new empirical evidence has been gathered. Higher scores for trust/governance/gap identification reflect specificity of the proposed controls, not achieved reliability or compliance. Biggest remaining risk: the knowledge layer adds complexity without incremental value vs native/rules-only alternatives. Three actions: (1) baseline and native benchmark; (2) secure data rights and run architecture spike; (3) shadow pilot and controlled correction-reuse test. Do not represent the evaluation as an official Product School score.


## V4 evidence-led decision (supersedes prior V3 assessment)
Offline synthetic ML experiment now executed: D 60.61% correct coverage vs B 30.30% and E rules with same knowledge 45.45%; misses 70% gate. Public market evidence confirms alternatives; no vendor tested or quote received. Ramp-aware synthetic economics fail 12-month gate at 25% realization. Therefore approve discovery only, not a full build: verify native/knowledge-enabled rules on the same independent sample, obtain approved data and staffing, validate user pain and Finance economics. If native wins, buy; if recurring knowledge adds insufficient value, simplify. Do not remove difficult events to meet coverage.

| Horizon | Owner role (proposed) | Next decision |
|---|---|---|
| H1, weeks 1–4 | Product / TAM / data / Finance | Confirm workload, at least one material unmet need, data rights, buyer/owner, native fit and full TCO. If no incremental value or access, stop/buy. |
| H2, weeks 5–12 | Engineering / QA / operations / security | Independent expert-labeled benchmark, compare strongest native/rules/ML, ≥95% auto accuracy, ≥70% correct coverage, ≥50% effort reduction, no critical violations; verify incremental knowledge benefit and full ramp-aware payback ≤12 months. If missed, pivot/narrow/buy/stop. |
| H3, months 3–6 | Sponsor | Roll out only proven route; test cross-workflow benefit separately. No production or commercialization authorization today. |

[Evaluation and evidence register](evaluation-v4.md) · [Market](../02-the-moat/public-market-evidence.md) · [Economics](../03-the-margin/v4-economics.md) · [Benchmark](../01-the-bet/benchmark/README.md).

