# 2026-10-25 — trustworthy-ai lec09 motivation-first revision (PR #58)

Verbatim slides ↔ slides-review transcript, in order, KST timestamps.

## 2026-10-25 00:22 KST — slides → slides-review

```
Review request — PR #58 (draft): https://github.com/albert-no/slides/pull/58
Branch trustworthy-ai-lec09-motivation-revision, commit 0401c6d.

Trustworthy AI lec09 (poisoning and backdoors), initial motivation-first revision following the lec08 pattern (#56). Albert asked for this before his detailed read, and also asked for real-world poisoning examples targeting frontier LLMs.

Deck 59 → 91 slides, 7 sections:
01 Why We Want Integrity (3–14): answer-key ELI5, Clever Hans tag (Lapuschkin 2019 Fig 2a, new crop), accident vs on purpose, stop sign, Tay (quote, mechanism not claimed), integrity def + 3 failure modes
02 Who Poisons, and Why (15–18): five motives; SpamBayes (Nelson LEET 2008: 101 emails = 1% of 10k)
03 Data Poisoning (19–32) / 04 Backdoors (33–47): Biggio, Frogs, BadNets setup slides; feature-space primer; guard-dog ELI5; clean accuracy + ASR
05 Web-Scale Data (48–57): Wikipedia dump timeline; Nightshade motive + Fig 7 (new crop, 50/100/300 poisons)
06 Poisoning Language Models (58–75): four doors; RLHF poisoning (Rando & Tramèr: ~5% to survive RLHF); PoisonedRAG (5 texts, ~90%); in the wild 69–71: fake support numbers in Perplexity / Google AI Overview (Aurascape, 8 Dec 2025), Pravda network (NewsGuard, 6 Mar 2025: 33.5% repeated, 7/10 cited), documented-vs-not
07 Defenses (76–91): why poison is hard to find; ELI5 slides for spectral signatures and Neural Cleanse

Note rebuilt (91 entries, 7 blocks = 90 min). OUTLINE leaf updated, outline-lint clean. Tech unchanged.

Please check especially: scoping of the in-the-wild slides (69–71 frame these as retrieval-layer, not weight poisoning; "LLM grooming" attributed to a watchdog group), the Tay framing (10), and pacing (18 min for section 06).
Known: lint warns on a `$60` inside SVG text (slide 51), pre-existing and renders literally as intended.
```
