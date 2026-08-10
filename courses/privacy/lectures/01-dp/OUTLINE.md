# privacy/lectures/01-dp/ — Differential privacy series

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

**Topic:** Why accurate aggregate answers destroy privacy — difference attacks, the Dinur–Nissim reconstruction theorems (all-queries and random-queries, with complete proofs), the LP relaxation making the attack polynomial-time, and the √n noise barrier that motivates differential privacy.

### Sections (46 slides)

| Section | Slide | Line |
|---|---|---|
| Title | 1 | `:40` |
| Contents | 2 | `:52` |
| **01 — Motivating attacks** (single query, roster, difference attack, reconstruction def.) | 3–8 | `:66` |
| **02 — Formal setup** (binary dataset, counting queries, curator model, attacker's program, trivial bound) | 9–14 | `:152` |
| **03 — Theorem 1: all queries** (intuition, statement, 4-step proof, recap chain, 1%/96% corollary) | 15–23 | `:229` |
| **04 — Theorem 2: random queries** (m=20n, anti-concentration intuition, statement, 4-step proof, recap chain, √n barrier) | 24–34 | `:345` |
| **05 — Efficient attack** (exponential search, relax-then-round geometry, relaxed program, LP recall, slack-variable LP, rounding guarantee) | 35–41 | `:489` |
| **06 — Implications** (trade-off table, aggregates unsafe, lecture recap) | 42–45 | `:600` |
| Q&A | 46 | `:649` |

### Key theorems

| Item | Slide(s) | Line |
|---|---|---|
| Def. reconstruction attack (blatant non-privacy) | 8 | `:137-151` |
| Claim: trivial consistency bound (minimizer within αn of every answer) | 14 | `:216-228` |
| Theorem 1 (Dinur–Nissim 2003): every query within αn ⇒ ≤ 4αn wrong bits | 17 | `:255-267` |
| Proof of Theorem 1 (pigeonhole → disagreement set is a query → triangle inequality; recap chain) | 18–22 | `:268-330` |
| Corollary: ±n/100 answers ⇒ ≥ 96% of bits recovered | 23 | `:331-344` |
| Theorem 2 (Dinur–Nissim 2003): m = 20n random queries ⇒ ≤ 256α²n² wrong bits w.p. ≥ 1−2⁻ⁿ | 27 | `:397-409` |
| Proof of Theorem 2 (kill criterion via reverse triangle → anti-concentration ≤ 9/10 → independence (9/10)^20n ≤ 2^−2n → union bound; recap chain) | 28–33 | `:410-475` |
| √n barrier: per-query noise E ⇒ ≤ 256E² wrong bits; noise o(√n) fatal | 34 | `:476-488` |
| Def. linear program | 39 | `:559-573` |
| LP relaxation: min–max → single slack variable t, box constraints, rounding keeps o(n) wrong bits | 38, 40–41 | `:547-558`, `:574-599` |

Diagrams: roster table (slide 5), query cards (6), bit-vector cell strips (10, 11, 16, 18), curator model actors (12), anti-concentration bell-curve SVG with survival-window band (26), relax-then-round polytope SVG (37), comparison/trade-off tables (25, 34, 43). Authoritative math source: `tex/dp.tex:55–249`.

---

## dp2-pure-dp.html

**Topic:** Randomized response (Warner 1965) with full estimation theory → $\varepsilon$-DP definition with hypothesis-testing reading → Laplace mechanism → DP selection (Exponential mechanism, Noisy Max). Every theorem carries a complete multi-slide proof with the key trick named on-slide.

### Sections (62 slides)

| Section | Slides | Line |
|---|---|---|
| Title / Contents | 1–2 | `:43-67` |
| **01 — Randomized response** | 3–13 | `:68-238` |
| | Motivation (respondent flow, deniability) | 4 | `:76` |
| | **RR mechanism (coin-tree)** | 5 | `:97` |
| | Privacy dial $\gamma$ (spectrum) | 6 | `:121` |
| | Mean → debiasing → estimator → variance | 7–10 | `:145, :160, :172, :182` |
| | **Chebyshev lemma → sample complexity $n = \tfrac{1}{16\gamma^2\beta\alpha^2}$** | 11–12 | `:192, :205` |
| | Trade-offs (50,000-respondent anchor) | 13 | `:218` |
| **02 — $\varepsilon$-DP definition** | 14–27 | `:239-453` |
| | Neighboring datasets (cell strip) | 15 | `:247` |
| | **Definition: $\varepsilon$-DP** + two-sided reading | 16–17 | `:265, :278` |
| | Why randomization is necessary | 18 | `:292` |
| | Numerical anchors ($e^\varepsilon$ table) | 19 | `:305` |
| | Hypothesis-testing view, forbidden-corner picture | 20–21 | `:320, :334` |
| | Covid FP/FN aside | 22 | `:371` |
| | **RR is $\varepsilon_\gamma$-DP, $\varepsilon_\gamma = \ln\frac{1/2+\gamma}{1/2-\gamma}$** + 3-slide proof + discussion | 23–27 | `:388, :405, :414, :427, :437` |
| **03 — Laplace mechanism** | 28–38 | `:454-615` |
| | **$\ell_1$ sensitivity** + worked examples (count, mean) | 29–30 | `:462, :478` |
| | Laplace distribution (pdf curve, tail) | 31 | `:498` |
| | **Laplace mechanism (DMNS 2006)** + densities picture | 32–33 | `:518, :532` |
| | Proof: product density → triangle inequality → calibrate + integrate | 34–36 | `:559, :571, :582` |
| | Accuracy ($\ln 100 \approx 4.6$ anchor); central vs local | 37–38 | `:592, :602` |
| **04 — Exponential mechanism** | 39–49 | `:616-766` |
| | Selection problems (voting, pricing); why output noise fails (revenue cliff) | 40–41 | `:624, :644` |
| | **Definition: EM (McSherry–Talwar 2007)** | 42 | `:667` |
| | **EM is $\varepsilon$-DP** + proof (score factor, normalizer factor) | 43–45 | `:680, :693, :702` |
| | **EM utility (high-prob + expectation)** + proofs | 46–48 | `:711, :728, :741` |
| | Numbers: voting with 100 candidates (36.8 votes) | 49 | `:754` |
| **05 — Noisy Max** | 50–60 | `:767-912` |
| | **Noisy Max algorithm ($\mathrm{Exp}(2\Delta/\varepsilon)$ noise)** | 51 | `:774` |
| | **NM is $\varepsilon$-DP** + strategy + intuition (freeze other noises) | 52–53 | `:789, :806` |
| | Proof: condition → threshold shift $\le 2\Delta$ → tail pays $e^\varepsilon$ → integrate out | 54–57 | `:828, :839, :850, :863` |
| | **NM utility** + union-bound proof | 58–59 | `:873, :886` |
| | EM vs NM comparison table | 60 | `:898` |
| Recap + Q&A | 61–62 | `:913-935` |

### Key theorems

| Item | Slide(s) | Line |
|---|---|---|
| Def. randomized response ($\Pr[Y_i = D_i] = \tfrac12 + \gamma$) | 5 | `:100-108` |
| Lemma (Chebyshev) | 11 | `:196-199` |
| Claim: RR sample complexity $n = \frac{1}{16\gamma^2\beta\alpha^2}$ for $(\alpha,\beta)$ | 12 | `:209-212` |
| Def. neighboring datasets (replace; add/delete variant) | 15 | `:258-262` |
| Def. $\varepsilon$-DP | 16 | `:269-273` |
| Theorem: RR is $\varepsilon_\gamma$-DP, $\varepsilon_\gamma = \ln\frac{1/2+\gamma}{1/2-\gamma} = 4\gamma + O(\gamma^3)$ | 23 | `:392-398` |
| Proof of RR privacy (cancellation → two-bit case table → points-to-events) | 24–26 | `:405-435` |
| Def. $\ell_1$ sensitivity | 29 | `:467-472` |
| Theorem: Laplace mechanism is $\varepsilon$-DP (DMNS 2006) | 32 | `:522-528` |
| Proof of Laplace (product density → triangle inequality → calibrate + integrate; recap chain) | 34–36 | `:559-590` |
| Laplace accuracy: $\Pr[|\text{err}| > \frac{\Delta_1}{\varepsilon}\ln\frac{1}{\beta}] = \beta$ | 37 | `:592-600` |
| Def. exponential mechanism (Gibbs weights, $2\Delta$ exponent) | 42 | `:671-677` |
| Theorem: EM is $\varepsilon$-DP + proof (score factor $e^{\varepsilon/2}$ × normalizer factor $e^{\varepsilon/2}$) | 43–45 | `:684-710` |
| Theorem: EM utility, $\Pr[q(Y) < q_{\max} - \frac{2\Delta(\log d + t)}{\varepsilon}] \le e^{-t}$ + proof (bad set, benchmark vs $y^\star$) | 46–47 | `:715-740` |
| Theorem: EM expected gap $\le \frac{2\Delta}{\varepsilon}(\log d + 1)$ (integrate-the-tail) | 48 | `:745-748` |
| Noisy Max algorithm box | 51 | `:778-782` |
| Theorem: NM is $\varepsilon$-DP + proof (condition on $Z_{-y}$, threshold $K(D)$ moves $\le 2\Delta$, exponential tail pays $e^\varepsilon$, integrate out) | 52–57 | `:793-871` |
| Theorem: NM utility (same bound as EM) + union-bound proof | 58–59 | `:877-896` |

Diagrams: respondent flow chain (slide 4), coin-tree SVG (5), $\gamma$-spectrum dial SVG (6), neighbor cell strips (15), forbidden-corner ROC SVG (21), Laplace pdf SVG (31), overlapping shifted densities SVG (33), revenue-cliff SVG (41), exponential-tail shift SVG with shaded bands (53). One TODO: real deployed-$\varepsilon$ figure (slide 19, `:316`). Authoritative math source: `tex/dp.tex`.

---

## dp3-properties.html

**Topic:** The algebra of $\varepsilon$ — adaptive composition, post-processing immunity, group privacy, and subsampling amplification, each with a complete multi-slide proof and the key trick named on-slide; why additive $\delta$-DP fails (two worked counterexamples); DP $k$-means as the capstone worked example combining Laplace, composition, and post-processing.

### Sections (55 slides)

| Section | Slides | Line |
|---|---|---|
| Title / Contents | 1–2 | `:52-76` |
| **01 — Basic composition** | 3–10 | `:77-214` |
| | Recall card ($\varepsilon$-DP, Laplace) + roadmap | 4 | `:86` |
| | Budget-bar intuition (SVG) | 5 | `:103` |
| | Adaptive-queries setting (SVG, $a_1$ feeds $\mathcal M_2$) | 6 | `:128` |
| | **Theorem: adaptive composition ($\varepsilon_1+\varepsilon_2$)** | 7 | `:160` |
| | Proof: factorize joint → bound each factor | 8–9 | `:173, :186` |
| | $k$-fold corollary + budget table | 10 | `:199` |
| **02 — Post-processing immunity** | 11–16 | `:215-311` |
| | Pipeline intuition (flow diagram) | 12 | `:224` |
| | **Theorem: $f \circ \mathcal M$ is $\varepsilon$-DP** | 13 | `:244` |
| | Proof: deterministic $f$ pulls back the event (preimage SVG) | 14 | `:257` |
| | Proof: randomized $f$ is a mixture | 15 | `:283` |
| | No privacy laundering | 16 | `:295` |
| **03 — Group privacy** | 17–20 | `:312-365` |
| | **Theorem: $t$ records cost $t\varepsilon$** | 18 | `:321` |
| | Proof: telescoping chain (hop diagram) | 19 | `:334` |
| | Scaling table (household anchor) | 20 | `:352` |
| **04 — Subsampling amplification** | 21–34 | `:366-571` |
| | Crowd intuition (hiding in the sample, SVG) | 22 | `:375` |
| | Two-worlds heuristic | 23 | `:400` |
| | **Definition: subsampled mechanism** (flow diagram) | 24 | `:412` |
| | **Theorem: $\varepsilon' = \ln(1+q(e^{\varepsilon}-1))$** | 25 | `:431` |
| | Proof plan (split / compare / blend / rearrange) | 26 | `:444` |
| | Proof: condition on membership ($A$, $B$) | 27 | `:459` |
| | Proof: three comparisons (i)–(iii) | 28 | `:469` |
| | Proof: coupling for (ii) (cell-pairing diagram) | 29 | `:482` |
| | **Proof: convex-combination trick, $\alpha^\star = q+(1-q)e^{-\varepsilon}$** | 30 | `:502` |
| | Proof: rearrange and conclude | 31 | `:513` |
| | Proof recap chain | 32 | `:526` |
| | Numbers table ($q=0.01 \Rightarrow \approx 60\times$) | 33 | `:539` |
| | Minibatch relevance (DP training pipeline) | 34 | `:553` |
| **05 — Why not additive DP?** | 35–43 | `:572-705` |
| | **Definition: additive $\delta$-DP** | 36 | `:581` |
| | CE1: publish everything w.p. $\delta$ (branch SVG → verification → verdict) | 37–39 | `:597, :620, :632` |
| | CE2: leak each record w.p. $\delta$ (cell strip → coupling → aggregate table) | 40–42 | `:645, :666, :676` |
| | Moral: protect the tails | 43 | `:690` |
| **06 — DP $k$-means** | 44–53 | `:706-854` |
| | $k$-means objective recap (scatter SVG) | 45 | `:715` |
| | Lloyd's algorithm | 46 | `:737` |
| | What must be noised (counts + sums flow) | 47 | `:752` |
| | **DP $k$-means algorithm (NRS 2007)** | 48 | `:772` |
| | **Theorem: DP $k$-means is $\varepsilon$-DP** | 49 | `:788` |
| | Proof: counts sensitivity $\le 2$ | 50 | `:804` |
| | Proof: sums sensitivity $\le 2$ (domain bound) | 51 | `:818` |
| | Proof: compose $2T$ releases, division free | 52 | `:828` |
| | Remarks + noise-scale table | 53 | `:838` |
| Recap (property/guarantee/trick table) + closer | 54–55 | `:857-874` |

### Key theorems

| Item | Slide(s) | Line |
|---|---|---|
| Theorem (adaptive composition): $(\mathcal M_1, \mathcal M_2(\cdot,\mathcal M_1))$ is $(\varepsilon_1+\varepsilon_2)$-DP | 7 | `:163-167` |
| Proof of composition (density-factorization trick → bound each factor → sum over $T$) | 8–9 | `:173-197` |
| Corollary: $k$-fold composition costs $\sum_i \varepsilon_i$ | 10 | `:202-205` |
| Theorem (post-processing immunity): $f \circ \mathcal M$ is $\varepsilon$-DP, $f$ arbitrary | 13 | `:247-251` |
| Proof of post-processing (preimage pull-back; randomized $f$ = mixture over seeds) | 14–15 | `:257-293` |
| Theorem (group privacy): $\le t$ records $\Rightarrow$ factor $e^{t\varepsilon}$ | 18 | `:325-329` |
| Proof of group privacy (telescoping trick: $t$ single-record hops) | 19 | `:334-349` |
| Definition: subsampled mechanism ($q = m/n$, no replacement) | 24 | `:415-418` |
| Theorem (amplification): $\varepsilon' = \ln(1+q(e^{\varepsilon}-1)) \approx q\varepsilon$ | 25 | `:434-438` |
| Proof of amplification (condition on $1 \in I$ → three comparisons → coupling → convex-combination trick with $\alpha^\star = q+(1-q)e^{-\varepsilon}$ → rearrange; recap chain) | 26–32 | `:444-537` |
| Definition: additive $\delta$-DP | 36 | `:584-588` |
| CE1: publish-all-w.p.-$\delta$ satisfies $\delta$-additive DP, not $\varepsilon$-DP for any $\varepsilon$ | 37–39 | `:597-643` |
| CE2: per-record leakage satisfies $\delta$-additive DP; someone leaks w.h.p. at useful $\delta \gtrsim 1/n$ | 40–42 | `:645-688` |
| DP $k$-means algorithm ($\varepsilon' = \varepsilon/(2T)$; $n_j, a_j$ + Lap$(2/\varepsilon')$) | 48 | `:775-783` |
| Theorem: DP $k$-means is $\varepsilon$-DP | 49 | `:791-794` |
| Proof of $k$-means privacy (counts sensitivity 2 → sums sensitivity 2 via $\lVert x \rVert_1 \le 1$ → compose $2T$; division post-processing) | 50–52 | `:804-836` |

Diagrams: budget-bar SVG (slide 5), adaptive-queries SVG (6), post-processing pipeline flow (12), preimage-mapping SVG (14), telescoping-chain hop diagram (19), crowd/sample SVG (22), subsampling flow (24), coupling cell-pairing strips (29), CE1 branch SVG (37), CE2 leak cell strip (40), $k$-means scatter SVG with assignment boundary (45), counts-and-sums noise flow (47), five numeric anchor tables (10, 20, 33, 42, 53), recap formula table (54). One TODO: real DP-$k$-means vs Lloyd cluster figure (slide 53, `:853`). Citations: DMNS TCC 2006 (composition), Dwork–Roth 2014 (post-processing, group privacy), NRS STOC 2007 ($k$-means). Authoritative math source: `tex/dp.tex:491–766`.

---

## dp4-approximate-dp.html

**Topic:** $(\varepsilon, \delta)$-DP definition and interpretation, privacy-loss RV technique with full tail-lemma proof, truncated Laplace, Gaussian mechanism with full 1-D and multi-D proofs, properties of approximate DP.

### Sections (53 slides)

| Section | Slides | Line |
|---|---|---|
| Title / Contents | 1–2 | `:47-71` |
| **01 — $(\varepsilon,\delta)$-DP** | 3–11 | `:72-230` |
| | Recall pure DP + Laplace | 4 | `:80` |
| | Gaussian noise breaks pure DP (tail SVG) | 5 | `:96` |
| | **Definition: $(\varepsilon,\delta)$-DP** | 6 | `:118` |
| | Ratio vs additive slack (numeric table) | 7 | `:134` |
| | $\delta$-sliver picture (SVG) | 8 | `:160` |
| | Interpretations (failure prob., ratio-outside-sliver) | 9 | `:187` |
| | What $\delta$ does *not* promise (publish-all counterexample) | 10 | `:202` |
| | Calibrating $\delta \ll 1/n$ ($n = 10^6$ anchor table) | 11 | `:215` |
| **02 — The privacy-loss random variable** | 12–20 | `:231-353` |
| | **Definition: privacy loss $I_{X,X'}(y)$, PLRV** | 13 | `:239` |
| | Pure DP restated: $\sup_y \lvert I \rvert \le \varepsilon$ | 14 | `:255` |
| | PLRV distribution picture (SVG) | 15 | `:273` |
| | **Lemma: tail bound suffices for $(\varepsilon,\delta)$-DP** | 16 | `:293` |
| | Proof: good/bad split | 17 | `:309` |
| | Proof: decompose the event | 18 | `:320` |
| | Proof: good piece, pointwise $\to$ setwise | 19 | `:332` |
| | Proof recap chain | 20 | `:342` |
| **03 — Truncated Laplace** | 21–27 | `:354-466` |
| | Recall Laplace: unbounded tails force $\delta = 0$ cost | 22 | `:362` |
| | Construction: truncate + renormalize (density SVG) | 23 | `:378` |
| | **Mechanism + Theorem: $\tau \ge \Delta + (\Delta/\varepsilon)\ln(1/\delta)$** | 24 | `:401` |
| | Where $\delta$ comes from (edge-sliver SVG) | 25 | `:417` |
| | Proof sketch | 26 | `:440` |
| | Laplace vs truncated comparison table | 27 | `:451` |
| **04 — Gaussian mechanism** | 28–43 | `:467-703` |
| | $\ell_2$ sensitivity definition | 29 | `:475` |
| | **Mechanism + Theorem: $\sigma \ge \Delta_2\sqrt{2\ln(1.25/\delta)}/\varepsilon$** | 30 | `:490` |
| | Shifted-Gaussians intuition picture (SVG) | 31 | `:507` |
| | Proof roadmap (4-step algo list) | 32 | `:533` |
| | Proof step 1: privacy loss of a shift | 33 | `:549` |
| | **Proof step 2: complete the square** | 34 | `:561` |
| | Proof: the loss is Gaussian, $I(Y) \sim \mathcal N(K^2/2\sigma^2, K^2/\sigma^2)$ | 35 | `:570` |
| | Proof step 3: Gaussian tail bound | 36 | `:582` |
| | Proof step 4: choosing $\sigma$ | 37 | `:595` |
| | Proof recap chain | 38 | `:605` |
| | **Lemma: projection $v \cdot Z \sim \mathcal N(0, \sigma^2 \lVert v \rVert^2)$** | 39 | `:617` |
| | Multi-dim reduction to 1-D | 40 | `:630` |
| | Projection picture (contour SVG) | 41 | `:641` |
| | Worked example: $d = 10^4$ counting queries | 42 | `:669` |
| | Why Gaussian wins: $\Delta_1 = d$ vs $\Delta_2 = \sqrt d$ (table) | 43 | `:687` |
| **05 — Properties of approximate DP** | 44–51 | `:704-817` |
| | **Theorem: post-processing** + preimage proof | 45 | `:712` |
| | **Theorem: basic composition** + sketch | 46 | `:726` |
| | $k$-fold composition (budget table) | 47 | `:744` |
| | **Theorem: group privacy** | 48 | `:760` |
| | Proof: telescoping hops (hop diagram) | 49 | `:773` |
| | **Theorem: Poisson subsampling** | 50 | `:790` |
| | Outlook: moments accountant, RDP | 51 | `:805` |
| Recap (mechanism/guarantee/trick table) + closer | 52–53 | `:818-836` |

### Key theorems

| Item | Slide(s) | Line |
|---|---|---|
| Definition: $(\varepsilon,\delta)$-DP | 6 | `:121-125` |
| Definition: privacy loss + PLRV $I_{X,X'}(Y)$ | 13 | `:242-247` |
| Lemma (tail bound suffices): $\Pr[I \gt \varepsilon] \le \delta \Rightarrow (\varepsilon,\delta)$-DP | 16 | `:296-301` |
| Proof of tail lemma (good/bad split → decompose → pointwise-to-setwise on the good piece; recap chain) | 17–20 | `:309-353` |
| Truncated Laplace mechanism + theorem: $\tau \ge \Delta + (\Delta/\varepsilon)\ln(1/\delta)$ | 24 | `:404-413` |
| Proof sketch of truncated Laplace (edge mass beyond $\tau - \Delta$ is the $\delta$) | 25–26 | `:417-450` |
| Theorem (Gaussian mechanism): $\sigma \ge \Delta_2\sqrt{2\ln(1.25/\delta)}/\varepsilon$, $\varepsilon \in (0,1)$ | 30 | `:497-502` |
| Proof of Gaussian mechanism, 1-D (loss of a shift → complete-the-square trick → $I(Y) \sim \mathcal N(K^2/2\sigma^2, K^2/\sigma^2)$ → Gaussian tail bound → choose $\sigma$; recap chain) | 33–38 | `:549-616` |
| Lemma (projection): $v \cdot Z \sim \mathcal N(0, \sigma^2 \lVert v \rVert^2)$, rotation-invariance proof | 39 | `:620-628` |
| Multi-dim reduction of the Gaussian proof to 1-D | 40 | `:630-640` |
| Theorem (post-processing) + preimage pull-back proof | 45 | `:715-723` |
| Theorem (basic composition): $(\varepsilon_1+\varepsilon_2, \delta_1+\delta_2)$ | 46 | `:729-732` |
| Theorem (group privacy): $\big(t\varepsilon,\ \frac{e^{t\varepsilon}-1}{e^{\varepsilon}-1}\delta\big)$ + telescoping proof with geometric $\delta$ sum | 48–49 | `:763-789` |
| Theorem (Poisson subsampling): $\varepsilon' = \ln(1+q(e^{\varepsilon}-1))$, $\delta' = q\delta$ | 50 | `:793-797` |

Diagrams: Gaussian-tail SVG (slide 5, `:101`), $\delta$-sliver SVG (8, `:164`), PLRV distribution SVG (15, `:277`), truncated-density SVG (23, `:383`), edge-sliver SVG (25, `:421`), shifted-Gaussians SVG (31, `:511`), contour-projection SVG (41, `:645`); proof-roadmap algo list (32, `:536`) and composition sketch (46, `:733`); telescoping hop diagram (49, `:776`); recap chains via stacked math (20, 38); six numeric tables (7 ratio-vs-additive, 9 interpretations, 11 $\delta$-calibration, 27 Laplace-vs-truncated, 43 $\ell_1$-vs-$\ell_2$, 47 $k$-fold budgets). Citations: Dwork, Kenthapadi, McSherry, Mironov, Naor EUROCRYPT 2006 (definition); Dwork–Roth 2014 (Gaussian mechanism, group privacy); Abadi et al. CCS 2016 + Mironov CSF 2017 (outlook). Authoritative math source: `tex/dp.tex:974–1157`.

---

## dp5-erm.html

**Topic:** Learning as optimization (ERM, excess risk, standing assumptions), exponential mechanism for ERM with full utility proof, advanced composition with proof sketch, the GD→SGD→Noisy GD ladder, DP-SGD with three-step privacy accounting and convex utility proof.

### Sections (60 slides)

| Section | Slides | Line |
|---|---|---|
| Title / Contents | 1–2 | `:51-74` |
| **01 — Learning as optimization** | 3–9 | `:76-187` |
| | From queries to models (flow diagram) | 4 | `:84` |
| | Population vs empirical loss | 5 | `:99` |
| | **Definition: ERM, excess risk** | 6 | `:118` |
| | Standing assumptions (4 cards, why-lines) | 7 | `:144` |
| | **Lemma: sensitivity of $L$ is $\Delta/n$** | 8 | `:157` |
| | Two routes (output vs path) | 9 | `:177` |
| **02 — Private ERM via the exponential mechanism** | 10–23 | `:189-406` |
| | Recall card: EM (dp2) | 11 | `:197` |
| | **Definition: EM for ERM** ($\propto e^{-\varepsilon n L/2\Delta}$) | 12 | `:209` |
| | Density-tilt diagram | 13 | `:222` |
| | **Utility theorem** $O(dGR\log(\varepsilon n/d)/\varepsilon n)$ | 14 | `:241` |
| | Proof roadmap (3 named tricks) | 15 | `:253` |
| | Proof: good/bad sets $A_1$, $A_2$ + level-set diagram | 16 | `:267` |
| | Proof: compare bad to good (density ratio) | 17 | `:294` |
| | Proof: volume ratio by geometry, $(2R/r)^d$ | 18 | `:307` |
| | Proof: exponential beats volume (choose $t$) | 19 | `:328` |
| | Proof: tail → expectation (split integral + tail diagram) | 20 | `:340` |
| | Proof: cap the tail, choose $r = 2Rd/\varepsilon n$ ∎ | 21 | `:366` |
| | Proof recap chain | 22 | `:376` |
| | Discussion: numbers table + sampling-hardness catch | 23 | `:389` |
| **03 — Advanced composition** | 24–32 | `:408-521` |
| | Recall card: basic composition (dp3) | 25 | `:416` |
| | Random-walk intuition diagram | 26 | `:428` |
| | **Advanced composition theorem** | 27 | `:449` |
| | Reading the bound (fluctuation vs drift) | 28 | `:462` |
| | Proof sketch: chain rule of privacy loss | 29 | `:474` |
| | Proof sketch: concentration buys $\sqrt{k}$ | 30 | `:485` |
| | Basic vs advanced numbers table | 31 | `:495` |
| | Budget planning per step | 32 | `:511` |
| **04 — The gradient-descent ladder** | 33–40 | `:523-644` |
| | GD algorithm box | 34 | `:531` |
| | GD contours diagram | 35 | `:547` |
| | **Theorem: GD rate $RG/\sqrt{T}$ (convex)** | 36 | `:571` |
| | SGD algorithm box | 37 | `:584` |
| | Unbiasedness of the sampled gradient | 38 | `:600` |
| | Noisy GD algorithm box | 39 | `:612` |
| | Ladder chain GD→SGD→noisy GD→DP-SGD | 40 | `:629` |
| **05 — DP-SGD** | 41–58 | `:646-903` |
| | Sensitivity problem (no useful $G$) | 42 | `:654` |
| | **Definition: clipping** + ball diagram | 43 | `:667` |
| | **DP-SGD algorithm** (6-step box) | 44 | `:692` |
| | **DP-SGD privacy theorem** ($\sigma \ge 2G\sqrt{2T\log(1/\delta)}/n\varepsilon$) | 45 | `:710` |
| | Accounting roadmap (3 steps) | 46 | `:723` |
| | Step 1: Gaussian mechanism, sensitivity $2G$ (recall dp4) | 47 | `:737` |
| | Step 2: subsampling amplification, $q = 1/n$ (recall dp3) | 48 | `:750` |
| | Step 3: compose $T$ steps | 49 | `:769` |
| | Accounting recap chain, solve for $\sigma$ ∎ | 50 | `:785` |
| | Why $T = O(n^2)$ steps are affordable | 51 | `:797` |
| | Fine print: advanced comp vs moments accountant vs RDP | 52 | `:807` |
| | **DP-SGD utility theorem (convex)** | 53 | `:821` |
| | Proof: noisy gradient oracle, $B^2 = G^2 + d\sigma^2$ | 54 | `:834` |
| | **Lemma: standard SGD convergence** | 55 | `:846` |
| | Proof: plug in and balance, $T = \varepsilon^2 n^2/d$ ∎ | 56 | `:858` |
| | EM-ERM vs DP-SGD table ($\sqrt{d}$ beats $d$) | 57 | `:871` |
| | Beyond convexity + pretrain/fine-tune flow | 58 | `:886` |
| Recap + closer | 59–60 | `:905-921` |

### Key theorems

| Item | Slides | Line |
|---|---|---|
| Lemma (sensitivity of $L$): $\lvert L(\theta;X) - L(\theta;X')\rvert \le \Delta/n$ | 8 | `:161-162` |
| EM-ERM utility theorem: excess risk $O(dGR\log(\varepsilon n/d)/\varepsilon n)$ | 14 | `:245-247` |
| EM-ERM utility proof (good/bad split → density ratio → volume ratio $(2R/r)^d$ → choose $t$ → tail integral with honest $\min(1,\cdot)$ cap → $r = 2Rd/\varepsilon n$; recap chain) | 16–22 | `:267-387` |
| Theorem (advanced composition): $\varepsilon' = \sqrt{2k\ln(1/\delta')}\,\varepsilon + k\varepsilon\frac{e^\varepsilon-1}{e^\varepsilon+1}$ | 27 | `:453-456` |
| Proof sketch (chain rule of privacy loss + Azuma-type concentration) | 29–30 | `:474-493` |
| Theorem (GD rate, convex): $\mathcal{L}(\theta_T) \le \mathcal{L}(\theta^\star) + RG/\sqrt{T}$ at $\alpha = R/(G\sqrt{T})$ | 36 | `:575-577` |
| Theorem (DP-SGD privacy): $\sigma \ge 2G\sqrt{2T\log(1/\delta)}/(n\varepsilon)$ | 45 | `:714-716` |
| Three-step accounting (Gaussian step with sensitivity $2G$ → amplify by $q=1/n$ → compose $T$; recap chain solving for $\sigma$) | 47–50 | `:737-795` |
| Lemma (standard SGD convergence): $RB/\sqrt{T}$ under $\mathbb{E}\lVert\tilde g\rVert^2 \le B^2$ | 55 | `:850-852` |
| Theorem (DP-SGD rate, convex): $O(RG\sqrt{d\log(1/\delta)}/\varepsilon n)$ at $T = \varepsilon^2 n^2/d$ | 53 | `:825-830` |

Diagrams: query→model flow (4, `:88`), population-vs-empirical chain (5, `:107`), excess-risk loss-curve SVG (6, `:125`), record-cells sensitivity strip (8, `:165`), density-tilt SVG (13, `:226`), good/bad level-set SVG (16, `:275`), volume-geometry balls SVG (18, `:312`), tail-integral area SVG (20, `:348`), random-walk envelope SVG (26, `:432`), GD contours SVG (35, `:551`), ladder chain (40, `:632`), clipping-ball SVG (43, `:674`), subsampling record-cells (48, `:757`), accounting chain (49, `:774`), pretrain/fine-tune flow (58, `:894`); algorithm boxes for GD/SGD/Noisy GD/DP-SGD (34, 37, 39, 44); recap chains via stacked math (22, 50, 56); three numeric tables (23 EM excess risk, 31 basic-vs-advanced, 57 EM vs DP-SGD). Citations: Dwork–Roth 2014 (advanced composition); Abadi et al. CCS 2016 (DP-SGD, moments accountant). Authoritative math source: `tex/dp.tex:1158–1506`. TODO marker: real figure from Abadi et al. (accuracy-vs-$\varepsilon$ curves) on slide 58.

---

## dp6-rdp.html

**Topic:** The composition-accounting problem, KL-DP and its tail weakness, Rényi divergence (definition, worked Gaussian example, both limits with proofs, monotonicity), $(\alpha,\varepsilon)$-RDP with full proofs of post-processing / additive composition / conversion to $(\varepsilon,\delta)$, the pure-DP bridge lemma $D_\alpha \le 2\alpha\varepsilon^2$ with advanced composition rederived, and the Gaussian mechanism's exact RDP cost via complete-the-square.

### Sections (56 slides)

| Section | Slides | Line |
|---|---|---|
| Title / Contents | 1–2 | `:47-69` |
| **01 — The accounting problem** (setting, advanced-composition bookkeeping, curve-vs-add diagram, ledger wishlist) | 3–7 | `:72-165` |
| | Two ways to keep the books (SVG) | 6 | `:116` |
| **02 — KL divergence privacy** (loss RV, definition, average-vs-worst figure, tail counterexample) | 8–12 | `:168-230` |
| | **Definition: KL-DP** | 10 | `:187` |
| | Weakness: tiny mean, catastrophic tail ($0.002$ vs $e^{20}$) | 12 | `:220` |
| **03 — Rényi divergence** (definition, log-MGF identity, worked example, both limits + proofs, monotonicity) | 13–21 | `:233-355` |
| | **Definition: $D_\alpha$** | 14 | `:241` |
| | Log-MGF identity $e^{(\alpha-1)D_\alpha} = \mathbb{E}_P[e^{(\alpha-1)L}]$ | 15 | `:254` |
| | Worked example: two shifted Gaussians, anchor table | 16 | `:264` |
| | Lemma + proof: $\alpha \to 1$ gives KL (L'Hôpital) | 17–18 | `:282, :294` |
| | Lemma + proof: $\alpha \to \infty$ gives max divergence (squeeze) | 19–20 | `:308, :320` |
| | Monotonicity in $\alpha$ (SVG plot) | 21 | `:333` |
| **04 — Rényi differential privacy** (definition, spectrum, three properties with full proofs, bridge lemma, advanced composition rederived) | 22–42 | `:358-622` |
| | **Definition: $(\alpha,\varepsilon)$-RDP** | 23 | `:366` |
| | The $\alpha$ spectrum (SVG axis) | 24 | `:380` |
| | **Post-processing** (DPI statement; mixture + Jensen proof) | 25–27 | `:402, :415, :425` |
| | **Composition (additive)** (statement; factorize + bound proof; $k$-fold corollary) | 28–30 | `:438, :450, :460` |
| | **Conversion to $(\varepsilon,\delta)$-DP** (statement; split / Markov / threshold proof; numeric example) | 31–36 | `:476, :490, :505, :516, :527, :538` |
| | **Bridge lemma: $\varepsilon$-DP $\Rightarrow$ $D_\alpha \le 2\alpha\varepsilon^2$** (Hoeffding + symmetrized-KL proof) | 37–40 | `:548, :562, :573, :586` |
| | Advanced composition rederived; $\sqrt{k}$ law via AM–GM | 41–42 | `:597, :615` |
| **05 — Gaussian mechanism via RDP** (recall, exact theorem, MGF intuition, complete-the-square proof, conversion, comparisons) | 43–54 | `:625-777` |
| | **Theorem: Gaussian is exactly $(\alpha, \alpha\Delta^2/2\sigma^2)$-RDP** | 45 | `:647` |
| | Intuition: Gaussian loss has Gaussian MGF | 46 | `:660` |
| | Proof: setup / expand / complete square / constant / finish | 47–51 | `:671, :683, :696, :706, :720` |
| | Optimize $\alpha$ for $(\varepsilon,\delta)$ (SVG trade-off plot) | 52 | `:733` |
| | RDP matches classic rule (single shot) | 53 | `:757` |
| | Where RDP wins: $T=1000$ composed Gaussians table ($124$ / $27$ / $3.2$) | 54 | `:767` |
| Recap + closer | 55–56 | `:783-796` |

### Key theorems

| Item | Line |
|---|---|
| KL-DP definition | `:193` |
| Rényi divergence definition | `:247` |
| Log-MGF identity | `:258` |
| Order-1 limit lemma (KL) | `:287` |
| Order-$\infty$ limit lemma (max divergence) | `:313` |
| $(\alpha,\varepsilon)$-RDP definition | `:372` |
| Post-processing theorem (via DPI) | `:407-408` |
| Composition theorem (additive) | `:443-444` |
| Conversion to $(\varepsilon,\delta)$-DP | `:483` |
| Bridge lemma ($D_\alpha \le 2\alpha\varepsilon^2$) | `:555` |
| Gaussian RDP theorem (Mironov 2017, equality) | `:653` |
| Optimized Gaussian conversion $\varepsilon(\delta)$ | `:736-737` |

Diagrams: curve-vs-add bookkeeping (slide 6), ledger pipeline chain (slide 7), average-vs-worst loss distribution (slide 11), monotonicity plot (slide 21), $\alpha$ spectrum axis (slide 24), advanced-composition pipeline chain (slide 41), $\alpha$-optimization trade-off plot (slide 52). Citations: Mironov, "Rényi Differential Privacy", CSF 2017; Dwork–Roth 2014.

---

# dp7-ml-paradigms.html — DP Paradigms in ML and PATE (47 slides)

Updated outline section for the leaf `OUTLINE.md` (do not merge automatically; line numbers verified against the current file).

## Deck section table

| # | Section | Slides | Lines |
|---|---------|--------|-------|
| — | Title / Contents | 1–2 | 70–94 |
| 01 | Where to inject noise? (output / objective / gradient perturbation) | 3–15 | 95–311 |
| 02 | The privacy boundary (input / inference / model DP) | 16–23 | 312–460 |
| 03 | PATE (teachers, noisy votes, student) | 24–35 | 461–678 |
| 04 | PATE privacy accounting | 36–41 | 679–775 |
| 05 | Trade-offs (PATE vs DP-SGD) | 42–46 | 776–839 |
| — | Closer (Q&A, .end-slide no-footer) | 47 | 840–845 |

## Key statements (with line numbers)

- Recall (private ERM), $L(w;X)=\frac1n\sum\ell(w;z_i)$, per-record move $\Delta_\ell/n$ — line 108
- Definition (output/parameter perturbation), $\Delta_{\arg\min}$, $Z\sim\mathrm{Lap}(\Delta_{\arg\min}/\varepsilon)^{\otimes d}$ — line 155
- Mean-vs-median micro-example: squared loss $\Delta=1/n$ vs absolute loss $\Delta_{\arg\min}=1$ — lines 195–207
- Mechanism (private mean), $\bar z+\mathrm{Lap}(\frac{1}{n\varepsilon})$ is $\varepsilon$-DP — line 213
- Definition (objective perturbation), $\hat w=\arg\min_w[L(w;X)+\langle b,w\rangle]$; Chaudhuri–Monteleoni–Sarwate JMLR 2011 — line 228
- Recall (DP-SGD), $\sigma \ge 2G\sqrt{2T\log(1/\delta)}/(n\varepsilon)$; Abadi et al. CCS 2016 — line 256
- Excess risk for convex private ERM: $O(d\cdot\ln(1/\delta)/(n\varepsilon))$ — lines 299–311
- Definition (input perturbation, local DP) — line 369; Recall (randomized response, $\varepsilon_\gamma=\ln\frac{1/2+\gamma}{1/2-\gamma}$) — line 375
- Definition (inference DP, per-query output perturbation), $M_x(X)=f_{A(X)}(x)+Z$, $\Delta_x$ — line 386
- Budget-exhaustion table ($k$ queries at $\varepsilon_0=0.1$ → $k\varepsilon_0$) — lines 397–414
- Definition (model DP, global DP), training map $M:X\mapsto\theta$ — line 420
- Recall (post-processing immunity) — line 435; Proposition (unlimited queries): adaptive $g(\theta)$ stays $(\varepsilon,\delta)$-DP — line 439
- Paradigm taxonomy table (mechanism / neighboring pair / guarantee covers) — lines 446–460
- PATE Phase 1, Definition (teacher ensemble), disjoint shards $X=X_1\sqcup\cdots\sqcup X_n$ — line 509; Papernot et al. ICLR 2017 cite — lines 483–484
- Vote histogram $v_y(x)=|\{i: T_i(x)=y\}|$, sensitivity $\lVert v-v'\rVert_\infty\le 1$ — lines 533–547
- Definition (noisy argmax aggregation), $\tilde v_y=v_y(x)+\mathrm{Lap}(1/\varepsilon_0)$; PATE-G Gaussian variant — line 554
- Recall (Noisy Max) — line 566; Proposition (per-query cost): each released label is $2\varepsilon_0$-DP — line 570; proof sketch via threshold argument — lines 576–591
- Phase 3 student distillation; public-pool standing assumption — lines 623–637
- PATE mechanism $M_{\mathrm{PATE}}(X)=(\hat y(x_1^{\mathrm{pub}}),\dots,\hat y(x_m^{\mathrm{pub}}))$ — lines 663–673; Corollary (student is model DP) — line 674
- Advanced composition $\varepsilon'=\sqrt{2m\log(1/\delta')}\cdot\varepsilon_q+m\varepsilon_q(e^{\varepsilon_q}-1)$ — lines 706–718
- Anchor numbers ($m=1000$, $\varepsilon_q=0.05$, $\delta'=10^{-5}$: basic 50, advanced ≈10.2) — lines 719–734
- Claim (informal, data-dependent accounting: consensus margin → tiny RDP cost) — line 740
- PATE vs DP-SGD comparison table — lines 811–826

## Diagrams

- Training-pipeline diagram with three injection points (slide 5, lines 115–149)
- Flat-valley vs strong-curvature SVG (argmin sensitivity, slide 7, lines 164–194)
- Three-barrier rows: input / inference / model DP (slide 17, lines 320–363)
- Teacher-voting consensus row (slide 26, lines 487–503); shard-cells diagram (slide 27)
- Consensus vs contested vote-histogram SVG (slide 32, lines 592–622)
- PATE full-pipeline row with "only privacy spend" under-label (slide 34, lines 638–662)
- Accounting ledger and recipe chains (slides 37, 41)

## Companion files

None. No speaker note or technical supplement for this deck yet.

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
