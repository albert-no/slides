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
