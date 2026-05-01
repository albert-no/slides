# privacy/diffusion/ — Diffusion generative models (5-lecture series)

Master-level course on diffusion: Bayes-route foundations → DDPM → SDE → DDIM → guidance + discrete diffusion. Companion notes: `diffusion3-sde-score-note.html` (off-slide proof detail for Lecture 3). `note/2_difffusion.tex` is LaTeX source covering Lectures 1–2.

## Files

| Deck | Topic |
|---|---|
| `diffusion1-foundations.html` | Generative models, VE forward, Bayes-route reverse, Tweedie |
| `diffusion2-ddpm.html` | VP forward, DDPM, VLB three-term decomposition, ε-loss |
| `diffusion3-sde-score.html` | Continuous-time SDE, Fokker–Planck, Anderson reverse, score matching |
| `diffusion4-ddim.html` | Non-Markovian forward, deterministic sampling, probability-flow ODE |
| `diffusion5-guidance-discrete.html` | Classifier guidance, CFG, inpainting, discrete diffusion |
| `note/2_difffusion.tex` | LaTeX source for Lectures 1–2 (rigorous mathematical write-up) |

---

## diffusion1-foundations.html — Foundations

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:1-68` |
| **01 — Generative models** | | `:72-129` |
| | Realistic is not enough | `:81` |
| | Sampling is non-trivial (Cauchy) | `:96` |
| | Inverse transform sampling (1D) | `:107` |
| | High dimension breaks this | `:118` |
| **02 — VE forward process** | | `:134-178` |
| | Forward `X^(n) = X^(n-1) + Z^(n)` | `:143` |
| | n steps in one shot | `:155` |
| | Terminal distribution | `:166` |
| | Goal: reverse the chain | `:178` |
| **03 — Reverse via Bayes** | Taylor + complete-square route | `:194-345` |
| | Setup | `:203` |
| | Proof outline | `:212` |
| | Step 1: Taylor expand P_X | `:226` |
| | Step 2: approximate P_Y | `:235` |
| | Step 3: substitute back | `:249` |
| | **Step 4: complete the square — KEY reverse conditional** | `:262` |
| | Reverse conditional, compactly (score) | `:287, :290` |
| | Reverse sampling rule | `:298` |
| | Why not subtract noise? | `:308` |
| **04 — Score function & Tweedie** | | `:353-424` |
| | Score function `s(x;n) = ∂_x log P_{X^(n)}` | `:362` |
| | **Tweedie's formula (Robbins 1956)** | `:374, :378` |
| | Train a denoiser, not a score | `:388` |
| | Denoiser-to-score conversion | `:399, :405` |

**Key:** Reverse conditional `:287-290`; Tweedie `:378-380`; denoiser-to-score `:405`.

---

## diffusion2-ddpm.html — DDPM

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:1-85` |
| **01 — VP forward** | | `:90-170` |
| | Why variance preserving | `:99` |
| | **VP forward** `X^(n) = √(1−β_n) X^(n-1) + √β_n Z^(n)` | `:114` |
| | n steps in one shot, `ᾱ_n = ∏(1−β_i)` | `:126, :129` |
| | **MGF definition + Lévy continuity** | `:139, :142` |
| | **Convergence: MGF proof** → `N(0,1)` | `:155, :158` |
| **02 — DDPM reverse** | | `:173-225` |
| | Reverse conditional, VP version | `:182` |
| | **Why not train µ directly** (score is the only unknown) | `:193` |
| | **Two routes to the score**: Tweedie (Lec 1) vs VLB (this lecture) | `:206` |
| **03 — Variational lower bound** | | `:228-460` |
| | **Maximum likelihood objective** (max log p_θ ↔ min NLL ↔ KL) | `:237` |
| | **Marginal is intractable** (high-dim integral, need an upper bound) | `:248` |
| | **Forward chain is Markov** + Bayes-on-chain identity | `:263` |
| | Likelihood → VLB (Jensen) | `:288` |
| | **Factor and telescope** (factor q + Markov + cancel → factored ratio) | `:301` |
| | **Three-term decomposition `L_N + Σ L_{n-1} + L_0`** | `:311` |
| | L_N: match the prior | `:320` |
| | **L_{n-1}: match each reverse step (training signal)** | `:335` |
| | **Target posterior `q(X^(n-1)\|X^(n),X^(0))` is exactly Gaussian** | `:348` |
| | Bayes derivation of posterior | `:362` |
| | **Not ordinary mean matching**: µ_n sees X^(0), µ_θ does not | `:376` |
| | **Mean matching → score matching** (substitute conditional score) | `:389` |
| | **ε ↔ score visual** (anti-parallel, scaled) | `:399` |
| | **ε-Reparameterization**: `s_θ = −ε_θ/√(1−ᾱ_n)` | `:436` |
| | **ε-Prediction Loss**: plain regression on noise | `:448` |
| **04 — Algorithms** | | `:450-538` |
| | Training algorithm (5 steps) | `:459` |
| | Sampling algorithm | `:476` |
| | **Three approximation errors** (forward+reverse chain, ①②③ cards) | `:495` |

**Key:** VP forward `:114`; one-shot `:129`; MGF def `:142`; MGF proof `:158`; MLE `:237`; Markov `:265`; VLB three-term `:303`; posterior exact `:340`; non-trivial mean matching `:368`; ε↔score `:391`; ε-loss `:437`; three-error chain `:495`.

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
| **02 — Non-Markovian forward** | | `:134-237` |
| | Setup | `:142` |
| | **DDIM forward — mixing recipe** (signal + recycled + fresh, coefficients TBD) | `:154` |
| | **Pin down $a_n$** (DDPM marginal ⇒ $a_n^2 + \sigma^2 = 1-\bar\alpha_n$, σ free) | `:164` |
| | **Forward conditional** (read off recipe as $q(X^{(n)}\|X^{(n+1)},X^{(0)})$) | `:176` |
| | **Marginals match DDPM (claim + proof by induction)** | `:190, :202` |
| | DDPM as special case | `:215` |
| | σ_n→0: deterministic forward | `:225` |
| **03 — Sampling** | | `:213-318` |
| | Training unchanged (same ε-net) | `:221` |
| | **DDIM sampling — the idea** (overview: estimate $\hat{X}^{(0)}$, plug in) | `:234` |
| | **Predicted clean signal** $\hat{X}^{(0)}$ | `:245` |
| | DDIM reverse update | `:254` |
| | Sampling algorithm | `:263` |
| | **Deterministic DDIM ($\sigma_n=0$)** — explicit map | `:284` |
| | **Continuous-time limit** ($\tau_t$ change of variable) | `:293` |
| | **Probability-flow ODE** | `:303` |
| **04 — Consequences** | | `:319-385` |
| | **Three benefits of determinism** (fewer steps, inversion, interpolation) | `:327` |
| | DDPM or DDIM? | `:353` |

**Key:** Marginal invariance `:164-167`; sampling overview `:234`; predicted-clean inversion `:245`; PF-ODE derivation `:284, :293, :303`.

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

## note/2_difffusion.tex

LaTeX source — rigorous write-up of foundational material:
- Sec 1: Generative models (distribution learning, sampling, Cauchy, inverse transform)
- Sec 2: 1D diffusion — VE forward + Bayes-route reverse

Underlying material for Lectures 1–2 (the deck versions are condensed presentations of this).
