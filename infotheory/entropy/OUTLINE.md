# infotheory/entropy/ — Entropy and basic information-theoretic quantities

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
| **01 — Entropy** | Self-information, definition, examples | `:63-178` |
| | Three desiderata for information | `:70` |
| | Self-information $i_X(x) = -\log p_X(x)$ | `:81` |
| | **Definition of entropy** | `:94` |
| | Reading the definition | `:105` |
| | Example — Bernoulli($p$) | `:115` |
| | Example — Uniform($n$) | `:126` |
| | Example — Geometric($p$) | `:137` |
| | Example — three-symbol source | `:148` |
| | Continuity (dyadic vs nearby) | `:156` |
| | Why $\log$? — additivity for independence | `:169` |
| **02 — Properties** | Bounds, concavity, max at uniform | `:180-258` |
| | **Theorem — non-negativity & uniform max** | `:188` |
| | Proof — $H(X)\ge 0$ | `:198` |
| | Recall — Jensen's inequality | `:206` |
| | **Theorem — $H(X)\le\log\|\mathcal{X}\|$** | `:217` |
| | **Concavity of entropy** | `:228` |
| | Proof — concavity | `:238` |
| | Example — mixing two coins | `:247` |
| **03 — Binary entropy** | $H_b(p)$, computations, plot | `:260-325` |
| | Definition + plot | `:268` |
| | Concavity from $H_b''$ | `:298` |
| | Worked values | `:306` |
| | Recursive identity (binary $\to$ general) | `:317` |
| **04 — KL divergence** | Definition, Gibbs, log-sum, examples | `:326-477` |
| | Motivation | `:334` |
| | **Definition of KL** | `:349` |
| | Reading the definition | `:360` |
| | **Theorem — Gibbs $D(p\|q)\ge 0$** | `:371` |
| | Proof — Gibbs via Jensen | `:382` |
| | Corollary — max entropy from Gibbs | `:393` |
| | Example — two Bernoullis (asymmetry) | `:403` |
| | Example — mismatch cost in coding | `:414` |
| | **Theorem — log-sum inequality** | `:425` |
| | Proof — log-sum | `:436` |
| | Corollary — joint convexity of KL | `:445` |
| | Pinsker's inequality (statement) | `:453` |
| Recap / Next | | `:464, :478` |

**Key:** entropy definition `:94`; $H(X)\ge 0$ proof `:198`; $H(X)\le\log\|\mathcal{X}\|$ `:217`; concavity `:228`; KL definition `:349`; Gibbs theorem `:371`; log-sum `:425`.

### Note (`entropy1-entropy-kl-note.html`)
- Khinchin's axiomatic characterization
- Functional-equation justification of $-\log$
- Concavity via second derivative on the simplex
- Worked $H_b(1/4)$ derivation
- Recursive splitting identity proof
- KL asymmetry — operational interpretation
- Gibbs via $\ln t \le t-1$
- Pinsker proof sketch (Csiszár reduction)

---

## entropy2-joint-mi-fano.html — Joint, conditional, MI, Fano

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:25, :36` |
| **01 — Joint and conditional** | $H(X,Y)$, $H(X\mid Y)$, chain rule | `:63-198` |
| | Joint entropy definition | `:71` |
| | Example — two coin flips | `:81` |
| | **Conditional entropy — two definitions** | `:90` |
| | Reading the definition | `:101` |
| | **Theorem — chain rule** | `:110` |
| | Proof — chain rule | `:120` |
| | Example — two correlated coins | `:131` |
| | **Theorem — conditioning reduces entropy** | `:147` |
| | Proof | `:158` |
| | $H(X\mid Y=y) > H(X)$ — concrete case | `:170` |
| | Functional dependence lemma | `:181` |
| | Subadditivity | `:191` |
| **02 — Mutual information** | Definition, Venn, examples | `:200-306` |
| | **Definition of MI** | `:208` |
| | Reading the definition | `:218` |
| | Venn picture | `:229` |
| | Example — Bernoulli pair (BSC) | `:254` |
| | Example — erasure channel | `:266` |
| | Bounds on MI | `:277` |
| | **Theorem — chain rule for MI** | `:287` |
| | Proof — chain rule for MI | `:296` |
| **03 — Conditional MI & DPI** | Markov, data processing | `:307-398` |
| | Conditional MI definition | `:315` |
| | Conditioning can increase MI (XOR) | `:326` |
| | Markov chain definition | `:338` |
| | **Theorem — DPI** | `:353` |
| | Proof — DPI | `:364` |
| | Corollary — function of $Y$ | `:374` |
| | Example — cascade of BSCs | `:386` |
| **04 — Fano's inequality** | Error lower bound, applications | `:399-505` |
| | Setup — inferring $X$ from $Y$ | `:407` |
| | **Theorem — Fano** | `:417` |
| | Proof — Fano (Step 1) | `:429` |
| | Proof — Fano (Step 2) | `:438` |
| | Application — channel coding converse | `:450` |
| | Example — binary estimation | `:462` |
| | Example — $M$-ary hypothesis testing | `:473` |
| | Equality in Fano | `:482` |
| Recap / Next | | `:492, :506` |

**Key:** chain rule `:110`; conditioning reduces entropy `:147`; MI definition `:208`; chain rule for MI `:287`; DPI `:353`; Fano `:417`.

### Note (`entropy2-joint-mi-fano-note.html`)
- Joint table example — full numbers
- Why $H(X\mid Y=y)$ can exceed $H(X)$
- Subadditivity → total correlation
- Three faces of MI (operational, KL, variational)
- Erasure channel capacity sketch
- XOR collider-bias detail
- DPI equality = sufficient statistic
- Cascade-BSC crossover composition
- Fano two forms
- Channel-coding converse full sketch
- Minimax statistical estimation via Fano
