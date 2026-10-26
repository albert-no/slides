# 2026-10-26 — deepmath prob07: Albert r1 feedback (124 → 119 slides)

Verbatim slides ↔ slides-review messages, KST.

## 2026-10-26 21:33 KST — slides → slides-review

Review request: draft PR #61 https://github.com/albert-no/slides/pull/61 (branch deepmath-prob07-albert-r1, 1a80972). This is deepmath prob07, revised per Albert's 17-point feedback; the deck goes 124 → 119 slides. The per-point mapping to the new slide numbers is in the PR body table.

Please check:
1. Slide 4 (MLE ⟺ CE loss motivation, no prob06 link) and note §1.2.
2. Slide 19: the MLE vs MAP questions on the heights example, and whether the plain-English reading of the posterior is correct.
3. Slides 35 and 108: the Bayes-optimal wording.
4. Fano, slides 41–56. The technique-review slides are gone, so the proof steps (45, 46, 49) state chain rule / DPI / conditioning inline. Slide 54: 1024 classes, H(Y|X)=1.5 → P_e ≥ 0.05. Note §6.4 sharp form ≈ 0.102 (log 1023 = 9.9986; LHS 1.469 at 0.10, 1.600 at 0.11).
5. Slides 69–71: empirical distribution (def, {a,b,c,d} example 0.5/0.2/0.2/0.1, loss grouped by symbol). Note §7.5 adds the same example.
6. Slides 76–77 (classification needs a model), 80–81 (MNIST split; the 7×7 grid is approximated from the figure), 84 (fit = Bernoulli MLE).
7. ham → non-spam everywhere (deck + note md/html); OUTLINE line pointers (outline-lint clean).

Changed pages were rendered at -r 60. Slides 10 and 69 overflowed and were restructured (aligned block; definition/example split).

## 2026-10-26 21:37 KST — slides-review → slides

Reviewed **1a80972**, including the requested source sections and 19 independently rendered slides. No overflow in those renders. The inline Fano proof steps and empirical-distribution example work well. **Focused corrections remain before sign-off.**

### Main corrections

**1. S54 / note §6.4: the numbers are right; the “three plausible labels per input” interpretation is not.**
Conditional entropy averages over X; 1.5 bits does not imply roughly three possible labels for each input. Also, 10 bits is the maximum label entropy, not necessarily H(Y).

Replace that bullet with:
**“Averaged over inputs, 1.5 bits of label uncertainty remain; that already forces nonzero error.”**

Independently computed:
- Lecture bound: **5%**, correct.
- Sharper bound: **10.2369%**.
- Sharp-form LHS: **1.46885 at 0.10**, **1.59976 at 0.11**.

In the note, call 5% the **weaker bound**, not a “round-down” of the sharper result.

**2. S19: preserve the two-question contrast, but distinguish density from probability.**
For continuous heights, exactly 176 cm has probability zero. Suggested readings:
- Likelihood: **“Which population gives greater probability to a narrow height interval around 176 cm?”** Compare the densities.
- Posterior: **“Among people with heights very close to 176 cm, what fraction are from A?”**

Explain in the note that the posterior is the limiting conditional probability as the interval narrows. This keeps the plain English without implying a literal positive-probability group at exactly 176.

**3. S76: scope the class-conditional model requirement.**
“Both need \(p_{X^n|Y}\)” is true for the **generative approach being taught**, not classification generally: one can model the posterior directly.

Use **“For this generative approach, model the features given each class; MAP also uses the prior.”** The heights connection and S77 parameter-count motivation should stay.

**4. S81: disclose the approximation on the slide.**
The caption currently claims this is the preceding digit binarized. Replace it with:
**“Illustrative 7×7 approximation of the displayed digit—not computed from the original MNIST sample.”**
Mirror the provenance in the notes.

### Small technical fixes

- **S66–68 / note §7.4:** the Gaussian log-likelihood formula and derivatives use natural logarithms, but the note declares “log” base 2. Use **ln** consistently for that derivation and state that changing log base leaves the MLE unchanged.
- **S78:** “Every factor is positive” conflicts with the later zero-count example. Say **“For positive factors, logs turn products into sums; zero factors give a −∞ log-score.”**
- **S41:** explicitly state **finite label set, \(2\le|\mathcal Y|&lt;\infty\), logs base 2**.
- **S4 / §1.2:** add **“discrete model”** to the probability formulation; the MLE–empirical-CE equivalence is otherwise correct.

### Checks that passed
- S35 and S108 correctly make Bayes optimality loss-specific.
- Fano’s proof steps are correct.
- S69–71’s counts, distribution and regrouped loss are correct.
- No standalone “ham” remains in the downloaded deck or either note.
- Your PR mapping should point the **Bernoulli-MLE fitting highlight to S83**, not S84; S84 fits the prior.

Please synchronize deck/notes and send the focused diff and affected renders. No wholesale rebuild needed.

## 2026-10-26 21:40 KST — slides → slides-review

Round-1 corrections pushed in a6ea511 (PR #61). Focused diff: deck +11/−8, both notes, and OUTLINE pointers re-synced (outline-lint 0 stale). Lint is ok, and slides 4/19/41/54/66/76/78/81 were re-rendered at -r 60 with no overflow.

1. S54: bullet → "Averaged over inputs, 1.5 bits of label uncertainty remain; that already forces nonzero error". Note §6.4 (md+html): 10 bits is described as the largest possible label entropy, not H(Y); the conditional-entropy averaging is spelled out; sharp floor ≈ 0.1024 (LHS 1.4689 / 1.5998); 5% is called "the weaker bound, valid but less tight".
2. S19: likelihood → "Which nationality gives more probability to heights near 176 cm, A or B?" (compare densities). Posterior → "among people with heights very close to 176 cm, the fraction from A". Note §3.3 explains the narrow-window reading: the posterior is the limit of Pr(Y=A | x ≤ X ≤ x+δ), not a positive-probability group at exactly 176.
3. S76: "For this generative approach, model the features given each class; MAP also uses the prior p_Y". Heights recall and S77 kept.
4. S81: caption → "illustrative approximation", plus a full-width line "Illustrative 7×7 approximation of the displayed digit — not computed from the original MNIST sample". Provenance mirrored in note §8.1.
Small fixes: S66 uses ln, plus "Natural log here; changing the log base rescales ℓ and leaves the MLE unchanged"; note §7.4 has ln throughout with the same remark. S78 uses your positive/zero-factor wording. S41 adds "Finite label set, 2 ≤ |Y| < ∞; logs base 2". S4 and §1.2 say "discrete model". The PR mapping S84 → S83 will be fixed in the PR body.

FYI: Albert has asked to merge now (21:37 KST), so I'm merging after this push. Any further findings will go in a follow-up PR.
