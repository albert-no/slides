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
| 2 | `prob02-kl-crossentropy/` — mismatch thm, KL ≥ 0, horse racing, CE loss = KL to one-hot | prob 249–538 | done (69 slides) |
| 3 | `prob03-mutual-information/` — joint/cond entropy, MI, DPI I–III, cond MI, differential entropy, MaxEnt Gaussian | prob 539–1210 | done (127 slides) |
| 4 | `prob04-random-processes/` — Markov processes, stationary dist., discrete diffusion | prob 1211–1455 | done (99 slides) |
| 5 | `prob05-concentration/` — Markov/Chebyshev/Chernoff, MGF, CLT sketch, LLN | prob 1457–1595 | done (107 slides) |
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

### prob02-kl-crossentropy — KL Divergence & Cross-Entropy Loss (69 slides)

`prob02-kl-crossentropy/prob02-kl-crossentropy.html` · source: prob 249–538.
Lecture 2 — answers prob01's teaser (wrong distribution Q); recalls entropy/Jensen
from prob01 instead of redefining; ends on a bridge to prob03 (two RVs → mutual
information).

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + TOC | 1–2 | prob02-kl-crossentropy/prob02-kl-crossentropy.html:20 |
| 01 | Why Cross-Entropy? (PyTorch CE loss, derive-not-accept, route map SVG) | 3–6 | prob02-kl-crossentropy/prob02-kl-crossentropy.html:91 |
| 02 | Recall & Teaser (surprisal/entropy + Jensen recall from prob01, E[log 1/Q] ≟ H(X)) | 7–11 | prob02-kl-crossentropy/prob02-kl-crossentropy.html:155 |
| 03 | The Mismatch Theorem (Thm 1 arc: 3-step proof, equality, edge-case exercise, H(P,Q) def :375, gap-axis picture) | 12–24 | prob02-kl-crossentropy/prob02-kl-crossentropy.html:221 |
| 04 | KL Divergence (def :423, P-vs-Q bars SVG, worked D(P‖Q)=0.224 ≠ D(Q‖P)=0.296, Thm 2, CE = H + KL) | 25–34 | prob02-kl-crossentropy/prob02-kl-crossentropy.html:411 |
| 05 | Gambling & Doubling Rate (red/black, all-in ruin, E[log S], Thm 3, doubling rate :689, horse race, Thm 4, 3-horse worked example, three-gamblers table) | 35–51 | prob02-kl-crossentropy/prob02-kl-crossentropy.html:554 |
| 06 | Cross-Entropy Loss (classifier pipeline SVG, CE loss def, 3-class worked table, one-hot pmf, Thm 5–6, soft labels, min CE = min KL) | 52–66 | prob02-kl-crossentropy/prob02-kl-crossentropy.html:818 |
| — | Recap chain, bridge to prob03, end slide | 67–69 | prob02-kl-crossentropy/prob02-kl-crossentropy.html:1043 |

Key theorems: **Thm 1** mismatch H(X) ≤ E[log 1/Q(X)], equality iff Q = p_X
(prob02-kl-crossentropy/prob02-kl-crossentropy.html:259); **Thm 2** information
inequality D(P‖Q) ≥ 0 (prob02-kl-crossentropy/prob02-kl-crossentropy.html:507);
**Thm 3** proportional betting, binary (prob02-kl-crossentropy/prob02-kl-crossentropy.html:653);
**Thm 4** proportional betting, M horses, W = log M − H(p) − D(p‖Q)
(prob02-kl-crossentropy/prob02-kl-crossentropy.html:757); **Thm 5** CE loss =
D(one-hot ‖ f(x)) (prob02-kl-crossentropy/prob02-kl-crossentropy.html:946);
**Thm 6** H(P,Q) = H(P) + D(P‖Q) (prob02-kl-crossentropy/prob02-kl-crossentropy.html:972).
Figures: figs/jensen.png (Jensen recall), figs/classification.png (classifier setup);
all other diagrams inline SVG. Worked numeric examples (3-outcome KL asymmetry,
3-horse race / three-gamblers, 3-class CE, soft labels) computed for this deck —
not in the tex — per worked-example mandate. Rigorous p_X(x) = 0 edge case left
as a hinted exercise (commented out in the tex too).

### prob03-mutual-information — Mutual Information & Data Processing (127 slides)

`prob03-mutual-information/prob03-mutual-information.html` · source: prob 539–1210.
Lecture 3 — answers prob02's teaser (two RVs); recalls entropy from prob01 and KL
from prob02 instead of redefining; ends on a bridge to prob04 (sequences in time →
Markov processes).

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + TOC | 1–2 | prob03-mutual-information/prob03-mutual-information.html:23 |
| 01 | Why Mutual Information? (layer = channel SVG, questions we can't ask yet, "information only decays" preview, route map) | 3–7 | prob03-mutual-information/prob03-mutual-information.html:99 |
| 02 | Joint Random Variables (joint pmf, running 2×2 table :225, marginals, conditional pmf, independence, random vectors, supervised learning = joint dist.) | 8–18 | prob03-mutual-information/prob03-mutual-information.html:201 |
| 03 | Joint & Conditional Entropy (H(X,Y) :363, Thm 1 additivity arc, guessing game returns :487, H(Y\|X) :540, Thm 2 chain rule, Thm 3 DPI I arc) | 19–45 | prob03-mutual-information/prob03-mutual-information.html:354 |
| 04 | Mutual Information (def :746, Venn diagram SVG :762, I(X;X), independence case, KL form :836, Thm 4 symmetry, Thm 5 I ≥ 0 arc, MI in AI) | 46–61 | prob03-mutual-information/prob03-mutual-information.html:737 |
| 05 | Data Processing (Thm 6 DPI II arc, Markov chains :1025, Thm 7 DPI III, layers only forget, cond. MI :1134, XOR triple counterexample :1164, chain rule for I) | 62–82 | prob03-mutual-information/prob03-mutual-information.html:961 |
| 06 | Differential Entropy (densities, change of variables, KL for densities, bins SVG :1390, Thm 8 discretization, h def :1461, exhibits 1–3 (negative h, no label invariance, scaling), Gaussian h, Thm 9–12) | 83–110 | prob03-mutual-information/prob03-mutual-information.html:1272 |
| 07 | Maximum Entropy (discrete recall, bounded-support exercise, variance budget, Thm 13 MaxEnt Gaussian full arc, why Gaussians are everywhere) | 111–123 | prob03-mutual-information/prob03-mutual-information.html:1676 |
| — | Recap chain, DPI-family recap, bridge to prob04, end slide | 124–127 | prob03-mutual-information/prob03-mutual-information.html:1853 |

Key theorems: **Thm 1** additivity H(X,Y) = H(X) + H(Y) under independence
(prob03-mutual-information/prob03-mutual-information.html:414); **Thm 2** chain rule
H(X,Y) = H(X) + H(Y|X) (prob03-mutual-information/prob03-mutual-information.html:601);
**Thm 3** DPI I: H(f(X)) ≤ H(X) (prob03-mutual-information/prob03-mutual-information.html:671);
**Thm 4** symmetry I(X;Y) = I(Y;X) (prob03-mutual-information/prob03-mutual-information.html:868);
**Thm 5** I(X;Y) ≥ 0 (prob03-mutual-information/prob03-mutual-information.html:883);
**Thm 6** DPI II: I(X; f(Y)) ≤ I(X;Y) (prob03-mutual-information/prob03-mutual-information.html:973);
**Thm 7** DPI III on Markov chain X−Y−Z (prob03-mutual-information/prob03-mutual-information.html:1067);
**Thm 8** discretization H(X^Δ) = h(X) − log Δ (prob03-mutual-information/prob03-mutual-information.html:1439);
**Thm 9** scale invariance I(aX;Y) = I(X;Y) (prob03-mutual-information/prob03-mutual-information.html:1592);
**Thm 10** chain rule for h (prob03-mutual-information/prob03-mutual-information.html:1630);
**Thm 11** independence iff I = 0, continuous (prob03-mutual-information/prob03-mutual-information.html:1645);
**Thm 12** DPI continuous (prob03-mutual-information/prob03-mutual-information.html:1657);
**Thm 13** Gaussian maximizes h under a variance budget
(prob03-mutual-information/prob03-mutual-information.html:1728).
Figures: figs/binary_image.png (supervised-learning slide); all other diagrams inline
SVG (layer-as-channel pipeline, entropy Venn diagram, Markov chain boxes,
bins-under-density, same-variance density comparison). XOR triple and guessing-game
examples are the tex's own; the running 2×2 joint-pmf table and its per-theorem
worked checks are not in the tex — added per worked-example mandate. Venn diagram
and pipeline SVGs added per visual mandate.

### prob04-random-processes — Random Processes & Markov Chains (99 slides)

`prob04-random-processes/prob04-random-processes.html` · source: prob 1211–1455.
Lecture 4 — answers prob03's teaser (sequences in time); recalls the chain rule of
probability from prob03 instead of redefining; ends on a bridge to prob05 (averages
of many draws → concentration).

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + TOC | 1–2 | prob04-random-processes/prob04-random-processes.html:32 |
| 01 | Why Sequences? (LM / diffusion / random-walk cards, one snapshot not enough, settling preview, route map) | 3–7 | prob04-random-processes/prob04-random-processes.html:124 |
| 02 | Random Processes (def, i.i.d. process, coin flips, "my na_e is Albert" text example, modeling spectrum) | 8–13 | prob04-random-processes/prob04-random-processes.html:216 |
| 03 | Markov Processes (memory-one idea, random walk example :335, 1st-order def :374, chain-rule recall (prob03) :390, factorization proposition + proof :406, kth-order def :449, next-token models, refined spectrum) | 14–26 | prob04-random-processes/prob04-random-processes.html:301 |
| 04 | Transition Matrices (prob-vector + matrix×vector reviews, P def :562, column sums, π_i def :591, Thm 1 arc, binary chain :658, three-state chain :728) | 27–43 | prob04-random-processes/prob04-random-processes.html:513 |
| 05 | Evolution in Time (Thm 2 π_t = P^t π_0 + proof, numeric evolution table :815, convergence chart :832, "distribution that does not move?" teaser) | 44–49 | prob04-random-processes/prob04-random-processes.html:780 |
| 06 | Stationary Processes (def :881, sliding-window picture, random-walk counterexample + fan-out, Markov vs. stationary axes, full spectrum) | 50–56 | prob04-random-processes/prob04-random-processes.html:873 |
| 07 | Stationary Distributions (three-state worked stationary example :1025, pinned start fails :1099, Thm 3 existence :1115, assumptions in pictures, binary worked, π* def :1184, eigen reviews :1199, eigen computations by hand :1244, symmetric-P exercise + solution :1310, random surfer) | 57–77 | prob04-random-processes/prob04-random-processes.html:1017 |
| 08 | Limiting Distributions (π_∞ def :1381, α=1 no-limit caveat, Thm 4 arc, rate via second eigenvalue :1451) | 78–86 | prob04-random-processes/prob04-random-processes.html:1373 |
| 09 | Discrete Diffusion (destroy-then-rebuild, ε-noising matrix :1515, sanity checks, uniform limit, data-dissolves picture :1554, denoiser f_θ, backwards generation, why it works) | 87–95 | prob04-random-processes/prob04-random-processes.html:1492 |
| — | Recap chain, running-examples recap, bridge to prob05, end slide | 96–99 | prob04-random-processes/prob04-random-processes.html:1646 |

Key theorems: **Prop.** Markov factorization P(x^n) = Π P(x_i|x_{i−1}) with proof
(prob04-random-processes/prob04-random-processes.html:406); **Thm 1** one-step
evolution π_i = P π_{i−1}, full arc overview/proof/summary
(prob04-random-processes/prob04-random-processes.html:604); **Thm 2** t-step
evolution π_t = P^t π_0 (prob04-random-processes/prob04-random-processes.html:788);
**Thm 3** existence of a stationary initial distribution under finite-state +
irreducible + aperiodic, stated without proof as in the tex
(prob04-random-processes/prob04-random-processes.html:1115); **Thm 4** limiting ⟹
stationary, with limit-both-sides proof
(prob04-random-processes/prob04-random-processes.html:1411).
Figures: all diagrams inline SVG — binary/three-state chain graphs, sliding window,
random-walk fan-out, modeling spectrum, noising pixel-grid sequence; the tex's
scribe12-markovex.png and scribe12-distribution.png are redrawn as SVG (noted on
the slides). Deviations from tex: the tex's duplicated/contradictory binary-chain
conditionals (p(1|0)=α and p(1|0)=1−α, prob 1297/1391) fixed to flip-α / stay-(1−α);
the tex's π_t vs π_i index mismatch (prob 1281) normalized to π_i. Added beyond the
tex per mandate: proofs for Thm 1/2, eigenvalue technique review + by-hand eigen
solutions of both running chains, symmetric-P exercise solution, convergence-rate
slides (second eigenvalue), numeric evolution table/chart, and the diffusion
forward/backward picture slides.

### prob05-concentration — Concentration Inequalities & the Law of Large Numbers (107 slides)

`prob05-concentration/prob05-concentration.html` · source: prob 1457–1595.
Lecture 5 — answers prob04's teaser (averages of many draws); recalls expectation/
variance from prob01 and independence from prob03 instead of redefining; one running
example (mean of n fair coin flips, Pr(X̄_n ≥ 3/4)) is re-answered by every bound;
ends on a bridge to prob06 (tail bounds uniform over a hypothesis class → Hoeffding
+ union bound).

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + TOC | 1–2 | prob05-concentration/prob05-concentration.html:23 |
| 01 | Why Averages? (minibatch loss / test accuracy / Monte Carlo cards, how-many-samples question, three-bounds preview, route map SVG) | 3–8 | prob05-concentration/prob05-concentration.html:115 |
| 02 | Warm-Up (expectation :237 / variance :253 recall from prob01, independence recall from prob03, product-rule proof, variance adds, coin running example :313, why not just compute it) | 9–16 | prob05-concentration/prob05-concentration.html:229 |
| 03 | Markov's Inequality (indicator technique :349, Thm 1 arc: statement :386, threshold form :398, 3-step proof, coin answer 0.67, tightness example :493, what it buys) | 17–29 | prob05-concentration/prob05-concentration.html:341 |
| 04 | Chebyshev's Inequality (squaring technique, Thm 2 arc, ασ-rule table :626, Var(X̄_n)=σ²/n :642, coin answer, Markov-vs-Chebyshev 4/n chart :675, 50,000-samples computation :698) | 30–42 | prob05-concentration/prob05-concentration.html:521 |
| 05 | Law of Large Numbers (convergence-in-probability def :718 + picture, Thm 3 arc, sample-path SVG :812, tails-vanish chart :834, where AI leans on it, the-gap teaser :872) | 43–53 | prob05-concentration/prob05-concentration.html:710 |
| 06 | Moment Generating Functions (def :896, moment machine M'(0)/M''(0), Taylor view, Bernoulli MGF :953, Gaussian MGF exercise via completing the square, Thm 4 uniqueness :1038, Prop. sums→products :1053, Gaussian-sum worked, coin-sum MGF :1095) | 54–69 | prob05-concentration/prob05-concentration.html:888 |
| 07 | Chernoff Bound (exponentiating-the-event technique :1142, Thm 5 arc :1166, free parameter t, coin 3-step optimization t*=ln 3 → exponent 0.1308 :1238, KL-exponent view :1278, 18,444-samples revisit :1295, what it buys) | 70–84 | prob05-concentration/prob05-concentration.html:1119 |
| 08 | Three Bounds Head-to-Head (escalation table, numeric table on Pr(X̄_n ≥ 3/4) :1361, log-scale chart :1376, takeaway) | 85–89 | prob05-concentration/prob05-concentration.html:1338 |
| 09 | Central Limit Theorem (shape question, standardization, Thm 6 :1452, sketch scope caveat, Taylor-at-zero + compound-interest-limit techniques, 3-step MGF sketch, Bin(16,½)-vs-bell chart :1569, what it buys) | 90–103 | prob05-concentration/prob05-concentration.html:1420 |
| — | Recap chain, one-coin-every-tool recap table, bridge to prob06, end slide | 104–107 | prob05-concentration/prob05-concentration.html:1617 |

Key theorems: **Thm 1** Markov Pr(X ≥ αE[X]) ≤ 1/α, non-negative X, full arc
(prob05-concentration/prob05-concentration.html:386); **Thm 2** Chebyshev
Pr(|X−μ| ≥ ασ) ≤ 1/α², full arc (prob05-concentration/prob05-concentration.html:558);
**Thm 3** weak LLN X̄_n → μ in probability, proved via Chebyshev + Var(X̄_n)=σ²/n
(prob05-concentration/prob05-concentration.html:756); **Thm 4** MGF uniqueness,
stated without proof as in the tex
(prob05-concentration/prob05-concentration.html:1038); **Prop.** MGFs turn
independent sums into products
(prob05-concentration/prob05-concentration.html:1053); **Thm 5** Chernoff
Pr(X ≥ α) ≤ M(t)e^{−tα} for all t > 0, full arc
(prob05-concentration/prob05-concentration.html:1166); **Thm 6** CLT, MGF-based
sketch flagged non-rigorous as in the tex
(prob05-concentration/prob05-concentration.html:1452).
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
