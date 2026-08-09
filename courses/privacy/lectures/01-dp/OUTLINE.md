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
