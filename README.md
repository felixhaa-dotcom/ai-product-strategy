# AI-Powered Wind Asset Operations Intelligence — V4

> Automate repeatable wind asset operations through a governed, reusable knowledge workflow. Prove status categorization first; use native capabilities when they meet requirements more economically.

**Confidentiality and evidence:** Employer, actual suppliers, locations and internal names are withheld. All financial, portfolio and staffing figures are synthetic scenario assumptions. Public market examples are independently selected and imply no supplier relationships. Executed test results are from synthetic local ML only; all financial, production and demand assumptions remain unvalidated. No operational data is included.

## Strategy at a Glance
| Component | Module | Status | Key Artifact |
|---|---|---|---|
| The Bet | M1 | [x] Draft | [01-the-bet](01-the-bet/) |
| The Moat | M2 | [x] Draft | [02-the-moat](02-the-moat/) |
| The Margin | M3 | [x] Draft | [03-the-margin](03-the-margin/) |
| The Contract | M4 | [x] Draft | [04-the-contract](04-the-contract/) |
| The Guardrails | M5 | [x] Draft | [05-the-guardrails](05-the-guardrails/) |
| The Pitch | M6 | [x] Draft | [06-the-pitch](06-the-pitch/) |

All six components are documented; none has been validated in production. V3 supersedes the feature-only framing.

## The Bet (M1)
- **Product:** AI-Powered Wind Asset Operations Intelligence. First use case: wind turbine event status categorization and comments for TAM; choose the simplest compliant route, not a predetermined custom AI platform.
- **AI Value Archetype:** Automator, with Copilot support for exceptions. No autonomous agents in v1.
- **Vulnerability Scores:** Contextual Moat 3/5 · Data Advantage 3/5 · Platform Exposure 2/5; composite 8/15 (provisional; 5 = strongest). Design target 11/15 conditional on evidence.
- **Top Risk:** Native or knowledge-enabled rules may solve the problem at lower risk-adjusted TCO; custom development currently misses synthetic coverage and illustrative ramp-aware payback gates.
- **Confidence:** M — subjective; interviews, benchmark, data rights, API feasibility and pilot pending.
- **Prototype:** [Functional offline ML classifier](01-the-bet/prototype-demo.html), trained local TF-IDF/naive Bayes, two mock source formats, fictional knowledge and simulated corrections. [Executed 330-case benchmark](01-the-bet/benchmark/README.md), 1,650 method/case predictions. No live LLM or API, no production or hosted URL. Headless UI smoke test passed; JS/Python 1,650 prediction/route comparisons matched.
- **Kill Criteria:** Week 4: stop if approved data access, feasible scope or credible economics cannot be established; buy if native meets requirements at lower risk-adjusted TCO. Week 12: stop/pivot if accuracy on automatically applied cases <95%, correct automation <70% of all in-scope events or end-to-end effort reduction <50%. No rollout with unresolved critical risks. Stop custom learning if no measured incremental lift.
- **Discovery:** Proposed 6–10 TAM interviews, two leads, 8–10 representative parks, 100 authorized historical events if feasible, five usability walkthroughs. No results claimed.

[Diagnostic](01-the-bet/diagnostic.md) · [Prototype bet](01-the-bet/prototype.md)

## The Moat (M2)
- **Data Flywheel Score:** 4/20 conservative unverified baseline; 17/20 target (Corrections 5, Preferences 3, Domain Context 5, Network 4).
- **Weakest Loop:** All four provisionally 1/5; prioritize expert corrections with independent holdout testing.
- **Top Encroachment Threat:** Public benchmark: Algorithm Energy markets automated loss categorization; Nabla Wind Hub markets shutdown classification; Microsoft Fabric offers multi-source wind integration architecture. [Public sources and fit/TCO test](02-the-moat/public-market-evidence.md). No supplier relationship or actual fit claimed.
- **Encroachment Defense:** Preserve authorized, versioned event mappings, evidence references, OEM context, contractual rules and validated corrections in a reusable knowledge layer. Compare native, specialist, rules-only and hybrid approaches using the same event benchmark.
- **Vendor Portability:** Not assessed. Target approved provider switch within 48 hours; manual fallback from the outset. Exportable schema and versioned model gateway proposed.
- **Proof of moat:** Synthetic experiment: D correct coverage 60.61% vs B ML only 30.30%, C ML+initial knowledge 45.45%, E rules+same knowledge 45.45%. No independent operational moat or cross-workflow evidence. Actual target +5pp coverage at target accuracy OR 10% less review effort at non-inferior quality vs best feasible comparator; simplify if absent.

[Data flywheel](02-the-moat/data-flywheel.md) · [Kill switch](02-the-moat/kill-switch.md)

## The Margin (M3)
- **Gross Margin (current):** N/A — internal manual process without standalone product revenue.
- **Gross Margin (AI-adjusted):** 67.1% hypothetical buyer-operated-review base; 45.8% with 3× inference, 43.1% with 2× fixed usage; 10× fixed −148.9%, 10× hybrid 68.9%, 10× hybrid with 3× inference 42.2%. Vendor-supplied review scenario −44.0%. All synthetic and full costs unknown.
- **Pricing Model:** Internal efficiency first; external hybrid pricing is a separate hypothetical option, not current revenue.
- **Pricing Today → Tomorrow:** No standalone tariff → illustrative €5/turbine/month + €0.25 per successfully automated classification; 70 outcomes = €22.50/month. No approved tariff or willingness-to-pay evidence.
- **Total AI COGS / unit:** €2.40 monthly inference per turbine; €2 fixed + €3 variable other COGS (illustrative buyer-operated review). €7.40 base total modeled COGS. Vendor review may add €25 at 30 cases × 0.5 min × €100/h.
- **Cascading Strategy:** Deterministic rules first; illustrative 80% small/20% frontier routing; human review for critical cases.
- **Net Margin Shift:** N/A — no standalone baseline. Illustrative internal scenario: 100 parks, 2.0 to 0.5 h/park/month, 75% effort reduction, 1,800 hours/year capacity release, €180,000 gross economic equivalent at €100/h. Not cash savings.
- **Break-even at:** 11.0 months steady-state, ~15.8 months with illustrative adoption ramp (25%/50%/100% over months 1–3/4–6/7–12), €32k investment, €10k annual OPEX, 25% realization. Year-one net €20,937.50 before initial investment; €11,062.50 unrecovered. Need ≥33.94% realization for 12-month gate under ramp. Not achieved; full Finance-reviewed actual model required.
- **Investment logic:** Compare compliant native, rules and hybrid using common quality and full ramp-aware cost; illustrative native scenario wins year-one economics, not a verified ranking. [Activity-based model](03-the-margin/v4-economics.md). Commercial option only with validated demand and ≥40% full contribution margin.

[Cost curve](03-the-margin/cost-curve.md)

## The Contract (M4)
- **Reliability Target:** >=95% auto-applied accuracy; >=70% correct automation of all in-scope events; <1% unsupported assertion rate, zero tolerated critical incidents; p95 <=10 seconds; drift <=0.5pp/week; proposed 99.5% availability during agreed service hours. All unmeasured.
- **Golden Dataset:** 20 synthetic qualitative specifications (14 edge, 5 adversarial) remain draft; separate executed benchmark of 330 synthetic held-out instances (250 routine, 80 mandatory review), 165 development cases, 40 training phrases and 10 simulated corrections. Shared generator, no independent expert validation.
- **Confidence UX:** Tiered calibrated confidence with evidence; auto-apply only routine cases >=95% and all controls; uncertain or critical cases go to review; withhold unsupported decisions.
- **HITL Architecture:** TAM reviewer, specialist for critical/ambiguous decisions, product/engineering/security for systemic incidents. Capture authorized corrections, evidence and versions. No unapproved learning.
- **Failure Mode Coverage:** 80/80 mandatory-review fixtures routed across all methods; explicit metadata/literal checks, not real security tests. Best correct coverage 200/330 = 60.61%, below 70% gate; synthetic auto accuracy 100% not production proof. Independently labeled holdout, statistical acceptance and calibrated confidence required.

[Golden dataset and reliability contract](04-the-contract/golden-dataset.md)

## The Guardrails (M5)
- **Compounding System:** Recurring synthetic code reuse demonstrated in controlled local experiment; real expert feedback, cross-workflow transfer and fleet insights unverified. Cross-workflow target ≥20% reconciliation effort reduction at non-inferior quality with separate business case.
- **Governance Posture:** Proposed accountable product, TAM, engineering/QA, data, security, operations and Finance roles. Versioned knowledge, provenance, tenant isolation, rights/retention, review and release records. Maturity 15/25 provisional; 24/25 target.
- **Autonomy Boundaries:** Authorized read/draft; validated low-risk write-back only after gates; critical classifications and customer communication require human approval. No autonomous SCADA/OT control, financial or contractual commitments.
- **Escalation Triggers:** Low confidence, evidence gaps, failed policy, critical event, security incident, reliability breach or queue overload.
- **Audit Cadence:** Continuous monitoring; daily queue review; weekly evaluations; monthly quality/cost; quarterly governance/vendor review. Proposed roles not appointed.
- **Shadow AI Audit (user-side):** 10 hypotheses, 0 verified; 5 proposed build, 3 partner, 2 ignore; adjacent spend unknown. Proposed interviews and evidence review in H1.
- **Agent Boundaries:** No autonomous agents in first release. Adapter, canonical schema, rule/retrieval layer, controlled model gateway, validators, review queue, approved write-back.
- **Regulatory Exposure:** Qualified owners to assess intended-purpose AI Act classification, applicable GDPR, critical-infrastructure obligations, ISMS and contractual data rights before production. No definitive legal conclusion.

[Compounding system and governance](05-the-guardrails/compounding-system.md)

## The Pitch (M6)
- **Horizon 1 (Now):** Weeks 1–4. Establish evidence, compare native/rules/hybrid, read-only feasibility and approved data, cost model, initial evaluation, governance and ownership. Week 4 stop/buy/validate gate.
- **Horizon 2 (Next):** Weeks 5–12. Shadow pilot, full cost and effort, calibrated quality, independent holdout, correction-reuse experiment, fallback and release gates. Week 12 scale/narrow/buy/pivot/stop decision.
- **Horizon 3 (Bet):** Months 3–6. Conditional expansion to additional OEMs/sources, test OEM report reconciliation reuse, explore operational analytics; no broad platform or external product approval.
- **Board Narrative:** Grow operational capacity, not repetitive work. Start with a bounded workflow and earn investment in reusable knowledge only through incremental value.
- **Ask:** Approve 10 person-days (€8,000 synthetic) for discovery within proposed 40-day / €32,000 12-week validation cap. Conditional 30 days (€24,000) only after H1 gate. Re-estimate external costs and scope; no rollout or hiring commitment. Owner/resource allocation proposed.
- **Key Strategic Change:** From a single AI feature to a reusable outcome-led knowledge workflow, now benchmarked against stronger rules-only control and public alternatives. Do not fund custom implementation until coverage and ramp-aware economics pass. Provisional design assessment V2 2.75, V3 3.375, V4 4.125/5; conservative evidence-weighted V4 3.625/5. Not official scores. [Evaluation and evidence register](06-the-pitch/evaluation-v4.md).

[Roadmap and evaluation record](06-the-pitch/roadmap.md) · [Board presentation](final-presentation.html)

## Remaining submission gaps
A shareable hosted URL, actual user/peer validation, real vendor benchmark and quotes, verified operating metrics and official course access are pending. Named public competitor examples are unrelated to any disclosed supplier relationship. The Product School parser previously misread numeric fields; use this reviewed README rather than overwriting it with incomplete automated output. All six modules and presentation are included as a draft for course submission after review.
