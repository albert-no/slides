# work-r2 — 2026-11-24-opt01-opt02-polish

Responds to review-r1 (reviewed 2244aea). Content commit `8e2964c`; this log commit follows it on branch `2026-11-24-opt01-opt02-polish`. Changes are limited to the four companion notes and the job record. Main decks (61 / 48), proof content, archives and outlines are unchanged. PR #80's head branch remains at the baseline.

## Dispositions
| Finding | Disposition | Change |
|---|---|---|
| F01 (blocking) | Fixed | opt02 note, HTML and MD. **S36:** the model definition $Q_x(y)=\dots$ is now its own display. A prose line follows, "The descent lemma says that for every candidate $y$,", and then $f(y)\le Q_x(y)$ on its own line. **S37:** the aligned derivation now has four lines: the bracket breaks before $+\tfrac2L\langle g,y-x\rangle$, and the result breaks before $+\tfrac L2\|y-(x-g/L)\|^2$. Every term is kept. "takes two lines" became "takes two steps". The text explaining why the square vanishes at $y=x-g/L$ is unchanged. **S141:** defines $B=2L(f(x_0)-f_{\text{low}})$, then gives three separate displays: the partial-sum bound $\le B$ for every $T$, the summability bound $\sum_{t\ge0}\dots\le B<\infty$, and, after "Therefore", $\|\nabla f(x_t)\|\to0$. The MD note mirrors the same grouping. |
| F02 (blocking) | Fixed | **S137 Message** (HTML + MD): "The smallest gradient norm among the first $T$ iterates, $\min_{0\le t\le T-1}\|\nabla f(x_t)\|$, is bounded by $O(1/\sqrt T)$; $O(1/\varepsilon^2)$ steps suffice to find an iterate with $\|\nabla f(x_t)\|\le\varepsilon$." The explanation keeps the explicit bound. **S123 closing** (HTML + MD) now uses the review's replacement text verbatim, with $x^\star$, $f^\star$ and $x_t$ in math. |
| F03 | Taken | opt01 S123 note, HTML and MD: "agree exactly when the residual has at most one nonzero singular value". |
| F04 | Taken, MD only | Removed the four "The caption reads: …" sentences (S34a, S34b, S34c, S65); each repeated the article's Message. S34c Details: "Plot frame" with viewBox and transforms became "Checks", which names what `figs/gd_model_build.py` asserts. The parameters, verbal curve descriptions and provenance stay. S36: "stated on section 10" became "stated in Section 10". S116: "proof on the following slides" became "proof in Sections 40-43" (S138, S139, S122, S123 = deck pages 40–43). The HTML note keeps its caption lines, because it is the speaker companion for the slides. |

## Checks
- **Display overflow:** tested by injecting a check of `.katex-display` scrollWidth against clientWidth. Chromium's minimum window is 500 px, so the page is pinned with `html{width:430px}`.
  - The test reproduces the review's failure on 2244aea: S36 527 vs 382 and S141 550 vs 382.
  - On this commit, both notes have no overflowing display at 430 or 1280.
  - Margin check at 360 px: the widest changed display is the S36 model definition at 330 px, which fits the review's 367 px. S37 no longer appears at 360.
  - Displays that overflow below 400 px (S10, S15, S64, S101, S106) are unchanged baseline articles, outside the 430 target.
- **Visual check:** rendered at 430 and inspected S36, S37, S141, S137 and S123. No scrollbars, every term visible, no collateral reflow.
- **KaTeX:** 0 errors in both HTML notes.
- **Lint:** `lint-deck.py` reports ok on both HTML notes. `lint-accessible-md.py` gives one baseline warning per MD note and no errors. The MD notes are ASCII-only.
- **IDs:** deck, HTML note and MD note ID sequences are identical (61 / 48).
- **Outlines:** `outline-lint.py` reports 0 stale pointers, plus the 5 pre-existing warnings.

## Record
- Copied review-r1.md unchanged. Refreshed job.md, requests.md and evidence.md, including E10 (Golub–Van Loan §8.6.3). This resolves the ch. 8 flag from work-r1.

## Plan issues
None.
