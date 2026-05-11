# infotheory/lossy/ — Lossy compression (4 lectures)

Rate–distortion theory from Shannon's theorem to modern applied LLM compression. Each deck paired with `-note.html`.

## Files

| Deck | Note | Topic |
|---|---|---|
| `lossy1-foundations.html` | `lossy1-foundations-note.html` | Rate–distortion foundations |
| `lossy2-gaussian-laplacian.html` | `lossy2-gaussian-laplacian-note.html` | Gaussian/Laplacian + Shannon LB + pruning + CROM |
| `lossy3-lattice-quip.html` | `lossy3-lattice-quip-note.html` | Lattice codes, QUIP, QUIP# |
| `lossy4-turboquant.html` | `lossy4-turboquant-note.html` | TURBOQUANT — online VQ via random rotations |

---

## lossy1-foundations.html — R(D) foundations

Section 05 collapsed: the binary toy now lives inside section 04 as the worked random-coding example, between Converse and the formal achievability slides.

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:74, :85` |
| **01 — Problem setup** | Distortion, block codes, achievable region | `:113-183` |
| | Lossless not enough | `:121` |
| | Three distortion functions | `:131` |
| | Block code, per-letter distortion | `:152` |
| | Achievable region & R(D) | `:160` |
| **02 — Scalar quantization** | R∈{0,1,2}, Lloyd–Max alternating updates | `:185-372` |
| | Toy Gaussian setup (bullets + cases) | `:193` |
| | R=0: c*=μ, distortion=σ² | `:208` |
| | R=1: one threshold (scalar quantizer) | `:220` |
| | R=2: **Lloyd–Max coupling lemma** | `:229` |
| | Lloyd–Max — initial state | `:245` |
| | Lloyd–Max — Step ① (update x̂) | `:275` |
| | Lloyd–Max — Step ② (update τ) | `:305` |
| | Lloyd–Max — converged | `:335` |
| | Lloyd–Max convergence proof | `:365` |
| **03 — Why blocks win** | VQ beats SQ even on i.i.d. | `:374-506` |
| | Vector quantization | `:382` |
| | Round cells beat rectangles (5-4-5-4-5 hex tiling) | `:390` |
| | Sphere-like cells win | `:496` |
| **04 — Shannon's theorem (with binary worked example)** | Converse, optimization, binary toy, random coding | `:629-985` |
| | **Theorem statement** | `:637` |
| | **What are we optimizing over?** (fixed/free/derived, convex program) | `:648` |
| | Why mutual information appears (intuition) | `:659` |
| | Converse — outline | `:677` |
| | Converse step 1 — rate ≥ I (DPI) | `:689` |
| | Converse step 2 — single-letterize | `:700` |
| | Converse step 3 — convexity | `:711` |
| | Converse — summary | `:723` |
| | Binary toy — setup | `:735` |
| | **Solving the optimization (binary)** — α derivation of $1{-}H_b(D)$ | `:747` |
| | Binary R(D) and the test channel | `:755` |
| | One source, many candidates (X has 12 ones) | `:764` |
| | **Codebook of 24 candidates** ($R \approx 0.191 > R(D)$, match at $m=18$) | `:792` |
| | Empirical joint matches the test channel — exact $9,3,3,9$ | `:834` |
| | Ball volume = typical-set size | `:866` |
| | Threshold rate from ball volume | `:877` |
| | **What if we pick a wrong marginal?** — Sanov rate $\rho(p,D)$ | `:886` |
| | **Penalty in numbers** — Bern(1/2) vs Bern(1/4) vs Bern(1/8) | `:898` |
| | From binary toy to general recipe | `:913` |
| | Generalization — the optimal test channel | `:924` |
| | Achievability — random codebook | `:938` |
| | Achievability — joint AEP | `:947` |
| | **Biased binary — setup** | `:958` |
| | **Biased binary — lower bound** (chain of inequalities) | `:969` |
| | **Biased binary — achievability** ($q = (p-D)/(1-2D)$) | `:985` |
| | **Biased binary — $R(D)$ and codebook law** | `:995` |
| | **Biased binary — plug in: $p=0.2, D=0.1$** | `:1006` |
| | **Biased binary — trivial regime $D \ge p$** | `:1017` |
| | **Forbidden reproduction — setup** (distortion table) | `:1029` |
| | **Forbidden — constraint forces structure** ($p(0,1)=0$) | `:1045` |
| | **Forbidden — marginal & $I(\alpha)$** | `:1054` |
| | **Forbidden — solving the optimization** (derivative) | `:1063` |
| | **Forbidden — compared to symmetric** (numerics table) | `:1072` |
| | **Uniform ternary — setup** ($Z = U\ominus V$) | `:1089` |
| | **Uniform ternary — chain of inequalities** | `:1097` |
| | **Uniform ternary — Shannon lower bound** | `:1113` |
| | **Uniform ternary — computing $\phi(D)$** | `:1122` |
| | **Uniform ternary — achievability** | `:1133` |
| Recap / End | | `:1147` |

**Key:** Achievable region `:160`; Lloyd–Max examples `:245, :275, :305, :335`; Shannon theorem `:637`; what we optimize `:648`; converse `:677–:723`; binary worked example `:735–:877`; binary optimization `:747`; suboptimal codebook penalty `:886, :898`; achievability `:938, :947`; biased binary `:958–:1017` (6 slides); forbidden reproduction `:1029–:1072` (5 slides); ternary uniform `:1089–:1133` (5 slides).

### Note (`lossy1-foundations-note.html`)
- Lossless vs lossy continuous sources
- Distortion modeling
- Block-code definition
- Achievable region convexity
- Distortion-ball cover of typical set
- R=1 Gaussian computation
- Lloyd–Max convergence detail
- VQ vs SQ details
- Random-coding rare-event bound
- Search creates dependence
- Volume-counting threshold

---

## lossy2-gaussian-laplacian.html — Gaussian, Laplacian, Shannon LB, pruning, CROM

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:19, :30` |
| **01 — Gaussian R(D)** | (1/2)log(σ²/D), achievability + converse, plug-ins | `:107-251` |
| | Statement | `:115` |
| | Achievability — backward Gaussian channel | `:122` |
| | Achievability — shell-cover picture | `:132` |
| | **Example — Heights ($\mu=170, \sigma^2=10$)**: scalar vs $R(D)$ | `:186` |
| | **Example — Plug in $\sigma^2 = 10$**: each bit cuts $D$ by 4 | `:202` |
| | Forward form — linear shrinkage | `:219` |
| | Converse — Gaussian maximizes entropy | `:228` |
| | Converse — sphere cover | `:236` |
| **02 — Shannon lower bound** | Gaussian = worst case | `:310-345` |
| | Statement (squared error) | `:318` |
| | Proof — maximize entropy of error | `:327` |
| | Gaussian hits the bound — hardest source | `:337` |
| **03 — Laplacian R(D)** | Atom at zero in optimal reproduction, plug-in | `:347-419` |
| | Setup + statement | `:355` |
| | Converse — auxiliary density trick | `:384` |
| | Achievability — sparse mixture | `:393` |
| | **Example — Plug in $\lambda = 1$**: sparsity grows as $D^2$ | `:404` |
| **04 — Pruning from R(D)** | Optimal NN compression is sparse | `:421-477` |
| | Network and compressed weights | `:429` |
| | **Theorem — weight-distortion bounds output-distortion** | `:437` |
| | Trained weights are Laplacian-like | `:446` |
| | Optimal Laplacian code is a sparsifier | `:459` |
| | Pruning is optimal | `:468` |
| **05 — EVT and CROM** | Rateless lossy via extremes | `:480-525` |
| | Extremes are almost predictable | `:488` |
| | CROM (send index, reconstruct spike) | `:497` |
| | Random rotations Gaussianize | `:506` |
| | Iterate with random rotations | `:514` |
| Recap | | `:530` |

**Key:** Gaussian R(D) `:115`; backward channel `:122`; heights example `:186`; Gaussian plug-in `:202`; Shannon LB `:318`; auxiliary density trick `:384`; Laplacian plug-in `:404`; layer-wise telescoping `:437`.

**Bug fixed:** literal `<` inside math (e.g. `0<D\le σ²`) was being parsed as start of `<i>`/`<D>` tags by the HTML lexer, cascading garbage into all subsequent slides. Replaced with `&lt;` at lines 73, 79, 174.

### Note (`lossy2-gaussian-laplacian-note.html`)
- Backward vs forward channel
- Auxiliary-density trick derivation
- Laplacian mixture verification (characteristic functions)
- Atom-at-zero is not artifact
- Why L1 not L2 for pruning
- Why CROM rotations Gaussianize

---

## lossy3-lattice-quip.html — Lattice codes, QUIP, QUIP#

Lecture-mode rewrite: encoder bottleneck spelled out (codebook table at low $d$, codebook size denoted $M = 2^{dR}$); arithmetic-in-quantized-space section opens with the naive dequant→add→requant baseline before the integer-add identity; lattice section with basis-vector / no-overlap-hex Voronoi / `e8.jpg` Coxeter image; explicit $\mathbb{Z}^8$-is-scalar vs $E_8$-coset comparison; dedicated slides on **how to pick the ball radius** (match typical set) and **$\mathcal{O}(d)$ $E_8$ rounding** (two-coset trick); QUIP uses $W_\Delta = \widehat W - W$ (not just $\Delta$).

**LDLQ section is reorganized** for pedagogical flow (2026-05-11 rewrite):

1. **Proxy setup.** Output objective → surrogate $W_\Delta$ → trace trick → proxy $\ell = \mathrm{tr}(W_\Delta H W_\Delta^\top)$ → what $H$ is (calibration covariance, *not* loss Hessian) → Hessian-tells-what-matters.
2. **Build the family, then pick $U$.** DPCM intuition → introduce the **linear-feedback family** $\widehat W = Q(W + (W-\widehat W)\,U)$ with $U$ str. upper triangular → why upper-triangular = causal feedback → **proxy in feedback form** $\widehat W - W = \eta\,(I+U)^{-1}$, giving $\ell = \mathrm{tr}(\eta\,(I+U)^{-1}\,H\,(I+U)^{-\top}\,\eta^\top)$ → **LDL of $H$ cancels** the cross-terms when $U \leftarrow \bar U$, leaving $\ell = \mathrm{tr}(\eta\,D\,\eta^\top)$.
3. **Algorithm + theorem.** LDLQ card → what $\bar U, D$ mean (Gram-Schmidt under $H$-inner-product) → Theorem 1 (worst-case $(m/4)\,\mathrm{tr}(D)$, average $(m/c)\,\mathrm{tr}(D)$, $c=12$ nearest / $6$ stochastic) → what Theorem 1 means ($\mathrm{tr}(D)/\mathrm{tr}(H) \le 0.65$ on OPT).
4. **Then add rotation.** Why outliers wreck quantization → incoherence definition → conjugation preserves the proxy (rotation orthogonals $U, V$ + $\widetilde H = V H V^\top$) → random rotation erases outliers (CLT; run LDLQ on $\widetilde W$ with $\widetilde H$).
5. **QUIP end-to-end** diagram $x \to V \to \widehat W \to U^\top \to y$.

**Key rewrite move:** the proxy is rewritten in the feedback variable $\eta$ *before* the LDL factorization is introduced, so the LDL choice $U \leftarrow \bar U$ visibly *derives* from the cancellation requirement instead of being asserted. Dropped slides: standalone "Factorizing $H$" (subsumed by "LDL Cancels"), "Gauss-Seidel on the Proxy" (duplicates DPCM), "LDLQ — Why the Correction" (subsumed by feedback-form + LDL-cancels). New slides: **Linear-Feedback Family**, **Proxy in Feedback Form**, **LDL of $H$ Cancels the Cross-Terms**.

QUIP\# section: BlockLDLQ broken into scalar-vs-block comparison + Theorem 4.1 bound slide; BlockLDLQ comparison cards use tight math-block margins.

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:19, :30` |
| **01 — The encoder problem** | Codebook size + search are both gigantic | `:63-141` |
| | What a real quantizer must do | `:71` |
| | Optimal VQ — what the encoder does (single $\mathcal{C}$+argmin block) | `:83` |
| | **The codebook is gigantic** ($M = 2^{dR}$ table, d=2,4,6,8 at R=4) | `:91` |
| | Encoding — a search you cannot run | `:111` |
| | Two escape routes | `:124` |
| **02 — Computing in quantized space** | Linear quantization preserves arithmetic | `:142-207` |
| | Uniform quantization (definition) | `:150` |
| | **The naive path — dequant → add → requant** (the wasteful baseline) | `:162` |
| | Quantized values still add (integer add on the grid) | `:173` |
| | Quantized values multiply (by integers) | `:182` |
| | Matrix-vector product, integer GEMM | `:191` |
| | The MSE penalty is small (≤1.53 dB) | `:199` |
| **03 — Lattice codes** | High-level; algebra replaces search | `:208-446` |
| | From cube grid to lattice (basis-vector viz) | `:216` |
| | **Voronoi cells — round beats square** (hex tiling redrawn, no overlap) | `:261` |
| | **Encoding: round, don't search** (worked $\mathbb{Z}^d$ example) | `:300` |
| | **Decoding: index → codeword** (E_8 ∩ ball = Gaussian typical set) | `:309` |
| | **$\mathbb{Z}^8$ is just scalar quantization** (cube cells, kissing 16) | `:326` |
| | **$E_8$ — one extra coset buys a round cell** ($E_8 = D_8 \cup (D_8 + \tfrac12\mathbf{1})$) | `:336` |
| | Why dimension 8? (Viazovska 2017, sweet spot) | `:348` |
| | **Visualizing $E_8$** — 240 tangent neighbors (`e8.jpg` right, kissing-number card left) | `:366` |
| | Finite codebook from a lattice | `:391` |
| | **Picking the ball — match the typical set** (ball radius $\sigma\sqrt{d}$) | `:403` |
| | **Rounding to $E_8$ in $\mathcal{O}(d)$** (two-coset algorithm spelled out) | `:415` |
| | Is it OK to use a lattice codebook? | `:427` |
| **04 — QUIP: incoherence processing** | Chee, Cai, Kuleshov, De Sa 2023 | `:447-715` |
| | We care about output, not weights | `:455` |
| | Surrogate — one layer at a time ($W_\Delta = \widehat W - W$, not $\Delta$) | `:464` |
| | **The trace trick** (step-by-step derivation, all in $W_\Delta$) | `:474` |
| | The proxy loss (linebreak-split highlight) | `:486` |
| | **What is $H$?** — calibration input covariance, *not* loss Hessian | `:498` |
| | The Hessian tells us what matters | `:506` |
| | **The idea — predict and correct (DPCM)** (high-level motivation, no math) | `:517` |
| | **The linear-feedback family** ($\widehat W = Q(W + (W-\widehat W)U)$, $U$ str. upper-triangular) | `:529` |
| | **Why "upper triangular"?** (causal-feedback intuition) | `:541` |
| | **Quantization residual $\eta$** — recall $\ell(\widehat W)$, define $\eta = Q(z) - z$, $\widehat W = z + \eta$ | `:549` |
| | **Proxy in feedback form** ($\widehat W - W = \eta(I+U)^{-1}$ → $\ell = \mathrm{tr}(\eta(I+U)^{-1}H(I+U)^{-\top}\eta^\top)$) | `:558` |
| | **LDL of $H$ cancels the cross-terms** ($H=(I+\bar U)D(I+\bar U)^\top$ → $\ell=\mathrm{tr}(\eta D\eta^\top)$) | `:567` |
| | **LDLQ — round with memory** (algorithm card; factorization spelled out) | `:576` |
| | **What $\bar U$ and $D$ mean** (Gram-Schmidt under $H$-inner-product) | `:588` |
| | **Worst-case and average proxy loss** (definitions; $\mathbb E\eta_{ij}^2 = \tfrac14, \tfrac1{12}, \tfrac16$) | `:607` |
| | **LDLQ is optimal (Theorem 1)** — worst $(m/4)\mathrm{tr}(D)$, avg $(m/c)\mathrm{tr}(D)$ | `:619` |
| | **What Theorem 1 means** — empirical $\mathrm{tr}(D)/\mathrm{tr}(H) \le 0.65$ across every OPT 125m–2.7b layer | `:632` |
| | Why outliers wreck quantization (motivates incoherence) | `:644` |
| | Incoherence — no outliers | `:666` |
| | **Conjugation preserves the proxy** (rotation $U, V$ + definition of $\widetilde H$) | `:675` |
| | Random rotation erases outliers (CLT half; LDLQ on $\widetilde W$ with $\widetilde H$) | `:686` |
| | QUIP — end to end ($V \to \widehat W \to U^\top$ inference diagram) | `:694` |
| **05 — QUIP#: Hadamard + lattice** | Tseng, Chee, Sun, Kuleshov, De Sa 2024 | `:718-841` |
| | Two upgrades over QUIP | `:726` |
| | **What is a Hadamard matrix?** ($H_8$ viz, bullets right) | `:743` |
| | Why Hadamard is fast enough | `:774` |
| | Random signs make it incoherent | `:783` |
| | $E_8$ codebook — decoded by index | `:792` |
| | **Scalar LDLQ vs BlockLDLQ** (stacked cards, equations on single lines) | `:803` |
| | BlockLDLQ — bound (Theorem 4.1) | `:819` |
| | Two-faced effective codebook | `:829` |
| Recap / End | | `:847, :857` |

**Key:** Codebook table (M, not K) `:91`; naive dequant→add→requant `:162`; integer add identity `:173`; hex Voronoi tiling fix `:261`; Z^8 vs E_8 coset intuition `:326, :336`; **e8.jpg viz** `:366`; **ball radius + O(d) rounding** `:403, :415`; **trace trick in $W_\Delta$** `:474`; **DPCM intuition** `:517`; **linear-feedback family** `:529`; **quantization residual $\eta$ + proxy in feedback form** `:549, :558`; **LDL cancels cross-terms** (the key derivation) `:567`; **LDLQ algorithm card** `:576`; **worst-case + avg definitions** `:607`; **Theorem 1 + interpretation** `:619, :632`; **conjugation preserves proxy** `:675`; **QUIP inference diagram** `:694`; **$H_8$ Hadamard viz** `:743`; scalar-vs-block LDLQ comparison `:803`.

**Papers:**
- QUIP — Chee, Cai, Kuleshov, De Sa, NeurIPS 2023 (arXiv:2307.13304)
- QUIP# — Tseng, Chee, Sun, Kuleshov, De Sa, ICML 2024 (arXiv:2402.04396)
- Viazovska, Ann. of Math. 2017 (E₈ sphere packing)

### Note (`lossy3-lattice-quip-note.html`)
- Codebook size — concrete numbers (4 KB → 275 GB)
- Why encoder search is intractable (LSH/kd-trees don't save it)
- Uniform quantization arithmetic — addition, integer scaling, inner product
- 1.53 dB high-resolution penalty
- Lattice as additive subgroup, translation symmetry
- E₈ construction, kissing number 240, Viazovska 8D optimality
- E₈ fast-rounding algorithm (4 steps)
- Proxy loss derivation, layer-wise greedy, orthogonal invariance
- Why outliers wreck quantization (dynamic range argument)
- Formal incoherence definition
- Why Kronecker rotation (cost vs uniform random)
- **LDLQ — full statement, feedback intuition, DPCM analogy, Theorem 1**
- LDLQ ↔ OPTQ/GPTQ equivalence
- Hadamard basics, FWHT, why random signs are necessary
- Berry-Esseen + union-bound argument for RHT incoherence
- BlockLDLQ Theorem 4.1
- E8P codebook compression (16 → 8-bit lookup, 1 KB)
- Practical caveats (calibration, scales, RVQ, fine-tuning, non-power-of-2)

---

## lossy4-turboquant.html — TURBOQUANT (online VQ for KV cache)

Front motivation now opens with self-attention (Q/K/V) before the KV cache, so the inner-product structure is established before we ask what to quantize. Part 06 spells out the actual implementation: K and V both use TURBOQUANT_prod (one composed call, not two parallel quantizers), with a slide on practical pieces (RHT, precomputed codebook, seeded sketch).

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:71, :84` |
| **KV cache intro** | Attention foundation / cache / vs weights / constraints | `:122-195` |
| | Self-attention: Q/K/V (`qkv.png` large + Levine CS182sp21 cite; no "two-IP" trailing line) | `:122` |
| | What is the KV cache? (growing-cache flow, 50 GB; sentences split across lines) | `:138` |
| | KV cache vs weight quantization (storage vs memory, visual contrast) | `:155` |
| | Compression constraints (online / data-obl / attention-preserving) | `:183` |
| **01 — Setup, rotation idea** | Random rotation → known coordinate distribution | `:196-282` |
| | Why scalar quantization fails | `:203` |
| | Random rotation creates a known law | `:214` |
| | **Picture: Slicing the sphere** (SVG sphere + chord) | `:223` |
| | **Lemma 1 — coordinate of a sphere point** | `:252` |
| | Two metrics, two quantizers (MSE vs IP design) | `:263` |
| **02 — MSE TURBOQUANT** | Target 4^{−b}, pipeline, algorithm, theorem | `:283-376` |
| | **Target: 4^{−b} — the Gaussian limit** (R(D) plug-in) | `:290` |
| | Pipeline: rotate, quantize, derotate (4-box diagram) | `:300` |
| | Algorithm: TURBOQUANT_mse | `:331` |
| | One-bit anchor 1−2/π | `:346` |
| | **Theorem: TURBOQUANT_mse** | `:354` |
| | **Proof — orthogonal invariance + Panter–Dite** | `:365` |
| **03 — Lower bound** | Yao + constant gap | `:377-394` |
| | Yao + constant gap (Sphere SLB *formal* + Picture: Covering both dropped; converse cited from Lec 2) | `:384` |
| **04 — Inner-product bias** | Good MSE ≠ good projections | `:395-444` |
| | One-bit MSE shrinks projections | `:402` |
| | Geometric reason — shrunken norm (vector visual) | `:410` |
| **05 — JL, QJL & inner-product TURBOQUANT** | JL lemma → QJL → two-stage | `:476-602` |
| | **Johnson–Lindenstrauss lemma (formal)** — $k = \mathcal{O}(\varepsilon^{-2}\log n)$ pairwise distances | `:452` |
| | **JL intuition** — $\chi^2$ concentration; broken into separate single-claim paragraphs | `:463` |
| | **JL preserves inner products** — polarization identity | `:476` |
| | **From JL to QJL** — 1-bit sign quantization of the sketch | `:485` |
| | QJL definition | `:493` |
| | **Lemma — QJL unbiased, 1/d variance** | `:500` |
| | Two-stage decomposition (residual-arrow visual) | `:510` |
| | Algorithm: TURBOQUANT_prod | `:548` |
| | **Theorem: TURBOQUANT_prod** | `:562` |
| **06 — KV cache implementation** | What/how it actually runs | `:576-657` |
| | **Which quantizer for K and V?** (both → TURBOQUANT_prod) | `:583` |
| | **TURBOQUANT_prod wraps TURBOQUANT_mse** (composition, not parallel) | `:600` |
| | Practical pieces (RHT $\Pi \in \mathbb R^{d\times d}$, precomputed codebook, seeded sketch) | `:615` |
| | **Dimensions used in the paper** — KV: head_dim $d{=}128$ (Llama-3.1-8B); NN: $d \in \{200, 1536, 3072\}$ | `:625` |
| | Empirical behavior (~3.5 bits/channel matches FP16; Llama-3.1-8B head dim $128$) | `:644` |
| Recap / End | | `:658, :668` |

**Key:** Q/K/V attention with large `qkv.png` (Levine CS182sp21) `:122`; Lemma 1 `:252`; Gaussian limit `:290`; pipeline diagram `:300`; TURBOQUANT_mse theorem `:354`; Yao + constant gap `:384` (Sphere SLB *and* Picture: Covering dropped — converse cited from Lec 2); **JL lemma + intuition + IP preservation + JL→QJL bridge** `:452, :463, :476, :485`; QJL lemma `:500`; two-stage visual `:510`; TURBOQUANT_prod theorem `:562`; **K/V composition `:600`**; **dimensions table** `:625` (head dim $d{=}128$ per attention head for KV; $d \in \{200, 1536, 3072\}$ for NN search).

### Note (`lossy4-turboquant-note.html`)
- KV cache — what and why (cache size formula, online/data-oblivious/attention-preserving constraints)
- Why a random rotation Gaussianizes any fixed unit vector (Haar invariance → uniform spherical → Gaussian marginal)
- Where 4^{−b} comes from (Gaussian R(D) derivation); lossy-quantizer bias (1-bit shrinks magnitude to σ√(2/π))
- Lemma 1 — full proof (slice argument + co-area Jacobian + Beta normalization + Gaussian limit)
- Lloyd–Max on f_d — alternating updates, Bennett high-resolution limit, sample-free codebook, orthogonal invariance
- Panter–Dite formula and ∫ f_d^{1/3}
- QJL lemma — unbiasedness and variance proof
- Inner-product TURBOQUANT — two-stage decomposition derivation and bit-budget split

**Audit (2026-05-11):** Slide screenshots verified at 1280×720. Fixed: `K_t\!,V_t` thin-space squashes commas → use plain comma; `QUIP\#` literal backslash → `QUIP#`; Two-Metrics highlight overlapping brand footer → trimmed intro + part-arrows; Theorem+proof one-slide overflow → split into theorem slide and proof slide; Geometric Reason `x̃` label on top of arrow → moved into wedge below arrow; Two-Stage `x̃_mse`/`r` labels cramped → repositioned with widened SVG; Algorithm+Theorem one-slide overflow → split into algorithm slide and theorem slide with aligned math block.
