# Cost Curve & Pricing Strategy

**Version 4 update:** The original course-format working draft is preserved below for iteration history. The final V4 section and root [README](../README.md) supersede earlier status, cost sensitivities and assessment where they differ.


**Confidentiality and evidence:** Employer, actual suppliers, locations and internal names are withheld. All financial, portfolio and staffing figures are synthetic scenario assumptions. All proposed controls, metrics, competitor profiles and architecture are unverified unless explicitly stated. No operational data is included.


**Disclosure:** All portfolio, workload, cost, budget and staffing figures are synthetic illustrations, not actual company data or approved commitments.

## Packaging Decision
- Leader: status classification.
- Filler: comments and standard summaries.
- Killer: advanced root cause and complex contractual analysis; add-on candidate; usage not verified.

## Cost Model
Illustrative baseline (synthetic scenario, not measured company data): 100 illustrative wind parks, 1–3 h/park/month; midpoint 2.0 h. Illustrative residual effort 0.5 h. At €100/h, midpoint capacity release is 1,800 h/year or €180,000/year gross economic equivalent. The synthetic hourly rate is a value proxy, not actual payroll cost. No hard savings established.

Operating cost, actual event counts, human-review cost and implementation effort require validation. Illustrative planning scenario: €10,000 annual incremental operating cost; €32,000 total one-time effort cap (40 person-days × 8 hours × €100/h, proposed, not approved). At 25% economic realization, annual benefit after operating cost is €35,000, simple payback 11.0 months after steady-state rollout. Excludes ramp-up, discounting and unbudgeted costs.

| Cost Category | Per-User/Month (per turbine proxy) | Notes |
|---|---:|---|
| Inference (primary model) | €1.92 | 24 frontier requests at €0.080 |
| Inference (cascading/triage) | €0.48 | 96 small requests at €0.005 |
| Infrastructure | Not separately estimated | Included only as a hypothesis in other COGS |
| Data/storage | Not separately estimated | Validate allocation |
| Human-in-the-loop | Not separately estimated | Validate residual review cost; no double counting |
| **Total AI COGS** | €2.40 inference only | Full AI COGS unknown |

**Total AI COGS / unit:** €2.40 inference per turbine/month (synthetic); full AI COGS unverified.

## Cascading Strategy
**Triage model:** Small approved model; provider not yet selected.
**Frontier model:** Approved high-capability model; provider not yet selected.
**Routing rule:** Deterministic rules first; use small model for routine cases, frontier for ambiguity, expert review for critical cases.
**Expected cascade ratio:** 80% small / 20% frontier (hypothesis).

- Rules before AI; small model for routine tasks, frontier for ambiguous cases; human review for critical cases.
- Illustrative request split 80/20; costs €0.005 / €0.080; blended €0.020 per model request.
- Provider-specific prices and actual routing not verified.

## Pricing Model
**Current pricing:** internal efficiency initiative; no confirmed standalone revenue.
- Strategy posture: Penetrate/adoption internally; Maximize only for a hypothetical external offer.
**Proposed AI pricing:** Hybrid; €5/turbine/month + €0.25/successful categorization. Assumes 70 successful outcomes out of 100 events and €22.50 monthly revenue per turbine. Not a proposed approved tariff.
**Model:** hybrid (hypothetical external offer); internal efficiency first.
- Unit of work: correctly automated categorization; failed attempts not billable.
- Illustrative 120 model requests × €0.020 = €2.40 AI inference cost; other assumed COGS €5.00; total €7.40; gross profit €15.10; margin 67.1%. Full costs including review and support must be verified.

## Stress Tests
| Commercial scenario | Revenue/turbine | AI cost | Total assumed COGS | Gross margin |
|---|---:|---:|---:|---:|
| Base | €22.50 | €2.40 | €7.40 | 67.1% |
| 3x inference | €22.50 | €7.20 | €12.20 | 45.8% |
| 2x usage, fixed revenue | €22.50 | €4.80 | €9.80 | 56.4% |
| 2x usage, hybrid revenue | €40.00 | €4.80 | €9.80 | 75.5% |
| +50% inference | €22.50 | €3.60 | €8.60 | 61.8% |

Other COGS held constant for illustration only; do not infer actual profitability. The per-turbine scenario is separate from the wind-park baseline; no conversion without asset counts.

**Stress response:** Reassess routing, model alternatives, actual review cost and pricing; block scale if economics or reliability fail.

## Board One-Pager
**Before (traditional SaaS):** Not applicable; internal manual process has no standalone product revenue or gross margin.
**After (AI-enabled):** Illustrative external revenue €22.50 per turbine/month, assumed COGS €7.40, gross margin 67.1%; not measured or approved.
**Gross Margin (current):** N/A — internal manual process.
**Gross Margin (AI-adjusted):** 67.1% (synthetic external scenario, not actual margin).
**Net margin shift:** N/A — no comparable standalone baseline; modeled internal effort reduction 75%.
**Break-even at:** 11.0 months after full rollout under synthetic 25% realization, €10,000 annual OPEX and €32,000 investment assumptions.


Before: 2,400 manual hours/year (100 × 12 × 2.0); after: 600 hours/year (100 × 12 × 0.5). Indicative 1,800 hours/year released, 75% reduction. At 25% realization and assumed annual OPEX €10,000: €35,000/year net economic benefit. Proposed cap €32,000; gate H1 at €8,000, then conditional release of €24,000. Validate the estimate with TAM, engineering and Finance before approval.

## V3: investment comparison and decision economics
Internal efficiency is the primary product business model. The commercial case is an option, not part of the approval ask. Compare four alternatives (manual / native / rules-only / hybrid) on a common workload and quality threshold. For each, include one-time integration, vendor license uplift, inference, retrieval, infrastructure, review/rework, monitoring/support, exit cost and implementation risk. Use incremental economic value vs the best feasible alternative, not only vs manual. If native wins, buy; avoid charging the project twice for existing infrastructure or review labor.

### Internal sensitivity (synthetic; 100 parks, €100/hour, €32k investment, €10k annual incremental OPEX)
| Effort reduction | Realization | Annual net value | Steady-state payback |
|---:|---:|---:|---:|
| 50% | 25% | €20,000 | 19.2 months |
| 75% | 25% | €35,000 | 11.0 months |
| 75% | 50% | €80,000 | 4.8 months |
| 75% | 75% | €125,000 | 3.1 months |
| 75% | 100% | €170,000 | 2.3 months |

At the 75% effort scenario, minimum realization for 12-month steady-state payback = (€32,000 + €10,000)/€180,000 = 23.33%. At 50% effort reduction it rises to 35%. Payback including pilot and rollout will be longer; H1 must build a monthly cash/economic-value model with adoption ramp and incremental costs. At week 12 the gate is <=12 months **from approved full-rollout investment under a Finance-approved schedule**, not an automatic pass from the synthetic steady-state scenario. Explicitly identify who redeploys capacity, what value it produces and how Finance recognizes avoided cost or additional contribution. No assumed layoffs or booked cash savings.

### Tenfold usage stress (illustrative commercial option)
| Scenario | Revenue / turbine-month | Assumed total COGS | Margin |
|---|---:|---:|---:|
| 10x usage, fixed revenue | €22.50 | €29.00 | -28.9% |
| 10x usage, hybrid | €180.00 | €29.00 | 83.9% |
| 10x usage, hybrid, 3x inference cost | €180.00 | €77.00 | 57.2% |
These optimistic hybrid sensitivities assume unchanged outcome rate, constant €5 other COGS and proportional demand. They are NOT forecasts: review cost, support, caps and willingness to pay may invalidate them. Test usage caps, variable human review and segment-specific demand before pricing. No commercialization gate until internal value and willingness to pay are evidenced. Advanced reconciliation is a separate value hypothesis; no double counting.


## V4 decision model — supersedes optimistic V3 stress assumptions
Read [activity-based economics and rollout sensitivity](v4-economics.md). 25% realization fails 12-month ramp-aware payback (~15.8 months); at least 33.94% needed under modeled ramp. Commercial variable costs scale with volume; 10× hybrid margin 68.9%, 10× fixed −148.9%, 10× hybrid with 3× inference 42.2%. Vendor-provided human review can make base margin negative (−44%). All are synthetic, not actual costs. Native/rules alternatives could win; incremental value and paid-demand evidence required.

