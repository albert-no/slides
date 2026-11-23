# work-r1 — 2026-11-23-opt01-opt03-four-hour-core

Round 1 of 3. Executes `plan-v1.md`.

## 1. Branch and commits

- Branch: `2026-11-23-opt01-opt03-four-hour-core`, from baseline `99cf2a220a92c83e938167c05745af15d9bafe13`.
- Job files copied unchanged: `b3040aa`.
- Preparation, structural only (plan §2 item 2): `47e2a47` opt01 notes and `26b9f95` opt03 notes, one article per baseline slide with no wording change.
- ID-only commit: `01ba79c`. It adds `data-slide-id` S01–S119 (opt01) and S01–S134 (opt03) to decks, HTML notes and Markdown notes and changes nothing else.
- Archive: `b28bd07`. Full decks and notes are copied to `<deck>/backup/<deck>-full*`; only wrappers changed (see §3).
- Content:
  - `c7e27da`: mechanical reorder plus structural slides.
  - Package commits `4a36be3` (P1), `ef4f941` (P2), `7466ab6` (P3), `69d5dc1` (P4a–c), `873bc50` (P4d–f), each merged.
  - Integration commits `733c9ce` (opt01) and `a3fb604` (opt03).
  - Outlines: `d8a41b4`.
  - Render fixes: `391acbe`.
- Review target: the SHA in the pointer message, which is the commit that adds this report.

## 2. Package summary

Work was split into five worker packages, each in its own worktree with a disjoint region and its own CSS prefix:
- w1 = P1a+P1b (`o1a`)
- w2 = P2 (`o1b`)
- w3 = P3a+P3b (`o1c`)
- w4 = P4a–c (`o3a`)
- w5 = P4d–f (`o3b`)

I did the integration: Contents, dividers, `N / M`, front matter, reference lists, cross-references and outlines.

**Result:**
- opt01 main has 68 slides (target ≈68): Opening 2, P1a 7, P1b 9, P2 22, P3a 21, P3b 6, Closing 1.
- opt03 main has 51 slides (target ≈51): Opening 2, P4a 7, P4b 9, P4c 7, P4d 12, P4e 10, P4f 3, Closing 1.
- Every main slide has a paired note article in both the HTML and the Markdown note, in deck order.

### Integration decisions (routine)
- **Theorem numbering.** Packages renumbered independently and left gaps; for example, P2 cited "Theorem 8, Step 1". Both mains and both notes now cite theorems **by name only**: "Theorem (SVD)", "Theorem (Eckart–Young–Mirsky, spectral)", "Lemma (descent lemma)" and so on. Neither main shows a theorem number.
- **Notation.** The compact SVD is written `U_r, Σ_r, V_r` everywhere; front matter no longer uses `U_c`. The orthogonal matrix in P1b is `Q`. opt03 uses `R^n`.
- **Note front matter and reference lists.** Both were rewritten for the new mains. Where a reference annotation still names a legacy theorem or section number, a disclaimer says that number refers to the full edition's note in `backup/`.
- **w3 generator path.** w3 created `gen/o1c_planes.py`; plan §6 allows only `figs/`, so I moved it to `figs/o1c_planes.py`.
- **Wilkinson URL.** Repaired to the E03 form (`.../3-5-lowrank.html`) in the main opt01 note. The archived full note keeps the baseline URL unchanged (archival integrity).

### Deviations (DESIGN_SYSTEM authority; argument, scope and facts unchanged)
- **opt01 S33:** "Claim" for square `Q`, as the plan specifies; the note remarks that only `QᵀQ = I` is used.
- **opt01 S66:** the input circle is drawn at 3× and labelled "unit circle (×3)"; the ellipse is to scale.
- **opt01 S36:** the recall card became an inline recall line plus a math block (vertical budget).
- **opt01 S73:** one contrast line instead of grid-2 cards; `Σa_ij²` was added to the theorem display.
- **opt01 S74:** retitled to describe the invariance proof. The trace proof moved to the note.
- **opt01 S101:** the Frobenius EYM is stated; its proof (Courant–Fischer, Weyl) is in the S101 note article, as the plan specifies.
- **opt01 S123, S117:** some empty space below the flow diagrams (Priority 3). I accepted it for scope and recap slides.
- **opt03 S84:** two iterations instead of four, with a descent-bound column added.
- **opt03 S14:** one-slide recall with no figure.
- **opt03 main:** the step range `α∈(0,2/L)`, the "global minimum" assumption and the exercise are removed under the plan's "step 1/L only" rule. All three remain in the backup.
- **opt03 S131:** a 3-row table instead of three cards, so each formula stays on one line at full size.
- **opt03 S10, S15:** reuse the chord and tangent plots from baseline S11/S16, relabelled.
- **Table headers:** `text-transform:none` on table headers that contain math, in opt03 S84 and the `o3b` tables, because the theme uppercases `th`.

### Plan issues (for slides-review; not decided by me)
1. **ℓ∞ definition (opt01 S28).** `‖x‖_∞ = max|x_i|` does not appear in E02 or E03. The slide cites it as "standard definition (not in the cited text)". Add a source or accept that wording.
2. **MML symmetric vs PSD (opt01 S51).** MML §4.5.3 says the eigendecomposition and the SVD of a symmetric matrix "are one and the same". That holds only for PSD matrices; in general the singular values are `|λ_i|`. The slide states the PSD version and the note records the discrepancy. Please confirm.
3. **Unsourced legacy facts kept in notes, not on slides:**
   - Prop. 7.4: Frobenius uniqueness iff `σ_k > σ_{k+1}` (opt01 S91 Sources, marked unsourced).
   - Smallest `L = sup‖∇²f‖₂` (opt03 S27 Details).
   Each needs a source or deletion; I did not repair either from memory.
4. **`R^d` vs `R^n` (opt03).** Plan rows and E04/E06 write `R^d`; the shared notation writes `R^n`. I used `R^n` throughout opt03.
5. **Cornell indexing (opt03 S89).** E06 states the nonconvex bound over `t∈{0..T}` with `f*` and `αL ≤ 1`. The slide states the `0..T−1` / `f_low` form obtained by summing `T` descent inequalities, as the plan prescribes. The cite says "stated for step α ≤ 1/L" and the note gives the reconciliation.
6. **Wilkinson EYM wording (opt01 S90).** Wilkinson states "rank-k B" and the slides say rank ≤ k. The on-page 2-norm proof covers ≤ k.

## 3. ID map

Statuses:
- `moved`: same title, new position.
- `moved, retitled` or `retained (retitled)`: the slide is in the main with a revised title or content.
- `archive-only`: the slide is only in `backup/<deck>-full.html` under the same ID.
- `new`: next free ID.

No ID was reused and no slide was split.

**Archives.** `backup/opt01-svd-lowrank-full.html` keeps 119 slides and `backup/opt03-convexity-gd-full.html` keeps 134, with ID order identical to the baseline. Compared with `01ba79c`, the only changes are:
- resource paths gain one `../` (CSS, KaTeX, `deck.js`, logo);
- the `<title>` and title pill say "Full / extended";
- each Markdown note gains a two-line "Archived edition" header.

Notes are byte-identical otherwise.

**Counts.**
- opt01: 64 retained + 4 new = 68 main; 64 + 55 archive-only = 119.
- opt03: 45 retained + 6 new = 51 main; 45 + 89 archive-only = 134.

## 4. Note mapping and loss check

**Structural preparation (`47e2a47`, `26b9f95`)** was kept separate from the semantic rewrite. The section-based notes were repartitioned into one article per baseline slide with no wording change. Loss check (strip tags, normalise whitespace, compare sentence by sentence, original → new):

| Note | HTML | Markdown |
|---|---|---|
| opt01 | 610 sentences/headings checked, 0 missing | 708 checked, 0 missing |
| opt03 | 778 checked, 0 missing | 843 checked, 0 missing |

The partition tables, duplicated paragraphs and legacy errors noted but not fixed are in the P0 worker reports, summarised in Appendix A.

**Semantic rewrite.** It happens only in the main notes; the full notes in `backup/` keep the structural edition verbatim. So every original subsection, equation and citation is still present in the archived full notes, and most also appear in the main notes.

**Pairing.** Every main slide has exactly one HTML `<article data-slide-id>` and one Markdown `### N. Title [Snn]` block with `BEGIN/END` markers, in deck order. Each article follows the prob09 pattern: message, explanation, details/sources. The ID-order check is in §9.

## 5. Pace

| Deck | Part | Slides | Minutes (plan) |
|---|---|---|---|
| opt01 | Opening (title, Contents) | 2 | in P1a |
| opt01 | P1a Why Low Rank? | 7 | 15 |
| opt01 | P1b Measuring Error | 9 | 25 |
| opt01 | P2 Reading an SVD | 22 | 45 |
| opt01 | P3a Best Low-Rank Approximation | 21 | 55 |
| opt01 | P3b Read the Answer, plus end slide | 7 | 10 |
| opt01 | **Total** | **68** | **150** |
| opt03 | Opening | 2 | in P4a |
| opt03 | P4a One Update | 7 | 15 |
| opt03 | P4b One Descent Inequality | 9 | 15 |
| opt03 | P4c Nonconvex Stationarity | 7 | 15 |
| opt03 | P4d Convex Optimality | 12 | 20 |
| opt03 | P4e Strongly Convex Geometric Decay | 10 | 20 |
| opt03 | P4f Three Guarantees, plus end slide | 4 | 5 |
| opt03 | **Total** | **51** | **90** |

Notes on the pace:
- Average pace is about 2.2 min/slide in opt01 and 1.8 min/slide in opt03.
- The longest stretches are the P2 hand-computed SVD and the P3a EYM witness proof, about 2.5 min/slide each, which includes questions.
- Several P3a slides are proof steps of a single argument.
- No topic was added beyond the plan's coverage table.
- Material that the plan's step-1/L-only rule removed from opt03 has no replacement slides.

## 6. Mathematical checks

Every item was recomputed by hand by the workers and re-checked by me unless stated otherwise.

**opt01, EYM:**
- The competitor quantifier is "for every `B` with rank `B ≤ k`" in both the spectral statement (S90) and the Frobenius statement (S101).
- The spectral proof is complete in the main deck: null space, subspace intersection, two-planes picture, witness `w`.
- The Frobenius statement is stated only, with the cite saying so. Its proof is in the S101 note article.

**opt01, spectral vs Frobenius:**
- S122: `diag(5,3,1)`, `k = 1` gives errors 3 vs √10.
- S83/S102: for the worked `A` both errors equal √5, because the residual has rank one.

**opt01, E08 worked matrix** `A = [[3,0],[4,5]]` (re-checked by me):
- `AᵀA = [[25,20],[20,25]]` has eigenvalues 45 and 5, so `σ = 3√5, √5`.
- `v₁ = (1,1)/√2`, `u₁ = (1,3)/√10`, and `A₁ = [[1.5,1.5],[4.5,4.5]]`.
- The residual squares sum to `2.25+2.25+0.25+0.25 = 5`.
- Energy kept is `45/50 = 90%`. The S103 bar is drawn at 810/900 px.

**opt01, S39 citation:**
- "MML eq. (4.64)" for the factor shapes comes from w2's reading of MML §4.5.
- I have not re-opened the PDF; this is the one cite I would ask the reviewer to spot-check.

**opt03:**

- **No PL or co-coercivity dependency in the main deck.** Both appear only as "not needed" in S96, S116 and the S140 table. The proofs use only the descent lemma, the tangent bound, the strong-convexity floor and the distance identity.
- **Nonconvex result (S89):**
  - `min_{0≤t≤T−1} ‖∇f(x_t)‖² ≤ 2L(f(x₀) − f_low)/T`.
  - Step `1/L`, with `f` bounded below by `f_low`.
  - The main deck stresses that this is a squared norm, a minimum over iterates, and convergence to a stationary point, not a minimum (S93, S136: `1 − cos x` stalls at `x = π`).
- **Convex result (S96, last iterate):** `f(x_T) − f* ≤ L‖x₀ − x*‖²/(2T)`, citing G&G Thm 3.4 (E04).
- **Strongly convex result (S116):** `‖x_T − x*‖² ≤ (1 − μ/L)^T ‖x₀ − x*‖²`.
  - The prefactor is 1 and `q = 1 − μ/L ∈ [0,1)`.
  - Step `1/L`, not `2/(μ+L)`.
  - Cites G&G Thm 3.6 and Remark 3.7 (E05).
- **E09 arithmetic, `f = 2x₁² + ½x₂²` with `L = 4`, `μ = 1`** (re-checked by me):
  - Iterates `(2,2) → (0,3/2) → (0,9/8)`, with `f = 10, 9/8, 81/128`.
  - Descent bounds are `3/2` and `27/32`; each value lies below its bound.
  - Squared distances are `8, 9/4, 81/64`, under `q^t D₀ = 8, 6, 9/2`.
  - S137 count: `T ≥ 80/ε²` for `L = 4`, `Δ = 10`. This is our derivation and is labelled as such.

## 7. Design and functional checks

- **`lint-deck.py`:** ok, with 0 errors and 0 warnings, on both mains and both backup full decks.
- **No font reduction:**
  - All package CSS stays inside its own prefix block.
  - The new `font-size` declarations are all 1.55rem, 1.7rem or 2.4rem, at or above the deck's body size.
  - opt03 has no new `font-size` declarations.
  - `lint-deck` reports 0 Priority-0 warnings.
- **`find-wordy.py`:** no flags on either main.
- **`find-dense.py`:** review prompts only.
  - opt01 flags L881 (S49), L907 (S51), L1333 (S122), L1345 (S123) and L1367 (S117). The words are mostly matrix entries or box labels.
  - opt03 flags L140 (S80), counted from overlay labels.
  - All of these were rendered (§8).
- **Page counters:** each deck has one `.slide-num` element, and `deck.js` fills it in (`N / 68`, `N / 51`), so no counter is duplicated.
- **Contents:** each deck has one Contents slide, and its entries match the region dividers.
- **Resource paths:**
  - Mains are unchanged.
  - Backups use `../../../../reference/…`; I rendered them and they load (§8).
- **TODOs:** none introduced in core content (`grep -c TODO` on the four main files = 0).
- **`outline-lint.py`:** 0 stale or missing pointers. Its 5 warnings are pre-existing ambiguous-basename warnings in `infotheory/` and `privacy/`.
- **Outlines** (`d8a41b4`):
  - `courses/deepmath/OUTLINE.md`:
    - deck-plan rows 10 and 12 now read 68 slides / 150 min and 51 slides / 90 min, with the full 119 / 134 in `backup/`;
    - opt02 and opt04 are marked backup-only;
    - new section tables for both mains plus full-edition subsections;
    - the count of accessible editions is now 17 files, about 19.4k lines.
  - New `courses/deepmath/backup/OUTLINE.md`.
  - Root `OUTLINE.md`: the deepmath line names the 2026 final block.
## 8. Renders

All renders use headless Chromium (`google-chrome` is absent) → PDF → `pdftoppm -r 60`.

**Workers.** Each worker rendered its own region and re-rendered the pages it fixed (w1–w5 reports).

**Integration audit.** A subagent read every page of both mains once: 68 + 51 pages. I then opened the flagged pages myself.

| Deck | Page / ID | Finding | Action |
|---|---|---|---|
| opt01 | 68 / S119 (end slide, baseline) | The divider touched the `∑_i` subscript | Divider `margin-top:28px`; re-rendered clean |
| opt03 | 11 / S33 | The line under the lemma card sat on the card edge | `margin-top:14px`; re-rendered clean |
| opt03 | 50 / S140 | Flow-box labels are smaller than body text | Kept. This is the canonical `.diagram-box` size (1.15rem, `deck.css`), not a reduction; lint gives no Priority-0 warning |
| opt03 | 4 / S80 | Last muted line ends about 6 px above the cite row; no overlap at -r 150 | Kept |
| opt01 | 67 / S117 | Lower ~45% empty under the recap flow | Kept (Priority 3; recap slide) |
| opt01 | 14 / S30 | Subagent reported an `e_1` label on the arrowhead | Not confirmed: I opened page 14 and found no such label |

**Clean pages:**
- The density-flagged slides (opt01 S49, S51, S122, S123, S117; opt03 S80) render without overflow.
- The plan §8 focus slides render with no overflow, no overlap and no raw TeX: vector/matrix norm labels, SVD factor shapes (S39), the worked factorization (S46–S49), the EYM witness proof (S85–S89), theorem assumption cards, rate formulas (S89, S96, S116) and the final summaries (S117, S131, S140).

**Backups:**
- I rendered both full decks (119 and 134 pages).
- I read the first, middle and last pages: opt01 pp. 1, 60, 119 and opt03 pp. 1, 67, 134.
- CSS, KaTeX, the title logo and the brand footer all load through the new `../../../../reference/` paths, and math renders.

## 9. Notes: width, agreement and Markdown

**Desktop.**
- Both HTML notes render to PDF with no KaTeX errors (spot-checked pages; `pdftotext` shows no raw TeX).
- One overflow found: the opt03 S106 recap chain was about 950 px wide in a 712 px column and was clipped in print.
  - Fixed in `391acbe`: it is now an `aligned` display on two lines, re-rendered clean on note p. 26.
- opt01 S102 ran slightly past the column but was not clipped.

**Narrow (~485 px, the smallest headless Chromium would lay out).**
- Prose wraps.
- Wide displays spilled the page in opt01 S82, S83, S90, S101, S102 and opt03 S105, S106, S138.
- Fixed in `391acbe`: both notes now set `.katex-display { overflow-x: auto }`, so a wide display scrolls inside its own box and no longer widens the page.

**Agreement.** Each article's message, explanation, details and sources were written together with its slide by the same package. Where a source differs from the slide, the article says so (§2 plan issues 2, 5, 6).

**Markdown.**
- Both `.md` notes are pure ASCII (`grep -P '[^\x00-\x7F]'` is empty).
- opt01 has 68 `### N. Title [Snn]` headings, N = 1..68 in sequence, each with one `BEGIN/END` pair.
- opt03 has 51, N = 1..51.
- Snn order equals the deck's `data-slide-id` order, and so does the HTML note's `<article>` order.
- Every figure and table on a main slide has a verbal description in its Markdown article. Tables are linearised; S131 and S140 are given as bullet lists with a legend.

## 10. Figure inventory

| Deck / ID | Figure | Source | Parameters and invariants |
|---|---|---|---|
| opt01 S87 | Two planes in R³ share a line | `courses/deepmath/opt01-svd-lowrank/figs/o1c_planes.py` (runs with stdlib only, prints coordinates) | S1 = {z=0}; S2 = span{(1,0.3,0),(0,−0.6,1)}; S1∩S2 = span{d}, d = (1,0.3,0); w = 0.8·d/‖d‖. The script asserts that the line and w lie in both planes. Fixed oblique projection, viewBox 1040×470 |
| opt03 S95 | Flat-bottom max(\|u\|−1,0)²: argmin, Δ_t, √D_t | `courses/deepmath/opt03-convexity-gd/figs/o3b_figs.py` | Convex, 2-smooth, argmin [−1,1]; x_t = 2.9, x* = 1; X = 320+75u, Y = 270−33f |
| opt03 S65 | E09 along (1,1): f, μ-floor, L-lid | same script | φ(s) = 1.25s²; anchor s₀ = −1; μ = 1, L = 4; lid clipped at the plot top |
| opt03 S110 | 1/T vs (3/4)^T on a log scale | same script | T = 1..24 |
| opt01 S80, S12, S13, S16, S18, S66, S52/S53, S41, S42, S91, S103 | Inline SVG, hand-placed or exact | Geometry comment in the HTML beside each SVG | S13/S16 are exact two-panel maps of C = [[1,1],[2,2]]. S66 has the ellipse to scale and the circle at ×3. S103 is drawn at 18 px per energy unit (810/900). S91 is a schematic number line |
| opt01 S39, S40, S44, S117, S123 | HTML/CSS flows and shape diagrams | `o1b-*` / `o1c-*` CSS | — |
| opt03 S80, S82, S34, S93, S136 | Inline SVG | Geometry comment in the HTML | S136: 1−cos x, L = 1, stalls at x = π. S82: f = u², steps 0.2 and 1.1 from u = 1.5. S34 reuses the baseline geometry |
| opt03 S10, S15 | Chord and tangent on u² | Reused from baseline S11 and S16 | Relabelled |

No unsourced legacy fact was copied onto a main slide. The unsourced items that remain in the notes are listed in §2, plan issue 3.

## Appendix A — worker reports (summary)

**P0a/P0b (structural).**
- Partition tables and duplicated paragraphs are in the worker reports.
- Legacy errors noted but not fixed (they remain in the archived full notes):
  - opt01: a square matrix with a left inverse is called invertible "by Theorem 1"; the converse in the old S33 note.
  - opt03: old Theorem 8/10 numbering, and co-coercivity proofs left out of the main.
- None of these was carried into a main note.

**w1–w5.** Deviations and plan issues are merged into §2. Math recomputations are merged into §6. Figures are merged into §10.

## Appendix B — ID maps

### opt01-svd-lowrank

baseline 119, main 68, full backup 119; backup ID order == baseline: True
| ID | baseline p. / title | new p. / title | status |
|---|---|---|---|
| S01 | 1. SVD &Low-Rank Approximation | 1. SVD and BestLow-Rank Approximation | retained (retitled) |
| S02 | 2. Contents | 2. Contents | retained |
| S03 | 3. The Optimization Half | — | archive-only |
| S04 | 4. Where the Probability Half Stopped | — | archive-only |
| S05 | 5. The Optimization Half, in Four Steps | — | archive-only |
| S06 | 6. Deep Learning Optimizes Matrices | — | archive-only |
| S07 | 7. SVD = the X-Ray | — | archive-only |
| S08 | 8. Low Rank Is Everywhere | — | archive-only |
| S09 | 9. Route Map | — | archive-only |
| S10 | 10. Rank, Range, Null Space | — | archive-only |
| S11 | 11. A Matrix, Column by Column | — | archive-only |
| S12 | 12. Definition — Span & Range | 5. Recall: Span and Range | moved, retitled |
| S13 | 13. Worked — a Collapsing Matrix | 7. Two Inputs Collapse to One Direction | moved, retitled |
| S14 | 14. Definition — Rank | 6. Rank Counts Independent Directions | moved, retitled |
| S15 | 15. Worked — Ranks by Inspection | — | archive-only |
| S16 | 16. Definition — Null Space | 8. Null Space Means Lost Directions | moved, retitled |
| S17 | 17. Worked — Null Space of $C$ | — | archive-only |
| S18 | 18. Theorem 1 — Rank–Nullity | 9. Rank and Nullity Add Up | moved, retitled |
| S19 | 19. Rank–Nullity — Sanity Checks | — | archive-only |
| S20 | 20. Rank–Nullity — the Picture | — | archive-only |
| S21 | 21. Definition — Orthogonal Complement | — | archive-only |
| S22 | 22. Theorem 2 — Split Any Vector | — | archive-only |
| S23 | 23. Theorem 3 — the Four Subspaces | — | archive-only |
| S24 | 24. Why AI Cares About Rank | — | archive-only |
| S25 | 25. Norms & Orthogonal Matrices | 10. Measuring Error | moved, retitled |
| S26 | 26. How Long Is a Vector? | — | archive-only |
| S27 | 27. Definition — Norm | 11. What Makes a Norm? | moved, retitled |
| S28 | 28. The $\ell_p$ Family | 12. Three Familiar Vector Norms | moved, retitled |
| S29 | 29. Worked — One Vector, Three Norms | 13. One Vector, Three Answers: 7, 5, 4 | moved, retitled |
| S30 | 30. Unit Balls — the Norms as Shapes | 14. Unit Balls Reveal the Metric | moved, retitled |
| S31 | 31. Definition — Orthogonal Matrix | 15. Orthogonal Maps Preserve Geometry | moved, retitled |
| S32 | 32. Example — Rotation by 45° | — | archive-only |
| S33 | 33. Theorem 4 — Orthogonal Maps Preserve Length | 16. Why Length Is Preserved | moved, retitled |
| S34 | 34. Implication — Rotations Are Free | — | archive-only |
| S35 | 35. The Singular Value Decomposition | 19. Reading an SVD | moved, retitled |
| S36 | 36. Recall — Eigendecomposition | 20. Recall: Symmetric Eigendecomposition | moved, retitled |
| S37 | 37. Technique Review — Eigen vs Singular | — | archive-only |
| S38 | 38. Theorem 5 — the SVD Exists | 21. Every Matrix Has an SVD | moved, retitled |
| S39 | 39. Reading the Shapes (Full SVD) | 22. Read the Factor Shapes | moved, retitled |
| S40 | 40. What Each Factor Does | 23. Rotate, Stretch, Rotate | moved, retitled |
| S41 | 41. Technique Review — the Outer-Product View | 26. A Sum of Rank-One Layers | moved, retitled |
| S42 | 42. Thin (Compact) SVD | 27. Compact SVD Keeps Active Directions | moved, retitled |
| S43 | 43. Thin Factors Are Not Orthogonal Matrices | — | archive-only |
| S44 | 44. Worked — SVD by Hand: the Plan | 28. One Matrix, One Construction | moved, retitled |
| S45 | 45. Worked — Step 1: Form $A^{\top}A$ | 29. Build the Symmetric Matrix $A^{\top}A$ | moved, retitled |
| S46 | 46. Worked — Step 2: Eigenvalues | 30. The Eigenvalues Are 45 and 5 | moved, retitled |
| S47 | 47. Worked — Step 2: Eigenvectors | 31. Orthonormal Input Directions | moved, retitled |
| S48 | 48. Worked — Step 3: Sigmas and $u_i$ | 32. Recover Stretches and Output Directions | moved, retitled |
| S49 | 49. Worked — Step 4: Assemble | 33. The Factors Reconstruct $A$ | moved, retitled |
| S50 | 50. Worked — Verify via Rank-1 Layers | 34. The First Layer Carries Most Energy | moved, retitled |
| S51 | 51. Eigenvalues $\neq$ Singular Values | 35. Eigenvalues Are Not Singular Values | moved, retitled |
| S52 | 52. Circle to Ellipse — Rotate First | 24. First Change the Input Coordinates | moved, retitled |
| S53 | 53. Circle to Ellipse — Stretch, Then Rotate Back | 25. Then Stretch and Reorient | moved, retitled |
| S54 | 54. SVD — What to Remember | — | archive-only |
| S55 | 55. The Pseudo-Inverse | — | archive-only |
| S56 | 56. When $A^{-1}$ Doesn't Exist | — | archive-only |
| S57 | 57. Definition — Moore–Penrose Pseudo-Inverse | — | archive-only |
| S58 | 58. Worked — $A^{\dagger}$ for the Running Matrix | — | archive-only |
| S59 | 59. Worked — $A^{\dagger}$, Finished | — | archive-only |
| S60 | 60. Worked — the Rank-Deficient Case | — | archive-only |
| S61 | 61. Sanity Check — $A A^{\dagger} A = A$ | — | archive-only |
| S62 | 62. $AA^{\dagger}$ and $A^{\dagger}A$ Are Projections | — | archive-only |
| S63 | 63. Teaser — Solving the Unsolvable | — | archive-only |
| S64 | 64. Matrix Norms | — | archive-only |
| S65 | 65. Two Ways to Measure a Matrix | — | archive-only |
| S66 | 66. Definition — Induced (Operator) Norm | 17. Spectral Norm: Worst Stretch | moved, retitled |
| S67 | 67. The Inequality It's Built For | — | archive-only |
| S68 | 68. Theorem 6 — Spectral Norm $=$ Top Sigma | 36. Largest Singular Value, Largest Stretch | moved, retitled |
| S69 | 69. Proof (Thm 6) — No Vector Beats $\sigma_1$ | 37. No Direction Beats the Largest Stretch | moved, retitled |
| S70 | 70. Proof (Thm 6) — And $v_1$ Achieves It | 38. The First Singular Vector Attains It | moved, retitled |
| S71 | 71. Worked — Max Stretch of $A$ | — | archive-only |
| S72 | 72. Definition — Frobenius Norm | 18. Frobenius Norm: Total Energy | moved, retitled |
| S73 | 73. Theorem 7 — Frobenius via Sigmas | 39. Frobenius Energy Sums Squared Stretches | moved, retitled |
| S74 | 74. Proof (Thm 7) — One Trace Chain | 40. Orthogonal Coordinates Preserve Total Energy | moved, retitled |
| S75 | 75. Worked — $\|A\|_F$ Two Ways | — | archive-only |
| S76 | 76. Definition — Nuclear Norm | — | archive-only |
| S77 | 77. One Vector, Three Norms | — | archive-only |
| S78 | 78. Nuclear Norm $\approx$ Convex Rank | — | archive-only |
| S79 | 79. Best Low-Rank Approximation | 41. Best Low-Rank Approximation | moved |
| S80 | 80. The Compression Question | 4. A Smaller Matrix, Controlled Error | moved, retitled |
| S81 | 81. The Candidate — Truncated SVD | 42. Candidate: Keep the $k$ Largest Layers | moved, retitled |
| S82 | 82. Worked — $A_1$ for the Running Matrix | 43. Worked: $A_1$ Is the Top Layer of $A$ | moved, retitled |
| S83 | 83. Worked — the Error of $A_1$ | 44. Worked: $A_1$'s Error Is the Discarded Layer | moved, retitled |
| S84 | 84. The Claim | — | archive-only |
| S85 | 85. Technique Review 1 — Rank–Nullity | 47. Recall: Low Rank Forces a Big Null Space | moved, retitled |
| S86 | 86. Technique Review 2 — Big Subspaces Must Meet | 48. Large Subspaces Must Intersect | moved, retitled |
| S87 | 87. Picture — Two Planes in $\mathbb{R}^3$ | 49. Two Planes in $\mathbb{R}^3$ Share a Line | moved, retitled |
| S88 | 88. Technique Review 3 — Bounding a Max From Below | 50. One Unit Witness Bounds the Maximum | moved, retitled |
| S89 | 89. Technique Review 4 — $\|Aw\|^2$ in the $v$-Basis | 51. Top $k{+}1$ Directions Stretch by $\geq \sigma_{k+1}$ | moved, retitled |
| S90 | 90. Theorem 8 — Eckart–Young–Mirsky | 45. Eckart–Young–Mirsky: Spectral Error | moved, retitled |
| S91 | 91. Reading the Statement | 46. Optimal: a Floor for All, Met by One | moved, retitled |
| S92 | 92. Proof Overview (Spectral Case) | 52. Proof Plan: Find One Witness | moved, retitled |
| S93 | 93. Step 1 — Every Competitor Has a Blind Spot | 53. Step 1: Every Competitor Has a Blind Spot | moved, retitled |
| S94 | 94. Step 2 — Where $A$ Is Still Strong | 54. Step 2: $A$ Stays Strong on $W$ | moved, retitled |
| S95 | 95. Step 3 — The Two Subspaces Collide | 55. Step 3: The Two Subspaces Share a Unit $w$ | moved, retitled |
| S96 | 96. Step 4 — The Witness Bound | 56. Step 4: Along $w$, the Residual Is $A$ | moved, retitled |
| S97 | 97. Step 4, Finished — $A$ Is Strong at $w$ | 57. Step 4 (continued): The Witness Is Not Small | moved, retitled |
| S98 | 98. Step 5 — Truncation Hits the Floor | 58. Step 5: Truncation Meets the Bound | moved, retitled |
| S99 | 99. Proof Summary — the Skeleton | 59. One Chain Proves the Spectral Theorem | moved, retitled |
| S100 | 100. The Key Trick, Named | — | archive-only |
| S101 | 101. The Frobenius Case | 60. Eckart–Young–Mirsky: Frobenius Error | moved, retitled |
| S102 | 102. Worked — EYM on the Running Matrix | 63. The Best Rank-One Error Is $\sqrt{5}$ | moved, retitled |
| S103 | 103. How Much Did $A_1$ Keep? | 64. One Layer Keeps 90% of the Energy | moved, retitled |
| S104 | 104. Implication — the License to Truncate | — | archive-only |
| S105 | 105. Netflix & Matrix Completion | — | archive-only |
| S106 | 106. The Recommendation Problem | — | archive-only |
| S107 | 107. Worked — a Tiny Ratings Matrix | — | archive-only |
| S108 | 108. Only Two Taste Patterns | — | archive-only |
| S109 | 109. Rank 2 $=$ Tastes $\times$ Genres | — | archive-only |
| S110 | 110. Worked — Fill In the Blanks | — | archive-only |
| S111 | 111. Formalizing — the Observed Set $\Omega$ | — | archive-only |
| S112 | 112. The Ideal Program — and Its Problem | — | archive-only |
| S113 | 113. The Convex Relaxation | — | archive-only |
| S114 | 114. Why the Relaxation Is a Win | — | archive-only |
| S115 | 115. The Same Shape, Everywhere in AI | — | archive-only |
| S116 | 116. Closing | 62. Read the Answer | moved, retitled |
| S117 | 117. Every Tool, One Line Each | 67. From Directions to the Optimal Error | moved, retitled |
| S118 | 118. Next — Least Squares | — | archive-only |
| S119 | 119.  | 68.  | moved |
| S120 | — | 3. Why Low Rank? | new |
| S121 | — | 61. $A_k$'s Error Is the Discarded Energy | new |
| S122 | — | 65. Worst Error and Total Error Can Differ | new |
| S123 | — | 66. What the Guarantee Covers | new |

### opt03-convexity-gd

baseline 134, main 51, full backup 134; backup ID order == baseline: True
| ID | baseline p. / title | new p. / title | status |
|---|---|---|---|
| S01 | 1. Convexity &Gradient Descent | 1. Gradient Descent:Three Guarantees | retained (retitled) |
| S02 | 2. Contents | 2. Contents | retained |
| S03 | 3. Why Convexity? | — | archive-only |
| S04 | 4. When the Formula Runs Out | — | archive-only |
| S05 | 5. Three Questions About One Update | — | archive-only |
| S06 | 6. Today's Three Results | — | archive-only |
| S07 | 7. The Constants Are Learning-Rate Theory | — | archive-only |
| S08 | 8. Route Map | — | archive-only |
| S09 | 9. Convexity | 26. Convex: Optimality | moved, retitled |
| S10 | 10. Definition — Convex Function | 27. Convexity Puts Chords Above | moved, retitled |
| S11 | 11. Chord Above the Graph | — | archive-only |
| S12 | 12. Convex vs. Nonconvex | — | archive-only |
| S13 | 13. Why AI Cares | — | archive-only |
| S14 | 14. The Gradient, Recalled | 5. Recall: The Gradient Gives First-Order Change | moved, retitled |
| S15 | 15. First-Order Characterization | 28. The Tangent Lies Below | moved, retitled |
| S16 | 16. Tangent Below the Graph | — | archive-only |
| S17 | 17. Why — the 1D Picture | — | archive-only |
| S18 | 18. The Hessian, Recalled | — | archive-only |
| S19 | 19. Recall — PSD | — | archive-only |
| S20 | 20. Theorem 1 — Second-Order Characterization | — | archive-only |
| S21 | 21. Worked — Is It Convex? | — | archive-only |
| S22 | 22. Worked — a Saddle Is Not Convex | — | archive-only |
| S23 | 23. The Running Example | — | archive-only |
| S24 | 24. Running Example — Contours | — | archive-only |
| S25 | 25. Smoothness | 10. One Descent Inequality | moved, retitled |
| S26 | 26. Lipschitz Continuity | — | archive-only |
| S27 | 27. Definition — $L$-Smooth | 7. $L$-Smoothness Bounds Gradient Change | moved, retitled |
| S28 | 28. Theorem 2 — Bounded Hessian | — | archive-only |
| S29 | 29. Proof Sketch — as in the Notes | — | archive-only |
| S30 | 30. Running Example — $L = 4$ | 9. Running Example: $L = 4$ | moved, retitled |
| S31 | 31. Technique Review — Restrict to a Segment | — | archive-only |
| S32 | 32. Technique Review — Cauchy–Schwarz | — | archive-only |
| S33 | 33. Lemma 1 — the Descent Lemma | 11. Smoothness Gives a Quadratic Upper Bound | moved, retitled |
| S34 | 34. The Picture — a Parabola Lid | 12. The Upper Bound Touches $f$ at $x$ | moved, retitled |
| S35 | 35. Descent Lemma — Proof Overview | — | archive-only |
| S36 | 36. Step 1 — Set Up $g$ | 13. Proof Step 1: Follow the Segment | moved, retitled |
| S37 | 37. Step 2 — Bound the Slope Drift | 14. Proof Step 2: Smoothness Bounds the Drift | moved, retitled |
| S38 | 38. Step 3 — Integrate | 15. Proof Step 3: Integrating $s$ Gives $\tfrac{1}{2}$ | moved, retitled |
| S39 | 39. Proof Summary — the Skeleton | — | archive-only |
| S40 | 40. What the Descent Lemma Buys | — | archive-only |
| S41 | 41. Theorem 3 — the Smoothness Sandwich | — | archive-only |
| S42 | 42. Reading the Statement | — | archive-only |
| S43 | 43. Proof — Right Side | — | archive-only |
| S44 | 44. Proof — Left Side, the Idea | — | archive-only |
| S45 | 45. Proof — Left Side, Minimize the Lid | — | archive-only |
| S46 | 46. Proof — Left Side, Best Direction | — | archive-only |
| S47 | 47. Sandwich, Checked on the Running Example | — | archive-only |
| S48 | 48. Smooth and Convex | — | archive-only |
| S49 | 49. Two Bounds Meet | — | archive-only |
| S50 | 50. Lemma 2 — Co-coercivity | — | archive-only |
| S51 | 51. What Co-coercivity Says | — | archive-only |
| S52 | 52. Proof of (i) — Overview | — | archive-only |
| S53 | 53. Proof of (i) — One Point, Two Bounds | — | archive-only |
| S54 | 54. Proof of (i) — Chain and Rearrange | — | archive-only |
| S55 | 55. Proof of (i) — the Best $z$ | — | archive-only |
| S56 | 56. Proof of (ii) — Overview | — | archive-only |
| S57 | 57. Proof of (ii) — the Tilted Function | — | archive-only |
| S58 | 58. Proof of (ii) — Apply the Sandwich | — | archive-only |
| S59 | 59. Proof of (ii) — Symmetrize | — | archive-only |
| S60 | 60. Proof of (ii) — Add Them | — | archive-only |
| S61 | 61. Proof Summary — Co-coercivity | — | archive-only |
| S62 | 62. Co-coercivity, Checked on the Running Example | — | archive-only |
| S63 | 63. Strong Convexity | 38. Strongly Convex: Geometric Decay | moved, retitled |
| S64 | 64. Definition — $\mu$-Strongly Convex | 39. Add a Quadratic Floor | moved, retitled |
| S65 | 65. The Two-Parabola Sandwich | 40. Curvature Is Bounded Below | moved, retitled |
| S66 | 66. Theorem 4 — Hessian Floor | — | archive-only |
| S67 | 67. Recall — Ridge Buys $\mu$ | — | archive-only |
| S68 | 68. Theorem 5 — Gradient Monotonicity | — | archive-only |
| S69 | 69. Proof — Add Two Floors | — | archive-only |
| S70 | 70. Theorem 6 — Strong Monotonicity | — | archive-only |
| S71 | 71. Proof — Same Trick, Stronger Floors | — | archive-only |
| S72 | 72. Technique Review — Completing the Square | — | archive-only |
| S73 | 73. Lemma 3 — the PL Condition | — | archive-only |
| S74 | 74. Reading PL — Gradient Norm Measures the Gap | — | archive-only |
| S75 | 75. Proof of PL — Rearrange the Floor | — | archive-only |
| S76 | 76. Proof of PL — Complete the Square | — | archive-only |
| S77 | 77. PL, Checked on the Running Example | — | archive-only |
| S78 | 78. PL as an Assumption of Its Own | — | archive-only |
| S79 | 79. Gradient Descent | 3. One Update | moved, retitled |
| S80 | 80. The Problem | 4. Goal: Minimize One Differentiable $f$ | moved, retitled |
| S81 | 81. The Algorithm | 8. One Fixed Step: $1/L$ | moved, retitled |
| S82 | 82. 1D Intuition — the Sign Does the Steering | 6. Small Steps Against the Gradient Go Downhill | moved, retitled |
| S83 | 83. Running Example — GD, Set Up by Hand | 17. One Step Zeroes the Stiff Coordinate | moved, retitled |
| S84 | 84. Four Iterations by Hand  ($\alpha = 1/4$) | 18. Two Steps: $f$ Falls From $10$ to $81/128$ | moved, retitled |
| S85 | 85. The Path on the Contours  ($\alpha = 1/4$) | — | archive-only |
| S86 | 86. Bigger Step — Zigzag  ($\alpha = 0.45$) | — | archive-only |
| S87 | 87. Too Big — Divergence  ($\alpha = 0.6 \gt 2/L$) | — | archive-only |
| S88 | 88. Three Step Sizes, One Lesson | — | archive-only |
| S89 | 89. Theorem 7 — GD Converges (Smooth Case) | 20. Nonconvex Guarantee: Small Squared Gradient | moved, retitled |
| S90 | 90. Proof — One Step Through the Lid | 16. The Step $1/L$ Decreases $f$ | moved, retitled |
| S91 | 91. Proof — Monotone and Bounded | 21. Proof Step 1: Sum the Decreases | moved, retitled |
| S92 | 92. Proof — Gradients Must Vanish | 22. Proof Step 2: Minimum at Most Average | moved, retitled |
| S93 | 93. Reading the Theorem | 23. Stationary Does Not Mean Minimum | moved, retitled |
| S94 | 94. Rate I — $O(1/T)$ | — | archive-only |
| S95 | 95. Assumptions and Goal | 29. Assume an Optimum Exists | moved, retitled |
| S96 | 96. Theorem 8 — $O(1/T)$ Convergence | 30. Convex: $O(1/T)$ Function Gap | moved, retitled |
| S97 | 97. Proof Overview | 31. Proof Plan: Spend Distance | moved, retitled |
| S98 | 98. Step 1 — Guaranteed Decrease | 32. Recall: One-Step Decrease | moved, retitled |
| S99 | 99. Step 2 — Bring In the Optimum | 33. Use the Tangent at $x_t$ | moved, retitled |
| S100 | 100. Technique Review — the Square, Completed Again | — | archive-only |
| S101 | 101. Step 3 — the Distance Identity | 34. Expand the Squared Distance | moved, retitled |
| S102 | 102. Corollary — the Distance Also Shrinks | — | archive-only |
| S103 | 103. Technique Review — Telescoping Sums | — | archive-only |
| S104 | 104. Step 4 — Telescope | 35. Distances Telescope | moved, retitled |
| S105 | 105. Step 5 — From Sum to Last Iterate | 36. The Last Gap Is Smallest | moved, retitled |
| S106 | 106. Proof Summary — the Skeleton | 37. The Convex Proof in One Chain | moved, retitled |
| S107 | 107. Corollary — Iteration Complexity $O(1/\varepsilon)$ | — | archive-only |
| S108 | 108. Bound vs. Reality on the Running Example | — | archive-only |
| S109 | 109. Rate II — Linear | — | archive-only |
| S110 | 110. The Goal — From $1/T$ to $c^{\,T}$ | 46. Linear Means Geometric | moved, retitled |
| S111 | 111. Theorem 9 — Subtract the Floor | — | archive-only |
| S112 | 112. What $h$ Knows About $f$ | — | archive-only |
| S113 | 113. Co-coercivity, Applied to $h$ | — | archive-only |
| S114 | 114. Unpack — Expand the Square | — | archive-only |
| S115 | 115. Unpack — Collect Terms | — | archive-only |
| S116 | 116. Theorem 10 — Linear Convergence | 41. Strongly Convex: Geometric Convergence | moved, retitled |
| S117 | 117. Proof Overview | — | archive-only |
| S118 | 118. Step 1 — Expand the Square | — | archive-only |
| S119 | 119. Step 2 — Co-coercivity at the Optimum | — | archive-only |
| S120 | 120. Step 3 — Group; Kill the Gradient Term | — | archive-only |
| S121 | 121. Technique Review — Unrolling a Recursion | — | archive-only |
| S122 | 122. Step 4 — Unroll | 44. Repeat the Same Contraction | moved, retitled |
| S123 | 123. Step 5 — Function Values Follow | 45. Function Values Follow Distance | moved, retitled |
| S124 | 124. Proof Summary — the Skeleton | — | archive-only |
| S125 | 125. Remark — $O(\log(1/\varepsilon))$ Iterations | — | archive-only |
| S126 | 126. Running Example — Contraction, Measured | 47. The Example Beats Its Bound | moved, retitled |
| S127 | 127. Geometric Shrinkage, Drawn | — | archive-only |
| S128 | 128. Bonus — PL Alone Gives the Linear Rate | — | archive-only |
| S129 | 129. Bonus — Unroll the PL Rate | — | archive-only |
| S130 | 130. Closing | 48. Three Guarantees | moved, retitled |
| S131 | 131. Every Tool, One Line Each | 49. Three Assumptions, Three Guarantees | moved, retitled |
| S132 | 132. The Constants You Now Own | — | archive-only |
| S133 | 133. Next — Stochastic Gradients | — | archive-only |
| S134 | 134. $x^{+} = x - \alpha\, \nabla f(x)$ | 51. $x_{t+1} = x_t - \tfrac{1}{L}\, \nabla f(x_t)$ | moved, retitled |
| S135 | — | 19. Nonconvex: Stationarity | new |
| S136 | — | 24. GD Can Stay at a Maximum | new |
| S137 | — | 25. The Square Changes the Rate | new |
| S138 | — | 42. Keep the Extra Curvature Term | new |
| S139 | — | 43. Nonnegative Gap Forces Contraction | new |
| S140 | — | 50. No Extra Conditions Needed | new |
