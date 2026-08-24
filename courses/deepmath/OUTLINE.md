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
| 6 | `prob06-generalization/` — Hoeffding, sub-Gaussian, union bound, finite-class generalization bound | new material (sequel to prob05) | done (105 slides) |
| 7 | `prob07-estimation/` — cond. expectation/tower, MLE/MAP, Fano (full proof), Naive Bayes, bias-variance, MMSE | prob 1563–1911 | done (126 slides) |
| 8 | `prob08-gaussian/` — MVN (3 defs, properties w/ proofs), Gaussian channel, Gaussian diffusion/DDPM, Gaussian discriminant | prob 1912–2519 (MIT OCW 6.436J citation) | done (131 slides) |
| 9 | `prob09-monte-carlo/` — Monte Carlo, importance sampling, variance trade-offs, policy gradient / RLHF hooks | new material | done (117 slides) |
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

### prob06-generalization — From Concentration to Generalization (105 slides)

`prob06-generalization/prob06-generalization.html` · **new material — not in tex**
(textbook-canonical statements/proofs only; sequel to prob05). Lecture 6 — answers
prob05's bridge (one fixed average → every hypothesis at once); recalls Chernoff/
MGF rules/Gaussian MGF from prob05 by name without re-proving; the prob05 coin
running example (Pr(X̄₁₀₀ ≥ 3/4)) returns to benchmark Hoeffding against Chernoff
2.1×10⁻⁶ and exact 2.8×10⁻⁷; ends on a bridge to prob07 (how to *choose* ĥ →
likelihood, MLE/MAP, bias–variance).

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + TOC | 1–2 | prob06-generalization/prob06-generalization.html:23 |
| 01 | Why Generalization? (train/test/gap cards, setup ℓ(h,z)∈[0,1] :139, true risk R(h) :153, empirical risk R̂_n :166, ERM :179, gap def :193, overfitting U-curve SVG :208, memorizer worked example R̂=0 vs R=1/2 :235, why fixed-h bounds fail for ĥ :245, route map SVG :260) | 3–13 | prob06-generalization/prob06-generalization.html:107 |
| 02 | Recall — the prob05 Toolkit (Chernoff card :300, MGF product/scale rules :315, Gaussian MGF e^{t²σ²/2} :330, what Chernoff needed vs. boundedness-only :345) | 14–18 | prob06-generalization/prob06-generalization.html:292 |
| 03 | Hoeffding's Lemma (goal :368, techniques: bounded-variance lemma Var ≤ (b−a)²/4 + midpoint proof :382, tilted distributions + bar-chart SVG :410, Taylor with Lagrange remainder :453, Thm 1 arc :466, 4-step proof ψ(0)=ψ'(0)=0 / ψ''=tilted variance / cap / integrate :492, proof summary chain :558, ±1 series sanity check (2k)! ≥ 2^k k! :573, any-mean corollary :585, what it buys) | 19–36 | prob06-generalization/prob06-generalization.html:360 |
| 04 | Sub-Gaussian Variables (definition variance proxy :621, Gaussian equality example :633, bounded-variable proxy table :646, Thm 2 tail bound arc :662, Chernoff+envelope+optimize t*=ε/σ² proof :687, two-sided :709, tail-envelope SVG :721, closure rules: scaling c²σ² :744, Prop. sums add proxies + 3-line proof :758, averages σ²/n :782, one-card calculus recap :796) | 37–51 | prob06-generalization/prob06-generalization.html:613 |
| 05 | Hoeffding's Inequality (Thm 3 arc exp(−2nε²/(b−a)²) :820, 3-step assembly proof :833, two-sided workhorse 2e^{−2nε²} :881, proof summary :894, coin returns table vs. prob05 :908, exponent 0.125-vs-0.1308 lesson :925, worked ±2%@95% → n ≥ 4,612 :939, Chebyshev-vs-Hoeffding table 12,500 vs 4,612 :951, what it buys) | 52–64 | prob06-generalization/prob06-generalization.html:812 |
| 06 | The Union Bound (Thm 4 Boole :989, one-line indicator proof :1001, Venn SVG overlap-counted-twice :1012, 10⁴-model farm thought experiment :1036, farm worked example 3.7% :1049, small-test-set vacuous case n=25 :1063, Bonferroni δ/m split :1077, what it buys +ln m :1090) | 65–73 | prob06-generalization/prob06-generalization.html:981 |
| 07 | The Generalization Theorem (finite classes: stumps/quantized nets :1112, risks recall card :1130, fixed h is a coin :1145, the trap ĥ not fixed :1159, the fix G_ε event :1172, Thm 5 arc sup gap ≤ √(ln(2|H|/δ)/2n) :1185, 3-step proof per-h → union → invert :1211, proof summary :1246, ε-tube SVG :1262, ERM corollary R(ĥ) ≤ min R + 2ε :1296, three-hop proof :1308, why-2ε SVG :1323, ln|H| = bits :1354, sample complexity 139/bit :1368, numbers table :1380, chart SVG n ≈ 739+139k :1397, confidence-is-cheap table :1425, VC/Rademacher road ahead (names only) :1441) | 74–95 | prob06-generalization/prob06-generalization.html:1104 |
| 08 | Why ERM Works (license to train :1462, approximation-vs-estimation split :1478, trade-off U-curve SVG :1488, honest slide: ResNet-50 bound vacuous ε ≈ 14.9, open research :1514, what survives: test-set bound |H|=1, validation, leaderboard overfitting :1529) | 96–101 | prob06-generalization/prob06-generalization.html:1454 |
| — | Recap chain, every-tool recap table, bridge to prob07, end slide R(ĥ) ≤ R(h*) + 2ε | 102–105 | prob06-generalization/prob06-generalization.html:1543 |

Key theorems: **Thm 1** Hoeffding's lemma E[e^{tX}] ≤ exp(t²(b−a)²/8) for X∈[a,b],
E[X]=0, full arc via tilted-distribution log-MGF (ψ'' = tilted variance ≤ (b−a)²/4,
Taylor with remainder) (prob06-generalization/prob06-generalization.html:470);
**Thm 2** sub-Gaussian tail Pr(X−μ ≥ ε) ≤ e^{−ε²/2σ²}, Chernoff + envelope +
optimize (prob06-generalization/prob06-generalization.html:666); **Prop.**
independent sums add variance proxies
(prob06-generalization/prob06-generalization.html:762); **Thm 3** Hoeffding's
inequality Pr(X̄_n−μ ≥ ε) ≤ exp(−2nε²/(b−a)²), assembled from Thm 1 + closure rules
+ Thm 2 (prob06-generalization/prob06-generalization.html:824); **Thm 4** union
bound, one-line indicator proof
(prob06-generalization/prob06-generalization.html:993); **Thm 5** finite-class
uniform convergence sup_h |R−R̂_n| ≤ √(ln(2|H|/δ)/2n) w.p. ≥ 1−δ, full arc
(prob06-generalization/prob06-generalization.html:1189); **Cor.** ERM guarantee
R(ĥ) ≤ min_h R(h) + 2ε, three-hop proof
(prob06-generalization/prob06-generalization.html:1300).
Figures: all diagrams inline SVG with hand-computed numbers (overfitting U-curve,
route map, tilting bar chart, sub-Gaussian tail envelope, union-bound Venn, ε-tube
with ERM pick, why-2ε two-hop ladder, approximation-estimation trade-off, sample-
complexity line n ≈ 739+139k). All numeric examples hand-computed: n ≥ 4,612 for
±2%@95% (ln 40/0.0008), model-farm 10⁴×3.7×10⁻⁶ = 3.7%, vacuous n=25 case
e^{−3.125} ≈ 0.044, sample-complexity table (10 → 1,199; 10³ → 2,120; 10⁶ → 3,501;
2¹⁰⁰ → 14,600), ResNet-50 honest slide (25.6M params × 32 bits → ln|H| ≈ 5.7×10⁸,
n = 1.28×10⁶ → ε ≈ 14.9). Cross-deck numbers (Chernoff 2.1×10⁻⁶, exact 2.8×10⁻⁷,
exponent 0.1308) taken from prob05's published slides. Illustrative-only counts
flagged on-slide: decision-stump class size 256d, ResNet-50 parameter count.

### prob07-estimation — Estimation: MLE, MAP & Fundamental Limits (126 slides)

`prob07-estimation/prob07-estimation.html` · **prob 1563–1911** plus conditional
expectation/tower (prob 1577–1592, deferred here from prob05 per deck plan).
Lecture 7 — answers prob06's bridge (how to *choose* ĥ → likelihood); recalls
prob02 CE loss, prob03 conditional pmf + heights model, prob04 diffusion teaser,
prob05 MGF add-and-subtract, prob06 H(Y|X)/chain rule/DPI by name without
re-proving; prob03's two-coin table (p(0,0)=1/2, p(1,0)=p(0,1)=1/4) returns three
times (conditional means, tower check, MMSE = 1/6 vs constant-guess 1/4); ends on
a bridge to prob08 (the Gaussian everywhere → multivariate Gaussian, linear
E[X|Y]).

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + TOC | 1–2 | prob07-estimation/prob07-estimation.html:23 |
| 01 | Why Estimation? (DL as estimation cards :132, prob06's open question :155, claim CE=MLE to prove today :171, route map SVG :182, inference vs. learning faces :220) | 3–8 | prob07-estimation/prob07-estimation.html:123 |
| 02 | Conditional Expectation (recall prob03 conditional pmf :249, definition :267, worked pmfs-first on prob03 table :283, both conditional means 2/3 and 0 :298, E[X|Y] is an RV :314, its own distribution :348, Thm 1 tower arc :360, proof :372, tower check 7/12·... = E[X]=1/4 :388, why it matters today :402) | 9–19 | prob07-estimation/prob07-estimation.html:240 |
| 03 | The Estimation Problem (sample/label setup :425, two-nationalities running example :439, two height densities SVG N(170,10²) vs N(180,15²) :452, two questions → two estimators :473) | 20–24 | prob07-estimation/prob07-estimation.html:416 |
| 04 | Maximum Likelihood (definition :500, MLE on heights :516, worked x=176 → 0.0333>0.0257 → A :529, decision-boundary SVG ≈179 :543, worked x=185 → B :565, what MLE ignores :577) | 25–31 | prob07-estimation/prob07-estimation.html:491 |
| 05 | Maximum a Posteriori (definition :598, Bayes' rule derivation :614, evidence drops out :628, heights with 9:1 prior :640, worked x=176 :654, worked x=185 — MLE/MAP disagree 0.0117 vs 0.0025 :666, prior moves boundary SVG ≈195 :681, Thm 2 MAP is Bayes optimal arc :701, 2-step proof :714, regularization is a prior :741) | 32–43 | prob07-estimation/prob07-estimation.html:589 |
| 06 | Fano's Inequality (fundamental-limit question :763, technique reviews: H(Y|X) :777, chain rule :791, two entropy bounds :804, DPI entropy form :820, Thm 3 arc P_e ≥ (H(Y|X)−1)/log|Y| :832, reading the bound :845, proof overview :859, 9 one-idea proof steps error flag → expansions → DPI → flag/label terms → sandwich :873–:976, proof summary aligned chain :988, sandwich picture SVG :1005, worked 8-class (2.5−1)/3 = 0.5 :1027, vacuous case :1038, what Fano buys :1050) | 44–66 | prob07-estimation/prob07-estimation.html:754 |
| 07 | Parameter Estimation (new target θ :1072, log-likelihood :1086, Bernoulli MLE derivation :1099, sanity checks :1136, worked 10 flips 7 heads L(0.5)=0.00098 < L(0.7)=0.00222 > L(0.9)=0.00048 :1150, log-lik curve SVG :1166, Gaussian MLE μ̂ and σ̂² :1187, promised proof CE loss = MLE :1230, via prob02 KL :1244, one identity three names :1257) | 67–81 | prob07-estimation/prob07-estimation.html:1063 |
| 08 | Naive Bayes (2ⁿ-parameter blowup 2⁴⁹ ≈ 5.6×10¹⁴ :1280, conditional-independence assumption :1294, spam-filter SVG :1310, binarized MNIST figure :1344, NB classifier :1361, fit by counting :1372, fit the prior :1387, MAP with fitted model :1400, worked 10-mail table p_free|spam=3/4 :1411, classify new mail 0.225/(0.225+0.033) ≈ 0.87 spam :1426, zero-count veto :1439, Laplace smoothing :1453, smoothed table 1/8, 2/8, 5/8 :1468, takeaway :1483) | 82–96 | prob07-estimation/prob07-estimation.html:1271 |
| 09 | Bias–Variance (estimator is an RV :1505, bias :1518, variance :1531, MSE :1546, technique review add-and-subtract :1559, Thm 4 MSE = Bias² + Var arc :1573, 2-step proof cross term dies :1588, dartboard SVG :1615, sample-mean example σ²/n :1648, worked p̂=S/10 vs p̃=(S+1)/12 :1664, numbers 0.025 vs 0.0174 (p=.5), 0.009 vs 0.0107 (p=.9) :1678, MSE-vs-p chart SVG crossings ≈0.14/0.86 :1693, regularization trade :1715) | 97–111 | prob07-estimation/prob07-estimation.html:1496 |
| 10 | MMSE Estimation (denoising channel SVG :1737, Thm 5 MMSE = E[X|Y] arc :1765, proof overview :1777, 4 proof steps insert/expand → tower kills cross term → read off :1790–:1827, proof summary :1838, worked prob03 table MMSE = 1/6 < 1/4 :1857, denoisers learn E[X|Y] :1871) | 112–122 | prob07-estimation/prob07-estimation.html:1728 |
| — | Recap chain, every-tool recap table, bridge to prob08, end slide X̂(Y)=E[X|Y] | 123–126 | prob07-estimation/prob07-estimation.html:1885 |

Key theorems: **Thm 1** tower property E[E[X|Y]] = E[X], full proof + table check
(prob07-estimation/prob07-estimation.html:360); **Thm 2** MAP minimizes error
probability, 2-step proof score-any-estimator → maximize each term
(prob07-estimation/prob07-estimation.html:701); **Thm 3** Fano's inequality
P_e ≥ (H(Y|X)−1)/log|Y|, full 9-step proof (error flag, two chain-rule expansions
of H(E,Y|Ŷ), DPI, bound both scenario terms, close the sandwich)
(prob07-estimation/prob07-estimation.html:832); **Thm 4** bias–variance
decomposition MSE = Bias² + Var, exact identity, add-and-subtract proof
(prob07-estimation/prob07-estimation.html:1573); **Thm 5** MMSE estimator is the
conditional mean, 4-step proof with tower killing the cross term
(prob07-estimation/prob07-estimation.html:1765).
Figures: MNIST digit (../figs/mnist.png, binarized 7×7 discussion); all other
diagrams inline SVG with hand-computed geometry (route map, two height densities,
MLE boundary ≈179 with pick-B crossing ≈145, prior-shifted boundary ≈195, Fano
sandwich, Bernoulli log-likelihood curve with max at 0.7, spam-mail feature map,
dartboard bias/variance quadrants, MSE-vs-p parabolas with crossings ≈0.14/0.86,
denoising channel). All numerics hand-computed (heights densities at 176/185, NB
10-mail table + 0.87 posterior + smoothed 1/8-2/8-5/8, coin likelihood table,
p̂-vs-p̃ MSE table, Fano 8-class floor 0.5, MMSE 1/6 vs 1/4). Deviations from
tex: prob 1661 MAP argmax written over the likelihood, fixed to the posterior;
prob 1791 prior-count indicator 1{y⁽ʲ⁾=0}, fixed to 1{y⁽ʲ⁾=1}; prob 1802
duplicate p(x_i|0) in the numerator, fixed to p(x_i|1); "twice as likely" vs
9/10 prior inconsistency in the heights example resolved to a 9/10 : 1/10 prior
throughout; spelling fixes (Conditioanl, funciton, classfication). Added beyond
the tex: tower-property proof, MAP Bayes-optimality proof, Bayes-rule derivation
slide, Fano technique-review slides, CE-loss=MLE bridge slides, and all worked
numeric examples above (the tex states the estimators but computes none of
them).

### prob08-gaussian — The Multivariate Gaussian (131 slides)

`prob08-gaussian/prob08-gaussian.html` · source: prob 1912–2519.
**Attribution: the tex credits MIT OpenCourseWare 6.436J / 15.085J Fundamentals of
Probability (Fall 2018), License CC BY-NC-SA 4.0 — preserved on-slide as a visible
credit line on the §02 section divider (prob08-gaussian/prob08-gaussian.html:228)
covering sections 02–08.** Lecture 8 — answers prob07's bridge (the Gaussian
everywhere, linear E[X|Y]); recalls prob05 MGF + uniqueness, prob04 Markov/diffusion
teaser, prob03 MaxEnt Gaussian, prob07 MMSE by name without re-proving; undergrad
DDPM treatment (grad-level rigor lives in `courses/privacy/lectures/02-generative/`
and `courses/infotheory/lectures/07-diffusion/` — this deck stops at the exact
forward process + Gaussian reverse-step form, no variational objective); ends on a
bridge to prob09 (integrals stop closing → Monte Carlo).

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + TOC | 1–2 | prob08-gaussian/prob08-gaussian.html:24 |
| 01 | Why Gaussians? (default noise model cards, 1D-so-far gap, today's claims, route map SVG) | 3–8 | prob08-gaussian/prob08-gaussian.html:115 |
| 02 | Warm-Up: Two Dimensions (jointly Gaussian pair :233, joint density :248, coupling picture, running example ρ=1/2 :287 + ellipse SVG, Thm 1 statement :322, slicing SVG, worked conditional :357, what the general case needs) | 9–18 | prob08-gaussian/prob08-gaussian.html:223 |
| 03 | Positive Semidefinite Matrices (PD/PSD def :393, bowl-vs-trough SVG, PD certificate :434, spectral decomposition :462, worked eigenpairs :475, symmetric square root :489 + worked :502, inverse, factorization exercise + solution, why this buys a density :553) | 19–31 | prob08-gaussian/prob08-gaussian.html:384 |
| 04 | Three Definitions (three-roads cards :575, Def 1 density :599, white noise :613, Def 2 constructive X=DW+μ :626 + coloring SVG, Def 3 projection :667 + shadow SVG, degeneracy :703, equivalence map :733) | 32–41 | prob08-gaussian/prob08-gaussian.html:566 |
| 05 | Vector Means & Covariances (mean vector :772, covariance matrix :784, self-covariance :800, PSD exercise + solution :813, correlation coefficient :840) | 42–48 | prob08-gaussian/prob08-gaussian.html:763 |
| 06 | The Properties Theorem (Thm 2 statement in three cards :861–:892, roadmap :908, part 1 affine :926, part 2 Cov=DD^T :957, part 3 marginals :988, part 4 density via change of variables :1028, part 5 MGF :1096, part 6 uncorrelated=independent :1141, part 7 conditionals via orthogonality :1211, conditional assembled :1345, Thm 1 finally proved :1360, Thm 2 recap :1374) | 49–85 | prob08-gaussian/prob08-gaussian.html:852 |
| 07 | The Gaussian Channel (Y=X+Z setup + block SVG :1397, joint covariance :1423, read off part 7 :1437, prob07 promise kept :1450, shrinkage SVG :1463, two-extremes sanity table :1483, two sampling orderings :1498, why the second matters :1520) | 86–94 | prob08-gaussian/prob08-gaussian.html:1390 |
| 08 | Gaussian Diffusion (prob04 teaser cashed in :1539, noising recursion :1553, variance preserving :1565, noising-chain SVG :1579, source exercise :1603, MGF telescope :1616–:1646, Thm 3 chain forgets :1660, closed form :1676, DDPM ᾱ notation :1688, worked β=0.02 schedule chart :1701, reverse step claim :1724 + via channel :1736, vectors :1751, generation skeleton :1763, scope today-vs-full-story :1787) | 95–112 | prob08-gaussian/prob08-gaussian.html:1532 |
| 09 | Gaussian Discriminant Analysis (one Gaussian per class :1812, decision rule :1826, boundary SVG :1839, back to MLE :1863, log-likelihood :1876, fit μ :1888, precision reparam :1904, trace trick :1917, scatter matrix :1930, matrix derivatives :1944, solve :1959, Thm 4 :1975, source exercises A/B :1991, GDA pipeline :2008) | 113–127 | prob08-gaussian/prob08-gaussian.html:1805 |
| — | Recap chain, every-tool recap table, bridge to prob09, end slide X=DW+μ | 128–131 | prob08-gaussian/prob08-gaussian.html:2020 |

Key theorems: **Thm 1** 2D conditional X|Y=y ~ N(μ₁+σ₁₂/σ₂₂(y−μ₂), σ₁₁−σ₁₂σ₂₁/σ₂₂),
stated in §02, proved as part-7 corollary
(prob08-gaussian/prob08-gaussian.html:322, proof :1360); **Thm 2** seven properties
of the multivariate normal (affine closure, Cov = DD^T, marginals, density when
V ≻ 0, MGF exp(s^Tμ + s^TVs/2), uncorrelated = independent, conditionals with
linear mean + variance shrinkage), all seven proved with per-part technique
reviews (prob08-gaussian/prob08-gaussian.html:861); **Thm 3** diffusion limit
X_n →d N(0,1) for any X₀ with an MGF, via MGF telescope
(prob08-gaussian/prob08-gaussian.html:1660); **Thm 4** Gaussian MLE μ̂ = sample
mean, Σ̂ = S/N via trace trick + matrix derivatives, biasedness remarked
(prob08-gaussian/prob08-gaussian.html:1975).
Figures: all diagrams inline SVG with hand-computed geometry (route map, running
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

### prob09-monte-carlo — Monte Carlo & Importance Sampling (117 slides)

`prob09-monte-carlo/prob09-monte-carlo.html` · **new material — not in tex**
(textbook-canonical statements and proofs only; every constant derived on-slide).
Lecture 9 — final probability deck; answers prob08's bridge (integrals stop
closing → sample them); recalls prob01 LOTUS/variance/Jensen, prob02 KL,
prob04 chain rule of probability, prob05 LLN/Chebyshev, prob06 Hoeffding,
prob07 MSE decomposition by name without re-proving; ends by closing the
probability half (prob01–prob09 recap map) and bridging to opt01 (SVD & least
squares — the optimization half).

| # | Section | Slides | Location |
|---|---|---|---|
| — | Title + TOC | 1–2 | prob09-monte-carlo/prob09-monte-carlo.html:23 |
| 01 | Why Sampling? (three uncomputable expectations cards :132, prob08 cliffhanger cashed in :156, integration by averaging :170, today's three upgrades :183, route map SVG :210) | 3–8 | prob09-monte-carlo/prob09-monte-carlo.html:123 |
| 02 | Recall — the Toolkit (prob01 LOTUS+variance card :251, prob05 LLN+Chebyshev card :266, prob06 Hoeffding card :281, what is genuinely new :296) | 9–13 | prob09-monte-carlo/prob09-monte-carlo.html:242 |
| 03 | The Monte Carlo Estimator (target :318, definition :332, Thm 1 unbiasedness arc :346, Thm 2 variance σ_f²/n arc :383, RMSE via prob07 MSE decomposition :407, Chebyshev guarantee :421, Hoeffding guarantee + inversion :434, worked π by darts :445, dartboard SVG hand-placed darts :461, six-darts table :486, exact statistics Var(π̂)=2.70/n :503, darts-per-digit table :514, guarantee two ways 539,200 vs 295,111 :529, what MC never asked :544) | 14–31 | prob09-monte-carlo/prob09-monte-carlo.html:309 |
| 04 | Error Scaling & Dimension (dimension absent from Thm 2 :566, grid integration :579, grid cost table 10^d :592, MC cost :609, error-vs-work log-log SVG :627, crossover d=4 :656, honest caveats (quasi-MC name only) :669, implication for AI :681) | 32–40 | prob09-monte-carlo/prob09-monte-carlo.html:557 |
| 05 | Importance Sampling (two failure modes :703, rare event Pr(X>10)=e⁻¹⁰ by hand :722, vanilla MC needs n≈2.2×10⁶ :731, the fix multiply-and-divide :744, Thm 3 IS identity arc w/ support condition :754, support counterexample estimate ≡0 :793, IS estimator definition + unbiased corollary :804, weights are likelihood ratios :819, p-vs-q SVG with weight bars :836, shifted-exponential proposal :864, every sample says e⁻¹⁰ exactly :877, too good — the dial :890) | 41–55 | prob09-monte-carlo/prob09-monte-carlo.html:694 |
| 06 | The Variance of IS (variance formula :912, the object ∫f²p²/q :925, Jensen recall (prob01) :938, Thm 4 optimal proposal q*∝\|f\|p arc, Jensen floor + attained :952–:1002, zero variance verified on rare event :1016, the catch: q* needs the answer :1029, other end of the dial :1042, light-tailed Exp(2) worked example :1053, E_q[w²]=∞ derived :1064, unbiased-consistent-useless :1079, tail rule Exp(1/2)→4/3 :1093, weight-degeneracy histogram SVG 95% :1109, one sample in disguise :1132) | 56–73 | prob09-monte-carlo/prob09-monte-carlo.html:903 |
| 07 | Self-Normalized IS (missing constant Z :1152, unnormalized weights w̃=Zw :1164, SNIS definition :1176, two MC estimators one ratio :1190, consistency sketch (continuous mapping named, not proved) :1203, biased flag worked 2/3≠1/2 :1217, ESS definition (flagged heuristic) :1228, ESS sanity checks n and 1.11 :1242, what ESS is not :1253, where SNIS runs in AI :1265) | 74–84 | prob09-monte-carlo/prob09-monte-carlo.html:1143 |
| 08 | The Score-Function Gradient (J(θ)=E[R] :1296, why plain MC gives no gradient :1310, log-derivative trick review :1324, Thm 5 score-function/REINFORCE identity arc, finite X, expand/swap/reread :1338–:1399, REINFORCE estimator :1413, worked two-action sigmoid policy :1426, identity agrees both sides 1/4 :1437, reading the identity :1448, baseline lemma + mean-zero score proof :1462, baseline at work variance 1/16→0 table :1477, REINFORCE pipeline SVG :1496) | 85–101 | prob09-monte-carlo/prob09-monte-carlo.html:1287 |
| 09 | Off-Policy & RLHF (off-policy problem :1536, it's Theorem 3 with π_θ/π_b :1548, sequences multiply weights (chain rule, prob04) :1561, degeneracy grows 1.1¹⁰⁰≈13,800 caricature :1574, keep the ratio near one (clipping/trust regions names only) :1587, recall prob02 KL card :1599, RLHF-shaped objective max E[r]−βD(π_θ‖π_ref) w/ scope note :1614, one pipeline every tool :1629) | 102–110 | prob09-monte-carlo/prob09-monte-carlo.html:1527 |
| — | Recap chain Thm 1–5, every-tool recap table, nine-decks map SVG, probability-half recap, bridge to opt01, end slide E_p[f]=E_q[f·p/q] | 111–117 | prob09-monte-carlo/prob09-monte-carlo.html:1649 |

Key theorems: **Thm 1** unbiasedness E[μ̂_n]=μ, linearity proof
(prob09-monte-carlo/prob09-monte-carlo.html:346); **Thm 2** Var(μ̂_n)=σ_f²/n via
independence, hence RMSE σ_f/√n in any dimension
(prob09-monte-carlo/prob09-monte-carlo.html:383); **Thm 3** IS identity
E_p[f]=E_q[f·p/q] under the support condition q>0 wherever fp≠0, LOTUS +
cancellation proof + counterexample
(prob09-monte-carlo/prob09-monte-carlo.html:754); **Thm 4** optimal proposal
q*=\|f\|p/c minimizes IS variance, Jensen floor c² attained, min Var = c²−μ²
(prob09-monte-carlo/prob09-monte-carlo.html:952); **Thm 5** score-function /
REINFORCE identity ∇_θ E[R]=E[R ∇_θ log π_θ] proved for finite X
(prob09-monte-carlo/prob09-monte-carlo.html:1338); **Lemma** baseline invariance
via mean-zero score (prob09-monte-carlo/prob09-monte-carlo.html:1462).
Figures: all diagrams inline SVG with hand-computed geometry (route map,
dartboard with six hand-placed darts, error-vs-work log-log chart with slopes
−1/2 / −2 / −0.1, proposal-vs-target densities with weight bars,
weight-degeneracy histogram, REINFORCE pipeline with feedback arrow, nine-decks
prob01–prob09 map).
Named-not-proved, flagged on-slide: strong LLN (finite mean, name only);
quasi-MC and \|V\|^T language-model state count (illustrative); grid error ~h²
with constants suppressed; SNIS consistency (continuous-mapping step named);
ESS (labeled heuristic, not a theorem); ∇/∑ interchange for continuous X
(dominated convergence named); per-token 1.1 weight-growth caricature; clipping
and trust regions (names only); RLHF objective labeled schematic with explicit
"no claims about any specific algorithm" scope note.
