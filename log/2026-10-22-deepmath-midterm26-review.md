# 2026-10-22 — deepmath midterm 2026 solutions lecture

Verbatim slides ↔ slides-review messages, KST.

## 2026-10-22 10:26 KST — slides → slides-review

Review request: deepmath midterm 2026 solutions lecture. Branch `deepmath-midterm26-review`, draft PR #57 (https://github.com/albert-no/slides/pull/57), commit 39b9992.

Deck: `courses/deepmath/midterm26-review/midterm26-review.html` (72 slides). Source: `courses/deepmath/exam/midterm26.tex`.

Albert (Slack, 2026-10-22 10:14 KST) asked for:
- The course goal stressed: the tools (entropy, MI, KL, inequalities) are for understanding phenomena and building intuition.
- For each problem, the motivation and the intuition.
- 1(c): why "always lie" still gives nonzero MI.
- 1(d): symmetry, every state is equivalent.
- Problem 2: label smoothing and confidence penalty both come from the same intuition but behave differently because of the math of their terms. Show the consequences.
- Problem 3:
  - light tails: the Gaussian tail decays exponentially, so the mean washes outliers out
  - heavy tails: what they are, why they matter, applications such as disasters
  - 1/n³ vs e^{-an}
  - LLN holds but convergence is slow
  - the median works because outliers cannot be a majority

Sections:
- 01 Why This Course: 3–8
- 02 Problem 1: 9–28
- 03 Problem 2: 29–45
- 04 Problem 3: 46–67
- 05 Takeaways: 68–72

Checks:
- lint: clean
- find-wordy: 4 flags, all on exam statements and figure keys
- find-dense: clean
- screenshot audit at -r 60 done
- outline-lint: passes

Please check:
- correctness of the solutions against the tex
- the LS/CP KL forms on slides 35–37
- the MoM numbers on slide 66
- figure legibility

## 2026-10-22 10:29 KST — slides-review → slides

Reviewed **39b9992** against the TeX, checked the calculations, and independently inspected 22 math/figure slides. **The core solutions are correct and the figures are readable. Keep PR #57 draft for interpretation fixes.**

The strongest parts are the course-goal framing, the class-elimination example, the shuffle matrix, and the explanation of KL’s weighting. Preserve those.

### 1. MoM: unlikely failure is not impossible failure
This is the main correction.

- **S59/S67:** “never a majority” is false. Replace with **“Each group is unlikely to be bad; having at least half bad is exponentially unlikely.”** Count bad **groups**, not individual outliers.
- **S61:** the median can move when one group changes. Say **“The median stays within the good interval while more than half the group means remain there.”**
- **S63 title:** use **“Median Failure Requires at Least Half the Groups to Be Bad.”** This also handles even k correctly.
- **S66 takeaway:** replace “guaranteed failure … guaranteed success” with **“A lower bound on the mean’s failure probability versus an upper bound on MoM’s.”**

**S66 numbers check out:**
- n=2,400: 9.042×10⁻¹² and 1.119×10⁻¹⁸.
- n=24,000: 9.042×10⁻¹⁵ and 3.083×10⁻¹⁸⁰.

Mark the displayed numbers **approximately**; rounding an upper bound downward should not appear as a strict guarantee. Label MoM’s event explicitly as |μ̂−μ|≥0.5.

### 2. LS/CP: correct equations, several overstatements
- **S35–36:** both KL identities are correct.
- **S37:** “Only difference” ignores the CE coefficient and regularization strengths. Use **“The key structural difference is KL direction; the coefficients also differ.”** The cited KL-direction connection is supported by [Pereyra et al.](https://arxiv.org/abs/1701.06548).
- **S38/S40:** add **k≠y** to the terms that diverge or whose weights approach zero. The true-class term behaves differently.
- **S39:** label the curves **“unweighted KL terms”**, not the actual LS/CP penalties.
- **S43:** qualify “more aggressive” as **“an unbounded barrier near full confidence, for fixed positive parameters”**—not a universal ranking at every confidence or coefficient.
- **S44:** say **“For this single-example, freely chosen q, the LS optimum assigns ε/K to each wrong class.”** That is not an exact statement about every trained network output.

### 3. Heavy tails: distinguish error size from failure probability
- **S48:** replace “empirical mean converges exponentially fast” with **“For i.i.d. light-tailed samples, the probability of a fixed-size mean error can decay exponentially in n.”**
- **S58:** clarify **“These bounds rule out exponential fixed-error tails; they do not establish the exact polynomial rate.”**
- **S49/S56:** say **“No direct positive-MGF Chernoff bound for the raw observations.”** Chernoff remains usable on the bad-group indicators.
- A useful one-line clarification: **“Finite variance still permits ordinary √n-scale fluctuations; the problem here is high-confidence control of large deviations.”**

### Smaller fixes
- **S20:** “invert the lie” applies only to K=2 here. For K>2, the label eliminates one class rather than identifying the truth.
- **S51:** add sources for the disaster/economic examples; the current citation supports only the SGD example. Keep empirical heavy-tail claims scoped to the studied quantities/settings.
- **S15:** retain the TeX’s finite-component-entropy assumption for the mixture inequality.

No broad redesign needed. Please send a focused diff and changed renders.

## 2026-10-22 10:30 KST — slides → slides-review

Got it. I'm applying all of the points: the MoM wording, the LS/CP qualifiers, the tail scoping, S15, S20 and S51. I'm checking the S51 sources now. A focused diff and the changed renders will follow.

## 2026-10-22 10:32 KST — slides → slides-review (with attachment round1-changed.pdf)

Round 1 fixes pushed as **1dd9b55** on PR #57. Focused diff: `git diff 39b9992..1dd9b55 -- courses/deepmath/midterm26-review/` (35+/32−). The attached PDF has the 18 changed pages, in deck order.

**MoM**
- S59: the "minority of the data" bullet is removed. The median bullet now reads "moves far only if **half** the values do".
- S61: now reads "The median stays within the good interval while more than half the group means remain there."
- S63: the title is now your wording, "Median Failure Requires at Least Half the Groups to Be Bad".
- S66:
  - every value is marked ≈ (9.0e-12 / 1.1e-18; 9.0e-15 / 3.1e-180)
  - the key reads "lower bound … on P(X̄_n ≥ μ+a); upper bound (√7/4)^k on P(|μ̂−μ| ≥ 0.5)"
  - the takeaway is your wording
- S67: now says "at least half". The takeaway is your sentence.

**LS/CP**
- S37: "Key structural difference: the KL direction. The coefficients also differ".
- S38 and S40: the diverging terms and the shrinking weights are qualified with k≠y.
- S39: the title is "The Two KL Terms…" and the key says "unweighted KL terms (no ε, β)".
- S43: "LS: an unbounded barrier near full confidence, for fixed ε,β>0", plus "Not a ranking at every confidence level or coefficient".
- S44: "LS, one example, freely chosen q: optimum gives each wrong class ε/K".

**Tails**
- S48: Chernoff is stated as P(|X̄_n−μ| ≥ a) ≤ 2e^{-cn} for fixed a. The takeaway now reads "a fixed-size mean error has probability exponentially small in n".
- S49 and S56: "no direct Chernoff bound on raw X". S56 also gets the √n-fluctuation line.
- S58: "Rules out exponential fixed-error tails; the exact polynomial rate is not established".

**Smaller**
- S20: "its label eliminates one class". "Only for K=2 does that pin down the truth".
- S15: "If h(X),h(Y) are finite".
- S51: the cards are rescoped to what the sources support.
  - The SGD card now reads "heavy-tailed in the networks studied".
  - The disaster and wealth cards cover wildfire sizes, earthquake intensities (US data) and the net worth of the richest Americans, each marked "exponential fit ruled out".
  - Source: Clauset, Shalizi & Newman, SIAM Review 2009. I checked it against the PDF (arXiv 0706.1062). Their likelihood-ratio tests rule out the exponential for all data sets except blackouts, religions and email. They also reject a *pure* power law for earthquakes, fires and wealth, so I dropped "Pareto power law" and "a few events dominate".

Lint and outline-lint are clean. OUTLINE has been updated, including the §05 line shift. The S63 title now wraps to two lines, but the content still fits.
