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

Lecture-mode rewrite: encoder bottleneck spelled out (codebook table at low $d$), new arithmetic-in-quantized-space section, lattice section with basis-vector / Voronoi / Coxeter-plane $E_8$ visualizations, lattice encode + decode shown explicitly, QUIP reframed from output → trace-trick → proxy, LDLQ shown as styled algorithm, Hadamard with $H_8$ visualization.

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:19, :30` |
| **01 — The encoder problem** | Codebook size + search are both gigantic | `:63-143` |
| | What a real quantizer must do | `:71` |
| | Optimal VQ — what the encoder does | `:83` |
| | **The codebook is gigantic** (table, d=2,4,6,8 at R=4) | `:92` |
| | Encoding — a search you cannot run | `:113` |
| | Two escape routes | `:126` |
| **02 — Computing in quantized space** | Linear quantization preserves arithmetic | `:144-198` |
| | Uniform quantization (definition) | `:152` |
| | Quantized values still add | `:164` |
| | Quantized values multiply (by integers) | `:173` |
| | Matrix-vector product, integer GEMM | `:182` |
| | The MSE penalty is small (≤1.53 dB) | `:190` |
| **03 — Lattice codes** | High-level; algebra replaces search | `:199-384` |
| | From cube grid to lattice (basis-vector viz) | `:207` |
| | **Voronoi cells — round beats square** (viz) | `:252` |
| | **Encoding: round, don't search** (worked $\mathbb{Z}^d$ example) | `:291` |
| | **Decoding: index → codeword** | `:300` |
| | Why dimension 8? (Viazovska 2017) | `:316` |
| | **Visualizing $E_8$ — 240 tangent neighbors** (Coxeter plane) | `:335` |
| | Finite codebook from a lattice | `:355` |
| | Is it OK to use a lattice codebook? | `:367` |
| **04 — QUIP: incoherence processing** | Chee, Cai, Kuleshov, De Sa 2023 | `:385-529` |
| | We care about output, not weights | `:393` |
| | Surrogate — one layer at a time | `:402` |
| | **The trace trick** (step-by-step derivation) | `:412` |
| | The proxy loss | `:424` |
| | The Hessian tells us what matters | `:433` |
| | Why outliers wreck quantization (viz) | `:444` |
| | Incoherence — no outliers | `:466` |
| | Random rotation erases outliers | `:475` |
| | **LDLQ — round with memory** (algorithm card) | `:485` |
| | LDLQ — why the correction (matrix form) | `:497` |
| | LDLQ — why it's optimal (Theorem 1) | `:506` |
| | QUIP — end to end | `:518` |
| **05 — QUIP#: Hadamard + lattice** | Tseng, Chee, Sun, Kuleshov, De Sa 2024 | `:530-641` |
| | Two upgrades over QUIP | `:538` |
| | **What is a Hadamard matrix?** ($H_8$ viz, bullets right) | `:555` |
| | Why Hadamard is fast enough | `:586` |
| | Random signs make it incoherent | `:595` |
| | $E_8$ codebook — decoded by index | `:604` |
| | BlockLDLQ — LDLQ with vector quantizers | `:615` |
| | Two-faced effective codebook | `:624` |
| Recap / End | | `:642, :655` |

**Key:** Codebook table `:92`; quantized arithmetic `:164-189`; lattice basis viz `:207`; Voronoi cells `:252`; encode/decode pair `:291, :300`; **$E_8$ Coxeter viz** `:335`; **trace trick** `:412`; LDLQ algorithm `:485`; **$H_8$ Hadamard viz** `:555`.

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

KV-cache motivation moved to the front of the deck.

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:57, :67` |
| **KV cache intro** | What it is, why compress | `:105-130` |
| | What is the KV cache? | `:105` |
| | Why compress the KV cache? | `:119` |
| **01 — Setup, rotation idea** | Random rotation → known coordinate distribution | `:132-189` |
| | Why scalar quantization fails | `:140` |
| | Random rotation creates a known law | `:151` |
| | **Lemma 1 — coordinate of a sphere point** | `:160` |
| | Two distortions | `:171` |
| **02 — MSE TURBOQUANT** | Lloyd–Max on f_d, 4^{−b} exponent | `:191-236` |
| | Algorithm: TURBOQUANT_mse (algorithmic style) | `:199` |
| | One-bit anchor 1−2/π | `:214` |
| | **Theorem and proof outline** | `:222` |
| **03 — Lower bound** | Sphere SLB + Yao | `:238-262` |
| | Sphere SLB | `:246` |
| | Yao + constant gap | `:255` |
| **04 — Inner-product bias** | Good MSE ≠ good projections | `:264-288` |
| | One-bit MSE shrinks projections | `:272` |
| | Geometric reason — shrunken norm | `:280` |
| **05 — QJL & inner-product TURBOQUANT** | Two-stage decomposition | `:290-340` |
| | QJL definition | `:298` |
| | **Lemma — QJL unbiased, 1/d variance** | `:305` |
| | Two-stage decomposition | `:315` |
| | **Algorithm and theorem (TURBOQUANT_prod)** | `:324` |
| **06 — KV cache** | Why TURBOQUANT fits the KV cache | `:342-363` |
| | Online, data-oblivious, attention-preserving | `:350` |
| Recap | | `:365` |

**Key:** Lemma 1 `:160`; TURBOQUANT_mse theorem `:222`; sphere SLB `:246`; QJL lemma `:305`; TURBOQUANT_prod `:324`.

### Note (`lossy4-turboquant-note.html`)
- KV cache — what and why (cache size formula, online/data-oblivious/attention-preserving constraints)
- Why a random rotation Gaussianizes any fixed unit vector (Haar invariance → uniform spherical → Gaussian marginal)
- Where 4^{−b} comes from (Gaussian R(D) derivation); lossy-quantizer bias (1-bit shrinks magnitude to σ√(2/π))
- Lemma 1 — full proof (slice argument + co-area Jacobian + Beta normalization + Gaussian limit)
- Lloyd–Max on f_d — alternating updates, Bennett high-resolution limit, sample-free codebook, orthogonal invariance
- Panter–Dite formula and ∫ f_d^{1/3}
- QJL lemma — unbiasedness and variance proof
- Inner-product TURBOQUANT — two-stage decomposition derivation and bit-budget split
