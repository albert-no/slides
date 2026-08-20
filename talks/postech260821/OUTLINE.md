# postech260821/ — POSTECH invited talk (Ok lab seminar), 2026-08-21

50-minute high-level talk for Prof. Jungseul Ok's lab (graduate AI students).
Theme: **small interventions, large effects** — high-leverage control points
in LLM reasoning and alignment. Intuition and implications only, no
derivations. The Ok-lab connection slides (SEAG/LSC, FedVPA-GP) live in the
backup section after the closer (moved 2026-08-15, Albert's request).
Folder renamed from `postech260819/` on 2026-08-20 (talk is actually
2026-08-21).

## Files

- `postech260821.html` — the deck (46 slides: 41 main + Q&A closer,
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

### Sections (46 slides total)

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
to exactly 8 tokens, and put submitted works first on 34d.

| # | Slide | Line |
|---|---|---|
| 1 | Title — Small Interventions, Large Effects (8/21) | 83 |
| 2 | Hook: 1 Position · 8 Tokens · 10 Pairs | 95 |
| 3 | Contents (4 parts) | 122 |
| 4 | **01 Where Rollouts Begin** (divider, Soeun Kim) | 164 |
| 5 | RLVR in One Picture (GRPO/DAPO flow, `diagram-flow lg`) | 175 |
| 6 | The Diversity Bottleneck (3 prior fixes + shared assumption) | 199 |
| 6b | Our Key Idea: Branch at the Root (SVG tree) | 225 |
| 7 | An Unlikely Lever (opener: 1st response token; XL token strip) | 256 |
| 8 | Sharp Prior, Flat Correctness (Fig 1; rank-20 = 2.7e-5; rank-~20 opener examples from Figs 9–11) | 283 |
| 9 | First Tokens Route Continuations | 303 |
| 10 | RLVR Sharpens the Wrong Habit (over-credited opener) | 328 |
| 11 | Proposed Method: REFT, Diversify Only Token One (method flow) | 353 |
| 12 | Consistent Gains, No Extra Cost (Table 1) | 377 |
| 12b | Distinguished, Not Just Another Knob (vs MT/LATR baselines + rollout cost) | 401 |
| 12c | Holds at Scale, Beyond Math (9B/14B gains, code RLVR, decoupling at scale — per-model lines) | 427 |
| 13 | Explore in Training, Commit at Test | 450 |
| 15 | **02 Eight Tokens of Safety** (divider, Jeung · Yoon) | 466 |
| 16 | Reasoning Cuts Both Ways (LRM risk; safety-tax card at bottom) | 478 |
| 17 | The Safety Primer (exactly 8 tokens: \n Let 's think about safety first . — XXL strip) | 500 |
| 17b | SafePath at a Glance (Figure 2 full-width) | 526 |
| 18 | Ninety Percent Less Harm (results) | 534 |
| 19 | Initiate, Don't Terminate (soft vs harsh primer) | 549 |
| 20 | The Primer Fires Again (emergent reactivation; enlarged fig 2c) | 562 |
| 21 | One Lever, Two Directions (REFT ↔ SafePath synthesis) | 589 |
| 22 | **03 Ten Harmless Pairs** (divider, Yoon · Jeung · Cho · Jeon) | 613 |
| 23 | Fine-Tuning as a Service (OpenAI DPO API, min 10 pairs) | 627 |
| 23b | Benign Data Attacks Exist, But… (TenBenign two-stage SFT + its tell) | 654 |
| 24 | The Truly Benign Attack (benign prompt · prefer helpful) | 674 |
| 25 | Frontier Models Fall for $2 (ASR 59/70/82%) | 688 |
| 26 | The Margin Has One Exit (DPO mechanism) | 702 |
| 26b | Why DPO, Not Just a Prefix (mechanism ablation on GPT-4o) | 717 |
| 26d | Nothing to Pattern-Match (any prefix works; refusal-mixture 59.13→68.40) | 742 |
| 27 | The Auditor's Dilemma (XSTest: same data, two intents) | 768 |
| 29 | **04 Behavior Is Not Deletion** (divider, Yoon · Jun) | 797 |
| 30 | One Term, Many Tasks (hub + 4 task leaves; adapted from icml2026 slide 2) | 809 |
| 30x | Suppressed Is Not Removed (GDPR promise, Dist formula, claim-vs-measure mismatch) | 846 |
| 30b | Surface Success Breaks Easily (paraphrase/fine-tune/quantization re-exposure) | 861 |
| 30c | A Matter of Removing Influence (suppress vs retrain; derived capability) | 880 |
| 34b | Papers in This Talk (4 featured entries: REFT · SafePath · Benign DPO · position) | 904 |
| 34c | Other Lab Publications: Unlearning & Safety (6 entries, full width) | 932 |
| 34d | Other Lab Publications: Discrete Diffusion (7 entries; submitted first: Reversal Curse · Confidence Shortcut · JUMP) | 962 |
| 35 | Q&A closer (albertno@yonsei.ac.kr · ai-isl.yonsei.ac.kr) | 996 |
| B0 | **Backup** (divider, dark) | 1004 |
| B1 | Two Questions, One Object (SEAG/LSC connection; was slide 14) | 1012 |
| B2 | Could Disentanglement Defend? (FedVPA-GP Figure 1; was slide 28) | 1031 |
| B3 | Why a Factored Space Might Help (FedVPA-GP comments; was slide 28) | 1041 |

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
