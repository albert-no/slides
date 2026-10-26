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
