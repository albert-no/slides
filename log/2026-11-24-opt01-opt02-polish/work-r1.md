# work-r1 — 2026-11-24-opt01-opt02-polish

Branch `2026-11-24-opt01-opt02-polish` from baseline `9fdba016e02405c96fa9d8a9c7224f4612361d16`. No ID-only commit (IDs inherited). PR #80's head branch untouched. Two parallel packages, each in its own worktree: opt01 (P1–P4) and opt02 (P5–P7), merged by `--no-ff`, then integration (outlines, counts) by slides.

Commits: e7f6e44 + 90a50d4 (opt01), b1b8362 + 4118fa1 (opt02), c5e9e0d / 2129fb1 (merges), eb94c20 (outlines/counts), plus this log commit.

Touched: opt01 triplet; opt02 triplet; `opt02-convexity-gd/figs/o3b_figs.py` (S65/S110); new `opt02-convexity-gd/figs/gd_model_build.py` (S34a–c); root `OUTLINE.md`; `courses/deepmath/OUTLINE.md`; `courses/deepmath/opt03-backup/OUTLINE.md` (count line only). Archive triplets byte-identical to baseline (`git diff 9fdba01 -- courses/deepmath/opt03-backup` shows only OUTLINE.md).

## Counts
- opt01: 68 → **61** (−9 deleted, S12 → S12a+S12b, new S124). Sections: title/TOC 1–2, 01 3–10, 02 11–19, 03 20–36, 04 37–55, 05 56–60, end 61.
- opt02: 51 → **48** (−6 deleted, S34 → S34a/b/c, new S141). Sections: 1–2, 3–8, 9–16, 17–23, 24–35, 36–44, 45–47, end 48.
- Deck / HTML note / MD note ID sequences identical (61/61/61, 48/48/48); headings renumbered, titles match.
- Updated count surfaces: root OUTLINE, deepmath OUTLINE (table rows + leaf headings), opt03-backup OUTLINE, note front matter. `.slide-num` is JS-computed.

## Opt01: comment → baseline page → ID → new page
| C | Base p | ID | New p / title | Change |
|---|---|---|---|---|
| C01 | 4 | S80 | 4 "A Smaller Matrix, Controlled Error" | Given / Choose / A = B + residual / Quality on separate lines, more space, no type change; storage aside moved to S124 note; note says the 2×2 saves nothing |
| C02 | 5 | S12a, S12b | 5 "Range Is the Column Span"; 6 "An Output Combines the Columns" | definition only; enlarged to-scale vector-addition SVG with a1, a2, x, Ax=(3,3), "one output" |
| C03 | 15 | S31 | 16 "Orthogonal Maps Preserve ℓ2 Geometry" | ‖Qx‖₂ = ‖x‖₂, distances and angles; "unit ℓ2 circle"; note: inner-product/distance identity, unit-vector example qualified |
| C04 | 23 | S40 | 24 "Rotate, Stretch, Rotate" | one large flow x → Vᵀx → ΣVᵀx → Ax with Rⁿ/Rᵐ labels at body size; rightmost factor first; rotation or reflection |
| C05 | 28 | S44 | 29 "Constructing the SVD" | generic 4-step flow, σᵢ = √λᵢ, "only if σᵢ > 0" on uᵢ = Avᵢ/σᵢ, orthonormal completion, "conceptual route, not a numerical algorithm"; matrix removed |
| C06 | 29–33 | S45–S49 | deleted | see coverage |
| C07 | 34 | S50 | 30 (title kept) | "Illustration:" framing; 50 = 45 + 5, 90%; "reconstruction, not optimality"; note derives this SVD self-contained |
| C08 | 35 | S51 | 31 "Eigenvalues and Singular Values Differ" | generic comparison, "In general the two lists differ", equal for symmetric PSD; numbers only as optional note counterexample |
| C09 | 43–44 | S82, S83 | deleted | see coverage |
| C10 | 46 | S91 | 40 "Optimality Needs Two Claims" | plot removed; (i) floor for every rank-≤k B, (ii) A_k attains it; "One candidate's error alone cannot establish optimality" |
| C11 | 60 | S101 | 54 (title kept) | "Frobenius optimality proof: beyond this lecture's scope."; note Message and proof heading "Optional, beyond lecture scope" |
| C11 | 61 | S121 | 55 (title kept) | added "Achievability only; not the Frobenius lower-bound proof" |
| C12 | 63, 65 | S102, S122 | deleted | see coverage |
| C12 | 64 | S103 | 57 "Energy Retention Guides Rank" | general R_k (A nonzero), complement, smallest k with R_k ≥ η, "energy share, not prediction accuracy"; centered-data caveat in note |
| C13 | new | S124 | 58 "Low Rank Compresses LLM Weights" | W (m×n) ≈ L (m×k) × R (k×n); mn → k(m+n), saving only if k(m+n) < mn; "Small matrix error does not guarantee model accuracy"; SVD-LLM (Wang, Zheng, Wan & Zhang, ICLR 2025, E05); note: L = U_kΣ_k, R = V_kᵀ, activation-aware objective, not plain truncation |
| item 17 | 1–2, 62, 66–68 | S01, S02, S116, S123, S117, S119 | 1–2, 56, 59–61 | divider/Contents "Rank, error and energy"; S117 recap adds R_k; S123 slide unchanged, note gets optional S122 paragraph; front matter no longer promises a worked example to the end |

## Opt02: comment → baseline page → ID → new page
| C | Base p | ID | New p / title |
|---|---|---|---|
| C14 | 9, 17, 18, 47 | S30, S83, S84, S126 | deleted; running-example remnants removed from front matter and S27/S137/S101/S104/S139/S123/S65/S110 notes |
| C15 | 12 | S34 → S34a/b/c | 11 "Start at the Current Point", 12 "Smoothness Adds an Upper Model", 13 "Minimize the Model, Then Step" — separate static slides, one shared frame, advanced manually |
| C16 | 11 | S33 | 10 — descent lemma stated as a standard tool; integral proof optional in note Details |
| C16 | 13, 14 | S36, S37 | 14 "Minimize a Safe Upper Model", 15 "Completing the Square Gives GD" |
| C16 | 15 | S38 | deleted |
| C16 | 16 | S90 | 16 — substitution proof and strict decrease for g ≠ 0 kept |
| C17 | 20–22 | S89, S91, S92 | 18–20 — finite-time theorem kept; minimum over iterates vs attained minimum of f distinguished in notes |
| C17 | new | S141 | 21 "Every Gradient Norm Vanishes" — Q/A "Yes, for the whole sequence"; Σ‖∇f(x_t)‖² ≤ 2L(f(x₀)−f_low) < ∞ ⇒ ‖∇f(x_t)‖ → 0; no last-iterate rate, no x_t convergence |
| C17 | 23, 25 | S93, S137 | 22, 23 |
| C18 | 24 | S136 | deleted |
| C19 | 30, 41 | S96, S116 | 28, 39 — headings "Theorem (smooth convex GD)" / "(strongly convex GD)"; cite Nesterov 2004 (classical treatment) + Garrigos & Gower 2024 Thm 3.4 / Thm 3.6, Remark 3.7 (exact bounds); notes: handbook is a correct reference, not the origin; earliest priority not established |
| C14 | 40 | S65 | 38 — generic μ/L floor and upper model at one base point |
| C20 | 46, 47 | S110, S126 | 44 (1/T vs q^T, illustrative q, "shapes only, not GD output"); S126 deleted |
| item 31 | shared | S01/S02/S25/S135/S130/S131/S140/S134 | 1/2/9/17/45/46/47/48 — S131 table keeps best-iterate rate; scope line below: "Nonconvex also: every ‖∇f(x_t)‖ → 0; no local-minimum guarantee" |

## Removed-content coverage
| Deck | ID | Where it lives |
|---|---|---|
| opt01 | S45, S46, S47, S48, S49 | `opt03-backup/opt01-svd-lowrank-full.html` l.883/896/906/922/936, `-full-note.html` l.353/361/369/375/383, `-full-note.md` l.486/494/504/512/524; S44 and S50 notes carry an optional pointer and a self-contained derivation of the S50 illustration |
| opt01 | S82, S83 | full.html l.1416/1429; full-note.html l.631/635; full-note.md l.876/880 |
| opt01 | S102 | full.html l.1686; full-note.html l.773; full-note.md l.1060 |
| opt01 | S122 | not in archive → optional diag(5,3,1) paragraph in S123 article (H and M) |
| opt02 | S30, S83, S84, S126 | `opt03-backup/opt03-convexity-gd-full.html` l.607/1327/1339/1946; `-full-note.html` l.499/1098/1102/1653; `-full-note.md` l.318/753/757/1136 |
| opt02 | S36, S37, S38 (old integral proof) | full.html l.700/712/724; full-note.html l.558/562/566; full-note.md l.368/372/376; also optional derivation in active S33 note |
| opt02 | S136 | not in archive → one optional paragraph in S93 note (H and M) |

## Figures
- opt02 S34a–c: `figs/gd_model_build.py` (prints coordinates, asserts checks). Inputs from E09: f(u)=u², x=−0.6, g=−1.2, L=3, step to −0.2; Q(−0.2)=0.12, f(−0.2)=0.04. Symbol labels only on-slide; parameters in cite line and notes.
- opt02 S65: `figs/o3b_figs.py`, φ(s)=s², μ=1, L=3, anchor s=−1 (curvature 2 strictly between μ and L).
- opt02 S110: `figs/o3b_figs.py`, illustrative q=0.8, T=1..24, log scale.
- Both generators re-run on the merged branch: "checks ok", no tracked file changes.
- opt01: S12b SVG enlarged, S31 relabelled, S40 flow enlarged, new HTML/CSS S44 flow and S124 dimension boxes; S91 plot and S103 bar removed. Opt01 generator unchanged.

## Checks (on merged branch unless noted)
- `lint-deck.py` both decks: ok (0 errors, 0 font-size warnings); HTML notes ok in package runs.
- `lint-accessible-md.py` both MD notes: one warning each ("the slide", MD line 3 / 5), present at baseline.
- MD notes ASCII-only (grep empty).
- `outline-lint.py`: 0 stale/missing pointers; 5 warnings, all pre-existing in infotheory/privacy outlines.
- find-wordy: no flags. find-dense (opt01): S80 72 words, S123 (unchanged slide), S119 closer — all render cleanly; baseline had 5 flags.
- Render (-r 60): opt01 changed pages 2, 4–6, 16, 18, 24–26, 29–31, 33–35, 40, 54–60 (package); integrator re-check of 24, 29, 40, 58. opt02 changed pages incl. 11–13, 15, 17, 21, 22, 28, 38, 39, 44, 46 (package); integrator re-check of 13, 15, 21, 28, 44, 46. No overflow, overlap or footer collision; S40/S44 labels at body size on the render.
- HTML notes: 0 KaTeX errors at 430 px (both). opt01 note: no horizontal overflow at 430/1280 px. opt02 note: checked at 1280 px; at 430 px wide display math scrolls inside its own box (`overflow-x: auto`), not the page.

## Judgment calls (my authority)
- Each deck had one editor, so each package also did its own deck's Contents, divider subtitles, recap and note front matter; I did outlines, counts and verification.
- opt01: the illustration matrix A=[[3,0],[4,5]] stays where slides already used it (S80, S29, S30, S52, S53, S50, S73, S70), restated each time; "running example" wording replaced by "illustration matrix" everywhere. S52 and S73 muted lines that pointed to the deleted worked slides were restated inline (mechanical neighbour fix).
- opt01 S80: storage aside moved to S124 rather than squeezed.
- opt02 S131: full-sequence limit as a scope line under the table instead of a fourth column.
- Took all plan "prefer" layouts.

## Facts flagged / removed
- Removed from the S51 note (H and M) an editor-added remark that "MML §4.5.3 states the symmetric case without the PSD condition" — not in evidence, not verified.
- S44 note keeps the baseline reference Golub & Van Loan, *Matrix Computations* 4th ed., ch. 8, now also used for "practical SVD algorithms work on A directly". The reference was already in the baseline note's list; the chapter pointer is not in evidence.md — unverified, flag for review.
- Earliest priority for the convex / strongly convex fixed-step rates: not asserted anywhere (per E06/E07).

## Plan issues
None.
