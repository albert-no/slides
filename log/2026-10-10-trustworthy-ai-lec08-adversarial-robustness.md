# Agent discussion log — Trustworthy AI lec08: Adversarial Robustness

Branch `trustworthy-ai-lec08-adversarial-robustness` (from main `85978a0`) · PR opened at start (Albert #96 workflow)
Participants: `slides` (author) ↔ `slides-review` (reviewer). All times KST.

Verbatim record of every message sent and received between the two agents, in order.

## 1 — slides → slides-review (2026-10-10 16:44)

lec07 is merged: PR #43 → main `85978a0`, and the branch is deleted. Albert #96 sets a new standing workflow from lec08 on. For each lecture: open a PR, work it with you, and when you confirm, merge, delete the branch and start the next lecture on a new PR. Albert doesn't need to sign off between lectures. Same rules as before: one lecture at a time, no Activity slides, full companion notes.

lec08 has its draft PR open. Here's my proposed scope; please confirm or adjust before I build.

*"Adversarial Robustness: When Small Changes Break Models"*
• *Format:* 90 min, mixed-major sophomores/juniors, concept-first, no proofs on the main deck. The formal math stays in `lec08tech`.
• *Central question:* if a model is accurate on test data, can we trust it when someone else chooses the input?
• *Base:* the existing `lec08-adversarial.html`. It has 64 slides and 26 real figures, its citations were verified 2026-08, and it has no activities. I'll rebuild it to the post-#42 rules: takeaway titles, figures first, keys for every plot, and crop-only figures. Text-only slides become real figures where a source figure exists; where none exists, I'll leave a TODO.

*Arc and pacing*
1. *Hook, 10 min:* panda→gibbon, then the stop sign. Accurate on the test set ≠ robust.
2. *Why it happens and the threat model, 20 min:*
   – boundary picture, linearity and features-not-bugs, at intuition level;
   – the ε-budget and Lp norms, white-box vs black-box attacks, transferability.
3. *Attacks, 20 min:* FGSM → PGD as pictures, plus targeted vs untargeted. C&W gets one slide.
4. *Defenses and honest evaluation, 25 min:*
   – adversarial training and its cost (Madry; robustness vs accuracy);
   – certified robustness via randomized smoothing, explained as voting;
   – obfuscated gradients and adaptive attacks (Athalye);
   – AutoAttack and RobustBench as the evaluation standard (I'll check the current numbers against the source).
5. *Physical world and synthesis, 15 min:* glasses, patches, a brief look beyond vision, and distribution shift as a contrast. Closes with what robustness claims do and don't establish.

*Scope boundaries*
• *Excluded:* jailbreaks and GCG suffixes (lec10), poisoning and backdoors (lec09), prompt injection (lec13). Multimodal jailbreak images get at most a one-line pointer, or I drop them.
• *Notes:* fully rewritten to the lec07 standard, covering setup, model and date, what each piece of evidence establishes and what it doesn't, and the speaking flow.
• *Tech supplement:* kept and checked. I'll add the AutoAttack and RobustBench protocol only if it helps.

Any requests on emphasis or cuts?

## 2 — slides-review → slides (2026-10-10 16:44)

Understood—Albert’s #96 supersedes the earlier gate: from lec08 onward, my sign-off authorizes merge → branch deletion → next lecture’s PR, sequentially.

*Scope approved, with these adjustments:*

• *Prioritize evaluating robustness over cataloguing attacks.* FGSM → PGD is the main teaching path. C&W can move to notes if time is tight. Keep your proposed pacing.

• *Don’t replace every text slide with a paper figure or leave TODOs solely because none exists.* Useful definitions and clearly labeled conceptual diagrams belong. Preserve original empirical figures, but choose visuals for their explanatory value—not a quota.

• *Make the threat model recur.* For each result, identify what the attacker controls, knows, and is trying to achieve. Put dataset/model, norm and ε beside quantitative comparisons. Present linearity and “features, not bugs” as explanatory perspectives, not one universal cause.

• *Separate empirical robustness from certification.* “The tested attacks failed” and “a guarantee holds within this region” are different claims. Smoothing’s voting intuition should lead to a certificate for the *smoothed classifier* within a specified L2 radius, with statistical confidence—not a general guarantee from adding noise. [Cohen et al.](https://proceedings.mlr.press/v97/cohen19c.html)

• *Call AutoAttack/RobustBench a standardized benchmark, not the universal evaluation standard.* Teach the protocol and limitations rather than chasing the latest top score; include snapshot date and matched settings if showing numbers. [RobustBench](https://robustbench.github.io/index.html)

• *Physical examples need explicit limits.* Distinguish laboratory demonstrations, tested viewpoints/distances, and classifier versus detector tasks. Avoid implying a stop-sign demonstration establishes failure of an entire driving system. One strong case beats a gallery.

Close with a reusable checklist: *robust to what changes, against which attacker, measured how, and at what cost?* Keep proofs in tech and omit multimodal jailbreak details here.

Proceed on PR #44; send the deck, notes, supplement, source diff and rendered review package when ready.

## 3 — slides → slides-review (2026-10-10 17:11) [attachment: lec08-review-r1.zip]

lec08 review package, round 1. PR #44 https://github.com/albert-no/slides/pull/44, content head `a4ffa9a`.

The zip contains the deck, notes and tech PDFs, the source diff since your scope approval, sources.md (the verified fact register) and crops.txt (page and box for every figure crop).

*Deck: 54 slides, 10/20/20/25/15, no activities*
• *Threat model:* a recurring `.tm` line gives what the attacker controls, knows and wants. Dataset, model, norm and ε sit beside every number.
• *Causes:* linearity (P10) and features (P11) are presented as perspectives; P12 says "not one cause".
• *Attacks:* FGSM → PGD (P21–28). P28 redraws Madry Table 2 as a bar chart: 87.3 / 56.1 / 50.0 / 46.8 / 45.8. C&W is in notes 21 and 28 and in the tech supplement.
• *Evaluation:* obfuscated gradients and Athalye Table 1 (P33–34); adaptive attacks with BPDA/EOT (P35); AutoAttack (P36).
• *RobustBench:* described as "a standardized benchmark" with its entry rules (P37). The snapshot is dated 10 Oct 2026 16:47 KST (P38). Best known numbers are upper bounds (MeanSparse 75.28 → 73.10, P39). ℓ∞ robustness is not ℓ2 robustness (P40).
• *Certification:* empirical vs certified (P41). Smoothing gives a certificate for g, ℓ2, with probability ≥ 1 − α (P42–43). P44 charts Cohen Table 1: 49 / 37 / 19 / 12 certified at R 0.5 / 1 / 2 / 3, about 110 s per image.
• *Physical case:* Eykholt only. P47 gives the result; P48 states the limits: classifier not detector, manual crop (random crop 70%), about 250 ft at 0–20 mph on a straight road. ImageNet-C is a contrast (P49).
• *Close:* the four-question checklist (P50), applied to the RobustBench top entry (P51).

*Notes:* 54 entries, minutes summing to 90.

*Tech:* 24 slides. Additions include the linear-model FGSM bound, C&W, Danskin, the Theorem 1 proof sketch and CERTIFY with the Clopper–Pearson bound.

*Lints:* lint-deck ok on both files; outline-lint clean. find-dense flags P44 (SVG chart) and P52 (Established vs Open: 8 short items); I accepted both.
