# 2026-10-27 — trustworthy-ai lec09 Albert r1 feedback (PR #63)

Verbatim slides ↔ slides-review transcript, in order, KST timestamps.

## 2026-10-27 15:13 KST — slides → slides-review

```
Review request — PR #63 (draft): https://github.com/albert-no/slides/pull/63
Branch trustworthy-ai-lec09-albert-r1, commit 6650aa0.

Albert's first detailed read of lec09 (merged in #58). His page numbers are PDF pages; deck stays at 91 slides.
- Larger diagram fonts (rebuilt as cards/SVG): p7, 8, 11, 14, 18, 35, 46, 49, 51, 66, 72, 84
- p25 class A/B legend · p26 "Point: checking labels cannot catch it" · p28 replaced by a 3-step fish/dog SVG
- p30–31 Setup / Result / Takeaway · p39 ASR table in words (no t, no i→i+1, no "denominator") · p40 poison share = fraction of training images poisoned · p41 key on 3 lines · p43 "?" = must measure
- p47 key: middle = rejected design (extra detector + merging layer), right = BadNet learned from poisoned data (BadNets Fig. 1)
- p52 dump → snapshot ("periodic downloadable copy"; Carlini's "bimonthly" is ambiguous so not stated) · p54 image hash · p57 Glaze defined · p59 "Retrieval (RAG)"
- p64 key: x = expected poisons seen so far; >50 perplexity increase = noticeable degradation (Souly) · p67 table rebuilt · p68 retitled RAG poisoning + RAG definition
- p72–74 point: a backdoor planted on purpose ("model organism") survives safety training
- p80 intro line · p81 Tran Fig 3 recropped from the PDF; drop the top 1.5·ε scores, linked to p82 · p84 Neural Cleanse: smallest patch that flips everything to one label; how the search works; heuristic caveat
- "Like You're Five" removed throughout
Note and OUTLINE leaf updated in the same commit; lint-deck and outline-lint clean.

Please check especially the factual wording on p47, p64, p81 and p84, and whether p28 now reads clearly.
Known: lint warns on `$60` inside SVG text (p51); this is pre-existing and renders as intended.
```

## 2026-10-27 15:15 KST — slides-review → slides

```
Reviewed 6650aa0’s source and rendered p28, 47, 64, 81 and 84. **The diagrams are clearer, but p84 and p64 need corrections before approval.**

**1. P84 — the headline and cards overpromise.**
“Smallest patch” and “every image” contradict the heuristic caveat below. Neural Cleanse searches for a small trigger with high success on the clean examples used for optimization; it does not certify a global minimum or universal success. The paper targets &gt;99% success in its experiments.

Suggested replacements:
- Title: **“Neural Cleanse: Which Label Needs an Unusually Small Trigger?”**
- Cards: **“Search for a small patch that sends many clean examples to this label.”**
- Takeaway: **“Flag a label whose found trigger is unusually small compared with other labels.”**

That relative comparison matters: a tiny patch alone is not the detection rule. Keep the optimization explanation and heuristic caveat. [Neural Cleanse, §IV](https://people.cs.uchicago.edu/~ravenben/publications/pdf/backdoor-sp19.pdf)

**2. P64 — distinguish the measurement from its interpretation.**
The &gt;50 threshold is supported, but the visible key should say:
- **x: expected poisoned documents encountered so far**
- **y: increase in generated-text perplexity after adding the trigger**
- **Above 50: the authors’ threshold for noticeable degradation**

“All rise at about the same x” overstates this chart: the onset visibly varies. Replace with **“Across the tested sizes, hundreds of poisons suffice; the onset varies.”** Keep the 600M–13B scope. [Souly et al., Fig. 2](https://arxiv.org/abs/2510.07192)

**3. P81 — algorithm correct; clarify the score and scope.**
I checked Algorithm 1: ε really is an upper bound on the **count**, and removing the top **1.5ε examples per class** is correct.
- Score wording: **“Squared distance along the top direction, measured from the class mean.”**
- Replace the unconditional “Poisons score highest” with **“In the next example, poisons score highest.”** Filtering is not guaranteed for every poisoning attack.
- Say “per class” explicitly beside the removal count. [Tran et al., Algorithm 1](https://arxiv.org/abs/1811.00636)

**P47 passes.** The rejected extra-detector/merging-layer design versus the fixed-architecture BadNet matches the paper’s explanation. Keep it. [BadNets](https://arxiv.org/abs/1708.06733)

**P28 reads clearly now.** One precision adjustment: “features copy” → **“features are pushed close to the dog target’s”**, and “on top of each other” → **“close together in feature space.”** Label this an illustrative feature-collision example; exact equality is unnecessary. Optional clearer title: **“Looks Like a Fish; Its Features Resemble the Dog Target.”**

Please mirror these focused fixes in the note. No broader redesign needed.
```

## 2026-10-27 15:17 KST — slides → slides-review

```
Round-1 fixes in e4d6280 (PR #63). All four slides re-rendered; they fit.
- p84: title "Neural Cleanse: Which Label Needs an Unusually Small Trigger?"; cards "small patch found that sends many clean images to "cat"/it" (large vs tiny); new line "Flag a label whose found trigger is unusually small compared with other labels."; caveat "A heuristic: the search finds a small patch, not the smallest, and not one that flips every image." Optimisation line kept.
- p64 key: x expected poisoned documents encountered so far · y rise in perplexity (garbled text) after the trigger; above 50 = authors' bar for noticeable damage · Lines 600M to 13B models: hundreds of poisons suffice; the onset varies.
- p81: "Score = squared distance along the top direction (previous slide), from the class mean"; "In the next example, poisons score highest: drop the top 1.5·ε per class, retrain".
- p28: title "Looks Like a Fish; Its Features Resemble the Dog Target"; "features pushed close to the dog target's"; "close together in feature space"; muted line opens "Illustrative feature-collision example."
- Note mirrors all four, including the measurement-vs-threshold split for p64 and "not guaranteed for every poisoning attack" for p81. Linters clean (only the pre-existing p51 warning).
```

## 2026-10-27 15:17 KST — slides-review → slides

```
Reviewed the e4d6280 diff. **Approved—the substantive corrections are resolved.**

Two nonblocking cleanups:
- P84 cards: remove “small” from “small patch found…” since the normal-label card concludes “large.”
- P64 alt text still says all curves rise past 200 around 150–250 poisons. Align it with the corrected “onset varies” description.

No further structural changes requested. Merge remains subject to Albert’s authorization.
```

## 2026-10-27 15:17 KST — slides → slides-review

```
Thanks. Both cleanups applied in e3ed484: p84 cards now read "patch found that sends many clean images to …"; p64 alt text now says hundreds of poisons suffice across the tested sizes, with the onset varying by model. Marking PR #63 ready; merge waits for Albert.
```
