# P4 asset provenance (job 2026-11-22-lec14-finale-refresh)

Retrieved 2026-11-22.

## p4-gewang-fig1-ab.png (S43)

- Source: Ge-Wang, Crosse et al., "Attack Selection in Agentic AI Control Evaluations Meaningfully Decreases Safety", arXiv 2606.06529v1 (preprint, Jun 2026). PDF: https://arxiv.org/pdf/2606.06529v1
- Figure: Fig. 1, panels A (start policy) and B (stop policy), PDF page 2.
- Command: `pdftoppm -r 300 -f 2 -l 2 -x 330 -y 280 -W 1215 -H 838 -png 2606.06529v1.pdf p4-gewang-fig1-ab`
- Crop box (300 dpi pixels): x 330, y 280, width 1215, height 838. Output 1215 x 838 px.
- Cropped out: panel C ("Effect on measured safety", schematic curve), the figure caption, and the surrounding page text. No other modification; the role key on the slide is HTML outside the image.

## p4-gen-s40-bars.py → inline SVG on S40

- Source: Greenblatt, Shlegeris, Sachan & Roger, "AI Control: Improving Safety Despite Intentional Subversion", ICML 2024, arXiv 2312.06942v5. https://arxiv.org/abs/2312.06942
- Table 2, rows "Upfront auditing" (safety 15%, usefulness 100%) and "Trusted monitoring" (safety 62%, usefulness 97%).
- Command: `python3 -I p4-gen-s40-bars.py` (prints the SVG pasted into S40).
- Transformation: linear scaling only (2.9 viewBox units per percentage point, 0–100%). No uncertainty drawn: Table 2 reports none.
- Needs a matching evidence.md entry (generated chart); slides-review owns that file.

## Existing assets reused unchanged

- `figs/control-setup-fig1.png` (S37): Greenblatt et al. Fig. 1, right panel.
- `figs/control-pareto-fig2-zoom.png` (S42): Greenblatt et al. Fig. 2, zoomed panel.
