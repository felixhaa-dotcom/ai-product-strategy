# AI Product Strategy — Wind Turbine Status Categorization

**Anonymization note:** This course case is based on a real type of operational workflow. Employer, internal initiative names, locations, platform names and supplier relationships are intentionally undisclosed. Portfolio sizes, workload estimates, internal rates, costs, budget and staffing allocations are synthetic teaching assumptions, not company data. No actual operational records, customer data or verified pilot results are included. Vendor A/B/C are anonymized competitive archetypes, not confirmed suppliers or verified competitor assessments.

**Status:** Strategy draft assembled from course work; not an approved business case or deployed product. Use only synthetic data and an approved private repository. No hosted prototype URL, actual backlog, verified provider setup or pilot results supplied.

## Strategy at a Glance
| Component | Summary |
|---|---|
| The Bet | Reduce repetitive wind turbine event categorization and commenting; Automator |
| The Moat | 8/15 provisional vulnerability; 4/20 assumed current flywheel, 17/20 target |
| The Margin | Internal capacity release is primary; €180,000 annual gross equivalent under synthetic scenario assumptions; commercial 67.1% illustrative only |
| The Contract | >=95% auto accuracy; >=70% correctly automated events; critical decisions human-reviewed |
| The Guardrails | Controlled autonomy, validated feedback, provider independence and security gates; 15/25 provisional maturity |
| The Pitch | Proposed 12-week staged validation; initial 10 PD/€8,000, total 40 PD/€32,000 conditional cap |

## The Bet (M1)
- **Product:** AI-powered Wind Turbine Status Categorization.
- **User:** Technical Asset Managers.
- **Hypothesis:** Automate routine classifications and comments while improving scalability and preserving control.
- **Kill criteria:** Stop at week 4 if data access infeasible or native option is better; stop/pivot at week 12 if <95% automatic accuracy, <70% successful automation, <50% manual effort reduction, or unresolved critical risk.
- [Diagnostic](01-the-bet/diagnostic.md) · [Prototype specification](01-the-bet/prototype.md) ([offline scripted demo](01-the-bet/prototype-demo.html); hosted URL pending).

## The Moat (M2)
- **Defensibility:** Workflow, authorized operational data, contractual logic and validated corrections; not the AI model.
- **Primary attacker:** Vendor A; validate native capability and cost before build.
- **Flywheel:** Capture corrections and demonstrate measurable lift on separate holdout.
- **Vendor portability:** Provider unconfirmed; target validated 48-hour switch or controlled manual fallback.
- [Data flywheel](02-the-moat/data-flywheel.md) · [Kill switch](02-the-moat/kill-switch.md).

## The Margin (M3)
- **Internal economics:** Synthetic scenario: 100 illustrative wind parks, baseline 1–3h/park/month, midpoint 2.0h; modeled residual effort 0.5h. 1,800h annual capacity release, gross equivalent €180,000 at €100/h. Validate before relying on figures.
- **Illustrative investment:** €32,000 effort cap and €10,000 annual incremental OPEX. At 25% economic realization, €35,000 net annual benefit; ~11.0-month steady-state payback (not rollout-adjusted). Cash savings not established.
- **Commercial option:** Hybrid pricing hypothesis €5/turbine/month + €0.25 per successfully automated classification. Separate turbine model, not actual revenue, no park-to-turbine conversion assumed.
- **Cost discipline:** Rules first, quality-gated model cascading, human review costs and actual TCO tracked.
- [Cost curve](03-the-margin/cost-curve.md).

## The Contract (M4)
- **Reliability:** >=95% accuracy on auto-applied cases; hallucination <1% target and zero tolerance for confirmed critical incidents; p95 <=10 seconds; drift <=0.5 pp/week.
- **Golden dataset:** 10 synthetic draft cases; target ~150 curated examples plus protected holdout and sufficient production sampling. No executed eval evidence supplied.
- **Human control:** Confidence >=95% plus mandatory checks for routine cases only; critical cases always human approved. Evidence, override and audit logs.
- [Golden dataset and reliability contract](04-the-contract/golden-dataset.md).

## The Guardrails (M5)
- **Governance:** Approved data access, no autonomous OT control or financial commitments; formal risk and data-rights assessment before release.
- **Compounding:** Recursive learning, cross-domain transfer, authorized fleet intelligence; all unverified today.
- **Shadow AI:** 10 discovery hypotheses, none verified, adjacent spend unknown; build differentiated capabilities and integrate commodities.
- [Compounding system and governance](05-the-guardrails/compounding-system.md).

## The Pitch (M6)
- **Audience:** Renewable asset management leadership.
- **H1 (0–4 weeks):** Measure baseline; compare native vs build; prove feasibility; curate evals; scope governance and costs.
- **H2 (1–3 months):** Run shadow-mode pilot, validate economics, reliability and feedback; no write-back without approval.
- **H3 (3–6 months):** Conditional phased rollout and limited experiments across OEMs and adjacent workflows.
- **Ask:** Approve 10 person-days (€8,000 effort equivalent) for discovery; reserve up to 30 further person-days (€24,000) conditional on the gate. No committed headcount or external OPEX funding assumed.
- [Roadmap, evaluation and board pitch](06-the-pitch/roadmap.md).

## Evidence and versioning
All estimates are provisional; portfolio and internal cost figures are synthetic scenario assumptions, not measured results. Update the component files first and reassemble README monthly. This manually consolidated draft has not been run through the Product School parser. Replace placeholders only with disclosure-approved evidence and an approved hosted prototype URL before submission.

## Final presentation
[Board pitch (HTML)](final-presentation.html) — standalone presentation based on the board pitch in the roadmap. Open locally or submit as a file, subject to company disclosure approval. This deck was created independently, not exported from the course Pitch Builder.
