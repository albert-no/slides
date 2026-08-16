# privacy/lectures/02-generative/ — Generative-model review (diffusion + LLM)

The privacy series opens with a **review of generative models**, then moves to the privacy stack (DP, MIA, memorization, unlearning, watermarking). This folder bundles both reviews:

- **Diffusion (5 lectures)** — continuous, score-based generation, from scratch.
- **LLM (1 deck)** — discrete autoregressive counterpart, brief.

Both fix the notation and observables that the downstream privacy decks attack or defend.

Companion notes: every diffusion lecture now has a paired `<deck>-note.html` with formal definitions, theorem statements, and full proof derivations beyond what the slides carry. `note/2_difffusion.tex` is LaTeX source covering Diffusion Lectures 1–2.

## Files

| Deck | Companion notes | Topic |
|---|---|---|
| `diffusion1-foundations.html` | `diffusion1-foundations-note.html` | Generative models, VE forward, Bayes-route reverse, Tweedie |
| `diffusion2-ddpm.html` | `diffusion2-ddpm-note.html` | VP forward, DDPM, VLB three-term decomposition, ε-loss |
| `diffusion3-sde-score.html` | `diffusion3-sde-score-note.html` | Continuous-time SDE, Fokker–Planck, Anderson reverse, score matching |
| `diffusion4-ddim.html` | `diffusion4-ddim-note.html` | Non-Markovian forward, deterministic sampling, probability-flow ODE |
| `diffusion5-guidance-discrete.html` | `diffusion5-guidance-discrete-note.html` | Classifier guidance, CFG, inpainting, discrete diffusion |
| `llm.html` | — | Tokens, decoder-only transformer, NLL pretraining, sampling, privacy hooks |
| `note/2_difffusion.tex` | | LaTeX source for Diffusion Lectures 1–2 (rigorous mathematical write-up) |

---

## diffusion1-foundations.html — Foundations

49 slides. Every major result is now stated as a Proposition/Theorem and proved
step-by-step on the slides (outline → steps → recap chain), with a figure on most
content slides.

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:29-80` |
| **01 — Generative models** | | `:82-272` |
| | Realistic is not enough (swatch-grid figure) | `:91` |
| | Mode collapse in one picture (bimodal vs spike) | `:121` |
| | Sampling is non-trivial (Cauchy density, "?" figure) | `:140` |
| | **Proposition: inverse-transform sampling (1D)** | `:161, :164` |
| | Inverse transform — the picture (CDF read-off) | `:174` |
| | Example — sampling the Cauchy (`X = γ tan(π(U−½))`) | `:199` |
| | Where the uniform comes from (binary expansion, `2^-n` error) | `:211` |
| | High dimension breaks this (ball/box accept-rate bar chart) | `:224` |
| | Learn a map, not a density | `:255` |
| **02 — VE forward process** | | `:274-375` |
| | Forward `X^(n) = X^(n-1) + Z^(n)` | `:283` |
| | Noising in pictures (three densities blurring) | `:305` |
| | n steps in one shot, `X^(n) = X^(0) + √n σ Z` | `:331` |
| | Terminal distribution | `:346` |
| | Goal: reverse the chain (generation-order chain diagram) | `:357` |
| **03 — Reverse via Bayes** | Taylor + complete-square route | `:377-663` |
| | Setup (rename `X, Z, Y`; one backward edge) | `:386` |
| | Proof outline (4 steps) | `:408` |
| | Step 1: Taylor expand `P_X` | `:422` |
| | Why local expansion works (zoom-to-noise-scale figure) | `:434` |
| | Step 2: approximate `P_Y` (odd Gaussian moment) | `:455` |
| | Step 3: substitute back (`1+a ≈ e^a`) | `:471` |
| | Step 4: merge the exponents | `:486` |
| | Step 4 (continued): complete the square | `:496` |
| | Proof recap (one `\stackrel` chain) | `:506` |
| | **Theorem: small-noise reverse conditional** | `:520, :523` |
| | Reverse sampling rule | `:535` |
| | The score shift in a picture (drift arrows uphill) | `:545` |
| | Why not subtract noise? | `:570` |
| | Estimation vs distribution matching (shrinkage two-panel figure) | `:582` |
| | **Proposition: MMSE = conditional mean** | `:617, :620` |
| | Proof — orthogonality of the error (expand the square) | `:629` |
| | Proof (continued) — killing the cross term (tower property) | `:646` |
| | Gaussian MMSE mismatch (variance `σx⁴/(σx²+σz²)`, fresh noise) | `:658` |
| **04 — Score function & Tweedie** | | `:666-813` |
| | Score function `s(x;n) = ∂_x log P_{X^(n)}` | `:679` |
| | **Theorem: Tweedie's formula (Robbins 1956)** | `:692, :695` |
| | Tweedie — proof outline (4 steps) | `:706` |
| | Proof — differentiate the convolution (Gaussian derivative identity) | `:720` |
| | Proof (continued) — recognize the posterior mean (Bayes) | `:733` |
| | Proof recap — Tweedie in one chain | `:747` |
| | Reading Tweedie (score arrow pulling `y` toward the mass) | `:761` |
| | Train a denoiser, not a score (squared-loss regression) | `:782` |
| | Denoiser-to-score `s_θ = (f_θ − x)/(nσ²)` | `:793, :798` |
| | Lecture recap | `:806` |

**Key:** Inverse-transform proposition `:164`; reverse conditional `:523-525`;
MMSE = conditional mean `:620`; Tweedie `:695-697`; denoiser-to-score `:798`.

**Companion note** (`diffusion1-foundations-note.html`): inverse-transform proof
plus worked Cauchy example, ball/box volume-ratio decay table, and the full
derivations the slides compress.

---

## diffusion2-ddpm.html — DDPM

61 slides. Math-detail revision: every major result is a Theorem/Lemma card
followed by a proof outline, numbered step slides, and a one-chain recap, with a
deck-local SVG figure (`.d2-fig`, `.d2-chain`) on most non-proof slides.

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:62-121` |
| **01 — The variance preserving process** | | `:123-357` |
| | Why variance preserving (VE vs VP variance-line figure) | `:132` |
| | **VP forward** `X^(n) = √(1−β_n) X^(n-1) + √β_n Z^(n)` | `:156` |
| | Variance is preserved (unit-variance induction) | `:174` |
| | **n steps in one shot**, `ᾱ_n = ∏(1−β_i)` | `:187` |
| | Proof — induction step (workhorse identity) | `:202` |
| | Schedule and the signal budget (signal/noise bar figure, ᾱ table) | `:212` |
| | **Definition (MGF)** | `:247, :250` |
| | **Theorem (Lévy continuity, MGF form)** | `:263, :266` |
| | **Theorem (terminal law of the VP chain)** → `N(0,1)` | `:277, :280` |
| | Proof — one-step MGF recursion | `:290` |
| | Proof (continued) — unroll to `n` | `:303` |
| | Proof (continued) — take the limit (`ᾱ_n → 0`) | `:316` |
| | Proof recap — one chain | `:326` |
| | The terminal forgets the data (three densities → `N(0,1)`) | `:339` |
| **02 — DDPM reverse model** | | `:368-465` |
| | Recall — small-noise reverse rule (Lec 1) | `:378` |
| | **Rescaling the VP step** (`W = X^(n)/√(1−β_n)`, `σ_eff²`) | `:391` |
| | Applying the rule (change of variables, exact combination) | `:406` |
| | **Reverse conditional, VP version** | `:419` |
| | **Why not train µ directly** (score is the only unknown) | `:434` |
| | **Two routes to the score**: Tweedie (Lec 1) vs VLB (this lecture) | `:446` |
| **03 — Variational lower bound** | | `:466-708` |
| | **Maximum likelihood objective** (NLL = KL + H(q)) | `:475` |
| | **Marginal is intractable** (N-fold integral) | `:490` |
| | **Lemma (forward Markov identity)** — Bayes on the chain | `:511, :514` |
| | Proof — two chain rules | `:532` |
| | Bound — proof outline (4 steps) | `:546` |
| | Step 1: insert the forward joint (multiply-and-divide trick) | `:563` |
| | Step 2: Jensen | `:573` |
| | Step 3: factor the ratio | `:585` |
| | Step 3 (continued): telescope | `:598` |
| | Step 4: three named factors | `:610` |
| | Step 4 (continued): sum of three terms | `:619` |
| | Proof recap — one chain | `:631` |
| | `L_N`: match the prior | `:644` |
| | **`L_{n-1}`: match each reverse step (training signal)** | `:658` |
| | Where the three terms live (bracketed-chain figure) | `:671` |
| **04 — Exact posterior to ε-loss** | | `:709-915` |
| | **Theorem (data-conditional posterior)** — exactly Gaussian | `:718, :721` |
| | Why conditioning on `X^(0)` helps (product-of-Gaussians figure) | `:730` |
| | Proof — Bayes and Markov | `:752` |
| | Proof (continued) — collect the quadratic (`β̃_n`) | `:765` |
| | Proof (continued) — read off the mean (`µ̃_n`) | `:775` |
| | **Posterior mean in score form** | `:785` |
| | Verifying the rewrite (`1−ᾱ_n−β_n = (1−β_n)(1−ᾱ_{n−1})`) | `:795` |
| | From KL to mean matching (equal-variance Gaussian KL) | `:808` |
| | **Not ordinary mean matching**: µ̃_n sees `X^(0)`, µ_θ does not | `:818` |
| | **Mean matching → score matching** | `:852` |
| | **ε ↔ score visual** (anti-parallel, scaled) | `:862` |
| | **ε-Reparameterization**: `s_θ = −ε_θ/√(1−ᾱ_n)` | `:888` |
| | **ε-Prediction Loss** `L_simple` | `:903` |
| **05 — Training and sampling** | | `:916-1035` |
| | Training algorithm (5 steps) | `:924` |
| | From `µ_θ` to the update | `:941` |
| | Sampling algorithm | `:952` |
| | **Three approximation errors** (forward+reverse dual chain, 3 cards) | `:971` |
| | Lecture recap | `:1020` |

**Key:** VP forward `:156`; one-shot `:187`; MGF def `:250`; Lévy `:266`;
terminal theorem `:280`; rescaling `:391`; VP reverse conditional `:419`;
Bayes-on-chain lemma `:514`; VLB outline `:546`; three-term sum `:619`;
posterior theorem `:721`; score form `:785`; ε↔score `:862`; ε-loss `:903`;
three-error chain `:971`.

**Companion note** (`diffusion2-ddpm-note.html`): schedule/signal-budget table
(§1.4), the full rescaling derivation with the exact score combination (§3.1–3.2),
the verified score-form rewrite (§5.3), and the `β̃_n` vs `β_n` variance
discussion (§6.2).

---

## diffusion3-sde-score.html — SDE + score matching

72 slides. Every major result is stated as a Theorem/Proposition/Lemma and proved
step-by-step on the slides (setup → outline → numbered steps → `\stackrel` recap
chain), with 13 deck-local SVG figures (`.d3-fig`, KaTeX overlay labels).

Companion notes file: `diffusion3-sde-score-note.html` (Brownian-motion and √Δt
scaling, order bookkeeping, heat-kernel check, FP uniqueness assumptions, full
Anderson sign tracking, linear-SDE kernel via Itô isometry, OU stationary law,
Euler–Maruyama error orders, DDPM↔SDE limit).

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:63-119` |
| **01 — Discrete to continuous** | | `:121-321` |
| | Why continuous time (staircase → smooth figure) | `:132` |
| | Random walk → Brownian motion (8/32/128-step figure) | `:161` |
| | **Definition: Brownian motion (Wiener process)** | `:185` |
| | Why the √Δt scaling (variance adds) | `:201` |
| | VE as SDE `dX_t = √β dW_t`; marginal consistency check | `:213, :224` |
| | VP as SDE (OU) via `√(1−βΔt)` Taylor | `:234` |
| | General forward SDE; drift/diffusion pictured | `:247, :267` |
| | Solution is a distribution (Itô integral, sample-path fan) | `:300` |
| **02 — Fokker–Planck** | | `:323-539` |
| | Two views of one process (path vs density figure) | `:334` |
| | Warm-up: pure diffusion = heat equation | `:356` |
| | **Theorem (1D Fokker–Planck):** `∂_t p_t = −∂_x(f p_t) + (g²/2)∂_x² p_t` | `:376, :379` |
| | Reading the equation (transport vs flattening figure) | `:389` |
| | Proof setup — why a test function; outline | `:416, :426` |
| | Steps 1–3 (Taylor, which orders survive, expectation, IBP) | `:439, :449, :464, :474` |
| | Stripping φ (fundamental lemma of calculus of variations) | `:487` |
| | Proof recap — one chain | `:499` |
| | Example: where VP settles (`p_∞ ∝ e^{−x²/2}` derived) | `:513` |
| | **Vector form (multi-D, divergence + Laplacian)** | `:529` |
| **03 — Anderson's reverse SDE** | | `:541-793` |
| | Flipping the drift is not enough (figure) | `:552` |
| | The score points uphill (bimodal + arrow figure) | `:587` |
| | **Theorem (Anderson 1982):** reverse drift = `f − g² ∂_x log p_t` | `:615, :618` |
| | **Two SDEs, same marginals** (forward/reverse figure) | `:628` |
| | Sanity check — Gaussian case (linear score) | `:657` |
| | Proof setup — strategy; outline | `:669, :684` |
| | Step 1 (run reverse forward), back to original time | `:697, :707` |
| | Step 2 (`p_t` solves that PDE), Step 3 (uniqueness) | `:717, :730` |
| | Proof recap — one chain | `:745` |
| | Why Anderson matters; where the error now lives | `:759, :781` |
| **04 — Score matching** | | `:795-1005` |
| | **Why learn the score** (chain view vs score view) | `:806` |
| | Natural loss is intractable (Fisher divergence) | `:828` |
| | Key idea — the kernel is known (mixture figure) | `:840` |
| | **Theorem (Vincent 2011): score matching = denoising** | `:865, :868` |
| | Proof setup; outline | `:878, :888` |
| | **Lemma (marginal score = posterior average of kernel scores)** | `:901, :904` |
| | Steps 1–3 (lemma proof, expand square, cross term, reassemble) | `:913, :927, :939, :952` |
| | Proof recap — one chain | `:963` |
| | Noisy target, correct optimum (averaging figure) | `:976` |
| **05 — Kernel, noise prediction, DDPM** | | `:1007-1204` |
| | **Proposition (VP transition kernel):** `γ_t = e^{−φ(t)/2}`, `σ_t² = 1 − γ_t²` | `:1018, :1021` |
| | Proof — mean ODE; variance ODE | `:1031, :1043` |
| | Signal/noise budget (`γ_t² + σ_t² = 1` curves) | `:1055` |
| | Conditional score in closed form (`−ε/σ_t`) | `:1076` |
| | ε-reparameterization | `:1090` |
| | Example: Ornstein–Uhlenbeck | `:1102` |
| | Training algorithm; Euler–Maruyama sampler | `:1112, :1128` |
| | DDPM is discrete score matching (correspondence table) | `:1147` |
| | Same loss, two derivations | `:1161` |
| | Multi-dimensional extension; recap | `:1175, :1188` |

**Key theorems:** Fokker–Planck `:379`; vector form `:529`; Anderson reverse SDE
`:618`; same-marginals figure `:628`; denoising score matching (Vincent 2011)
`:868`; marginal-score lemma `:904`; VP transition kernel `:1021`.

---

## diffusion4-ddim.html — DDIM

75 slides. Math-detail revision mirroring deck 3: every major result is a
Theorem/Proposition/Definition card followed by a proof outline, numbered step
slides, and a one-chain `\stackrel` recap, with 15 deck-local SVG figures
(`.d4-fig`, `.d4-algo`, `.d4-chain`, KaTeX overlay labels).

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:76-127` |
| **01 — What the DDPM Loss Sees** | | `:129-308` |
| | The sampling bottleneck (1000 network calls) | `:137` |
| | Recall — forward marginal; recall — the ε-loss | `:162, :175` |
| | What the loss touches (marginal-only figure) | `:187` |
| | **Proposition (the loss sees only marginals)** | `:220, :223` |
| | Proof — change of measure | `:232` |
| | Two joints, one marginal (figure) | `:242` |
| | What we may change / DDIM in one sentence | `:263, :288` |
| **02 — A Non-Markovian Forward** | | `:310-681` |
| | Markov vs. non-Markovian (two-row edge figure) | `:318` |
| | What we demand (three requirements) | `:363` |
| | Construction order (terminal law first, then backward conditionals) | `:379` |
| | **The mixing recipe** (signal + recycled + fresh) | `:405` |
| | Pinning the coefficients — mean; — variance | `:415, :425` |
| | **The noise budget** $a_n^2+\sigma_{n+1}^2 = 1-\bar\alpha_n$ (bar figure) | `:434` |
| | **Definition (the σ-family)** — forward conditional | `:459, :463` |
| | **Theorem (the σ-family preserves every marginal)** | `:471, :475` |
| | Proof outline (3 steps, backward induction) | `:483` |
| | Step 1 base case; Step 2 whitening; Step 3 two Gaussians add | `:497, :507, :518` |
| | Proof recap — one chain | `:527` |
| | Same pair, different triple | `:536` |
| | How correlated are neighbors? `ρ_n(σ)=√(1−σ²/(1−ᾱ_n))` | `:553, :563` |
| | A two-step example (numeric, ᾱ₁=0.8, ᾱ₂=0.5) | `:586` |
| | **DDPM is one member** (`σ² = β̃_{n+1}`) + two verification slides | `:603, :613, :622` |
| | The other end: `σ ≡ 0` (deterministic forward) | `:630` |
| | The family at a glance | `:660` |
| **03 — DDIM Sampling** | | `:683-1080` |
| | Training is untouched / the gap | `:691, :705` |
| | **Predicted clean signal**; why that guess is optimal (Tweedie recall) | `:715, :724` |
| | Jump back, re-noise (two-move figure) | `:736` |
| | The recycled term collapses (to $\varepsilon_\theta$ identically) | `:767` |
| | **The DDIM reverse update**; sampling algorithm | `:776, :793` |
| | **The deterministic map** (`σ ≡ 0`) | `:809` |
| | Why steps can be skipped; striding the chain | `:823, :833` |
| | Two sources of error (approximation vs discretization) | `:868` |
| | The right coordinates `Y_n = X^{(n)}/√ᾱ_n`, `τ_n = √((1−ᾱ_n)/ᾱ_n)` | `:886` |
| | **Proposition (exact Euler form)** — DDIM is exactly Euler | `:896, :900` |
| | Proof outline (3 steps) + steps + recap chain | `:909, :925, :934, :943, :952` |
| | The same ODE in score form (`ε_θ = −√(1−ᾱ_t) s_θ`) | `:961` |
| | **Theorem (probability-flow ODE, Song et al. 2021)** | `:971, :975` |
| | Proof outline; Step 1 diffusion as transport; Step 2 match the velocity | `:984, :1001, :1011` |
| | Why *half* the score | `:1020` |
| | A continuum of reverse dynamics (λ-family) | `:1042` |
| | Three dynamics, one marginal; different paths, same cloud | `:1054, :1062` |
| **04 — Consequences** | | `:1082-1231` |
| | Why fewer steps work | `:1090` |
| | Quality vs. step count (schematic curve; TODO real figure) | `:1106` |
| | Inversion: images get latents; inversion in practice | `:1128, :1156` |
| | Interpolation: why linear fails; spherical interpolation (slerp) | `:1166, :1176` |
| | DDPM or DDIM? (comparison table) | `:1202` |
| | Recap | `:1219` |

**Key:** Loss-invariance proposition `:223`; σ-family definition `:463`; marginal
invariance theorem `:475`; proof recap `:527`; noise budget `:434`; correlation
dial `:563`; DDPM special case `:603`; predicted clean signal `:715`; DDIM
reverse update `:776`; deterministic map `:809`; exact-Euler proposition `:900`;
PF-ODE theorem `:975`; λ-family `:1042`.

**Companion note** (`diffusion4-ddim-note.html`): neighbor correlation as a
function of σ (§3.3b), the three-step DDPM special-case verification (§3.4),
strided sampling on a subsequence (§4.4), exactness of the (Y, τ) picture (§5.6),
the λ-family with its Fokker–Planck proof (§5.7), solver orders and acceleration
(§6.1), DDIM inversion error analysis (§6.2), and the slerp/lerp norm
computation (§6.3).

---

## diffusion5-guidance-discrete.html — Guidance + discrete diffusion

95 slides. Math-detail revision mirroring decks 3–4: every major result is a
Theorem/Proposition/Definition/Lemma card followed by a proof outline, numbered
step slides, and a one-chain `\stackrel` recap, with deck-local SVG figures
(`.d5-fig`, `.d5-algo`, `.d5-chain`, KaTeX overlay labels).

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:75-127` |
| **01 — Classifier guidance** | | `:129-491` |
| | Why conditional generation (four tasks, figure) | `:138` |
| | Two approaches (per-label model vs. one model + steering) | `:174` |
| | Recall — reverse SDE; recall — score and noise | `:200, :213` |
| | What conditioning requires | `:226` |
| | **Proposition (conditional score = score + classifier gradient)** | `:241` |
| | Proof outline; Step 1 Bayes at level $t$; Step 2 logs; Step 3 differentiate | `:254, :270, :282, :292` |
| | Proof recap — one chain | `:302` |
| | Reading the decomposition (unconditional + push, figure) | `:315` |
| | The classifier must see noise (figure); training the noisy classifier | `:348, :382` |
| | The guided reverse SDE; guidance in $\varepsilon$-form | `:399, :414` |
| | Classifier-guided sampler (`d5-algo`) | `:424` |
| | **What $\omega$ actually samples** (tilted target $p_t\,p_t(y\mid x)^{\omega}$) | `:445` |
| | Proof, and a caveat (the tilt is not a diffusion for $\omega\ne1$) | `:458` |
| | The tilt in a picture | `:474` |
| **02 — Inpainting** | | `:494-773` |
| | What is inpainting (figure); the task, formally | `:502, :530` |
| | Goal as conditional sampling | `:543` |
| | **Lemma (the forward process factorizes over coordinates)** + proof | `:555, :567` |
| | The ideal conditional score | `:577` |
| | Why pasting clean pixels fails (out-of-domain figure) | `:591` |
| | Key idea — noise the observation ($\zeta_n$) | `:620` |
| | **Proposition (the paste is exact in law)** | `:633` |
| | Where the approximation lives (exact tower decomposition) | `:645` |
| | The two approximations (drop clean conditioning; one fresh draw) | `:657` |
| | Boundary check; the inpainting sampler (`d5-algo`) | `:682, :697` |
| | The sampler in a picture; variants (RePaint, ILVR, DPS) | `:718, :760` |
| **03 — Classifier-free guidance** | | `:775-1041` |
| | Why drop the classifier; the idea | `:783, :799` |
| | **Theorem (the CFG identity)** | `:811` |
| | Proof outline; Step 1 invert Bayes; Step 2 substitute; Step 3 collect | `:826, :842, :852, :862` |
| | Proof recap — one chain | `:875` |
| | Guidance as extrapolation (figure); a dual-role network (figure) | `:888, :916` |
| | Training with condition dropout; from score to $\varepsilon$ | `:946, :962` |
| | The sampling rule; classifier-free sampler (`d5-algo`) | `:972, :982` |
| | What CFG samples (same tilt, no classifier); CFG in practice | `:1003, :1016` |
| **04 — Discrete diffusion** | | `:1043-1599` |
| | What breaks on tokens (figure); keep the recipe, change the noise | `:1051, :1079` |
| | Forward — transition matrices; example — uniform kernel | `:1094, :1107` |
| | Uniform vs. absorbing; two transition graphs (figure) | `:1117, :1142` |
| | Absorbing kernel in closed form; the continuous-time limit | `:1183, :1193` |
| | **Definition (rate matrix)** | `:1204` |
| | **Theorem (reverse rate matrix** $\bar Q_t(y,x) = \frac{p_t(y)}{p_t(x)}Q_t(x,y)$**)** | `:1217` |
| | Proof outline; Step 1 one small step; Step 2 Bayes on the pair; Step 3 limit | `:1231, :1248, :1258, :1271` |
| | Two sanity checks; proof recap — one chain | `:1281, :1295` |
| | **Definition (the discrete score = ratio vector)**; why call it a score | `:1308, :1321` |
| | Sampling the reverse chain (`d5-algo`); why the squared loss fails | `:1342, :1359` |
| | **Definition (score entropy)**; **Theorem (score entropy is a divergence)** | `:1373, :1386` |
| | Proof — differentiate in $s$; the barrier (figure); the target is unknown | `:1402, :1412, :1433` |
| | **Theorem (denoising score entropy, Lou–Meng–Ermon 2024)** | `:1445` |
| | Proof outline; Step 1 decouple; Step 2 minimize pointwise; Step 3 telescope | `:1458, :1474, :1484, :1494` |
| | Proof recap — one chain | `:1506` |
| | Sequence space ($K^L$); corrupt each position alone (Hamming-1) | `:1519, :1532` |
| | The reverse inherits the sparsity ($L(K-1)$ outputs, figure) | `:1542` |
| | Sampling a sequence (tau-leaping, `d5-algo`) | `:1570` |
| | Continuous and discrete, side by side (dictionary table) | `:1586` |
| | Series recap | `:1602` |

**Key:** Conditional-score proposition `:241`; tilted-target proposition `:445`;
coordinatewise forward lemma `:555`; exact-paste proposition `:633`; two
approximations `:657`; CFG identity theorem `:811`; rate-matrix definition
`:1204`; reverse-rate theorem `:1217`; discrete-score definition `:1308`; score
entropy `:1373`; score entropy is a divergence `:1386`; denoising score entropy
theorem `:1445`; Hamming-1 sparsity `:1532, :1542`.

**Companion note** (`diffusion5-guidance-discrete-note.html`): tilted fixed
point with proof and the "the tilt is not a diffusion" caveat (§1.4–§1.5),
coordinatewise forward lemma and exact-paste proposition with the tower
decomposition and the two named approximations (§2.3a–§2.3b), the reverse-rate
formula proved by infinitesimal Bayes plus two sanity checks (§5.2), the
fine-grid limit that justifies the word "score" (§5.2a), and denoising score
entropy with its full three-step proof (§6.6).

---

## llm.html — Brief LLM Overview

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:1-67` |
| **01 — Setup** | | `:72-119` |
| | Why this brief LLM pass | `:80` |
| | Tokens and sequences ($\mathcal{V}$, BPE) | `:93` |
| | **Autoregressive factorization** + LLM = $p_\theta(\cdot\mid x_{<t})$ | `:108` |
| **02 — Architecture** | | `:121-180` |
| | **Decoder-only transformer (allyouneed.png)** | `:131` |
| | Logits → softmax next-token distribution | `:151` |
| | **Sequential generation (cascade.png)** — autoregressive inference loop | `:166` |
| **03 — Training** | | `:181-278` |
| | **Pretraining objective** (per-token NLL / cross-entropy) | `:191` |
| | Scale (corpus, params) → memorization is real | `:206` |
| | **Post-training I — SFT** (data / loss / effect / output bullets, masked NLL) | `:231` |
| | **Post-training II — Preference setup** (RLHF vs DPO motivation) | `:246` |
| | **DPO loss** (full formula, implicit reward, NPO preview for unlearning) | `:263` |
| **04 — Sampling and privacy hooks** | | `:279-369` |
| | **Sampling — Temperature** (logit def, $\tau\to 0,1,\infty$ limits) | `:289` |
| | **Sampling — Truncation** (top-$k$, top-$p$ nucleus) | `:305` |
| | **Per-token signals → privacy** (4-card map) | `:322` |
| | Roadmap to next four lectures | `:349` |
| Closer (Q&A) | | `:364` |

**Key references:** autoregressive factorization `:113`; decoder-only image `:135`; sequential-generation cascade `:171`; pretraining loss `:194`; SFT loss `:241`; **preference setup** `:246`; **DPO loss + NPO preview** `:263-275`; temperature sampling `:294`; truncation rules `:309`; 4-card privacy map `:326-346`.

**Image assets:** `allyouneed.png` (Vaswani et al. transformer figure), `cascade.png` (converted from `cascade.webp`, autoregressive decoding cascade) — both in this folder, inlined by `scripts/bundle.py`.

**Privacy-series hooks established here:**
- $p_\theta(\cdot\mid x_{<t})$ — central object referenced by every subsequent deck
- Per-token loss $\ell_t$ — the leak signal in MIA (`privacy/lectures/04-mia/mia5-llm.html`) and memorization (`privacy/lectures/03-memorization/memorization-llm.html`)
- Sampling step — where watermarks (`privacy/lectures/06-watermark/watermark.html`) modify outputs
- Weight edit on conditionals — unlearning (`privacy/lectures/05-unlearning/unlearning1-foundations.html`, `unlearning2-llm.html`)

---

## note/2_difffusion.tex

LaTeX source — rigorous write-up of foundational diffusion material:
- Sec 1: Generative models (distribution learning, sampling, Cauchy, inverse transform)
- Sec 2: 1D diffusion — VE forward + Bayes-route reverse

Underlying material for Diffusion Lectures 1–2 (the deck versions are condensed presentations of this).
