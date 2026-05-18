# dllm/ — Diffusion LLMs (single talk)

Invited talk: **Why Diffusion LLMs Behave Differently, and How to Control Them.** Motivates dLLMs from continuous diffusion, summarizes recent progress, then focuses on two lab papers (Rainbow Padding, DAPD) with brief mentions of A2D, dgMARK, reversal curse, info-theoretic diffusion. No companion notes — all proof/intuition is in-deck.

## Files

- `dllm.html` — the deck
- `sde.png` — Song et al. SDE forward/reverse figure (slide 3)

## dllm.html

**Topic:** Inductive biases, failure modes, and control surfaces of masked discrete diffusion LLMs.

### Sections (33 slides total)

All citations positioned beside the brand footer (bottom-left), left-aligned and full-width — see local `<style>` override at top of `dllm.html`.

- **Framing**
  - Title slide
  - Contents (5-part outline)
  - Continuous Diffusion at a Glance — `sde.png`, Song et al. ICLR 2021 Oral
  - Masked Diffusion at a Glance — vertical $x_0 \to x_t \to x_{T-1} \to x_T$ token diagram, Austin et al. NeurIPS 2021
  - AR vs Diffusion LLMs comparison table

- **Part I — Recent progress in dLLMs** (section divider 01)
  - Reverse process needs a ratio — discrete-only; forward $Q_t(x\!\to\!y)$ and reverse $\bar Q_t(y\!\to\!x)$
  - SEDD — full score-entropy loss equation, Lou, Meng, Ermon, ICML 2024
  - RADD — concrete-score factorization with $\underbrace{}$ labels, Ou et al. NeurIPS 2024
  - RADD training — CE on masked positions, $\mathcal{L}_{\text{RADD}}$ one-liner
  - "What a Trained dLLM Gives You" — $p_\theta(x_i \mid x_S)$ marginal-predictor primitive (one-line)
  - LLaDA & LLaDA 2.0 — Nie et al. NeurIPS 2025
  - Diffusion beats AR under data scarcity — `scaling.png`, Prabhudesai et al. NeurIPS 2025

- **Part II — Our lab's work** (section divider 02)
  - "A New Paradigm" emphasis slide (abstract)

  | Topic | Slides | Citation |
  |---|---|---|
  | **Rainbow Padding** (02·a divider + 5) | confidence decoding example (Kim et al. ICML 2025 Outstanding), setup, EOS overflow, root cause, scheme | Kim, Jeon, Kim, Jeung, No, ICLR 2026 |
  | **DAPD** (02·b divider + 5) | parallel as dLLM-native (diagrammatic), dependency-graph sampling, graph coloring, attention oracle, coloring algorithm | Kim, Jeon, Jeon, No, ICML 2026 |
  | **More from the lab** (02·c divider + 4) | **info-theoretic discrete diffusion (lead)**, A2D, dgMARK, reversal curse — image-only with citations | see below |

- Q&A end slide

### Key formulas / claims

| Item | Slide |
|---|---|
| Forward/reverse SDE and forward/reverse CTMC | Reverse-process-needs-a-ratio |
| SEDD score-entropy loss (full equation) | SEDD |
| RADD concrete-score factorization `s_t(y\|x_t) = ((1-α_t)/α_t) · p_θ(y\|x_t^unmasked)` | RADD |
| EOS positional bias `Pr_θ(eos\|i) ↑ as i → N` | Rainbow root cause |
| Neighbor-conditional `p(x_i \| x_{S_i})` on undirected dependency graph | DAPD/dependency-graph sampling |
| Symmetric attention dependency score `s_ij = (a_ij + a_ji)/2` | DAPD oracle |
| DAPD Welsh–Powell coloring with lookahead (4 steps) | DAPD algorithm |

### Citations

External papers cited (full titles, per venue):
- **Score SDE** — Song, Sohl-Dickstein, Kingma, Kumar, Ermon, Poole, "Score-Based Generative Modeling through Stochastic Differential Equations", ICLR 2021 Oral
- **D3PM** — Austin et al., "Structured Denoising Diffusion Models in Discrete State-Spaces", NeurIPS 2021
- **SEDD** — Lou, Meng, Ermon, "Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution", ICML 2024
- **RADD** — Ou, Nie, Xue, Zhu, Lin, Bian, Li, "Your Absorbing Discrete Diffusion Secretly Models the Conditional Distributions of Clean Data", NeurIPS 2024
- **LLaDA** — Nie et al., "Large Language Diffusion Models", NeurIPS 2025
- **LLaDA 2.0** — Zhu et al., 2025
- **Data-constrained scaling** — Prabhudesai, Wu, Zadeh, Fragkiadaki, Pathak, "Diffusion Beats Autoregressive in Data-Constrained Settings", NeurIPS 2025
- **Confidence decoding** — Kim, Shah, Kontonis, Kakade, Chen, "Train for the Worst, Plan for the Best: Understanding Token Ordering in Masked Diffusions", ICML 2025 Outstanding Paper Award
- **Reversal curse (original)** — Berglund, Tong, Kaufmann, Balesni, Stickland, Korbak, Evans, "The Reversal Curse: LLMs trained on 'A is B' fail to learn 'B is A'", ICLR 2024

Lab papers (full titles per `ai-isl.yonsei.ac.kr/publications.html`):
- **Rainbow Padding** — Kim, Jeon, Kim, Jeung, No, "Rainbow Padding: Mitigating Early Termination in Instruction-Tuned Diffusion LLMs", ICLR 2026
- **DAPD** — Kim, Jeon, Jeon, No, "Dependency-Aware Parallel Decoding via Attention for Diffusion LLMs", ICML 2026
- **A2D** — Jeung, Yoon, Cho, Jeon, Shin, Hong, No, "A2D: Any-Order, Any-Step Safety Alignment for Diffusion Language Models", ICLR 2026
- **dgMARK** — Hong, No, "dgMARK: Decoding-Guided Watermarking for Diffusion Language Models", ICML 2026
- **Reversal Curse in MDMs** — Jeon, Shin, Kim, Lee, No, "A Theoretical Analysis of Why Masked Diffusion Models Mitigate the Reversal Curse", preprint 2026
- **Information-Theoretic Discrete Diffusion** — Jeon, Shin, Jeon, No, "Information-Theoretic Discrete Diffusion", NeurIPS 2025

### Companion content

None. All material on slide. For deeper diffusion theory, see `infotheory/diffusion/` (VAE/ELBO derivations, parameterizations) and `privacy/generative/` (Bayes-route, SDE, score-matching theorem, discrete diffusion).
