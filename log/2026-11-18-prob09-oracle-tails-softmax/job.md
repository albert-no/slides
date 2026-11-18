job: 2026-11-18-prob09-oracle-tails-softmax
size: medium
deck: courses/deepmath/prob09-monte-carlo/prob09-monte-carlo.html
audience / mode / duration: junior undergraduate AI majors / rigorous, example-led / no pacing constraint
baseline: b96c6060c05de3b28c20a918bb388d7b2e6b68a1 (70-slide current PR77 head; all requested page numbers)
id commit: c47b198f8e8d0153fee6923ce2dafe8b13f4fe77 (inherited; stable IDs already present)
branch: 2026-11-17-prob09-major-revision (existing PR77 continuation; no second PR/branch)
pr: 77 (open, unmerged)
pr url: https://github.com/albert-no/slides/pull/77
state: in-work
round: 2 of 2
current plan: plan-v1.md
review candidate: 74ee8118731e4758c51366f11c0951b586e482a5
latest review: review-r1.md — revise; F01/F02 blocking, F03 nonblocking
current action: work order for F01/F02 layout simplification; await work-r2 exact pushed SHA
albert decisions:
- 2026-11-18 16:49 KST: simplify current p40, answer whether heavier tails are better on p45, and replace the difficult p47 example with a simpler one such as softmax. Earlier waiver of pacing remains. No merge order.
verification: RO/RW mounts reconfirmed; fresh GitHub REST verifies PR77 open/unmerged at b96c606, base main b20ab73ac7e74e9489d379cf9caad7565f17e31e

## Sizing and scope

Medium, not a restructure: the five-part argument is unchanged, but replacing the Bayesian running example requires coordinated changes beyond the three named pages (its later application, notation bridges and notes). One new textbook definition is checked, not a literature survey. No large-job approval gate is needed. Up to two review rounds.

Allowed scope: target deck and its two notes editions, local generators/figures needed for the revised tail comparison and softmax arithmetic, the Deepmath leaf outline and genuinely stale root pointers. No earlier lecture, shared design/reference/script or RL changes. The just-approved pp4-5 log-loss revision is not reopened.

## Reconciled requests

1. p40 is a readability change, not a demand for additional theory. Reduce the oracle explanation to one circular-dependence idea; keep required caveats without the overloaded four-box chain.
2. p45 asks whether more tail mass is better, whereas the current slide only proves heavier tails are not necessary. Answer the stronger question directly: no monotonic improvement; excessive tail mass can worsen the variance for the same integrand.
3. Softmax is simpler as a normalizer example, but a three-outcome softmax has an easy, computable Z. Do not pretend otherwise. Use the small case to explain normalization and the conditional large-outcome case to motivate leaving the full sum uncomputed. The worked sample ratio later uses no Z even though the tiny toy supplies an exact check.

The previous Bayesian example is being replaced at the author's request, not merely trimmed for density. Retire its active derivations and cross-references rather than teaching two competing examples. Prior job records remain historical evidence, unchanged.
