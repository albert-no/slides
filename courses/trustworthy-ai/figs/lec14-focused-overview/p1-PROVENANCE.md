# P1 asset provenance (job 2026-11-27-lec14-focused-overview)

## p1-vend1-architecture.png (slide S57b)

- Source: Anthropic, "Project Vend: Can Claude run a small shop? (And why does that matter?)", 27 Jun 2025, https://www.anthropic.com/research/project-vend-1. Figure 2 (the text says "see Figure 2 for a depiction of the setup"; on-page caption "Basic architecture of the demonstration."), setup section, directly after the tool list.
- File: https://assets.claude.com/8565f8d42b64173f35ac33c14e4e6c6e7bb7693b.png (4096×2304 PNG, retrieved 2026-11-27, sha256 77d4e142c79c9056ce48f7119ef5cf26a330fcd5235a21905de8b882376c254a).
- Processing (crop + uniform downscale only; no erasing, redrawing or recolouring):
  1. `mutool convert -o fig2.pdf fig2.png` (wraps the PNG as one 4096×2304 pt page, 1 px = 1 pt).
  2. `pdftoppm -r 24 -x 77 -y 140 -W 1223 -H 587 -png -singlefile fig2.pdf crop` (scale 1/3; crop box in source pixels ≈ left 231, top 420, width 3669, height 1761).
  3. Copied unchanged to `p1-vend1-architecture.png` (1223×587).
- Removed: the embedded title "Basic Architecture of Project Vend" and the outer beige margin. Kept: all five nodes (Anthropic employees, Claudius, Wholesalers, Andon Labs, Physical vending machine), every arrow and every arrow label.
- The role key on the slide (agent / people doing physical work / customers) is set in HTML beside the image, not drawn on it.

## Reused read-only (no change)

- `../lec14-finale-refresh/p1-vend1-shop.png` (S57a) and `../lec14-finale-refresh/p1-vend2-networth.png` (S53a); provenance in `../lec14-finale-refresh/p1-PROVENANCE.md`.

## Own diagrams

S05a, S05b, S52a, S52b, S53b, S58a, S58b, S13, S59 are inline SVG teaching diagrams written by hand in the slide HTML, each labelled "Illustrative" (or "Schematic") on the slide. They contain no numbers. S52b's two bars have no axis, no values and no scale: they show only the qualitative relationship "sale price below purchase cost" reported in the phase-one post ("Selling at a loss"). No generator script.
