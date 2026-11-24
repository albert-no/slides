# Round 1 review

- Job: `2026-11-24-opt01-opt02-polish`
- Baseline: `9fdba016e02405c96fa9d8a9c7224f4612361d16`
- Reviewed commit: `2244aea04c44369d216d928c9e70b5341cddca2e`
- Branch: `2026-11-24-opt01-opt02-polish`
- Verdict: **revise** — two blocking companion-note findings, F01–F02.
- Next round: 2 of 2. No main-deck redesign or new plan version is needed.

## What matters

The main decks answer Albert's comments well. Keep the larger diagrams, the one retained SVD illustration, the two explicit optimality obligations, and the three-frame upper-model build. The distinction between full-sequence gradient convergence and a best-iterate rate is correct on the main slides. The spectral, convex and strongly-convex proof sequences remain intact.

Two note issues prevent approval: the new elementary/summability equations require horizontal scrolling at a narrow viewport, and two short summaries lose the nonconvex qualifiers. Fix those without reopening the main argument. The remaining two findings are small and nonblocking.

## Request coverage

Pages are baseline → reviewed; IDs are deck-qualified. Deleted IDs have no new main page.

| Comment | Status | Location / result |
|---|---|---|
| C01 | Done | opt01 S80, 4→4: readable spacing between the statements. |
| C02 | Done | opt01 S12→S12a/S12b, 5→5–6: definition, then a self-contained example. |
| C03 | Done | opt01 S31, 15→16: explicitly Euclidean/L2 geometry. |
| C04 | Done | opt01 S40, 23→24: enlarged diagram labels, legible at final size. |
| C05 | Done | opt01 S44, 28→29: generic conceptual construction, larger labels, positive-singular-value restriction. |
| C06 | Done | opt01 S45–S49, 29–33: removed from the main triplet; original archive retained. |
| C07 | Done | opt01 S50, 34→30: retained standalone illustration and 50=45+5 energy interpretation. |
| C08 | Done | opt01 S51, 35→31: general distinction, with the symmetric-PSD exception. |
| C09 | Done | opt01 S82/S83, 43–44: worked example removed. |
| C10 | Done | opt01 S91, 46→40: puzzling plot replaced by lower bound for all competitors + an attaining candidate. |
| C11 | Done | opt01 S101, 60→54: proof explicitly beyond lecture scope on-slide and in both notes; theorem retained. |
| C12 | Done | opt01 S102/S122 removed; S103, 64→57: general retained-energy ratio, not another worked exercise. S121 candidate-error identity remains. |
| C13 | Done | opt01 new S124, page58: LLM weight compression, parameter-saving condition and quality caveat. |
| C14 | Done | opt02 running-example pages removed; S65/S110 use generic concept/rate pictures. Numerical provenance is subordinate note detail, not a running lecture exercise. |
| C15 | Done | opt02 S34→S34a/b/c, 12→11–13: manual visual build, each static page understandable; verbal descriptions supplied. |
| C16 | Partial | opt02 S33/S36/S37, 11/13/14→10/14/15: elementary model minimization given the stated lemma; integral proof optional only. Note reflow remains, F01. |
| C17 | Partial | opt02 new S141, page21, and S89/S91/S92/S93/S137/recap: full-sequence limit and best-iterate rate correctly distinguished on-slide. Note reflow/summary consistency remain, F01–F02. |
| C18 | Done | opt02 S136, page24: removed from main; unique counterexample retained only as optional S93 note detail. |
| C19 | Done | opt02 S96/S116, 30/41→28/39: neutral theorem headings; G&G for exact modern bounds, Nesterov as earlier treatment, no unverified first-discovery claim. |
| C20 | Done | opt02 S126, page47: removed from main. |

## Blocking findings

### 1. F01 — Reflow three GD note displays

- **Type:** design rule. **Blocking:** yes. DS §9 requires narrow-view math to be broken into steps, not horizontally scrolled or shrunk.
- **Where:** `courses/deepmath/opt02-convexity-gd/opt02-convexity-gd-note.html`: S36/page14 line219; S37/page15 line235; S141/page21 line314. Matching Markdown: `courses/deepmath/opt02-convexity-gd/opt02-convexity-gd-note.md`, S36 line267, S37 display in Section15, S141 line402.
- **Problem:** at an actual 430-wide viewport, S36 and S141 have display widths 527 and 550 inside 367 available. Their right-hand content is offscreen. S37 is marginal (368 inside367) but also produces a visible horizontal scrollbar. A non-overflowing article/document does not make the internal math scrollers pass.
- **Precise instruction:** S36: separate the definition of Q_x from f(y)≤Q_x(y), put “for every y” in prose, and break the model definition at a natural algebraic boundary if necessary. S141: separate the finite budget, summability and limit conclusion; for example define B=2L(f(x_0)-f_low), then show sum ||grad f(x_t)||²≤B<∞ and the limit on separate lines. S37: add a natural algebraic break so the completing-square derivation has width margin rather than a scrollbar. Preserve every term and the explanation of why the square vanishes at y=x−g/L. Mirror the mathematical grouping in Markdown. Do not shrink type, clip content, or merely hide the scrollbars.
- **Why:** these are the two new explanations Albert specifically requested; a reader must see each complete mathematical step.
- **Acceptance:** render the three articles at ~430 and desktop width, inspect them, and confirm no display requires horizontal scrolling. Check their neighbouring articles for collateral effects.

### 2. F02 — Keep the best-iterate rate and full-sequence limit distinct in short notes

- **Type:** fact / unmet request C17. **Blocking:** yes. DS §9 also requires qualifiers in the Message, not only in the longer explanation.
- **Where:** S137/page23, `courses/deepmath/opt02-convexity-gd/opt02-convexity-gd-note.html` line347 and `courses/deepmath/opt02-convexity-gd/opt02-convexity-gd-note.md` line450; S123/page43, same files lines670 and931 respectively.
- **Current → replacement:**
  1. S137 Message: “the gradient norm itself falls only like O(1/sqrt T) ... costs on the order of ...” → “The smallest gradient norm among the first T iterates is bounded by O(1/sqrt T); O(1/epsilon²) steps suffice to find one with norm at most epsilon.” Use the files' mathematical notation. The existing explanation already gives the correct explicit bound; retain it.
  2. S123 closing comparison: replace “Both the iterates and the function values converge to the optimum, the unique minimizer. This is much more than the nonconvex conclusion, which only finds a point with small gradient.” with “The iterates converge to the unique minimizer x*, and their function values converge to f*. Under the nonconvex assumptions, every gradient norm tends to zero, but convergence of x_t to a minimizer is not guaranteed.”
- **Why:** “only like” can sound like an exact or last-iterate rate; “only finds a point” omits the newly proved whole-sequence statement. Neither is the intended distinction. The main slides are already correct and need no change.

## Smaller findings — nonblocking

### 3. F03 — Include the zero-residual case

- **Type:** fact. **Blocking:** no; optional-note edge case, not the taught example or theorem.
- **Where:** opt01 S123/page59, `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank-note.html` line831 and `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank-note.md` line1083.
- **Current → new:** “the two norms agree only when the residual has a single nonzero singular value” → “the two norms agree exactly when the residual has at most one nonzero singular value.”
- **Why:** the zero matrix also has equal spectral and Frobenius norms. The displayed example and bounds need no change.

### 4. F04 — Student-note presentation cleanup [judgment]

- **Type:** preference. **Blocking:** no; slides decides. The mathematical descriptions are sufficient without the images, so this does not independently hold up approval.
- **Where:** `courses/deepmath/opt02-convexity-gd/opt02-convexity-gd-note.md`: S34a/b/c pages11–13, lines197–252; S36/page14 line271; S65/page38 line807; S116/page39 line841.
- **Instruction:** consider replacing “The caption reads” wrappers with the takeaway itself or removing the repeated sentence. Keep the verbal curve descriptions and analytic parameters; implementation viewBox/coordinate transforms at line252 can stay in the generator rather than student prose. “stated on section 10” → “stated in Section 10”; “proof on the following slides” → “proof in Sections 40–43.”
- **Why:** the Markdown edition reads more naturally as a standalone lesson rather than a description of slide production. Do not rewrite unaffected sections or remove figure provenance.

## Sources and flagged facts

- Added E10 to the living `evidence.md`: checked Golub–Van Loan, Matrix Computations, 4th ed., §8.6.3, printed pp488–489. It supports the S44 note's numerical-computation caveat. The chapter 8 citation is valid; a more precise section pointer is optional. Refresh the tracked evidence copy on the next push.
- Removing the unverified MML editorial remark is accepted. The retained PSD qualifier is supported directly by the algebra and registered sources.
- Confirmed the full-gradient claim by summability under global L-smoothness, a finite lower bound and step 1/L. No attained objective minimum is needed, and no iterate/minimizer convergence or last-iterate rate is claimed by that argument.
- Source attribution does not claim historical priority that the evidence has not established.
- **Plan issues / changes:** none. F01–F02 implement existing readability and consistency requirements; no plan-v2.

## Checks and review scope

- Reviewed exact git diff and archived commit, not a working tree. Main/HTML-note/Markdown ID sequences match, with 61 opt01 and 48 opt02 entries; IDs unique and both Markdown files ASCII.
- Rendered both complete main decks and inspected changed pages plus neighbours. Enlarged opt01 diagrams, spacing/split, scope labels, energy/LLM pages and GD builds/rate pictures are legible; no clipping or footer loss observed in the inspected pages.
- Inspected both HTML notes at 430 and 1280. No KaTeX errors; no article/document horizontal overflow. Opt01 displays fit. Opt02 internal display scrolling is recorded in F01, including S37's marginal overflow found by visual inspection.
- Core spectral EYM and convex/strongly-convex main proof blocks are byte-identical to baseline. All four archive triplets are byte-identical. Removed unique material is in the specified surviving note details.
- Main lint passes with no errors/type warnings; accessible-Markdown lint has no errors and one existing introductory visual-reference warning per deck. Both local figure generators' checks pass. Root/course/backup outline counts and semantic pointers checked; documentation index checks pass.
- Whole-repository outline lint in this extraction has one unrelated pre-existing absolute-path error in the unchanged trustworthy-ai OUTLINE and five unrelated ambiguity warnings. These are not introduced by this job and are not correction scope.

## Round 2 work order

Resolve F01–F02; report dispositions for F03–F04. Limit changes to affected companions, any consequent outline metadata, and the job record. Preserve the 61/48 main decks, proof content, four archives, duration and scope. Refresh living job/evidence copies and copy this review unchanged into the tracked record. Send work-r2 with an exact pushed SHA and per-finding disposition.

Keep PR #80's existing head branch at the baseline while this revision is unapproved. No new PR, merge, force push or main push. Round 2 review will cover changed note sections and neighbours, plus consistency checks; unresolved blocking findings at the round limit go to Albert.
