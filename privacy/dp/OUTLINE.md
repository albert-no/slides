# privacy/dp/ — Differential privacy series

Eight-deck lecture series on differential privacy. `dp1`–`dp7` build the foundations (reconstruction attacks → pure DP → properties → approximate DP → DP-SGD → RDP → DP in ML / PATE). `dp8-fl` is the capstone applied talk (NeurIPS 2023: exact-optimal LDP mean estimation under shared randomness, with extensions to DP in modern ML).

## Files

| File | Purpose |
|---|---|
| `dp1-reconstruction.html` | Lecture 1 — Reconstruction attacks (Dinur–Nissim, LP relaxation) |
| `dp2-pure-dp.html` | Lecture 2 — Randomized response, $\varepsilon$-DP, Laplace, exponential mechanism, Noisy Max |
| `dp3-properties.html` | Lecture 3 — Composition, post-processing, group privacy, subsampling, DP $k$-means, why additive DP fails |
| `dp4-approximate-dp.html` | Lecture 4 — $(\varepsilon,\delta)$-DP, privacy-loss RV, truncated Laplace, Gaussian mechanism, properties of approximate DP |
| `dp5-erm.html` | Lecture 5 — DP-ERM (exponential mechanism), advanced composition, GD/SGD/Noisy GD/DP-SGD |
| `dp6-rdp.html` | Lecture 6 — KL-DP, Rényi divergence, RDP definition + properties, Gaussian via RDP |
| `dp7-ml-paradigms.html` | Lecture 7 — Output/objective/gradient perturbation; Input vs Inference vs Model DP; PATE |
| `dp8-fl.html` | Lecture 8 / capstone — DP in federated learning (NeurIPS 2023 RRSC) |
| `dp-fl.pdf` | PDF export of DP-FL |
| `dp-fl.txt` | Compressed text outline / handout for DP-FL |
| `figs/` | Slide figures (`sphereical_cap.jpg`, `rrsc.png`) |
| `tex/dp.tex` | Source LaTeX lecture notes for `dp1`–`dp7` |

---

## dp1-reconstruction.html

**Topic:** Reconstruction attacks motivate differential privacy. Difference attack on suppressed counts; Dinur–Nissim theorems for all-queries and polynomially-many random queries; LP relaxation for an efficient attacker.

### Sections (23 slides)

| Section | Slide | Line |
|---|---|---|
| Title / Contents | 1–2 | `:27-50` |
| **01 — Motivating attacks** | 3–6 | `:51-95` |
| | Single sensitive query | 4 | `:59` |
| | Difference attack | 5 | `:73` |
| | **Definition: Reconstruction attack** | 6 | `:86` |
| **02 — Formal setup** | 7–10 | `:97-141` |
| | Binary dataset, counting queries | 8 | `:105` |
| | Reconstruction optimization | 9 | `:117` |
| | **Claim: trivial consistency bound** | 10 | `:130` |
| **03 — Dinur–Nissim theorems** | 11–18 | `:142-241` |
| | **Theorem 1: all queries, error $4\alpha n$** | 12, proof 13 | `:150`, `:162` |
| | Corollary: 1%-error → 96%-recovery | 14 | `:178` |
| | Realistic regime: $m = 20n$ random | 15 | `:192` |
| | **Theorem 2: polynomial random queries → $256\alpha^2 n^2$** | 16, proof 17–18 | `:204`, `:216` |
| **04 — Efficient attack** | 19–22 | `:242-288` |
| | LP relaxation | 20 | `:250` |
| | LP refresher | 21 | `:263` |
| | Implications | 22 | `:275` |

### Key theorems

| Item | Line |
|---|---|
| Dinur–Nissim Theorem 1 (all-queries) | `:156-160` |
| Dinur–Nissim Theorem 2 (random queries) | `:209-214` |
| LP-relaxation attack | `:253-258` |

---

## dp2-pure-dp.html

**Topic:** Randomized response → $\varepsilon$-DP definition → Laplace mechanism → DP selection (Exponential mechanism, Noisy Max). All major proofs included.

### Sections (32 slides)

| Section | Slides | Line |
|---|---|---|
| Title / Contents | 1–2 | `:29-52` |
| **01 — Randomized response** | 3–8 | `:53-131` |
| | RR mechanism, debiased estimator, variance | 4–6 | `:61-95` |
| | **Chebyshev / sample complexity** | 7 | `:97` |
| | Trade-off summary | 8 | `:111` |
| **02 — $\varepsilon$-DP definition** | 9–16 | `:132-229` |
| | Neighboring datasets | 10 | `:140` |
| | **Definition: $\varepsilon$-DP** | 11 | `:152` |
| | Why randomization is necessary | 12 | `:165` |
| | Hypothesis-testing interpretation | 14 | `:191` |
| | Covid example (FP/FN) | 15 | `:205` |
| | **RR is $4\gamma$-DP** | 16 | `:220` |
| **03 — Laplace mechanism** | 17–21 | `:230-290` |
| | **$\ell_1$ sensitivity** | 18 | `:238` |
| | **Laplace mechanism + proof** | 19–20 | `:254, :266` |
| | Noise variance | 21 | `:279` |
| **04 — Selection: EM &amp; Noisy Max** | 22–30 | `:291-418` |
| | Motivating selection (voting, pricing) | 23 | `:299` |
| | **Definition: Exponential mechanism** | 24 | `:316` |
| | **EM utility (high-prob, expectation)** + proofs | 25–26 | `:328, :344` |
| | Example: most-frequent item | 27 | `:360` |
| | **Definition: Noisy Max** | 28 | `:373` |
| | **Noisy Max is $\varepsilon$-DP + proof** | 29 | `:389` |
| | Noisy Max utility + proof | 30 | `:403` |

### Key theorems

| Item | Line |
|---|---|
| $\varepsilon$-DP definition | `:155-157` |
| Laplace mechanism | `:258-260` |
| Laplace mechanism proof | `:268-275` |
| Exponential mechanism definition | `:319-321` |
| EM high-prob utility | `:332-334` |
| Noisy Max DP proof | `:393-401` |

---

## dp3-properties.html

**Topic:** Composition, post-processing, group privacy, subsampling amplification (with proof), critique of additive DP, DP $k$-means as a worked example.

### Sections (27 slides)

| Section | Slides | Line |
|---|---|---|
| Title / Contents | 1–2 | `:33-57` |
| **01 — Composition** | 3–6 | `:58-102` |
| | **Basic composition + proof** | 4–5 | `:66, :77` |
| | $k$-fold composition | 6 | `:88` |
| **02 — Post-processing immunity** | 7–9 | `:103-137` |
| | **Theorem + proof** | 8 | `:111` |
| | Why it matters | 9 | `:126` |
| **03 — Group privacy &amp; subsampling** | 10–16 | `:138-219` |
| | **Group privacy: $t\varepsilon$** | 11 | `:146` |
| | **Subsampling: $\varepsilon' = \ln(1+q(e^\varepsilon-1))$** | 12 | `:161` |
| | Subsampling proof (setup → 3 inequalities → conclusion) | 13–15 | `:174, :185, :196` |
| **04 — Why not additive DP?** | 17–20 | `:220-270` |
| | Counterexample 1 (leak all w.p. $\delta$) | 19 | `:241` |
| | Counterexample 2 (per-element leakage) | 20 | `:257` |
| **05 — DP $k$-means** | 21–25 | `:271-343` |
| | Standard $k$-means algorithm | 22 | `:279` |
| | **DP $k$-means algorithm** | 23 | `:295` |
| | **Theorem: DP $k$-means is $\varepsilon$-DP + proof** | 24 | `:312` |
| | Remarks (Gaussian variant) | 25 | `:331` |
| Recap + closer | 26–27 | `:344-364` |

### Key theorems

| Item | Line |
|---|---|
| Basic composition | `:69-71` |
| Post-processing theorem | `:114-116` |
| Group privacy | `:149-151` |
| Subsampling amplification formula | `:168-170` |
| DP $k$-means privacy theorem | `:315-317` |

---

## dp4-approximate-dp.html

**Topic:** $(\varepsilon, \delta)$-DP definition, privacy-loss RV technique, truncated Laplace, Gaussian mechanism with full 1-D and multi-D proofs, properties of approximate DP.

### Sections (24 slides)

| Section | Slides | Line |
|---|---|---|
| Title / Contents | 1–2 | `:29-52` |
| **01 — $(\varepsilon,\delta)$-DP** | 3–7 | `:53-112` |
| | **Definition: $(\varepsilon,\delta)$-DP** | 4 | `:61` |
| | Interpretations | 5 | `:77` |
| | **Privacy-loss random variable** | 6 | `:89` |
| | Good/bad split proof technique | 7 | `:102` |
| **02 — Truncated Laplace** | 8–9 | `:113-133` |
| **03 — Gaussian mechanism** | 10–16 | `:134-221` |
| | **Definition + theorem (Gaussian mechanism)** | 11 | `:142` |
| | **Proof: 1-D privacy loss + tail bound** | 12–13 | `:158, :171` |
| | Multi-dim lemma + proof | 14–15 | `:182, :193` |
| | $\ell_2$ vs $\ell_1$ sensitivity | 16 | `:204` |
| **04 — Properties of approx. DP** | 17–22 | `:222-295` |
| | Post-processing + proof | 18 | `:230` |
| | Basic composition | 19 | `:245` |
| | Group privacy | 20 | `:259` |
| | Subsampling amplification | 21 | `:271` |
| | Many-iteration accounting (MA, RDP) | 22 | `:283` |
| Recap + closer | 23–24 | `:296-314` |

### Key theorems

| Item | Line |
|---|---|
| $(\varepsilon,\delta)$-DP definition | `:64-66` |
| Privacy-loss RV definition | `:92-94` |
| Gaussian mechanism theorem | `:148-150` |
| Multi-dim lemma | `:185-187` |

---

## dp5-erm.html

**Topic:** Empirical risk minimization, exponential mechanism for ERM with utility proof, advanced composition, DP-SGD algorithm with privacy and utility theorems.

### Sections (23 slides)

| Section | Slides | Line |
|---|---|---|
| Title / Contents | 1–2 | `:24-69` |
| **01 — ERM setup** | 3–5 | `:72-102` |
| | ERM + population vs empirical | 4 | `:80` |
| | Assumptions (constraint, bounded loss, Lipschitz) | 5 | `:93` |
| **02 — Exponential mechanism for ERM** | 6–10 | `:104-160` |
| | EM for ERM | 7 | `:113` |
| | **Utility theorem** | 8 | `:128` |
| | Proof: volume ratio | 9 | `:140` |
| | Proof: tail → expectation | 10 | `:152` |
| **03 — Advanced composition** | 11–13 | `:162-201` |
| | **Advanced composition theorem** | 12 | `:171` |
| | Intuition (chain rule, $\sqrt k$) | 13 | `:185` |
| **04 — DP-SGD** | 14–21 | `:203-322` |
| | GD algorithm + convergence | 15 | `:213` |
| | SGD &amp; Noisy GD | 16 | `:233` |
| | **DP-SGD algorithm** | 17 | `:254` |
| | **DP-SGD privacy theorem** | 18 | `:273` |
| | Subsampling amplification in DP-SGD | 19 | `:290` |
| | **DP-SGD utility (convex)** | 20 | `:302` |
| | Nonconvex remark | 21 | `:319` |
| Recap + closer | 22–23 | `:330-345` |

### Key theorems

| Item | Line |
|---|---|
| EM-for-ERM utility theorem | `:131-133` |
| Advanced composition | `:174-176` |
| DP-SGD privacy theorem | `:276-278` |
| DP-SGD convex utility theorem | `:312-315` |

---

## dp6-rdp.html

**Topic:** KL-DP, Rényi divergence + limits, $(\alpha, \varepsilon)$-RDP, additive composition, conversion to $(\varepsilon, \delta)$, Gaussian mechanism via RDP with proof.

### Sections (21 slides)

| Section | Slides | Line |
|---|---|---|
| Title / Contents | 1–2 | `:24-66` |
| **01 — KL-DP** | 3–4 | `:69-92` |
| | **Definition: KL-DP** | 4 | `:78` |
| **02 — Rényi divergence** | 5–7 | `:95-126` |
| | **Definition** | 6 | `:104` |
| | Limits ($\alpha \to 1$, $\alpha \to \infty$) | 7 | `:117` |
| **03 — RDP &amp; properties** | 8–13 | `:129-203` |
| | **Definition: $(\alpha,\varepsilon)$-RDP** | 9 | `:138` |
| | **Composition (additive in $\varepsilon$)** | 10 | `:152` |
| | **Conversion to $(\varepsilon,\delta)$-DP** | 11 | `:166` |
| | Lemma: $D_\infty \le \varepsilon \Rightarrow D_\alpha \le 2\alpha\varepsilon^2$ | 12 | `:179` |
| | Advanced composition via RDP | 13 | `:191` |
| **04 — Gaussian via RDP** | 14–19 | `:205-285` |
| | **Theorem (Gaussian RDP)** | 15 | `:215` |
| | Conversion to $(\varepsilon,\delta)$ | 16 | `:229` |
| | Proof steps 1–3 | 17–19 | `:243, :257, :269` |
| Recap + closer | 20–21 | `:288-310` |

### Key theorems

| Item | Line |
|---|---|
| Rényi divergence definition | `:107-109` |
| $(\alpha,\varepsilon)$-RDP definition | `:141-143` |
| Composition (additive) | `:155-157` |
| Conversion to $(\varepsilon,\delta)$ | `:169-171` |
| Gaussian RDP theorem | `:218-220` |

---

## dp7-ml-paradigms.html

**Topic:** Three DP-ERM perturbation strategies (output / objective / gradient); Input-DP vs Inference-DP vs Model-DP; PATE three-phase architecture with privacy accounting and trade-offs.

### Sections (20 slides)

| Section | Slides | Line |
|---|---|---|
| Title / Contents | 1–2 | `:23-66` |
| **01 — Where to inject noise?** | 3–4 | `:69-95` |
| | Three perturbation strategies | 4 | `:78` |
| **02 — Privacy boundary** | 5–8 | `:97-141` |
| | Input perturbation / Local DP | 6 | `:106` |
| | Inference DP + critical flaw | 7 | `:118` |
| | **Model DP (Global DP) — the goal** | 8 | `:131` |
| **03 — PATE** | 9–14 | `:143-220` |
| | PATE intuition (consensus) | 10 | `:151` |
| | Phase 1 — teacher ensemble | 11 | `:164` |
| | Phase 2 — noisy aggregation | 12 | `:178` |
| | Phase 3 — student model | 13 | `:192` |
| | Pipeline diagram | 14 | `:207` |
| **04 — Accounting &amp; trade-offs** | 15–18 | `:223-273` |
| | Privacy accounting (composition vs RDP) | 16 | `:231` |
| | Advantages | 17 | `:246` |
| | Limitations | 18 | `:258` |
| Recap + closer | 19–20 | `:275-292` |

---

## dp8-fl.html

**Topic:** From DP foundations through PrivUnit to RRSC exact-optimality (NeurIPS 2023), then DP in modern ML (DP-SGD, DP-Diffusion, DP-RDM).

### Sections

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:1-250` |
| **01 — FL & mean estimation** | | `:255-360` |
| | Federated learning (4-step diagram) | `:265` |
| | Three challenges in FL (compress, privacy, utility) | `:325` |
| | **Core primitive: $\hat\mu = \frac{1}{n}\sum x_i$ with bits + LDP + low MSE** | `:348` |
| **02 — LDP vs Central DP** | | `:364-574` |
| | **Definition: $(\varepsilon,\delta)$-DP (Dwork et al. 2006)** | `:374, :377` |
| | Local vs central DP comparison | `:393` |
| | Central trust bar | `:399` |
| | LDP trust bar (untrusted server) | `:427` |
| | **Definition: LDP (density-ratio form)** | `:460, :465` |
| | **LDP mean estimation: minimax rate $\Theta(d/(n\min(\varepsilon, \varepsilon^2)))$ (DJW 2013)** | `:483, :488` |
| | Gaussian mechanism is suboptimal | `:501` |
| | **PrivUnit (Bhowmick et al. 2018): spherical-cap, optimal constant** (cols layout) | `:523, :529` |
| | Missing axis: communication / finite bits | `:548` |
| **03 — Exact optimality (NeurIPS 2023)** | | `:576-827` |
| | Problem setup (jointly optimize rate, utility, privacy) | `:586` |
| | LDP with shared randomness (seed U public) | `:617` |
| | **Result I — canonical protocols** (single encoder/decoder, unbiased) | `:658, :661` |
| | **Result II — codebook schemes are optimal** | `:678, :681` |
| | **Result III — RRSC: rotationally symmetric simplex codebook** | `:694, :699` |
| | **Result IV — k-closest encoding is optimal** (two-level density) | `:743, :748` |
| | RRSC → PrivUnit as M→∞ | `:760` |
| | Unified framework (SQKR, FT21, MMRC vs RRSC) | `:778` |
| | Experiments | `:804` |
| | Open question: optimal among all protocols? | `:816` |
| **04 — DP in modern ML** | | `:832-1009` |
| | DP-SGD pipeline (clip + noise + accounting) | `:842` |
| | **DP-Diffusion (Ghalebikesabi et al. 2023)** — public pretrain, private FT | `:857` |
| | **DP-RDM (Lebensold et al. 2024)** — privatize retrieval | `:883` |
| | DP-RDM pipeline diagram + SGM (inline) | `:910` |
| | DP-RDM intuition (privacy boundary, λ knob) | `:964` |
| | DP at realistic scale | `:985` |
| | Q&A | `:1012` |

### Key theorems / formulas

| Item | Line |
|---|---|
| (ε,δ)-DP definition | `:377-379` |
| LDP definition (density ratio ≤ e^ε) | `:465-466` |
| LDP minimax rate `Θ(d/(n min(ε,ε²)))` | `:488-490` |
| PrivUnit spherical-cap mechanism | `:529-531` |
| Result I: canonical protocols | `:661-668` |
| Result II: codebook optimality | `:681-683` |
| Result III: RRSC (Haar-rotated simplex) | `:699-702` |
| Result IV: k-closest two-level density | `:748-749` |
| Sampled Gaussian Mechanism (inline highlight) | `:953-955` |

## dp-fl.txt

35-slide compressed outline (FL → challenges → mean est. → LDP vs DP → PrivUnit → RRSC → experiments → DP-Diffusion). Companion to the deck, not a duplicate. Quick reference handout.

## No companion `-note.html`

Unlike `mia/`, there is no separate notes file. Proof detail is in-deck. For the foundational decks (`dp1`–`dp7`), the source LaTeX lecture notes are in `tex/dp.tex`. For deeper context on cited DP-FL papers, look up DJW 2013, Bhowmick 2018, Ghalebikesabi 2023, Lebensold 2024.
