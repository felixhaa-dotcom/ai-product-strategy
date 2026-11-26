# Kill Switch Audit

**Version 4 update:** The original course-format working draft is preserved below for iteration history. The final V4 section and root [README](../README.md) supersede earlier status, cost sensitivities and assessment where they differ.


**Confidentiality and evidence:** Employer, actual suppliers, locations and internal names are withheld. All financial, portfolio and staffing figures are synthetic scenario assumptions. All proposed controls, metrics, competitor profiles and architecture are unverified unless explicitly stated. No operational data is included.


## Current Setup
- **Primary provider:** To be confirmed.
- **Integration depth:** Not verified.
- **Time to switch today:** Not tested.

## Vendor Dependency Assessment
| Dimension | Current state | Risk | 48-hour action (target capability) |
|---|---|---|---|
| Provider | Unconfirmed | Unknown | Activate preapproved alternative |
| Abstraction | Unverified | Potentially high | Change gateway configuration rather than application code |
| Routing | Unverified | Potentially high | Redirect requests or fall back to manual workflow |
| Eval | Unverified | Potentially high | Run release gates and representative tests before restoring automation |

## Portability Score
Not assessed — readiness unverified; neither Ready nor Locked can be substantiated.

## If primary vendor doubles pricing tomorrow:
Benchmark approved alternatives and fall back to manual processing if quality or compliance gates fail.

## If primary vendor ships a competing product:
Compare native capability and total cost; preserve authorized knowledge and business logic.

## Stress Test
- If pricing doubles: benchmark approved alternatives on quality and total cost before migrating.
- If ToS restricts use case: suspend affected processing; use compliant fallback or manual process.
- If provider ships competing product: compare build vs buy; preserve authorized data and business logic.
- Risk level: potentially high until portability demonstrated.

## Three Actions
- This week: inventory dependencies and contractual data rights.
- This month: define provider-independent interface and benchmark dataset.
- This quarter: test switching between two approved providers within 48 hours, subject to funding and security approval.

## V3 capability design and exit test
Use source-specific read-only adapters -> canonical event schema -> approved rule engine and retrieval -> model gateway -> validation/policy engine -> review queue -> approved write-back adapter. The knowledge layer uses versioned, exportable structured records and references. No specific provider or integration is assumed available. Start with one adapter and a second synthetic source; add a real second source only if the H1 evidence supports it.

| Time after provider incident | Planned action | Proposed owner |
|---|---|---|
| 0–1 h | Suspend affected automation; route to manual queue; preserve audit records | Operations lead + platform on-call |
| 1–8 h | Check permitted alternative, configuration, data residency and incident impact | Engineering + security |
| 8–24 h | Run versioned regression suite and compare cost/latency/quality | QA + TAM specialist |
| 24–48 h | Restore only after designated product/security/operations approvals; otherwise remain manual | Product + operations |

**Acceptance:** Restore compliant automated service within 48h in a drill, or explicitly fail the portability gate; manual fallback must remain usable from the outset. Measure recovery separately from switching time. No production recovery promise yet. Record actual drill time, costs, failures and approvals. If an alternative cannot pass gates, reconsider dependency or use native functionality.


## V4 local fallback demonstration
A local deterministic route and separately executable local ML engine now exist on synthetic data. Eighty mandatory-review fixtures were routed to review across all methods; the simulated outage fixture uses supplied metadata. This is not a real vendor-switch or incident drill. Production 48h portability remains unverified. Keep local manual queue, versioned export, independent restore drill and measured provider fallback as H2 gates.

