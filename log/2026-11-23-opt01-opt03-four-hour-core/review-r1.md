# Review r1 — four-hour SVD/GD core

- Job: 2026-11-23-opt01-opt03-four-hour-core
- Reviewed commit: **19e8acfdcb736b6232d820324c0bb5d64cfe6259**
- Baseline: 99cf2a220a92c83e938167c05745af15d9bafe13
- ID-only commit: 01ba79c7b18bb7538c0c8bcd34f6141dd604d075
- Round: 1 of 3
- Verdict: **revise**

## What matters

1. The restructure and central proofs work. Keep the 150+90-minute split, the single SVD example, the distinction between achievability and optimality, and the shared GD proof. The main nonconvex theorem is correctly stated; several shorter note summaries drop its lower-bound assumption.
2. The companions are not finished: nine HTML articles hide long equations behind horizontal scrolling, and both Markdown editions reproduce instructor descriptions of slide layout instead of consistently standing alone for the blind reader.
3. Finish the small mathematical/source corrections below, enlarge the final GD mechanism labels, and remove stale deferred-topic descriptions from the course index. No new lecture content or full redesign is requested.

## Coverage of Albert's requests

| Request | Status at reviewed commit |
|---|---|
| C01 | Done: 2026 course-path update present. |
| C02 | Done: prob09 120 minutes, opt01 150 and opt03 90; week 15 remains final. |
| C03 | Done structurally: two main decks, 68 and 51 slides, paired HTML/Markdown notes. Companion acceptance remains open under F01/F08. prob09 files unchanged. |
| C04 | Done: “The Optimization Half” and the old four-lecture opening are archive-only. |
| C05 | Done in substance: norms, SVD, spectral EYM proof, Frobenius theorem/error interpretation, full Frobenius proof in notes. Corrections F03–F06 remain. |
| C06 | Done preservation: 119/134 original slides and original notes retained; opt02/04 untouched and backup-only. Index wording needs F09. |
| C07 | Done: no probability pruning or future lec renumbering. |
| C08 | Done in substance: one fixed step 1/L, three guarantees, no alternate algorithm/proof machinery required. F02 corrects note overclaims. |
| C09 | Done on main slides: strong convexity kept; co-coercivity/PL not needed; convex rate called sublinear; nonconvex local-optimum claim explicitly rejected with a counterexample. F02/F07 remain. |
| C10 | Done: opt01/opt03 are the active decks, remaining material preserved in backups. F09 finishes navigation. |
| C11 | Approved outline implemented without changing the argument or total duration. This review is not PR approval or a merge order. |

## Findings and changes required

Paths and line numbers below refer to the reviewed commit. Apply content corrections to both HTML and Markdown notes; do not change the frozen full-original backups. `[judgment]` items need slides' contextual handling, not a context-free mechanical worker.

### 1. F01 — Long note equations still require horizontal scrolling
**Type:** design rule. **Blocking:** yes. **Rule:** DS §9 requires long display math broken into steps at about 430px, not hidden in a scrolling container.

- `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank-note.html`: S82/p43 (article starts line 573), S83/p44 (589), S90/p45 (605), S101/p60 (823), S102/p63 (877).
- `courses/deepmath/opt03-convexity-gd/opt03-convexity-gd-note.html`: S105/p36 (523), S106/p37 (539), S138/p42 (615), S123/p45 (665).

At an actual 430px viewport, for example, opt01 S82 has a 659px equation inside 332px, S90 681px inside 293px, and S102 743px inside 332px; opt03 S106 is 523px inside 367px. Both files' line 12 adds `overflow-x:auto`; this contains the page but does not make the derivation readable without horizontal scrolling.

**Fix [judgment]:** break these displays into semantic steps/short aligned rows; put quantifiers or explanatory clauses into prose where useful. Preserve the complete algebra at unchanged type size. Do not use horizontal scrolling, clipping or scaling as the acceptance fix. Test all articles at 430px after the edit, and check the changed articles at desktop width too. Corresponding Markdown sections should preserve the same mathematical steps.

### 2. F02 — Restore the lower bound in nonconvex summaries
**Type:** fact. **Blocking:** yes. **Evidence:** E06, E12.

`courses/deepmath/opt03-convexity-gd/opt03-convexity-gd-note.html`:
- S01/p1, line 52: “Smoothness alone gives approximate stationarity” → “Smoothness and a lower bound on f give approximate stationarity”. Also say “an attained minimum” in the convex summary.
- S27/p7, line 116: “The first guarantee ... uses smoothness alone” → “The nonconvex guarantee uses smoothness and boundedness below, but not convexity.”
- S135/p19, line 275: “Part 3 uses smoothness alone” → “Part 3 uses smoothness and boundedness below”. Keep the best-gradient, not minimum, distinction.

Mirror in `courses/deepmath/opt03-convexity-gd/opt03-convexity-gd-note.md`, lines 20, 113, 331. Do **not** replace legitimate “smoothness alone” statements about the one-step descent inequality (e.g. S98).

**Reason:** f(x)=x is smooth but has constant nonzero gradient. The correct assumption on the theorem slide must survive into the short teaching summaries.

### 3. F03 — Energy is the squared Frobenius norm
**Type:** fact. **Blocking:** yes. **Evidence:** E03/E08.

- `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank.html`, S73/p39, line 986: “||A||_F is total energy” → “||A||_F^2 is total energy”. The theorem display is already correct.
- `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank-note.html`, S73/p39, lines 524 and 528, and `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank-note.md`, lines 610 and 616: make the same square/root distinction in the contrast and definition sentences.
- In both note editions, S72/p18 Message: “The Frobenius norm adds up every squared entry” → “The squared Frobenius norm adds up every squared entry”. Keep the displayed norm definition with its square root.

**Reason:** the lecture explicitly distinguishes the two errors and interprets 45/50 as energy; these sentences currently contradict that distinction.

### 4. F04 — Two norm claims need qualification
**Type:** fact. **Blocking:** yes. **Evidence:** E10/E12.

1. `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank.html`, S28/p12, line 408: “Only l2 is length” → “l2 gives Euclidean length” (retain the (1,1) numerical contrast). In `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank-note.html` line 174 and `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank-note.md` line 155, replace “Only l2 is geometric length” consistently. Other norms also define lengths/metrics.
2. `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank-note.html`, S27/p11, line 164, and `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank-note.md`, line 143: “Squared norms ... are smooth” → “Squared Euclidean and Frobenius norms are smooth objectives”. General squared norms need not be differentiable.

### 5. F05 — Qualify SVD construction and repair the rank justification
**Type:** fact. **Blocking:** yes. **Evidence:** E02/E12.

1. `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank.html`, S38/p21, line 615: add “for sigma_i>0” to `u_i=Av_i/sigma_i`. The theorem explicitly allows zero singular values. Keep the existing orthonormal-completion explanation in the notes; update their slide-description sentence too (`courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank-note.html` line 285; `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank-note.md` line 276).
2. `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank-note.html`, S42/p27, line 364, and `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank-note.md`, line 386: “thin factors are not orthogonal matrices” → “factors have orthonormal columns but need not be square orthogonal matrices”. In the full-rank square example, they are square orthogonal matrices. The main slide's explicit r<m example can stay.
3. `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank-note.html`, S81/p42, line 562, and `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank-note.md`, line 662: replace “The layers ... are linearly independent, so A_k has rank exactly k” with the valid reason: `A_k v_i = sigma_i u_i` for i<=k gives k independent outputs, and its range is contained in their span. Thus rank is k. Independence of rank-one matrices alone is insufficient.
4. `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank-note.html`, S123/p66, line 931, and `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank-note.md`, line 1182: replace the categorical “both break the closed form: the minimizer is no longer obtained by truncating an SVD” with “The unweighted EYM guarantee does not apply to general weighted or missing-entry objectives; truncating the given matrix's SVD is not generally guaranteed to solve them.”

### 6. F06 — Close the reported source gaps, not with unresolved disclaimers
**Type:** fact. **Blocking:** yes.

1. `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank.html`, S28/p12, citation following line 408, and both matching note articles: replace “standard definition (not in the cited text)” / “not found ... flagged” with **Boyd & Vandenberghe, Convex Optimization (CUP 2004), Appendix A.1.3, p.635**, official URL in E10. This supplies the already-required infinity norm; no extra topic.
2. `[judgment]` `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank-note.html`, S91/p46, lines 640–643, and `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank-note.md`, lines 778–782: remove the optional **Proposition 7.4 Frobenius uniqueness** paragraph and its “not independently sourced” sentence from the current-course notes. It is outside the core, the sketch does not justify the full equality characterization, and its indexing does not cover the stated k=0 setup. It remains preserved in the full backup. Keep the directly checked spectral nonuniqueness counterexample if useful.
3. `[judgment]` `courses/deepmath/opt03-convexity-gd/opt03-convexity-gd-note.html`, S27/p7, line 119, and `courses/deepmath/opt03-convexity-gd/opt03-convexity-gd-note.md`, line 117: preferably omit the optional smallest-L/Hessian sentence. If retained, cite E11 and qualify it as the least **nonnegative** Lipschitz bound, finite when a global bound exists; choose a positive L for GD. Retain the direct L=4 calculation, not a new Hessian prerequisite.
4. `courses/deepmath/opt03-convexity-gd/opt03-convexity-gd-note.html`, S80/p4, line 80, and `courses/deepmath/opt03-convexity-gd/opt03-convexity-gd-note.md`, line 63: replace “Problem setup: plan-v1 shared notation” with the public E06 problem/algorithm source. A job plan is not teaching evidence. Keep the curve labelled our illustration.

### 7. F07 — The final GD mechanism labels are below body size
**Type:** design rule. **Blocking:** yes. **Rule:** DS §8 primary diagram labels.

`courses/deepmath/opt03-convexity-gd/opt03-convexity-gd.html`, S140/p50, lines 877–899. The diagram's descent/distance/tangent boxes and the two outcomes use the native small diagram-box type, visibly much smaller than the body-size table below. These labels carry the argument; they are not non-crucial annotations. The native component exception does not make essential mechanism labels exempt from §8.

**Fix [judgment]:** use body-size primary labels throughout this diagram, simplifying or rearranging the flow if needed. Keep the explicit three answers below. No shared design-system change. Render the whole slide at 1280x720 and check that all labels and formulas fit.

### 8. F08 — Make the Markdown notes student-facing and standalone
**Type:** design rule. **Blocking:** yes. **Rule:** `courses/deepmath/OUTLINE.md` accessible-edition contract (lines 16–23), DS §9, plan §4.

- `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank-note.md`, all 68 sections: e.g. S80/p4 line 51 (“The slide shows ... boxed matrices”); S38/p21 line 276 (“The theorem card ... last card line ... muted line”); S99/p59 describes rows rather than presenting the recap directly.
- `courses/deepmath/opt03-convexity-gd/opt03-convexity-gd-note.md`, all 51 sections: e.g. S81/p8 line 129 (“The algorithm box has three lines”), S106/p37 line 727 (“The highlight box on the slide is the takeaway to say aloud”), S140/p50 line 1012 (“The flow on the slide”).

**Fix [judgment]:** retain IDs/order, every mathematical statement, proof, table value, source and useful verbal figure description, but rewrite layout/speaking narration as direct exposition. “The display computes X” → compute X; “the muted line warns Y” → state Y; references to a slide/box/column as evidence → the relevant formula or explanation. Do not leave a “see the slide” dependency. Describe geometry/encodings in words where that supplies information, not an instruction to look at a visual. Cross-references within the standalone document can name its section and the content. Linearize the existing tables/recap chain explicitly. The HTML instructor note may retain instructor-facing narration; agreement means the same content, not identical sentences.

**Reason:** these editions are for a blind student reading linearly through speech/braille, not for someone presenting the slide deck. The current files are largely literal instructor-note transcriptions despite claiming a standalone student edition.

### 9. F09 — The course overview still advertises deferred topics as active
**Type:** unmet request. **Blocking:** yes. **Requests:** C06/C08/C10.

`courses/deepmath/OUTLINE.md`, deck-plan table rows 10 and 12 (lines 45 and 47): the opt01 main path is still described with pseudo-inverse, nuclear norms and Netflix; opt03 still advertises co-coercivity and PL. The status cells have new counts, so these rows read as the current syllabus.

**Fix:** describe opt01 as rank/nullity, vector/spectral/Frobenius norms, SVD and EYM; describe opt03 as fixed-step GD, smoothness/descent, nonconvex stationarity, convex function-gap and strongly convex geometric rates. Keep deferred topics in the existing full-edition/backup descriptions. No renumbering.

## Nonblocking preference

10. **F10 — Optional note-scope cleanup [judgment].** Type: preference; blocking: no. `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank.html`, S101/p60: “the proof needs min–max (Weyl) inequalities” → “the proof in the note uses min–max/Weyl inequalities” avoids implying every proof needs that route. In the matching HTML/Markdown note, consider leaving the nuclear-norm/general-Mirsky extension in the full backup only; retain the complete Frobenius proof and its prerequisites. No extra theorem is needed for the four-hour core. Slides decides.

## Decisions on work-r1 plan issues

- Infinity norm: E10 supplies the missing citation (F06). This completes provenance for the existing required definition, not a scope expansion.
- Symmetric versus PSD: **accept the PSD correction** and the note recording the source discrepancy. The worked nonsymmetric example is correct.
- Optional unsourced facts: disposition in F06; no need to expand the lecture to teach uniqueness or Hessian theory.
- R^n versus R^d: accept; consistent local notation.
- Cornell index/lower-bound specialization: accept the exact T-gradient version. The telescoping proof justifies it without assuming an attained lower bound.
- Rank-at-most-k: accept; the proof covers every such competitor.
- Named theorems, two-iteration example, tables instead of cards, compact-SVD subscript r, and blank space below concise recap/scope slides: accepted. No argument/time change; plan-v1 remains the execution plan. Evidence additions E10–E13 are source completions and review calculations, not new required lecture material.

## Review checks completed

- Read the exact candidate through git and extracted it with git archive; never reviewed a moving working tree.
- Read all 119 main slides and all 119 paired HTML articles. Compared Markdown section content with HTML, accounting for ASCII and LaTeX spelling/linearization differences; substantive content is synchronized, but the accessibility style fails F08.
- Rendered both complete main decks in Chromium, inspected every page, and inspected suspect pages at full 1280x720. No page-edge clipping or footer overlap found. F07 is the essential-label size issue.
- KaTeX errors: zero in both mains and both current HTML notes. Independent lint: both mains clean. These do not override the findings above.
- Tested all current note articles at actual 430px viewport: the nine internal horizontal-scroll failures are listed in F01. No other article-level horizontal overrun found in that check.
- IDs/orders: main slides = HTML articles = Markdown sections, 68/68/68 and 51/51/51. Markdown files are ASCII-only.
- Independently checked the ID-only commit by removing only its IDs/markers: all six files match the parent. Full backups differ from the prepared/ID-tagged originals only by archive identification and necessary paths/navigation; all original slide bodies are retained. Baseline substantive note paragraphs/equations and Markdown content are preserved, with path adjustments. Archive preservation is not scientific reapproval of legacy claims.
- Local resources resolve for both mains, both HTML notes and all four backup HTMLs. No prob01–prob09, opt02/opt04 content, exam, tex, reference or shared-script changes in the baseline-to-candidate diff.
- Recomputed the examples, checked the spectral EYM and Frobenius-note proofs, and checked all three GD proofs/indices/constants against E02–E07. Ran both local figure generators and checked their algebraic invariants (E13).
- Received plan/requests/evidence copies match the announced working files exactly before this review's evidence append. Scope and counts agree across the detailed outlines, subject to the stale overview descriptions in F09.

## Next handoff

Address F01–F09; F10 is optional. Push `work-r2.md` with the exact new SHA, each finding's disposition, changed-slide/article list, render checks and any new page/ID mappings. Preserve 150+90 minutes; splits are allowed if needed for legibility. Refresh the living job/evidence copies and copy this review unchanged. Next review rechecks changed slides/articles and neighbours, not the full unchanged deck. Do not open the PR yet.
