# infotheory/lectures/07-diffusion/ — Diffusion as Hierarchical VAE (3 lectures)

Information-theoretic treatment: VAE/ELBO → hierarchical VAE = diffusion → parameterizations + Tweedie + channel view. Each deck paired with `-note.html` for full derivations.

## Files

| Deck | Note | Topic |
|---|---|---|
| `diff1-vae-elbo.html` | `diff1-vae-elbo-note.html` | Variational bound and the VAE |
| `diff2-diffusion.html` | `diff2-diffusion-note.html` | Diffusion as a hierarchical VAE |
| `diff3-parameterizations.html` | `diff3-parameterizations-note.html` | Predict x₀, noise, or score — parameterizations and Tweedie |

---

## diff1-vae-elbo.html — Variational bound and the VAE

| Section | Slide content | Line |
|---|---|---|
| Title / Contents | | `:19, :30` |
| **01 — Why a bound** | Latent-variable models, intractable likelihood | `:58-89` |
| | Latent-variable model | `:66` |
| | Maximum likelihood is blocked | `:74` |
| | Plan: variational posterior | `:82` |
| **02 — ELBO: two paths, one bound** | Jensen + KL identity | `:91-128` |
| | Path 1 (Jensen on log-expectation) | `:98` |
| | Path 2 (KL identity) | `:105` |
| | Same bound, different stories | `:112` |
| **03 — What the bound asks** | Reconstruction − rate | `:130-194` |
| | Two seams of the joint (factorization table) | `:137` |
| | ELBO decomposes | `:148` |
| | Reconstruction — what it computes | `:155` |
| | Gaussian decoder — reconstruction is MSE | `:162` |
| | Rate vs distortion | `:169` |
| | Why prior KL = rate ($I(X;Z)$ + marginal mismatch) | `:186` |
| **04 — The VAE** | Instantiating the ELBO with concrete choices | `:196-291` |
| | From ELBO to algorithm (three design choices) | `:203` |
| | VAE architecture (diagram: $x \to$ encoder $\to z \to$ decoder $\to \hat x$) | `:214` |
| | Gaussian encoder | `:233` |
| | Closed-form KL (prior explicit) | `:241` |
| | Gradient problem | `:249` |
| | Reparameterization trick (consolidated) | `:257` |
| | VAE loss = negative ELBO (recon + rate) | `:266` |
| | Posterior collapse | `:274` |

**Key formulas:** ELBO `:101`; two seams of the joint `:137`; reconstruction = MSE `:162`; prior KL = rate `:186`; Gaussian KL `:241`; reparameterization `:257`; VAE loss `:266`.

### Note (`diff1-vae-elbo-note.html`)
- Why intractable integral matters (MC variance, importance sampling) `:29`
- KL gap and posterior approximation `:35`
- Reparameterization as pathwise derivative; Gumbel-softmax / score-function alternatives `:51`
- Closed-form Gaussian KL `:68`
- Posterior collapse diagnostics (per-dim KL, free bits) `:80`
- The ELBO: one quantity, six faces (Forms 1–6 map) `:90`
- Information-theoretic ELBO interpretation, β-VAE tradeoff `:149`
- Bridge to diffusion `:168`

---

## diff2-diffusion.html — Diffusion as hierarchical VAE

| Section | Slide content | Line |
|---|---|---|
| Title / Contents | | `:19, :31` |
| **01 — Forward chain** | VP forward, frozen encoder | `:58-93` |
| | VP setup | `:66` |
| | **Lemma — q(x_t\|x_0) closed form** (induction shown in full) | `:74` |
| | Master reparameterization | `:86` |
| **02 — Reverse chain** | Learned Gaussian kernels | `:95-141` |
| | Generative model | `:103` |
| | Diffusion is hierarchical VAE (diagram) | `:110` |
| **03 — ELBO decomposition** | $L_T + \sum L_{t-1} + L_0$; derive via Bayes + telescope | `:142-199` |
| | Apply Lecture 1 ELBO; chain factorization + Bayes trick | `:150` |
| | Split and telescope (Bayes-split log; telescoping identity) | `:158` |
| | **Collect into three terms** (defines $L_T, L_{t-1}, L_0$) | `:166` |
| | $L_T$: prior matching (no training) | `:177` |
| | $L_0$: final reconstruction | `:184` |
| | Interior $L_{t-1}$ — only $\theta$-dependent term; need closed-form posterior | `:192` |
| **04 — DDPM target** | Closed-form $q(x_{t-1}\mid x_t,x_0)$; KL → MSE on mean | `:201-238` |
| | **Closed form by complete-the-square** (full algebra: expand both log-Gaussians, match precision + mean) | `:209` |
| | $L_{t-1}$ becomes MSE on the mean | `:222` |
| | Three parameterizations of $\mu_\theta$ | `:229` |

**Key:** q(x_t\|x_0) lemma + induction `:74`; chain-factor ELBO + Bayes substitution `:150`; split + telescope `:158`; three-term ELBO `:166`; interior $L_{t-1}$ `:192`; reverse conditional Gaussian (DDPM), complete-the-square algebra now on-slide `:209`; KL→MSE `:222`. Full numeric sanity check still lives in `diff2-diffusion-note.html`.

### Note (`diff2-diffusion-note.html`)
- Variance-preserving vs variance-exploding `:25`
- ELBO expansion — deck now derives this in full on-slide; note keeps only the shared-parameters-across-$t$ remark, pointer to deck `:31`
- Why linear-Gaussian reverse stays Gaussian `:36`
- **Complete the square** — deck now derives this in full on-slide; note trimmed to a pointer plus the weighted-average-in-the-limit remark `:42`
- Why L_T vanishes `:48`
- L_0 treatment `:54`
- Numerical sanity check `:60`
- Connection to rate–distortion `:67`

---

## diff3-parameterizations.html — Three Tools, One Model

Reframed: diffusion as a working example of three information-theoretic techniques (ELBO, Tweedie, Fisher divergence), not a self-contained diffusion tutorial.

| Section | Slide content | Line |
|---|---|---|
| Title / Contents | | `:19, :31` |
| **01 — Diffusion recap** | The model we will analyze | `:63-90` |
| | The forward-reverse machine | `:71` |
| | Three predictions, one object | `:79` |
| **02 — Tool 1: Variational bound** | ELBO reduces training to MSE | `:87-122` |
| | Recall — ELBO bounds the intractable | `:95` |
| | Diffusion ELBO decomposes ($L_T + \sum L_t + L_0$) | `:104` |
| | Interior term = MSE on the mean | `:111` |
| **03 — Tool 2: Tweedie's formula** | Posterior mean = rescaled score | `:119-160` |
| | **Theorem (Robbins/Tweedie)** | `:127` (statement `:129`) |
| | **Proof — differentiate the marginal** (diff-under-integral shown; solve-for step shown) | `:138` |
| | Tweedie unifies the predictions (derivation of $\mathbb{E}[\varepsilon\mid x_t]$ shown, not asserted) | `:150` |
| **04 — Tool 3: Fisher divergence** | ELBO MSE = score gap = DSM | `:161-217` |
| | Recall — Fisher divergence (Lecture 6) | `:169` |
| | Step 1 — apply Tweedie to both means | `:178` |
| | Step 2 — MSE becomes Fisher | `:188` |
| | Step 3 — recognize denoising form (substituted Fisher expression with $s_\theta$ shown; Vincent DSM) | `:196` |
| | **Theorem — ELBO $\equiv$ Sum of DSM** | `:206` |
| **05 — Convergence** | Three roads, one objective | `:218-253` |
| | Three tools, one loss (chained equation) | `:226` |
| | The information-theoretic arc | `:241` |

**Key:** Tweedie theorem `:127` (statement `:129`); Tweedie proof `:138`; three predictions unified (derivation shown) `:150`; ELBO $\equiv$ DSM theorem `:206` (capstone); three-tool convergence `:226`.

### Note (`diff3-parameterizations-note.html`)
- Why ε-prediction wins (loss conditioning at noise level) `:25`
- Tweedie in exponential-family form (Efron 2011) `:36`
- Score-matching vs denoising loss (Vincent 2011) `:53`
- Why all three give same model `:65`
- Channel-coding view detail (SNR, successive refinement) `:71`
- Log-SNR view (Salimans &amp; Ho) `:83`
- Connection to rate-distortion `:94`
- Score-matching equivalence (cites Lecture 6 / `divergence/div2` for Fisher + DSM); corrected to reference deck Section 04, where the capstone proof actually lives `:100`
