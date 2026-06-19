# math260624dllm/ — Diffusion LLMs (mathematics-conference version)

Invited talk for a **mathematics** audience: **Why Diffusion LLMs Behave Differently, and How to Control Them.** Same arc as the KICS version (`../kics260521dllm/`) but reworked for mathematicians — more Gaussian SDE theory, deeper SEDD/RADD, a formal problem statement for DAPD, and all secondary lab work compressed to two slides. June 2026.

Sibling deck: `../kics260521dllm/kics260521dllm.html` (general-audience original). Reuse figures, differentiate depth.

## Files

- `math260624dllm.html` — the deck (31 slides)
- `sde.png` — Song et al. SDE forward/reverse figure (slide 4)
- `scaling.png` — data-constrained scaling Pareto (slide 18)
- `mercury.png` — Inception Labs Mercury preview image (slide 19; public og:image)
- `diffusiongemma.png` — Google DiffusionGemma preview image (slide 19; public og:image, converted from webp)
- `infotheoreticdllm.png`, `a2d.png`, `dgmark.png`, `reversalcurse.png` — legacy lab figures (carried from KICS deck; **not used** in this version's compressed lab slides, kept for parity)

## math260624dllm.html

**Topic:** The mathematics of masked discrete diffusion — Gaussian foundations, concrete-score losses, and parallel decoding as graph coloring.

Citations sit bottom-left beside the brand footer (local `<style>` override).

### Sections (31 slides)

- **Framing** — Title (1), Contents 5-part (2)

- **01 · Gaussian Diffusion Theory** (divider slide 3)
  - Continuous Diffusion at a Glance — `sde.png`, Song et al. ICLR 2021 (4)
  - Forward SDE and Its Marginal Law — VP/VE Itô SDE + Fokker–Planck PDE (5, **new**)
  - Reverse SDE and the Score — Anderson reverse SDE + probability-flow ODE + score matching (6, **new**)
  - Masked Diffusion at a Glance — vertical token diagram, Austin et al. NeurIPS 2021 (7)
  - AR vs Diffusion LLMs comparison table (8)
  - Discrete Analogue: A Ratio, Not a Gradient — CTMC forward/reverse rates (9)

- **02 · Discrete Diffusion and Its Losses** (divider slide 10)
  - SEDD — Concrete Score and the Reverse Rate: rate matrix $Q_t$, reverse rate via concrete score (11, **new**)
  - SEDD — Score Entropy: A Tractable Loss: full SE loss, Bregman + denoising note (12)
  - RADD — Absorbing Score Is Time-Free: factorization theorem (13)
  - RADD — ELBO = Any-Order Autoregressive NLL: NELBO → reweighted CE → random-order AR (14, **new**)
  - What a Trained dLLM Gives You — universal marginal predictor $p_\theta(x_i\mid x_S)$ (15)

- **03 · dLLMs at Scale and in Practice** (divider slide 16)
  - LLaDA & LLaDA 2.0 — Nie et al. NeurIPS 2025 (17)
  - Diffusion Beats AR Under Data Scarcity — `scaling.png`, Prabhudesai et al. NeurIPS 2025 (18)
  - dLLMs in Practice — Mercury (Inception) | DiffusionGemma (Google) two-panel (19, **new**)

- **04 · DAPD** (divider slide 20)
  - Why Parallel Decoding? — NFE motivation (21)
  - Parallel Decoding: A Formal Problem — independence-iff-factorizes + total correlation $\mathrm{TC}$ (22, **new**)
  - The Challenge: Marginals, not the Joint (23)
  - Sampling on a Dependency Graph — two-option SVG diagram (24)
  - Parallel Sampling = Graph Coloring — edge ⇔ TC>ε, steps = χ(G) (25)
  - Attention = Dependency Oracle — symmetric score $s_{ij}$, TC surrogate (26)
  - Algorithm: Coloring with Lookahead — Welsh–Powell (27)

- **05 · More from the Lab** (divider slide 28)
  - Rainbow Padding: Curing <eos> Overflow — compressed single slide, EOS bias formula + fix (29)
  - More from the Lab — 2×2 grid: info-theoretic diffusion, reversal curse, A2D, dgMARK (30)

- Q&A end slide (31)

### Key formulas / claims

| Item | Slide |
|---|---|
| Forward SDE + Fokker–Planck PDE | 5 |
| Anderson reverse SDE + probability-flow ODE | 6 |
| Discrete forward/reverse CTMC rates `\bar Q_t = Q_t · p_t(x)/p_t(y)` | 9 |
| SEDD reverse rate matrix `\bar Q_t(x,y) = (p_t(y)/p_t(x)) Q_t(y,x)` | 11 |
| SEDD score-entropy loss (Bregman, denoising form) | 12 |
| RADD time-free factorization `s_t = ((1-α_t)/α_t) · p_θ(y\|x_t^unmasked)` | 13 |
| RADD: absorbing NELBO = reweighted CE = random-order AR NLL | 14 |
| DAPD independence criterion + total correlation `TC = D_KL(joint ‖ ∏ marginals)` | 22 |
| Parallel steps = chromatic number `χ(G)`, edge ⇔ TC>ε | 25 |
| Symmetric attention dependency score `s_ij = (a_ij + a_ji)/2` | 26 |
| EOS positional bias `Pr_θ(eos\|i) ↑ as i → N` | 29 |

### Citations

External: Song et al. (ICLR 2021), Anderson (1982), Vincent (Neural Comp. 2011), Austin et al. (NeurIPS 2021), Lou–Meng–Ermon SEDD (ICML 2024), Ou et al. RADD (NeurIPS 2024), Nie et al. LLaDA (NeurIPS 2025), Prabhudesai et al. (NeurIPS 2025), Kim–Shah et al. confidence decoding (ICML 2025), Berglund et al. reversal curse (ICLR 2024), Inception Labs Mercury (2026), Google DeepMind DiffusionGemma (2026).

Lab: Rainbow Padding (Kim, Jeon, Kim, Jeung, No — ICLR 2026); DAPD (Kim, Jeon, Jeon, No — ICML 2026); A2D (Jeung et al. — ICLR 2026); dgMARK (Hong, No — ICML 2026); Reversal Curse in MDMs (Jeon et al. — preprint 2026); Information-Theoretic Discrete Diffusion (Jeon, Shin, Jeon, No — NeurIPS 2025).

### Companion content

None. For deeper Gaussian diffusion theory (Fokker–Planck proof, Anderson proof, Vincent score-matching theorem), see `courses/privacy/lectures/02-generative/diffusion3-sde-score.html`.
