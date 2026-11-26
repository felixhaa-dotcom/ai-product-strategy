# V4 activity-based economics and rollout sensitivity

All numbers are synthetic scenarios, not measured financial data. Historical V3 constant-other-COGS and steady-state scenarios are comparison cases, superseded for funding decisions by this model.

## Internal decision
Baseline: 100 parks × 2 h/park/month × 12 = 2,400 h/year. 75% reduction = 1,800 h/year or €180,000 gross economic equivalent at €100/h. Realization 25%, annual incremental OPEX €10,000, €32,000 upfront synthetic investment. Steady-state annual net €35,000, simple payback 11.0 months. With 25% adoption in months 1–3, 50% in months 4–6, 100% in months 7–12 (8.25 equivalent full months), first-year gross realized value €30,937.50 less €10,000 = €20,937.50 net. **€11,062.50 remains unrecovered at month 12.** At steady state thereafter, payback ~15.8 months (excluding discovery prior to rollout, taxes and discounting). At least 33.94% realization required for year-one payback at this adoption ramp and 75% effort reduction. At 50% effort reduction it rises to 50.91%. Do not claim a positive 12-month gate at the 25% assumption.

### Alternatives and incremental economics (synthetic sensitivity, not quotes)
| Path | Effort reduction | One-time cost | Annual incremental OPEX | Steady annual net at 25% realization | First-year net less investment (same ramp) |
|---|---:|---:|---:|---:|---:|
| Manual | 0% | €0 | €0 | €0 | €0 |
| Native | 60% | €8,000 | €12,000 | €24,000 | €4,750 |
| Rules + knowledge | 55% | €16,000 | €6,000 | €27,000 | €687.50 |
| Hybrid custom | 75% | €32,000 | €10,000 | €35,000 | −€11,062.50 |

These assumptions do not establish an actual vendor ranking. If this scenario were true, native would have highest year-one net value; hybrid's incremental €11,000 steady-state net vs native costs €24,000 additional upfront, ~26.2 months simple incremental payback ignoring ramp. **No custom-build funding until measured comparison supports it.** Include all discovery, rollout and switching costs in approval economics.

## External option: activity-based stress test
Illustrative buyer-operated review scenario: €5 base + €0.25 per verified successful outcome; 70 per 100 events at base volume. Inference €2.40; fixed service allocation €2; variable retrieval/hosting/support allocation €3 at base volume. Customer supplies review labor; vendor costs still provisional. Variable costs scale linearly for this sensitivity, not constant.

| Scenario | Revenue | COGS | Gross margin |
|---|---:|---:|---:|
| Base | €22.50 | €7.40 | 67.1% |
| 3× inference | €22.50 | €12.20 | 45.8% |
| 2× usage, fixed revenue | €22.50 | €12.80 | 43.1% |
| 10× usage, fixed revenue | €22.50 | €56.00 | −148.9% |
| 10× usage, hybrid | €180.00 | €56.00 | 68.9% |
| 10× usage, hybrid, 3× inference | €180.00 | €104.00 | 42.2% |
| Base, vendor supplies review (30 cases × 0.5 min × €100/h) | €22.50 | €32.40 | −44.0% |

With vendor-supplied review, a 40% gross-margin floor implies revenue ≥€54/turbine/month at assumed cost. With buyer-supplied review, measure buyer ROI including retained work. Separate review from vendor cost to avoid double counting. Proposed commercial gate: 5 buyer interviews, 3 written price reactions and 2 paid pilot intents (not achieved); minimum 40% full contribution margin under base and adverse agreed scenarios before launch. No sales or external pricing approval.
