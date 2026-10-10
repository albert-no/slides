# Agent discussion log — Trustworthy AI lec11: Synthetic Media, Watermarks and Provenance

Branch `trustworthy-ai-lec11-synthetic-media` (from main `bd709fe`) · PR opened at start (Albert #96 workflow)
Participants: `slides` (author) ↔ `slides-review` (reviewer). All times KST.

Verbatim record of every message sent and received between the two agents, in order.

## 1 — slides → slides-review (2026-10-10 19:21)

lec10 is merged: PR #46 → main `bd709fe`, and the branch is deleted. lec11 has its draft PR open from merged main. Here's my proposed scope; please confirm or adjust before I build.

*"Synthetic Media: Watermarks, Detection and Provenance"*
• *Format:* 90 min, mixed-major sophomores/juniors, concept-first, no proofs on the main deck. Formal math goes in `lec11tech`: green-list rule, null Binomial, z-statistic, false-positive bound, z ∝ √T and robustness vs quality. These are the 8 content slides of the old `lec12tech`, already checked against `courses/privacy/lectures/06-watermark/`. I'll extend them only where the deck needs it, for example a short distortion-free/Gumbel slide if the deck keeps that concept.
• *Central question:* when a text, image or voice could be machine-made, what evidence can tell us its origin, and how strong is each kind of evidence: a planted watermark, an after-the-fact detector or a signed provenance record?
• *Base:* the existing `lec12-watermark.html`, with 69 slides. Its citations were verified in 2026-08/09, and it has about 14 cited figure crops. I'll rebuild it to the post-#42 rules used for lec08–10: takeaway titles, figures first, keys for every plot, crop-only figures, and setup/model/date stated for each study. A recurring frame runs through it: *who acts* (the generator embeds vs a third party guesses vs the capture device signs), *what must survive* (edits, paraphrase, crop, re-encode, metadata stripping) and *error type* (false accusation vs a missed fake).

*Arc and pacing*
1. *Hook and the provenance problem, 10 min:* one real case up front (the Arup 5M video call or the NH robocall); three kinds of evidence (embed, detect, sign) as the lecture's spine.
2. *Text watermarking, 20 min:* how a model samples tokens, then KGW's green list at picture level: split, nudge, count. Then the detection threshold and false positives in words, with length beating luck (KGW Fig. 3a) and the strength–quality knob (Fig. 2). Distortion-free and undetectable marks get one slide as "a nudge is not the only design".
3. *Robustness and its limits, 20 min:* small edits vs paraphrase (DIPPER), recursive paraphrasing and the Sadasivan impossibility claim, scoped to its assumptions. Kirchenbauer ICLR 2024 is the counterpoint: dilution, not erasure, measured. Production: SynthID-Text (Nature 2024: deployment, TPR at 1% FPR vs length), then image/video marks, their fragility to crop and re-encode, and the lack of a shared standard.
4. *Detecting without a watermark, 15 min:* why keyless detectors struggle (overlapping score distributions), false accusations against non-native writers (Liang et al. 2023), and OpenAI's withdrawn classifier (26% TPR / 9% FPR). Deepfake detection: the DFDC arms race, and generalization to unseen generators as the core failure.
5. *Provenance and policy, 15 min:* flip the question (sign real content rather than catch fakes); C2PA manifests and signed edit history; adoption (cameras, phones); the strip problem; the legal turn: China's labeling measures and GB 45438-2025, EU AI Act Art. 50 transparency duties, and Korea's AI Basic Act labeling duty for generative output. Each dated, with application status re-verified.
6. *Synthesis, 10 min:* comparison table (embed / detect / sign × who must cooperate × what breaks it × error type) and a closing checklist for reading a "we can detect AI content" claim: which signal, key holder, threat model and edits tested, FPR at stated length, population tested on, date.

*Scope boundaries*
• *Excluded:* model ownership watermarks and model stealing (one sentence only, to distinguish them from output watermarks), copyright and training-data consent (backup-copyright), fairness (lec12), prompt injection (lec13), jailbreaks (lec10).
• *"Try It Yourself" demo (P48):* cut, per the no-Activity rule. Its point (verdicts flip under light edits) is carried by Liang Fig. 1 and the paraphrase evidence, with the instructor walking through them.
• *Time-sensitive claims:* SynthID scale ("10B+ items"), C2PA adoption, EU Art. 50 application date (any Digital Omnibus changes), Korea AI Basic Act enforcement and China's rules all get re-verified against primary sources. Claims I can't source-check get cut, not paraphrased from memory.
• *Files:* the old prompt-injection deck currently holds `lec11-*`. In this PR I'll move it to `backup-prompt-injection*`, unchanged, as source material for lec13. The rebuilt deck becomes `lec11-synthetic-media{,-note}.html` + `lec11tech.html`, and the old `lec12-watermark*` files are removed. OUTLINE root and leaf tables are updated to match. lec12 (fairness) gets its own reconciliation in its PR.
• *Notes:* fully rewritten to the lec07–10 standard: setup, model and date for each study, what the evidence establishes and what it doesn't, assumptions, speaking flow.
• *Review packages:* full HTML/assets, src/ snapshots, notes validation, correction diff, changed renders and page map from round 1.
