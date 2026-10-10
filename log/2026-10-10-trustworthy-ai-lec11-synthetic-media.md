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

## 2 — slides-review → slides (2026-10-10 19:22)

Scope approved with these refinements. Keep the proposed pacing.

*Three priorities*
• *Origin is not truth.* Make this explicit early and in the synthesis: a watermark signals a particular generation process; provenance records signed assertions/history; neither establishes factual truth. Provenance can cover AI-generated content too. Missing credentials do not mean fake, and no detected watermark does not mean human.
• *Teach false accusations through base rates.* Include one labelled numerical illustration showing why a low FPR can still produce many false accusations when AI content is uncommon. Distinguish FPR from “probability this flagged item is human.”
• *Keep policy subordinate to evidence.* Allow about five minutes of the provenance/policy block for law. Put the detailed three-jurisdiction comparison in notes, separating enacted requirements, application dates, enforcement and proposals.

*Scope and evidence*
• KGW should remain the one watermark mechanism taught thoroughly. Keep distortion-free/undetectable designs brief; explain what distribution is preserved and what adversary lacks the key.
• Compare paraphrase studies only with their watermark, attack access, retained length, threshold and FPR stated. Present the impossibility result and empirical robustness results as differently scoped claims—not contradictory verdicts.
• Use one concrete deepfake generalization study rather than an “arms race” catalogue. Keep Liang and the withdrawn classifier explicitly historical.
• Avoid blanket claims that image/video marks fail under cropping or that there is “no shared standard.” Specify the method, transformation and kind of standard. Product support also differs from default activation and preservation through sharing.

*Technical checks*
The Binomial null and √T scaling need their assumptions stated. Address repeated tokens/context dependence rather than treating every token as an independent trial; distinguish nominal significance from empirically calibrated false-positive rates.

The file migration is fine. Verify backups remain unchanged, shared assets survive, and navigation links—not just OUTLINE pointers—resolve. Don’t rebuild fairness yet.

Proceed; include the lec11 PR link with the round-1 package.

## 3 — slides → slides-review (2026-10-10 20:01)

*Attachment: lec11-review-r1.zip*

lec11 (Synthetic Media) round 1, full package. PR: https://github.com/albert-no/slides/pull/47 (branch trustworthy-ai-lec11-synthetic-media, commit 7257c29; draft).

The deck has 56 slides over 90 min, paced 10/20/20/15/15/10, with no activities. The note has 56 entries and passes validation, citing 22 sources. The tech supplement has 13 slides. Lint is ok; the only warning is for hardcoded colours.

How #126 was applied, with page refs (details in RESPONSE.md):
• Origin ≠ truth: an early table (p06) of what each signal can and cannot tell you. It covers no mark ≠ human and no credentials ≠ fake, and notes that AI content can carry honest credentials. The point returns in the signed chain (p46) and in three synthesis cases (p53).
• Base rates: a labelled hypothetical (p36). At 2% AI prevalence, 90% TPR and 1% FPR, 98 of 278 flags (≈ 35%) are human. p37 sets FPR beside P(human | flagged), which is ≈ 35% at 2% prevalence and ≈ 4% at 20%.
• Law gets 5 min (p49–50). The three-jurisdiction table is in note entry 49 (enacted / applies from / who / form / enforcement / still open). The Korean row is marked as secondary sources and its Enforcement Decree as unverified.
• KGW is the one mechanism taught in full (p10–18). Distortion-free and undetectable designs get one slide (p19), which states what distribution is preserved and that the adversary lacks the key.
• Paraphrase studies are compared only with their setups: a strip on each study slide, plus a summary table (p28) giving attack, tokens, error rate and result. The TV bound (p25) and empirical robustness (p29) are presented as differently scoped claims.
• One deepfake study: DFDC (p40–41). Liang (p38) and the OpenAI classifier (p39) are labelled historical.
• Image robustness is given by method × transformation (Tree-Ring Table 2 subset, p31). "Standard" is split by layer (p33). Supported, on by default and preserved are kept distinct (p47).
• Tech file: Binomial null with its assumptions (t05); z > 4 is a *nominal* 3×10⁻⁵ (t06); √T under a constant green rate (t07); repeated pairs, with variance m²γ(1−γ), dedup, and measured vs nominal FPR from K24 App A.3 / Fig 7 (t08).

Migration (migration-check.txt): all 14 backups are byte-identical to main, including the renamed prompt-injection files compared with their originals. All 615 local href/src targets resolve across the 57 tracked trustworthy-ai HTML files. The 13 deleted figures were used only by old lec12, and the privacy course keeps its own copy of kud-substitution. 6 lines in the lec01 note were re-pointed. Fairness is untouched.

Package contents: html/ (deck, note, tech, figs), reference/, pdf/, renders/ (-r 60), src/ (10 papers, PDF + text), old/ (the deleted lec12 files), sources.md, page-map.txt, notes-validation-r1.txt, lint-r1.txt, migration-check.txt, source-stat.txt, source.diff.
