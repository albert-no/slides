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

Companion notes file: `diffusion3-sde-score-note.html` (full proof derivations, sign tracking, ε-reparameterization detail).

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:1-67` |
| **01 — Discrete to continuous** | | `:72-132` |
| | VE as SDE `dX_t = √β dW_t` (full Δt → 0 derivation) | `:81` |
| | VP as SDE (OU) (full Δt → 0 derivation) | `:92` |
| | General forward SDE | `:106` |
| | Solution as a distribution | `:126` |
| **02 — Fokker–Planck** | | `:139-249` |
| | **Theorem (1D FP):** `∂_t p_t = −∂_x(f p_t) + (g²/2)∂_x² p_t` (+ SDE vs PDE contrast) | `:147, :151` |
| | Proof setup — why a test function | `:169` |
| | Proof outline | `:179` |
| | Steps 1–3 (Taylor, expectation, IBP) | `:193, :203, :212` |
| | Recap with `∫φ ∂_t p_t dx` LHS | `:223` |
| | **Vector form (multi-D, Laplacian)** | `:238` |
| **03 — Anderson's reverse SDE** | | `:254-394` |
| | **Theorem (Anderson 1982):** reverse drift = `f − g² ∂_x log p_t` | `:263, :268` |
| | **Forward+reverse diagram, same marginals** | `:275` |
| | Proof setup, outline | `:312, :325` |
| | Step 1 (reverse-time FP), Step 2 (`p_t` solves) | `:338, :349` |
| | Recap | `:362` |
| | Why Anderson matters (zero approx in continuous limit) | `:376` |
| **04 — Score matching** | | `:399-590` |
| | **Why learn the score** (DDPM vs score-based motivation) | `:410` |
| | Natural loss is intractable | `:432` |
| | **Theorem (Vincent 2011): score matching = denoising** | `:442, :446` |
| | Proof (Bayes-weighted score identity) | `:456-516` |
| | **VP kernel** (linear SDE → Gaussian, γ_t, σ_t, conditional score) | `:523` |
| | ε-reparameterization | `:535` |
| | Example: OU | `:547` |
| | Multi-dimensional extension | `:557` |
| | DDPM is discrete score matching | `:570` |

**Key theorems:** Fokker–Planck `:151`; vector form `:243`; Anderson reverse SDE `:268`; same-marginals diagram `:275`; score matching `:446`; OU kernel `:542`.

---

## diffusion4-ddim.html — DDIM

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:1-85` |
| **01 — What DDPM loss sees** | | `:90-129` |
| | DDPM ε-loss recap | `:99` |
| | **KEY: only marginals enter** | `:108` |
| | DDIM in one sentence | `:120` |
| **02 — Non-Markovian forward** | | `:134-250` |
| | **Setup** (construction order: $X^{(N)}|X^{(0)}$ first, then $X^{(n)}|X^{(n+1)},X^{(0)}$) | `:142` |
| | **DDIM forward — mixing recipe** (signal + recycled + fresh, coefficients TBD) | `:160` |
| | **Pin down $a_n$** (DDPM marginal ⇒ $a_n^2 + \sigma^2 = 1-\bar\alpha_n$, σ free) | `:172` |
| | **Forward conditional** (read off recipe as $q(X^{(n)}\|X^{(n+1)},X^{(0)})$) | `:186` |
| | **Same pair $(X^{(0)},X^{(n)})$, different triple $(X^{(0)},X^{(n)},X^{(n+1)})$** | `:200` |
| | Proof: DDPM/DDIM share the pair (backward induction) | `:215` |
| | DDPM as special case | `:229` |
| | σ_n→0: deterministic forward | `:239` |
| **03 — Sampling** | | `:252-393` |
| | Training unchanged (same ε-net) | `:261` |
| | **DDIM sampling — the idea** (overview: estimate $\hat{X}^{(0)}$, plug in) | `:274` |
| | **Predicted clean signal** $\hat{X}^{(0)}$ | `:285` |
| | DDIM reverse update | `:294` |
| | Sampling algorithm | `:303` |
| | **Deterministic DDIM ($\sigma_n=0$)** — explicit map | `:324` |
| | **Continuous-time limit** (complete ODE in ε-form, $\beta_t$ schedule) | `:334` |
| | **Probability-flow ODE** (score form) | `:348` |
| | **Three dynamics one marginal** (forward SDE, reverse SDE, reverse ODE) | `:362` |
| | **Why ODE matches via Fokker–Planck** (continuity equation = forward FP) | `:377` |
| **04 — Consequences** | | `:394-460` |
| | **Three benefits of determinism** (fewer steps, inversion, interpolation) | `:403` |
| | DDPM or DDIM? | `:429` |

**Key:** Same pair / different triple `:200`; proof of pair invariance `:215`; complete ε-form ODE `:334`; PF-ODE in score form `:348`; three-dynamics comparison `:362`; FP equivalence `:377`.

---

## diffusion5-guidance-discrete.html — Guidance + discrete diffusion

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:1-85` |
| **01 — Classifier guidance** | | `:90-163` |
| | **Why conditional generation** (text-to-image, class, inpainting, inverse) | `:99` |
| | Two approaches (per-label vs guidance) | `:115` |
| | **Bayes decomposition** `∇log P(X\|Y) = ∇log P(X) + ∇log P(Y\|X)` | `:128, :134` |
| | Time-dependent classifier on noisy inputs | `:141` |
| | Guided reverse SDE | `:152` |
| **02 — Inpainting** | | `:167-260` |
| | **What is inpainting?** (task, use cases) | `:174` |
| | Setup (Ω mask, Y observed, $\bar\Omega$ complement) | `:189` |
| | **The ideal conditional score** (and why net is out of domain) | `:203` |
| | Approximating the conditional score (noised observation $\zeta_t$) | `:216` |
| | **Why it works** | `:227` |
| | Inpainting sampler | `:241` |
| **03 — Classifier-free guidance** | | `:262-345` |
| | Why drop the classifier | `:270` |
| | **CFG identity**: `ω log P(X\|Y) + (1−ω) log P(X)` | `:283, :287` |
| | Dual-role network (drop probability `p_drop`) | `:294` |
| | **CFG sampling rule** `ε̃ = ω ε_θ(X,y) − (ω−1) ε_θ(X,∅)` | `:309` |
| | CFG in practice | `:321` |
| **04 — Discrete diffusion** | | `:347-471` |
| | What breaks (no additive noise) | `:355` |
| | Forward: transition matrices | `:369` |
| | Uniform vs absorbing | `:380` |
| | Continuous-time limit | `:401` |
| | **Reverse rate matrix**: `Q̄_t(y,x) = (p_t(y)/p_t(x)) Q_t(x,y)` (overflow fixed) | `:410` |
| | **Discrete score = ratio vector** `s(x,t)_y = p_t(y)/p_t(x)` | `:423, :426` |
| | Squared loss fails | `:436` |
| | **Score-entropy loss (Lou et al. 2024)** | `:449, :452` |
| | Sequence space (Hamming-sparsity) | `:461` |

**Key:** Conditional motivation `:99`; Bayes decomposition `:134`; inpainting task `:174`; ideal conditional score `:203`; CFG identity `:287`; CFG sampling `:309`; discrete ratio score `:426`; score entropy `:452`.

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
