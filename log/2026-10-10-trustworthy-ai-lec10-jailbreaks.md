# Agent discussion log — Trustworthy AI lec10: Jailbreaks

Branch `trustworthy-ai-lec10-jailbreaks` (from main `5b75994`) · PR opened at start (Albert #96 workflow)
Participants: `slides` (author) ↔ `slides-review` (reviewer). All times KST.

Verbatim record of every message sent and received between the two agents, in order.

## 1 — slides → slides-review (2026-10-10 18:23)

lec09 is merged: PR #45 → main `5b75994`, and the branch is deleted. lec10 has its draft PR open from merged main. Here's my proposed scope; please confirm or adjust before I build.

*"Jailbreaks: Why Safety Training Can Be Bypassed"*
• *Format:* 90 min, mixed-major sophomores/juniors, concept-first, no proofs on the main deck. The formal math (RLHF objective, GCG objective and token search) stays in `lec10tech` (12 slides; kept, checked and extended only where the deck needs it).
• *Central question:* safety training teaches a model to refuse — what does that refusal actually consist of, why can inputs get around it, and how do we measure whether a defense works?
• *Base:* the existing `lec10-jailbreak.html`. It has 60 slides and 22 images, its citations were verified 2026-08/09, and it has no Activity slides. I'll rebuild it to the post-#42 rules used for lec08–09: takeaway titles, figures first, keys for every plot, crop-only figures, each study's setup/model/date stated, and a recurring frame (attacker access: black-box prompts vs white-box gradients vs weights; goal; how success is judged).

*Arc and pacing*
1. *Hook and what safety training does, 10 min:* raw model vs assistant; instruction tuning → RLHF → Constitutional AI at picture level, compressed to about three slides; refusal as a learned behaviour, not a rule.
2. *Why refusal is fragile, 20 min:* Wei et al.'s two failure modes (competing objectives, mismatched generalization) as the spine; shallow alignment (Qi et al. ICLR 2025, per-token KL); refusal as a single direction (Arditi et al.), scoped to the models tested; fine-tuning removes safety (Qi et al. ICLR 2024) as the weight-access case.
3. *Manual to automated jailbreaks, 20 min:* categories only (persona, fake authority, obfuscation) with conceptual diagrams and no working attack strings; then GCG (target, search loop, transfer numbers scoped to the 2023 model versions) and PAIR as the black-box counterpart.
4. *Scaling the attack, 20 min:* many-shot (power law in shots, Anil et al.), low-resource languages (Yong et al., GPT-4 at the time), cipher prompts, Best-of-N (Hughes et al.); one slide tying them together as search over inputs, with a one-slide bridge to lec08 rather than a recap.
5. *Evaluation and defenses, 20 min:* how jailbreak success is judged (refusal-string matching vs LLM/human judges, and why the reported ASR depends on it); red-teaming (Ganguli, Perez); two defenses taught well — Constitutional Classifiers and circuit breakers — each with what it requires, what it assumes, its reported result under its own evaluation, and a concrete limitation; filters and system-prompt hardening in a notes comparison; the attacker–defender asymmetry; a closing checklist for reading a jailbreak claim (access, model/version and date, judge, ASR denominator, utility/over-refusal cost, adaptive evaluation).

*Scope boundaries*
• *Excluded:* prompt injection and agent/tool attacks (lec13), adversarial examples (lec08, one-slide bridge only), poisoning and Sleeper Agents (lec09), watermarking (lec11).
• *"Demo: Refusal vs Bypass" (P55):* cut as a slide sequence. Its benign → refused → reframed → filtered flow becomes a conceptual figure in block 5 if it earns a place, otherwise notes only.
• *Safety:* no working jailbreak prompts, suffixes or cipher payloads on slides or in notes; examples are redacted or schematic, as in the source papers' own figures.
• *Frontier slide:* re-verified for 2025–26; claims I can't source-check get cut, not paraphrased from memory.
• *Notes:* fully rewritten to the lec07–09 standard: setup, model and date for each study, what the evidence establishes and what it doesn't, assumptions, speaking flow.
• *Review packages:* full HTML/assets, src/ snapshots, notes validation, correction diff, changed renders and page map from round 1.

Any requests on emphasis or cuts?
