# work-r2 — 2026-11-10-lec12-visual-motivation

- Branch: `2026-11-10-lec12-visual-motivation`; previous head `6d1e21c` (work-r1).
- Head commit: named in the pointer message (the commit that adds this file).
- Scope: F01–F07 and the optional F08, plus their direct consequences. Nothing else changed.
- Result: main 74 → 76 slides, note 74 → 76 articles (same ID order), tech 23 slides. Still 90 min.

## Findings

- **F01, OUTLINE duplication. Fixed.**
  - Rebuilt `courses/trustworthy-ai/OUTLINE.md` from baseline `cd0da5c`.
  - lec09/10/11 now appear once each, matching baseline. There is one lec12 section; the index row, tech row and figure-index line are updated.
  - Pointers and counts are recomputed for the 76-slide deck: sections 1–11 / 12–28 / 29–43 / 44–61 / 62–71 / 72–76.
  - `outline-lint`: 0 stale pointers. Its 5 warnings are pre-existing and belong to infotheory and privacy.
- **F02, shrunk plot keys. Fixed at native size.**
  - Removed `.p4-key p` (1.25rem plus line-height and margin overrides) and `.p4-key p.p4-axis`. Every key line is now native `p`.
  - S41a/S41b:
    - axis reading moved to one line above the figure;
    - images 385px tall;
    - key entry is "reduction, 95% band";
    - cite defines "reduction = exponentiated gradient".
  - S42: axis key on one line.
  - S43a:
    - axis key split into two lines;
    - muted caveat moved below the row;
    - image 390px.
  - **New S76** (before S44a), a dedicated figure-key step.
    - Shows all nine AIF360 methods, grouped by stage: pre-processing 4, in-processing 2, post-processing 3.
    - Dark dot = LR, light dot = RF.
    - Colours redrawn from the Fig. 5 legend.
    - Stages come from AIF360 Table 2 (paper PDF p.8).
  - S44a/S44b staged keys. Each highlights the methods its reading discusses:
    - S44a: disparate impact remover; adversarial debiasing.
    - S44b: reweighing; reject option; adversarial debiasing.
    - Each slide ends with a muted pointer to the full key on S76.
    - Plots are unchanged: no data erased, no repainting.
    - S44a's "These two run on differently processed data" comes from the paper's p.8 text.
    - S44a's "Seven other methods overlap" is a reading of the plotted figure, not a number taken from the paper text.
  - No slide exceeds 7 lines.
- **F03, cut labels. Fixed.**
  - Hardt Fig. 1 re-cropped from the original PDF (p.7, 300 dpi). Both crops keep the full panel title and the top 1.0 tick:
    - `p2-hardt-fig1-eqodds.png`: `-x 905 -y 300 -W 570 -H 645`;
    - `p2-hardt-fig1-eqopp.png`: `-x 1530 -y 300 -W 640 -H 645`.
  - S17a/b:
    - images 460px tall;
    - cites now say "cropped with its panel title; key set beside the image" (S17a also notes the legend is removed).
  - S39 split into S39a (SPD) and S39b (DI).
    - New assets are the paper's own raster panels, extracted unmodified with `pdfimages -png -f 9 -l 9` from Bellamy et al. 2018:
      - `p4-aif360-fig4a-spd.png` (Fig. 4a);
      - `p4-aif360-fig4c-di.png` (Fig. 4c).
    - Each slide carries:
      - a one-line definition;
      - the image at 390px;
      - a key with rows (dataset · attribute), before/after colours, ±1 SD and the ideal value;
      - the caveat "Training data, not a trained model."
    - Cite: "Full panel image, unmodified; its top and right edges are cut in the source." The source raster itself is clipped, so no crop of mine causes that cut.
    - The shared `figs/reweighing-aif360.png` is untouched; lec12 no longer uses it.
- **F04, Bianchi archetypes. Fixed as specified.**
  - S51b box: "Separate nearest matches: gender (2); race (3)".
  - The note explains:
    - CLIP cosine comparison against Chicago Face Dataset archetypes;
    - gender and race matched separately;
    - there are no six combined archetypes.
  - 99% / 56% and the self-identification caveat are kept.
- **F05, S54a. Fixed as specified.**
  - Box: "Black patients / need understated by cost"; aria-label updated to match.
  - The note keeps "at a given score, Black patients were sicker".
- **F06, S54b and note. Fixed as specified.**
  - Box: "Fairness on cost is not fairness on need."
  - The note carries both sentences from the finding verbatim.
  - The old "jails someone" sentence and a duplicate closing sentence are removed.
- **F07, tech S61b. Fixed as specified.**
  - The equality is restricted to (s, a) with Pr[S = s, A = a] > 0, and the slide adds "Discrete score values here."
  - The equation is set on two aligned lines; on one line it ran past the right edge.
- **F08, tech S60 (optional). Taken.**
  - Underbraces removed.
  - Added a native-size line: "Denominators, in order: group · positives · negatives · selected."
- Nonblocking items: left as accepted. That covers S17b blank space, the BBQ borders and the inline source colours (still the only lint warning).

## Slide mapping (main pages, r1 → r2)

| r1 page | r2 page | ID |
|---|---|---|
| 1–47 | 1–47 | unchanged |
| 48 | 48, 49 | S39 → S39a, S39b |
| 49–56 | 50–57 | S40a … S43b |
| — | 58 | new S76 (method key) |
| 57–74 | 59–76 | S44a … S56 |

- Note: two articles added (S39a/S39b replace S39; new S76).
  - Headings renumbered 1–76; pacing recomputed, total 90.
  - Mitigation keeps its 20 min: S39a/b 0.75 each, S76 0.5, S44a/b 1 each.
  - Cross-references updated: slide 63 (Darker-skinned), 56–57 (FICO), 67.
- Tech: no page change.

## Sources used this round

- Bellamy et al. 2018 (AIF360):
  - Fig. 4(a) and 4(c) raster panels (PDF p.9);
  - Table 2 stage assignments and the p.8 text on differently processed data (PDF p.8);
  - Fig. 5 legend colours.
- Hardt, Price, Srebro 2016: Fig. 1 re-cropped from the saved PDF (p.7).
- No new facts beyond these. None corrected from memory.

## Checks

- `lint-deck.py`:
  - main: one warning, hardcoded inline colours (accepted in review-r1);
  - note and tech: ok.
- `outline-lint.py`: 0 stale or missing pointers.
- Rendered at `-r 60` and viewed:
  - main pp21, 22, 48, 49, 53, 54, 55, 56, 57, 58, 59, 60, 70, 73, 74;
  - tech pp4, 6.
- Fixed after render:
  - S39a title wrap;
  - S39b caveat touching the cite;
  - S17b panel title clipped on the right (crop widened);
  - S76 wrapped key-entry alignment;
  - S61b equation overflow.
- Final renders show no overflow, overlap, clipped labels or detached arrows on these pages.
