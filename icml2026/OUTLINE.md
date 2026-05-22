# icml2026/ — ICML 2026 5-min talk

Recorded talk (SlidesLive) for ICML 2026 Position paper. Max length 5 minutes.
Poster ID 67198 · <https://icml.cc/virtual/2026/poster/67198> (time/location TBA).

## Files

- `icml2026.html` — the deck (10 slides, ~30 sec each)
- `unlearning_position.pdf` — the position paper (Yoon, Jun, No, ICML 2026)
- `instruction.pdf` — SlidesLive recording instructions (deadline 2026-06-01 AOE)

## icml2026.html

**Topic:** Position paper — "machine unlearning" should be reserved for dataset-defined deletion (retrain-indistinguishability); other usages need different terminology.

### Sections (10 slides total)

| # | Slide | Line |
|---|---|---|
| 1 | Title — Yoon, Jun, No, ICML 2026 | ~24 |
| 2 | Hook: "Unlearning" labels too many things | ~38 |
| 3 | What unlearning should mean (formal definition) | ~53 |
| 4 | Taxonomy: suppression · obfuscation · editing · refusal | ~65 |
| 5 | Benchmarks reward surface suppression (TOFU / MUSE / RWKU / WMDP) | ~78 |
| 6 | Derived capabilities — synthetic reasoning, poisoning | ~91 |
| 7 | Adversarial probes break surface success | ~103 |
| 8 | Call for action — reference model + derived-capability probes | ~117 |
| 9 | Position restated | ~131 |
| 10 | **See you at the poster!** (URL, ID 67198) | ~142 |

### Key claims

- Machine unlearning $=$ $\mathrm{Dist}(\mathcal{L}(\Theta'), \mathcal{L}(\Theta_R)) \le \tau$ with $\Theta_R \sim \mathrm{Train}(D \setminus F)$ (slide 3).
- Four reuses of "unlearning" by intent: output suppression, representation obfuscation, knowledge editing, behavioral refusal (slide 4).
- Output-failure benchmarks (lower ROUGE / QA acc / likelihood) without a retrain reference $\ne$ removing training influence (slide 5).
- Derived capabilities (transferable skills induced by $F$) survive surface forgetting (slide 6).
- Recommendation: reference model with provenance, distributional distances, derived-capability probes, intervention-based recovery tests (slide 8).

### Companion content

None. Paper PDF lives next to the deck for reference.

### Cross-reference

- Background lecture: `privacy/unlearning/unlearning.html` — full lecture-length treatment of unlearning definitions, classification, LLM unlearning, benchmarks. The ICML 2026 deck distills the *position* into 10 slides.
