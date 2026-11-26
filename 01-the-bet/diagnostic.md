# Three-Axis Vulnerability Diagnostic

**Version 4 update:** The original course-format working draft is preserved below for iteration history. The final V4 section and root [README](../README.md) supersede earlier status, cost sensitivities and assessment where they differ.


**Confidentiality and evidence:** Employer, actual suppliers, locations and internal names are withheld. All financial, portfolio and staffing figures are synthetic scenario assumptions. All proposed controls, metrics, competitor profiles and architecture are unverified unless explicitly stated. No operational data is included.


## Product
**Product:** AI-Powered Wind Asset Operations Intelligence (first wedge: wind turbine status categorization).
**Your Role:** Digital Product Management (anonymized).
**AI Value Archetype:** Automator; Copilot for exceptions. Orchestration is a possible future capability, not a v1 promise.

## Scores
### Contextual Moat — 3/5
**Score rationale:** Established technical asset management workflows and contract-specific rules; switching costs not proven.
**Named attacker (from partner challenge):** Vendor A (masked profile; peer review pending).

### Data Advantage — 3/5
**Score rationale:** Potential historical data and expert classifications; no demonstrated compounding loop.
**Named attacker (from partner challenge):** Vendor B (masked profile; peer review pending).

### Platform Exposure — 2/5
**Score rationale:** Existing monitoring providers could bundle equivalent functionality. 1 = exposed, 5 = protected.
**Named attacker (from partner challenge):** Vendor A (masked profile; peer review pending).

**Vulnerability Scores:** Moat 3/5 · Data 3/5 · Platform 2/5.
**Composite:** 8/15 (provisional; qualitative band only).

## Top Vulnerability
Native platform functionality may displace the core feature before proprietary learning loops are established.

## Confidence Level
M — provisional; independent peer review and competitor fit assessment pending.

## Competitor pressure
- Vendor A: established asset performance platform; evaluate native features and cost.
- Vendor B: specialist renewable analytics provider; evaluate data intelligence.
- Vendor C: adjacent analytics platform; evaluate outage management and interoperability.

Disclosure: Employer and competitor identities withheld; vendor profiles and scores are hypotheses, not verified market evidence.

## Revised product thesis (V3)
For technical asset managers handling recurring operational events across multiple sources, provide an evidence-backed workflow that normalizes events, applies approved rules, suggests classifications/comments and captures expert decisions. The long-term product is a reusable operations knowledge layer plus narrowly scoped workflows. The initial customer is internal operations; the economic buyer is operations leadership. Start with one classification workflow, not a general AI platform.

**Job to be done:** When an operational event arrives, determine its category and documented cause quickly enough to keep downstream reporting reliable, without repeating source interpretation or losing contractual context.

**Why now:** The workflow can be tested against existing manual decisions and monitoring products. Availability of usable data, repeated pain and buyer demand are hypotheses, not established market signals.

**Core hypothesis:** A governed cross-source workflow will correctly automate >=70% of all in-scope events, achieve >=95% accuracy among automatically applied cases and reduce end-to-end manual effort by >=50%, with a lower risk-adjusted TCO than the best compliant alternative. If an incumbent meets the need more cheaply, adopt it and retain only justified integration/knowledge components.

## Evidence acquisition plan (weeks 1–4)
| Hypothesis | Method and proposed sample | Decision threshold | Evidence owner |
|---|---|---|---|
| Repetitive work is material | Interview 6–10 asset managers and 2 operational leads; time study 8–10 representative parks, preferably two OEMs; log elapsed active effort and rework | Median effort and annualized volume support Finance-approved payback <=12 months; otherwise narrow or stop | Product + TAM lead |
| Cross-source context creates unmet value | Review 100 historical events if authorized; compare a native workflow, rules-only and evidence-backed approach on identical events | Identify at least one recurring material gap; if native covers requirements at lower risk-adjusted TCO, buy | Product + architecture |
| Data can legally and technically be used | Test approved read-only sample; check source completeness, event identity, access rights | Required fields present for >=95% of pilot records or scoped exclusion with measured coverage; unresolved rights/security issue stops pilot | Data owner + security |
| Operators adopt the workflow | Observe five task walkthroughs; compare time and correctness against manual workflow | At least 4/5 can complete intended task without facilitator, no critical usability blocker; exploratory signal only | Product + TAM |

Log source, sampling method, period, observation, owner, confidence and decision for each result. Do not fabricate interviews, results or vendor tests.

## V3 vulnerability diagnostic
Current evidence-based starting scores remain 3/5 contextual moat, 3/5 data advantage, 2/5 platform exposure = 8/15. Future design targets: 4/5, 4/5, 3/5 = 11/15, contingent on proven multi-source workflow fit, measured correction reuse and native alternative assessment. Broader positioning alone does not establish a moat. No named supplier is disclosed; illustrative competitor profiles do not satisfy the named-attacker evidence requirement fully.


## V4 evidence and sharpened bet (supersedes V3 where different)
Industry evidence supports the generic problem and technical plausibility, not this customer's workload. Named public benchmark competitors: Algorithm Energy, Nabla Wind Hub and Microsoft Fabric; see [public evidence](../02-the-moat/public-market-evidence.md). No actual supplier affiliations disclosed. Initial vulnerability score remains 8/15; public threats confirm exposure. Executed [synthetic benchmark](benchmark/README.md) shows D at 60.61% correct coverage, short of 70%; no production approval. V4 bet: choose the minimum-complexity compliant solution, and invest in ML only for incremental value vs knowledge-enabled rules. Existing native offerings are not yet tested. The 12-week gate remains unchanged.

