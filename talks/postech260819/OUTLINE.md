# postech260819/ — POSTECH invited talk (Ok lab seminar), 2026-08-19

50-minute high-level talk for Prof. Jungseul Ok's lab (graduate AI students).
Theme: **small interventions, large effects** — high-leverage control points
in LLM reasoning and alignment. Intuition and implications only, no
derivations. Parts 1–3 each end by connecting to the Ok lab's work (SEAG,
LSC, FedVPA-GP) at a high level.

## Files

- `postech260819.html` — the deck (40 slides)
- `figs/` — figure crops captured from the cited papers (14 PNGs)
- `figs/authors/` — lab-member headshots for section dividers (6 photos,
  from ai-isl.yonsei.ac.kr/team.html)

## postech260819.html

**Structure:** hook → 4 parts. 01 REFT (core, ~15 min) · 02 SafePath (~10 min)
· 03 Benign DPO with the GPT fine-tuning-service framing (~12 min) · 04
unlearning position (3 content slides). Each section divider carries the
lab authors' photos (`.authors-row`).

### Sections (40 slides total)

Letter-suffixed slides were added after the original numbering was fixed:
12b/12c/26b/26c/26d carry NeurIPS 2026 rebuttal experiments for REFT and
Benign DPO; 6b, 23b, 30b, 30c came from the 2026-08-14 revision. Original
slides 31–34 (part 05, open questions) were removed in that revision.

| # | Slide | Line |
|---|---|---|
| 1 | Title — Small Interventions, Large Effects | 46 |
| 2 | Hook: 1 Position · 8 Tokens · 10 Pairs | 58 |
| 3 | Contents (4 parts) | 85 |
| 4 | **01 Where Rollouts Begin** (divider, Soeun Kim) | 127 |
| 5 | RLVR in One Picture (GRPO/DAPO flow, `diagram-flow lg`) | 138 |
| 6 | The Diversity Bottleneck (3 prior fixes + shared assumption) | 162 |
| 6b | Our Key Idea: Branch at the Root (SVG tree) | 188 |
| 7 | An Unlikely Lever (opener: 1st response token, or 1st after `<think>`) | 219 |
| 8 | Sharp Prior, Flat Correctness (full-height Fig 1; rank-20 = 2.7e-5) | 246 |
| 9 | First Tokens Route Continuations | 257 |
| 10 | RLVR Sharpens the Wrong Habit (over-credited opener) | 282 |
| 11 | REFT: Diversify Only Token One (method flow) | 307 |
| 12 | Consistent Gains, No Extra Cost (Table 1) | 331 |
| 12b | Distinguished, Not Just Another Knob (rebuttal: vs MT/LATR baselines + rollout cost) | 355 |
| 12c | Holds at Scale, Beyond Math (rebuttal: 9B/14B gains, code RLVR, decoupling at scale) | 381 |
| 13 | Explore in Training, Commit at Test | 403 |
| 14 | Two Questions, One Object (SEAG/LSC connection) | 417 |
| 15 | **02 Eight Tokens of Safety** (divider, Jeung · Yoon) | 438 |
| 16 | Reasoning Cuts Both Ways (LRM risk; safety-tax card at bottom) | 450 |
| 17 | The Safety Primer (8-token fine-tune) | 472 |
| 18 | Ninety Percent Less Harm (results) | 497 |
| 19 | Initiate, Don't Terminate (soft vs harsh primer) | 512 |
| 20 | The Primer Fires Again (emergent reactivation) | 525 |
| 21 | One Lever, Two Directions (REFT ↔ SafePath synthesis) | 550 |
| 22 | **03 Ten Harmless Pairs** (divider, Yoon · Jeung · Cho · Jeon) | 574 |
| 23 | Fine-Tuning as a Service (OpenAI DPO API, min 10 pairs) | 588 |
| 23b | Benign Data Attacks Exist, But… (TenBenign two-stage SFT + its tell) | 615 |
| 24 | The Truly Benign Attack (benign prompt · prefer helpful) | 635 |
| 25 | Frontier Models Fall for $2 (ASR 59/70/82%) | 649 |
| 26 | The Margin Has One Exit (DPO mechanism) | 663 |
| 26b | Why DPO, Not Just a Prefix (rebuttal: mechanism ablation on GPT-4o) | 678 |
| 26c | The Finding Holds Up (rebuttal: seeds/judges robustness + test-time safeguards) | 703 |
| 26d | Nothing to Pattern-Match (rebuttal: any prefix works; refusal-mixture 59.13→68.40) | 730 |
| 27 | The Auditor's Dilemma (XSTest: same data, two intents) | 756 |
| 28 | Could Disentanglement Defend? (FedVPA-GP connection) | 783 |
| 29 | **04 Behavior Is Not Deletion** (divider, Yoon · Jun) | 808 |
| 30 | Suppressed Is Not Removed (strict promise vs practice) | 820 |
| 30b | Surface Success Breaks Easily (paraphrase/fine-tune/quantization re-exposure) | 849 |
| 30c | A Matter of Removing Influence (suppress vs retrain; derived capability) | 868 |
| 35 | Q&A closer (albertno@yonsei.ac.kr · ai-isl.yonsei.ac.kr) | 892 |

### Papers presented (ours)

- **REFT** — Kim, No, "Where Rollouts Begin: Low-Load, High-Leverage
  First-Token Diversification for RLVR", 2026 (Figures 1–4, Table 1).
- **SafePath** — Jeung, Yoon, Kahng, No, NeurIPS 2025 (Figures 1, 2, 4, 7).
- **Benign DPO attack** — Yoon, Jeung, Cho, Jeon, No, 2026 (Figures 1, 2a, 5,
  Table 4).
- **Unlearning position** — Yoon, Jun, No, ICML 2026 (slides 30–30c; the
  full treatment is `talks/icml2026/icml2026.html`).

### Other papers introduced

- TenBenign — Xie, Song, Luo, "Attack via Overfitting: 10-Shot Benign
  Fine-tuning to Jailbreak LLMs", NeurIPS 2025 (slide 23b, prior art for
  part 03).

### Ok-lab papers cited (connections, high-level)

- SEAG — Lee, Park, Kim, Ok, ACL 2025 (Figure 1, slide 14).
- LSC — Lee, Kim, Hwang, Park, Ok, EMNLP 2025 Findings (slide 14).
- FedVPA-GP — Koo, Kim, Jang, Ok, ICML 2026 (Figure 2, slide 28).
- (PaT was cited by the removed part-05 discussion slides; `figs/pat-fig2.png`
  is kept on disk but no longer used by the deck.)

### Figure inventory (`figs/`)

reft-fig1/2/3/4, safepath-fig1/2/4/7, bdpo-fig1/2a/5, seag-fig1,
fedvpa-fig2 — cropped from the papers' PDFs, cited on-slide. pat-fig2 unused
(kept for reuse). safepath-fig2 bottom-cropped 2026-08-14 to drop a
half-clipped caption row. `authors/`: soeun, wonje, sangyeon, yoonjun,
dongjae, yeachan.

### Companion content

None (invited talk; speaker notes not requested).

### Cross-reference

- Unlearning position in depth: `talks/icml2026/icml2026.html` and
  `courses/privacy/lectures/05-unlearning/` (foundations + LLM decks).
