# work-r2 — job 2026-11-18-prob09-clarity-trim

## Branch and commits

- Branch `2026-11-17-prob09-major-revision` (PR #77 continuation). The reviewed candidate was 6cf17f6.
- The head commit contains the round-2 fixes, this report, the copy of review-r1.md, and the refreshed living files (job.md, evidence.md).
- No slides were added, removed or moved: still 70, with the same mapping as work-r1.

## Findings

| ID | Disposition | What was done |
|---|---|---|
| F01 | fixed | **S132 Message (H, M):** "The unnormalized posterior can be evaluated pointwise; obtaining the normalized density still requires the integral $Z$." **S72 closing sentence (H, M):** "…whose unnormalized density is available pointwise; the estimator never needs its normalizing integral, and the numerical value of that integral computed later is used only to validate the estimate." The main slides are unchanged. |
| F02 | fixed | **S63b Message (H, M):** "For $f \ge 0$ with $0 \lt \mu = \mathbb E_p[f] \lt \infty$, the oracle proposal $q^* = fp/\mu$ makes every contribution equal to $\mu$, so its sample mean has zero variance for every $n$; evaluating the oracle weights still requires $\mu$, the unknown answer." The conditions now match the main slide and the explanation. |
| F03 | taken | **S109a (H):** "The first synthesis slide" → "The closing comparison". **Prerequisites (H, M):** the prob08 entry now reads "the standard normal, used as the prior in the Bayesian unknown-$Z$ example". The pathwise step in S77's proof was not touched. |
| F04 | taken | **S132 citation (D)** split into two lines: "Our logistic-normal toy; curves: `gen/p9f_unknown_z.py`" / "Stan User's Guide, v2.40: posterior normalization; logistic regression". The version comes from evidence 2026-11-18 E07. Exact section titles and links stay in the H/M Sources. Citation type size is unchanged. |

## Plan issues

None.

## Unsourced facts

None.

## Checks

- lint-deck: ok.
- outline-lint: 0 stale pointers. No deck line numbers shifted, so OUTLINE.md is unchanged.
- Narrow check of H at 430 px: no overflow.
- Render at -r 60: page 47 (S132) shows the citation on two intact lines with no overlap. Pages 46 and 48 were re-rendered; their slide source is unchanged.
