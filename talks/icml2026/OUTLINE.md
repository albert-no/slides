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
| 1 | Title — Yoon\*, Jun\*, No (with photos for co-first authors) | 58 |
| 2 | The Initial Definition of Unlearning (formal, retrain-indist.) | 81 |
| 3 | One Term, Many Tasks — diagram of 4 task branches | 99 |
| 4 | What Today's Papers Actually Do — manual output control | 139 |
| 5 | Benchmarks Check Output Failure — no retrained reference | 155 |
| 6 | Suppressing Output Is Not Enough — derived capabilities | 189 |
| 7 | Surface Success Breaks Easily — adversarial probes | 213 |
| 8 | The Mismatch in the Literature — frame vs method vs metric | 233 |
| 9 | Pick a Lane — indistinguishability OR output control | 258 |
| 10 | **See you at the poster!** (URL, ID 67198, time/location) | 281 |

### Key claims

- Machine unlearning $=$ $\mathrm{Dist}(\mathcal{L}(\Theta'), \mathcal{L}(\Theta_R)) \le \tau$ with $\Theta_R \sim \mathrm{Train}(D \setminus F)$ (slide 3 — initial definition from Ginart / Guo / Izzo).
- Four reuses of "unlearning" by intent: output suppression, representation obfuscation, knowledge editing, behavioral refusal (slide 4 — all manual output control).
- Output-failure benchmarks (lower ROUGE / QA acc / likelihood) without a retrain reference $\ne$ removing training influence (slide 5).
- Derived capabilities (transferable skills induced by $F$) survive surface forgetting (slide 6).
- Mismatch in the literature: papers cite retrain-indistinguishability but implement output suppression and score with output metrics (slide 8).
- Recommendation: pick a lane — either compare to retrained reference (indistinguishability) or state the goal is output control / alignment and stop claiming indistinguishability (slide 9).

### Citations used (all verified against official venues)

- Slide 3: Ginart et al., NeurIPS 2019 · Guo et al., ICML 2020 · Izzo et al., AISTATS 2021.
- Slide 6: Pawelczyk et al., "Machine Unlearning Fails to Remove Data Poisoning Attacks", ICLR 2025 · Thaker et al., "Guardrail Baselines for Unlearning in LLMs", SeT LLM @ ICLR 2024 · Jia et al., "SOUL", EMNLP 2024.
- Slide 7: Maini et al., TOFU, COLM 2024 · Lynch et al., "Eight Methods…", arXiv 2024 · Łucki et al., "Adversarial Perspective", TMLR 2025 · Zhang et al., "Catastrophic Failure of LLM Unlearning via Quantization", ICLR 2025 · Yoon et al., "Rethinking Benign Relearning", ICLR 2026.

### Companion content

None. Paper PDF lives next to the deck for reference.

### Cross-reference

- Background lecture: `privacy/unlearning/unlearning.html` — full lecture-length treatment of unlearning definitions, classification, LLM unlearning, benchmarks. The ICML 2026 deck distills the *position* into 10 slides.
