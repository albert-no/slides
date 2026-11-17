# work-r3 — prob09 major revision, round 3 (review-r2 fixes)

- Branch `2026-11-17-prob09-major-revision`. The round-3 content commit is `029fc74`; the head named in the pointer adds this file and the refreshed living files. Content diff for this round: `git diff 79b3163 029fc74`.
- `review-r2.md` was copied unchanged at its pointer (`5e2ffaa`). `job.md`, `requests.md` and `evidence.md` are refreshed at this push and match the working folder (`job.md` round 3, `evidence.md` through E31).
- Still 86 slides (`1 / 86`); no slide added, removed, moved or retitled. The deck, the HTML note and the Markdown edition keep the same 86 IDs in the same order.

## Findings

| ID | Resolution (all in `029fc74`) |
|---|---|
| F01 | D S109a: the bottom highlight ("Unbiased or consistent is not low error: check the second moment") is removed; the table keeps its 22/42/36% columns and type is unchanged. The warning lives in the note: H and M S109a say it is not on the slide and is said aloud ("unbiased or consistent does not mean low error; the second moment decides that"). M's description now says the slide has no highlight line. S109b keeps its highlight ("Available is not efficient"). |
| F09 | The note-local `.katex-display { overflow-x: auto; overflow-y: hidden; }` rule is removed from H. The long displays are split into steps in H and M: S19 `E[μ̂_n] = (1/n) Σ E[f(X_i)]` / `= (1/n)·nμ = μ`; S116 `RMSE(μ̂_n)/ρ = √(ρ(1−ρ)/(nρ²))` / `= √((1−ρ)/(nρ))`; S90 `Σ R ∇_θ p_θ` / `= Σ p_θ R s_θ` (the final ∎ spacing is `\quad`). Font sizes unchanged. |
| F15 | D S116 lead: "Rare ρ: small indicator variance ρ(1−ρ)" and "Relative RMSE = √((1−ρ)/(nρ)): small only with enough draws". Muted line: "At fixed n and 0 < ρ ≤ 1/2: rarer events lower absolute RMSE but raise relative RMSE". The aria-label ends "at rho = 1/2, absolute SD is 1/2 and relative SD is 1; the curves do not meet on the displayed range." H and M match: relative RMSE is small only when n is large compared with 1/ρ; the fixed-n comparison is stated for 0<ρ≤1/2 and as a distribution-level RMSE, not the error of one run; the ρ = 1/2 endpoint values are stated. Still generic: no Exp(1), e^{-10} or the run-size numbers. Facts as in E31. |
| F16 | Taken: H S109b no longer says "as the Gaussian comparison did". (M had no such phrase.) |

## Preferences and judgment calls

- F16 taken. No other judgment calls this round.

## Plan issues

None.

## Checks run (at `029fc74`)

- `lint-deck.py`: deck ok, HTML note ok. `lint-accessible-md.py`: 0 ERROR. The MD is ASCII-only (no non-ASCII bytes).
- `outline-lint.py`: 0 stale or missing pointers. OUTLINE is unchanged: no title, slide or section change, and its S116 / synthesis descriptions still hold.
- Note math, per `.katex-display` (after fonts and KaTeX load, `svg` radical artifacts and `.hide-tail` excluded): no glyph extends past its parent's content box and no display scrolls, at true-mobile 430 (iframe 445 → clientWidth 430), narrow-desktop 430 (iframe 430 → 415) and 1280. Whole note at 430: document scrollWidth = clientWidth, 0 KaTeX errors, 86 articles.
- Visual check at 430: screenshots of the S19, S116 and S90 displays show the lower limits (i=1, x), fractions and radicals fully visible, with no clipping or scrollbar on the display.
- Deck render at 60 dpi: pages 15 (S116), 84 (S109a), 85 (S109b), 86 (closer). S116 lead and muted lines fit on one line each; S109a ends after the table with no overflow or footer collision; no tofu.
- **Limit (unchanged from r2):** no device-emulation pass with a scale factor; true-mobile 430 is the iframe-width approximation above.
