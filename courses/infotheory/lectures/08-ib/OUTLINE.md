# infotheory/lectures/08-ib/ — Information Bottleneck (2 lectures)

Compression for relevance: the IB problem, self-consistent equations, rate-distortion view, information plane. Connects to MI bounds from `mi/`, rate-distortion from `lossy/`, DPI from `entropy/`. Each deck paired with `-note.html`.

## Files

| Deck | Note | Topic |
|---|---|---|
| `ib1-foundations.html` | `ib1-foundations-note.html` | IB Lagrangian, self-consistent equations, R(D) equivalence, information plane |
| `ib2-deep-learning.html` | `ib2-deep-learning-note.html` | DNN information plane, Shwartz-Ziv hypothesis, Variational IB, the debate |

---

## ib1-foundations.html — The Information Bottleneck

| Section | Slide content | Line |
|---|---|---|
| Title / Contents | | `:19, :31` |
| **01 — Compression for relevance** | IB problem, Markov chain, Lagrangian, DPI | `:58-178` |
| | The central question | `:66` |
| | From source coding to relevance | `:95` |
| | The Markov constraint $Y - X - T$ | `:114` |
| | **Definition (IB Lagrangian)** | `:128` |
| | Two extremes of $\beta$ | `:141` |
| | DPI constrains the problem | `:165` |
| **02 — Self-consistent equations** | Optimal encoder, variational proof | `:179-265` |
| | Optimization setup | `:187` |
| | Derived quantities $p(t)$, $p(y\|t)$ | `:196` |
| | **Theorem (IB Optimal Encoder, Tishby et al.)** | `:206` |
| | Proof — variational derivative | `:216` |
| | Proof — isolate $p(t\|x)$ | `:225` |
| | Proof — conclusion | `:233` |
| | Self-consistency (three coupled equations) | `:241` |
| | Reading the encoder (Gibbs interpretation) | `:253` |
| **03 — IB as rate-distortion** | Log-loss distortion, R(D) equivalence | `:266-327` |
| | Recall — rate-distortion | `:274` |
| | **Lemma (Relevance Decomposition)** | `:284` |
| | Proof of relevance decomposition | `:295` |
| | **Theorem (IB-RD Equivalence)** | `:307` |
| | Why log-loss is natural | `:317` |
| **04 — The information plane** | DPI bounds, IB curve, phase transitions, DNN layers | `:328-464` |
| | **Definition (Information Plane)** | `:336` |
| | DPI constrains the region | `:364` |
| | The IB curve (optimal frontier) | `:378` |
| | Phase transitions in $\beta$ | `:391` |
| | DNN layers in the plane | `:404` |
| | Forward pointer to Lecture 2 | `:426` |
| | The IT perspective | `:442` |

**Key formulas:** IB Lagrangian `:132`; optimal encoder (Gibbs form) `:210`; relevance decomposition `:288`; IB-RD equivalence `:311`; IB curve `:380`; DPI chain for DNN `:420`.

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
| Title / Contents | | `:19, :34` |
| **01 — DNN as Markov chain** | IT motivation, layer representations, DPI, information plane | `:60-114` |
| | Why IT for deep learning? | `:69` |
| | Layer representations (Markov chain) — **`fig/dnn.png`** | `:81` |
| | DPI for every layer | `:91` |
| | Layers in the information plane | `:102` |
| **02 — Information plane hypothesis** | Fitting-then-compressing | `:114-191` |
| | **Conjecture (Shwartz-Ziv and Tishby, 2017)** | `:123` |
| | The fitting phase | `:135` |
| | The compression phase | `:146` |
| | Information plane in training — **`information_plane.png`** | `:157` |
| | Watch: optimization in the plane — **embedded video** | `:166` |
| | Why compression might help (generalization bound) | `:178` |
| **03 — Variational Information Bottleneck** | Tractable IB for neural networks | `:191-297` |
| | The tractability problem | `:200` |
| | **Lemma (Rate Upper Bound)** | `:210` |
| | Lower bound on $I(T;Y)$ (BA recall) | `:222` |
| | **Definition (VIB, Alemi et al., 2017)** | `:233` |
| | VIB architecture (Gaussian encoder) | `:244` |
| | Connection to the VAE | `:252` |
| | What $\beta$ controls | `:282` |
| **04 — The debate** | What survives scrutiny | `:297-407` |
| | The estimation problem (binning) | `:306` |
| | Activation function dependence (Saxe et al.) | `:315` |
| | What does not survive | `:328` |
| | What survives | `:338` |
| | IT implications for deep learning | `:349` |
| | The IB arc (five-tool connection table) | `:360` |
| | Summary | `:398` |

**Figures:** `fig/dnn.png` (encoder–decoder Markov chain) and `information_plane.png` (3-panel training trajectory) + embedded YouTube — all from Shwartz-Ziv and Tishby, arXiv:1703.00810.

**Key formulas:** DPI chain `:96`; Shwartz-Ziv conjecture `:123`; rate upper bound `:214`; BA lower bound `:227`; VIB objective `:237`; VIB = VAE with classifier decoder `:252`.

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
