# dllm/ — Diffusion LLMs (single talk)

Invited talk: **Why Diffusion LLMs Behave Differently, and How to Control Them.** Surveys five control surfaces for masked-discrete-diffusion language models. No companion notes — all proof/intuition is in-deck.

## Files

- `dllm.html` — the deck

## dllm.html

**Topic:** Inductive biases, failure modes, and control surfaces of masked discrete diffusion LLMs.

### Sections (line numbers)

- **Title / contents / framing** (`:21-180`)
  - `:21` Title slide
  - `:34` Contents (5-part outline)
  - `:84` From toy to competitive (SEDD 2023 → LLaDA 2.0 100B)
  - `:109` Masked diffusion at a glance (forward/reverse on tokens)
  - `:138` AR vs diffusion LLMs comparison table
  - `:159` Two key inductive biases (bidirectional + any-order)

- **Part I — Recent progress in field** (`:182-286`)
  - `:182` Section divider
  - `:192` SEDD: score-entropy loss (Lou et al., ICML 2024)
  - `:206` RADD: absorbing diffusion = any-order AR (Ou et al., NeurIPS 2024)
  - `:222` LLaDA: 8B-scale dLLM (Nie et al., 2025)
  - `:239` Dream 7B + LLaDA 2.0 (Ye et al. 2025; Zhu et al. 2025)
  - `:265` Field milestones table (incl. MDLM, Sahoo et al. NeurIPS 2024)

- **Part II–V — Five control surfaces** (`:287-694`)

  | Surface | Lines | Result | Citation |
  |---|---|---|---|
  | **Rainbow Padding** (robustness) | `:318-434` | Cyclic distinct pad tokens fix EOS overflow | Kim, Jeon, Kim, Jeung, No, ICLR 2026 (`:430`) |
  | **A2D** (safety) | `:436-535` | Token-level [EOS] refusal at any masked position; DIJA neutralized | Jeung et al., ICLR 2026 (`:531`) |
  | **dgMARK** (attribution) | `:537-582` | Parity-guided unmasking-order steering; logits untouched | Hong, No, preprint 2026 (`:578`) |
  | **Reversal Curse** (understanding) | `:584-670` | Shared-storage + gradient alignment → forward step decreases reverse loss | Jeon, Shin, Kim, Lee, No, arXiv:2602.02133, 2026 (`:666`) |
  | **DAPD** (decoding) | `:672-693` | Attention-induced dependency graph + independent sets | Kim, Jeon, Jeon, No, arXiv:2603.12996, 2026 (`:691`) |

- **Synthesis** (`:695-822`)
  - `:695` Section divider
  - `:705` Five surfaces, one thread
  - `:728` Practical guidance
  - `:762` Open problems
  - `:800` Key takeaways
  - `:815` Q&A end slide

### Key formulas / claims

| Item | Line |
|---|---|
| SEDD score-entropy loss `L_SE = E[Σ s_θ(y\|x_t,t) − log s_θ(x_0\|x_t,t)]` | `:198` |
| RADD factorization `s_θ(y\|x_t,t) = p(y\|x_t^unmasked) · λ(t)` | `:213` |
| EOS positional bias `p_θ(eos | i) ↑ as i → N` | `:351` |
| A2D alignment objective: maximize `E[log p_θ([EOS] | x_t, i)]` on harmful spans | `:459` |
| Attention-weight-sharing `α_{A→B} = softmax(q_A^⊤ k_B)` | `:614` |
| Gradient alignment `∇L_fwd · ∇L_rev > 0` | `:619` |

### Citations

External papers cited:
- **SEDD** — Lou, Meng, Ermon, ICML 2024 (`arXiv:2310.16834`)
- **RADD** — Ou et al., NeurIPS 2024 (`arXiv:2406.03736`)
- **MDLM** — Sahoo et al., NeurIPS 2024 (`arXiv:2406.07524`)
- **LLaDA** — Nie et al., 2025 (`arXiv:2502.09992`)
- **Dream 7B** — Ye et al., 2025 (`arXiv:2508.15487`)
- **LLaDA 2.0** — Zhu et al., 2025 (`arXiv:2512.15745`)
- **DIJA** — Wen et al., 2025 (`arXiv:2507.11097`)

Lab papers:
- **Rainbow Padding** — Kim, Jeon, Kim, Jeung, No, ICLR 2026 (`arXiv:2510.03680`)
- **A2D** — Jeung, Yoon, Cho, Jeon, Shin, Hong, No, ICLR 2026 (`arXiv:2509.23286`)
- **Reversal Curse** — Jeon, Shin, Kim, Lee, No, 2026 (`arXiv:2602.02133`)
- **DAPD** — Kim, Jeon, Jeon, No, 2026 (`arXiv:2603.12996`)
- **dgMARK** — Hong, No, preprint 2026

### Companion content

None. All material on slide. For deeper diffusion theory, see `infotheory/diffusion/` (VAE/ELBO derivations, parameterizations) and `privacy/generative/` (Bayes-route, SDE, score-matching theorem, discrete diffusion).
