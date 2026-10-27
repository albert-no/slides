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
