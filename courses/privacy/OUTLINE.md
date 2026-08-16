# privacy/ — Privacy, copyright & provenance in generative models

Master-level course. Top-level folders separate the artifact types: slide lectures,
exams, and the frozen Overleaf archive.

## Folder map

- **`lectures/`** — the slide series: 6 numbered topic folders (`01-dp/` … `06-watermark/`).
  DP is an 8-deck series; generative is a 6-deck review (5 diffusion + 1 LLM); MIA is a 5-deck
  series; memorization and unlearning are 2-deck series; watermark is a single deck. Full
  section tables, cross-deck theorem pointers, reading order, and the quick-lookup table live
  in **`lectures/OUTLINE.md`**.
- **`exam/`** — homework / midterm / final set: HW1–4 (`.tex`/`.pdf`, HW4 also `.html`),
  midterms 2025–26 and finals 2024–25 (PDF), 2026/27 final drafts (`.tex`), `hw4old.tex` (prior
  10-problem draft), `backup-problems/` (the 5 problems cut from HW4), and shared style
  (`math_hw.sty`, `versions.sty`, `math_commands.tex`). Full table in **`exam/OUTLINE.md`**.
- **`overleaf/`** — **frozen legacy archive** (do not edit). Full Overleaf export: lecture-note
  source (`1_dp.tex`, `2_difffusion.tex`, `3_watermark.tex`, `4_MIA.tex`), `hw_exam/` (all
  homework + exam `.tex`, including per-year `2024-1/`, `2025-1/`), `images/`, `old/` drafts,
  `references.bib`, and style files. The slide decks under `lectures/` are the working copy.
- **`privacy.md`**, **`slide.pdf`** — loose course material (syllabus notes; the unlearning
  source talk).

## Lecture topics (see `lectures/OUTLINE.md` for the full index)

| # | Folder | Topic |
|---|---|---|
| 1 | `lectures/01-dp/` | Differential privacy: reconstruction → pure/approx DP → DP-SGD → RDP → PATE → DP-FL capstone (NeurIPS 2023) |
| 2 | `lectures/02-generative/` | Generative-model review: diffusion (Bayes-route, DDPM, SDE, DDIM, guidance/discrete) + brief LLM deck |
| 3 | `lectures/03-memorization/` | Memorization in diffusion & LLMs: lawsuits, detection, SAIL, CLIP-pad, canary→ACR |
| 4 | `lectures/04-mia/` | Membership inference attacks: foundations, shadow models, theory, LiRA/RMIA, LLM MIA |
| 5 | `lectures/05-unlearning/` | Machine unlearning: certified/Newton, classification & LLM methods, benchmarks, lab |
| 6 | `lectures/06-watermark/` | LLM watermarking: green-list, distortion-free, undetectable, robustness, radioactivity |

## Conventions

- **Deck/note pairing**: deck = "what is true"; note = "why and how to apply". The diffusion,
  memorization, MIA, unlearning and watermark decks have note companions; `01-dp/` (8 decks)
  and `02-generative/llm.html` do not. Filenames use the singular `<deck>-note.html`, except
  `05-unlearning/`, which uses the plural `<deck>-notes.html` for legacy reasons.
- **OUTLINE tiers**: this root file = folder map; `lectures/OUTLINE.md` = series index with the
  cross-deck quick-lookup table and theme connections; each `lectures/NN-*/OUTLINE.md` = that
  deck's detailed line-numbered outline.
- **Editing**: edit slides under `lectures/`; reference path from a deck is `../../../../reference/`
  (four levels: deck → `NN-topic` → `lectures` → `privacy` → `courses` → repo root).
