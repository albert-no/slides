# privacy/ — Privacy, copyright & provenance in generative models

Master-level course. Top-level folders separate the artifact types: slide lectures
and exams.

## Folder map

- **`lectures/`** — the slide series: 6 numbered topic folders (`01-dp/` … `06-watermark/`).
  DP and MIA are multi-deck series with paired `<deck>-note.html` companions; generative is a
  6-deck review (5 diffusion + 1 LLM); memorization/unlearning are short 2-deck series and
  watermark is a single deck. Full section tables, cross-deck theorem pointers, reading order,
  and the quick-lookup table live in **`lectures/OUTLINE.md`**.
- **`exam/`** — homework / exam set: `hw1sol`–`hw4` (`.tex`/`.pdf`), `hw4.html` + `hw4sol.html`,
  and shared style (`math_hw.sty`, `versions.sty`, `math_commands.tex`).
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

- **Deck/note pairing**: DP, generative (diffusion), and MIA decks have a `<deck>-note.html`
  companion — deck = "what is true"; note = "why and how to apply".
- **OUTLINE tiers**: this root file = folder map; `lectures/OUTLINE.md` = series index with the
  cross-deck quick-lookup table and theme connections; each `lectures/NN-*/OUTLINE.md` = that
  deck's detailed line-numbered outline.
- **Editing**: edit slides under `lectures/`; reference path from a deck is `../../../../reference/`
  (four levels: deck → `NN-topic` → `lectures` → `privacy` → `courses` → repo root).
