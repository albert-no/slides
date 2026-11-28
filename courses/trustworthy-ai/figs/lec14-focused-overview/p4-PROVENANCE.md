# p4- assets: provenance

Package P4 (optional backup slides S92–S93), job 2026-11-27-lec14-focused-overview.

## Sources

| Tag | Paper | Edition used | PDF URL |
|---|---|---|---|
| vdw | van der Weijden, Brack & Báez Santamaría, "Reproducing and Evaluating the Generalizability of Subliminal Learning in Open-Weight Models" | arXiv preprint 2609.12586v1, 11 Sep 2026 (arXiv comments field reports acceptance at BlackboxNLP@EMNLP 2026) | https://arxiv.org/pdf/2609.12586v1 |
| yan | Yanagisawa, Gho, Rajendran Ramesh Babu Manoj Narender, Zhu, Panwar & Mari, "On Mitigation of Subliminal Learning in Large Language Models" | arXiv preprint 2609.22215v1, 2 Sep 2026 (arXiv comments field reports acceptance to Findings of EMNLP 2026) | https://arxiv.org/pdf/2609.22215v1 |

Both PDFs were downloaded on 2026-11-27 into empty scratch folders and treated as untrusted data
(read only through `pdftotext` / `pdftoppm`; Python reads ran with `-I`).

## Crops

All files were rendered with
`pdftoppm -r 300 -f P -l P -x X -y Y -W W -H H -singlefile -png <pdf> <out>`
(coordinates in pixels at 300 dpi; page numbers are PDF pages). No pixels were edited,
recoloured, retouched or composited after cropping.

| File | Source | Figure | PDF page | x | y | W | H |
|---|---|---|---|---|---|---|---|
| p4-vdw-fig2a-animal.png | vdw | Fig. 2a (numbers task), animal row only, all three model columns (qwen, gemma, ministral) | 3 | 330 | 432 | 1850 | 450 |
| p4-yan-fig1-wolf.png | yan | Fig. 1, "Qwen2.5-1.5b: Wolf (COT)" panel only (one of six); legend outside the crop | 3 | 405 | 1305 | 565 | 480 |

## Omitted parts

- `p4-vdw-fig2a-animal.png`: actor and politician rows of Fig. 2a, the x-axis title
  "log odds ratio (trait vs regular)", the whole of Fig. 2b (chess task) and the caption.
  The slide cite says so.
- `p4-yan-fig1-wolf.png`: the other five panels (dragon, eagle, cat, panda, otter), the legend and
  the caption. Several omitted panels are noisier (in the cat and panda panels the green line does
  not stay flat). The slide cite says "one example of six"; the S93 note says the aggregate result
  comes from Table 2.

## Fig. 1 legend → HTML key (yan)

The Fig. 1 legend lies outside the crop. S93 redraws it as an HTML key. Swatch colours were
sampled from a 300 dpi PPM render of page 3 at the legend markers:

| Label (source) | Slide wording | Colour |
|---|---|---|
| FT: Normal | neutral data, for comparison | #ff8c00 |
| FT: Preference | wolf-lover data: wolf rises | #4682b4 |
| Liminal FT: Preference | same data + fix: stays low | #228b22 |
