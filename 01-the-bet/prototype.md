# The Prototype Bet

**Version 4 update:** The original course-format working draft is preserved below for iteration history. The final V4 section and root [README](../README.md) supersede earlier status, cost sensitivities and assessment where they differ.


**Confidentiality and evidence:** Employer, actual suppliers, locations and internal names are withheld. All financial, portfolio and staffing figures are synthetic scenario assumptions. All proposed controls, metrics, competitor profiles and architecture are unverified unless explicitly stated. No operational data is included.


## What I Built
V4 functional offline supervised-ML classifier plus separate historical scripted UX demonstration. Two synthetic source formats, five classification paths, actual predicted labels and review routing. No live LLM, real API or hosted deployment verified.
## Tool Used
Python/scikit-learn training and benchmark, standalone HTML/JavaScript inference UI; no external model provider.
## Prototype Link
[Functional offline classifier](prototype-demo.html); [original UX mock-up](prototype-ux-mock.html); approved shareable hosted URL pending.
## AI Value Archetype
Automator (with Copilot support for exceptions).
## The Bet in One Sentence
A governed, platform-independent operational knowledge workflow can reduce repetitive asset management effort; status categorization is the first test, and native capabilities are preferred wherever they meet requirements at lower risk-adjusted cost.
## Kill Criteria
At week 4, stop if data access is not feasible or an approved native alternative meets requirements at lower total cost. At week 12, stop/pivot if accuracy of automatic classifications is below 95%, successful automation below 70% of all in-scope events, or manual effort reduction below 50%; any unresolved critical reliability/security issue blocks rollout.

**Initial confidence:** 70% subjective hypothesis, not a measured probability.

## Prototype scope
Use synthetic records only: event queue, evidence panel, category suggestions, confidence bands, mandatory review for critical cases, and audit/override history. No write-back or real operational data in a public demo.

## V3 prototype hypothesis and tasks
The original V3 UX mock-up adds two fictitious source systems, normalized event evidence and a session-only expert knowledge record. Test whether a reviewer can trace an event to its source, distinguish a routine recommendation from a critical exception, override with rationale and inspect the resulting audit record. Test with five representative users; success = four complete all tasks unaided, with no critical misunderstanding. No tests have been run. Scripted confidence is not calibrated model confidence. The V3 scripted UX mock-up has no network connection, model inference, persistent knowledge or live integrations. Do not treat it as a working production AI product. A shareable hosted URL remains pending; use approved hosting or submit the local HTML as allowed by the course.


## V4 functional prototype (supersedes previous scripted-only status)
[Standalone local classifier](prototype-demo.html) implements trained TF-IDF / multinomial naive Bayes plus fictional OEM-scoped knowledge and policy gates. [Original scripted UX walkthrough](prototype-ux-mock.html) is kept separately. [Benchmark report](benchmark/README.md) includes actual Python run, full input/prediction files and browser/Python parity check. No LLM, live monitoring/API, production confidence calibration or hosted URL. The model is intentionally small, and a live LLM is not assumed to be needed. A real shareable URL and user usability test are pending.

