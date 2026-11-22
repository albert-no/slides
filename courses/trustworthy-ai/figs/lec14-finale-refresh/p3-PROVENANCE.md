# P3 asset provenance (lec14 finale refresh, job 2026-11-22-lec14-finale-refresh)

All assets are crop-only renders of the arXiv PDFs (no redrawing, recolouring or relabelling),
made with poppler `pdftoppm ... -png -singlefile`. Retrieved 2026-11-22.

| Asset | Source | Figure / page | Command (crop box in pixels at the given DPI) | What was cropped |
|---|---|---|---|---|
| p3-hammond-fig1.png (888×558) | https://arxiv.org/pdf/2502.14143v1 — Hammond et al., "Multi-Agent Risks from Advanced AI" | Fig. 1, PDF page 10 | `pdftoppm -r 300 -f 10 -l 10 -x 795 -y 918 -W 888 -H 558 -png -singlefile` | Decision tree only; caption and body text excluded |
| p3-mast-fig1.png (1195×615) | https://arxiv.org/pdf/2503.13657v3 — Cemri et al., "Why Do Multi-Agent LLM Systems Fail?" | Fig. 1, PDF page 2 | `pdftoppm -r 215 -f 2 -l 2 -x 318 -y 206 -W 1195 -H 615 -png -singlefile` | Whole figure (stage header, categories, 14 modes, shares); caption excluded. The slide adds an external enlarged category key, not drawn on the image |
| p3-prompt-infection-fig6a.png (801×471) | https://arxiv.org/pdf/2410.07283v1 — Lee & Tiwari, "Prompt Infection" | Fig. 6(a), PDF page 8 | `pdftoppm -r 300 -f 8 -l 8 -x 444 -y 339 -W 801 -H 471 -png -singlefile` | Panel (a) plot; subcaption excluded |
| p3-prompt-infection-fig6b.png (801×471) | same | Fig. 6(b), PDF page 8 | `pdftoppm -r 300 -f 8 -l 8 -x 1302 -y 339 -W 801 -H 471 -png -singlefile` | Panel (b) plot; subcaption excluded |

Diagrams drawn as inline SVG in the deck (not assets): S28 chess-verification example (after Cemri et al. §4, FM-3.2),
S29 forwarding schematic (after Lee & Tiwari Fig. 2; no attack text), S33 channel diagram (after Motwani et al. §3, Fig. 1; no scheme).
All three are labelled illustrative in their cites.
