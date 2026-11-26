# V4 self-evaluation — eight course dimensions

Rubric 1–5. Design score measures quality of the strategy, not implementation maturity or an official Product School assessment. Evidence-weighted score discounts unresolved operational and commercial evidence. Both are author judgments, not an independent evaluator.

| Dimension | V3 design | V4 design | Evidence-weighted V4 | Strength / limitation / recommendation |
|---|---:|---:|---:|---|
| Bet validation | 3 | 4 | 3 | Public industry evidence plus falsifiable scoped experiment; no actual TAM interviews. Measure end-to-end workload and buyer demand in H1. |
| Capability | 3 | 4 | 4 | Executable local ML, two mock adapters, actual predictions and JS parity; no live integration, LLM or staffing validation. Secure read-only test access and scope production. |
| Impact | 3 | 4 | 3 | Ramp-aware alternative economics expose a failed investment gate; no measured workload or realized benefit. Finance to validate incremental benefits and adoption. |
| Defensibility | 3 | 4 | 3 | Named public alternatives and controlled knowledge/rules ablation; no independent operational moat or vendor performance. Benchmark against native and unseen OEMs. |
| Pricing | 3 | 4 | 3 | Variable cost and reviewer responsibility stress tests; no paid WTP or actual costs. Obtain quotes and price reactions before commercialization. |
| Trust/reliability | 4 | 4 | 4 | Actual controlled routing and ML outputs plus explicit failed coverage gate; draft golden specs and safety controls not production-tested. Independent expert holdout and calibrated thresholds. |
| Governance/scale | 4 | 4 | 4 | Specific approvals, rollback, access and fallback requirements; real ownership, shadow audit and 10× drill pending. Assign owners and verify controls. |
| Gap identification | 4 | 5 | 5 | Documents failed gates, stronger controls, alternatives, assumptions and accountable decisions, without hiding adverse results. Close priority gaps, not just scoring. |
| Total | 27/40 (3.375) | 33/40 (4.125) | 29/40 (3.625) | Design target met provisionally; production readiness not demonstrated. |

**Overall design score:** 4.125/5 (4.13 rounded). **Evidence-weighted score:** 3.625/5 (3.63 rounded). Design 4 means a specific, testable plan and explicit decisions, not proven outcomes; gap 5 is a subjective design assessment. Independent reviewers may score lower.

**Biggest risk:** Native or simpler rules/knowledge solution meets need at lower full cost, while custom approach fails coverage and ramp-aware economic gates.

**Top 3 actions:** (1) authorized TAM interviews, time-and-motion baseline and demand; (2) compare actual native/rules/ML on expert-labeled events, including unseen codes and all mandatory reviews; (3) validate incremental ramp-aware economics, governance and release readiness.

## Evidence register
| Item | Status | Evidence / next action |
|---|---|---|
| Market category and substitutes | Public desk research | [Named public alternatives and research](../02-the-moat/public-market-evidence.md); no actual supplier claim. |
| Local supervised ML and normalization | Executed synthetic | [Code, input, actual results and predictions](../01-the-bet/benchmark/README.md); two mock sources, no API. |
| Feedback reuse | Executed synthetic | 10 simulated correction records; repeated code reuse; no actual experts or independent generalization. |
| Mandatory review | Executed routing fixtures | 80/80 routed; no production security proof. |
| Coverage | Failed in synthetic test | 60.61% vs 70%; investigate missing evidence and unmapped codes, do not relax controls. |
| 12-month investment | Failed illustrative ramp scenario | ~15.8 months at 25% realization; no actual cost or demand. |
| User evidence / shadow AI | Pending | 6–10 TAM, 2 leads, five walkthroughs; actual observations required. |
| Data rights / live source access / release | Pending | Obtain approval; test on representative permitted holdout and real fallback. |
| Commercial willingness to pay | Pending | Price reactions and paid pilot intent; no actual sales. |
