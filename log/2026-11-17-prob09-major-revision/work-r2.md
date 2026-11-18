# work-r2 — prob09 major revision, round 2 (review-r1 fixes)

- Branch `2026-11-17-prob09-major-revision`. The head is the commit named in the pointer, and it contains this file. The round-2 content commits are `ea95e74` (F01 plus the F11 prob01 attribution) and `7bfa690` (F02–F14). Content diff for this round: `git diff 3f4bdd7 <head>`. The ID commit is still `c47b198`.
- `review-r1.md` was copied unchanged at its pointer (`fb95d79`). `job.md`, `requests.md` and `evidence.md` are refreshed at this push and are unchanged from the working folder.
- The deck has 86 slides (`1 / 86`). The deck, the HTML note and the Markdown edition each carry the same 86 IDs in the same order (checked by script).

## Slide mapping changes this round

| ID | r1 page | r2 page | change |
|---|---|---|---|
| S109 | 84 | — | split (F01) |
| S109a | — | 84 | "Choose an Expectation Estimator by Its Requirements": ordinary MC, IS, SNIS |
| S109b | — | 85 | "Choose a Gradient Estimator by Its Requirements": pathwise, score |
| S113 | 85 | 86 | closer, unchanged |
| S82 | 54 | 54 | retitled "What You Can Compute Decides What Is Available" (F06) |
| S26 | 6 | 6 | retitled "Six Points Illustrate the Recipe" (F14) |

No other slide was added, removed or moved.

## Findings

| ID | Resolution |
|---|---|
| F01 | S109 is split into S109a (expectation estimators, with the target's integrability and IID draws in the lead) and S109b (gradient estimators, with the target named as a gradient). Each claim now carries its conditions: the RMSE needs σ_f finite; IS variance is finite only if E_q[(fw)²] is finite; SNIS is "consistent; generally biased at finite n"; pathwise is "unbiased under those conditions"; score says "a constant baseline b keeps the mean". The highlight lines are "Unbiased or consistent is not low error" and "Available is not efficient". The note and the MD have one article each, and the MD pace line moved with them. |
| F02 | D S76 now says "generally dependent" in the label and in the aria-label. H and M say "with possible finite-sample bias" and "generally biased at finite sample sizes". The S76 details say expectation does not commute with a ratio because division is nonlinear and the two averages are generally dependent. |
| F03 | H and M S79 give the general IID limit ESS/n → (E_q[w])²/E_q[w²] for a positive finite mean and a finite second moment. They reduce it to 1/E_q[w²] only for w = p/q with full coverage, and add the four-state counterexample (E_q[w] = 3/4, E_q[w²] = 9/16, so the limit is 1, not 16/9). The S70 Message reads "One draw holds 95% of the normalized weight; its contribution still depends on f." |
| F04 | D S63: the right-hand side keeps the indicator, 1{x>10} e^{-(x-10)}, and the figure label is "q*(x) = e^{-(x-10)} / for x > 10" on two lines. Putting the label on two lines also fixes an overlap with the x = 10 dashed line that the render showed. H and M match: zero for x ≤ 10. |
| F05 | D S103: "Weight factors independent under π_b". H and M say the factors w_t are independent under π_b, here because both policies factor position by position. |
| F06 [judgment] | Taken as a nonexclusive capability map. S82 has three rows, each reading sufficient inputs → available estimator, with no yes/no branching. The lead reads "Each row lists sufficient inputs; several rows can hold at once". The closing line reads "These requirements tell us which estimators are available, not which is best". H and M are retitled and rewritten to match ("row" instead of "branch"). OUTLINE Part 04 is updated. |
| F07 | D S96b: "An action-dependent b(X) need not cancel: requires E[b(X) s_θ(X)] = 0". H and M state that the mean is preserved exactly under that condition. They add the assumptions E[R²s²] < ∞ and 0 < E[s²] < ∞ (zero score is the trivial case) and the vector form with trace conditions and b* = E[R‖s‖²]/E[‖s‖²]. The b(b − 2b*) < 0 criterion is kept. |
| F08 | 8.1: S48 Message is the reviewer's sentence (1/4). 8.2: D S54 validity reads "q > 0 wherever fp ≠ 0; E_p\|f\| < ∞". H and M add integrability, say missing coverage can bias the estimator (the four-state example), and separate an infinite second moment from a large finite one. 8.3: S64 Message reads "c, which is \|μ\| for a one-sign integrand and μ for this nonnegative indicator". 8.4: S121 Message is replaced with the reviewer's sentence. 8.5: H S128 and M S128 carry the ordinary-pathwise-formula sentence. 8.6: S24 reads "at most 0.05". S118 reads "f w = 0 up to 10" and "just above x = 10" in D, the aria-label, H and M. |
| F09 | H head has `<meta name="viewport" content="width=device-width, initial-scale=1">`. S94's expectation expansion is split into steps (two terms on separate lines, then the result) in H and M. Font sizes are unchanged. Per-article check (every `article` element, after fonts and KaTeX load) at 430 px: no element extends past the viewport, doc scrollWidth equals clientWidth, 0 KaTeX errors, 86 articles. S115 and S94 are clean. 1280 px is clean too. **Disclosure:** I added a note-local rule, `.katex-display { overflow-x: auto; overflow-y: hidden; }`. It has no effect at 430 px or wider, where nothing overflows. At 360 px it makes three long displays (S19, S22, S116) scroll inside their own box instead of widening the page. If you read this as a forbidden workaround, I will remove it; the 430 px result does not depend on it. **Limit:** I ran the 430 px check in an iframe of that width, where the viewport meta makes the layout width 430. I did not run a separate device-emulation pass with a scale factor, because the headless toolchain here has no emulation driver. |
| F10 | 10.1: S64 has no ↺ glyph; the loopback is the text "Circular: the weight needs c, and here c = μ is the answer". S121 boxes read "LLN: μ̂_IS → μ" and "no finite RMSE, no usual CLT bar", with no ✓ or ✗. The notes have no ✓, ✗ or ↺. (D S54 keeps ✓ beside Exp(0.1); it renders correctly.) 10.2: S122 cells read "q covers fp" and "q covers all of p", and a note-local rule adds 36 px between columns. The full-target versus fp distinction is kept, and the table type is unchanged; the render shows clearly separate cells. The M table line matches. 10.3: S88 underbraces read "changes" and "fixed"; the lead reads "A finite expectation is a weighted sum over fixed outcomes; only the weights depend on θ". 10.4: S101 drops the grey p/q identity and keeps only the relabelled policy identity; the lead line names the IS identity. H S101 now says "The lead line names the importance-sampling identity…". 10.5: S125 is one line per column: J = θ² + 1, J′ = 2θ / ∂_θ(θ+ε)² = 2X, E[2X] = 2θ. The expansions stay in H and M. 10.6: S96a proof has three lines: definition and log-derivative, finite sum, total probability. The full steps stay in H and M. |
| F11 | Prerequisites in H, M and OUTLINE: prob01 is LOTUS and Jensen; prob05 is the mean and variance of a sample mean, LLN, Chebyshev and CLT; the variance attribution to prob01 is gone. OUTLINE prob09: 86 slides (header and the root status row), synthesis row "expectation estimators (S109a), gradient estimators (S109b); closer", pages 84–86, S116 description, S82 description, and every line pointer recomputed. The prob08 Gaussian-construction link (pathwise X = θ + ε) is named in the prerequisite sentence. opt01 prose: "begins the optimization half after prob09 closes the probability sequence", without naming any deck on-slide. Only these OUTLINE lines changed. `outline-lint`: 0 stale. |
| F12 | 12.1: S125 sources in H and M cite E15 (Gaussian reparameterization example) and E24 (`gen/p9d_gradient_checks.py`) instead of E13. The other E13 citations were checked and are correct. 12.2: M uses `q(4)=0\lt p(4)`; the MD lint now reports no ERROR. 12.3: S100 descriptions in H and M match the layout: on the left, the behavior box (amber) is stacked above the current box (blue); the estimate box is on the right. 12.4: S43: D cite adds "the tail continues past x = 14". H says the plot stops at 14 and μ is the whole tail past 10. M says the shaded patch is the tail up to 14 and the whole area past 10 is e^{-10}. The finite patch is no longer called the whole probability. |
| F13 [judgment] | Taken. S116 is a generic Bernoulli(ρ) bridge: "Event indicator Y ~ Bernoulli(ρ), so μ = ρ" plus the variance-versus-relative-RMSE line. The marker line, the two dots, the ≈148 and ≈0.0067 labels and the ρ = e^{-10} tick are removed; a neutral 10^{-4} tick replaces it. The aria-label is rewritten. The muted line is the lesson "At fixed n, smaller ρ: smaller absolute error, larger relative error". The plot's provenance moved to a cite line. H and M drop Exp(1), X > 10, e^{-10}, 2,202,547 and the 0.635 example. The no-hit illustration now reads (1−ρ)^n. Part 02 (S43/S44 and later) keeps all the concrete numbers. |
| F14 (optional) | Taken: S26 is "Six Points Illustrate the Recipe" in D, H and M. OUTLINE did not list the title. |

## Preferences and judgment calls

- F06 and F13: took the reviewer's suggested direction, as above.
- F14: taken.
- S109a/S109b: added fixed column widths (22/42/36%) to both synthesis tables. Without them the S109a highlight touched the footer in the render. Type is unchanged.
- F09: the `.katex-display` scroll rule, disclosed above.

## Plan issues

None.

## Checks run (at `7bfa690`; this report adds no source change)

- `lint-deck.py`: deck ok, HTML note ok. `lint-accessible-md.py`: no ERROR. The remaining warnings are the pre-existing visual-reference and slide-number style warnings. The MD is ASCII-only (grep for non-ASCII: none).
- `outline-lint.py`: 0 stale or missing pointers.
- ID order and pairing: deck, H articles and M blocks each hold the same 86 IDs in the same order, with no duplicates.
- Render at 60 dpi, every changed slide: pages 6, 15, 17, 27, 30, 37, 38, 41, 47, 50, 54, 60, 64, 70, 71, 77, 79, 84, 85. After the S63, S116 and S109a/b fixes, I re-rendered pages 15, 37, 84 and 85. No overflow, overlap, tofu or footer collision remains.
- Note at 430 px and 1280 px: per-article overflow check clean, 0 KaTeX errors, 86 articles.
