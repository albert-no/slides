# P2 asset provenance (job 2026-11-22-lec14-finale-refresh)

## p2-weij-fig4-claude3.png

- Used on: `lec14-agentic-threats.html`, slide S21 ("Instructions Can Lower Test Scores Selectively").
- Source: van der Weij, Hofstätter, Jaffe, Brown, Ward, "AI Sandbagging: Language Models can Strategically Underperform on Evaluations", ICLR 2025, arXiv 2406.07358v4, Figure 4.
- Source URL: https://arxiv.org/html/2406.07358v4/figures/wmdp_sandbagging_prompting_results_cropped.png
  (1474 × 388 px; same raster as the one embedded in the v4 PDF, page 6, so this is the highest resolution available).
- Retrieved: 2026-11-22.
- Crop box (source pixels): x 748–1474, y 0–388 → output 726 × 388 px. No rescaling, no recolouring, no redrawing.
- What was cropped out: the left (GPT-4) panel, and with it the shared y-axis label "Accuracy" (which sits in the left panel). The right panel title "Claude 3", its bars, value labels, legend, random-baseline line and the Control / Target grouping are unchanged.
- Key on the slide is ours (model name, what "sandbagging" means here, WMDP vs controls, y = accuracy with refusals excluded).
- Method: headless Chromium screenshot of a 726 × 388 clipping div holding the source image offset by −748 px (`--force-device-scale-factor=1`).
