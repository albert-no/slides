# Deep Learning Math — content outline

Mathematical foundations course for **junior (3rd-year) undergrad AI majors**. Two source
scribe-note files (Albert's LaTeX): `tex/probability25.tex` and `tex/optimization25.tex`.
Pace: slow and complete — every major theorem gets technique review → statement →
proof overview → proof details → proof summary → implication. Motivation slides
(why this math shows up in AI) open every deck. No slide-count cap.

Decks live at `courses/deepmath/<deck>/<deck>.html` (reference path `../../../reference/`).
Shared source images in `figs/`.
Past homework and exams (2024–25, PDFs as handed out) in `exam/`: `hw1sol`–`hw4sol`,
`midterm24_sol`, `midterm25_prob`, `midterm25_sol`, `final24sol`, `final25sol`; 2026 midterm
source `midterm26.tex` (exam 2026-10-20), reviewed in `midterm26-review/` (below).

**Accessible editions.** Every deck's speaker note also ships as a screen-reader Markdown
edition at `<deck>/<deck>-note.md`; the midterm26 review, the prob06 backup full edition and the four
optimization decks in `opt03-backup/` have one too (17 files, ~19.4k lines total). These are written for a
blind student who reads through a Markdown-to-braille/speech converter, so they follow a
fixed contract: plain ASCII only (no smart quotes, em dashes, Unicode math or diacritics),
all math in LaTeX (`$…$` inline, `$$…$$` display with `\tag{}` for numbered equations),
every figure replaced by a verbal description, every table linearised into bullets with an
explicit legend, and no reference to the slides or the visual layout — each file stands
alone. Section numbering matches the HTML note it derives from. When a note changes, its
`.md` edition must change in the same edit.

**Cross-folder overlap** (this course is the *undergrad math-foundations* treatment —
differentiate, don't duplicate): entropy/KL/MI/Fano have a grad-level treatment in
`courses/infotheory/lectures/01-entropy/`; differential entropy + MaxEnt Gaussian in
`03-diffentropy/`; diffusion/DDPM rigor in `courses/privacy/lectures/02-generative/`
and `courses/infotheory/lectures/07-diffusion/`.

## Deck plan (11 active decks + optimization backup collection — status)

| # | Deck | Source (tex lines) | Status |
|---|---|---|---|
| 1 | `prob01-foundations/` — probability review, entropy, Jensen, H ≤ log M | prob 13–451 (through max-entropy) | done (72 slides) |
| 2 | `prob02-kl-crossentropy/` — mismatch thm, KL ≥ 0, f-divergences, betting/doubling rate/perplexity, proper scoring rules, CE loss = KL, population risk & Bayes classifier, forward vs reverse KL | prob 249–538 + DL extensions | done (86 slides, 2026-09 revisions) |
| 3 | `prob03-mutual-information/` — joint/cond entropy, MI, DPI I–III, cond MI, differential entropy, MaxEnt Gaussian | prob 539–1210 | done (128 slides, 2026-09 revision) |
| 4 | `prob04-random-processes/` — Markov processes, stationary dist., discrete diffusion | prob 1211–1455 | done (99 slides) |
| 5 | `prob05-concentration/` — Markov/Chebyshev/Chernoff, MGF, CLT sketch, LLN | prob 1457–1595 | done (106 slides) |
| 6 | `prob06-generalization/` — Hoeffding, sub-Gaussian, union bound, finite-class generalization bound | new material (sequel to prob05) | done (51 slides, senior-undergrad default; full / advanced 105 in backup/) |
| 7 | `prob07-estimation/` — cond. expectation/tower, MLE/MAP, Fano (full proof), Naive Bayes, bias-variance, MMSE, generative models as MLE? (LLMs, DDPM) | prob 1563–1911 | done (130 slides) |
| 8 | `prob08-gaussian/` — MVN (3 defs, properties w/ proofs), Gaussian channel, Gaussian diffusion/DDPM, Gaussian discriminant | prob 1912–2519 (MIT OCW 6.436J citation) | done (154 slides) |
| 9 | `prob09-monte-carlo/` — Monte Carlo, importance sampling, variance trade-offs, RL sample reuse | new material | done (70 slides) |
| 10 | `opt01-svd-lowrank/` — rank/nullity, vector/spectral/Frobenius norms, SVD and Eckart–Young–Mirsky | opt 1–435 | done — **68 slides, 150 min** (restructured 2026-11-23); full / extended 119 in `opt03-backup/` |
| 11 | `opt02-convexity-gd/` — fixed-step GD, smoothness/descent, nonconvex stationarity, convex function-gap and strongly convex geometric rates | opt 795–1319 | done — **51 slides, 90 min** (restructured 2026-11-23; folder renamed from `opt03-convexity-gd/` 2026-11-24); full / extended 134 in `opt03-backup/` |

Optimization backup collection (not one of the 11, not taught in 2026): `opt03-backup/` — the full
opt01 (119 slides) and opt03 (134) editions, the old opt02 regression/ERM/ridge deck (110; opt 436–794,
1463–1517) and the old opt04 SGD deck (117; opt 1320–1462, 1520–1600), each with HTML note and
Markdown edition; index in `opt03-backup/OUTLINE.md`. Their filenames keep the historical lecture
numbers 10–13.

Exam-review deck (not one of the 11): `midterm26-review/` — midterm 2026 solutions lecture (74 slides).

Dropped from source by request: operator theory (opt 1603–1761), acceleration/AGM
(1765–1889), GDM/RMSprop/Adam (1981–2056), SAM (2060–2091).

## Per-deck outlines

### prob01-foundations — Probability Foundations & Entropy (72 slides)

`prob01-foundations/prob01-foundations.html` · source: prob 13–451.
Lecture 1 — defines everything from scratch; ends on a bridge to prob02 (wrong
distribution → cross-entropy/KL).
Companion: `prob01-foundations/prob01-foundations-note.html` — detailed definitions, expanded proofs, lemmas, references.
Accessible edition: `prob01-foundations/prob01-foundations-note.md` — screen-reader Markdown edition of that note (803 lines): plain ASCII, LaTeX math, figures replaced by verbal descriptions, self-contained (no references to the slides).

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + TOC | 1–2 | prob01-foundations/prob01-foundations.html:43 |
| 01 | Why Probability? (collecting data = sampling xᵢ ~ P :103, models learn distributions :148) | 3–5 | prob01-foundations/prob01-foundations.html:103 |
| 02 | Probability Review (Ω, F, P; coin, 5×5 image, MNIST, CIFAR-10, |Ω| table) | 6–14 | prob01-foundations/prob01-foundations.html:190 |
| 03 | Random Variables (map, pmf, expectation, LOTUS exercise) | 15–22 | prob01-foundations/prob01-foundations.html:325 |
| 04 | Entropy (surprisal :513, H def :552, worked examples, h₂(p), guessing game :682, twenty-questions tree :728, two dice :795, AI examples :834, explore-vs-exploit bandit :901, explorativeness :939) | 23–45 | prob01-foundations/prob01-foundations.html:483 |
| 05 | Properties (Thm 1–3, Jensen technique review + induction proof, max-entropy proof, entropy scale :1283) | 46–69 | prob01-foundations/prob01-foundations.html:967 |
| — | Recap chain, bridge to prob02, end slide | 70–72 | prob01-foundations/prob01-foundations.html:1357 |

Key theorems: **Thm 1** non-negativity H(X) ≥ 0 (prob01-foundations/prob01-foundations.html:975);
**Thm 2** Jensen E[f(X)] ≤ f(E[X]) for concave f, proved by induction on support size
(statement prob01-foundations/prob01-foundations.html:1078); **Thm 3** maximum entropy
H(X) ≤ log M, equality iff uniform (prob01-foundations/prob01-foundations.html:1198).
Figures: figs/binary_image.png, figs/mnist.png, figs/cifar10.jpeg, figs/jensen.png,
figs/mnist-three.png (the real MNIST "3" cropped out of figs/mnist.png, reused on the
models-learn-distributions slide so the pmf peaks at label 3); all other diagrams inline SVG. Slides 4, 5,
37 (question tree), 41, 43 (bandit), 54 (Jensen points) and 67 (D₁/D₂ pmfs) carry KaTeX
labels as absolutely-positioned HTML spans over the SVG (deck-local `.p1-fig`/`.fl` CSS in
the deck's own `<style>` block — KaTeX skips SVG `<text>`). Jensen proof (induction) is not
in the tex (source states Jensen without proof) — added per full-treatment mandate.

### prob02-kl-crossentropy — KL Divergence & Cross-Entropy Loss (86 slides)

`prob02-kl-crossentropy/prob02-kl-crossentropy.html` · source: prob 249–538, extended 2026-09 for a
future-DL-scientist audience (rigor raised, DL connections made concrete), then trimmed per
review (2026-09-06: additivity/LLN, coding costume, Shannon guessing game and the DL zoo removed;
perplexity moved into the CE section; 2026-09-08: log-sum lemma / KL convexity, MLE identity,
softmax gradient / log-sum-exp / MSE-vs-CE removed; one-play $S$-vs-$B$ slide and a proper
doubling-rate definition $W(q)$ added; horse-race and classifier diagrams relabelled in KaTeX).
Lecture 2 — answers prob01's teaser (wrong distribution Q); recalls entropy/Jensen
from prob01 instead of redefining; ends on a bridge to prob03 (two RVs → mutual
information). Bits by default; "nats" stated wherever torch or e^CE appears.
Companion: `prob02-kl-crossentropy/prob02-kl-crossentropy-note.html` (544 lines, §1–7 + refs [1]–[13]) — full definitions, every deck theorem proved, cited (not proved) locality uniqueness of the log score.
Accessible edition: `prob02-kl-crossentropy/prob02-kl-crossentropy-note.md` — screen-reader Markdown edition of that note (1111 lines): plain ASCII, LaTeX math, figures replaced by verbal descriptions, self-contained (no references to the slides); section numbers match the HTML note.

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + TOC | 1–2 | prob02-kl-crossentropy/prob02-kl-crossentropy.html:38 |
| 01 | Why Cross-Entropy? (PyTorch CE loss, derive-not-accept, route map SVG with three costumes) | 3–6 | prob02-kl-crossentropy/prob02-kl-crossentropy.html:114 |
| 02 | Recall & Teaser (surprisal/entropy + Jensen recall from prob01, E[log 1/Q] ≟ H(X)) | 7–11 | prob02-kl-crossentropy/prob02-kl-crossentropy.html:183 |
| 03 | The Mismatch Theorem (Thm 1 arc: 3-step proof, equality, edge-case exercise, H(P,Q) def :401, gap-axis picture) | 12–24 | prob02-kl-crossentropy/prob02-kl-crossentropy.html:249 |
| 04 | KL Divergence (def :452, conventions :465, support in DL :480, P-vs-Q bars SVG :494, worked D(P‖Q)=0.224 ≠ D(Q‖P)=0.296 :525, Thm 2 :565 + proof :578, Thm 3 CE = H + KL :591, f-divergence def :619, Thm 4 :631, zoo table :644, what KL alone brings :658, preview :672) | 25–41 | prob02-kl-crossentropy/prob02-kl-crossentropy.html:444 |
| 05 | Betting (red/black :692, all-in ruin, E[log S], Thm 5 :768, one play B→S with geometric-mean caveat :780, doubling-rate definition W(q) = 1 − h₂(p) − D, max at q = p :801, growth picture :820, horse race KaTeX-overlay figure :843, Thm 6 :875, 3-horse worked example :901, three-gamblers table :913, betting = modeling :926) | 42–56 | prob02-kl-crossentropy/prob02-kl-crossentropy.html:684 |
| 06 | Cross-Entropy Loss (classifier pipeline KaTeX-overlay figure :968, CE loss def :1011, 3-class worked table :1024, LM costume :1038, perplexity def + why it matters :1072, three candidate losses :1089, proper scoring def :1103, log strictly proper :1116, linear not proper :1131, Brier proper :1145, three-scores table :1160, locality :1174 [uniqueness stated, cited in note §6.5], one-hot pmf :1188, Thm 7 :1201, soft labels :1228, min CE = min KL :1240, population view :1253, Thm 8 :1266, Bayes corollary :1279, calibrated-vs-overconfident table :1293, why log settled :1307) | 57–80 | prob02-kl-crossentropy/prob02-kl-crossentropy.html:940 |
| 07 | KL Across Deep Learning (forward vs reverse support argument, two cards :1328; one-Gaussian-to-two-bumps SVG :1355 [numerical grid experiment, nats]) | 81–83 | prob02-kl-crossentropy/prob02-kl-crossentropy.html:1320 |
| — | Recap chain, bridge to prob03, end slide | 84–86 | prob02-kl-crossentropy/prob02-kl-crossentropy.html:1382 |

Key theorems: **Thm 1** mismatch H(X) ≤ E[log 1/Q(X)], equality iff Q = p_X
(prob02-kl-crossentropy/prob02-kl-crossentropy.html:286); **Thm 2** information
inequality D(P‖Q) ≥ 0 (prob02-kl-crossentropy/prob02-kl-crossentropy.html:565);
**Thm 3** H(P,Q) = H(P) + D(P‖Q) (prob02-kl-crossentropy/prob02-kl-crossentropy.html:591);
**Thm 4** every f-divergence ≥ 0 (prob02-kl-crossentropy/prob02-kl-crossentropy.html:631);
**Thm 5** proportional betting, binary (prob02-kl-crossentropy/prob02-kl-crossentropy.html:768);
**Definition** doubling rate W(q) = E[log S/B] = 1 − h₂(p) − D((p,1−p)‖(q,1−q)), maximized iff q = p
(prob02-kl-crossentropy/prob02-kl-crossentropy.html:801);
**Thm 6** proportional betting, M horses, W = log M − H(p) − D(p‖Q)
(prob02-kl-crossentropy/prob02-kl-crossentropy.html:875); **Thm 7** CE loss =
D(one-hot ‖ f(x)) (prob02-kl-crossentropy/prob02-kl-crossentropy.html:1201);
**Thm 8** population CE = E_X[H(P_Y|X)] + E_X[D(P_Y|X ‖ f(X))], Bayes-optimal corollary
(prob02-kl-crossentropy/prob02-kl-crossentropy.html:1266).
Not covered (removed 2026-09-08 per review): log-sum inequality, convexity of D, MLE = min CE, softmax gradient.
Stated, not proved (no on-slide flag; citation in the note): locality uniqueness of the log score
(Bernardo 1979; Gneiting & Raftery 2007). Lossless compression / Kraft is not covered; additivity and the LLN view were dropped.
Figures: figs/jensen.png (Jensen recall), figs/classification.png (classifier setup);
all other diagrams inline SVG (route map, P-vs-Q bars, growth at rate W, one Gaussian fitted to
two bumps, etc.); horse-race and classifier-pipeline figures are SVG shapes with KaTeX labels
overlaid via the deck-local `.p2-fig`/`.fl` pattern (KaTeX skips SVG `<text>`). Worked numeric
examples (3-outcome KL asymmetry, f-divergence zoo, 3-horse race / three-gamblers,
perplexity for K = 2/10/50000, 3-class CE, three scores × three reports,
soft labels, calibrated-vs-overconfident, Gaussian grid fit)
computed for this deck — not in the tex — per worked-example mandate; all reproduced in the note.
Rigorous p_X(x) = 0 edge case left as a hinted exercise (commented out in the tex too).

### prob03-mutual-information — Mutual Information & Data Processing (128 slides)

`prob03-mutual-information/prob03-mutual-information.html` · source: prob 539–1210.
Lecture 3 — answers prob02's teaser (two RVs); recalls entropy from prob01 and KL
from prob02 instead of redefining; ends on a bridge to prob04 (sequences in time →
Markov processes).
Companion: `prob03-mutual-information/prob03-mutual-information-note.html` — detailed definitions, expanded proofs, lemmas, references.
Accessible edition: `prob03-mutual-information/prob03-mutual-information-note.md` — screen-reader Markdown edition of that note (1285 lines): plain ASCII, LaTeX math, figures replaced by verbal descriptions, self-contained (no references to the slides).

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + TOC | 1–2 | prob03-mutual-information/prob03-mutual-information.html:52 |
| 01 | Why Mutual Information? (layer = channel SVG, questions we can't ask yet, "information only decays" preview, route map) | 3–7 | prob03-mutual-information/prob03-mutual-information.html:128 |
| 02 | Joint Random Variables (joint pmf, running 2×2 table :258, marginals, conditional pmf, independence, random vectors, supervised learning = joint dist.) | 8–18 | prob03-mutual-information/prob03-mutual-information.html:230 |
| 03 | Joint & Conditional Entropy (H(X,Y) :392, Thm 1 additivity arc, guessing game returns :516, H(Y\|X) :609, Thm 2 chain rule, Thm 3 DPI I arc) | 19–45 | prob03-mutual-information/prob03-mutual-information.html:383 |
| 04 | Mutual Information (def :819, Venn diagram SVG :835, I(X;X), independence case, KL form :908, Thm 4 symmetry, Thm 5 I ≥ 0 arc, MI in AI) | 46–61 | prob03-mutual-information/prob03-mutual-information.html:810 |
| 05 | Data Processing (Thm 6 DPI II arc, Markov chains :1104, Thm 7 DPI III, layers only forget, cond. MI :1214, three-circle Venn caution :1244, XOR triple counterexample :1273, chain rule for I) | 62–83 | prob03-mutual-information/prob03-mutual-information.html:1040 |
| 06 | Differential Entropy (densities, change of variables, KL for densities, bins SVG :1509, Thm 8 discretization, h def :1576, exhibits 1–3 (negative h, no label invariance, scaling), Gaussian h, Thm 9–12) | 84–111 | prob03-mutual-information/prob03-mutual-information.html:1383 |
| 07 | Maximum Entropy (discrete recall, bounded-support exercise, variance budget, Thm 13 MaxEnt Gaussian full arc, why Gaussians are everywhere) | 112–124 | prob03-mutual-information/prob03-mutual-information.html:1791 |
| — | Recap chain, DPI-family recap, bridge to prob04, end slide | 125–128 | prob03-mutual-information/prob03-mutual-information.html:1968 |

Key theorems: **Thm 1** additivity H(X,Y) = H(X) + H(Y) under independence
(prob03-mutual-information/prob03-mutual-information.html:440); **Thm 2** chain rule
H(X,Y) = H(X) + H(Y|X) (prob03-mutual-information/prob03-mutual-information.html:666);
**Thm 3** DPI I: H(f(X)) ≤ H(X) (prob03-mutual-information/prob03-mutual-information.html:741);
**Thm 4** symmetry I(X;Y) = I(Y;X) (prob03-mutual-information/prob03-mutual-information.html:937);
**Thm 5** I(X;Y) ≥ 0 (prob03-mutual-information/prob03-mutual-information.html:952);
**Thm 6** DPI II: I(X; f(Y)) ≤ I(X;Y) (prob03-mutual-information/prob03-mutual-information.html:1049);
**Thm 7** DPI III on Markov chain X−Y−Z (prob03-mutual-information/prob03-mutual-information.html:1143);
**Thm 8** discretization H(X^Δ) = h(X) − log Δ (prob03-mutual-information/prob03-mutual-information.html:1550);
**Thm 9** scale invariance I(aX;Y) = I(X;Y) (prob03-mutual-information/prob03-mutual-information.html:1704);
**Thm 10** chain rule for h (prob03-mutual-information/prob03-mutual-information.html:1742);
**Thm 11** independence iff I = 0, continuous (prob03-mutual-information/prob03-mutual-information.html:1757);
**Thm 12** DPI continuous (prob03-mutual-information/prob03-mutual-information.html:1769);
**Thm 13** Gaussian maximizes h under a variance budget
(prob03-mutual-information/prob03-mutual-information.html:1840).
Figures: figs/binary_image.png (supervised-learning slide); all other diagrams inline
SVG (layer-as-channel pipeline, route map, guessing-game question rows, entropy Venn
diagram, three-circle Venn caution, Markov chain boxes, layer chain, bins-under-density,
same-variance density comparison). Math labels on the pipeline/route/guessing-game/Venn/
Markov/layer-chain figures are KaTeX `.fl` overlays in a `.p3-fig` wrapper (deck-local
`<style>`), not SVG `<text>`; the same style block adds `.p3-step` spaced rows (proof
overviews, exercise lists) and the `th .katex` uppercase fix. XOR triple and guessing-game
examples are the tex's own; the running 2×2 joint-pmf table and its per-theorem
worked checks are not in the tex — added per worked-example mandate. Venn diagram
and pipeline SVGs added per visual mandate.

### prob04-random-processes — Random Processes & Markov Chains (99 slides)

`prob04-random-processes/prob04-random-processes.html` · source: prob 1211–1455.
Lecture 4 — answers prob03's teaser (sequences in time); recalls the chain rule of
probability from prob03 instead of redefining; ends on a bridge to prob05 (averages
of many draws → concentration).

Companion: `prob04-random-processes/prob04-random-processes-note.html` — detailed
definitions, expanded proofs, lemmas, references.
Accessible edition: `prob04-random-processes/prob04-random-processes-note.md` — screen-reader Markdown edition of that note (1268 lines): plain ASCII, LaTeX math, figures replaced by verbal descriptions, self-contained (no references to the slides).

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + TOC | 1–2 | prob04-random-processes/prob04-random-processes.html:51 |
| 01 | Why Sequences? (LM / diffusion / random-walk cards, one snapshot not enough, settling preview, route map) | 3–7 | prob04-random-processes/prob04-random-processes.html:143 |
| 02 | Random Processes (def, i.i.d. process, coin flips, "my na_e is Albert" text example, modeling spectrum) | 8–13 | prob04-random-processes/prob04-random-processes.html:234 |
| 03 | Markov Processes (memory-one idea, random walk example :353, 1st-order def :392, chain-rule recall (prob03) :408, factorization proposition + proof :424, kth-order def :467, next-token models, refined spectrum) | 14–26 | prob04-random-processes/prob04-random-processes.html:319 |
| 04 | Transition Matrices (prob-vector + matrix×vector reviews, P def :580, column sums, π_i def :609, Thm 1 arc, binary chain :679, three-state chain :751) | 27–43 | prob04-random-processes/prob04-random-processes.html:531 |
| 05 | Evolution in Time (Thm 2 π_t = P^t π_0 + proof, numeric evolution table :842, convergence chart :859, "distribution that does not move?" teaser) | 44–49 | prob04-random-processes/prob04-random-processes.html:807 |
| 06 | Stationary Processes (def :908, sliding-window picture, random-walk counterexample + fan-out, Markov vs. stationary axes, full spectrum) | 50–56 | prob04-random-processes/prob04-random-processes.html:900 |
| 07 | Stationary Distributions (three-state worked stationary example :1059, pinned start fails :1142, Thm 3 existence :1158, assumptions in pictures, binary worked, π* def :1229, eigen reviews :1244, eigen computations by hand :1287, symmetric-P exercise + solution :1353, random surfer) | 57–77 | prob04-random-processes/prob04-random-processes.html:1051 |
| 08 | Limiting Distributions (π_∞ def :1433, α=1 no-limit caveat, Thm 4 arc, rate via second eigenvalue :1503) | 78–86 | prob04-random-processes/prob04-random-processes.html:1425 |
| 09 | Discrete Diffusion (destroy-then-rebuild, ε-noising matrix :1567, sanity checks, uniform limit, data-dissolves picture :1606, denoiser f_θ, backwards generation, why it works) | 87–95 | prob04-random-processes/prob04-random-processes.html:1544 |
| — | Recap chain, running-examples recap, bridge to prob05, end slide | 96–99 | prob04-random-processes/prob04-random-processes.html:1664 |

Key theorems: **Prop.** Markov factorization P(x^n) = Π P(x_i|x_{i−1}) with proof
(prob04-random-processes/prob04-random-processes.html:424); **Thm 1** one-step
evolution π_i = P π_{i−1}, full arc overview/proof/summary
(prob04-random-processes/prob04-random-processes.html:622); **Thm 2** t-step
evolution π_t = P^t π_0 (prob04-random-processes/prob04-random-processes.html:815);
**Thm 3** existence of a stationary initial distribution under finite-state +
irreducible + aperiodic, stated without proof as in the tex
(prob04-random-processes/prob04-random-processes.html:1158); **Thm 4** limiting ⟹
stationary, with limit-both-sides proof
(prob04-random-processes/prob04-random-processes.html:1463).
Figures: diagrams are inline SVG with KaTeX labels overlaid as HTML spans (`.p4-fig`/`.fl`, pattern from prob03) — route map, memory-one strip, random-walk line, binary/three-state chain graphs, sliding window, random-walk fan-out, irreducible/aperiodic glosses, three-page random surfer (P and π* = (0.4, 0.2, 0.4) worked); modeling spectrum stays plain SVG. Real figure: `figs/schiff-noise-processes.png` ("The cat sat on the mat" corrupted by absorbing vs. uniform kernels; Schiff et al., ICLR 2025, as redrawn in the Kuleshov Group blog 2026; cited on the slide and as note ref [13]) replaces the former noising pixel-grid sequence on the data-dissolves slide; the tex's
scribe12-markovex.png and scribe12-distribution.png are redrawn as SVG (noted on
the slides). Deviations from tex: the tex's duplicated/contradictory binary-chain
conditionals (p(1|0)=α and p(1|0)=1−α, prob 1297/1391) fixed to flip-α / stay-(1−α);
the tex's π_t vs π_i index mismatch (prob 1281) normalized to π_i. Added beyond the
tex per mandate: proofs for Thm 1/2, eigenvalue technique review + by-hand eigen
solutions of both running chains, symmetric-P exercise solution, convergence-rate
slides (second eigenvalue), numeric evolution table/chart, and the diffusion
forward/backward picture slides.

### prob05-concentration — Concentration Inequalities & the Law of Large Numbers (106 slides)

`prob05-concentration/prob05-concentration.html` · source: prob 1457–1595.
Lecture 5 — answers prob04's teaser (averages of many draws); recalls expectation/
variance from prob01 and independence from prob03 instead of redefining; one running
example (mean of n fair coin flips, Pr(X̄_n ≥ 3/4)) is re-answered by every bound;
ends on a bridge to prob06 (tail bounds uniform over a hypothesis class → Hoeffding
+ union bound).
Companion: `prob05-concentration/prob05-concentration-note.html` — detailed definitions, expanded proofs, lemmas, references.
Accessible edition: `prob05-concentration/prob05-concentration-note.md` — screen-reader Markdown edition of that note (1187 lines): plain ASCII, LaTeX math, figures replaced by verbal descriptions, self-contained (no references to the slides).

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + TOC | 1–2 | prob05-concentration/prob05-concentration.html:45 |
| 01 | Why Averages? (minibatch loss / test accuracy / Monte Carlo cards, how-many-samples question, three-bounds preview, route map SVG) | 3–8 | prob05-concentration/prob05-concentration.html:137 |
| 02 | Warm-Up (expectation :260 / variance :276 recall from prob01, independence recall from prob03, product-rule proof, variance adds, coin running example :336, why not just compute it) | 9–16 | prob05-concentration/prob05-concentration.html:252 |
| 03 | Markov's Inequality (indicator technique :372, Thm 1 arc: statement :409, threshold form :421, 3-step proof, coin answer 0.67, tightness example :514, what it buys) | 17–29 | prob05-concentration/prob05-concentration.html:364 |
| 04 | Chebyshev's Inequality (squaring technique, Thm 2 arc, ασ-rule table :645, Var(X̄_n)=σ²/n :661, coin answer, Markov-vs-Chebyshev 4/n chart :694, 50,000-samples computation :718) | 30–42 | prob05-concentration/prob05-concentration.html:542 |
| 05 | Law of Large Numbers (convergence-in-probability def :738 + picture, Thm 3 arc, sample-path SVG :830, tails-vanish chart :853, where AI leans on it, the-gap teaser :894) | 43–53 | prob05-concentration/prob05-concentration.html:730 |
| 06 | Moment Generating Functions (def :918, moment machine M'(0)/M''(0), Taylor view, Bernoulli MGF :975, Gaussian MGF exercise via completing the square, Thm 4 uniqueness :1060, Prop. sums→products :1075, Gaussian-sum worked, coin-sum MGF :1103) | 54–69 | prob05-concentration/prob05-concentration.html:910 |
| 07 | Chernoff Bound (exponentiating-the-event technique :1164, Thm 5 arc :1188, free parameter t, coin 3-step optimization t*=ln 3 → exponent 0.1308 :1284, KL-exponent view :1315, 18,444-samples revisit :1328, what it buys) | 70–84 | prob05-concentration/prob05-concentration.html:1141 |
| 08 | Three Bounds Head-to-Head (escalation table, numeric table on Pr(X̄_n ≥ 3/4) :1381, log-scale chart :1396, takeaway) | 85–89 | prob05-concentration/prob05-concentration.html:1358 |
| 09 | Central Limit Theorem (shape question, standardization, Thm 6 :1472, sketch scope caveat, Taylor-at-zero + compound-interest-limit techniques, 3-step MGF sketch, Bin(16,½)-vs-bell chart :1587, what it buys) | 90–103 | prob05-concentration/prob05-concentration.html:1440 |
| — | One-coin-every-tool recap table (chain takeaway folded in as its muted line), bridge to prob06, end slide | 104–106 | prob05-concentration/prob05-concentration.html:1636 |

Key theorems: **Thm 1** Markov Pr(X ≥ αE[X]) ≤ 1/α, non-negative X, full arc
(prob05-concentration/prob05-concentration.html:409); **Thm 2** Chebyshev
Pr(|X−μ| ≥ ασ) ≤ 1/α², full arc (prob05-concentration/prob05-concentration.html:579);
**Thm 3** weak LLN X̄_n → μ in probability, proved via Chebyshev + Var(X̄_n)=σ²/n
(prob05-concentration/prob05-concentration.html:776); **Thm 4** MGF uniqueness,
stated without proof as in the tex
(prob05-concentration/prob05-concentration.html:1060); **Prop.** MGFs turn
independent sums into products
(prob05-concentration/prob05-concentration.html:1075); **Thm 5** Chernoff
Pr(X ≥ α) ≤ M(t)e^{−tα} for all t > 0, full arc
(prob05-concentration/prob05-concentration.html:1188); **Thm 6** CLT, MGF-based
sketch flagged non-rigorous as in the tex
(prob05-concentration/prob05-concentration.html:1472).
Figures: all diagrams inline SVG (route map, indicator step, tightening-density
picture, LLN sample path with fixed seed, exact-vs-Chebyshev decay, Markov-vs-
Chebyshev 4/n curve, step-vs-exponential lid, log-scale head-to-head,
Bin(16,½)-vs-bell). All numeric tables hand-computed from binomial sums (exact
Pr(S₁₆ ≥ 12) = 2517/65536 ≈ 0.038; Chernoff exponent D(Bern(3/4)‖Bern(1/2)) ≈
0.1308). Deviations from tex: prob 1569 "mean 0" fixed to mean μ; prob 1571–1572
garbled LLN bound σ²/(nε) fixed to σ²/(nε²); prob 1542 "M(Y)(t)" fixed to M_Y(t);
prob 1529's incomplete Gaussian-sum exercise completed via MGF product +
uniqueness. Conditional expectation (prob 1577–1592) deferred to prob07 per deck
plan. Added beyond the tex, flagged on-slide as illustration: Markov tightness
example, KL-divergence form of the optimized Chernoff exponent, Gaussian-actual
column in the ασ table.

### prob06-generalization — From Concentration to Generalization (51 slides)

`prob06-generalization/prob06-generalization.html` · **default deck, senior undergraduates** (no time limit,
rigorous mode). Rewritten 2026-10 from the 105-slide deck, which is kept as the
full / advanced edition below, in `prob06-generalization/backup/` (not linked from this deck). One running example throughout: choosing a spam
filter from a finite class. Assumptions (i.i.d. sample, loss in [0,1]) are stated
early. Recurring red "Lucky one" callout (`.p6-lucky`): a model picked on training data carries no
test guarantee by itself. Sub-Gaussian calculus, the KL bridge, the KL plot, the three-way coin table and the
VC machinery (growth function, Sauer) are in the notes only; the slides never cite the notes. No tech supplement.

Companion: `prob06-generalization/prob06-generalization-note.html` — the notes:
setup, Chernoff/KL, Hoeffding's lemma proof, union bound and selection bias, Theorem 3 proof,
VC/Sauer precise statements, ResNet-50 calculation, validation set, references.
Generated from the Markdown edition.
Accessible edition: `prob06-generalization/prob06-generalization-note.md` (716 lines):
screen-reader Markdown, LaTeX math, figures described verbally.

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + TOC | 1–2 | prob06-generalization/prob06-generalization.html:48 |
| 01 | Why Generalization? (spam-filter running example :126, why a class H: fixed architecture limits capability :156, two error rates :170, pipeline D → n i.i.d. samples → minimize R̂ₙ over a predefined H → ĥ, with the lecture's question "is R(ĥ) small?" :184, two assumptions :216, ERM and gap :230, why concentration cannot be applied to ĥ directly :244, memorizer as the extreme example, qualified (atomless X, independent fair labels) :269) | 3–11 | prob06-generalization/prob06-generalization.html:116 |
| 02 | Hoeffding's Inequality (fixed filter = biased coin :291, fixed before data: unbiased :347, chosen after data: optimistic, E R̂(ĥ) ≤ R(h*) ≤ E R(ĥ) :362, lucky filter: 30-email grid, ĥ 0/5 on training vs 14/25 on the rest :375, Lemma 1 :620, Thm 1 with "fix the model before seeing the training data" + why not the optimized Chernoff/KL bound (depends on unknown p) :633, five-step proof: Markov→Chernoff :649, independence :663, lemma per factor :677, optimize t = 4nε :689, lower tail + factor 2 :701; decay chart :715, ±2%@95% → n ≥ 4,612 :744) | 12–25 | prob06-generalization/prob06-generalization.html:281 |
| 03 | Selection and the Union Bound (best of 1,000 useless filters :763, the selection trap :800, Thm 2 union bound :815, guard every filter at once :827, reading the union: did a useless filter get lucky? (making it rare controls ERM's optimism) :841, price ×\|H\| table with n=25 / n=100 takeaways :851) | 26–32 | prob06-generalization/prob06-generalization.html:753 |
| 04 | The Finite-Class Theorem (one bound for every h covers ĥ: Pr(\|gap(ĥ)\|>ε) ≤ Pr(∃h: \|gap(h)\|>ε) :879, Thm 3 :896, three-line proof :910, Cor 4 ERM within 2ε, displayed :926, Cor 4 proof table incl. the ERM step :940, equation chain + two-hop picture :956, sample size formula :985, sample-size table :1001) | 33–41 | prob06-generalization/prob06-generalization.html:869 |
| 05 | Beyond Finite Classes (thresholds give at most n+1 labelings :1027, ln\|H\| → d_VC with SSBD Thm 6.8 :1063) | 42–44 | prob06-generalization/prob06-generalization.html:1017 |
| 06 | The Validation Set (bound can exceed 1 :1085, validation set predicts unseen test error :1100, framework diagram: train k models (any method) → freeze H = {h₁…h_k} → score on m unseen validation examples → pick ĥ; = ERM over \|H\| = k with n = m, Cor 4 gives R(ĥ) ≤ min_j R(h_j) + 2ε :1114, picking among k models; adaptivity caveat :1151) | 45–49 | prob06-generalization/prob06-generalization.html:1075 |
| — | Recap table, end slide | 50–51 | prob06-generalization/prob06-generalization.html:1163 |

Key theorems: **Lemma 1** Hoeffding's lemma (prob06-generalization/prob06-generalization.html:623); **Thm 1** Hoeffding's
inequality (prob06-generalization/prob06-generalization.html:636); **Thm 2** union bound (prob06-generalization/prob06-generalization.html:818); **Thm 3** finite-class uniform
convergence (prob06-generalization/prob06-generalization.html:900); **Cor 4** ERM within 2ε (prob06-generalization/prob06-generalization.html:929); SSBD Thm 6.8 stated informally
(prob06-generalization/prob06-generalization.html:1070). Growth function, Sauer's lemma, precise VC theorems (SSBD Thms 6.8, 6.11) and Rademacher (SSBD 26.5) are
in the notes only.

### prob06-generalization-full — Full / advanced edition (105 slides)

`prob06-generalization/backup/prob06-generalization-full.html` · **new material — not in tex**
(textbook-canonical statements/proofs only; sequel to prob05). Lecture 6 — answers
prob05's bridge (one fixed average → every hypothesis at once); recalls Chernoff/
MGF rules/Gaussian MGF from prob05 without re-proving them (the slides state the
tools, not the source deck); the prob05 coin
running example (Pr(X̄₁₀₀ ≥ 3/4)) returns to benchmark Hoeffding against Chernoff
2.1×10⁻⁶ and exact 2.8×10⁻⁷; ends on a bridge to prob07 (how to *choose* ĥ →
likelihood, MLE/MAP, bias–variance).

Companion: `prob06-generalization/backup/prob06-generalization-full-note.html` — detailed definitions, expanded proofs, lemmas, references.
Accessible edition: `prob06-generalization/backup/prob06-generalization-full-note.md` — screen-reader Markdown edition of that note (1148 lines): plain ASCII, LaTeX math, figures replaced by verbal descriptions, self-contained (no references to the slides).

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + TOC | 1–2 | prob06-generalization/backup/prob06-generalization-full.html:45 |
| 01 | Why Generalization? (train/test/gap cards, setup ℓ(h,z)∈[0,1] :161, true risk R(h) :175, empirical risk R̂_n :188, ERM :201, gap def :215, overfitting U-curve SVG :230, memorizer worked example R̂=0 vs R=1/2 :254, why fixed-h bounds fail for ĥ :265, route map SVG :280, destination preview gap ≲ √((complexity+confidence)/n) :312) | 3–14 | prob06-generalization/backup/prob06-generalization-full.html:129 |
| 02 | Recall — the Concentration Toolkit (Chernoff card :342, MGF product/scale rules :357, Gaussian MGF e^{t²σ²/2} :372, what Chernoff needed vs. boundedness-only :387) | 15–19 | prob06-generalization/backup/prob06-generalization-full.html:334 |
| 03 | Hoeffding's Lemma (goal :410, techniques: bounded-variance lemma Var ≤ (b−a)²/4 + midpoint proof :424, tilted distributions (discrete-case scope line) + bar-chart SVG :452, Taylor with Lagrange remainder :494, Thm 1 arc :507, 4-step proof ψ(0)=ψ'(0)=0 / ψ''=tilted variance / cap / integrate :531, proof summary chain :597, ±1 series sanity check (2k)! ≥ 2^k k! :612, any-mean corollary :624, what it buys) | 20–37 | prob06-generalization/backup/prob06-generalization-full.html:402 |
| 04 | Sub-Gaussian Variables (definition variance proxy :660, Gaussian equality example :672, bounded-variable proxy table :685, Thm 2 tail bound arc :701, Chernoff+envelope+optimize t*=ε/σ² proof :724, two-sided :746, tail-envelope SVG :758, closure rules: scaling c²σ² :780, Prop. sums add proxies + 3-line proof :794, averages σ²/n :818, one-card calculus recap :832) | 38–52 | prob06-generalization/backup/prob06-generalization-full.html:652 |
| 05 | Hoeffding's Inequality (Thm 3 arc exp(−2nε²/(b−a)²) :856, 3-step assembly proof :869, two-sided workhorse 2e^{−2nε²} :915, proof summary :928, coin returns table vs. Chernoff/exact :942, exponent 0.125-vs-0.1308 lesson :959, worked ±2%@95% → n ≥ 4,612 :973, Chebyshev-vs-Hoeffding table 12,500 vs 4,612 :985, what it buys) | 53–65 | prob06-generalization/backup/prob06-generalization-full.html:848 |
| 06 | The Union Bound (Thm 4 Boole :1023, one-line indicator proof :1035, Venn SVG overlap-counted-twice :1046, 10⁴-model farm thought experiment :1070, farm worked example 3.7% :1083, small-test-set vacuous case n=25 :1097, Bonferroni δ/m split :1111, what it buys +ln m :1124) | 66–74 | prob06-generalization/backup/prob06-generalization-full.html:1015 |
| 07 | The Generalization Theorem (finite classes: stumps/quantized nets :1146, risks recall card :1164, fixed h is a coin :1179, the trap ĥ not fixed :1193, the fix G_ε event :1206, Thm 5 arc sup gap ≤ √(ln(2|H|/δ)/2n) :1219, 3-step proof per-h → union → invert :1243, proof summary :1278, ε-tube SVG :1294, ERM corollary R(ĥ) ≤ min R + 2ε :1325, three-hop proof :1337, why-2ε SVG :1352, complexity as description length (bits/nats) :1380, sample complexity 139/bit :1394, numbers table :1406, chart SVG n = ⌈737.78+138.63k⌉ :1423, confidence-is-cheap table :1448, VC/Rademacher road ahead (names only) :1464) | 75–96 | prob06-generalization/backup/prob06-generalization-full.html:1138 |
| 08 | Why ERM Works (license to train :1485, approximation-vs-estimation split :1501, trade-off U-curve SVG :1511, honest slide: ResNet-50 bound vacuous ε ≈ 14.9, open research :1538, what survives: test-set bound |H|=1, validation, leaderboard overfitting :1553) | 97–102 | prob06-generalization/backup/prob06-generalization-full.html:1477 |
| — | Every-tool recap table (chain takeaway folded in as its muted line), bridge to prob07, end slide R(ĥ) ≤ R(h*) + 2ε | 103–105 | prob06-generalization/backup/prob06-generalization-full.html:1568 |

Key theorems: **Thm 1** Hoeffding's lemma E[e^{tX}] ≤ exp(t²(b−a)²/8) for X∈[a,b],
E[X]=0, full arc via tilted-distribution log-MGF (ψ'' = tilted variance ≤ (b−a)²/4,
Taylor with remainder) (prob06-generalization/backup/prob06-generalization-full.html:511);
**Thm 2** sub-Gaussian tail Pr(X−μ ≥ ε) ≤ e^{−ε²/2σ²}, Chernoff + envelope +
optimize (prob06-generalization/backup/prob06-generalization-full.html:705); **Prop.**
independent sums add variance proxies
(prob06-generalization/backup/prob06-generalization-full.html:798); **Thm 3** Hoeffding's
inequality Pr(X̄_n−μ ≥ ε) ≤ exp(−2nε²/(b−a)²), assembled from Thm 1 + closure rules
+ Thm 2 (prob06-generalization/backup/prob06-generalization-full.html:860); **Thm 4** union
bound, one-line indicator proof
(prob06-generalization/backup/prob06-generalization-full.html:1027); **Thm 5** finite-class
uniform convergence sup_h |R−R̂_n| ≤ √(ln(2|H|/δ)/2n) w.p. ≥ 1−δ, full arc
(prob06-generalization/backup/prob06-generalization-full.html:1223); **Cor.** ERM guarantee
R(ĥ) ≤ min_h R(h) + 2ε, three-hop proof
(prob06-generalization/backup/prob06-generalization-full.html:1329).
Figures: all diagrams inline SVG with hand-computed numbers (overfitting U-curve,
route map, tilting bar chart, sub-Gaussian tail envelope, union-bound Venn, ε-tube
with ERM pick, why-2ε two-hop ladder, approximation-estimation trade-off, sample-
complexity line n = ⌈737.78+138.63k⌉). All numeric examples hand-computed: n ≥ 4,612 for
±2%@95% (ln 40/0.0008), model-farm 10⁴×3.7×10⁻⁶ = 3.7%, vacuous n=25 case
e^{−3.125} ≈ 0.044, sample-complexity table (10 → 1,199; 10³ → 2,120; 10⁶ → 3,501;
2¹⁰⁰ → 14,601), ResNet-50 honest slide (25.6M params × 32 bits → ln|H| ≈ 5.7×10⁸,
n = 1.28×10⁶ → ε ≈ 14.9). Cross-deck numbers (Chernoff 2.1×10⁻⁶, exact 2.8×10⁻⁷,
exponent 0.1308) taken from prob05's published slides. Illustrative-only counts
flagged on-slide: decision-stump class size 256d, ResNet-50 parameter count.

### prob07-estimation — Estimation: MLE, MAP & Fundamental Limits (130 slides)

`prob07-estimation/prob07-estimation.html` · **prob 1563–1911** plus conditional
expectation/tower (prob 1577–1592, deferred here from prob05 per deck plan).
Lecture 7 — opens on likelihood as the origin of the CE loss (no prob06 link, per
Albert 2026-10-26); recalls
prob02 CE loss, prob03 conditional pmf + heights model, prob04 diffusion teaser,
prob05 MGF add-and-subtract, prob06 H(Y|X)/chain rule/DPI by name without
re-proving; prob03's two-coin table (p(0,0)=p(0,1)=1/4, p(1,0)=1/2) returns twice
(conditional means 2/3 and 0, MMSE = 1/6 vs constant-guess 1/4); ends on
a bridge to prob08 (the Gaussian everywhere → multivariate Gaussian, linear
E[X|Y]).

Companion: `prob07-estimation/prob07-estimation-note.html` — detailed definitions, expanded proofs, lemmas, references.
Accessible edition: `prob07-estimation/prob07-estimation-note.md` — screen-reader Markdown edition of that note (1843 lines): plain ASCII, LaTeX math, figures replaced by verbal descriptions, self-contained (no references to the slides).

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + TOC | 1–2 | prob07-estimation/prob07-estimation.html:45 |
| 01 | Why Estimation? (DL as estimation cards :162, where the loss comes from: max likelihood ⟺ min CE loss :163, claim CE=MLE to prove today :179, inference vs. learning faces :193) | 3–6 | prob07-estimation/prob07-estimation.html:155 |
| 02 | Conditional Expectation (recall prob03 conditional pmf :224, definition :243, worked conditional pmfs + means 2/3 and 0 :259, E[X|Y] is an RV with its own distribution :276, Thm 1 tower arc :317, proof :330, why it matters today :347) | 7–14 | prob07-estimation/prob07-estimation.html:215 |
| 03 | The Estimation Problem (sample/label setup :372, two-nationalities running example :387, two height densities SVG N(170,10²) vs N(180,15²) :401, two questions about x=176: likelihood (MLE) vs posterior (MAP) in plain English :422) | 15–19 | prob07-estimation/prob07-estimation.html:363 |
| 04 | Maximum Likelihood (definition :454, MLE on heights :471, worked x=176 → 0.0333>0.0257 → A :485, decision-boundary SVG ≈179 :500, worked x=185 → B :523, what MLE ignores :536) | 20–26 | prob07-estimation/prob07-estimation.html:445 |
| 05 | Maximum a Posteriori (definition :559, Bayes' rule derivation :576, evidence drops out :591, heights with 9:1 prior :604, worked x=176 :619, worked x=185 — MLE/MAP disagree 0.0117 vs 0.0025 :632, prior moves boundary SVG, both MAP edges ≈129/≈195 :648, Bayes-optimal defined + Thm 2 MAP is Bayes optimal :675, 2-step proof :690, regularization can encode a prior :719) | 27–38 | prob07-estimation/prob07-estimation.html:550 |
| 06 | Fano's Inequality (fundamental-limit question :743, Thm 3 arc P_e ≥ (H(Y|X)−1)/log|Y| stated first :758, reading the bound :773, proof overview :788, 9 one-idea proof steps (techniques — chain rule, DPI, conditioning average — named inline) :801–:912, proof summary &mdash; sandwich picture SVG + takeaway line :925, worked 1024-class (1.5−1)/10 = 0.05 :949, vacuous case :964, what Fano buys :977) | 39–56 | prob07-estimation/prob07-estimation.html:734 |
| 07 | Parameter Estimation (new target θ :1001, log-likelihood :1016, Bernoulli MLE in cases form + derivation :1030, the obvious guess (empirical mean) is the MLE + LLN/Hoeffding :1071, worked 10 flips 7 heads L(0.5)=0.00098 < L(0.7)=0.00222 > L(0.9)=0.00048 :1086, log-lik curve SVG :1103, Gaussian MLE μ̂ and σ̂² :1125, empirical distribution definition :1173, example a b a c a d b a c a → (0.5,0.2,0.2,0.1) bar SVG :1186, average loss grouped by symbol :1219, promised proof CE loss = MLE :1236, via KL :1251, one identity three names :1265) | 57–74 | prob07-estimation/prob07-estimation.html:992 |
| 08 | Naive Bayes (classification needs a model p_X^n|Y — MLE/MAP argmax, heights Gaussian recall, parametric modeling :1289, 2ⁿ-parameter blowup 2⁴⁹ ≈ 5.6×10¹⁴ :1306, conditional-independence assumption :1320, spam-filter SVG :1339, MNIST 28×28 figure :1375, binarized 7×7 grid SVG + itemized description :1386, NB classifier :1459, fit by counting = Bernoulli MLE :1471, fit the prior :1487, MAP with fitted model :1501, worked 10-mail table spam/non-spam p_free|spam=3/4 :1513, classify new mail 0.225/(0.225+0.033) ≈ 0.87 spam :1529, zero-count veto :1543, Laplace smoothing :1558, smoothed table 1/8, 2/8, 5/8 :1574, takeaway :1590) | 75–91 | prob07-estimation/prob07-estimation.html:1281 |
| 09 | Bias–Variance (estimator is an RV :1614, bias :1628, variance :1642, MSE :1658, technique review add-and-subtract :1672, Thm 4 MSE = Bias² + Var arc :1687, 2-step proof cross term dies :1703, dartboard SVG :1732, sample-mean example σ²/n :1768, worked p̂=S/10 vs p̃=(S+1)/12 :1785, numbers 0.025 vs 0.0174 (p=.5), 0.009 vs 0.0107 (p=.9) :1800, MSE-vs-p chart SVG crossings ≈0.14/0.86 :1816, regularization trade :1839) | 92–106 | prob07-estimation/prob07-estimation.html:1605 |
| 10 | MMSE Estimation (denoising channel SVG + MMSE is Bayes-optimal for squared error :1863, Thm 5 MMSE = E[X|Y] arc :1893, proof overview :1906, 4 proof steps insert/expand → tower kills cross term → read off :1918–:1958, proof summary :1970, worked prob03 table MMSE = 1/6 < 1/4 :1990, denoisers learn E[X|Y] :2005) | 107–117 | prob07-estimation/prob07-estimation.html:1854 |
| 11 | Generative Models (section :2020, learn p_data then sample pipeline SVG + MLE ⟺ min KL (discrete data/models) :2029, two families cards ChatGPT/Claude/Llama · Stable Diffusion/Imagen :2064, LLM chain rule = exact likelihood :2086, worked "the cat sat" 4.32+6.64+2.32 = 13.29 bits, perplexity ≈21.5 :2104, pretraining is MLE at scale — GPT-3 300B tokens, Llama 3 405B/15.6T, CE SFT is MLE, RLHF is not :2122, diffusion: auxiliary forward process chain SVG, q(x_t|x_{t−1}), closed form ᾱ_t, DDPM T=1000 :2140, DDPM Gaussian backward steps p_θ = N(μ_θ, σ_t²I) :2184, each backward step is a fixed-variance Gaussian MLE, μ* = E[x_{t−1}|x_t,t] (Thm 5), continuous-Gaussian teaching model t ≥ 2, discretized t=1 decoder :2202, the full ELBO is path-likelihood training (path NLL = −ELBO + const); simple loss reweighted denoising; neither is image MLE, θ-dependent gap :2219, scorecard — only LLM cross-entropy training is exact MLE of q_θ(x); diffusion full bound = path MLE, simple loss reweighted :2238) | 118–128 | prob07-estimation/prob07-estimation.html:2020 |
| — | Bridge to prob08, end slide X̂(Y)=E[X|Y] | 129–130 | prob07-estimation/prob07-estimation.html:2255 |

Key theorems: **Thm 1** tower property E[E[X|Y]] = E[X], full proof + table check
(prob07-estimation/prob07-estimation.html:317); **Thm 2** MAP minimizes error
probability, 2-step proof score-any-estimator → maximize each term
(prob07-estimation/prob07-estimation.html:675); **Thm 3** Fano's inequality
P_e ≥ (H(Y|X)−1)/log|Y|, full 9-step proof (error flag, two chain-rule expansions
of H(E,Y|Ŷ), DPI, bound both scenario terms, close the sandwich)
(prob07-estimation/prob07-estimation.html:758); **Thm 4** bias–variance
decomposition MSE = Bias² + Var, exact identity, add-and-subtract proof
(prob07-estimation/prob07-estimation.html:1687); **Thm 5** MMSE estimator is the
conditional mean, 4-step proof with tower killing the cross term
(prob07-estimation/prob07-estimation.html:1893).
Figures: MNIST digit (../figs/mnist.png); binarized 7×7 grid SVG (cells from
approximate 4×4 block means of that figure, thresholded); all other
diagrams inline SVG with hand-computed geometry (two height densities,
MLE boundary ≈179 with pick-B crossing ≈145, prior-shifted boundary ≈195, Fano
sandwich, Bernoulli log-likelihood curve with max at 0.7, spam-mail feature map,
empirical-distribution bars, dartboard bias/variance quadrants, MSE-vs-p parabolas with crossings ≈0.14/0.86,
denoising channel, generative pipeline, diffusion noising/denoising chain). All numerics hand-computed (heights densities at 176/185, NB
10-mail table + 0.87 posterior + smoothed 1/8-2/8-5/8, coin likelihood table,
p̂-vs-p̃ MSE table, Fano 1024-class floor 0.05 (sharp ≈0.102 in note), MMSE 1/6 vs 1/4; generative section: "the cat sat" per-token bits; GPT-3 and Llama 3 checked against the arXiv papers cited in the note refs 8–9; DDPM equations, schedule and Langevin/score-matching quotes checked against Ho et al. 2020 (ref 7), refs 11–12 Song & Ermon 2019 and Vincent 2011 via its bibliography). Deviations from
tex: prob 1661 MAP argmax written over the likelihood, fixed to the posterior;
prob 1791 prior-count indicator 1{y⁽ʲ⁾=0}, fixed to 1{y⁽ʲ⁾=1}; prob 1802
duplicate p(x_i|0) in the numerator, fixed to p(x_i|1); "twice as likely" vs
9/10 prior inconsistency in the heights example resolved to a 9/10 : 1/10 prior
throughout; spelling fixes (Conditioanl, funciton, classfication). Added beyond
the tex: tower-property proof, MAP Bayes-optimality proof, Bayes-rule derivation
slide, Fano technique-review slides, CE-loss=MLE bridge slides, and all worked
numeric examples above (the tex states the estimators but computes none of
them).

### prob08-gaussian — The Multivariate Gaussian (154 slides)

`prob08-gaussian/prob08-gaussian.html` · source: prob 1912–2519.
**Attribution: the tex credits MIT OpenCourseWare 6.436J / 15.085J Fundamentals of
Probability (Fall 2018), License CC BY-NC-SA 4.0 — preserved on-slide as a visible
credit line on the §02 section divider (prob08-gaussian/prob08-gaussian.html:220)
covering sections 02–08.** Lecture 8 — answers prob07's bridge (the Gaussian
everywhere, linear E[X|Y]); recalls prob05 MGF + uniqueness, prob04 Markov/diffusion
teaser, prob03 MaxEnt Gaussian, prob07 MMSE by name without re-proving; undergrad
DDPM treatment (grad-level rigor lives in `courses/privacy/lectures/02-generative/`
and `courses/infotheory/lectures/07-diffusion/` — this deck stops at the exact
forward process + Gaussian reverse-step form, no variational objective); ends on a
bridge to prob09 (integrals stop closing → Monte Carlo).

Companion: `prob08-gaussian/prob08-gaussian-note.html` — detailed definitions, expanded proofs, lemmas, references.
Accessible edition: `prob08-gaussian/prob08-gaussian-note.md` — screen-reader Markdown edition of that note (1987 lines): plain ASCII, LaTeX math, figures replaced by verbal descriptions, self-contained (no references to the slides).

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + TOC | 1–2 | prob08-gaussian/prob08-gaussian.html:47 |
| 01 | Why Gaussians? (default noise model cards, recall, 1D-so-far gap, today's claims) | 3–7 | prob08-gaussian/prob08-gaussian.html:139 |
| 02 | Warm-Up: Two Dimensions (jointly Gaussian pair :224, joint density :239, coupling picture, running example :278, eigenpairs orient the ellipse :292, Thm 1 statement :325, 3D surface cut :337, normalize the slice :477, worked conditional :514, what the general case needs) | 8–18 | prob08-gaussian/prob08-gaussian.html:215 |
| 03 | Positive Semidefinite Matrices (PD/PSD def :550, bowl-vs-trough SVG, PD certificate :605, linear-algebra facts, eigendecomposition in matrix form :633, spectral decomposition :668, worked eigenpairs :683, symmetric square root :697 + worked :710, inverse, factorization exercise + solution, λ_min integrability bound :761) | 19–32 | prob08-gaussian/prob08-gaussian.html:542 |
| 04 | Multivariate Normal — three equivalent definitions (overview :783, Def 1 density :808, white noise :822, Def 2 constructive X=DW+μ :835 + coloring SVG, Def 3 projection :876 + shadow SVG, degeneracy :912, equivalence diagram: what is proved :944) | 33–42 | prob08-gaussian/prob08-gaussian.html:775 |
| 05 | Vector Means & Covariances (mean vector :990, covariance matrix :1002, self-covariance :1018, PSD exercise + solution :1031, correlation coefficient :1058) | 43–49 | prob08-gaussian/prob08-gaussian.html:982 |
| 06 | The Properties Theorem — state one part, prove it (Def-2 standing assumption :1080; part 1 projections :1096; part 2 mean/Cov=DD^T :1141; part 3 affine closure :1182 + marginals by selection :1207; part 4 density :1334 via volume intuition :1348–:1413 + proof :1430; part 5 MGF :1486; part 6 coordinates & blocks :1543 + counterexample :1558; part 7 setup :1643, statement :1658, proof :1674–:1731, orthogonality test :1747–:1776, projection picture :1788, affine vs conditional mean :1822, residual :1840–:1886; conditional assembled :1907; Thm 1 proved :1922; summaries parts 1–3/4–6/7 :1936–:1965) | 50–102 | prob08-gaussian/prob08-gaussian.html:1072 |
| 07 | The Gaussian Channel (Y=X+Z setup + block SVG :1986, joint covariance :2013, read off part 7 :2027, promise kept (prob07 MMSE) :2041, shrinkage SVG :2054, two extremes :2074, two sampling orderings :2090, why the second matters :2115) | 103–111 | prob08-gaussian/prob08-gaussian.html:1980 |
| 08 | Gaussian Diffusion (back from prob07 :2135, today's questions :2176, noising recursion :2190, variance preserving :2202, noising-chain figure :2216, source exercise :2247, MGF telescope :2260–:2290, Thm 3 chain forgets :2304, closed form :2321, DDPM ᾱ notation :2334, worked β=0.02 schedule :2348, three reverse objects :2372, exact reverse given x_0 :2387, stationary Gaussian benchmark :2403, vectors :2419, simplified reverse sampler :2432, prob07's learning view :2457 + target :2484) | 112–132 | prob08-gaussian/prob08-gaussian.html:2128 |
| 09 | Gaussian Discriminant Analysis (spam filter, new likelihood :2508, one Gaussian per class :2529, Mahalanobis distance :2545 + figure :2561, decision rule :2600, curved boundary SVG :2616, back to MLE :2733, log-likelihood :2746, fit μ :2759, variance→covariance goal :2776, precision reparam :2790, why the trace trick :2805 + calculation :2834, scatter matrix :2853, matrix derivatives :2865, solve :2881, Thm 4 :2898, source exercises :2916, GDA pipeline :2931) | 133–152 | prob08-gaussian/prob08-gaussian.html:2501 |
| — | Bridge to prob09, end slide X=DW+μ | 153–154 | prob08-gaussian/prob08-gaussian.html:2947 |

Key theorems: **Thm 1** 2D conditional X|Y=y ~ N(μ₁+σ₁₂/σ₂₂(y−μ₂), σ₁₁−σ₁₂σ₂₁/σ₂₂),
stated in §02, proved as part-7 corollary
(prob08-gaussian/prob08-gaussian.html:325, proof :1922); **Thm 2** seven properties
of the multivariate normal (affine closure, Cov = DD^T, marginals, density when
V ≻ 0, MGF exp(s^Tμ + s^TVs/2), uncorrelated = independent, conditionals with
linear mean + variance shrinkage), each part stated then proved, summaries at
(prob08-gaussian/prob08-gaussian.html:1936); **Thm 3** diffusion limit
X_n →d N(0,1) for any X₀ with an MGF, via MGF telescope
(prob08-gaussian/prob08-gaussian.html:2304); **Thm 4** Gaussian MLE μ̂ = sample
mean, Σ̂ = S/N via trace trick + matrix derivatives, biasedness remarked
(prob08-gaussian/prob08-gaussian.html:2898).
Figures: all diagrams inline SVG with hand-computed geometry (running
2D ellipse + slice, bowl-vs-trough quadratic surfaces, coloring-white-noise map,
projection shadows, channel block diagram, shrinkage line, noising chain, β=0.02
schedule polylines, generation pipeline, two-class quadratic boundary).
Deviations from tex: prob 1933 2D density exponent transpose fixed; prob 1939–40
2D conditional variance fixed to σ₁₁−σ₁₂σ₂₁/σ₂₂; prob 2085/2156 "density in
Definition 2" corrected to Definition 1; prob 2332–33 two-step telescope exponent
typo 1−(1−β) fixed to 1−(1−β)² (noted on-slide); spelling fixes silently
(reqwuires, convaraince). Flagged on-slide rather than proved: the equivalence
reverse directions Def 1→Def 2 and Def 3→Def 2 (stated in the source without
proof); the Gaussian reverse-diffusion step (source claims it for small β — made
plausible via the §07 channel at stationarity, explicitly labeled an
approximation). Added beyond the tex per mandate: PSD worked examples
(eigenpairs, square root, factorization), part-by-part technique-review slides,
the running 2D numeric example re-checked after part 7, channel sanity tables,
the worked β=0.02 schedule, DDPM ᾱ dictionary slide, and the GDA exercises'
hint slide.

### prob09-monte-carlo — Monte Carlo & Importance Sampling (70 slides)

`prob09-monte-carlo/prob09-monte-carlo.html` · **new material — not in tex**
Lecture 9 — final probability deck; junior undergraduates, rigorous and
example-led; no duration target (Albert C13, job 2026-11-18-prob09-clarity-trim).
Answers prob08's bridge (integrals stop closing → sample them). Argument: Monte
Carlo turns an expectation into computation; choosing the sampler changes the
error, not the target. Opens with ML motivation (expected log loss = forward KL + fixed entropy H(P);
its sample average fits the model by KL from data samples alone, without
evaluating P; pass rate from sampled replies). Recalls prob01
LOTUS/Jensen, prob02 KL, prob04 chain rule, prob05 sample-mean mean/variance,
LLN/Chebyshev/CLT, prob06 Hoeffding, prob07 MSE decomposition without re-proving.
Ends with the expectation-estimator synthesis table (S109a) and the IS-identity
closer. The gradient-estimation chapter (pathwise, score function, baselines,
S109b) was retired in job 2026-11-18-prob09-clarity-trim (Albert C11).

Companion: `prob09-monte-carlo/prob09-monte-carlo-note.html` — one article per slide (`data-slide-id` equals the slide's), Message → explanation → Details/Sources; rebuilt references; source labels: bare E## = 2026-11-17 evidence, "evidence 2026-11-18 E##" = clarity-trim job, "oracle-tails-softmax E##" = job 2026-11-18-prob09-oracle-tails-softmax.
Accessible edition: `prob09-monte-carlo/prob09-monte-carlo-note.md` — same 70 sections in slide order (headings carry `[Sxx]`), ASCII text + LaTeX, figures described in words, self-contained.
Generators: `prob09-monte-carlo/gen/` (`p9a_part01.py`, `p9b_calc.py`, `p9b_figs.py`, `p9c_snis_examples.py`, `p9e_compounding.py`, `p9e_kl_counterexample.py`, `p9f_unknown_z.py` deterministic softmax checker, no randomness); figures in `prob09-monte-carlo/fig/` (p9a-rare-sd.svg, p9b-*.svg incl. p9b-heavy.svg, p9e-compounding.svg, PPO Fig. 1 crops p9e-ppo-fig1-{pos,neg}.png).

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + Contents (five parts) | 1–2 | prob09-monte-carlo/prob09-monte-carlo.html:113 |
| 01 | Estimate an Expectation (log loss targets forward KL + fixed entropy; fit the model without evaluating P: average data log loss is Monte Carlo; sampled replies estimate pass rate; sample-evaluate-average with IID; six hand-chosen darts; sample mean; unbiased ≠ accurate with exact binomial pmf; RMSE σ_f/√n; standard error defined, estimated SE s_Y/√n; CLT interval vs Chebyshev / Hoeffding; bounded averages concentrate; rare-event toy: small absolute error hides failure, relative error needs enough hits) | 3–16 | prob09-monte-carlo/prob09-monte-carlo.html:173 |
| 02 | Change the Sampler (rare tail P(X>10), X~Exp(1); visit useful outcomes; weights w = p/q; IS identity theorem + two-slide proof S47a–S47b; support counterexample; IS estimator; practical Exp(0.1) proposal; weighted contributions fw; relative variance and n_IS; coverage ≠ variance) | 17–31 | prob09-monte-carlo/prob09-monte-carlo.html:516 |
| 03 | Control Proposal Risk (second moment decides; sample where contributions matter; optimal proposal q* = \|f\|p/c + two-slide proof; identical contributions → zero estimator variance for one-sign f; oracle weights need the answer μ (sampling q* ≠ evaluating fp/q*); light-tailed Exp(2) → infinite second moment; consistency ≠ error bar; heavier proposal helps this integrand (5/27); more tail mass can hurt: Exp(1/10) gives 1.916 > ordinary MC; heavier tails neither required nor automatically better) | 32–45 | prob09-monte-carlo/prob09-monte-carlo.html:792 |
| 04 | Remove the Normalizer (softmax needs a global sum Z, toy masses 1/2/4, Z = 7; target known up to Z, Z = Σ_k p̃(k); unnormalised weights; positive total; sampled softmax weights, uniform q, batch A,C,C → 8/9 vs 4/7; ratio of two averages; consistency; one-draw SNIS bias; normalisation does not guarantee improvement; weight dominance; ESS; healthy ESS can miss support; capability map) | 46–59 | prob09-monte-carlo/prob09-monte-carlo.html:1022 |
| 05 | Reuse Samples in RL (behaviour-policy data; IS correction; per-token ratio product; compounding toy E[w²] = 1.1^T; behaviour vs reference roles; KL is not a variance certificate; RL objectives contain expectations — scoped InstructGPT reward-plus-KL objective; PPO clipping as surrogate with advantage defined, Schulman et al. Fig. 1) | 60–68 | prob09-monte-carlo/prob09-monte-carlo.html:1357 |
| — | Synthesis: expectation estimators (S109a); closer E_p[f] = E_q[f·p/q] | 69–70 | prob09-monte-carlo/prob09-monte-carlo.html:1566 |

Key theorems (unnumbered on slides): **Theorem (importance-sampling identity)**
E_p[f] = E_q[f·p/q] when q > 0 wherever fp ≠ 0 (prob09-monte-carlo/prob09-monte-carlo.html:605, proof S47a–S47b);
**Theorem (optimal proposal)** q* = \|f\|p/c minimises the IS second moment
(prob09-monte-carlo/prob09-monte-carlo.html:833, proof S60–S61).
Named-not-proved, flagged: strong LLN; CLT interval as approximate; SNIS
consistency; ESS as a heuristic diagnostic; PPO clipping and the RLHF objective
scoped to the cited sources.

### opt01-svd-lowrank — SVD & Best Low-Rank Approximation (68 slides, 150 min)

`opt01-svd-lowrank/opt01-svd-lowrank.html` · **opt 1–435** (core subset; restructured 2026-11-23, job
`2026-11-23-opt01-opt03-four-hour-core`). Lecture 10 — taught after prob09 in the
2026 final block, split across weeks 13–14 (150 min). Argument: rank and two error
norms → read an SVD → Eckart–Young–Mirsky (truncated SVD is best in both the
spectral and Frobenius norms) → read every number off one matrix. Running example
A=[[3,0],[4,5]] (σ = 3√5, √5); rank-1 sidekick C=[[1,1],[2,2]]. Stable slide IDs
(`data-slide-id`) shared with the full edition. Pseudo-inverse, four fundamental
subspaces, nuclear norm, matrix completion and the least-squares bridge are only in
the full edition (below).

Companion: `opt01-svd-lowrank/opt01-svd-lowrank-note.html` — one article per slide (message → explanation → details → sources); the full Frobenius EYM proof (Courant–Fischer, Weyl) is in the S101 article.
Accessible edition: `opt01-svd-lowrank/opt01-svd-lowrank-note.md` — screen-reader Markdown edition of that note (1285 lines): plain ASCII, LaTeX math, figures replaced by verbal descriptions, self-contained (no references to the slides).

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + TOC | 1–2 | opt01-svd-lowrank/opt01-svd-lowrank.html:100 |
| 01 | Why Low Rank? (smaller matrix, controlled error :168, span/range :185, rank :222, collapse to one direction :246, null space :283, rank–nullity :322) | 3–9 | opt01-svd-lowrank/opt01-svd-lowrank.html:161 |
| 02 | Measuring Error (norm axioms :356, ℓ1/ℓ2/ℓ∞ :387, 7, 5, 4 worked :412, unit balls :446, orthogonal Q preserves length :478/:513, spectral norm = worst stretch :526, Frobenius = total energy :563) | 10–18 | opt01-svd-lowrank/opt01-svd-lowrank.html:349 |
| 03 | Reading an SVD (symmetric eigendecomposition recall :595, SVD theorem :605, factor shapes :619, rotate–stretch–rotate :653–:714, rank-one layers :757, compact SVD :782, SVD of A by hand :810–:895, eigenvalues ≠ singular values :907, ‖A‖₂=σ₁ with upper bound + witness :930–:966, ‖A‖_F²=Σσᵢ² :978, invariance :991) | 19–40 | opt01-svd-lowrank/opt01-svd-lowrank.html:588 |
| 04 | Best Low-Rank Approximation (truncation candidate :1013, worked A₁ and its error :1023/:1038, EYM spectral statement :1049, floor-for-all reading :1063, tools: null space, subspace intersection, two planes in R³, witness, top-k+1 stretch :1094–:1154, proof plan + Steps 1–5 :1166–:1237, one-chain recap :1247, EYM Frobenius statement :1263, achievability :1277) | 41–61 | opt01-svd-lowrank/opt01-svd-lowrank.html:1006 |
| 05 | Read the Answer (best rank-1 error √5 :1300, 90% energy :1313, spectral vs Frobenius error :1333, what the guarantee covers :1345, global recap :1367) | 62–67 | opt01-svd-lowrank/opt01-svd-lowrank.html:1293 |
| — | End slide | 68 | opt01-svd-lowrank/opt01-svd-lowrank.html:1385 |

Key theorems (cited by name on-slide, no numbers): **rank–nullity** (stated,
proof in note; opt01-svd-lowrank/opt01-svd-lowrank.html:326); **orthogonal invariance** claim, proved
(opt01-svd-lowrank/opt01-svd-lowrank.html:517); **SVD existence** (stated; opt01-svd-lowrank/opt01-svd-lowrank.html:609); **spectral norm = σ₁**, upper
bound + witness proof (opt01-svd-lowrank/opt01-svd-lowrank.html:934); **Frobenius norm identity** (opt01-svd-lowrank/opt01-svd-lowrank.html:982);
**Eckart–Young–Mirsky, spectral** — proved in five steps via subspace
intersection (opt01-svd-lowrank/opt01-svd-lowrank.html:1053); **Eckart–Young–Mirsky, Frobenius** — stated, proof in
the note (opt01-svd-lowrank/opt01-svd-lowrank.html:1267).
Figures: inline SVG/HTML with hand-computed geometry; S87 two-planes geometry
from `opt01-svd-lowrank/figs/o1c_planes.py`.
Stated-not-proved on-slide: rank–nullity, SVD existence, Frobenius EYM
(proofs in the note). Uniqueness dropped (spectral minimizer non-unique).

### opt02-convexity-gd — Gradient Descent: Three Guarantees (51 slides, 90 min)

`opt02-convexity-gd/opt02-convexity-gd.html` · **opt 795–1319** (core subset; restructured 2026-11-23, job
`2026-11-23-opt01-opt03-four-hour-core`; folder renamed from `opt03-convexity-gd/`
2026-11-24). Lecture 11 — taught after opt01 in
week 14 (90 min); self-contained, assumes nothing from the backup regression deck. One algorithm,
GD with step 1/L, one descent inequality, three guarantees: nonconvex + lower
bound → min squared gradient O(1/T) (stationarity, not a local minimum);
convex + attained optimum → last function gap O(1/T); μ-strongly convex →
geometric decay of distance and gap. Running example f = 2x₁² + ½x₂²
(L = 4, μ = 1; f falls 10 → 81/128 in two steps). Co-coercivity, PL, Hessian
tests and other step sizes are only in the full edition (below). Stable slide
IDs shared with the full edition.

Companion: `opt02-convexity-gd/opt02-convexity-gd-note.html` — one article per slide (message → explanation → details → sources).
Accessible edition: `opt02-convexity-gd/opt02-convexity-gd-note.md` — screen-reader Markdown edition of that note (1100 lines): plain ASCII, LaTeX math, figures replaced by verbal descriptions, self-contained (no references to the slides).

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + TOC | 1–2 | opt02-convexity-gd/opt02-convexity-gd.html:64 |
| 01 | One Update (goal + nonconvex schematic :140, gradient recall :165, downhill steps :176, L-smoothness :210, step 1/L :224, running example L = 4 :240) | 3–9 | opt02-convexity-gd/opt02-convexity-gd.html:133 |
| 02 | One Descent Inequality (descent lemma :263, touches f at x :276, proof steps 1–3 :303–:329, step 1/L decreases f by ‖∇f‖²/2L :341, worked steps :354/:367) | 10–18 | opt02-convexity-gd/opt02-convexity-gd.html:256 |
| 03 | Nonconvex: Stationarity (theorem :395, proof steps :408/:421, stationary ≠ minimum :433, GD stays at a maximum :456, the square changes the rate :480) | 19–25 | opt02-convexity-gd/opt02-convexity-gd.html:388 |
| 04 | Convex: Optimality (chords above :503, tangent below :537, assume an optimum :566, O(1/T) function gap :600, proof plan + steps :614–:673, one-chain recap :683) | 26–37 | opt02-convexity-gd/opt02-convexity-gd.html:496 |
| 05 | Strongly Convex: Geometric Decay (quadratic floor :706, curvature bounded below :718, theorem :748, contraction proof :762–:794, linear = geometric :804, example beats its bound :840) | 38–47 | opt02-convexity-gd/opt02-convexity-gd.html:699 |
| 06 | Three Guarantees (assumptions → guarantees table :864, no extra conditions needed :877) | 48–50 | opt02-convexity-gd/opt02-convexity-gd.html:857 |
| — | End slide x_{t+1} = x_t − ∇f(x_t)/L | 51 | opt02-convexity-gd/opt02-convexity-gd.html:903 |

Key results (cited by name on-slide): **descent lemma** (opt02-convexity-gd/opt02-convexity-gd.html:267), proved in three
steps; **nonconvex rate** min_t ‖∇f(x_t)‖² ≤ 2L(f(x_0) − f_low)/T (opt02-convexity-gd/opt02-convexity-gd.html:399);
**convex O(1/T)**, Garrigos & Gower 2024 Thm 3.4 (opt02-convexity-gd/opt02-convexity-gd.html:604); **strongly convex
geometric rate**, Garrigos & Gower 2024 Thm 3.6 (opt02-convexity-gd/opt02-convexity-gd.html:752). All three proved
on-slide by one distance/descent argument; no co-coercivity, no PL.
Figures: inline SVG; S95/S65/S110 generated by
`opt02-convexity-gd/figs/o3b_figs.py`.

### opt01-svd-lowrank-full — Full / extended edition (119 slides; backup, `opt03-backup/`)

`opt03-backup/opt01-svd-lowrank-full.html` · the pre-2026-11-23
lecture, archived unchanged apart from paths and the title (rank/range/null,
four subspaces, norms, SVD, pseudo-inverse, spectral/Frobenius/nuclear norms,
Eckart–Young–Mirsky, Netflix/matrix completion; bridge to least squares).
Slide IDs S01–S119 in baseline order; an Snn in the main deck is the same slide.

Companion: `opt03-backup/opt01-svd-lowrank-full-note.html` — one article per slide, the full legacy note.
Accessible edition: `opt03-backup/opt01-svd-lowrank-full-note.md` (1248 lines).

### opt03-convexity-gd-full — Full / extended edition (134 slides; backup, `opt03-backup/`)

`opt03-backup/opt03-convexity-gd-full.html` · the pre-2026-11-23
lecture, archived unchanged apart from paths and the title (convexity,
Hessian tests, L-smoothness, descent lemma, sandwich, co-coercivity, strong
convexity, PL, GD convergence with both rates, step-size cliff at 2/L).
Slide IDs S01–S134 in baseline order.

Companion: `opt03-backup/opt03-convexity-gd-full-note.html` — one article per slide, the full legacy note.
Accessible edition: `opt03-backup/opt03-convexity-gd-full-note.md` (1262 lines).

### opt02-regression-erm — Linear Regression, ERM & Ridge (110 slides; backup, `opt03-backup/`)

`opt03-backup/opt02-regression-erm.html` · **opt 436–794 + 1463–1517**
(least squares, feature maps, multi-output, ERM/Bayes risk, ridge merged in).
Historical Lecture 11 (backup in 2026, not taught) — answers opt01's bridge (x = A†b, proof delivered as the deck
centerpiece); recalls opt01 compact SVD / pseudo-inverse / rotations-are-free /
orthogonal split as technique reviews, prob05 LLN, prob06 ERM +
approximation/estimation split, prob07 MMSE / MAP / bias–variance, prob08
symmetric-eigenvalue facts by name without re-proving. Running example
(−1,0), (0,1), (1,3) carried through SVD by hand → θ\*=(4/3, 3/2), SSE=1/6 →
normal equations → orthogonality check → feature map (exact fit) → ridge
θ_λ=(4/(3+λ), 3/(2+λ)) with the λ=1 crossing. Ends bridging to opt03
(convexity + gradient descent).

Companion: `opt03-backup/opt02-regression-erm-note.html` — detailed definitions, expanded proofs, lemmas, references.
Accessible edition: `opt03-backup/opt02-regression-erm-note.md` — screen-reader Markdown edition of that note (467 lines): plain ASCII, LaTeX math, figures replaced by verbal descriptions, self-contained (no references to the slides).

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + TOC | 1–2 | opt03-backup/opt02-regression-erm.html:44 |
| 01 | Why Regression? (the pseudo-inverse explained :152, simplest trainable model, today's three results cards :192, route map SVG :215) | 3–7 | opt03-backup/opt02-regression-erm.html:144 |
| 02 | Linear Regression (data :279, linear model, height-weight SVG :303, dummy feature :335, interpretability, squared loss :359, training problem :371, running 3-point example + scatter SVG :383) | 8–16 | opt03-backup/opt02-regression-erm.html:271 |
| 03 | Matrix Form (stack the data :433, one objective one norm :446, tall/square/fat SVG :455, regression = tall case, running example has no exact solution :490, best we can do :504) | 17–23 | opt03-backup/opt02-regression-erm.html:425 |
| 04 | The Least-Squares Theorem (technique reviews 1–4: compact SVD :523, pseudo-inverse :538, rotations free :553, vector split :567; Thm 1 :582, reading :595, 5-step proof overview :607, Steps 1–5 one idea per slide :620–:685, every minimizer + smallest :696, uniqueness :709, proof-summary skeleton :720, key trick named :735, worked SVD :748, worked A† and θ\* :759, worked fitted line + residual table :773, implications :819, :833) | 24–46 | opt03-backup/opt02-regression-erm.html:515 |
| 05 | Geometry & Normal Equations (range(A) :853, projection picture SVG :866, solution is a projection AA†=U_cU_cᵀ :890, residual orthogonal :904, TR gradients of quadratics :918, Thm 2 :931, expansion proof both directions :944–:958, two formulas one answer (AᵀA)⁻¹Aᵀ=A† :972, worked normal equations :987, worked perpendicular check :999, which route when :1011) | 47–59 | opt03-backup/opt02-regression-erm.html:845 |
| 06 | Feature Maps (bend the model (tex log/x/x² example) :1033, feature map def :1045, worked add x² :1058, worked elimination, exact fit :1072, line-vs-parabola SVG :1084, more features never hurt training :1127, feature engineering → learning :1140) | 60–67 | opt03-backup/opt02-regression-erm.html:1025 |
| 07 | Multi-Output Regression (vector labels :1162, objective splits by output :1175, m independent regressions Θₖ=A†Bₖ :1186, linear layer implication :1200) | 68–72 | opt03-backup/opt02-regression-erm.html:1154 |
| 08 | Empirical Risk Minimization (one frame :1219, recall prob06 card :1230, loss def :1243, two classic losses + SVG :1255, predictions vs label space (prob02 CE recall) :1282, expected risk :1294, Bayes risk & predictor :1309, f\*=E[Y\|X] via prob07 MMSE :1323, empirical risk + prob05 LLN :1335, approximation-vs-estimation SVG :1348, least squares is ERM table :1373, when ERM backfires :1388) | 73–85 | opt03-backup/opt02-regression-erm.html:1211 |
| 09 | Ridge Regression (fragile predictors :1410, Cauchy–Schwarz sensitivity :1421, regularizer def (tex ℓ1 typo fixed) :1433, regularized ERM :1446, Thm 3 :1458, reading (no rank condition) :1470, TR eigenvalue shift (prob08 recall) :1481, Lemma AᵀA+λI invertible :1494, proof overview :1508, Step 1 gradient :1520, Step 2 strict win :1531, proof summary :1545, ridge through SVD shrinkage :1558, λ→0⁺ = A†B answers least-norm teaser :1571, worked ridge :1584, turning-the-dial table + coefficient-vs-λ chart :1595, worked three fits SVG :1633, underfit/just-right/overfit panels :1667, ridge = MAP prior (prob07) :1702, what λ buys (bias–variance, validation) :1713) | 86–106 | opt03-backup/opt02-regression-erm.html:1402 |
| — | Closing: every-tool table with the one-chain line folded in, bridge to iterative methods, end slide θ\*=A†B | 107–110 | opt03-backup/opt02-regression-erm.html:1727 |

Key theorems: **Thm 1** least-squares solution θ\* = A†B minimizes ‖Aθ−B‖₂²
and is the least-norm minimizer, full 5-step SVD proof (insert SVD + complete
basis, rotate residual, drop constant, split θ, solve surviving piece)
(opt03-backup/opt02-regression-erm.html:582); **Thm 2** normal
equations AᵀAθ̂ = AᵀB characterize minimizers, expansion proof in both
directions, (AᵀA)⁻¹Aᵀ = A† under full rank
(opt03-backup/opt02-regression-erm.html:931); **Lemma** AᵀA + λI is
invertible for every A and λ > 0, eigenvalue-shift argument
(opt03-backup/opt02-regression-erm.html:1494); **Thm 3** ridge closed
form θ\*_λ = (AᵀA+λI)⁻¹AᵀB, unique for any A, gradient + strict-verification
proof (opt03-backup/opt02-regression-erm.html:1458).
Figures: 12 inline SVGs with hand-computed geometry (route map,
height-weight sketch, running-example scatter, tall/square/fat block shapes,
fitted line + residuals, projection of B onto range(A) with right-angle marker,
line-vs-parabola fit, quadratic-vs-absolute loss curves,
approximation-vs-estimation map, coefficient-vs-λ decay chart with the λ=1
crossing, three-fits comparison, underfit/just-right/overfit 3-panel). Every
label is a KaTeX `<span class="fl">` absolutely positioned over the SVG via the
`.o2-fig` wrapper (KaTeX cannot typeset inside SVG `<text>`), so figure text is
real math at 1.55rem / 1.25rem regardless of the SVG scale; the four scatter
plots share one 500×320 viewBox and one coordinate map x→250+110x, y→240−55y.
Deviations from tex: opt 500 y{(1)} → y^{(1)}; opt 538 U ∈ R^{n×n} → R^{N×N};
opt 573 mismatched parenthesis fixed; opt 605 Θ dimension "n×m" → m×n; opt 611
θ_k x → θ_kᵀx; opt 615 ‖·‖² on scalar residuals → (·)²; opt 1498 ℓ1
regularizer formula (duplicated the ℓ2 formula) fixed to Σ\|θᵢ\|; opt 1513
ridge exercise's full-rank assumption dropped (invertibility proved for any
A); spelling fixes silently (Typlically). Added beyond the tex per mandate:
Thm 2 normal equations + proof (tex states least squares only via SVD),
AA† = U_cU_cᵀ projection derivation, ridge-through-SVD shrinkage
σᵢ/(σᵢ²+λ), the λ→0⁺ → A†B limit, Bayes predictor under squared loss
= E[Y\|X] via prob07 MMSE recall, and all worked numeric examples above (the
tex sets up the running objects but computes none of them).

### opt04-sgd — Stochastic Gradient Descent (117 slides; backup, `opt03-backup/`)

`opt03-backup/opt04-sgd.html` · **opt 1320–1462, 1520–1600** (SGD setup,
unbiasedness, full O(1/√K) convex proof for the averaged iterate,
mini-batch 1/b variance, strongly-convex SGD O(log k/k) with decreasing
steps). Historical Lecture 13 (backup in 2026, not taught), written as the course finale: answers the cost problem left by
gradient descent (full gradients cost N backprops; sample one instead and
pay with variance). Every borrowed tool — tangent floor, telescoping,
unrolling, uniform expectation, Jensen, variance of averages, tower — is
restated on its own Technique Review card as self-contained content, with
no deck-id citations on any slide (style rule 10); provenance is recorded
here only. Per Albert's request, operator theory,
Nesterov/acceleration, and GDM/RMSprop/Adam math are all dropped —
momentum/RMSprop/Adam appear as one names-only slide. Running example
L_i(θ) = ½(θ − c_i)², c = (0, 3, 6) (θ* = 3, σ² = 6 at every θ) carried
through: full gradient by hand → sampled spread {0,−3,−6} at θ=0 → four
SGD steps at α = ½ (draws 6,0,3,6: θ = 3, 1.5, 2.25, 4.125) vs GD → same
draws at α = 0.1 → noise floors 2.0 vs 0.316 → Thm 2 constants G²+σ² = 42,
D = 3, bound 19.44/√(K+1) → b=1 vs b=3 variance 6 vs 2 (27 triples) →
strongly-convex rewrite L = f + ½θ² (μ=1, G=3), schedule 1/(k+1) makes the
iterate the running average of sampled c's → bound 30(1+log(k+1))/(k+1)
vs Thm 2, crossover ≈ 300 (solve 30(1+log(k+1))/(k+1) = 11.62/√(k+1); the
old "≈ 10³" read the decade spacing of the worked table, not the switch
point — the note's §7.7 gives k ≈ 299). Closes the whole course: 13-deck
map, what-you-can-now-read, end slide θ_{k+1} = θ_k − α g_k.

Companion: `opt03-backup/opt04-sgd-note.html` — detailed definitions, expanded proofs, lemmas, references.
Accessible edition: `opt03-backup/opt04-sgd-note.md` — screen-reader Markdown edition of that note (681 lines): plain ASCII, LaTeX math, figures replaced by verbal descriptions, self-contained (no references to the slides).

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + TOC | 1–2 | opt03-backup/opt04-sgd.html:50 |
| 01 | Why SGD? (bill for one GD step :158, N is millions :169, sample-don't-sum :192, four results :207, route map SVG :231) | 3–8 | opt03-backup/opt04-sgd.html:150 |
| 02 | The Finite-Sum Objective (ERM :262, GD priced :274, running example :286, three-parabolas SVG :300, full gradient by hand :328, the gap :345) | 9–15 | opt03-backup/opt04-sgd.html:254 |
| 03 | The Stochastic Gradient (algorithm box :364, three-candidates SVG :378, TR uniform expectation (from prob01) :407, Thm 1 unbiasedness :420 + proof :433, worked check table :447, unbiased ≠ zero :464, truth + noise σ²=6 :479, epochs remark :492) | 16–25 | opt03-backup/opt04-sgd.html:356 |
| 04 | SGD by Hand (α=½ midpoint step :511, run table :523, GD comparison :541, two-paths SVG :562, 2-D companion :595, contour SVG :608, reading the picture :649, averaged iterate θ̄₄ = 2.175 :670) | 26–34 | opt03-backup/opt04-sgd.html:503 |
| 05 | Noise vs Progress (α=0.1 table :695, error recursion :716, mean dies/variance survives :730, noise floor ασ²/(2−α) table :743, racing-to-floors SVG :762, step-size dial :791, three escape plans :812) | 35–42 | opt03-backup/opt04-sgd.html:687 |
| 06 | The O(1/√K) Theorem (E_k notation :843, variance assumption honestly :856, bounded gradients :869, running constants :886, Thm 2 :899, reading :914, overview :927, Steps 1–9 one idea/slide :943–:1155 with TRs tangent floor :973, tower :1019, telescoping :1046, balance :1085, Jensen :1141 interleaved; one-step inequality read :1005, balance U-curve SVG :1112, skeleton :1170, worked bound table :1186, GD-vs-SGD total work :1205, average-vs-last remark :1224) | 43–69 | opt03-backup/opt04-sgd.html:835 |
| 07 | Mini-Batching (update :1249, still unbiased :1261, TR variance of averages (from prob05) :1273, Thm 3 :1287 + proof :1300, b=1 vs b=3 worked :1311, histogram SVG :1328, full-batch corner :1364, what b buys :1381, GPU price :1395, choosing b :1416) | 70–81 | opt03-backup/opt04-sgd.html:1241 |
| 08 | Strongly Convex SGD (regularized problem :1436, kill-the-floor schedule :1448, running example rewritten :1461, Thm 4 :1473, reading :1486, overview :1499, TR unrolling :1513, Steps 1a/1b weights = 1/(k+1) :1525–:1538, worked running average :1551 + table :1561, TR splitting square :1579, Steps 2a/2b :1591–:1604, TR strong floor :1617, Steps 3a/3b contraction :1631–:1645, Step 4 schedule :1659, Step 5a weighted telescope a₀=0 :1672, TR harmonic sum + integral SVG :1685, Step 5b :1718, Step 6 Jensen :1731, skeleton :1744, log-removable remark :1759, worked bound table :1771, log-log rates SVG :1790) | 82–108 | opt03-backup/opt04-sgd.html:1428 |
| 09 | In Practice (recipe table :1826, proved-vs-run honesty :1844, descendants names only :1862) | 109–112 | opt03-backup/opt04-sgd.html:1818 |
| 10 | Closing the Course (every-tool table :1894, 13-deck course map SVG :1913, what you can now read :1967, end slide θ_{k+1} = θ_k − α g_k :1987) | 113–117 | opt03-backup/opt04-sgd.html:1886 |

Key theorems: **Thm 1** unbiasedness E[∇L_{i_k}(θ)] = ∇L(θ), two-line
proof via uniform expectation (opt03-backup/opt04-sgd.html:420); **Thm 2**
convex SGD O(1/√K): with α = D/(√(G²+σ²)√(K+1)), E[L(θ̄_K) − L*] ≤
√(G²+σ²)·D/√(K+1) for the averaged iterate — full 9-step proof
(opt03-backup/opt04-sgd.html:899); **Thm 3** mini-batch variance σ²/b for
i.i.d. with-replacement batches, proved via the variance of an average
(opt03-backup/opt04-sgd.html:1287); **Thm 4** strongly convex SGD with
α_k = 1/(μ(k+1)): E[F(x̄_k) − F(x*)] ≤ (2(G²+σ²)/μ)·(1+log(k+1))/(k+1) —
full 6-step proof via unrolling, weighted telescope with vanishing head,
harmonic sum (opt03-backup/opt04-sgd.html:1473).
Figures: ten inline SVGs, all rebuilt in the 2026-09 pass on the
KaTeX-over-SVG overlay pattern — the `.o4-fig` wrapper (CSS at
opt03-backup/opt04-sgd.html:25) is `position:relative; align-self:start`,
the SVG carries shapes only (zero `<text>`), and every label is an
absolutely positioned `<span class="fl">` at left = x/W, top =
(y − minY − 6)/H, so math renders through KaTeX at a fixed 1.55rem
(annotations `.fl-sub`, 1.25rem) regardless of the SVG's scale factor. A
caption `<p>` must stay *outside* the wrapper or every percentage top
drifts. Each figure carries an HTML comment recording its coordinate map,
and each map was re-derived from the algebra it depicts: route map;
three parabolas + average (L_i = (x−c_i)², X = 105+45x, Y = 292−11v);
three-candidates number line; SGD-vs-GD iterate paths (Y = 300−60x, the
two recursions written out); 2-D contours with midpoint-exact paths at
26 px/unit (outermost r=208 ring dropped — it collided with the legend);
racing-to-different-floors from m_{k+1} = (1−α)²m_k + 6α², floors
6α/(2−α) = 2.0 and 0.3158; balance-point U-curve for 0.045/α + 21α
(progress green, noise red, so the two dashed curves are told apart by
colour, not by label proximity); b=1 vs b=3 histogram on a shared
540 px-per-unit-probability scale; harmonic-sum integral boxes;
log–log rate comparison (Thm 4 vs Thm 2, crossing at k ≈ 300);
13-deck course map, its 9-wide probability row split 5+4 so every label
fits at ≥1.25rem.
Deviations from tex: tex's Lipschitz constant L renamed G (clash with
the smoothness constant L of the previous lecture; noted on-slide); Thm 4
stated for E[F(x̄_k) − F(x*)]
with F = f + (μ/2)‖x‖² (tex writes f and omits the expectation); tex
1435/1446 final-constant typo (√(L²+σ²) misplaced) corrected to
√(G²+σ²)·D/√(K+1); tex 1582–1583 average /k corrected to /(k+1); index
inconsistency at tex 1426/1432 resolved (θ_{K+1} after summing k=0..K);
tex 1363 I_k ∈ → I_k ⊆; tex 1375's garbled mini-batch sentence rendered
as variance ÷b / compute ×b / GPU parallelism; spelling typos fixed
silently (convditional, bith, miminzer). Honesty caveats on-slide: the
quadratic running example is not globally Lipschitz (G = 6 valid on the
interval the run lives in); bounded variance labeled an assumption.
Added beyond the tex per mandate: noise-floor recursion v∞ = ασ²/(2−α)
with numeric floors 2.0/0.316; the 2-D contour companion; GD-vs-SGD total
work O(N/ε) vs O(1/ε²) table; balance U-curve; b=1/b=3 histogram
enumeration; θ_i = 1/(k+1) running-average simplification of the unrolled
weights; harmonic-sum technique review with integral picture; Thm 2 vs
Thm 4 worked bound comparison (crossover ≈ 300); and all worked numeric
tables (the tex sets up the running example but computes none of the
runs).
2026-09 revision: the closer's equation-chain slide ("Today, as One
Chain") was folded into the every-tool table per DESIGN_SYSTEM §2 (one
closing summary, the other's takeaway as a single muted line), taking the
deck from 118 to 117 slides.

### midterm26-review — Midterm Solutions: Tools for Seeing (74 slides)

`midterm26-review/midterm26-review.html` · solution lecture for `exam/midterm26.tex` (exam 2026-10-20). Theme
(Albert, 2026-10-22): entropy / MI / KL and the inequalities are tools for understanding phenomena —
every problem gets its motivation and intuition before the computation. Built by
a generator script (not committed); no tech supplement.

Companion: `midterm26-review/midterm26-review-note.html` (§1–9 + refs [1]–[6]) — full solutions in prose, the derivations the slides compress (asymptotic H(K), label-W bounds with equality cases, general I(ε) formula, n=3 shuffle matrix and exact distributions, δ-move, e^t=7 optimality), all numbers re-derived. Generated from the accessible edition `midterm26-review/midterm26-review-note.md` (829 lines; same text and sections, LaTeX math, tables as lists).

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title | 1 | midterm26-review/midterm26-review.html:52 |
| 01 | Why This Course (why learn tools: learn → apply → see loop; you will keep learning tools (this course → later → after graduation); two layers: tools vs phenomena SVG, tools are weapons) | 2–8 | midterm26-review/midterm26-review.html:63 |
| 02 | Problem 1 (1(a) count vs position, chain rule, bound H(K) ≤ log(n+1) instead of computing it (exact vs bound table n=10/100/1000), 6.66 vs 93.3 bits bar; 1(b) derivation h(Z)=h(Z|W)+I(Z;W), the extra bit is the label; 1(c) label channel, always-lie ε=1 still informative (0.415 bits for K=4), I-vs-ε plot K=2/K=10, useless iff ε=(K−1)/K; 1(d) top-to-random shuffle (itemized move), doubly stochastic but not symmetric 6×6 matrix, repeat the move: any start → uniform (n=3 bars after 0/1/2/5 moves)) | 9–31 | midterm26-review/midterm26-review.html:176 |
| 03 | Problem 2 (CE over-confidence, design challenge, label smoothing vs confidence penalty, 2(a) from the L_LS definition to KL forms D(u‖q) vs −D(q‖u) (Pereyra et al.), 2(b) limits from the definitions, limits table + penalty plot K=2, 2(c) behaviour near one-hot (δ-move: −log(1−δ)=O(δ), H(q)∼δlog(1/δ)), consequences (Müller et al.), lesson) | 32–48 | midterm26-review/midterm26-review.html:550 |
| 04 | Problem 3 (light tails: Gaussian tail table, why the mean works; heavy tails x^-3 vs Gaussian log plot, where they live (wildfires, earthquakes, wealth — Clauset et al.; SGD gradient noise — Simsekli et al.), 1/n³ vs e^(-an) table; 3(a) finite variance, infinite MGF; 3(b) one big sample lower bound; median of means algorithm, one outlier spoils one vote, 3(c)(i)–(iv) exponential bound (√7/4)^k, each with its Show statement; numbers table; 3(d); robust estimation (Lugosi–Mendelson, Yin et al.)) | 49–71 | midterm26-review/midterm26-review.html:798 |
| 05 | Takeaways (what we expect, closer) | 72–74 | midterm26-review/midterm26-review.html:1123 |

