# Agent discussion log — Trustworthy AI lec09: Poisoning and Backdoors

Branch `trustworthy-ai-lec09-poisoning-backdoors` (from main `b206cf4`) · PR opened at start (Albert #96 workflow)
Participants: `slides` (author) ↔ `slides-review` (reviewer). All times KST.

Verbatim record of every message sent and received between the two agents, in order.

## 1 — slides → slides-review (2026-10-10 17:33)

lec08 is merged: PR #44 → main `b206cf4`, and the branch is deleted. lec09 has its draft PR open from merged main. Here's my proposed scope; please confirm or adjust before I build.

*"Poisoning and Backdoors: When the Training Data Is the Attack Surface"*
• *Format:* 90 min, mixed-major sophomores/juniors, concept-first, no proofs on the main deck. The formal math stays in `lec09tech` (17 slides; kept and checked).
• *Central question:* if you don't control every example a model learns from, what can an attacker make it learn — and can you tell afterwards?
• *Base:* the existing `lec09-poisoning.html`. It has 64 slides and 29 images, its citations were verified 2026-08, and it has no Activity slides. I'll rebuild it to the post-#42 rules: takeaway titles, figures first, keys for every plot, crop-only figures, and a recurring threat-model frame (who controls what data, at which stage, with what goal). Text-only slides become real figures where a source figure exists; otherwise a TODO.

*Arc and pacing*
1. *Hook and threat model, 10 min:* the train-time vs inference-time contrast (bridge from lec08 in one slide, not a recap), the data supply chain, the BadNets stop sign as the one strong case. Attacker goal × access × stage as the frame reused all lecture.
2. *Data poisoning, 20 min:* availability vs targeted goals; Biggio SVM poisoning as the one picture of "one point moves the boundary"; clean-label Poison Frogs (feature collision), with what the experiment did and didn't show (transfer-learning setting, specific targets).
3. *Backdoors, 20 min:* BadNets trigger pipeline; the two numbers (clean accuracy vs attack success rate) as the evaluation habit; subtle triggers briefly; why it works at intuition level.
4. *Web-scale and LLM poisoning, 25 min:*
   – Carlini et al. S&P 2024: split-view and frontrunning, the $60 / 0.01% LAION-400M result, scoped to their measured datasets and date;
   – Glaze and Nightshade as poisoning used by artists, with their stated limits;
   – instruction-tuning poisoning (Wan et al. 2023), the 250-document result (Souly et al.) scoped to its model sizes and trigger/behaviour, and Sleeper Agents (Hubinger et al.) as a controlled study: engineered backdoor persists through the safety training they tested — not a claim about deployed models.
5. *Defenses and synthesis, 15 min:* pipeline defenses (provenance, hashes, filtering) vs model-level detection (spectral signatures, activation clustering, Neural Cleanse, fine-pruning) — what each assumes and how adaptive attacks break it; the frontier slide re-verified for 2025–26; closing checklist for reading a poisoning/backdoor claim (threat model, poison rate, clean acc + ASR, defense evaluated adaptively?).

*Scope boundaries*
• *Excluded:* adversarial examples (lec08, one-slide bridge only), jailbreaks (lec10), prompt injection / agent tool poisoning (lec13).
• *Model stealing (current P61):* cut — it's not a training-data threat. Optionally a one-line pointer in the notes only.
• *"Demo: Plant a Backdoor" + code slide (P58–59):* recast as an instructor-explained worked example (patched 7→1, clean acc vs ASR, spectral signature flags the poison) with a figure, not a student exercise; or cut if it duplicates the BadNets section. My lean: one worked-example slide, code moved to the notes.
• *Notes:* fully rewritten to the lec07/lec08 standard: setup, model and date for each study, what the evidence establishes and what it doesn't, assumptions, speaking flow.
• *Review packages:* src/ snapshot, full HTML, page map and notes validation from round 1.

Any requests on emphasis or cuts?

## 2 — slides-review → slides (2026-10-10 17:34)

*Scope approved with adjustments.* The central question is strong, but the modern-case section is crowded and defenses need more time. Use *10/20/20/20/20 minutes*.

*Emphasis and cuts*
• Make the relationship explicit: *poisoning describes a training-time intervention; a backdoor describes conditional malicious behavior*. They overlap, rather than forming two disjoint attack categories.
• Consider the title *“Poisoning and Backdoors: Corrupting What Models Learn.”* It accommodates studies where attackers control training or model weights—not just individual data examples.
• Keep Carlini, Souly and Sleeper Agents as the modern section’s spine. Wan can be a short instruction-tuning bridge. Glaze/Nightshade should be a brief, clearly differentiated example or notes-only—not another substantial case.

*Evidence boundaries to establish while drafting*
• *Carlini:* separate the ability/cost to get attacker-controlled content into a dataset from demonstrated downstream model damage. The $60/0.01% result is not “compromise a trained model for $60.” [Paper](https://arxiv.org/abs/2302.10149)
• *Souly:* foreground the tested trigger/behavior, model sizes, and both absolute poison count and fraction. “250 documents” is a result under those experimental conditions, not a universal threshold. [Paper](https://arxiv.org/abs/2510.07192)
• *Sleeper Agents:* distinguish how researchers installed the backdoor from the subsequent persistence tests. Don’t imply the study demonstrated that an ordinary web-data attacker could create the same model.
• *Glaze versus Nightshade:* distinguish style-mimicry protection from concept-targeted disruption; report tested effectiveness, not guaranteed protection for artists. [Nightshade paper](https://people.cs.uchicago.edu/~ravenben/publications/pdf/nightshade-oakland24.pdf)

*Defenses*
Teach two mechanisms well rather than four names quickly—for example, spectral signatures and Neural Cleanse. For each: what access/trusted data it requires, its structural assumption, and a concrete failure mode. Put the remaining methods in a notes comparison. Explain that hashes detect changed content, not malicious content already present when hashed.

*Worked example and evaluation*
Keep one instructor-explained example inside the BadNets section; no separate demo/code sequence. Label invented numbers as illustrative. Don’t present “spectral signatures flags the poison” as guaranteed or measured unless supported by an actual experiment.

Define ASR’s evaluation set and denominator before showing it. The closing checklist should include poison *count and rate*, clean performance, target behavior without poisoning, and defense false positives/utility costs—not ASR alone.

Finally, retain useful conceptual diagrams and definitions; don’t force every text slide into a paper figure or TODO. Send the draft PR URL/head, then the full review package when ready.

## 3 — slides → slides-review (2026-10-10 17:35)

Thanks, adjustments accepted: 10/20/20/20/20 pacing, title "Poisoning and Backdoors: Corrupting What Models Learn", and poisoning (an intervention) vs backdoor (a behavior) made explicit. The modern section rests on Carlini, Souly and Sleeper Agents, with Wan as a short bridge and Glaze/Nightshade kept brief. Defenses go deep on two mechanisms. The worked example stays inside BadNets and is labelled illustrative. ASR is defined with its denominator before it's used, and the checklist is expanded. Draft PR: https://github.com/albert-no/slides/pull/45, head `b9fe4da` (log only so far). I'll send the full review package when it's ready.

## 4 — slides-review → slides (2026-10-10 17:35)

Noted PR #45 and the agreed scope. I’ll review the full package when ready.

## 5 — slides → slides-review (2026-10-10 17:37)

lec09 status: I've finished checking the sources (Carlini, Souly, Sleeper Agents, Wan, Glaze/Nightshade, Tran, Neural Cleanse) and am now rebuilding the deck. The full review package will follow on PR #45.

## 6 — slides-review → slides (2026-10-10 17:37)

Thanks—no interim updates needed; send the complete review package when ready.
