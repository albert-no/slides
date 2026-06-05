# infotheory/ — Information Theory & its applications in deep learning

Master-level course (AAI5016). Top-level folders separate the four artifact types:
slides, LaTeX lecture notes, exams, and the frozen legacy source.

## Folder map

- **`lectures/`** — the slide series: 8 numbered topic folders (`01-entropy/` … `08-ib/`),
  each a paired `<deck>.html` + `<deck>-note.html`. This is the primary teaching material.
  Full section table, cross-deck theorem pointers, and reading order live in
  **`lectures/OUTLINE.md`**.
- **`notes/`** — clean, canonical LaTeX lecture notes (2026). `main.tex` +
  `section/` (8 subfiled `.tex`, one per course unit) + `macro.tex`, `aai5016.sty`,
  and only the images actually referenced. Compiles standalone (needs `bbm.sty` from a
  full TeX / Overleaf install). This is the working copy to edit going forward.
- **`exam/`** — flat folder of finals: `final24/25/26.{tex,pdf}`, `final26.html`,
  `final26sol.pdf`, `backup26.html`, and shared `style/` (`it_hw.sty`, `macro.tex`).
  Earlier-year exam variants are preserved in the archive (`overleaf/hwexam/`).
- **`overleaf/`** — **frozen legacy archive** (do not edit). Full 2026 Overleaf export:
  `lecturenote/` (original tree), `hwexam/` (all exam years), `images/`, style files.
  `lecturenote/` here is the historical source; the cleaned working copy is the
  top-level `notes/`.
- **`elgamal.pdf`** — loose reference handout (ElGamal, *Lecture Notes on Network
  Information Theory* style material).

## Lecture topics (see `lectures/OUTLINE.md` for the full index)

| # | Folder | Topic |
|---|---|---|
| 1 | `lectures/01-entropy/` | Entropy, KL, joint/conditional, MI, DPI, Fano |
| 2 | `lectures/02-lossless/` | Lossless compression: Kraft, Huffman, AEP, arithmetic, LZ |
| 3 | `lectures/03-diffentropy/` | Differential entropy, MaxEnt/Gaussian/EPI, AWGN, water-filling, I-MMSE |
| 4 | `lectures/04-lossy/` | Rate–distortion + modern LLM compression (QUIP#, TURBOQUANT) |
| 5 | `lectures/05-mi/` | Variational MI bounds (BA, DV, NWJ, MINE), InfoNCE, CLIP |
| 6 | `lectures/06-divergence/` | $f$-divergence + GAN, Fisher divergence + denoising score matching |
| 7 | `lectures/07-diffusion/` | VAE/ELBO, hierarchical VAE, parameterizations, ELBO $\equiv$ DSM |
| 8 | `lectures/08-ib/` | Information Bottleneck: IB Lagrangian, VIB, information plane |

## Conventions

- **Deck/note pairing**: every `<deck>.html` has a `<deck>-note.html` companion —
  deck = "what is true"; note = "why and how to apply".
- **OUTLINE tiers**: this root file = folder map; `lectures/OUTLINE.md` = series index
  with per-deck section tables and the cross-deck theorem-pointer table; each
  `lectures/NN-*/OUTLINE.md` = that deck's detailed line-numbered outline.
- **Editing**: edit slides under `lectures/`, notes under `notes/`. Never edit
  `overleaf/` — it is the archive.
