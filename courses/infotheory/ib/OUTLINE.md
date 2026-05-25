# infotheory/ib/ — Information Bottleneck (2 lectures)

Compression for relevance: the IB problem, self-consistent equations, rate-distortion view, information plane. Connects to MI bounds from `mi/`, rate-distortion from `lossy/`, DPI from `entropy/`. Each deck paired with `-note.html`.

## Files

| Deck | Note | Topic |
|---|---|---|
| `ib1-foundations.html` | `ib1-foundations-note.html` | IB Lagrangian, self-consistent equations, R(D) equivalence, information plane |
| `ib2-deep-learning.html` | *(planned)* | DNN information plane, Shwartz-Ziv hypothesis, Variational IB, the debate |

---

## ib1-foundations.html — The Information Bottleneck

| Section | Slide content | Line |
|---|---|---|
| Title / Contents | | `:19, :30` |
| **01 — Compression for relevance** | IB problem, Markov chain, Lagrangian, DPI | `:58-152` |
| | The central question | `:65` |
| | From source coding to relevance | `:73` |
| | The Markov constraint $Y - X - T$ | `:95` |
| | **Definition (IB Lagrangian)** | `:109` |
| | Two extremes of $\beta$ | `:122` |
| | DPI constrains the problem | `:141` |
| **02 — Self-consistent equations** | Optimal encoder, variational proof | `:153-239` |
| | Optimization setup | `:160` |
| | Derived quantities $p(t)$, $p(y\|t)$ | `:169` |
| | **Theorem (IB Optimal Encoder, Tishby et al.)** | `:179` |
| | Proof — variational derivative | `:189` |
| | Proof — isolate $p(t\|x)$ | `:198` |
| | Proof — conclusion | `:206` |
| | Self-consistency (three coupled equations) | `:214` |
| | Reading the encoder (Gibbs interpretation) | `:226` |
| **03 — IB as rate-distortion** | Log-loss distortion, R(D) equivalence | `:240-304` |
| | Recall — rate-distortion | `:247` |
| | **Lemma (Relevance Decomposition)** | `:258` |
| | Proof of relevance decomposition | `:269` |
| | **Theorem (IB-RD Equivalence)** | `:281` |
| | Why log-loss is natural | `:293` |
| **04 — The information plane** | DPI bounds, IB curve, phase transitions, DNN layers | `:305-420` |
| | **Definition (Information Plane)** | `:312` |
| | DPI constrains the region | `:323` |
| | The IB curve (optimal frontier) | `:335` |
| | Phase transitions in $\beta$ | `:348` |
| | DNN layers in the plane | `:361` |
| | Forward pointer to Lecture 2 | `:383` |
| | The IT perspective | `:399` |

**Key formulas:** IB Lagrangian `:112`; optimal encoder (Gibbs form) `:182`; relevance decomposition `:261`; IB-RD equivalence `:284`; IB curve `:338`; DPI chain for DNN `:370`.

### Note (`ib1-foundations-note.html`)
- Why IB, not just rate-distortion `:29`
- Sufficiency and minimal sufficient statistics `:35`
- Full variational derivative for $I(X;T)$ and $I(T;Y)$ `:51`
- KL decomposition step `:76`
- Blahut-Arimoto iteration for IB `:87`
- Relevance decomposition proof detail `:100`
- Properties of log-loss distortion `:115`
- Properties of the IB curve `:125`
- Phase transitions and critical $\beta_1$ `:135`
- DPI monotonicity caveat (deterministic layers, continuous variables) `:149`
- Connection to Lecture 2 `:157`

---

## ib2-deep-learning.html — IB and Deep Learning

| Section | Slide content | Line |
|---|---|---|
| Title / Contents | | `:19, :30` |
| **01 — DNN as Markov chain** | IT motivation, layer representations, DPI, information plane | `:58-121` |
| | Why IT for deep learning? | `:65` |
| | Layer representations (Markov chain) | `:77` |
| | DPI for every layer | `:97` |
| | Layers in the information plane | `:108` |
| **02 — Information plane hypothesis** | Fitting-then-compressing | `:122-178` |
| | **Conjecture (Shwartz-Ziv and Tishby, 2017)** | `:129` |
| | The fitting phase | `:141` |
| | The compression phase | `:153` |
| | Why compression might help (generalization bound) | `:165` |
| **03 — Variational Information Bottleneck** | Tractable IB for neural networks | `:179-286` |
| | The tractability problem | `:186` |
| | **Lemma (Rate Upper Bound)** | `:197` |
| | Lower bound on $I(T;Y)$ (BA recall) | `:210` |
| | **Definition (VIB, Alemi et al., 2017)** | `:222` |
| | VIB architecture (Gaussian encoder) | `:233` |
| | Connection to the VAE | `:240` |
| | What $\beta$ controls | `:270` |
| **04 — The debate** | What survives scrutiny | `:287-393` |
| | The estimation problem (binning) | `:294` |
| | Activation function dependence (Saxe et al.) | `:303` |
| | What does not survive | `:315` |
| | What survives | `:325` |
| | IT implications for deep learning | `:336` |
| | The IB arc (five-tool connection table) | `:347` |

**Key formulas:** DPI chain `:100`; Shwartz-Ziv conjecture `:132`; rate upper bound `:200`; BA lower bound `:213`; VIB objective `:225`; VIB = VAE with classifier decoder `:241`.

### Note (`ib2-deep-learning-note.html`)
- DPI for deterministic functions `:25`
- ReLU subtlety `:39`
- Original Shwartz-Ziv experimental setup `:50`
- SGD noise argument `:58`
- Xu-Raginsky generalization bound `:68`
- Proof of rate upper bound `:80`
- Connection to Barber-Agakov `:100`
- VIB vs $\beta$-VAE `:112`
- Saxe et al. detailed experiments `:125`
- Binning critique `:140`
- Geometric compression `:150`
- Current consensus `:160`
