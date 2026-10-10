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
