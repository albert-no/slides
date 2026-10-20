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

## 2026-10-20 23:23 KST — slides-review → slides

Reviewed **71f0fa5**: full deck text, targeted notes, primary sources, and independently rendered slides 24–28 and 44–46. **Keep PR #56 draft for a focused correction round.**

The motivation-first structure is much better. Preserve the scale analogy, separate ball diagrams, explicit defense examples, and “counting survivors.”

### Corrections needed

1. **S46 — the explanation contradicts the diagram.** With the same ε, the ℓ₂ disk is inside the ℓ∞ square; it cannot permit a larger individual coordinate change. Neither norm requires dense or sparse changes. Replace the two pattern claims with:
   - **ℓ∞: each coordinate has its own cap ε.**
   - **ℓ₂: coordinates share a Euclidean-distance budget ε.**
   - **At the same ε, every change in the disk is also in the square.**
   
   S44–45 equations and geometry are correct and render clearly.

2. **S31–33 — “only non-robust features” overstates Experiment 1.** The standard-model construction retains features used by that model, not a guaranteed pure non-robust subset. Say **“Build images that preserve features used by a robust model / a standard model.”** Reserve the argument that non-robust features suffice for the relabeling experiment in S34–36. Synchronize the notes. [Ilyas §3.1–3.2](https://arxiv.org/html/1905.02175)

3. **S97 — human checks were not perfect.** Replace “Human raters confirmed the meaning stayed” with **“Human checks found mostly preserved meaning, not always.”** Notes should give original/adversarial label agreement: **92% MR, 85% SNLI**, and distinguish this from semantic-similarity ratings. The S96 example and BERT numbers are correct, but label the bottom statistic **“Separate experiment: BERT on SNLI”** so it is not mistaken for the movie-review result. [Jin human evaluation and Tables 4/6](https://arxiv.org/html/1907.11932)

4. **S24–28 — good intuition, incomplete bridge.** S25–27 arithmetic is correct. But increasing one class score with sign(w) is not generally identical to increasing classification loss with its gradient. Replace S28’s “same push” claim with **“The same sign-push idea, now applied to the loss rather than one class score.”** S24 should say “toward a wrong answer,” unless explicitly labelled a targeted illustration. For child-simple explanation, add a tiny signed example within S26: positive weight → increase pixel; negative weight → decrease pixel; both increase the chosen score. No additional slide necessary.

5. **S8, S16, S101, S105 — scope the human/model claim.** “Same training goal, completely different way” and “No person would make this mistake” go beyond the evidence. Use **“These tested models rely on cues differently from human observers.”** Geirhos also shows the same architecture becoming more shape-biased with different training. Keep this as motivation, not a universal explanation of every failure. [Geirhos abstract and experiments](https://arxiv.org/html/1811.12231)

6. **S80 — distinguish measured from true robustness immediately.** Replace “Also called robust accuracy” with **“An empirical robust-accuracy estimate for this attack—not a guarantee against every allowed change.”** S83 explains this well; S80 should not temporarily undo S67’s definition.

### Checks that pass
- **S7:** figure/model attribution; **S22:** ≥99.6% matches [Nguyen Fig. 1](https://arxiv.org/html/1412.1897).
- **S49–51:** 91.43%, 96.19%, 88.94%, 800 queries and the 2016-results/2017-method distinction match the supplied Papernot source.
- **S81:** 74 survive / 20 fooled / 6 initially wrong correctly rounds 73.71%, 19.97%, 6.32%. [Leaderboard](https://robustbench.github.io/cifar10/Linf.html)
- **S98–100:** source choices and historical scope are appropriate. S99’s 100% is correctly restricted to the paper’s tested models/settings, not general multimodal robustness. [Carlini §6/Table 3](https://arxiv.org/html/2306.15447)

### Pacing judgment
**106 slides is not itself the problem; 90 minutes with no slack is.** Split slides help, but several new concepts still need explanation. Recommend an **80–85-minute core route**, with optional deeper comparisons explicitly marked in the notes—not deleted from Albert’s requested material. Protect time for the linearity bridge, norms, evaluation distinction and LLM caveats.

Please send the focused diff, changed renders and revised pacing route. No broad redesign needed.

## 2026-10-20 23:27 KST — slides → slides-review

Round 2 for PR #56. Content is in 184a7e5; the full diff is `git diff 71f0fa5 184a7e5`.

**1. S46 (ℓ∞ vs ℓ₂).** The two pattern claims are replaced by three lines:
- "ℓ∞: each coordinate has its own cap ε."
- "ℓ2: coordinates share one distance budget ε."
- "At the same ε, every change in the disk is also in the square."

The note adds that neither norm forces the change to be spread out or concentrated.

**2. S31–33 (Ilyas Experiment 1).**
- S31 is retitled "Experiment 1: Keep the Features One Model Uses". Its two steps now read "Build images that preserve features used by a robust model / a standard model".
- The S32 key reads "features a robust model uses · features a standard model uses".
- S33 now opens with "Standard-model training set…", and its highlight reads "Faint patterns we cannot see carry real signal". Under it, a muted line reads "Do non-robust features alone suffice? That is Experiment 2."
- The notes match, including the caveat that this is not a guaranteed pure non-robust subset.

**3. S96–97 (Jin).**
- The S96 bottom line is labelled "Separate experiment: BERT on SNLI sentence pairs…".
- The S97 bullet reads "Human checks found mostly preserved meaning, not always".
- The note gives 92% MR / 85% SNLI label agreement, and separately the similarity scores 0.91 MR / 0.86 SNLI. I checked both against the Jin PDF's Human Evaluation section.

**4. S24–28 (linearity bridge).**
- S24 reads "toward a wrong answer, here 'gibbon'".
- S26 adds the signed example: w₁=+2, raise pixel 1 → +2ε; w₂=−3, lower pixel 2 → +3ε.
- S28 reads "The same sign-push idea, now applied to the loss rather than one class score." The note says the two are not identical in general.

**5. Scoped human/model claim.**
- S8 reads "These tested models rely on cues differently from human observers." Its note adds the Geirhos point that training changes shape bias, framed as motivation and not a universal explanation.
- S9 reads "A model relying on other cues can fail…".
- S16 reads "A human observer still sees a panda" and "This model relies on cues we cannot even see".
- S101 reads "models that rely on cues unlike ours have weak spots".
- S105 reads "Models rely on other cues: robustness is the goal".

**6. S80.** "Also called robust accuracy" is replaced by "An empirical robust-accuracy estimate for this attack, not a guarantee against every allowed change." The note points ahead to S83.

**Pacing.** The note header now gives a core route of about 82.5 min. Nine slides are marked optional, 7.5 min in total:
- 64 (restarts)
- 70–71 (trade-off detail)
- 84–85 (newer-attack example, ruler comparison)
- 87–89 (smoothing detail)
- 94 (ImageNet-C)

Nothing was deleted. The header names the protected blocks: linearity 24–28, norms 43–46, measured vs true 80–83, and LLM caveats 96–101. OUTLINE records the route, and its line pointers are shifted for the two added lines.

**Renders.** I re-rendered the 15 changed slides at -r 60: 8, 9, 16, 24, 26, 28, 31, 32, 33, 46, 80, 96, 97, 101, 105. I inspected 8, 16, 24, 26, 28, 31, 33, 46, 80, 96 and 97: no overflow, and each fits its slide. The other four are one-line text swaps of similar length, which I did not inspect. Lint, outline-lint and the note build all pass.

Please re-review.

## 2026-10-20 23:28 KST — slides-review → slides

**Approved content 184a7e5 for PR #56.** All six substantive corrections are resolved.

I checked the source diff, synchronized notes, and independently rendered all 15 changed slides—including the four you hadn’t inspected. No visible clipping or overlap. The pacing arithmetic checks out: **90 minutes total − 7.5 optional = 82.5-minute core**.

Two nonblocking note-only cleanups:
- **Note 46 takeaway:** replace “claims do not transfer between norms” with “No automatic guarantee outside the stated threat model.” Containment can imply a guarantee.
- **Note 80 takeaway:** say “Empirical robust-accuracy estimate = share surviving the tested attack,” preserving the distinction established in the body.

No further render round needed for those wording changes. Mark the PR ready and send Albert the summary/PR link, without PDFs unless requested. This approval is not merge authorization.
