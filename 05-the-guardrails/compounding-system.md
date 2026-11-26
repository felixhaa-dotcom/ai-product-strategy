# Compounding System Design

**Version 4 update:** The original course-format working draft is preserved below for iteration history. The final V4 section and root [README](../README.md) supersede earlier status, cost sensitivities and assessment where they differ.


**Confidentiality and evidence:** Employer, actual suppliers, locations and internal names are withheld. All financial, portfolio and staffing figures are synthetic scenario assumptions. All proposed controls, metrics, competitor profiles and architecture are unverified unless explicitly stated. No operational data is included.


## Feedback Loops
| Loop | Input | Output | Compounds today? | Status |
|---|---|---|---|---|
| Recursive Learning | Validated corrections | Better classification | N | Missing (unverified) |
| Cross-Domain Transfer | Validated event knowledge | Better adjacent analytics and OEM reconciliation | N | Missing (unverified) |
| Network Intelligence | Authorized portfolio patterns | Better comparable asset classifications | N | Missing (unverified) |

**Broken loop identified by partner:** Pending actual peer review; hypothesis: corrections do not systematically reach product improvements.
**Fix plan:** Capture, validate and reuse feedback through governed pipeline; measure quality lift against fixed holdout.

## Context Connectivity
Target a shared internal data platform as provider-independent governed knowledge layer. Share data only where contractual rights, access controls and permitted purposes allow. Avoid assuming that data can be shared across clients or legal entities.

## Governance Policy
**Scope:** AI event categorization, comments, approved retrieval, routing, evals, feedback.
**Autonomy boundaries:** Read authorized data and draft suggestions automatically. Low-risk write-back only after approval of validation gates. Human approval for critical classifications and customer communications. No SCADA control or autonomous financial commitments.
**Escalation triggers:** Low confidence, evidence gap, security incident, critical event, reliability breach.
**Audit cadence:** Continuous technical monitoring; daily TAM exception review; weekly product eval; monthly quality/cost; quarterly digital product/security/legal review. Roles proposed; named owners pending.
**Regulatory exposure (EU AI Act / other):** Formal EU AI Act intended-purpose classification, GDPR where applicable, NIS2 / applicable national critical-infrastructure rules relevance, ISMS and contractual data rights to be assessed before rollout. No definitive legal classification asserted.

## Agent Topology
Not shipping autonomous agents in this version. Governed predefined workflow with controlled model calls and approval gates.

## Shadow AI Audit
| Workaround hypothesis | Signal | Frequency hypothesis | Proposed decision |
|---|---|---|---|
| AI OEM code interpretation | Capability | H | Build |
| Status comments | Capability | H | Build |
| External monitoring export analysis | Workflow | H | Build |
| OEM report summarization | Capability | H | Build |
| Classification cross-checks | Trust | M | Build / improve reliability |
| AI-assisted spreadsheet analysis | Workflow | H | Partner |
| Report translation | Capability | M | Partner |
| External integration automation | Workflow | M | Partner |
| Email rewriting | Capability | H | Ignore |
| Presentation formatting | Capability | M | Ignore |

**Total tools found:** 0 verified; 10 hypotheses.
**Tools after triage:** 5 proposed Build candidates; 3 Partner and 2 Ignore candidates, not verified.
**Estimated hidden spend:** Unknown (adjacent user spend, not measured).

**Pattern Assessment:** 10 hypotheses, 0 verified; 5 build, 3 partner, 2 ignore candidates. Adjacent spend unknown, not zero. Dominant hypothesized signal: capability gap.
**Action Plan:** Interview TAM and review permitted support/usage data. Validate frequency × strategic relevance; partner for commodity AI, avoid duplicate generic features. Repeat quarterly.

## Responsible AI Maturity
Compliance 3/5; Transparency 3/5; Fairness 3/5; Privacy 3/5; Accountability 3/5. Total 15/25 provisional self-assessment; target 24/25. No verified audit evidence yet.

## V3 governance operating model (roles proposed, appointments pending)
| Control / decision | Accountable role | Responsible role | Required evidence |
|---|---|---|---|
| Intended purpose, scope, funding gates | Product sponsor | Product lead | Approved scope, decision log |
| Data access, tenancy and retention | Data owner | Data engineering | Rights register, access/retention tests |
| Taxonomy and critical-event rules | TAM lead | Domain specialists | Approved version and adjudication log |
| Model change and evaluation | Product lead | Engineering/QA | Regression, holdout and cost report |
| Security and incident response | Security lead | Platform on-call | Threat assessment, incident and fallback drill |
| Economic realization | Finance owner | Operations + product | Time study, verified full costs and redeployment plan |
| Release to automatic write-back | Operations sponsor | Product + QA | All gates passed; security and domain sign-offs |

## Knowledge governance and scale
Use scoped knowledge collections, provenance, taxonomy/rule versioning, least-privilege retrieval, no unauthorized cross-tenant reuse, and auditable deletion/revocation. Treat externally supplied documents as untrusted data, not instructions. Separate correction submission, specialist approval and publication. Holdout is inaccessible to development feedback. Record model/rule versions with every decision and support rollback; no self-modifying agent. At 10x volume test queue latency, reviewer hours, model quota, per-tenant throughput, storage/access boundaries and total cost. Agree capacity/queue thresholds with operations before rollout; throttle or route manually if gates fail. No autonomous OT, financial or contractual commitments.

## Shadow AI discovery plan
The ten entries above are interview hypotheses, not observed workarounds. In weeks 1–4, interview proposed 6–10 TAM users and two leads, ask what AI tools they use, frequency, motivation, paid spend, data exposure and unmet workflow need. Review only permitted evidence. Classify frequency × strategic relevance; build where repeated unmet needs match the knowledge workflow, partner for commodity tasks, ignore unrelated workarounds. Log anonymized evidence and reassess quarterly. Do not report unobserved spend as zero. Current maturity 15/25 is a provisional self-assessment; target 24/25 only after documented controls. Review intended-purpose classification and applicable data/security obligations with qualified owners before production; no definitive legal conclusion.


## V4 operational test evidence and residual controls
[Benchmark](../01-the-bet/benchmark/README.md) used two mock formats, synthetic metadata gates, model abstention and simulated correction records, plus a rules-only control. No external tenant system, live policy enforcement, network/OT access, actual learning approvals or independent security test. Enforce separate production data rights, scoped IAM, knowledge approvals (two-person review for material mappings), model/knowledge rollback, test 10× queue capacity and real provider fallback. Shadow AI audit remains 0 verified; use interview guide and evidence register in discovery.

