# infotheory/lectures/03-diffentropy/ — Differential entropy and continuous-domain MI (3 lectures)

Three-lecture series. Continuous-domain analogue of the discrete entropy series. Paired with `-note.html` companions.

## Files

| Deck | Note | Topic |
|---|---|---|
| `diffentropy1-foundations.html` | `diffentropy1-foundations-note.html` | Definition, examples, scaling, joint/conditional |
| `diffentropy2-maxent-gaussian.html` | `diffentropy2-maxent-gaussian-note.html` | MaxEnt principle, Gaussian, EPI |
| `diffentropy3-mi-awgn.html` | `diffentropy3-mi-awgn-note.html` | MI, AWGN capacity, water-filling, I-MMSE |

---

## diffentropy1-foundations.html — Foundations

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:24, :35` |
| **01 — Discrete to continuous** | | `:63-149` |
| | A thought experiment (motivation) | `:71` |
| | Why a new definition | `:91` |
| | **Definition — differential entropy** | `:106` |
| | Discretization bridge | `:117` |
| | Reading the bridge | `:129` |
| | Not an absolute information count (interpretation) | `:140` |
| **02 — Examples** | Standard families | `:150-225` |
| | Uniform $[a,b]$ | `:158` |
| | Gaussian $\mathcal{N}(\mu,\sigma^2)$ | `:170` |
| | Exponential | `:182` |
| | Laplace | `:193` |
| | Cauchy | `:205` |
| | Multivariate Gaussian | `:213` |
| **03 — Properties** | Scaling, can be negative | `:226-329` |
| | Translation invariance | `:234` |
| | **Scaling — $h(aX) = h(X) + \log\|a\|$** | `:245` |
| | Scaling — the picture (intuition) | `:257` |
| | Technique — change of variables | `:278` |
| | Linear transformation | `:289` |
| | A puzzle | `:300` |
| | $h$ can be negative | `:308` |
| | What is meaningful | `:318` |
| **04 — Joint and conditional** | Chain rule, KL, MI | `:330-459` |
| | Joint differential entropy | `:338` |
| | Conditional differential entropy | `:348` |
| | Chain rule | `:358` |
| | KL divergence (continuous) | `:368` |
| | Why KL is scale-invariant | `:378` |
| | Conditioning reduces $h$ | `:389` |
| | Mutual information — definition | `:397` |
| | **Theorem — MI scaling invariance** | `:407` |
| | Why MI survives the infinities (interpretation) | `:422` |
| | Example — independent Gaussians | `:430` |
| | Example — correlated Gaussians | `:440` |
| Recap / Next | | `:449, :461` |

**Key:** definition `:106`; discretization bridge `:117`; scaling `:245`; MI definition `:397`; MI invariance `:407`.

### Note (`diffentropy1-foundations-note.html`)
- Thought-experiment motivation for a new definition
- Discretization bridge proof
- Why $h$ can be negative (expanded)
- Cauchy entropy computation
- Multivariate Gaussian $h$ derivation
- Change-of-variables technique
- Linear-transform Jacobian
- KL convexity, Pinsker, DPI
- Why MI survives the infinities (detail)
- Mixed discrete/continuous case

---

## diffentropy2-maxent-gaussian.html — MaxEnt and the Gaussian

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:24, :35` |
| **01 — MaxEnt principle** | Lagrangian, exponential family | `:63-134` |
| | A design question (motivation) | `:70` |
| | The MaxEnt question | `:85` |
| | Lagrangian | `:93` |
| | The MaxEnt density (exp family) | `:101` |
| | Catalogue — three constraint types | `:109` |
| | Jaynes' rationale (least-informative prior) | `:122` |
| **02 — Gaussian = MaxEnt** | Variance constraint | `:135-243` |
| | **Theorem — Gaussian MaxEnt** | `:142` |
| | Intuition — cross term vanishes | `:153` |
| | Proof — KL inequality (setup) | `:161` |
| | Proof — cross-term | `:168` |
| | Proof — combining | `:180` |
| | **The KL trick — general recipe** | `:191` |
| | Proof variant — Lagrangian | `:199` |
| | Numerical examples | `:208` |
| | **Corollary — Hadamard's inequality** | `:220` |
| | Intuition — correlation is wasted uncertainty | `:228` |
| **03 — Multivariate Gaussian** | Hadamard, conditioning | `:244-296` |
| | **Theorem — multivariate MaxEnt** | `:251` |
| | Conditioning Gaussians | `:262` |
| | MI for Gaussians | `:271` |
| | Translation invariance revisited | `:282` |
| **04 — EPI** | Entropy power inequality | `:297-406` |
| | Definition — entropy power | `:304` |
| | Why is Gaussian noise the worst? (motivation) | `:317` |
| | **Theorem — EPI** | `:331` |
| | Equivalent form | `:342` |
| | Intuition — adding de-peaks slowly | `:350` |
| | Special case — both Gaussian | `:358` |
| | Why "Gaussians are hardest" | `:368` |
| | Application — AWGN converse sketch | `:375` |
| | Application — CLT-style | `:387` |
| Recap | | `:395` |

**Key:** Gaussian MaxEnt `:142`; KL-trick proof `:161-189`; general KL trick `:191`; Hadamard `:220`; EPI `:331`.

### Note (`diffentropy2-maxent-gaussian-note.html`)
- Design-question motivation (least-informative prior)
- Variational calculus rigor
- Cross-term-vanishes intuition
- Gaussian via generalized KL trick
- Hadamard direct proof + correlation-as-wasted-uncertainty intuition
- Schur complement detail
- Worst-case-noise motivation for EPI
- Entropy-powers-add-sub-additively intuition
- EPI proof sketch (Stam)
- Why EPI ⇒ Gaussian-hardest
- Vector Gaussian channel capacity

---

## diffentropy3-mi-awgn.html — MI and the AWGN Channel

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:24, :35` |
| **01 — Continuous MI** | Definition, properties, examples | `:63-127` |
| | Definition (recap) | `:71` |
| | Discretization bridge for MI | `:83` |
| | Properties — all inherited | `:95` |
| | Example — bivariate Gaussian | `:107` |
| | Example — additive Gaussian noise | `:118` |
| **02 — AWGN channel** | $C = \tfrac{1}{2}\log(1+\mathrm{SNR})$ | `:130-249` |
| | Setup | `:138` |
| | Motivation — how many bits through noise? | `:150` |
| | **Theorem — Shannon–Hartley** | `:161` |
| | Technique — two sides of a capacity proof | `:171` |
| | Proof — achievability | `:181` |
| | Proof — converse | `:192` |
| | Intuition — why EPI supplies the converse | `:204` |
| | Interpretation — the Shannon limit | `:214` |
| | Numerical examples | `:224` |
| | Bandwidth-limited form | `:237` |
| **03 — Parallel channels** | Water-filling | `:250-362` |
| | Motivation — the power-budget puzzle | `:258` |
| | Setup | `:269` |
| | Optimization problem | `:277` |
| | Technique — Lagrangian / KKT | `:284` |
| | **Theorem — water-filling** | `:291` |
| | Water-filling — picture (uneven-floor metaphor) | `:305` |
| | Interpretation — water level = shadow price | `:336` |
| | Example — three sub-channels | `:346` |
| | Application — frequency-selective | `:355` |
| **04 — Connections** | I-MMSE, de Bruijn, diffusion | `:363-478` |
| | MMSE | `:371` |
| | Intuition — information meets estimation | `:379` |
| | **Theorem — I-MMSE** | `:389` |
| | Sanity check — Gaussian input | `:400` |
| | Interpretation — what I-MMSE buys you | `:411` |
| | Technique — small-SNR perturbation flavor | `:418` |
| | **Theorem — de Bruijn** | `:428` |
| | Intuition — entropy under smoothing (heat eq.) | `:439` |
| | Application — diffusion models | `:446` |
| Recap series + Connections | | `:455, :467` |

**Key:** Shannon–Hartley `:161`; water-filling `:291`; I-MMSE `:389`; de Bruijn `:428`.

### Note (`diffentropy3-mi-awgn-note.html`)
- Achievability/converse reusable pattern (continuous setting)
- Why EPI, not just MaxEnt (block converse)
- AWGN full coding theorem outline
- Bandwidth-limited continuous-time form
- Water-filling KKT derivation
- I-MMSE proof sketch (Guo–Shamai–Verdú) + small-SNR perturbation + integral form
- de Bruijn via heat equation
- Diffusion-models information-theoretic loss
