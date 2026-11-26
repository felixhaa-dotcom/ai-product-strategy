# AI Product Roadmap – Version 4

**AI-Powered Wind Asset Operations Intelligence**

All initiatives are proposed. This anonymized planning backlog is not an actual company Jira export. No new operational validation results are claimed.

## Horizon 1 – Ship (0–4 weeks)

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

## Horizon 2 – Validate (1–3 months)

*Objective: Prove technical reliability, incremental differentiation and economic viability through a controlled pilot.*

| Initiative | Strategy Component | Hypothesis | Kill Criteria | Confidence |
|---|---|---|---|---|
| 07 – Benchmark and shadow-mode pilot | Bet | The selected automation approach materially reduces repetitive operational work. | By week 12, stop or pivot if correct automation of all in-scope events is below 70% or end-to-end effort reduction is below 50%. | M |
| 08 – Reliability and human review evaluation | Contract | Risk-based automation can deliver reliable classifications without compromising critical decisions. | By week 12, block automated write-back if auto-applied accuracy is below 95%, critical violations remain unresolved or mandatory release controls fail. | M |
| 09 – Test incremental knowledge and correction reuse | Moat | Reusable operational knowledge creates measurable value over the best feasible alternative. | By week 12, stop custom learning if neither a 5 pp increase in correct automation coverage at target accuracy nor a 10% reduction in review effort at non-inferior quality is achieved. | M |
| 10 – Optimize full cost and adoption economics | Margin | The selected solution generates sufficient economic value after accounting for implementation, operating costs and adoption ramp-up. | By week 12, stop scaling if Finance-reviewed, ramp-adjusted payback exceeds 12 months. | M |
| 11 – Verify portability, security and fallback | Guardrails | The selected solution can operate without unacceptable vendor dependency or operational risk. | By week 12, block scaling if the required 48-hour provider replacement, operational fallback, critical controls or approvals cannot be demonstrated. | M |

**Week 12 decision gate:** Scale, simplify, buy, pivot or stop based on measured pilot results. No production rollout is approved by default.

## Horizon 3 – Explore (3–6 months)

*Objective: Explore additional value from the proven workflow and reusable operational knowledge.*

| Initiative | Strategy Component | What must be true first | Confidence |
|---|---|---|---|
| 12 – Expand across additional OEMs and sources | Moat | H2 gates are passed and knowledge can be reused across authorized sources without compromising quality. | L |
| 13 – Explore OEM report reconciliation | Moat | The knowledge layer is validated; a separate experiment targets at least 20% reconciliation effort reduction at non-inferior quality. Separate business case; avoid double counting. | L |
| 14 – Conditional phased rollout | Margin | All technical, economic, adoption and governance gates are passed. Rollout investment requires separate approval. | L |
| 15 – Explore operational analytics | Moat | A specific unmet analytical need and measurable incremental value are identified. Remove from active funding scope until then. | L |
| 16 – Explore external demand and pricing | Margin | Internal value is demonstrated, willingness to pay is validated, review responsibilities are established and full contribution margin reaches at least 40%. | L |

H3 is an exploration and conditional rollout-planning horizon, not a commitment to implement all five initiatives.

## Unmapped (cut or rethink)

| Initiative | Why it's unmapped | Recommendation |
|---|---|---|
| None | All 16 initiatives have a defensible link to a strategy component. | Defer vague operational analytics until a specific outcome and hypothesis exist. |

## Mapping Disagreements

No explicit user-locked mappings were supplied. The following change is recommended relative to the imported CSV component labels:

| Initiative | Imported component | Recommended component | Why |
|---|---|---|---|
| 13 – Explore OEM report reconciliation | Guardrails | Moat | Its primary purpose is to validate cross-workflow knowledge reuse as a source of differentiation, while governance remains a prerequisite. |

The automatic unmapped classification of initiative 12 is corrected to Moat. Other mappings follow the imported component labels rather than the tool's automatic keyword guesses.

**Roadmap critique:** H1 has the most initiatives (6 of 16), intentionally emphasizing discovery; H2 still needs independently validated evidence and H3 needs separate use-case business cases. Protect OEM report reconciliation as the H3 experiment that most directly tests cross-workflow knowledge reuse. Cut generic operational analytics from the active backlog today and reconsider only once a specific unmet need and measurable outcome are identified.
