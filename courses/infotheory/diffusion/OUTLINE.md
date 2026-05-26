# infotheory/diffusion/ — Diffusion as Hierarchical VAE (3 lectures)

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
| Title / Contents | | `:19, :30` |
| **01 — Forward chain** | VP forward, frozen encoder | `:58-90` |
| | VP setup | `:66` |
| | **Lemma — q(x_t\|x_0) closed form** | `:76` |
| | Master reparameterization | `:83` |
| **02 — Reverse chain** | Learned Gaussian kernels | `:92-138` |
| | Generative model | `:100` |
| | Diffusion is hierarchical VAE (diagram) | `:107` |
| **03 — ELBO decomposition** | $L_T + \sum L_{t-1} + L_0$; derive via Bayes + telescope | `:139-194` |
| | Apply Lecture 1 ELBO; chain factorization + Bayes trick | `:147` |
| | Split and telescope (Bayes-split log; telescoping identity) | `:155` |
| | **Collect into three terms** (defines $L_T, L_{t-1}, L_0$) | `:163` |
| | $L_T$: prior matching (no training) | `:174` |
| | $L_0$: final reconstruction | `:181` |
| | Interior $L_{t-1}$ — only $\theta$-dependent term; need closed-form posterior | `:188` |
| **04 — DDPM target** | Closed-form $q(x_{t-1}\mid x_t,x_0)$; KL → MSE on mean | `:198-232` |
| | **Closed form by complete-the-square** (merged Bayes + lemma) | `:206` |
| | $L_{t-1}$ becomes MSE on the mean | `:217` |
| | Three parameterizations of $\mu_\theta$ | `:224` |

**Key:** q(x_t\|x_0) `:76`; chain-factor ELBO + Bayes substitution `:147`; split + telescope `:155`; three-term ELBO `:163`; interior $L_{t-1}$ `:189`; reverse conditional Gaussian (DDPM) `:206`; KL→MSE `:217`. Complete-the-square algebra lives in `diff2-diffusion-note.html`.

### Note (`diff2-diffusion-note.html`)
- Variance-preserving vs variance-exploding `:25`
- Detailed ELBO expansion `:31`
- Why linear-Gaussian reverse stays Gaussian `:49`
- **Complete the square — full derivation** (algebra for $\tilde\mu_t, \tilde\beta_t$) `:55`
- Why L_T vanishes `:82`
- L_0 treatment `:88`
- Numerical sanity check `:94`
- Connection to rate–distortion `:101`

---

## diff3-parameterizations.html — Three Tools, One Model

Reframed: diffusion as a working example of three information-theoretic techniques (ELBO, Tweedie, Fisher divergence), not a self-contained diffusion tutorial.

| Section | Slide content | Line |
|---|---|---|
| Title / Contents | | `:19, :30` |
| **01 — Diffusion recap** | The model we will analyze | `:63-85` |
| | The forward-reverse machine | `:70` |
| | Three predictions, one object | `:78` |
| **02 — Tool 1: Variational bound** | ELBO reduces training to MSE | `:87-117` |
| | Recall — ELBO bounds the intractable | `:94` |
| | Diffusion ELBO decomposes ($L_T + \sum L_t + L_0$) | `:103` |
| | Interior term = MSE on the mean | `:110` |
| **03 — Tool 2: Tweedie's formula** | Posterior mean = rescaled score | `:119-154` |
| | **Theorem (Robbins/Tweedie)** | `:126` |
| | **Proof — differentiate the marginal** | `:137` |
| | Tweedie unifies the predictions (bridge to Tool 3) | `:146` |
| **04 — Tool 3: Fisher divergence** | ELBO MSE = score gap = DSM | `:156-209` |
| | Recall — Fisher divergence (Lecture 6) | `:163` |
| | Step 1 — apply Tweedie to both means | `:172` |
| | Step 2 — MSE becomes Fisher | `:182` |
| | Step 3 — recognize denoising form (Vincent DSM) | `:190` |
| | **Theorem — ELBO $\equiv$ Sum of DSM** | `:198` |
| **05 — Convergence** | Three roads, one objective | `:211-253` |
| | Three tools, one loss (chained equation) | `:218` |
| | The information-theoretic arc | `:233` |

**Key:** Tweedie theorem `:126`; Tweedie proof `:137`; three predictions unified `:146`; ELBO $\equiv$ DSM theorem `:198` (capstone); three-tool convergence `:218`.

### Note (`diff3-parameterizations-note.html`)
- Why ε-prediction wins (loss conditioning at noise level) `:25`
- Tweedie in exponential-family form (Efron 2011) `:36`
- Score-matching vs denoising loss (Vincent 2011) `:53`
- Why all three give same model `:65`
- Channel-coding view detail (SNR, successive refinement) `:71`
- Log-SNR view (Salimans &amp; Ho) `:83`
- Connection to rate-distortion `:94`
- Score-matching equivalence (cites Lecture 6 / `divergence/div2` for Fisher + DSM) `:99`
