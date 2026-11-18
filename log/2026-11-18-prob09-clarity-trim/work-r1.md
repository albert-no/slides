# work-r1 — job 2026-11-18-prob09-clarity-trim

## Branch and commits

- Branch `2026-11-17-prob09-major-revision` (PR #77 continuation). The baseline is 5f4b1d9 (86 slides). The result has 70 slides. No new ID commit: stable IDs are inherited from c47b198.
- ab0a557: log, job files copied.
- 018dcbd: pre-pass.
  - Retired S33/S37 (C03) and the gradient chapter S83–S128 plus S109b (C11).
  - Title subtitle, five-part Contents, S03/S99 dividers, note front matter; pace lines removed (C13).
- 6917e2c: P4, RL section.
- a4ed878 → merge 02e8997: P3, unknown Z.
- d26be5a → merge a08c018: P1, motivation, SE and rare event.
- 9fa85e8 → merge d4de37e: P2, IS contributions, zero variance and tails.
- 4eceaf9: integration.
  - Evidence-label convention; global renumbering of the note headings; `[[Sxx]]` resolved; `1 / 70`; `\text{IID}` everywhere.
  - Dead CSS and reference items removed; OUTLINE.md updated; narrow-width display splits in H.
- Head: this commit (work-r1 plus refreshed living files).

## Packages

- **P1 (C01, C02, C04).**
  - New S130 "One-Hot Cross-Entropy Equals KL" and S131 "Population Loss Requires an Average".
  - S04 rewritten as "Sampled Replies Estimate Pass Rate".
  - S114 "Standard Error Measures Estimator Spread": SE defined on the slide (C02).
  - S116 split into S116a "Small Absolute Error Can Hide Failure" (generic Bernoulli toy, ρ=0.001, n=1000) and S116b "Relative Error Needs Enough Hits".
  - `gen/p9a_part01.py` reproduces: P(no hit)=0.3676954248; n ≥ 99,900 for 10% relative RMSE; relative RMSE 0.9995 at n=1000.
  - The old per-draw SD figure `fig/p9a-rare-sd.svg` moved into H S116b; the S114 tails line moved to H/M.
- **P2 (C05, C06, C07, C08).**
  - S118 "Average Weighted Contributions to Estimate the Target" defines fw and μ in the diagram (C05).
  - S57 restructured around one message (C06).
  - S63 split into S63a "Random Draws Can Give Identical Contributions" and S63b "Constant Contributions Give Zero Estimator Variance". The variance is that of the contributions/estimator, not of X (C07).
  - S69 split into S69a "A Heavier Proposal Helps This Integrand" (Var 5/27, ratio 5.4) and S69b "Heavier Tails Are Not a Requirement" (counterexample Exp(1.5), Var 29/3) (C08).
  - `gen/p9b_calc.py` and `gen/p9b_figs.py` updated; added `fig/p9b-identical.svg` and `fig/p9b-var.svg`; deleted `fig/p9b-oracle.svg`.
- **P3 (C09, C10).**
  - New S132 "Bayes Leaves a Normalizing Integral" (figure `fig/p9f-bayes.svg`) and S133 "Likelihood Weights Remove the Unknown Z".
  - S73 gained the toy line; IID on S76/S77.
  - `gen/p9f_unknown_z.py`: Z=0.29337903585809, numerator 0.19006855378714, μ=0.64786003959422; seeded batch (seed 20261118, n=10000) μ̂_SN=0.6480.
- **P4 (C11, C12).**
  - S106 rewritten as "RL Objectives Contain Expectations" (estimation framing, no score gradients).
  - S104 gained a one-line advantage definition. S100/S101 changed in the notes only (gradient framing removed). Mohamed et al. sources dropped.
  - `gen/p9d_gradient_checks.py` deleted; the E21 gradient check removed from `gen/p9e_kl_counterexample.py`.

## Slide mapping

`slide ID | old page | new page | status`

| ID | old | new | status |
|---|---|---|---|
| S01 | 1 | 1 | edited (pre-pass) |
| S02 | 2 | 2 | edited (pre-pass) |
| S03 | 3 | 3 | edited (pre-pass) |
| S130 | — | 4 | new (P1) |
| S131 | — | 5 | new (P1) |
| S04 | 4 | 6 | rewritten (P1) |
| S06 | 5 | 7 | IID |
| S26 | 6 | 8 | unchanged |
| S16 | 7 | 9 | IID |
| S19 | 8 | 10 | unchanged |
| S22 | 9 | 11 | unchanged |
| S114 | 10 | 12 | rewritten (P1) |
| S115 | 11 | 13 | unchanged |
| S24 | 12 | 14 | unchanged |
| S116a | 15 | 15 | split of S116 (old p15) (P1) |
| S116b | 15 | 16 | split of S116 (old p15) (P1) |
| S41 | 16 | 17 | unchanged |
| S43 | 17 | 18 | unchanged |
| S44 | 18 | 19 | unchanged |
| S45 | 19 | 20 | unchanged |
| S50 | 20 | 21 | unchanged |
| S46 | 21 | 22 | unchanged |
| S47a | 22 | 23 | unchanged |
| S47b | 23 | 24 | unchanged |
| S48 | 24 | 25 | unchanged |
| S49 | 25 | 26 | IID |
| S117 | 26 | 27 | unchanged |
| S118 | 27 | 28 | rewritten (P2) |
| S119 | 28 | 29 | unchanged |
| S120 | 29 | 30 | unchanged |
| S54 | 30 | 31 | unchanged |
| S55 | 31 | 32 | unchanged |
| S56 | 32 | 33 | unchanged |
| S57 | 33 | 34 | rewritten (P2) |
| S59 | 34 | 35 | unchanged |
| S60 | 35 | 36 | unchanged |
| S61 | 36 | 37 | unchanged |
| S63a | 37 | 38 | split of S63 (old p37) (P2) |
| S63b | 37 | 39 | split of S63 (old p37) (P2) |
| S64 | 38 | 40 | unchanged |
| S66 | 39 | 41 | unchanged |
| S68 | 40 | 42 | unchanged |
| S121 | 41 | 43 | IID |
| S69a | 42 | 44 | split of S69 (old p42) (P2) |
| S69b | 42 | 45 | split of S69 (old p42) (P2) |
| S72 | 43 | 46 | notes only (integration) |
| S132 | — | 47 | new (P3) |
| S73 | 44 | 48 | edited (P3) |
| S74 | 45 | 49 | IID |
| S75 | 46 | 50 | unchanged |
| S133 | — | 51 | new (P3) |
| S76 | 47 | 52 | IID (P3) |
| S77 | 48 | 53 | IID (P3) |
| S78 | 49 | 54 | unchanged |
| S122 | 50 | 55 | unchanged |
| S70 | 51 | 56 | unchanged |
| S79 | 52 | 57 | unchanged |
| S81 | 53 | 58 | unchanged |
| S82 | 54 | 59 | unchanged |
| S99 | 75 | 60 | edited (pre-pass) |
| S100 | 76 | 61 | notes only (P4) |
| S101 | 77 | 62 | notes only (P4) |
| S102 | 78 | 63 | unchanged |
| S103 | 79 | 64 | unchanged |
| S129 | 80 | 65 | unchanged |
| S105 | 81 | 66 | unchanged |
| S106 | 82 | 67 | rewritten (P4) |
| S104 | 83 | 68 | edited (P4) |
| S109a | 84 | 69 | unchanged |
| S113 | 86 | 70 | unchanged |

Retired (23): S33(p13) S37(p14) S83(p55) S84(p56) S85(p57) S123(p58) S124(p59) S125(p60) S126(p61) S86(p62) S87(p63) S88(p64) S89(p65) S90(p66) S92(p67) S93(p68) S94(p69) S96a(p70) S96b(p71) S97(p72) S127(p73) S128(p74) S109b(p85).
"IID" means only `iid`→`IID` changed on the slide.

## Deviations from the plan

1. **S33/S37** were retired in the pre-pass rather than in a package, because the deletion is mechanical and they share no material with other slides.
2. **p9d generator** deleted together with the E21 check in `p9e_kl_counterexample.py`. Both verified only the retired gradient chapter; no remaining slide or note cites them.
3. **S73**: the muted line "Knowing p ∝ p̃ gives no value of p/q" was removed for density. Its content is already in the slide's diagram ("w = p/q blocked without Z") and in the H/M notes.
4. **S63a**: the identity $Y = f p/q^* = e^{-10}$ is a single inline line under the schematic rather than a display block, to fit the vertical budget without shrinking type.
5. **Figure widths** (layout choice): `p9b-identical.svg` on S63a is capped at max-width 880 px, leaving room for the identity line and the highlight. `p9b-var.svg` on S69a is capped at 1000 px for label legibility (DESIGN_SYSTEM §8).
6. **Evidence labels.** Both jobs number their evidence E01…, so a bare label was ambiguous. H and M Conventions now state: a bare E## is the 2026-11-17 record; "evidence 2026-11-18 E##" is this job's record. All this-job citations in D/H/M are prefixed.
7. **S116a/b numbering**: the toy uses ρ=0.001, n=1000 (expected hits 1) on S116a, and S116b reuses the same pair. Per requests.md C04, the exponential case's numbers are not previewed.
8. **Moved from slides to notes (H and M):**
   - e^-1 and the 8100× ratio (S118)
   - signed f·p (S57)
   - E_q[w²]=4/3 (S69a)
   - the λ-family formula (S69b)
   - the tails remark (S114)
   - the per-draw SD figure (S116b)
9. **S72 notes** gained one sentence introducing the concrete Bayesian case before the general statement.

## Plan issues

None.

## Unsourced facts

None found. Every displayed number is reproduced by a generator run (p9a, p9b_calc, p9f) or by exact arithmetic checked by hand: the λ-family second moment 2/(λ(2−λ)³), 5/27, 29/3, and the S63a identity. External claims cite evidence entries.

## Checks

- **lint-deck**: ok, no errors or font-size warnings.
- **find-wordy**: 2 review prompts (S59 theorem statement at 16 words; S104 advantage line at 16 words). Both are §1 bounded exceptions and render on one line.
- **find-dense**: prompts on S131, S04, S63b and S133. Their renders are clean.
- **outline-lint**: 0 stale pointers.
- **H/M**: 70 = 70 = 70 sections, IDs in deck order, headings sequential.
- **Narrow check of H**: clean at 430 px. At 360 px residual overflows remain:
  - S22 +12, S47b +9 (both as in the baseline)
  - S69a +35 (the baseline S69 block)
  - S69b +26, S130 +5 (new)
- **Render (-r 60), full deck rendered after integration.** Read pages 1–7, 9, 12, 15, 16, 26, 28, 34, 38, 39, 43–45, 47–49, 51–53, 60, 67–70. That covers every new, split or rewritten slide, plus the IID-changed slides and their neighbours at the part boundaries. No clipping, overlap or bad breaks.
