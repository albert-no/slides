# infotheory/notes/ — LaTeX lecture notes (canonical, 2026)

Clean working copy of the AAI5016 lecture notes. Edit here; the original Overleaf
export is frozen at `../overleaf/lecturenote/`.

## Build

`main.tex` is the entry point: preamble + `\subfile{section/<unit>.tex}` ×8.
Compile with `pdflatex main.tex` (needs `bbm.sty` from a full TeX / Overleaf install).
`\graphicspath{{images/}}`; `images/` holds only the figures actually referenced.

## Files

- `main.tex` — document shell, title, TOC, 8 `\subfile` includes.
- `macro.tex`, `aai5016.sty` — shared macros + class style.
- `section/` — one `.tex` per unit, mapped to the slide series:
  | Section file | Slide folder |
  |---|---|
  | `Introduction.tex` | — |
  | `Entropy.tex` | `../lectures/01-entropy/` |
  | `Lossless_compression.tex` | `../lectures/02-lossless/` |
  | `Differential_entropy.tex` | `../lectures/03-diffentropy/` |
  | `Lossy_compression.tex` | `../lectures/04-lossy/` |
  | `turboquant.tex` | `../lectures/04-lossy/` (TURBOQUANT) |
  | `Diffusion.tex` | `../lectures/07-diffusion/` |
  | `MI_estimation.tex` | `../lectures/05-mi/` |
- `images/` — referenced figures only (Huffman, prefix codes, classification,
  Markov example, scribe19 lossy diagrams, E8 sphere, etc.).

Non-subfiled drafts from the archive (`lattice.tex`, `application.tex`,
`applications.tex`, `llm_comp.tex`) were intentionally dropped — see `../overleaf/`
to recover them.
