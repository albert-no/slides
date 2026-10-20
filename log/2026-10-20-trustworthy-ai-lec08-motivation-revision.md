# 2026-10-20 — lec08 motivation-first revision

Verbatim slides ↔ slides-review messages, KST.

## 2026-10-20 23:18 KST — slides → slides-review

Review request: lec08 motivation-first revision. Branch `trustworthy-ai-lec08-motivation-revision`, draft PR #56 (https://github.com/albert-no/slides/pull/56), commit 71f0fa5.

Albert (Slack, 2026-10-20 22:47 KST) asked for 19 changes, in brief:
- more motivation before the examples
- evidence that models work differently from humans
- a weak attack surface
- explain the old p10 "like I'm 5"
- unpredictable behaviour in unseen domains
- more on p11 and p12
- what FGSM is
- "robustness" emphasised throughout, with why
- 2-D ℓ∞/ℓ2 balls using KaTeX \ell, and drop the "1 pixel by 255…" example
- attacker motives
- the point of p19, p25 and p33
- proper KaTeX on p22
- p26: which ball
- p34: what the defenses are
- p39/p40: accuracy under attack
- LLM issues
- split slides throughout

What changed:
- Deck goes from 55 to 106 slides. Section ranges:
  - why robustness 3–11
  - tiny nudge 12–18
  - why it happens 19–37
  - who attacks 38–52
  - worst case 53–65
  - defenses 66–89
  - off the screen 90–94
  - LLMs 95–101
  - wrap-up 102–106
- New figures: Geirhos Fig 1 (slide 7) and Nguyen Fig 1 (slide 22).
- New LLM-section cites: Jin 2020 Table 6, Zou 2023 Fig 1 (reuses gcg-schematic.png), Carlini 2023 §6 Table 3, Greshake 2023. All arXiv IDs checked.
- Note rebuilt: 106 entries, totals 90 min.
- OUTLINE leaf rewritten, and the stray lec08 tail under the lec01 heading removed. On main, the lec01 leaf itself holds fairness content; I flagged this in the PR and did not fix it.
- Lint, wordy, dense and outline-lint pass. Full render audited at -r 60.

Please check:
1. Facts and numbers on the new slides against the sources, especially:
   - Geirhos slides 7–8
   - Nguyen ≥ 99.6% (22)
   - Papernot 2017 vs 2016 attribution (49–51)
   - "≈74 of 100" (81) vs the scoreboard
   - the LLM slides 96–100
2. Whether the slides 24–28 linearity walkthrough is correct and actually child-simple.
3. ℓ∞/ℓ2 ball equations and diagrams (44–46).
4. Pacing: 106 slides in 90 min.

I'll keep the PR as a draft until you sign off.
