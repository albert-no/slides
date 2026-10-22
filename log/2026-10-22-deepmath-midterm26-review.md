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
