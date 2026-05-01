# privacy/ — Privacy series

Six sub-tracks: diffusion (foundations course, no notes), DP (single NeurIPS 2023 talk), MIA (5-lecture series with paired notes), plus three single-deck topics — memorization, unlearning, watermarking. Together they form the privacy / copyright / provenance stack.

## Subfolders

- **`diffusion/`** — Diffusion generative models from scratch (5 lectures). No companion `-note.html` files; proofs are in-deck. `note/2_difffusion.tex` is LaTeX source covering Lectures 1–2. See `diffusion/OUTLINE.md`.
- **`dp/`** — Differential privacy + federated learning (NeurIPS 2023 talk). Single deck `DP-FL.html` plus `dp-fl.txt` (compressed handout) and `figs/`. See `dp/OUTLINE.md`.
- **`mia/`** — Membership inference attacks (5 lectures, paired notes). Plus legacy `old/MIA.html`. See `mia/OUTLINE.md`.
- **`memorization/`** — Memorization in language models (single deck). Carlini extraction, scaling laws, books/production extraction, copyright. See `memorization/OUTLINE.md`.
- **`unlearning/`** — Machine unlearning (single comprehensive deck). Definitions, classification methods, LLM methods, benchmarks, lab work. Source: `slide.pdf` (the talk Albert gave on this topic). See `unlearning/OUTLINE.md`.
- **`watermark/`** — LLM watermarking (single deck). Green-list, distortion-free, undetectable, robustness, radioactivity. See `watermark/OUTLINE.md`.

## Quick lookup

| Topic | Where | Lines |
|---|---|---|
| Bayes-route reverse derivation | `diffusion/diffusion1-foundations.html` | `:194-345` |
| Tweedie's formula | `diffusion/diffusion1-foundations.html` | `:374` |
| DDPM VP forward + VLB + ε-loss | `diffusion/diffusion2-ddpm.html` | `:90-333` |
| Fokker–Planck + Anderson reverse SDE | `diffusion/diffusion3-sde-score.html` | `:135-315` |
| Score-matching theorem | `diffusion/diffusion3-sde-score.html` | `:339` |
| DDIM (deterministic, ODE, inversion) | `diffusion/diffusion4-ddim.html` | `:134-281` |
| Classifier-free guidance | `diffusion/diffusion5-guidance-discrete.html` | `:202-282` |
| Discrete diffusion + score-entropy loss | `diffusion/diffusion5-guidance-discrete.html` | `:287-425` |
| (ε,δ)-DP definition | `dp/DP-FL.html` | `:375-395` |
| Local DP minimax rate | `dp/DP-FL.html` | `:483` |
| PrivUnit mechanism | `dp/DP-FL.html` | `:523` |
| **RRSC + k-closest exact-optimality (NeurIPS 2023)** | `dp/DP-FL.html` | `:571-822` |
| DP-Diffusion / DP-RDM | `dp/DP-FL.html` | `:852-1004` |
| Yeom overfitting bound | `mia/mia3-theory.html` | `:143` |
| Sablayrolles BB≈WB | `mia/mia3-theory.html` | `:436` |
| LiRA | `mia/mia4-modern.html` | `:264-503` |
| RMIA | `mia/mia4-modern.html` | `:647-720` |
| InfoRMIA (LLM token-level) | `mia/mia5-llm.html` | `:427-590` |
| Memorization — canary entropy + exposure null | `memorization/memorization.html` | `:194-235` |
| Counterfactual + long-tail (Feldman) | `memorization/memorization.html` | `:277-302` |
| Carlini scaling laws + repetition formal | `memorization/memorization.html` | `:353-380` |
| Min-K%++ probe | `memorization/memorization.html` | `:412` |
| Cooper book extraction | `memorization/memorization.html` | `:453` |
| Certified $(\varepsilon,\delta)$ unlearning | `unlearning/unlearning.html` | `:175` |
| Newton-step / Sekhari capacity theorems | `unlearning/unlearning.html` | `:189-216` |
| Influence function | `unlearning/unlearning.html` | `:259` |
| SCRUB / SalUn / $\ell_1$-sparse | `unlearning/unlearning.html` | `:276-318` |
| IDI / COLA (lab) | `unlearning/unlearning.html` | `:396-424` |
| GA collapse + NPO bounded + SimNPO | `unlearning/unlearning.html` | `:479-538` |
| TOFU / WMDP / RWKU / MUSE benchmarks | `unlearning/unlearning.html` | `:648-702` |
| Benign + syntactic relearning | `unlearning/unlearning.html` | `:705-728` |
| Pawelczyk verification hardness | `unlearning/unlearning.html` | `:748` |
| Kirchenbauer green-list + entropy bound | `watermark/watermark.html` | `:164-222` |
| Gumbel-max trick + proof | `watermark/watermark.html` | `:252-295` |
| Aaronson distortion-free proof | `watermark/watermark.html` | `:325` |
| Edit-distance robustness theorem | `watermark/watermark.html` | `:356` |
| Christ–Gunn–Zamir undetectable + construction | `watermark/watermark.html` | `:386-419` |
| Adaptive / WaterMax | `watermark/watermark.html` | `:486-516` |
| SynthID-Text production | `watermark/watermark.html` | `:542` |

## Theme connections

- **diffusion ↔ MIA**: diffusion-model MIA is a research frontier — `mia/mia4-modern.html:731-789` covers it. The diffusion-models theory in `privacy/diffusion/` provides the substrate.
- **DP ↔ MIA**: `mia/mia1-foundations.html:601-617` shows DP as MIA bound (`Adv ≤ e^ε−1+δ`); `dp/DP-FL.html` builds the DP machinery. DP-SGD is referenced from `mia/mia4-modern.html:117`.
- **DP ↔ unlearning**: certified $(\varepsilon,\delta)$-unlearning reuses the DP definition from `dp/DP-FL.html:375` — same bound, different distribution comparison.
- **memorization ↔ unlearning ↔ MIA**: memorization is the *signal* unlearning aims to remove and MIA aims to detect. `memorization/memorization.html` motivates the other two; defenses slide flows directly into `unlearning/`. `unlearning/unlearning.html:317` reuses the SALUN MIA-Efficacy column.
- **memorization ↔ watermark**: both about provenance under copyright pressure, but opposite directions — memorization detects unintended retention, watermarking adds intended traceability. Same lawsuits motivate both.
- **dgMARK ↔ watermark**: lab thread for diffusion LLMs — full context in `dllm/dllm.html:524-569`, broader watermark survey here.
- **Theoretical diffusion (`infotheory/diffusion/`) vs from-scratch (`privacy/diffusion/`)**: same math, different presentation. The infotheory series uses information-theoretic / hierarchical-VAE framing (cleaner for theory students); the privacy series uses the Bayes-+-Taylor route and goes further (5 lectures including SDE, DDIM, CFG, discrete).
