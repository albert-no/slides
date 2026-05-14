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
| | Path 1 (Jensen on log-expectation) | `:99` |
| | Path 2 (KL identity) | `:106` |
| | Same bound, different stories | `:113` |
| **03 — What the bound asks** | Reconstruction − rate | `:130-161` |
| | ELBO decomposes | `:138` |
| | Rate vs distortion | `:145` |
| **04 — The VAE** | Gaussian encoder, reparam, training | `:163-227` |
| | Gaussian encoder | `:171` |
| | Reparameterization trick | `:187` |
| | **Lemma (pushforward / pathwise gradient)** | `:198` |
| | VAE training loop | `:206` |
| | Posterior collapse | `:217` |

**Key formulas:** ELBO `:101`; reparameterization identity `:189`; Lemma `:198`; Gaussian KL `:175`.

### Note (`diff1-vae-elbo-note.html`)
- Why intractable integral matters (MC variance, importance sampling) `:29`
- KL gap and posterior approximation `:35`
- Reparameterization as pathwise derivative; Gumbel-softmax / score-function alternatives `:51`
- Closed-form Gaussian KL `:68`
- Posterior collapse diagnostics (per-dim KL, free bits) `:80`
- Information-theoretic ELBO interpretation, β-VAE tradeoff `:90`
- Bridge to diffusion `:109`

---

## diff2-diffusion.html — Diffusion as hierarchical VAE

| Section | Slide content | Line |
|---|---|---|
| Title / Contents | | `:19, :30` |
| **01 — Forward chain** | VP forward, frozen encoder | `:58-90` |
| | VP setup | `:66` |
| | **Lemma — q(x_t\|x_0) closed form** | `:76` |
| | Master reparameterization | `:83` |
| **02 — Reverse chain** | Learned Gaussian kernels | `:92-118` |
| | Generative model | `:100` |
| | Diffusion is hierarchical VAE | `:107` |
| **03 — True reverse conditional** | Two Gaussians, complete the square | `:119-152` |
| | Goal and Bayes | `:127` |
| | Variance | `:134` |
| | Mean | `:142` |
| | **Lemma (Gaussian reverse conditional)** | `:145, :147` |
| **04 — ELBO decomposition** | L_T + Σ L_t + L_0; KL → MSE on mean | `:153-211` |
| | Apply Lecture 1 ELBO | `:161` |
| | Three-term decomposition | `:163, :165` |
| | L_T and L_0 boundary | `:169` |
| | Interior L_t | `:186` |
| | KL → MSE on mean | `:193, :195` |
| | Three parameterizations of μ_θ | `:200` |

**Key:** q(x_t\|x_0) `:76`; reverse conditional Gaussian `:147`; ELBO three-term `:163`.

### Note (`diff2-diffusion-note.html`)
- Variance-preserving vs variance-exploding `:25`
- Detailed ELBO expansion `:31`
- Why linear-Gaussian reverse stays Gaussian `:49`
- Why L_T vanishes `:55`
- L_0 treatment `:61`
- Numerical sanity check `:67`
- Connection to rate–distortion `:74`

---

## diff3-parameterizations.html — Parameterizations + Tweedie

| Section | Slide content | Line |
|---|---|---|
| Title / Contents | | `:19, :31` |
| **01 — Master identity** | One linear relation | `:62-77` |
| | Three variables, two free | `:71` |
| **02 — Three parameterizations** | x₀ / ε / score | `:82-115` |
| | Predict x₀ | `:91` |
| | Predict ε | `:99` |
| | Predict score | `:108` |
| **03 — Tweedie's bridge** | Posterior mean = rescaled score | `:117-158` |
| | **Theorem (Robbins/Tweedie)** | `:126` |
| | **Proof — differentiate the marginal** (split: setup + continued) | `:137, :145` |
| | Three names, one object | `:152` |
| **04 — Channel view** | Forward = noise channel, reverse = decoding | `:160-194` |
| | Each step is additive Gaussian channel | `:169` |
| | Reverse = approximate decoding | `:177` |
| | Successive refinement analogy | `:184` |
| **05 — Score-matching equivalence** | ELBO MSE $\equiv$ denoising score matching | `:196-237` |
| | A second divergence behind diffusion | `:205` |
| | **Theorem — ELBO term $\equiv$ DSM (Vincent / Song et al.)** | `:216` |
| | Two routes, one network (recap chain) | `:227` |
| | Forward pointer to `divergence/div2-fisher-score.html` | (inline in `:227`) |

**Key:** Master identity `:71`; Tweedie theorem `:126`; Tweedie proof `:137, :145`; equivalence of three predictions `:152`; ELBO $\equiv$ DSM theorem `:216`.

### Note (`diff3-parameterizations-note.html`)
- Why ε-prediction wins (loss conditioning at noise level) `:25`
- Tweedie in exponential-family form (Efron 2011) `:36`
- Score-matching vs denoising loss (Vincent 2011) `:53`
- Why all three give same model `:65`
- Channel-coding view detail (SNR, successive refinement) `:71`
- Log-SNR view (Salimans & Ho) `:83`
- Connection to rate–distortion `:94`
- Score-matching equivalence (forward pointer to `divergence/div2`) `:102`
