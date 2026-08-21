# postech260821/ — POSTECH invited talk (Ok lab seminar), 2026-08-21

50-minute high-level talk for Prof. Jungseul Ok's lab (graduate AI students).
Theme: **small interventions, large effects** — high-leverage control points
in LLM reasoning and alignment. Intuition and implications only, no
derivations. The Ok-lab connection slides (SEAG/LSC, FedVPA-GP) live in the
backup section after the closer (moved 2026-08-15, Albert's request).
Folder renamed from `postech260819/` on 2026-08-20 (talk is actually
2026-08-21).

## Files

- `postech260821.html` — the deck (45 slides: 40 main + Q&A closer,
  then a backup divider + 3 backup slides)
- `figs/` — paper figures (16 PNGs; author-provided renders as of 2026-08-15)
- `figs/authors/` — lab-member headshots for section dividers (6 photos,
  from ai-isl.yonsei.ac.kr/team.html)

## postech260821.html

**Structure:** hook → 4 parts. 01 REFT (core, ~15 min) · 02 SafePath (~10 min)
· 03 Benign DPO with the GPT fine-tuning-service framing (~12 min) · 04
unlearning position (4 content slides) · two lab-publication slides before
the closer. Each section divider carries the lab authors' photos
(`.authors-row`).

### Sections (45 slides total)

Letter-suffixed slides were added after the original numbering was fixed:
12b/12c/26b/26d carry NeurIPS 2026 rebuttal experiments for REFT and
Benign DPO; 6b, 23b, 30b, 30c came from the 2026-08-14 revision. Original
slides 31–34 (part 05, open questions) were removed in that revision;
34b/34c/34d (publication records, webpage format with lab members
underlined) were added 2026-08-14/15. The 2026-08-15 revision removed the
robustness slide 26c, dropped "rebuttal" from all citations, and split the
publications list into per-category slides (quantization dropped). Later on
2026-08-15 the two Ok-lab connection slides (old 14 and 28) moved to a new
backup section (B0–B3); old 28 was split into a figure slide (B2, FedVPA-GP
Figure 1) and a comments slide (B3). The 2026-08-20 revision split slide 17
(primer text vs Figure-2 diagram → 17/17b), replaced slide 30 with two
slides adapted from the ICML 2026 deck (30/30x), corrected the primer strip
to exactly 8 tokens, and put submitted works first on 34d. The 2026-08-21
revision (day-of, 7 items) removed the synthesis slide 21, added a
Base-(before-GRPO) row to 12b's table (Pass@1/8/64 = 80.14/94.16/98.18,
arXiv 2605.28295 Tables 1/3), rewrote 12c's decoupling bullet with from→to
accuracies (92.48→90.25, 96.66→96.63; rebuttal), forced 17's primer strip
one-line with a larger follow-up line, pinned 17b's figure to the top, and
reordered 34d chronologically (submitted works last).

| # | Slide | Line |
|---|---|---|
| 1 | Title — Small Interventions, Large Effects (8/21) | 86 |
| 2 | Hook: 1 Position · 8 Tokens · 10 Pairs | 98 |
| 3 | Contents (4 parts) | 125 |
| 4 | **01 Where Rollouts Begin** (divider, Soeun Kim) | 167 |
| 5 | RLVR in One Picture (GRPO/DAPO flow, `diagram-flow lg`) | 178 |
| 6 | The Diversity Bottleneck (3 prior fixes + shared assumption) | 202 |
| 6b | Our Key Idea: Branch at the Root (SVG tree) | 228 |
| 7 | An Unlikely Lever (opener: 1st response token; XL token strip) | 259 |
| 8 | Sharp Prior, Flat Correctness (Fig 1; rank-20 = 2.7e-5; rank-~20 opener examples from Figs 9–11) | 286 |
| 9 | First Tokens Route Continuations | 306 |
| 10 | RLVR Sharpens the Wrong Habit (over-credited opener) | 331 |
| 11 | Proposed Method: REFT, Diversify Only Token One (method flow) | 356 |
| 12 | Consistent Gains, No Extra Cost (Table 1) | 380 |
| 12b | Distinguished, Not Just Another Knob (vs MT/LATR baselines + rollout cost; Base-before-GRPO row) | 403 |
| 12c | Holds at Scale, Beyond Math (9B/14B gains, code RLVR, decoupling at scale — per-model lines) | 427 |
| 13 | Explore in Training, Commit at Test | 450 |
| 15 | **02 Eight Tokens of Safety** (divider, Jeung · Yoon) | 466 |
| 16 | Reasoning Cuts Both Ways (LRM risk; safety-tax card at bottom) | 478 |
| 17 | The Safety Primer (exactly 8 tokens: \n Let 's think about safety first . — XXL strip, one line) | 500 |
| 17b | SafePath at a Glance (Figure 2 full-width, top-pinned) | 526 |
| 18 | Ninety Percent Less Harm (results) | 534 |
| 19 | Initiate, Don't Terminate (soft vs harsh primer) | 549 |
| 20 | The Primer Fires Again (emergent reactivation; enlarged fig 2c) | 562 |
| 22 | **03 Ten Harmless Pairs** (divider, Yoon · Jeung · Cho · Jeon) | 591 |
| 23 | Fine-Tuning as a Service (OpenAI DPO API, min 10 pairs) | 605 |
| 23b | Benign Data Attacks Exist, But… (TenBenign two-stage SFT + its tell) | 632 |
| 24 | The Truly Benign Attack (benign prompt · prefer helpful) | 652 |
| 25 | Frontier Models Fall for $2 (ASR 59/70/82%) | 666 |
| 26 | The Margin Has One Exit (DPO mechanism) | 680 |
| 26b | Why DPO, Not Just a Prefix (mechanism ablation on GPT-4o) | 695 |
| 26d | Nothing to Pattern-Match (any prefix works; refusal-mixture 59.13→68.40) | 720 |
| 27 | The Auditor's Dilemma (XSTest: same data, two intents) | 746 |
| 29 | **04 Behavior Is Not Deletion** (divider, Yoon · Jun) | 775 |
| 30 | One Term, Many Tasks (hub + 4 task leaves; adapted from icml2026 slide 2) | 787 |
| 30x | Suppressed Is Not Removed (GDPR promise, Dist formula, claim-vs-measure mismatch) | 824 |
| 30b | Surface Success Breaks Easily (paraphrase/fine-tune/quantization re-exposure) | 839 |
| 30c | A Matter of Removing Influence (suppress vs retrain; derived capability) | 858 |
| 34b | Papers in This Talk (4 featured entries: REFT · SafePath · Benign DPO · position) | 882 |
| 34c | Other Lab Publications: Unlearning & Safety (6 entries, full width) | 910 |
| 34d | Other Lab Publications: Discrete Diffusion (7 entries, chronological: NeurIPS 2025 · ICLR 2026 · ICML 2026 · submitted) | 940 |
| 35 | Q&A closer (albertno@yonsei.ac.kr · ai-isl.yonsei.ac.kr) | 974 |
| B0 | **Backup** (divider, dark) | 982 |
| B1 | Two Questions, One Object (SEAG/LSC connection; was slide 14) | 990 |
| B2 | Could Disentanglement Defend? (FedVPA-GP Figure 1; was slide 28) | 1009 |
| B3 | Why a Factored Space Might Help (FedVPA-GP comments; was slide 28) | 1019 |

### Papers presented (ours)

- **REFT** — Kim, No, "Where Rollouts Begin: Low-Load, High-Leverage
  First-Token Diversification for RLVR", 2026 (Figures 1–4, Table 1;
  rank-20 opener examples from Appendix Figures 9–11).
- **SafePath** — Jeung, Yoon, Kahng, No, NeurIPS 2025 (Figures 1, 2, 4, 7).
  Primer training target verified against the SAFEPATH code + DeepSeek-R1-
  Distill-Qwen-7B tokenizer: 8 tokens = `\n Let 's think about safety first .`
  (`<think>` is the anchor, not part of the 8).
- **Benign DPO attack** — Yoon, Jeung, Cho, Jeon, No, 2026 (Figures 1, 2a, 5,
  Table 4).
- **Unlearning position** — Yoon, Jun, No, ICML 2026 (slides 30–30c; the
  full treatment is `talks/icml2026/icml2026.html`).

### Other papers introduced

- TenBenign — Xie, Song, Luo, "Attack via Overfitting: 10-Shot Benign
  Fine-tuning to Jailbreak LLMs", NeurIPS 2025 (slide 23b, prior art for
  part 03).

### Ok-lab papers cited (connections, high-level)

- SEAG — Lee, Park, Kim, Ok, ACL 2025 (Figure 1, backup slide B1).
- LSC — Lee, Kim, Hwang, Park, Ok, EMNLP 2025 Findings (backup slide B1).
- FedVPA-GP — Koo, Kim, Jang, Ok, ICML 2026 (Figure 1, backup slides B2–B3).
- (PaT was cited by the removed part-05 discussion slides; `figs/pat-fig2.png`
  is kept on disk but no longer used by the deck.)

### Figure inventory (`figs/`)

reft-fig1/2/3/4, safepath-fig1/2/2c/4/7, bdpo-fig1/2a/5, seag-fig1,
fedvpa-fig1 — cited on-slide. On 2026-08-15 Albert supplied clean renders
(figs.zip, then fig_a/fig_b) replacing the PDF crops for reft-fig1–4,
safepath-fig1/2/4/7, bdpo-fig1/2a/5, seag-fig1, and adding safepath-fig2c
("SafePath at Inference" panel, slide 20 above safepath-fig4) and
fedvpa-fig1 (framework overview, backup B2). pat-fig2 and fedvpa-fig2
unused (kept for reuse). `authors/`: soeun, wonje, sangyeon, yoonjun,
dongjae, yeachan.

### Companion content

None (invited talk; speaker notes not requested).

### Cross-reference

- Unlearning position in depth: `talks/icml2026/icml2026.html` and
  `courses/privacy/lectures/05-unlearning/` (foundations + LLM decks).
- Slides 30/30x adapt slides 2–3 of `talks/icml2026/icml2026.html`
  (`.task-hub`/`.task-leaf` styles copied into this deck's local `<style>`).
