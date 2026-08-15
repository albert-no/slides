# postech260819/ — POSTECH invited talk (Ok lab seminar), 2026-08-19

50-minute high-level talk for Prof. Jungseul Ok's lab (graduate AI students).
Theme: **small interventions, large effects** — high-leverage control points
in LLM reasoning and alignment. Intuition and implications only, no
derivations. Parts 1–3 each end by connecting to the Ok lab's work (SEAG,
LSC, FedVPA-GP) at a high level.

## Files

- `postech260819.html` — the deck (42 slides)
- `figs/` — paper figures (15 PNGs; author-provided renders as of 2026-08-15)
- `figs/authors/` — lab-member headshots for section dividers (6 photos,
  from ai-isl.yonsei.ac.kr/team.html)

## postech260819.html

**Structure:** hook → 4 parts. 01 REFT (core, ~15 min) · 02 SafePath (~10 min)
· 03 Benign DPO with the GPT fine-tuning-service framing (~12 min) · 04
unlearning position (3 content slides) · two lab-publication slides before
the closer. Each section divider carries the lab authors' photos
(`.authors-row`).

### Sections (42 slides total)

Letter-suffixed slides were added after the original numbering was fixed:
12b/12c/26b/26d carry NeurIPS 2026 rebuttal experiments for REFT and
Benign DPO; 6b, 23b, 30b, 30c came from the 2026-08-14 revision. Original
slides 31–34 (part 05, open questions) were removed in that revision;
34b/34c/34d (publication records, webpage format with lab members
underlined) were added 2026-08-14/15. The 2026-08-15 revision removed the
robustness slide 26c, dropped "rebuttal" from all citations, and split the
publications list into per-category slides (quantization dropped).

| # | Slide | Line |
|---|---|---|
| 1 | Title — Small Interventions, Large Effects | 64 |
| 2 | Hook: 1 Position · 8 Tokens · 10 Pairs | 76 |
| 3 | Contents (4 parts) | 103 |
| 4 | **01 Where Rollouts Begin** (divider, Soeun Kim) | 145 |
| 5 | RLVR in One Picture (GRPO/DAPO flow, `diagram-flow lg`) | 156 |
| 6 | The Diversity Bottleneck (3 prior fixes + shared assumption) | 180 |
| 6b | Our Key Idea: Branch at the Root (SVG tree) | 206 |
| 7 | An Unlikely Lever (opener: 1st response token; XL token strip) | 237 |
| 8 | Sharp Prior, Flat Correctness (full-height Fig 1; rank-20 = 2.7e-5) | 264 |
| 9 | First Tokens Route Continuations | 275 |
| 10 | RLVR Sharpens the Wrong Habit (over-credited opener) | 300 |
| 11 | REFT: Diversify Only Token One (method flow) | 325 |
| 12 | Consistent Gains, No Extra Cost (Table 1) | 349 |
| 12b | Distinguished, Not Just Another Knob (vs MT/LATR baselines + rollout cost) | 373 |
| 12c | Holds at Scale, Beyond Math (9B/14B gains, code RLVR, decoupling at scale) | 399 |
| 13 | Explore in Training, Commit at Test | 421 |
| 14 | Two Questions, One Object (SEAG/LSC connection) | 435 |
| 15 | **02 Eight Tokens of Safety** (divider, Jeung · Yoon) | 456 |
| 16 | Reasoning Cuts Both Ways (LRM risk; safety-tax card at bottom) | 468 |
| 17 | The Safety Primer (8-token fine-tune) | 490 |
| 18 | Ninety Percent Less Harm (results) | 515 |
| 19 | Initiate, Don't Terminate (soft vs harsh primer) | 530 |
| 20 | The Primer Fires Again (emergent reactivation) | 543 |
| 21 | One Lever, Two Directions (REFT ↔ SafePath synthesis) | 570 |
| 22 | **03 Ten Harmless Pairs** (divider, Yoon · Jeung · Cho · Jeon) | 594 |
| 23 | Fine-Tuning as a Service (OpenAI DPO API, min 10 pairs) | 608 |
| 23b | Benign Data Attacks Exist, But… (TenBenign two-stage SFT + its tell) | 635 |
| 24 | The Truly Benign Attack (benign prompt · prefer helpful) | 655 |
| 25 | Frontier Models Fall for $2 (ASR 59/70/82%) | 669 |
| 26 | The Margin Has One Exit (DPO mechanism) | 683 |
| 26b | Why DPO, Not Just a Prefix (mechanism ablation on GPT-4o) | 698 |
| 26d | Nothing to Pattern-Match (any prefix works; refusal-mixture 59.13→68.40) | 723 |
| 27 | The Auditor's Dilemma (XSTest: same data, two intents) | 749 |
| 28 | Could Disentanglement Defend? (FedVPA-GP connection) | 776 |
| 29 | **04 Behavior Is Not Deletion** (divider, Yoon · Jun) | 801 |
| 30 | Suppressed Is Not Removed (strict promise vs practice) | 813 |
| 30b | Surface Success Breaks Easily (paraphrase/fine-tune/quantization re-exposure) | 842 |
| 30c | A Matter of Removing Influence (suppress vs retrain; derived capability) | 861 |
| 34b | Papers in This Talk (4 featured entries: REFT · SafePath · Benign DPO · position) | 885 |
| 34c | Other Lab Publications: Unlearning & Safety (6 entries, full width) | 913 |
| 34d | Other Lab Publications: Discrete Diffusion (7 entries, full width) | 943 |
| 35 | Q&A closer (albertno@yonsei.ac.kr · ai-isl.yonsei.ac.kr) | 977 |

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

reft-fig1/2/3/4, safepath-fig1/2/2c/4/7, bdpo-fig1/2a/5, seag-fig1,
fedvpa-fig2 — cited on-slide. On 2026-08-15 Albert supplied clean renders
(figs.zip) replacing the PDF crops for reft-fig1–4, safepath-fig1/2/4/7,
bdpo-fig1/2a/5, and adding safepath-fig2c ("SafePath at Inference" panel,
slide 20 above safepath-fig4). pat-fig2 unused (kept for reuse). `authors/`:
soeun, wonje, sangyeon, yoonjun, dongjae, yeachan.

### Companion content

None (invited talk; speaker notes not requested).

### Cross-reference

- Unlearning position in depth: `talks/icml2026/icml2026.html` and
  `courses/privacy/lectures/05-unlearning/` (foundations + LLM decks).
