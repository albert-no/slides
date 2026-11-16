# Review round 2 — approved

- Job: `2026-11-16-lec12-fairness-clarity`
- Reviewed commit: **`4be105b2f1765f493a615b659fc853b73044a75e`**
- Baseline: `6f5088cdfc7877ea7965b972df91c8447562b5f4`
- Previous review: `f6c0205ff9ebff33b52e205c87765ba3a3a674e8`
- Verdict: **approved**
- Round: 2 of 2

All seven blocking findings are closed. The revised explanations now agree across the main slides, short note messages and detailed notes. Keep the new example-first foundations and explicit distinctions between the fairness criteria.

## Findings rechecked

| Finding | Slide / page | Result |
|---|---|---|
| F01 | S79 / 23 | Closed: the Message specifies both the comparison population and the counted outcome; all four fractions retained correctly. |
| F02 | S80 / 27 | Closed: the three summary-table rules can coexist; the later impossibility triple is correctly identified as equal PPV/FPR/FNR under stated conditions. |
| F03 | S76 / 70 | Closed: calibrated equalized-odds is described as a feasible score-based generalized-error-cost relaxation, not the same label-flipping LP; Pleiss citation and locators added. |
| F04 | S49a / 77 | Closed: an unsupported named answer no longer establishes a religious cause; systematic stereotype-aligned behavior is what is tested. |
| F05 | S50a / 79 | Closed: zero includes the ambiguous all-Unknown boundary; the disambiguated undefined-score case is retained. |
| F06 | S44b / 72 | Closed: y and the approximate 0.745 reading both explicitly say balanced accuracy. Figure/type unchanged; subtitle and key fit. |
| F07 | S38 / 57 | Closed: four stacked records preserve every weight-table value and the exact-2/3 explanation. The full note document no longer scrolls horizontally at 430px. |

No new blocking findings or unresolved preferences. The accepted “one percentage point” wording change is correct. The additional note-local code-wrapping rule is a justified completion of F07: it fixes the two long S47/S48 filenames without changing content, size or shared styles.

## Request coverage

The baseline-to-revised page trail remains in work-r1/review-r1; no pages moved in round 2.

| Comment | Status / location |
|---|---|
| C01 | Content done: main and companion notes approved. PR follows the final-record push and log-only verification. |
| C02 | Done: unsupported S77 importance-photo example removed. |
| C03 | Done: sourced occupation example on S51a/p5; unavailable X post not asserted as evidence. |
| C04 | Done: S74/S51a/S78 distinguish learned patterns and fairness judgments. |
| C05 | Done: S04a/b and S54a explain cost versus need, allocation consequence and mechanism limits. |
| C06 | Done: S07 names the datasets' evaluation tasks. |
| C07 | Done: S12a/b and S13a–d distinguish approval, prediction and missing outcomes. |
| C08 | Done: S79/S80 summary tables; S16 navy-box key; F01/F02 closed. |
| C09 | Done: S17a one-line shared-point interpretation. |
| C10 | Done: S17b one-line equal-height interpretation. |
| C11 | Done: S20a moved before the example; foundations expanded through S81; F01/F02 closed. |
| C12 | Done: S14/S15/S16/S80 one-line criteria. |
| C13 | Done: S21b profit maximization subject to equalized odds. |
| C14 | Done: S23a/S27 identify Northpointe. |
| C15 | Done: S29 contextualizes the base rate. |
| C16 | Done: S30 rejects FPR as a universal target. |
| C17 | Done: S32a/S33 define recorded rearrest and distinguish the flag. |
| C18 | Done: S32b/S82 show incompatible and compatible cases with conditions. |
| C19 | Done: S40a/b repeated cost-sensitive fitting, not an extra detector. |
| C20 | Done: S75/S83 explain feasible mixtures and same-sign gaps. |
| C21 | Done: S84 experiment protocol; S41a/b curve messages. |
| C22 | Done: S43a/b scope constrained lender-profit costs. |
| C23 | Done: S76/S44a/b nine alternatives and distinct baselines; F03/F06 closed. |
| C24 | Done: S45/S54a distinguish rate mitigation from label validity. |
| C25 | Done: S49a/b/S50a/b define context sufficiency and score interpretation; F04/F05 closed. |

## Verification

- Exact-commit diff: only S44b's two main-slide text lines, seven note articles, note-local `overflow-wrap` for code, and this job's record changed since round 1. No changes to the argument, slide order, generators, technical supplement, shared styles or scripts.
- Read changed notes with their surrounding explanations and checked consistency with round 1's verified primary sources (E08/E10/E19–E22). No new factual claims outside the approved corrections.
- Independently rendered and visually checked main pp71–73 at 1280×720. No clipping, collision, broken image or KaTeX error; S44b's labels fit without smaller type or image.
- Notes checked at 1100px and true 430px viewports, with targeted visual inspection of S79/S80/S38/S76/S49a/S50a and the S47/S48 code wrapping. All article elements checked excluding hidden MathML: **no overflow**; narrow document scroll/client width both **415px** (430px viewport minus scrollbar). Desktop scroll/client width both 1085px. No KaTeX errors.
- 87 unique main IDs and 87 matching note IDs in the same order. Timing still 90 minutes; section budgets unchanged at 10/25/15/20/13/7. Main line counts and outline locators unchanged.
- Main lint: no errors/font warnings; the same baseline 30 hardcoded-color occurrences. Notes lint and diff whitespace check clean. Outline lint has only the previously recorded unrelated lec09 workspace-file pointer missing in this container; no lec12 issue.
- The copied review-r1 is byte-identical to the frozen owner file.

## Final record and PR gate

Approval is pinned to `4be105b2f1765f493a615b659fc853b73044a75e`. Copy this review unchanged and refresh the living job files, then push the final record. Return a pointer with the final pushed SHA. Commits after the approved SHA must touch **only** `log/2026-11-16-lec12-fairness-clarity/`; slides-review will verify that before opening the PR against main. No merge authorization.
