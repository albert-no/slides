# postech260819/ — POSTECH invited talk (Ok lab seminar), 2026-08-19

50-minute high-level talk for Prof. Jungseul Ok's lab (graduate AI students).
Theme: **small interventions, large effects** — high-leverage control points
in LLM reasoning and alignment. Intuition and implications only, no
derivations. Each part ends by connecting to the Ok lab's work (SEAG, LSC,
PaT, FedVPA-GP) at a high level.

## Files

- `postech260819.html` — the deck (35 slides)
- `figs/` — figure crops captured from the cited papers (14 PNGs)

## postech260819.html

**Structure:** hook → 5 parts. 01 REFT (core, ~15 min) · 02 SafePath (~10 min)
· 03 Benign DPO with the GPT fine-tuning-service framing (~12 min) · 04
unlearning position (short, 1 content slide) · 05 synthesis + 4 discussion
questions aimed at the audience's toolkit.

### Sections (35 slides total)

| # | Slide | Line |
|---|---|---|
| 1 | Title — Small Interventions, Large Effects | 33 |
| 2 | Hook: 1 Position · 8 Tokens · 10 Pairs | 45 |
| 3 | Contents (5 parts) | 72 |
| 4 | **01 Where Rollouts Begin** (divider) | 122 |
| 5 | RLVR in One Picture (GRPO/DAPO flow) | 130 |
| 6 | The Diversity Bottleneck (SVG tree: methods branch late) | 154 |
| 7 | An Unlikely Lever (first token after `<think>`) | 197 |
| 8 | Sharp Prior, Flat Correctness (rank-20: 70.4% vs 75.3%) | 224 |
| 9 | First Tokens Route Continuations | 247 |
| 10 | RLVR Sharpens the Wrong Habit (over-credited opener) | 270 |
| 11 | REFT: Diversify Only Token One (method flow) | 295 |
| 12 | Consistent Gains, No Extra Cost (Table 1) | 319 |
| 13 | Explore in Training, Commit at Test | 343 |
| 14 | Two Questions, One Object (SEAG/LSC connection) | 357 |
| 15 | **02 Eight Tokens of Safety** (divider) | 378 |
| 16 | Reasoning Cuts Both Ways (LRM safety tax) | 386 |
| 17 | The Safety Primer (8-token fine-tune) | 417 |
| 18 | Ninety Percent Less Harm (results) | 442 |
| 19 | Initiate, Don't Terminate (soft vs harsh primer) | 457 |
| 20 | The Primer Fires Again (emergent reactivation) | 470 |
| 21 | One Lever, Two Directions (REFT ↔ SafePath synthesis) | 495 |
| 22 | **03 Ten Harmless Pairs** (divider) | 519 |
| 23 | Fine-Tuning as a Service (OpenAI DPO API, min 10 pairs) | 527 |
| 24 | The Truly Benign Attack (benign prompt · prefer helpful) | 554 |
| 25 | Frontier Models Fall for $2 (ASR 59/70/82%) | 568 |
| 26 | The Margin Has One Exit (DPO mechanism) | 582 |
| 27 | The Auditor's Dilemma (XSTest: same data, two intents) | 597 |
| 28 | Could Disentanglement Defend? (FedVPA-GP connection) | 624 |
| 29 | **04 Behavior Is Not Deletion** (divider) | 649 |
| 30 | Suppressed Is Not Removed (strict promise vs practice) | 657 |
| 31 | **05 Small Levers, Open Questions** (divider) | 688 |
| 32 | Four Levers, Four Guarantees (taxonomy table) | 696 |
| 33 | Discussion: Adaptive Exploration (Q1 gated REFT, Q2 PaT analog) | 717 |
| 34 | Discussion: Safety Under Small Updates (Q3 compose, Q4 certify axis) | 736 |
| 35 | Q&A closer | 757 |

### Papers presented (ours)

- **REFT** — Kim, No, "Where Rollouts Begin: Low-Load, High-Leverage
  First-Token Diversification for RLVR", 2026 (Figures 1–4, Table 1).
- **SafePath** — Jeung, Yoon, Kahng, No, NeurIPS 2025 (Figures 1, 2, 4, 7).
- **Benign DPO attack** — Yoon, Jeung, Cho, Jeon, No, 2026 (Figures 1, 2a, 5,
  Table 4).
- **Unlearning position** — Yoon, Jun, No, ICML 2026 (definition only; the
  full treatment is `talks/icml2026/icml2026.html`).

### Ok-lab papers cited (connections, high-level)

- SEAG — Lee, Park, Kim, Ok, ACL 2025 (Figure 1, slide 14).
- LSC — Lee, Kim, Hwang, Park, Ok, EMNLP 2025 Findings (slide 14).
- PaT — Yoon, Lee, Song, Wang, Chen, Ok, ACL 2026 (Figure 2, slide 33).
- FedVPA-GP — Koo, Kim, Jang, Ok, ICML 2026 (Figure 2, slide 28).

### Figure inventory (`figs/`)

reft-fig1/2/3/4, safepath-fig1/2/4/7, bdpo-fig1/2a/5, seag-fig1, pat-fig2,
fedvpa-fig2 — all cropped from the papers' PDFs, cited on-slide.

### Companion content

None (invited talk; speaker notes not requested).

### Cross-reference

- Unlearning position in depth: `talks/icml2026/icml2026.html` and
  `courses/privacy/lectures/05-unlearning/` (foundations + LLM decks).
