# P1 asset provenance (job 2026-11-22-lec14-finale-refresh)

All source images were retrieved on 2026-11-22. Processing was crop and resize only (sharp, Node), with no erasing, redrawing or recolouring. Keys and relabelled categories are set in the slide HTML, outside the images.

## p1-vend1-shop.png (slide S52)

- Source: Anthropic, "Project Vend: Can Claude run a small shop? (And why does that matter?)", 27 Jun 2025, https://www.anthropic.com/research/project-vend-1. Photo of the office shop (fridge, baskets, self-checkout tablet) in the setup section.
- File: https://assets.claude.com/a2fb5f5f8027a143fd39480d4bf6c91f942e1489.jpg (requested at `?w=3840`; 3225×4000 JPEG).
- Processing: not cropped. Resized to width 480 (480×596).

## p1-vend2-networth.png (slide S53)

- Source: Anthropic, "Project Vend: Phase two", 18 Dec 2025, https://www.anthropic.com/research/project-vend-2. Net-worth-over-time figure (the source gives it no figure number).
- File: https://assets.claude.com/6a40fb63a2e17a97b0a100e8e3bcdcd5433b2ec6.png (3840×2160).
- Crop box (source pixels): left 68, top 358, width 3704, height 1733. Then resized to width 1200 (1200×561).
- Removed: the embedded title "Net worth over time" and the outer margin. Kept: axes, axis titles, tick labels, the dashed change markers with their labels, and the curve.

## p1-metr-forecast-vs-observed.png (slide S54a)

- Source: METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", 10 Jul 2025, https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/. Forecast-versus-observed chart; it is also Fig. 1 of Becker, Rush, Barnes, Rein, arXiv 2507.09089. Licence: CC-BY (stated on the image footer "metr.org | CC-BY").
- File: https://metr.org/assets/images/downlift/forecasted-vs-observed.png (2562×1540).
- Crop box (source pixels): left 0, top 310, width 2562, height 1110 (rows 310–1419). Then resized to width 1200 (1200×520).
- Removed: the title and subtitle block, the METR logo, the bottom category labels, and the footer "metr.org | CC-BY". Kept: all five groups, the y axis with tick labels and axis title, the speedup and slowdown arrows, and the error bars.
- Known clip: the bottom 3 source rows of the "+40%" tick label (rows 1420–1422) fall outside the crop.
- The five category labels (economics experts, ML experts, developers before, developers after, measured) are re-set in HTML below the image. Their column centres are at 23.2%, 39.4%, 55.6%, 71.8% and 89.3% of the image width, measured on the source.

## p1-gen-curves.py (slides S06 and S09)

- Command: `python3 p1-gen-curves.py` (standard library only). It prints the SVG path data used inline on the slides.
- S06: the exact values 0.95^n for n = 0..20, endpoint 0.95^20 ≈ 0.3585. Plot mapping X = 80 + 25.5n, Y = 340 − 300p. On the slide the y coordinates are then compressed to 40 + (Y − 40) × 0.85 so the chart fits.
- S09: a schematic logistic p = 1/(1 + exp((x − 575)/70)) for x = 110..1040, step 10, with Y = 270 − 230p. It is not fitted to any data.
