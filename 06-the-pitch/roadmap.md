# Three-Horizon Roadmap & Board Pitch

**Version 4 update:** The Roadmap section contains the current Roadmap Builder output. Earlier course-format drafts and V3 assessment are retained for iteration history. The final V4 section and root [README](../README.md) supersede earlier status, cost sensitivities and assessment where they differ.


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

**Version 4 — Roadmap Builder output:** This is the current 16-initiative roadmap. All initiatives are proposed; the anonymized backlog is not a company Jira export. Start relative to funding approval. Review monthly. No new operational validation results are claimed. Earlier V3 tables below are retained for iteration history, not as the active roadmap.

### Horizon 1 – Ship (0–4 weeks)

*Objective: Establish the evidence required for an informed investment decision.*

| Initiative | Strategy Component | Why it ships now | Confidence |
|---|---|---|---|
| 01 – Validate user needs and workload | Bet | Establish the operational baseline through 6–10 TAM interviews, two leads and 8–10 representative parks. | H |
| 02 – Compare native and specialist alternatives | Moat | Identify existing alternatives before committing to proprietary development. | H |
| 03 – Read-only data integration feasibility | Bet | Confirm authorized data access, event normalization and adapter feasibility. | H |
| 04 – Validate ramp-aware business case | Margin | Establish full costs, economic realization and comparative investment returns. | H |
| 05 – Define independent evaluation and release gates | Contract | Establish expert-labeled test data, quality metrics and mandatory acceptance criteria. | H |
| 06 – Confirm governance owners and data rights | Guardrails | Establish accountability, permissions, security requirements and validate shadow AI hypotheses. | H |

**Week 4 decision gate:** Proceed only if a material unmet user need, authorized data access, technical feasibility, sufficient resources and credible economics can be established. Select the most economically viable compliant approach. Stop if feasibility cannot be established; buy rather than build if a compliant native alternative wins.

The proposed discovery investment is capped at 10 person-days. High confidence refers to the importance of these discovery deliverables, not certainty of favorable results or guaranteed completion within that capacity.

### Horizon 2 – Validate (1–3 months)

*Objective: Prove technical reliability, incremental differentiation and economic viability through a controlled pilot.*

| Initiative | Strategy Component | Hypothesis | Kill Criteria | Confidence |
|---|---|---|---|---|
| 07 – Benchmark and shadow-mode pilot | Bet | The selected automation approach materially reduces repetitive operational work. | By week 12, stop or pivot if correct automation of all in-scope events is below 70% or end-to-end effort reduction is below 50%. | M |
| 08 – Reliability and human review evaluation | Contract | Risk-based automation can deliver reliable classifications without compromising critical decisions. | By week 12, block automated write-back if auto-applied accuracy is below 95%, critical violations remain unresolved or mandatory release controls fail. | M |
| 09 – Test incremental knowledge and correction reuse | Moat | Reusable operational knowledge creates measurable value over the best feasible alternative. | By week 12, stop custom learning if neither a 5 pp increase in correct automation coverage at target accuracy nor a 10% reduction in review effort at non-inferior quality is achieved. | M |
| 10 – Optimize full cost and adoption economics | Margin | The selected solution generates sufficient economic value after accounting for implementation, operating costs and adoption ramp-up. | By week 12, stop scaling if Finance-reviewed, ramp-adjusted payback exceeds 12 months. | M |
| 11 – Verify portability, security and fallback | Guardrails | The selected solution can operate without unacceptable vendor dependency or operational risk. | By week 12, block scaling if the required 48-hour provider replacement, operational fallback, critical controls or approvals cannot be demonstrated. | M |

**Week 12 decision gate:** Scale, simplify, buy, pivot or stop based on measured pilot results. No production rollout is approved by default.

### Horizon 3 – Explore (3–6 months)

*Objective: Explore additional value from the proven workflow and reusable operational knowledge.*

| Initiative | Strategy Component | What must be true first | Confidence |
|---|---|---|---|
| 12 – Expand across additional OEMs and sources | Moat | H2 gates are passed and knowledge can be reused across authorized sources without compromising quality. | L |
| 13 – Explore OEM report reconciliation | Moat | The knowledge layer is validated; a separate experiment targets at least 20% reconciliation effort reduction at non-inferior quality. Separate business case; avoid double counting. | L |
| 14 – Conditional phased rollout | Margin | All technical, economic, adoption and governance gates are passed. Rollout investment requires separate approval. | L |
| 15 – Explore operational analytics | Moat | A specific unmet analytical need and measurable incremental value are identified. Remove from active funding scope until then. | L |
| 16 – Explore external demand and pricing | Margin | Internal value is demonstrated, willingness to pay is validated, review responsibilities are established and full contribution margin reaches at least 40%. | L |

H3 is an exploration and conditional rollout-planning horizon, not a commitment to implement all five initiatives.

### Unmapped (cut or rethink)

| Initiative | Why it's unmapped | Recommendation |
|---|---|---|
| None | All 16 initiatives have a defensible link to a strategy component. | Defer vague operational analytics until a specific outcome and hypothesis exist. |

### Mapping Disagreements

No explicit user-locked mappings were supplied. The following change is recommended relative to the imported CSV component labels:

| Initiative | Imported component | Recommended component | Why |
|---|---|---|---|
| 13 – Explore OEM report reconciliation | Guardrails | Moat | Its primary purpose is to validate cross-workflow knowledge reuse as a source of differentiation, while governance remains a prerequisite. |

The automatic unmapped classification of initiative 12 is corrected to Moat. Other mappings follow the imported component labels rather than the tool's automatic keyword guesses.

**Roadmap critique:** H1 has the most initiatives (6 of 16), intentionally emphasizing discovery; H2 still needs independently validated evidence and H3 needs separate use-case business cases. Protect OEM report reconciliation as the H3 experiment that most directly tests cross-workflow knowledge reuse. Cut generic operational analytics from the active backlog today and reconsider only once a specific unmet need and measurable outcome are identified.

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

