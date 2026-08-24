# Deep Learning Math — content outline

Mathematical foundations course for **junior (3rd-year) undergrad AI majors**. Two source
scribe-note files (Albert's LaTeX): `tex/probability25.tex` and `tex/optimization25.tex`.
Pace: slow and complete — every major theorem gets technique review → statement →
proof overview → proof details → proof summary → implication. Motivation slides
(why this math shows up in AI) open every deck. No slide-count cap.

Decks live at `courses/deepmath/<deck>/<deck>.html` (reference path `../../../reference/`).
Shared source images in `figs/`.

**Cross-folder overlap** (this course is the *undergrad math-foundations* treatment —
differentiate, don't duplicate): entropy/KL/MI/Fano have a grad-level treatment in
`courses/infotheory/lectures/01-entropy/`; differential entropy + MaxEnt Gaussian in
`03-diffentropy/`; diffusion/DDPM rigor in `courses/privacy/lectures/02-generative/`
and `courses/infotheory/lectures/07-diffusion/`.

## Deck plan (13 decks — status)

| # | Deck | Source (tex lines) | Status |
|---|---|---|---|
| 1 | `prob01-foundations/` — probability review, entropy, Jensen, H ≤ log M | prob 13–451 (through max-entropy) | done (72 slides) |
| 2 | `prob02-kl-crossentropy/` — mismatch thm, KL ≥ 0, horse racing, CE loss = KL to one-hot | prob 249–538 | planned |
| 3 | `prob03-mutual-information/` — joint/cond entropy, MI, DPI I–III, cond MI, differential entropy, MaxEnt Gaussian | prob 539–1210 | planned |
| 4 | `prob04-random-processes/` — Markov processes, stationary dist., discrete diffusion | prob 1211–1455 | planned |
| 5 | `prob05-concentration/` — Markov/Chebyshev/Chernoff, MGF, CLT sketch, LLN | prob 1457–1595 | planned |
| 6 | `prob06-generalization/` — Hoeffding, sub-Gaussian, union bound, finite-class generalization bound | new material (sequel to prob05) | planned |
| 7 | `prob07-estimation/` — cond. expectation/tower, MLE/MAP, Fano (full proof), Naive Bayes, bias-variance, MMSE | prob 1563–1911 | planned |
| 8 | `prob08-gaussian/` — MVN (3 defs, properties w/ proofs), Gaussian channel, Gaussian diffusion/DDPM, Gaussian discriminant | prob 1912–2519 (MIT OCW 6.436J citation) | planned |
| 9 | `prob09-monte-carlo/` — Monte Carlo, importance sampling, variance trade-offs, policy gradient / RLHF hooks | new material | planned |
| 10 | `opt01-svd-lowrank/` — rank/range/null, SVD, pseudo-inverse, spectral & nuclear norms, Eckart–Young–Mirsky, Netflix | opt 1–435 | planned |
| 11 | `opt02-regression-erm/` — least squares θ\*=A†B (full proof), ERM/Bayes risk, ridge + closed form | opt 436–794, 1463–1517 | planned |
| 12 | `opt03-convexity-gd/` — convexity, L-smoothness, co-coercivity, strong convexity, PL, GD O(1/T) + linear rate | opt 795–1319 | planned |
| 13 | `opt04-sgd/` — SGD O(1/√K) proof, mini-batching, strongly-convex SGD O(log k/k) | opt 1320–1462, 1520–1600 | planned |

Dropped from source by request: operator theory (opt 1603–1761), acceleration/AGM
(1765–1889), GDM/RMSprop/Adam (1981–2056), SAM (2060–2091).

## Per-deck outlines

### prob01-foundations — Probability Foundations & Entropy (72 slides)

`prob01-foundations/prob01-foundations.html` · source: prob 13–451.
Lecture 1 — defines everything from scratch; ends on a bridge to prob02 (wrong
distribution → cross-entropy/KL).

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + TOC | 1–2 | prob01-foundations/prob01-foundations.html:26 |
| 01 | Why Probability? (data = samples, models = distributions) | 3–6 | prob01-foundations/prob01-foundations.html:83 |
| 02 | Probability Review (Ω, F, P; coin, 5×5 image, MNIST, CIFAR-10, |Ω| table) | 7–15 | prob01-foundations/prob01-foundations.html:185 |
| 03 | Random Variables (map, pmf, expectation, LOTUS exercise) | 16–23 | prob01-foundations/prob01-foundations.html:320 |
| 04 | Entropy (surprisal prob01-foundations/prob01-foundations.html:512, H def :548, worked examples, h₂(p), guessing game :678, AI examples :793) | 24–45 | prob01-foundations/prob01-foundations.html:478 |
| 05 | Properties (Thm 1–3, Jensen technique review + induction proof, max-entropy proof) | 46–69 | prob01-foundations/prob01-foundations.html:887 |
| — | Recap chain, bridge to prob02, end slide | 70–72 | prob01-foundations/prob01-foundations.html:1251 |

Key theorems: **Thm 1** non-negativity H(X) ≥ 0 (prob01-foundations/prob01-foundations.html:899);
**Thm 2** Jensen E[f(X)] ≤ f(E[X]) for concave f, proved by induction on support size
(prob01-foundations/prob01-foundations.html:1002); **Thm 3** maximum entropy
H(X) ≤ log M, equality iff uniform (prob01-foundations/prob01-foundations.html:1122).
Figures: figs/binary_image.png, figs/mnist.png, figs/cifar10.jpeg, figs/jensen.png;
all other diagrams inline SVG. Jensen proof (induction) is not in the tex (source
states Jensen without proof) — added per full-treatment mandate.
