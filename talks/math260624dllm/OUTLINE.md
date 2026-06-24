# math260624dllm/ — Diffusion LLMs (mathematics-conference version)

Invited talk for a **mathematics** audience: **Why Diffusion LLMs Behave Differently, and How to Control Them.** Same arc as the KICS version (`../kics260521dllm/`) but reworked for mathematicians — more Gaussian SDE theory, deeper SEDD/RADD, a formal problem statement for DAPD, and all secondary lab work compressed to two slides. June 2026.

Sibling deck: `../kics260521dllm/kics260521dllm.html` (general-audience original). Reuse figures, differentiate depth.

## Files

- `math260624dllm.html` — the deck (31 slides)
- `gpt-image.png` — OpenAI GPT-Image illustrative sample, "learn a distribution, then sample" motivation (slide 3; OpenAI image-gen cookbook)
- `sde.png` — Song et al. SDE forward/reverse figure (slide 4)
- `scaling.png` — data-constrained scaling Pareto, Prabhudesai et al. (slide 16)
- `sahoo-pareto.png` — speed–quality Pareto (Fig 1) from `github.com/s-sahoo/scaling-dllms`, Sahoo et al. ICML 2026 (slide 17)
- `mercury.png` — Inception Labs Mercury preview image (slide 18; public og:image)
- `diffusiongemma.png` — Google DiffusionGemma preview image (slide 18; public og:image, converted from webp)
- `infotheoreticdllm.png`, `a2d.png`, `dgmark.png`, `reversalcurse.png` — legacy lab figures (carried from KICS deck; **not used** in this version's compressed lab slides, kept for parity)

## math260624dllm.html

**Topic:** The mathematics of masked discrete diffusion — Gaussian foundations, concrete-score losses, and parallel decoding as graph coloring.

Citations sit bottom-left beside the brand footer (local `<style>` override).

### Sections (31 slides)

No contents slide — title flows straight into the first divider.

- **01 · Diffusion** (divider slide 2) — Gaussian SDEs through discrete-diffusion losses, one arc
  - Image Generation: Learn a Distribution, then Sample — `gpt-image.png`, two-step framing (learn $p_\theta\approx p_{\text{data}}$ / sample $x\sim p_\theta$); OpenAI GPT-Image illustrative sample (3)
  - Continuous Diffusion at a Glance — `sde.png`, Song et al. ICLR 2021 (4)
  - Itô Diffusion and Anderson's Theorem — forward Itô SDE + Anderson reverse SDE (same marginals); Fokker–Planck named as the key to the proof (5)
  - Sampling: Integrate the Reverse SDE — forward/reverse same-marginals diagram, generation = draw $\bar X_T\sim\mathcal N(0,I)$ then integrate down (6; modeled on privacy diffusion3 slide 19)
  - Masked Diffusion at a Glance — vertical token diagram, Austin et al. NeurIPS 2021 (7)
  - AR vs Diffusion LLMs comparison table (8)
  - Discrete Analogue: A Ratio, Not a Gradient — CTMC rate matrix $Q_t$ + concrete-score reverse rate (merged concept + SEDD setup); reverse-rate identity credited to Kelly 1980, Sun et al. ICLR 2023 (9)
  - SEDD — Score Entropy: A Tractable Loss: full SE loss, Bregman + denoising note (10)
  - RADD — Absorbing Score Is Time-Free: factorization theorem, $t$-independence (11)
  - RADD — Training = Any-Order GPT: cross-entropy on a random position given any partial subsequence (no ELBO/Bregman framing) (12)

- **02 · The dLLM** (divider slide 13)
  - What a Trained dLLM Gives You — universal marginal predictor $p_\theta(x_i\mid x_S)$ (14)
  - LLaDA & LLaDA 2.0 — Nie et al. NeurIPS 2025 (15)
  - Diffusion Beats AR Under Data Scarcity — `scaling.png`, Prabhudesai et al. NeurIPS 2025 (16)
  - Scaling Beyond Masked Diffusion — `sahoo-pareto.png`, MDLM/Duo/Eso-LMs frontier, Sahoo et al. ICML 2026 (`github.com/s-sahoo/scaling-dllms`) (17)
  - dLLMs in Practice — Mercury (Inception) | DiffusionGemma (Google) two-panel, 1.5× larger images (18)

- **03 · DAPD** (divider slide 19 — lists authors: Bumjun Kim\*, Dongjae Jeon\*, Moongyu Jeon\*, Albert No)
  - Why Parallel Decoding? — NFE motivation (20)
  - Parallel Decoding: A Formal Problem — independence-iff-factorizes + total correlation $\mathrm{TC}$ (21)
  - The Challenge: Marginals, not the Joint (22)
  - Sampling on a Dependency Graph — two-option SVG diagram (23)
  - Greedy: Unmask a Maximum Independent Set — MIS each step ≈ where prior parallel-decoding work sits (implicitly/explicitly); locally optimal, global problem is coloring (24)
  - Parallel Sampling = Graph Coloring — edge ⇔ TC>ε, steps = χ(G) (25)
  - Attention = Dependency Oracle — symmetric score $s_{ij}$, TC surrogate (26)
  - Algorithm: Coloring with Lookahead — Welsh–Powell (27)

- **04 · More from the Lab** (divider slide 28)
  - Rainbow Padding: Curing <eos> Overflow — compressed single slide, EOS bias formula + fix (29)
  - More from the Lab — 2×2 grid: info-theoretic diffusion, reversal curse, A2D, dgMARK (30)

- Q&A end slide (31)

### Key formulas / claims

| Item | Slide |
|---|---|
| Forward Itô SDE + Anderson reverse SDE (Fokker–Planck = proof key) | 5 |
| Sampling = draw `\bar X_T ~ N(0,I)`, integrate reverse SDE to t=0 | 6 |
| CTMC reverse rate / concrete score `\bar Q_t(x,y) = (p_t(y)/p_t(x)) Q_t(y,x)` (Kelly 1980; Sun et al. 2023) | 9 |
| SEDD score-entropy loss (Bregman, denoising form) | 10 |
| RADD time-free factorization `s_t = ((1-α_t)/α_t) · p_θ(y\|x_t^unmasked)` | 11 |
| Training = any-order GPT: CE on `x_0^{σ(k)} \| x_0^{σ(<k)}` | 12 |
| DAPD independence criterion + total correlation `TC = D_KL(joint ‖ ∏ marginals)` | 21 |
| Greedy maximum independent set per step (locally optimal; global = coloring) | 24 |
| Parallel steps = chromatic number `χ(G)`, edge ⇔ TC>ε | 25 |
| Symmetric attention dependency score `s_ij = (a_ij + a_ji)/2` | 26 |
| EOS positional bias `Pr_θ(eos\|i) ↑ as i → N` | 29 |

### Citations

External: Song et al. (ICLR 2021), Anderson (1982), Vincent (Neural Comp. 2011), Austin et al. (NeurIPS 2021), Kelly "Reversibility and Stochastic Networks" (1980) + Sun et al. score-based CT discrete diffusion (ICLR 2023) [reverse-rate identity, slide 8], Lou–Meng–Ermon SEDD (ICML 2024), Ou et al. RADD (NeurIPS 2024), Nie et al. LLaDA (NeurIPS 2025), Prabhudesai et al. (NeurIPS 2025), Sahoo et al. "Scaling Beyond Masked Diffusion Language Models" (ICML 2026; `github.com/s-sahoo/scaling-dllms`), Berglund et al. reversal curse (ICLR 2024), Inception Labs Mercury (2026), Google DeepMind DiffusionGemma (2026).

Lab: Rainbow Padding (Kim, Jeon, Kim, Jeung, No — ICLR 2026); DAPD (Kim, Jeon, Jeon, No — ICML 2026); A2D (Jeung et al. — ICLR 2026); dgMARK (Hong, No — ICML 2026); Reversal Curse in MDMs (Jeon et al. — preprint 2026); Information-Theoretic Discrete Diffusion (Jeon, Shin, Jeon, No — NeurIPS 2025).

### Companion content

None. For deeper Gaussian diffusion theory (Fokker–Planck proof, Anderson proof, Vincent score-matching theorem), see `courses/privacy/lectures/02-generative/diffusion3-sde-score.html`.
