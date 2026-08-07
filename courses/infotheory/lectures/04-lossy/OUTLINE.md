# infotheory/lectures/04-lossy/ — Lossy compression (4 lectures)

Rate–distortion theory from Shannon's theorem to modern applied LLM compression. Each deck paired with `-note.html`.

## Files

| Deck | Note | Topic |
|---|---|---|
| `lossy1-foundations.html` | `lossy1-foundations-note.html` | Rate–distortion foundations |
| `lossy2-gaussian-laplacian.html` | `lossy2-gaussian-laplacian-note.html` | Gaussian/Laplacian + Shannon LB + pruning + CROM |
| `lossy3-lattice-quip.html` | `lossy3-lattice-quip-note.html` | Lattice codes, QUIP, QUIP# |
| `lossy4-turboquant.html` | `lossy4-turboquant-note.html` | TURBOQUANT — online VQ via random rotations |

---

## lossy1-foundations.html — R(D) foundations (78 slides)

Section 05 collapsed: the binary toy now lives inside section 04 as the worked random-coding example, between Converse and the formal achievability slides. Grew 66→78 slides: new R(D)-intuition build-up ("What Does R=0/R=1 Mean?", "Scalar Quantization Is Partitioning", "Fix the Partition/Representatives"), a "Why Scalar Cells Are Boxes" slide, and a "Two Notions of R(D)" / "Where I(X;X̂) Sits" / "The Constraint Set" run-up before the Shannon theorem statement.

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:75, :87` |
| **01 — Problem setup** | Distortion, block codes, achievable region | `:122-183` |
| | Lossless not enough | `:122` |
| | Three distortion functions | `:132` |
| | Block code, per-letter distortion | `:153` |
| | Achievable region & R(D) | `:161` |
| **02 — Scalar quantization** | R∈{0,1,2}, Lloyd–Max alternating updates | `:194-583` |
| | Toy Gaussian setup (bullets + cases) | `:194` |
| | What does R=0 mean? | `:209` |
| | R=0: c*=μ, distortion=σ² | `:226` |
| | What does R=1 mean? | `:239` |
| | R=1: one threshold, two cells | `:262` |
| | Scalar quantization is partitioning | `:271` |
| | Fix the partition: best representative? | `:301` |
| | Fix the representatives: best partition? | `:321` |
| | R=2: **Lloyd–Max coupling lemma** | `:342` |
| | Lloyd–Max — initial state | `:358` |
| | Lloyd–Max — Step ① (update x̂) | `:388` |
| | Lloyd–Max — Step ② (update τ) | `:418` |
| | Lloyd–Max — converged | `:448, :478, :508, :538` |
| | Lloyd–Max convergence proof | `:568` |
| **03 — Why blocks win** | VQ beats SQ even on i.i.d. | `:585-756` |
| | Vector quantization | `:585` |
| | Why scalar cells are boxes | `:593` |
| | Round cells beat rectangles (5-4-5-4-5 hex tiling) | `:601` |
| | Sphere-like cells win | `:707` |
| **04 — Shannon's theorem (with binary worked example)** | Converse, optimization, binary toy, random coding | `:758-1339` |
| | Two notions of R(D) | `:758` |
| | Where I(X;X̂) sits | `:777` |
| | The constraint set: all valid test channels | `:795` |
| | **Theorem statement** | `:806-810` |
| | **What are we optimizing over?** (fixed/free/derived, convex program) | `:817` |
| | Why minimize, not maximize? | `:828` |
| | Why mutual information appears (intuition) | `:838` |
| | Same idea as channel capacity | `:856` |
| | Converse — outline | `:863` |
| | Converse step 1 — rate dominates information (DPI) | `:875` |
| | Converse step 2 — single-letterize | `:886` |
| | Converse step 3 — convexity | `:897` |
| | Converse — summary | `:909` |
| | Binary toy — setup | `:921` |
| | **Solving the optimization (binary)** — α derivation of $1{-}H_b(D)$ | `:933` |
| | Binary R(D) and the test channel | `:941` |
| | One source, many candidates (X has 12 ones) | `:950` |
| | **Codebook — candidates 1–12 of 24** ($R \approx 0.191 > R(D)$) | `:978` |
| | **Codebook — candidates 13–24 (match at $m=18$)** | `:1008` |
| | Empirical joint matches the test channel — exact $9,3,3,9$ | `:1038` |
| | Ball volume = typical-set size | `:1070` |
| | Threshold rate from ball volume | `:1081` |
| | **What if we pick a wrong marginal?** — Sanov rate $\rho(p,D)$ | `:1090` |
| | **Penalty in numbers** — Bern(1/2) vs Bern(1/4) vs Bern(1/8) | `:1102` |
| | From binary toy to general recipe | `:1118` |
| | Generalization — the optimal test channel | `:1129` |
| | Achievability — random codebook | `:1143` |
| | Achievability — joint AEP | `:1152` |
| | **Biased binary — setup** | `:1161` |
| | **Biased binary — lower bound** (chain of inequalities) | `:1172` |
| | **Biased binary — achievability** ($q = (p-D)/(1-2D)$) | `:1184` |
| | **Biased binary — $R(D)$ and codebook law** | `:1195` |
| | **Biased binary — plug in: $p=0.2, D=0.1$** | `:1206` |
| | **Biased binary — trivial regime $D \ge p$** | `:1217` |
| | **Forbidden reproduction — setup** (distortion table) | `:1228` |
| | **Forbidden — constraint forces structure** ($p(0,1)=0$) | `:1244` |
| | **Forbidden — marginal & $I(\alpha)$** | `:1253` |
| | **Forbidden — solving the optimization** (derivative) | `:1262` |
| | **Forbidden — compared to symmetric** (numerics table) | `:1271` |
| | **Uniform ternary — setup** ($Z = U\ominus V$) | `:1288` |
| | **Uniform ternary — chain of inequalities** | `:1296` |
| | **Uniform ternary — Shannon lower bound** | `:1307` |
| | **Uniform ternary — computing $\phi(D)$** | `:1316` |
| | **Uniform ternary — achievability** | `:1327` |
| Recap / End | | `:1341, :1354` |

**Key:** Achievable region `:161`; Lloyd–Max examples `:358, :388, :418, :448`; Shannon theorem `:806`; what we optimize `:817`; converse `:863–:909`; binary worked example `:921–:1081`; binary optimization `:933`; suboptimal codebook penalty `:1090, :1102`; achievability `:1143, :1152`; biased binary `:1161–:1217` (6 slides); forbidden reproduction `:1228–:1271` (5 slides); ternary uniform `:1288–:1327` (5 slides).

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

## lossy2-gaussian-laplacian.html — Gaussian, Laplacian, Shannon LB, pruning, CROM (38 slides)

Grew 34→38 slides: section 01 gained a "Recap" pair ("Recap — the Scenario", "Recap — Encode, Send, Decode") and an "Achievability — Worked Codebook" slide alongside the renamed "Achievability — the Construction".

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:67, :79` |
| **01 — Gaussian R(D)** | (1/2)log(σ²/D), achievability + converse, plug-ins | `:112-313` |
| | Recap — the scenario | `:119` |
| | Recap — encode, send, decode | `:127` |
| | Statement | `:145` |
| | Achievability — the construction | `:152` |
| | Achievability — worked codebook | `:161` |
| | Achievability — backward Gaussian channel | `:188` |
| | Achievability — shell-cover picture | `:199` |
| | **Example — Heights ($\mu=170, \sigma^2=10$)**: scalar vs $R(D)$ | `:253` |
| | **Example — Plug in $\sigma^2 = 10$**: each bit cuts $D$ by 4 | `:269` |
| | Forward form — linear shrinkage | `:286` |
| | Converse — Gaussian maximizes entropy | `:295` |
| | Converse — sphere cover | `:303` |
| **02 — Shannon lower bound** | Gaussian = worst case | `:378-410` |
| | Statement (squared error) | `:385` |
| | Proof — maximize entropy of error | `:394` |
| | Gaussian hits the bound — hardest source | `:404` |
| **03 — Laplacian R(D)** | Atom at zero in optimal reproduction, plug-in | `:415-484` |
| | Setup + statement | `:422` |
| | Converse — auxiliary density trick (KL-swap step + substitution shown) | `:451` |
| | Achievability — sparse mixture (MI derivation via $h(X)-h(N)$ shown) | `:462` |
| | **Example — Plug in $\lambda = 1$**: sparsity grows as $D^2$ | `:474` |
| **04 — Pruning from R(D)** | Optimal NN compression is sparse | `:492-546` |
| | Network and compressed weights | `:499` |
| | **Theorem — weight-distortion bounds output-distortion** (statement only; note has no proof of this bound) | `:507` |
| | Trained weights are Laplacian-like | `:516` |
| | Optimal Laplacian code is a sparsifier | `:529` |
| | Pruning is optimal | `:538` |
| **05 — EVT and CROM** | Rateless lossy via extremes | `:551-593` |
| | Extremes are almost predictable | `:558` |
| | CROM (send index, reconstruct spike) | `:567` |
| | Random rotations Gaussianize | `:576` |
| | Iterate with random rotations | `:584` |
| Recap | | `:600` |

**Key:** Gaussian R(D) `:145`; achievability construction + worked codebook `:152, :161`; backward channel `:188`; heights example `:253`; Gaussian plug-in `:269`; Shannon LB `:385`; auxiliary density trick `:451`; Laplacian achievability MI derivation `:462`; Laplacian plug-in `:474`; layer-wise telescoping `:507`.

**Bug fixed (historical):** literal `<` inside math (e.g. `0<D\le σ²`) was being parsed as start of `<i>`/`<D>` tags by the HTML lexer, cascading garbage into all subsequent slides. Fixed with `&lt;` substitutions; line numbers above are current post-edit values.

### Note (`lossy2-gaussian-laplacian-note.html`)
- Backward vs forward channel
- Auxiliary-density trick — now a pointer to the deck's on-slide KL-swap derivation (`:384`) plus the one unique bit: why $q$ is chosen Laplace-shaped
- Laplacian mixture verification (characteristic functions)
- Atom-at-zero is not artifact
- Why L1 not L2 for pruning
- Why CROM rotations Gaussianize

---

## lossy3-lattice-quip.html — Lattice codes, QUIP, QUIP# (66 slides)

Lecture-mode rewrite: encoder bottleneck spelled out (codebook table at low $d$, codebook size denoted $M = 2^{dR}$); arithmetic-in-quantized-space section opens with the naive dequant→add→requant baseline before the integer-add identity; lattice section with basis-vector / no-overlap-hex Voronoi / `e8.jpg` Coxeter image; explicit $\mathbb{Z}^8$-is-scalar vs $E_8$-coset comparison; dedicated slides on **how to pick the ball radius** (match typical set) and **$\mathcal{O}(d)$ $E_8$ rounding** (two-coset trick); QUIP uses $W_\Delta = \widehat W - W$ (not just $\Delta$).

**LDLQ section is reorganized** for pedagogical flow (2026-05-11 rewrite):

1. **Proxy setup.** Output objective → surrogate $W_\Delta$ → trace trick → proxy $\ell = \mathrm{tr}(W_\Delta H W_\Delta^\top)$ → what $H$ is (calibration covariance, *not* loss Hessian) → Hessian-tells-what-matters.
2. **Build the family, then pick $U$.** DPCM intuition → introduce the **linear-feedback family** $\widehat W = Q(W + (W-\widehat W)\,U)$ with $U$ str. upper triangular → why upper-triangular = causal feedback → **proxy in feedback form** $\widehat W - W = \eta\,(I+U)^{-1}$, giving $\ell = \mathrm{tr}(\eta\,(I+U)^{-1}\,H\,(I+U)^{-\top}\,\eta^\top)$ → **LDL of $H$ cancels** the cross-terms when $U \leftarrow \bar U$, leaving $\ell = \mathrm{tr}(\eta\,D\,\eta^\top)$.
3. **Algorithm + theorem.** LDLQ card → what $\bar U, D$ mean (Gram-Schmidt under $H$-inner-product) → Theorem 1 (worst-case $(m/4)\,\mathrm{tr}(D)$, average $(m/c)\,\mathrm{tr}(D)$, $c=12$ nearest / $6$ stochastic) → what Theorem 1 means ($\mathrm{tr}(D)/\mathrm{tr}(H) \le 0.65$ on OPT).
4. **Then add rotation.** Why outliers wreck quantization → incoherence definition → conjugation preserves the proxy (rotation orthogonals $U, V$ + $\widetilde H = V H V^\top$) → random rotation erases outliers (CLT; run LDLQ on $\widetilde W$ with $\widetilde H$).
5. **QUIP end-to-end** diagram $x \to V \to \widehat W \to U^\top \to y$.

**Key rewrite move:** the proxy is rewritten in the feedback variable $\eta$ *before* the LDL factorization is introduced, so the LDL choice $U \leftarrow \bar U$ visibly *derives* from the cancellation requirement instead of being asserted. Dropped slides: standalone "Factorizing $H$" (subsumed by "LDL Cancels"), "Gauss-Seidel on the Proxy" (duplicates DPCM), "LDLQ — Why the Correction" (subsumed by feedback-form + LDL-cancels). New slides: **Linear-Feedback Family**, **Proxy in Feedback Form**, **LDL of $H$ Cancels the Cross-Terms**.

QUIP\# section: BlockLDLQ broken into scalar-vs-block comparison + Theorem 4.1 bound slide; BlockLDLQ comparison cards use tight math-block margins.

**QUIP# section trimmed from 8 → 4 slides** (2026-08 rewrite): now "QUIP's Limitation" → "What QUIP# Fixes" → "The Hadamard/Incoherence Upgrade, Roughly" → "QUIP# — Net Effect", replacing the earlier "Two upgrades" / "What is a Hadamard matrix?" / "Why Hadamard is fast enough" / "Random signs" / "E_8 codebook" / "Scalar vs BlockLDLQ" / "BlockLDLQ bound" / "Two-faced codebook" run. Section 03 (Lattice codes) also gained new build-up slides ("The First Practical Alternative", "Can We Close the Gap?", "When Do We Actually Reach for a Lattice?", "A Concrete Example — Same Budget, Two Grids") and section 04 gained "Why Independent Rounding Leaves Value on the Table", "What $U$ Literally Does", and "Background — What Is an LDL$^\top$ Decomposition?".

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:19, :31` |
| **01 — The encoder problem** | Codebook size + search are both gigantic | `:64-149` |
| | What a real quantizer must do | `:71` |
| | Optimal VQ — what the encoder does (single $\mathcal{C}$+argmin block) | `:83` |
| | **The codebook is gigantic** ($M = 2^{dR}$ table, d=2,4,6,8 at R=4) | `:91` |
| | Encoding — a search you cannot run | `:111` |
| | Two escape routes | `:124` |
| **02 — Computing in quantized space** | Linear quantization preserves arithmetic | `:143-213` |
| | **The first practical alternative** (new: motivates scalar-per-coordinate path) | `:150` |
| | Uniform quantization (definition) | `:157` |
| | **The naive path — round-trip through floats** (the wasteful baseline) | `:169` |
| | Quantized values still add (integer add on the grid) | `:180` |
| | Quantized values multiply (by integers) | `:189` |
| | Matrix-vector product, integer GEMM | `:198` |
| | The MSE penalty is small (≤1.53 dB) | `:206` |
| **03 — Lattice codes** | High-level; algebra replaces search | `:224-489` |
| | **Can we close the gap?** (new: motivates leaving scalar quantization) | `:214` |
| | **When do we actually reach for a lattice?** (new) | `:231` |
| | **A concrete example — same budget, two grids** ($\mathbb{Z}^2$ vs $A_2$, new) | `:242` |
| | From cube grid to lattice (basis-vector viz) | `:260` |
| | **Voronoi cells — round beats square** (hex tiling redrawn, no overlap) | `:305` |
| | **Encoding: round, don't search** (worked $\mathbb{Z}^d$ example) | `:344` |
| | **Decoding: index → codeword** (E_8 ∩ ball = Gaussian typical set) | `:353` |
| | **$\mathbb{Z}^8$ is just scalar quantization** (cube cells, kissing 16) | `:370` |
| | **$E_8$ — one extra coset buys a round cell** ($E_8 = D_8 \cup (D_8 + \tfrac12\mathbf{1})$) | `:380` |
| | Why dimension 8? (Viazovska 2017, sweet spot) | `:392` |
| | **Visualizing $E_8$** — 240 tangent neighbors (`e8.jpg` right, kissing-number card left) | `:410` |
| | Finite codebook from a lattice | `:433` |
| | **Picking the ball — match the typical set** (ball radius $\sigma\sqrt{d}$) | `:445` |
| | **Rounding to $E_8$ in $\mathcal{O}(d)$** (two-coset algorithm spelled out) | `:457` |
| | Is it OK to use a lattice codebook? | `:469` |
| **04 — QUIP: incoherence processing** | Chee, Cai, Kuleshov, De Sa 2023 | `:490-787` |
| | We care about output, not weights | `:497` |
| | Surrogate — one layer at a time ($W_\Delta = \widehat W - W$, not $\Delta$) | `:506` |
| | **The trace trick** (step-by-step derivation, all in $W_\Delta$) | `:516` |
| | The proxy loss (linebreak-split highlight) | `:528` |
| | **What is $H$?** — calibration input covariance, *not* loss Hessian | `:540` |
| | The Hessian tells us what matters | `:548` |
| | **Why independent rounding leaves value on the table** (new: motivates feedback) | `:559` |
| | **The idea — predict and correct (DPCM)** (high-level motivation, no math) | `:567` |
| | **The linear-feedback family** ($\widehat W = Q(W + (W-\widehat W)U)$, $U$ str. upper-triangular) | `:579` |
| | **What $U$ literally does** (new: concrete walk-through) | `:588` |
| | **Why "upper triangular"?** (causal-feedback intuition) | `:596` |
| | **Quantization residual $\eta$** — recall $\ell(\widehat W)$, define $\eta = Q(z) - z$, $\widehat W = z + \eta$ | `:604` |
| | **Proxy in feedback form** ($\widehat W - W = \eta(I+U)^{-1}$ → $\ell = \mathrm{tr}(\eta(I+U)^{-1}H(I+U)^{-\top}\eta^\top)$) | `:613` |
| | **Background — what is an LDL$^\top$ decomposition?** (new prerequisite slide) | `:622` |
| | **LDL of $H$ cancels the cross-terms** ($H=(I+\bar U)D(I+\bar U)^\top$ → $\ell=\mathrm{tr}(\eta D\eta^\top)$; cancellation shown via explicit substitution + underbraced $(I+\bar U)^{-1}(I+\bar U)=I$ pair) | `:631` |
| | **LDLQ — round with memory** (algorithm card; factorization spelled out) | `:642` |
| | **What $\bar U$ and $D$ mean** (Gram-Schmidt under $H$-inner-product) | `:654` |
| | **Worst-case and average proxy loss** (definitions; $\mathbb E\eta_{ij}^2 = \tfrac14, \tfrac1{12}, \tfrac16$) | `:673` |
| | **LDLQ is optimal (Theorem 1)** — worst $(m/4)\mathrm{tr}(D)$, avg $(m/c)\mathrm{tr}(D)$ | `:685-688` |
| | **What Theorem 1 means** — empirical $\mathrm{tr}(D)/\mathrm{tr}(H) \le 0.65$ across every OPT 125m–2.7b layer | `:701` |
| | Why outliers wreck quantization (motivates incoherence) | `:713` |
| | Incoherence — no outliers | `:735` |
| | **Conjugation preserves the proxy** (rotation $U, V$ + definition of $\widetilde H$) | `:744` |
| | Random rotation erases outliers (CLT half; LDLQ on $\widetilde W$ with $\widetilde H$) | `:755` |
| | QUIP — end to end ($V \to \widehat W \to U^\top$ inference diagram) | `:763` |
| **05 — QUIP#: Hadamard + lattice** | Tseng, Chee, Sun, Kuleshov, De Sa 2024 | `:788-839` |
| | QUIP's limitation (Kronecker rotation cost + scalar codebook, new framing) | `:795` |
| | What QUIP# fixes (faster rotation / rounder codebook, new) | `:802` |
| | **The Hadamard/incoherence upgrade, roughly** (replaces old Hadamard-matrix deep dive) | `:817` |
| | QUIP# — net effect (data + hardware impact, new) | `:824` |
| Recap / End | | `:840, :851` |

**Key:** Codebook table (M, not K) `:91`; naive round-trip-through-floats `:169`; integer add identity `:180`; concrete two-grid example `:242`; hex Voronoi tiling fix `:305` (lattice packing gain anchor); Z^8 vs E_8 coset intuition `:370, :380`; **e8.jpg viz** `:410`; **ball radius + O(d) rounding** `:445, :457`; **trace trick in $W_\Delta$** `:516`; **why independent rounding fails + DPCM intuition** `:559, :567`; **linear-feedback family + what $U$ does** `:579, :588`; **quantization residual $\eta$ + proxy in feedback form** `:604, :613`; **LDL background + LDL cancels cross-terms** (the key derivation) `:622, :631`; **LDLQ algorithm card** `:642`; **worst-case + avg definitions** `:673`; **Theorem 1 + interpretation** `:685, :701`; **conjugation preserves proxy** `:744`; **QUIP inference diagram** `:763`; **QUIP# Hadamard/incoherence upgrade (Hadamard step anchor)** `:817`; QUIP# net effect `:824`.

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
- **LDLQ — orthogonality intuition + incoherence payoff** (feedback-form derivation and LDL cancellation now live on-slide; note points there and adds Lemma 2's incoherence→tr(D) bound giving QUIP's quantitative 2-bit guarantee)
- LDLQ ↔ OPTQ/GPTQ equivalence
- **Hadamard basics, FWHT, why random signs are necessary** — now the note's exclusive home for this derivation; the deck's QUIP# section was trimmed from 8 to 4 slides ("QUIP's Limitation" → "What QUIP# Fixes" → "The Hadamard/Incoherence Upgrade, Roughly" → "QUIP# — Net Effect", `:795-824`), so the deck only sketches the idea and points here for Sylvester's construction, FWHT recursion, and the random-sign-flip argument
- Berry-Esseen + union-bound argument for RHT incoherence
- **BlockLDLQ Theorem 4.1** — now the note's exclusive home; the deck's old "Scalar LDLQ vs BlockLDLQ" comparison and "BlockLDLQ — bound" slides were dropped in the QUIP# trim above
- E8P codebook compression (16 → 8-bit lookup, 1 KB)
- Practical caveats (calibration, scales, RVQ, fine-tuning, non-power-of-2)

---

## lossy4-turboquant.html — TURBOQUANT (online VQ for KV cache) (43 slides)

Front motivation opens with self-attention (Q/K/V) before the KV cache, so the inner-product structure is established before we ask what to quantize. Part 06 spells out the actual implementation: K and V both use TURBOQUANT_prod (one composed call, not two parallel quantizers), with a slide on practical pieces (RHT, precomputed codebook, seeded sketch).

**2026-08 changes:** added a 2-slide numerical 128-dim outlier bar-chart example ("Numerical Picture: 128 Coordinates, Before and After" → "After a Random Rotation: Energy Spread Evenly") right after "Random Rotation Creates a Known Law". Removed "Picture: Slicing the Sphere" and "Lemma 1 — Coordinate of a Sphere Point" from the deck — both are now note-only (Lemma 1's proof lives in the note, `lossy4-turboquant-note.html:74`). "Target: 4^{-b}" split into two slides: "Recall: Gaussian Rate–Distortion R(D)" (states R(D) first) then "Invert: Target D(R) = 4^{-b}$" (inverts to the distortion target). Removed the "Proof — Orthogonal Invariance + Panter–Dite" slide from the deck — now note-only, with a pointer left on the Theorem slide. Pipeline-diagram font sizes enlarged; Theorem TURBOQUANT_prod card padding reduced (both cosmetic, no line-count change).

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:71, :84` |
| **KV cache intro** | Attention foundation / cache / vs weights / constraints | `:122-195` |
| | Self-attention: Q/K/V (`qkv.png` large + Levine CS182sp21 cite; no "two-IP" trailing line) | `:122` |
| | What is the KV cache? (growing-cache flow, 50 GB; sentences split across lines) | `:138` |
| | KV cache vs weight quantization (storage vs memory, visual contrast) | `:155` |
| | Compression constraints (online / data-obl / attention-preserving) | `:183` |
| **01 — Setup, rotation idea** | Random rotation → known coordinate distribution | `:196-521` |
| | Why scalar quantization fails | `:203` |
| | Random rotation creates a known law | `:214` |
| | **Numerical picture: 128 coordinates, before and after** (outlier bar chart, new) | `:223` |
| | **After a random rotation: energy spread evenly** (bar chart after $\Pi x$, new) | `:362` |
| | Two metrics, two quantizers (MSE vs IP design) | `:501` |
| **02 — MSE TURBOQUANT** | Target 4^{−b}, pipeline, algorithm, theorem | `:522-615` |
| | **Recall: Gaussian rate–distortion $R(D)$** (states $R(D)$ first) | `:529` |
| | **Invert: target $D(R) = 4^{-b}$** (inverts to the distortion target) | `:539` |
| | Pipeline: rotate, quantize, derotate (4-box diagram; fonts enlarged) | `:549` |
| | Algorithm: TURBOQUANT_mse | `:580` |
| | One-bit anchor 1−2/π | `:595` |
| | **Theorem: TURBOQUANT_mse** (proof pointer only; proof moved to note) | `:603` |
| **03 — Lower bound** | Yao + constant gap | `:616-633` |
| | Yao + constant gap (Sphere SLB *formal* + Picture: Covering both dropped; converse cited from Lec 2) | `:623` |
| **04 — Inner-product bias** | Good MSE ≠ good projections | `:634-683` |
| | One-bit MSE shrinks projections | `:641` |
| | Geometric reason — shrunken norm (vector visual) | `:649` |
| **05 — JL, QJL & inner-product TURBOQUANT** | JL lemma → QJL → two-stage | `:684-817` |
| | **Johnson–Lindenstrauss lemma (formal)** — $k = \mathcal{O}(\varepsilon^{-2}\log n)$ pairwise distances | `:691-693` |
| | **JL intuition** — $\chi^2$ concentration; broken into separate single-claim paragraphs | `:702` |
| | **JL preserves inner products** — polarization identity | `:715` |
| | **From JL to QJL** — 1-bit sign quantization of the sketch | `:724` |
| | QJL definition | `:732` |
| | **Lemma — QJL unbiased, 1/d variance** | `:739-741` |
| | Two-stage decomposition (residual-arrow visual) | `:751` |
| | Algorithm: TURBOQUANT_prod | `:789` |
| | **Theorem: TURBOQUANT_prod** (card padding reduced) | `:803-805` |
| **06 — KV cache implementation** | What/how it actually runs | `:818-899` |
| | **Which quantizer for K and V?** (both → TURBOQUANT_prod) | `:825` |
| | **TURBOQUANT_prod wraps TURBOQUANT_mse** (composition, not parallel) | `:842` |
| | Practical pieces (RHT $\Pi \in \mathbb R^{d\times d}$, precomputed codebook, seeded sketch) | `:857` |
| | **Dimensions used in the paper** — KV: head_dim $d{=}128$ (Llama-3.1-8B); NN: $d \in \{200, 1536, 3072\}$ | `:867` |
| | Empirical behavior (~3.5 bits/channel matches FP16; Llama-3.1-8B head dim $128$) | `:886` |
| Recap / End | | `:900, :912` |

**Key:** Q/K/V attention with large `qkv.png` (Levine CS182sp21) `:122`; **numerical outlier example (before/after rotation)** `:223, :362`; Gaussian $R(D)$ recall + inversion to $4^{-b}$ `:529, :539`; pipeline diagram `:549`; TURBOQUANT_mse theorem `:603` (proof now note-only); Yao + constant gap `:623` (Sphere SLB *and* Picture: Covering dropped — converse cited from Lec 2); **JL lemma + intuition + IP preservation + JL→QJL bridge** `:691, :702, :715, :724`; QJL lemma `:739`; two-stage visual `:751`; TURBOQUANT_prod theorem `:803`; **K/V composition `:842`**; **dimensions table** `:867` (head dim $d{=}128$ per attention head for KV; $d \in \{200, 1536, 3072\}$ for NN search).

**Removed from deck, now note-only:** "Picture: Slicing the Sphere" and "Lemma 1 — Coordinate of a Sphere Point" (proof detail lives in `lossy4-turboquant-note.html:74`); "Proof — Orthogonal Invariance + Panter–Dite" (lives in the note under Panter–Dite / Lloyd–Max sections).

### Note (`lossy4-turboquant-note.html`)
- KV cache — what and why (cache size formula, online/data-oblivious/attention-preserving constraints)
- Why a random rotation Gaussianizes any fixed unit vector (Haar invariance → uniform spherical → Gaussian marginal)
- Where 4^{−b} comes from (Gaussian R(D) derivation); lossy-quantizer bias (1-bit shrinks magnitude to σ√(2/π))
- **Lemma 1 — proof detail (co-area Jacobian mechanics) + concentration corollary** — now the note's exclusive home; "Picture: Slicing the Sphere" and "Lemma 1 — Coordinate of a Sphere Point" were dropped from the deck (replaced there by the 128-dim numerical outlier example at deck `:223, :362`)
- **Lloyd–Max on f_d — alternating updates, Bennett high-resolution limit, sample-free codebook, orthogonal invariance** — now the note's exclusive home for the TURBOQUANT_mse proof; the deck's "Proof — Orthogonal Invariance + Panter–Dite" slide was dropped, with a pointer left on the Theorem slide (deck `:603`)
- **Panter–Dite formula and ∫ f_d^{1/3}** — same proof-migration as above
- QJL lemma — pointer to the deck's proof (`:739`) plus the unique bit-budget/sketch-dimension trade-off (why variance is genuinely 1/d)
- Inner-product TURBOQUANT — two-stage decomposition derivation and bit-budget split

**Audit (2026-05-11):** Slide screenshots verified at 1280×720. Fixed: `K_t\!,V_t` thin-space squashes commas → use plain comma; `QUIP\#` literal backslash → `QUIP#`; Two-Metrics highlight overlapping brand footer → trimmed intro + part-arrows; Theorem+proof one-slide overflow → split into theorem slide and proof slide; Geometric Reason `x̃` label on top of arrow → moved into wedge below arrow; Two-Stage `x̃_mse`/`r` labels cramped → repositioned with widened SVG; Algorithm+Theorem one-slide overflow → split into algorithm slide and theorem slide with aligned math block.
