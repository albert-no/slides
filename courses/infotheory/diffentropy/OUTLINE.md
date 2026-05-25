# infotheory/diffentropy/ — Differential entropy and continuous-domain MI (3 lectures)

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
| **01 — Discrete to continuous** | | `:63-117` |
| | Why a new definition | `:70` |
| | **Definition — differential entropy** | `:85` |
| | Discretization bridge | `:96` |
| | Reading the bridge | `:108` |
| **02 — Examples** | Standard families | `:121-193` |
| | Uniform $[a,b]$ | `:128` |
| | Gaussian $\mathcal{N}(\mu,\sigma^2)$ | `:140` |
| | Exponential | `:152` |
| | Laplace | `:163` |
| | Cauchy | `:175` |
| | Multivariate Gaussian | `:183` |
| **03 — Properties** | Scaling, can be negative | `:197-255` |
| | Translation invariance | `:204` |
| | **Scaling — $h(aX) = h(X) + \log\|a\|$** | `:215` |
| | Linear transformation | `:227` |
| | $h$ can be negative | `:238` |
| | What is meaningful | `:246` |
| **04 — Joint and conditional** | Chain rule, KL, MI | `:258-381` |
| | Joint differential entropy | `:266` |
| | Conditional differential entropy | `:276` |
| | Chain rule | `:286` |
| | KL divergence (continuous) | `:296` |
| | Why KL is scale-invariant | `:306` |
| | Conditioning reduces $h$ | `:317` |
| | Mutual information | `:325` |
| | **Theorem — MI scaling invariance** | `:335` |
| | Example — independent Gaussians | `:350` |
| | Example — correlated Gaussians | `:360` |
| Recap / Next | | `:369, :381` |

**Key:** definition `:85`; bridge `:96`; scaling `:215`; KL invariance `:306`; MI invariance `:335`.

### Note (`diffentropy1-foundations-note.html`)
- Discretization bridge proof
- Why $h$ can be negative
- Cauchy entropy computation
- Multivariate Gaussian $h$ derivation
- Linear-transform Jacobian
- KL convexity, Pinsker, DPI
- Mixed discrete/continuous case

---

## diffentropy2-maxent-gaussian.html — MaxEnt and the Gaussian

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:24, :35` |
| **01 — MaxEnt principle** | Lagrangian, exponential family | `:63-115` |
| | The MaxEnt question | `:70` |
| | Lagrangian | `:78` |
| | The MaxEnt density (exp family) | `:86` |
| | Catalogue — three constraint types | `:94` |
| | Why MaxEnt is useful | `:107` |
| **02 — Gaussian = MaxEnt** | Variance constraint | `:118-194` |
| | **Theorem — Gaussian MaxEnt** | `:126` |
| | Proof — KL inequality (setup) | `:137` |
| | Proof — cross-term | `:144` |
| | Proof — combining | `:156` |
| | Proof variant — Lagrangian | `:167` |
| | Numerical examples | `:176` |
| | **Corollary — Hadamard's inequality** | `:188` |
| **03 — Multivariate Gaussian** | Hadamard, conditioning | `:197-248` |
| | **Theorem — multivariate MaxEnt** | `:205` |
| | Conditioning Gaussians | `:216` |
| | MI for Gaussians | `:225` |
| | Translation invariance revisited | `:236` |
| **04 — EPI** | Entropy power inequality | `:250-338` |
| | Definition — entropy power | `:258` |
| | **Theorem — EPI** | `:271` |
| | Equivalent form | `:282` |
| | Special case — both Gaussian | `:290` |
| | Why "Gaussians are hardest" | `:300` |
| | Application — AWGN converse sketch | `:307` |
| | Application — CLT-style | `:319` |
| Recap | | `:327` |

**Key:** Gaussian MaxEnt `:126`; KL-trick proof `:137-165`; Hadamard `:188`; EPI `:271`.

### Note (`diffentropy2-maxent-gaussian-note.html`)
- Variational calculus rigor
- Gaussian via generalized KL trick
- Hadamard direct proof
- Schur complement detail
- EPI proof sketch (Stam)
- Why EPI ⇒ Gaussian-hardest
- Vector Gaussian channel capacity

---

## diffentropy3-mi-awgn.html — MI and the AWGN Channel

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:24, :35` |
| **01 — Continuous MI** | Definition, properties, examples | `:63-127` |
| | Definition (recap) | `:70` |
| | Discretization bridge for MI | `:82` |
| | Properties — all inherited | `:94` |
| | Example — bivariate Gaussian | `:106` |
| | Example — additive Gaussian noise | `:117` |
| **02 — AWGN channel** | $C = \tfrac{1}{2}\log(1+\mathrm{SNR})$ | `:129-206` |
| | Setup | `:137` |
| | **Theorem — Shannon–Hartley** | `:149` |
| | Proof — achievability | `:159` |
| | Proof — converse | `:170` |
| | Numerical examples | `:182` |
| | Bandwidth-limited form | `:195` |
| **03 — Parallel channels** | Water-filling | `:208-291` |
| | Setup | `:216` |
| | Optimization problem | `:224` |
| | **Theorem — water-filling** | `:231` |
| | Water-filling — picture | `:245` |
| | Example — three sub-channels | `:276` |
| | Application — frequency-selective | `:285` |
| **04 — Connections** | I-MMSE, de Bruijn, diffusion | `:293-381` |
| | MMSE | `:301` |
| | **Theorem — I-MMSE** | `:309` |
| | Sanity check — Gaussian input | `:320` |
| | **Theorem — de Bruijn** | `:331` |
| | Application — diffusion models | `:342` |
| Recap series + Connections | | `:351, :363` |

**Key:** Shannon–Hartley `:149`; water-filling `:231`; I-MMSE `:309`; de Bruijn `:331`.

### Note (`diffentropy3-mi-awgn-note.html`)
- AWGN full coding theorem outline
- Bandwidth-limited continuous-time form
- Water-filling KKT derivation
- I-MMSE proof sketch (Guo–Shamai–Verdú)
- de Bruijn via heat equation
- Diffusion-models information-theoretic loss
