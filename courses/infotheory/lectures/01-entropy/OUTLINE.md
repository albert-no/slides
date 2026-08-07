# infotheory/lectures/01-entropy/ — Entropy and basic information-theoretic quantities

Two-lecture foundation series. Discrete-domain definitions, properties, and inequalities. Paired with `-note.html` companions.

## Files

| Deck | Note | Topic |
|---|---|---|
| `entropy1-entropy-kl.html` | `entropy1-entropy-kl-note.html` | Entropy, $H_b$, KL divergence |
| `entropy2-joint-mi-fano.html` | `entropy2-joint-mi-fano-note.html` | Joint, conditional, MI, DPI, Fano |

---

## entropy1-entropy-kl.html — Entropy and KL Divergence

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:24, :35` |
| **01 — Entropy** | Self-information, definition, examples | `:70-223` |
| | Motivation — a guessing game | `:70` |
| | Three desiderata for information | `:97` |
| | Self-information $i_X(x) = -\log p_X(x)$ | `:108` |
| | Technique — why $-\log$ is forced | `:121` |
| | **Definition of entropy** | `:130` |
| | Reading the definition | `:141` |
| | Example — Bernoulli($p$) | `:151` |
| | Example — Uniform($n$) | `:162` |
| | Example — Geometric($p$) | `:173` |
| | Example — three-symbol source | `:184` |
| | Continuity (dyadic vs nearby) | `:192` |
| | Why $\log$? — additivity for independence | `:205` |
| **02 — Properties** | Bounds, concavity, max at uniform | `:224-372` |
| | Intuition — where uncertainty lives | `:224` |
| | **Theorem — non-negativity & uniform max** | `:252` |
| | Proof — $H(X)\ge 0$ | `:262` |
| | Recall — Jensen's inequality | `:270` |
| | Technique — applying Jensen | `:281` |
| | **Theorem — $H(X)\le\log\|\mathcal{X}\|$** | `:294` |
| | **Concavity of entropy** | `:305` |
| | Proof — concavity | `:315` |
| | Example — mixing two coins | `:324` |
| | Interpretation — losing the label | `:336` |
| **03 — Binary entropy** | $H_b(p)$, computations, plot | `:373-438` |
| | Definition + plot | `:373` |
| | Concavity from $H_b''$ | `:403` |
| | Worked values | `:411` |
| | Recursive identity (binary $\to$ general) | `:422` |
| **04 — KL divergence** | Definition, Gibbs, log-sum, examples | `:439-632` |
| | A wrong codebook (motivation) | `:439` |
| | Motivation | `:460` |
| | **Definition of KL** | `:475` |
| | Reading the definition | `:486` |
| | Intuition — why divergence is non-negative | `:497` |
| | **Theorem — Gibbs $D(p\|q)\ge 0$** | `:506` |
| | Proof — Gibbs via Jensen | `:517` |
| | Technique — the $\ln t \le t-1$ trick | `:528` |
| | Corollary — max entropy from Gibbs | `:537` |
| | Example — two Bernoullis (asymmetry) | `:547` |
| | Interpretation — mismatch cost in coding | `:558` |
| | What KL measures (three faces) | `:569` |
| | **Theorem — log-sum inequality** | `:580` |
| | Proof — log-sum | `:591` |
| | Corollary — joint convexity of KL | `:600` |
| | Pinsker's inequality (statement) | `:608` |
| Recap / Next | | `:619, :633` |

**Key:** entropy definition `:130`; $H(X)\ge 0$ proof `:262`; $H(X)\le\log\|\mathcal{X}\|$ `:294`; concavity `:305`; KL definition `:475`; Gibbs theorem `:506`; log-sum `:580`.

### Note (`entropy1-entropy-kl-note.html`)
- Khinchin's axiomatic characterization
- Functional-equation justification of $-\log$
- Concavity via second derivative on the simplex
- Worked $H_b(1/4)$ derivation
- Recursive splitting identity proof
- KL asymmetry — operational interpretation
- Gibbs via $\ln t \le t-1$
- Pinsker proof sketch (Csiszár reduction)
- A wrong codebook — cross-entropy numerics
- What KL measures — three faces (coding, testing, betting)
- Interpretation — losing the label (concavity gap = $I(X;T)$)

---

## entropy2-joint-mi-fano.html — Joint, conditional, MI, Fano

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:25, :36` |
| **01 — Joint and conditional** | $H(X,Y)$, $H(X\mid Y)$, chain rule | `:64-217` |
| | Joint entropy definition | `:71` |
| | Example — two coin flips | `:81` |
| | **Conditional entropy — two definitions** | `:91` |
| | Reading the definition | `:102` |
| | **Theorem — chain rule** | `:111` |
| | Proof — chain rule | `:121` |
| | Intuition — telescoping the chain | `:132` |
| | Example — two correlated coins | `:140` |
| | Why — does a side observation help? | `:156` |
| | **Theorem — conditioning reduces entropy** | `:167` |
| | Proof | `:178` |
| | $H(X\mid Y=y) > H(X)$ — concrete case | `:190` |
| | Functional dependence lemma | `:201` |
| | Subadditivity | `:211` |
| **02 — Mutual information** | Definition, Venn, examples | `:220-367` |
| | Why — a number for "shared bits" | `:228` |
| | **Definition of MI** | `:240` |
| | Reading the definition | `:250` |
| | Intuition — three faces of MI | `:261` |
| | Venn picture | `:280` |
| | Example — Bernoulli pair (BSC) | `:305` |
| | Example — erasure channel | `:317` |
| | Bounds on MI | `:328` |
| | What MI measures — channel capacity | `:338` |
| | **Theorem — chain rule for MI** | `:349` |
| | Proof — chain rule for MI | `:358` |
| **03 — Conditional MI & DPI** | Markov, data processing | `:369-487` |
| | Conditional MI definition | `:377` |
| | Conditioning can increase MI (XOR) | `:388` |
| | Markov chain definition | `:400` |
| | Why — can cleanup recover lost signal? | `:415` |
| | **Theorem — DPI** | `:426` |
| | Intuition — information only leaks | `:437` |
| | Proof — DPI (technique: chain + non-neg) | `:454` |
| | Corollary — function of $Y$ | `:464` |
| | Example — cascade of BSCs | `:476` |
| **04 — Fano's inequality** | Error lower bound, applications | `:489-626` |
| | Setup — inferring $X$ from $Y$ | `:497` |
| | Why — a floor on guessing error | `:507` |
| | **Theorem — Fano** | `:518` |
| | Intuition — guess well ⇒ low entropy | `:530` |
| | Proof — Fano (Step 1, auxiliary indicator) | `:540` |
| | Proof — Fano (Step 2) | `:549` |
| | Application — channel coding converse | `:561` |
| | Example — binary estimation | `:573` |
| | Example — $M$-ary hypothesis testing | `:585` |
| | Equality in Fano | `:594` |
| Recap / Next | | `:603, :617` |

**Key:** chain rule `:111`; conditioning reduces entropy `:167`; MI definition `:240`; chain rule for MI `:349`; DPI `:426`; Fano `:518`.

### Note (`entropy2-joint-mi-fano-note.html`)
- Joint table example — full numbers
- Why $H(X\mid Y=y)$ can exceed $H(X)$
- Subadditivity → total correlation
- Three faces of MI (operational, KL, variational)
- What MI measures — capacity + noisy-channel coding theorem
- Erasure channel capacity sketch
- XOR collider-bias detail
- DPI equality = sufficient statistic
- Cascade-BSC crossover composition
- Fano two forms
- Channel-coding converse full sketch
- Minimax statistical estimation via Fano
