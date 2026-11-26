# Executed offline benchmark — V4

**Scope:** Fully synthetic, locally executed supervised text-classification experiment. No employer data, actual OEM codes, actual supplier relationship, LLM, real API, OT access, or production performance claims.

## Method
- Python 3.13.5, scikit-learn 1.8.0; TF-IDF unigram/bigram features and multinomial naive Bayes trained on 40 synthetic phrases. Two mock source adapters normalize the same canonical schema.
- Development: 165 generated cases (seed 21); held-out synthetic instances: 330 (seed 87), 250 routine category cases and 80 mandatory-review cases. Shared generator, templates and author; this is not independent external validation.
- The threshold (0.55) was selected on development cases only. It is an uncalibrated model score, not a 95% production confidence guarantee. The control route uses explicit synthetic metadata and literal text checks.
- C adds ten fictional OEM-scoped mappings. D adds ten simulated approved correction records from separate development examples. E is the essential stronger control: the same knowledge and corrections as D, with keyword rules instead of ML. Repeated codes intentionally test reuse, not generalization to unseen codes.

| Approach | Auto | Correct | Review | Auto accuracy | Correct coverage (all 330) | Mandatory-review misses |
|---|---:|---:|---:|---:|---:|---:|
| A · Keyword rules | 50 | 50 | 280 | 100.0% | 15.15% | 0/80 |
| B · Local ML | 100 | 100 | 230 | 100.0% | 30.30% | 0/80 |
| C · ML + knowledge | 150 | 150 | 180 | 100.0% | 45.45% | 0/80 |
| D · ML + knowledge + corrections | 200 | 200 | 130 | 100.0% | 60.61% | 0/80 |
| E · Rules + identical knowledge | 150 | 150 | 180 | 100.0% | 45.45% | 0/80 |

**Interpretation:** D classified 200/330 correctly (60.61%); +30.31pp vs B, +15.16pp vs C, +15.16pp vs E. All 80 mandatory-review fixtures routed to review in every arm; explicit flags and literal phrases make this a routing/control test, not a red-team security evaluation. The 100% auto-eligible accuracy is a property of this deliberately controlled synthetic dataset and not evidence for actual reliability. 50 unknown-code cases correctly abstain but are still counted against all-event coverage. The 70% all-in-scope coverage target was missed (231 correct events required; gap 31). **Do not relabel the denominator or reduce safety gates.** Routine-only correct coverage of D is 80% (200/250), a diagnostic segment only.

## Decision
Do not authorize production. Test a rules/lookup baseline with identical domain knowledge against more robust ML and native offerings on an independently labeled authorized sample, including novel code families, noisy text, unseen OEMs, overlapping causes and adversarial variants. If the rules or native path is equivalent and cheaper, adopt it. The synthetic experiment justifies a bounded feasibility phase, not a moat or an LLM implementation.

## Reproduction
`python -m pip install -r requirements.txt` then `python run_benchmark.py`. See `results.json`, `predictions.csv`, `test_events.json`, `development_events.json`, `synthetic_corrections.json`, `model_params.json`. Local latency is recorded for reproducibility only and varies by machine; no production latency/cost conclusion.

The standalone browser classifier uses exported learned weights, without network access. JS/Python check: **1650 classification and route comparisons matched Python.** Headless Chromium smoke test using the HTML content directly: 70 example/method combinations plus invalid JSON passed; no page errors. Navigation of all 11 board slides passed. Direct file:// loading was blocked by the test environment, so local-file navigation and hosted deployment are not verified. Run `node verify_browser.js` from this directory. The old scripted UX walkthrough is separate and does not prove model behavior.
