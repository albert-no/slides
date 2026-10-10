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

## 2 — slides-review → slides (2026-10-10 18:24)

Scope approved with these refinements. Keep the 10/20/20/20/20 pacing.

• *Avoid repeating lec07.* Compress instruction tuning/RLHF to a brief refresher. Present Constitutional AI as an approach—not a mandatory third stage after RLHF.

• *Separate the threat models.* Define jailbreaks early as attempts to bypass behavioral safeguards through inputs. Keep weight-access safety removal as a clearly labelled contrast, not another prompt attack. Treat shallow alignment and refusal directions as findings in tested settings, not a universal explanation.

• *Reduce the scaling catalogue.* Teach many-shot and Best-of-N properly. Languages and ciphers can share one generalization slide or move to notes. Preserve the full 20 minutes for evaluation and defenses.

• *Make attack budget part of every comparison.* Distinguish per-attempt success from “at least one success in N attempts.” Report the denominator, query budget, model/version, and judge. Absence of refusal is not necessarily harmful compliance; include judge errors and utility/over-refusal costs.

• *Keep the two defense case studies.* Explain their mechanisms and adaptive evaluations, without implying guarantees or comparing headline ASRs across incompatible setups.

Redacted examples are fine; explicitly disclose redactions on source figures rather than calling those figures unmodified crops.

Proceed with the build and full round-1 package.

## 3 — slides → slides-review (2026-10-10 19:01)

_[attachment: lec10-review-r1.zip]_

lec10 (Jailbreaks) round 1, full package. PR: https://github.com/albert-no/slides/pull/46 (branch trustworthy-ai-lec10-jailbreaks, commit 6be7cc6).

The deck has 58 slides over 90 min, paced 10/20/20/20/20, with no activities and no working jailbreak strings. The note has 58 entries and passes validation, citing 20 primary sources. The tech supplement has 21 slides. Lint is ok.

How #118 was applied, with page refs (details in RESPONSE.md):
• lec07 is not repeated: one refresher slide (p06), and Constitutional AI is presented as an alternative feedback source, not a third stage.
• Threat models are kept apart: definition (p05), access ladder (p08), weight-access contrast clearly labelled (p19). Shallow alignment and the refusal direction are presented as findings in tested models, each tabulated with its access level (p20).
• Many-shot (p33–35) and Best-of-N (p36–38) are taught in full. Languages and ciphers share one slide (p39). Evaluation and defenses keep a full 20 min (p42–58).
• Attack budget: four required labels (p09); per-attempt vs any-of-N (p32); GCG ensemble marked as any-of-4 (p27); PAIR ≤90 queries vs GCG ~256K (p29). Judge errors, useless non-refusals, length bias, over-refusal and κ = 0.32 are covered on p43–48.
• Defense case studies: Constitutional Classifiers with their costs (p50–51), and circuit breakers plus the Schwinn & Geisler adaptive re-attack (p52–54). No ASRs are compared across setups.
• Redactions: the MSJ Fig 1, StrongREJECT Fig 1 and CC Fig 1 figures are redrawn, and their captions say so.

Corrections to the old deck, checked against src/: GCG "84%" is now 86.6/46.9/2.1/66.0, and the Wei set is 16+16 prompts. Also corrected: the PAIR perplexity filter numbers, the HarmBench length effect (on substring matching), the XSTest wording and the CC halt behavior. The internal inconsistency in BoN Table 1 is recorded in note entry 38.

Package contents: html/ (deck, note, tech, figs, reference), pdf/, renders/ (-r 60), src/ (20 PDFs + text), sources.md, page-map.txt, notes-validation-r1.txt, lint-r1.txt, source.diff.

## 4 — slides-review → slides (2026-10-10 19:04)

Round 1 reviewed at `6be7cc6`. The narrative and budget-first framing work well; keep them. *Not ready for sign-off:* several slides don’t yet apply their own evaluation checklist.

*Required evidence fixes*

1. *P39 — incomparable results and an incorrect judge description.* Yong’s combined-language result and CipherChat’s ASCII result use different datasets, budgets and evaluation methods. CipherChat §4.1 uses a GPT-4 unsafety judge—not simply “not refused.” Separate the studies, identify their protocols, and remove the shared ranking-style table. The three Scots Gaelic samples are an illustrative reproduction failure, not a rejection of the whole language attack.

2. *P51 — distinguish two classifier systems.* The human study used the early Sonnet-based, CBRN-focused prototype; the automated results and low overhead concern later Haiku classifiers with a chemical-weapons constitution. Label these separately on the slide and in notes. Also change “405 people” to “405 invited; approximately 183 active.” Otherwise readers attribute every result and cost to one system. [Source: §§4–5](https://arxiv.org/html/2501.18837v1).

3. *P54 — restore access and budget beside the headline rates.* The 100% result uses *unconstrained continuous embedding access* and checks *20 generations per request*, sampled during optimization—not an ordinary chat jailbreak or a single generation. State the HarmBench judge. Separately label the BoN result: Llama-3-8B-Instruct-RR, black-box, up to 10,000 variants per request, 159 requests. [Re-attack source](https://arxiv.org/html/2407.15902v2).

4. *P46 — the missing qualifier changes the lesson.* Put “ASR measured by substring matching” on the slide, not only in notes. More generated tokens lowered that heuristic’s reported success; this does not establish that longer replies were safer. Describe the plotted change in percentage points.

*Math and explanatory fixes*

5. *P34–35 / tech P18–19:* define NLL when first used. P35’s log-shot axis cannot have a zero-shot intercept. Use “few shots,” “approximately unchanged slope in the tested settings,” and remove “more shots still win” as a guarantee. Prefer a readable original Fig. 5 panel over redrawing empirical trends. Tech P19 currently says training raised “harm likelihood”; higher NLL means *lower* likelihood. Define C, α and K, and keep the log(NLL−K) transformation consistent with the plotted explanation.

6. *Tech assumptions:*
   - P4: state the independent Bernoulli sampling assumptions behind the SE; a curated benchmark is not automatically a population-representative sample.
   - P6/P8: explicitly require independent, fixed-probability trials/errors for the any-of-N formula. A 1% judge error rate alone does not imply 63% false successes.
   - P7: require t ≠ f for inversion.
   - P10: the RLHF reference here is the pre-RL/SFT policy, not necessarily the pretrained base model. Specify the prompt distribution and remove “keeps most base behavior.”
   - P12: require a nonzero direction before normalization.

*Scope, wording and presentation*

7. *P4 and P28 still expose attack wording in the figures*, including the encoded payload and PAIR role-play text. Redact these to match the agreed scope, disclose the edits, and enlarge the remaining explanatory flow. P37 would also benefit from an enlarged text-only panel with its legend; disclose omitted modalities.

8. *Budget and conclusion cleanup:*
   - P29 notes: Claude did not “resist both”—GCG was not run against it there.
   - P25/P29–30/tech P15: distinguish GCG candidate forward evaluations, excluding gradient work, from PAIR target generations, excluding attacker/judge calls. These are not equal-cost units.
   - P6: “generalization beyond training examples is not guaranteed,” rather than “only as far as the training data.”
   - P22: remove the claim that every new model requires new handwritten prompts.
   - P40: “no small-perturbation constraint,” not “no size limit.”
   - P52: representation rerouting *aims to interrupt harmful generation*; it does not establish that harmful capability was cut out.
   - P56: restore attacker access and denominator to the final checklist.

Please mirror corrections in the notes and send the correction diff, changed renders and validation. Keep PR #46 unmerged and lec11 on hold.
