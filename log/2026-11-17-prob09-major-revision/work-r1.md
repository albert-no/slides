# work-r1 — prob09 major revision, round 1 build

- Branch: `2026-11-17-prob09-major-revision`, built from baseline `b20ab73ac7e74e9489d379cf9caad7565f17e31e`. The reviewable head is the commit named in the pointer, and it contains this file.
- Setup commit A: `08e7f86`. Touches only the HTML note and adds 113 unlabelled `<article>` wrappers.
- Setup commit B, the ID commit: `c47b198`. Adds `data-slide-id` S01–S113 to the 113 deck slides and the 113 note articles. Please record this as `id commit`. Content diff: `git diff c47b198 <head>`.
- Plan files: `plan-v1.md` and `plan-v2.md` are copied unchanged. `job.md`, `requests.md` and `evidence.md` are refreshed from the working folder at this push.

## Setup equivalence checks (rerun for this report)

| Check | Result |
|---|---|
| Commit A with every `<article>`/`</article>` tag removed, compared with the baseline note after whitespace normalization | identical |
| Commit B note with every ` data-slide-id="…"` removed, compared with the commit A note | byte-identical |
| Commit B deck with every ` data-slide-id="…"` removed, compared with the baseline deck | byte-identical |
| `git diff 08e7f86 c47b198` | 2 files, 226 lines changed. Each changed line is one ID attribute. |
| Render of the note at 1280 px and at 430 px, commit A against baseline (at setup time) | no visual change |

## Block-to-baseline assignment in commit A

- Every numbered `h2`/`h3` block of the baseline note went into the article of the first baseline slide it explains.
- The assigned slide numbers are strictly increasing in file order (asserted when the wrappers were built), so no block was out of order or relocated.
- 65 articles received blocks. The other 48 were empty scaffolds; none remain in the final note.
- The unnumbered `References` block was left outside the articles.

| baseline slide ID | baseline page | note blocks (h2/h3) assigned in commit A |
|---|---|---|
| S03 | 3 | 1  Why Sampling? |
| S04 | 4 | 1.1 The problem, stated once |
| S05 | 5 | 1.2 What “uncomputable” means here |
| S09 | 9 | 2  Recall — the Toolkit |
| S10 | 10 | 2.1 LOTUS, variance, linearity (prob01) |
| S11 | 11 | 2.2 LLN and Chebyshev (prob05) |
| S12 | 12 | 2.3 Hoeffding (prob06) |
| S13 | 13 | 2.4 What is genuinely new |
| S14 | 14 | 3  The Monte Carlo Estimator |
| S16 | 16 | 3.1 Definition, with conditions |
| S17 | 17 | 3.2 Theorem 1: unbiasedness, proof in full |
| S20 | 20 | 3.3 Theorem 2: variance, with the skipped step restored |
| S22 | 22 | 3.4 RMSE |
| S23 | 23 | 3.5 Guarantee I: Chebyshev, and consistency |
| S24 | 24 | 3.6 Guarantee II: Hoeffding, inversion derived |
| S25 | 25 | 3.7 Worked example: $\pi$ by darts, every number rechecked |
| S30 | 30 | 3.8 Guarantee two ways — verified, with a rounding note |
| S31 | 31 | 3.9 What Monte Carlo never asked |
| S32 | 32 | 4  Error Scaling & Dimension |
| S33 | 33 | 4.1 The remarkable absence |
| S34 | 34 | 4.2 The competitor: grid integration, with the $h^2$ claim derived |
| S35 | 35 | 4.3 Cost of accuracy, both methods |
| S38 | 38 | 4.4 The crossover at $d = 4$ |
| S39 | 39 | 4.5 Honest caveats, slightly expanded |
| S41 | 41 | 5  Importance Sampling |
| S42 | 42 | 5.1 Two failure modes of vanilla MC |
| S46 | 46 | 5.2 Theorem 3: the IS identity, support condition made precise |
| S48 | 48 | 5.3 The counterexample, computed in full |
| S49 | 49 | 5.4 The IS estimator and its unbiasedness |
| S50 | 50 | 5.5 Weights are likelihood ratios — and a condition worth flagging |
| S52 | 52 | 5.6 The tailored proposal on the rare event, verified |
| S55 | 55 | 6  The Variance of IS |
| S56 | 56 | 6.1 The variance formula |
| S57 | 57 | 6.2 The object to watch |
| S58 | 58 | 6.3 Jensen recalled, with the equality case proved |
| S59 | 59 | 6.4 Theorem 4: the optimal proposal, proof and equality analysis in full |
| S63 | 63 | 6.5 Zero variance verified on the rare event |
| S66 | 66 | 6.6 The infinite-variance example, computed in full |
| S70 | 70 | 6.7 Weight degeneracy: the finite-$n$ face |
| S72 | 72 | 7  Self-Normalized IS |
| S73 | 73 | 7.1 The missing constant and unnormalized weights |
| S75 | 75 | 7.2 SNIS defined |
| S76 | 76 | 7.3 Two MC estimators, one ratio |
| S77 | 77 | 7.4 Consistency, with the continuous-mapping step closed |
| S78 | 78 | 7.5 Bias: the ratio-estimator argument, in full |
| S79 | 79 | 7.6 ESS: derivation, not just definition |
| S81 | 81 | 7.7 What ESS is not |
| S82 | 82 | 7.8 Where SNIS runs |
| S83 | 83 | 8  The Score-Function Gradient |
| S84 | 84 | 8.1 A new kind of problem |
| S86 | 86 | 8.2 The log-derivative trick |
| S87 | 87 | 8.3 Theorem 5, proof in full (finite case) |
| S92 | 92 | 8.4 The REINFORCE estimator and its unbiasedness |
| S93 | 93 | 8.5 Worked check: the two-action sigmoid policy, every number verified |
| S96 | 96 | 8.6 The baseline lemma, with the variance computation the deck omits |
| S98 | 98 | 8.7 Reading the identity, and the pipeline |
| S99 | 99 | 9  Off-Policy & RLHF |
| S100 | 100 | 9.1 Off-policy is Theorem 3 |
| S102 | 102 | 9.2 Sequences multiply weights (chain rule, proved) |
| S103 | 103 | 9.3 Degeneracy grows with length: the caricature, made precise |
| S104 | 104 | 9.4 Keep the ratio near one |
| S105 | 105 | 9.5 KL recalled, and one connection made explicit |
| S106 | 106 | 9.6 The RLHF-shaped objective |
| S107 | 107 | 10  What the Deck Leaves Out; 10.1 When IS fails in high dimension: degeneracy as a theorem; 10.2 Reparameterization vs. REINFORCE (the estimator comparison the deck hints at) |
| S109 | 109 | 10.3 The bias–variance trades, collected; 10.4 Smaller pointers |
## Per-package outcome

The packages were built in parallel, one worktree each, and merged in this order: P1, P3, P4, P5, P2. Scope checks against each merge base showed that every package touched only its own IDs, its own note articles and Markdown blocks, and its own CSS prefix.

| Package | Commit | Slides | Outcome |
|---|---|---|---|
| P1, Part 01 | `30d5371` | 12 (S04–S116) | Inline-SVG exhibits. Generator `gen/p9a_part01.py`. S19 uses an exact Bin(6, π/4) exhibit. S37 shows d = 2, 8 and 20. Retired recall and proof material went to the S16/S19/S22/S24/S115/S37 notes. |
| P2, Parts 02–03 | `bc63086` | 25 | Covers the IS identity, the split proof S47a/S47b, optimal proposal S59–S61, and the variance-risk examples S63–S69. Generators `gen/p9b_calc.py` and `gen/p9b_figs.py`. The S64 Sources line was corrected to cite E04. |
| P3, Part 04 | `e771e50` | 11 | Covers the SNIS, ESS and diagnostics slides S73–S82, S122, S70 and S79. Generator `gen/p9c_snis_examples.py`. The S70/S79 notes absorb retired S71 and S80. |
| P4, Part 05 | `85c0836` | 19 | Covers pathwise and score-function gradients, the finite-space proof, and the baselines S96a/S96b, S97, S127 and S128. Generator `gen/p9d_gradient_checks.py`. |
| P5, Part 06 | `663f56e` | 8 | Covers sample reuse, behavior vs reference, KL vs weight variance, scoped RLHF, and PPO clipping using unmodified crops of PPO Fig. 1. Generators `gen/p9e_compounding.py` and `gen/p9e_kl_counterexample.py`. |
| Integration | `bb52375`, `0f1b690`, `fdfa73a`, `8dfe5dd`, `8fee239`, `1667b63`, `5954c21`, then fixes | 10 structural slides plus shared surfaces | See below. |

**Integration work:**
- The 85-slide scaffold and retirement removals.
- Title subtitle, six-part Contents and dividers (S01–S03, S41, S55, S72, S83, S99).
- The S109 synthesis table.
- Structural note articles and Markdown blocks.
- Comments between slides that name each slide's ID and title, plus part banners.
- Note preamble: purpose and audience, how to use, conventions.
- Pace lines per part.
- A rebuilt 9-entry References list. Kong was dropped because no article cites it.
- Markdown part headings and a References section.
- Note references by slide ID were rewritten as page numbers.
- The `OUTLINE.md` entry.
- Notation reconciliation: `\hat\mu_n`, `\hat\mu_{\mathrm{IS}}`, `\hat\mu_{\mathrm{SN}}`, `\pi_{\text{ref}}`, `\ln`. The one remaining `\log` sits inside the quotation of Ouyang's objective.
- Theorem titles unnumbered: "Theorem (importance-sampling identity / optimal proposal / score-function identity)".
- Post-audit fixes: S16 underbrace spacing; S44 lead line; role and aria-label on 15 figure SVGs: 8 had no label and 7 had `role="img"` without text.

## Count and pacing

- Final count: 85 slides, 85 HTML note articles and 85 Markdown blocks, all in the same ID order.
- Every slide sits on its plan-v2 target page, so the per-part counts and time budgets are as planned. The note's pace lines state them:

| Part | Pages | Slides | Minutes | Elapsed at start |
|---|---|---|---|---|
| Opening + Part 01 | 1–15 | 15 | 25 | 0 |
| Part 02 | 16–30 | 15 | 25 | 25 |
| Part 03 | 31–42 | 12 | 25 | 50 |
| (break) | | | | 75 |
| Part 04 | 43–54 | 12 | 20 | 75 |
| Part 05 | 55–74 | 20 | 35 | 95 |
| Part 06 | 75–83 | 9 | 15 | 130 |
| Closing | 84–85 | 2 | 5 | 145 |

- Baseline accounting: 113 baseline IDs. 4 are on the same page, 61 moved, 2 split (S47 into S47a/S47b, S96 into S96a/S96b) and 46 retired, following the plan-v2 disposition table. The 16 new IDs are S114–S129.

## Slide mapping

"—" means the ID has no page on that side. Retired IDs follow the plan-v2 disposition table; their kept details are in the notes named there.

| slide ID | old page | new page | split/moved/retired |
|---|---|---|---|
| S01 | 1 | 1 | kept |
| S02 | 2 | 2 | kept |
| S03 | 3 | 3 | kept |
| S04 | 4 | 4 | kept |
| S05 | 5 | — | retired |
| S06 | 6 | 5 | moved |
| S07 | 7 | — | retired |
| S08 | 8 | — | retired |
| S09 | 9 | — | retired |
| S10 | 10 | — | retired |
| S11 | 11 | — | retired |
| S12 | 12 | — | retired |
| S13 | 13 | — | retired |
| S14 | 14 | — | retired |
| S15 | 15 | — | retired |
| S16 | 16 | 7 | moved |
| S17 | 17 | — | retired |
| S18 | 18 | — | retired |
| S19 | 19 | 8 | moved |
| S20 | 20 | — | retired |
| S21 | 21 | — | retired |
| S22 | 22 | 9 | moved |
| S23 | 23 | — | retired |
| S24 | 24 | 12 | moved |
| S25 | 25 | — | retired |
| S26 | 26 | 6 | moved |
| S27 | 27 | — | retired |
| S28 | 28 | — | retired |
| S29 | 29 | — | retired |
| S30 | 30 | — | retired |
| S31 | 31 | — | retired |
| S32 | 32 | — | retired |
| S33 | 33 | 13 | moved |
| S34 | 34 | — | retired |
| S35 | 35 | — | retired |
| S36 | 36 | — | retired |
| S37 | 37 | 14 | moved |
| S38 | 38 | — | retired |
| S39 | 39 | — | retired |
| S40 | 40 | — | retired |
| S41 | 41 | 16 | moved |
| S42 | 42 | — | retired |
| S43 | 43 | 17 | moved |
| S44 | 44 | 18 | moved |
| S45 | 45 | 19 | moved |
| S46 | 46 | 21 | moved |
| S47 | 47 | — | split → S47a, S47b |
| S47a | — | 22 | split from S47 |
| S47b | — | 23 | split from S47 |
| S48 | 48 | 24 | moved |
| S49 | 49 | 25 | moved |
| S50 | 50 | 20 | moved |
| S51 | 51 | — | retired |
| S52 | 52 | — | retired |
| S53 | 53 | — | retired |
| S54 | 54 | 30 | moved |
| S55 | 55 | 31 | moved |
| S56 | 56 | 32 | moved |
| S57 | 57 | 33 | moved |
| S58 | 58 | — | retired |
| S59 | 59 | 34 | moved |
| S60 | 60 | 35 | moved |
| S61 | 61 | 36 | moved |
| S62 | 62 | — | retired |
| S63 | 63 | 37 | moved |
| S64 | 64 | 38 | moved |
| S65 | 65 | — | retired |
| S66 | 66 | 39 | moved |
| S67 | 67 | — | retired |
| S68 | 68 | 40 | moved |
| S69 | 69 | 42 | moved |
| S70 | 70 | 51 | moved |
| S71 | 71 | — | retired |
| S72 | 72 | 43 | moved |
| S73 | 73 | 44 | moved |
| S74 | 74 | 45 | moved |
| S75 | 75 | 46 | moved |
| S76 | 76 | 47 | moved |
| S77 | 77 | 48 | moved |
| S78 | 78 | 49 | moved |
| S79 | 79 | 52 | moved |
| S80 | 80 | — | retired |
| S81 | 81 | 53 | moved |
| S82 | 82 | 54 | moved |
| S83 | 83 | 55 | moved |
| S84 | 84 | 56 | moved |
| S85 | 85 | 57 | moved |
| S86 | 86 | 62 | moved |
| S87 | 87 | 63 | moved |
| S88 | 88 | 64 | moved |
| S89 | 89 | 65 | moved |
| S90 | 90 | 66 | moved |
| S91 | 91 | — | retired |
| S92 | 92 | 67 | moved |
| S93 | 93 | 68 | moved |
| S94 | 94 | 69 | moved |
| S95 | 95 | — | retired |
| S96 | 96 | — | split → S96a, S96b |
| S96a | — | 70 | split from S96 |
| S96b | — | 71 | split from S96 |
| S97 | 97 | 72 | moved |
| S98 | 98 | — | retired |
| S99 | 99 | 75 | moved |
| S100 | 100 | 76 | moved |
| S101 | 101 | 77 | moved |
| S102 | 102 | 78 | moved |
| S103 | 103 | 79 | moved |
| S104 | 104 | 83 | moved |
| S105 | 105 | 81 | moved |
| S106 | 106 | 82 | moved |
| S107 | 107 | — | retired |
| S108 | 108 | — | retired |
| S109 | 109 | 84 | moved |
| S110 | 110 | — | retired |
| S111 | 111 | — | retired |
| S112 | 112 | — | retired |
| S113 | 113 | 85 | moved |
| S114 | — | 10 | new |
| S115 | — | 11 | new |
| S116 | — | 15 | new |
| S117 | — | 26 | new |
| S118 | — | 27 | new |
| S119 | — | 28 | new |
| S120 | — | 29 | new |
| S121 | — | 41 | new |
| S122 | — | 50 | new |
| S123 | — | 58 | new |
| S124 | — | 59 | new |
| S125 | — | 60 | new |
| S126 | — | 61 | new |
| S127 | — | 73 | new |
| S128 | — | 74 | new |
| S129 | — | 80 | new |
## Deviations from the plan

1. **S104 uses r for the PPO probability ratio.** This matches the unmodified PPO Fig. 1 crop and is defined on the slide. It clashes with the note convention "r = learned reward". Alternative: relabel the ratio in the slide text and keep the crop as published.
2. **S105 shows the E14 numbers on the slide** (KL 0.00174 nats against E_q[w²] ≈ 10001). The plan put them in the note. They are the slide's evidence.
3. **S19 uses an exact binomial exhibit** (Bin(6, π/4) distribution of the six-dart estimate) instead of a simulated one.
4. **S37 shows d = 2, 8 and 20.** The d = 4 line coincides with the MC line; that case is explained in the note.
5. **S33** dropped its second bullet.
6. **S109's worked examples** moved to its note, so the synthesis table fits without shrinking type.
7. **S106's citation line** drops "not a survey"; the subtitle carries the scope.
8. **S122 adds an exact MSE toy** (IS against SNIS at n = 1) that the plan did not ask for.
9. **S44's qualifier** "a spread target, not a 95% guarantee" moved into the lead line, so the slide fits its vertical budget. "Not a runtime" stays in the S44 note.
10. **Large empty areas** remain on pages 4, 41, 64 and 68. That is Priority 3; nothing was added to fill them.

## Plan issues (decision needed)

1. **S26 title and E17.** The title is "Six Draws Give a Noisy Estimate", but the six points come from E17 and are hand-chosen, not a random run. The slide says "hand-chosen, not a random run". Keep, or change the title?
2. **E10 locator is wrong.** The Ouyang objective is in arXiv v1 §3.5, eq. (2). The NeurIPS version has it only as prose, in §3.4. The note cites arXiv v1 §3.5, eq. (2). evidence.md needs a correction entry.
3. **Generator paths differ from evidence.md.** E12 and E19 are produced by `gen/p9c_snis_examples.py`, and E13 by `gen/p9d_gradient_checks.py`.
4. **Our own derivations with no evidence entry:**
   - the S122 bias expansion, labelled heuristic in the note;
   - the S122 MSE toy;
   - the dominated-convergence conditions in the S87 and S124 notes;
   - the baseline variance formula Var(g_b) − Var(g_0) = E[s²]·b(b − 2b*) in the S96b note;
   - the |V|^T direct-counting argument in P1's note.
   Each is derived in full in its note. Please add E entries or accept them as our calculation.
5. **b = 2b\* ties with b = 0.** In the toy, b\* = 1/2 and b = 1 gives the same variance as b = 0. A constant baseline strictly reduces variance only when 0 < b < 2b\*; the general formula is in the S96b note. Please confirm the strict-improvement wording in the S96b/S97/S127 notes.
6. **Action naming.** The two-action example names its actions a_1 (R = 1) and a_0 (R = 0).
7. **No evidence entry for the Bayes-rule context** in the S73 and S82 notes.
8. **Continuity with opt01.** The opt01 outline entry still says it "answers prob09's bridge", but the bridge slides (S112 and others) are retired. opt01 is out of scope and was not touched.
9. **Midpoint-rule rate attribution.** The m^{-2} rate is attributed to E03 (Owen, quadrature chapter §§7.1, 7.4). Please confirm that E03 covers it.

## Unsourced facts

- No new external facts were added without an E entry.
- Our own calculations are listed in plan issue 4.
- Every number on the slides is recomputed by a generator below.
- Facts not repeated from memory: none were corrected from recall. Kong's "§7.6" reference was stale and was dropped together with the Kong entry, not re-located.

## Generators (all under `courses/deepmath/prob09-monte-carlo/gen/`)

After running all seven from a clean tree, `git status` showed no changes, so the committed figures and numbers are reproducible byte for byte.

| Script | Inputs / seed | Produces |
|---|---|---|
| `p9a_part01.py` | exact; no seed | Darts σ_f² = π(4 − π); the S19 Bin(6, π/4) pmf; S22 RMSE curve; S115 Chebyshev n = 539,354; S24 Hoeffding n = 295,111; S37 schematic; S116 curves and n ≥ 2,202,547 |
| `p9b_calc.py` | exact; no seed | E11 rare-event numbers; IS n = 1331, speedup 1654.8; relative second moment e/0.19 = 14.3067 |
| `p9b_figs.py` | deterministic; no seed | Part 02–03 figures, schematic and illustrative ones labelled as such |
| `p9c_snis_examples.py` | exact fractions; no seed | S78 biases; S122 MSE and n·bias table; S70/S79 ESS 1.107; S81 |
| `p9d_gradient_checks.py` | exact fractions; Simpson on [−12, 12] with N = 24,000; seed 20261117 | Toy J′ values; baseline variances 1/16, 0 and 9/16 for b = 0, ½ and 2; Gaussian check and its draws |
| `p9e_compounding.py` | closed form; no seed | 1.1^T (13,780.6 at T = 100); `fig/p9e-compounding.svg` |
| `p9e_kl_counterexample.py` | closed form; no seed | E14: KL 0.00174 nats, E_q[w²] 10000.9998; E21 finite-difference check |

The PPO crops `fig/p9e-ppo-fig1-pos.png` and `fig/p9e-ppo-fig1-neg.png` were rendered with `pdftoppm` at 300 dpi from page 3 of arXiv:1707.06347v2. They are unmodified.

## Checks run

- **Lint.** `lint-deck.py` passes on the deck and the HTML note. `outline-lint.py` reports 0 stale pointers; its 5 warnings are pre-existing in other folders. `find-wordy`/`find-dense` flags reviewed and kept as bounded exceptions: S22, S37, S54, S59 and S128.
- **Structure.**
  - 85 unique IDs, in the same order in the deck, the HTML note and the Markdown.
  - No empty articles or placeholders.
  - Deck titles match note headings, apart from cosmetic differences on S01 and S113.
  - No numbered "Theorem N".
  - No forbidden phrases.
- **Render.**
  - Full deck rendered at 60 dpi (85 pages) and read by an audit subagent: no blockers.
  - I inspected pages 6, 7, 8, 9, 14, 15, 17, 18, 40, 44, 47, 49, 51, 52, 53, 54, 59, 72, 76, 77, 78, 80 and 83 myself.
  - After the fixes I re-rendered and inspected pages 7 and 18.
  - Each package rendered its own range: P1 pages 4–15, P3 44–54, P4 56–74 and P5 76–83.
- **Audit items not changed:**
  - S43: the inset's y-tick label sits slightly outside the inset frame. It is a generated figure and still readable.
  - S68, S124 and S101: their last lines clear the cite band at 60 dpi.
  - S127 and S128: the "Var" fractions are small but readable.
  - S104: the PPO crops stay at their current size. The slide's task is the clipping argument, not reading the figure.
  - The audit's S47b underbrace and S57 label notes were not re-inspected by me.
- **Accessibility.**
  - Note at 430 px and 1280 px: scroll width equals client width, 0 KaTeX errors, 85 articles.
  - Deck: 14 of 14 images have alt text. All 26 inline SVGs now carry an `aria-label` (25) or `aria-hidden` (1).
  - Markdown is pure ASCII, with LaTeX and readable "Part N" headings.
