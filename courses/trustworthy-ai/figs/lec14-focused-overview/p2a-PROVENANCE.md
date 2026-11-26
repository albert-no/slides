# p2a- assets: provenance

Package P2a (block "Learning hidden behaviors", S60–S72b), job 2026-11-27-lec14-focused-overview.

## Sources

| Tag | Paper | Edition used | PDF URL |
|---|---|---|---|
| cloud | Cloud et al., "Language models transmit behavioural traits through hidden signals in data", Nature 652, 615–621 | Final Nature edition, issue dated 16 April 2026 (page header "Vol 652 \| 16 April 2026"), doi 10.1038/s41586-026-10319-8 | https://www.nature.com/articles/s41586-026-10319-8.pdf |
| betley | Betley et al., "Training large language models on narrow tasks can lead to broad misalignment", Nature 649, 584–589 | Final Nature edition, PDF header 15 January 2026, doi 10.1038/s41586-025-09937-5 | https://www.nature.com/articles/s41586-025-09937-5.pdf |

Both PDFs were downloaded on 2026-11-27 into empty scratch folders and treated as untrusted data
(read only through `pdftotext` / `pdftoppm`; Python reads ran with `-I`).

## Crops

All files were rendered with
`pdftoppm -r 300 -f P -l P -x X -y Y -W W -H H -singlefile -png <pdf> <out>`
(coordinates in pixels at 300 dpi; page numbers are PDF pages). No pixels were edited,
recoloured, retouched or composited after cropping.

| File | Source | Figure | PDF page | x | y | W | H |
|---|---|---|---|---|---|---|---|
| p2a-cloud-fig2-roles.png | cloud | Fig. 2, right part (unrelated prompts, sample, filter, fine-tune, student) | 2 | 869 | 2496 | 1156 | 414 |
| p2a-cloud-fig2-filter.png | cloud | Fig. 2, teacher-sample-filter part | 2 | 869 | 2496 | 856 | 414 |
| p2a-cloud-fig2-learner.png | cloud | Fig. 2, reference model fine-tuned into student | 2 | 1518 | 2496 | 507 | 414 |
| p2a-cloud-fig2-teacher.png | cloud | Fig. 2, left part (trait given to reference model, giving the teacher) | 2 | 474 | 2496 | 538 | 414 |
| p2a-cloud-fig1-teacher.png | cloud | Fig. 1, teacher with owl bias and generated numbers | 2 | 145 | 194 | 785 | 196 |
| p2a-cloud-fig3a.png | cloud | Fig. 3a (misalignment and TruthfulQA bars) | 3 | 465 | 192 | 801 | 474 |
| p2a-cloud-fig4a.png | cloud | Fig. 4a (animal preference bars), legend excluded | 4 | 480 | 312 | 765 | 522 |
| p2a-cloud-fig5a.png | cloud | Fig. 5a (cross-model heat map) | 5 | 480 | 192 | 756 | 642 |
| p2a-betley-fig1-train.png | betley | Fig. 1, training example (left column only) | 2 | 366 | 195 | 951 | 264 |

## Accepted edge fragments

Neighbouring parts of the source figures that a rectangular crop could not exclude without
cutting labels:

- `p2a-cloud-fig2-roles.png`, `p2a-cloud-fig2-filter.png`: a thin blue sliver of the trait box
  and the letter "e" at the left edge.
- `p2a-cloud-fig2-teacher.png`: the fragment "Unrel" and part of a box outline at the top right
  (the next label in Fig. 2). The S69a note mentions it.

## Fig. 4a legend → HTML key

The Fig. 4a legend lies outside the crop. S68 redraws it as an HTML key with the source's exact
labels. Swatch colours were sampled from a 300 dpi PPM render of page 4 at the legend markers:

| Label (source) | Colour |
|---|---|
| GPT-4.1 nano | #d3d3d3 |
| FT: regular numbers | #808080 |
| FT: animal numbers | #1f77b4 |
| FT: other animals | #add8e6 |

The S67a diagram uses the same four colours.

## Own diagrams

S61b, S62a, S62b, S63b, S64, S67a, S67b, S69b, S71 and S72b use inline SVG drawn by hand in the
slide markup. There is no generator file. Each is labelled "Illustrative" on the slide. The
example answers in S67b are invented and labelled as examples. S63b paraphrases the source's
Fig. 1 outcome panel and shortens its questions.

## Display masking (integrator, 2026-11-27)

The PNG files are unchanged. Three slides hide crop leftovers with a CSS `clip-path` polygon on the `<img>`; no source content inside the panel is hidden:
- `p2a-cloud-fig2-roles.png` (S61a) and `p2a-cloud-fig2-filter.png` (S66a): the pale box fragment and stray glyph at the left edge.
- `p2a-cloud-fig2-teacher.png` (S69a): the fragment of the next label at the top right. The S69a cite now says "fragment of the next label masked".
