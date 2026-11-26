# Data Flywheel Map

**Version 4 update:** The original course-format working draft is preserved below for iteration history. The final V4 section and root [README](../README.md) supersede earlier status, cost sensitivities and assessment where they differ.


**Confidentiality and evidence:** Employer, actual suppliers, locations and internal names are withheld. All financial, portfolio and staffing figures are synthetic scenario assumptions. All proposed controls, metrics, competitor profiles and architecture are unverified unless explicitly stated. No operational data is included.


**Disclosure:** Competitor names are masked for confidentiality. Vendor A/B/C are illustrative competitor profiles; specific named-company evidence is not included in this external version.

## Flywheel Loops
| Loop | Score today | What is captured today | How it compounds (target) | Target |
|---|---:|---|---|---:|
| Corrections | 1 | Not verified | Store approved corrections and reuse as knowledge and eval examples | 5 |
| Preferences | 1 | Not verified | Govern team/contract-specific rules | 3 |
| Domain Context | 1 | Not verified | Transfer validated OEM patterns across comparable assets | 5 |
| Network | 1 | Not verified | Reuse authorized fleet-level insights | 4 |

### Correction Loop - 1/5
**What you capture today:** Not verified.
**How it compounds:** Approved corrections improve knowledge and evaluation coverage. Target 5/5.

### Preference Loop - 1/5
**What you capture today:** Not verified.
**How it compounds:** Governed team and contract rules improve relevance. Target 3/5.

### Domain Context Loop - 1/5
**What you capture today:** Not verified.
**How it compounds:** Reuse validated OEM patterns on comparable assets. Target 5/5.

### Network Loop - 1/5
**What you capture today:** Not verified.
**How it compounds:** Reuse authorized fleet insights. Target 4/5.

**Total Flywheel Score: 4/20**
Current score is a conservative unverified assumption; target 17/20.
**Weakest Loop:** All tied; prioritize Corrections.
**Fix for weakest loop:** Capture evidence, original and corrected category, rationale, reviewer and version; reuse approved feedback and measure lift on a separate holdout.

## Competitive Positioning
M1 starting hypothesis: own workflow depth 3/5 and data advantage 3/5. Target approximately 4.7/5 and 4.6/5 respectively; these are illustrative, not measurements.

## Encroachment Threat Assessment
| Attacker | Vector | Time to threat (hypothesis) | Value at risk (scenario) |
|---|---|---|---|
| Vendor A | Platform encroachment | Now–6 months | 70–90% |
| Vendor B | Vertical competitor | Now–12 months | 40–70% |
| Vendor C | Adjacent expansion | Now–12 months | 50–80% |

### 1. Platform Encroachment
**Attacker:** Vendor A (masked).
**Vector:** Native classification bundled into existing platform.
**Time-to-threat:** Now–6 months (hypothesis).
**% of value at risk:** 70–90% (scenario).

### 2. Vertical Competitor
**Attacker:** Vendor B (masked).
**Vector:** Specialized renewable analytics.
**Time-to-threat:** Now–12 months (hypothesis).
**% of value at risk:** 40–70% (scenario).

### 3. Adjacent Expansion
**Attacker:** Vendor C (masked).
**Vector:** Expansion of outage management.
**Time-to-threat:** Now–12 months (hypothesis).
**% of value at risk:** 50–80% (scenario).

Ranges are stress assumptions, not verified market forecasts. Value means potential internal benefit of own development displaced, not revenue.

## 90-Day Encroachment Plan
**Attacker:** Vendor A (hypothetical; peer review pending).
**Attack vector (target the weakest loop):** Native classifications and correction capture.
**Weeks 1-4 - what they ship:** Classification and comments.
**Weeks 5-8 - how they poach users:** Bundle features into licenses.
**Weeks 9-12 - why users don't come back:** Capture feedback and increase switching costs.
**Your defense:** Maintain authorized operational knowledge, contractual logic and feedback independently of provider; buy commodity functionality when better value.

## V3: defensibility is a testable asset, not a broader feature list
The product is an adapter-based operational workflow with a reusable knowledge layer. Store versioned event mappings, approved rule references, evidence provenance and expert adjudications independently of the model. Use native classifications when adequate. Keep customer-specific knowledge isolated; only share permitted derived knowledge. Portability protects against dependence but is not itself a moat.

| Approach | What it wins on | What could defeat it | Test |
|---|---|---|---|
| Native monitoring features | Existing integration and adoption | Missing cross-source or contractual context | Same labeled event set, full TCO, auditability |
| Specialist solution | Domain models and mature workflows | Integration/rights gaps, duplication | Same benchmark, delivery and exit costs |
| Rules-only internal workflow | Transparency and low model cost | Ambiguous unstructured evidence | Baseline accuracy, coverage, maintenance hours |
| Proposed hybrid workflow | Cross-source normalization, approved knowledge and exception handling | Data rights, complexity, insufficient quality lift | Incremental benefit against strongest baseline |

**Minimum viable knowledge record:** event ID, source and timestamp, normalized taxonomy version, supporting evidence references, authorized scope, applicable rule version, original decision, corrected decision, reason, reviewer role, validation status. Retention and rights are inherited from policy; no raw customer data in shared learning without permission.

**Feedback experiment (H2):** Freeze a representative holdout and compare baseline and correction-enabled workflows on the same cases. Pre-register target: >=5 percentage-point lift in correct automation coverage at >=95% auto accuracy, or >=10% reduction in review time without accuracy deterioration. Report confidence intervals and segment results; collect enough cases for meaningful comparisons. If neither condition is met, discontinue custom learning investment and use a simpler native/rules solution. No training on the holdout. Knowledge is reviewed, versioned and reversible; no automatic model fine-tuning from user feedback.

**Cross-workflow reuse experiment (H3):** Test a second workflow (OEM report reconciliation) with and without validated event knowledge; target >=20% less reconciliation effort at non-inferior quality, or retire the reuse assumption. Do not count this benefit in the first workflow's ROI. Current 4/20 and target 17/20 remain unchanged until actual evidence exists.


## V4 measured synthetic knowledge-reuse experiment
[Benchmark](../01-the-bet/benchmark/README.md): 330 synthetic cases. D (ML plus base knowledge plus ten simulated approved corrections) = 60.61% correct coverage; C before corrections = 45.45%; E rules plus identical knowledge = 45.45%; B ML alone = 30.30%. This demonstrates recurring-code reuse in a designed scenario, not an actual compounding moat, independent generalization or competitor advantage. Maintain 4/20 unverified operational maturity; target 17/20. Public named alternatives and selection gates: [market evidence](public-market-evidence.md). Prioritize the simplest route; evaluate unseen code/OEM families and held-out expert adjudication before claiming advantage.

