# review-r2 — Final review

- Reviewed commit: `9a7342a5ef1a90b90225f2f4e4078f45af26d070`.
- Previous reviewed commit: `74ee8118731e4758c51366f11c0951b586e482a5`.
- Verdict: **approved**. No open blocking findings.
- Round: 2 of 2. Approval is for this exact commit, not an unreviewed later content change.

## Coverage and closure

| Item | Slide / page | Result |
|---|---|---|
| C01 | S64 / 40 | Done; the approved three-step oracle explanation is unchanged. |
| C02 | S69b / 45 | Done; direct heavier-is-not-always-better comparison and both notes are unchanged. |
| C03 / F01 | S132 / 47 | Closed: one normalization table, within the five-element budget; duplicate bar removed. Masses, probabilities, Z=7 and the easy-toy/large-sum scope remain visible. Numerical logits remain in both notes. |
| C03 / F02 | S133 / 51 | Closed: only concrete ratio arithmetic remains; batch caption sits beside the three draws. In live 1280×720 presentation mode, scrollHeight=clientHeight=720 and the divider is restored to 4px. No type reduction; the 8/9 versus 4/7 error comparison and finite-n qualification remain. |
| F03 | S64 / 40, M | Closed: accessible text now describes the red line rather than a nonexistent return arrow. |

No new findings. Bottom whitespace on S132 is acceptable; do not refill it. Keeping S74's generic dummy variable x is also acceptable. No change to the plan's argument, scope or evidence was necessary.

## Verification

- Read the exact r1→r2 diffs in D/H/M and the outline. Changes are confined to the requested layout/description fixes, unused local styling removal, shifted pointers and job records. No new facts or altered calculations.
- Rendered and inspected pp46–48 and 50–52 from an exact-commit archive. Both changed main slides and their neighbours have no overflow or KaTeX errors in the layout audit. Independently inspected S133 in live presentation mode to confirm F02's correction, not only its PDF appearance.
- S132/S133 HTML notes rendered and inspected at actual 430px mobile (scale 1, article width 382px) and 1280px desktop. No horizontal overflow, math/code outside the article, or KaTeX errors. Read both notes editions for consistency with the revised exhibits and retained details.
- D/H lint passes. M is ASCII, with 23 accessible-edition warnings (unchanged baseline count). D/H/M retain 70 matching IDs in unchanged order.
- Target leaf outline lint: 0 stale/missing pointers and 0 warnings. Seven section pointers and two theorem pointers checked against their actual destination lines. The unrelated repository-wide outline issue recorded in r1 is unchanged and outside scope.
- Requests, evidence, plan-v1 and review-r1 tracked copies match owner originals exactly. The mathematical and figure-reproduction checks from r1 remain applicable: no generator, figure data or example arithmetic changed in r2.

## Final handoff

Copy this review and the current living job header unchanged into `log/2026-11-18-prob09-oracle-tails-softmax/`, push, and send the exact final SHA. After this reviewed commit, only that job-record directory may change without another content review. Owner will verify the push and update existing PR #77; do not open another PR. No merge authorization.
