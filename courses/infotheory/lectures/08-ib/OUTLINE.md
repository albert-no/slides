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
| **01 — Compression for relevance** | IB problem, Markov chain, Lagrangian, DPI | `:58-176` |
| | The central question | `:66` |
| | From source coding to relevance | `:95` |
| | The Markov constraint $Y - X - T$ | `:114` |
| | **Definition (IB Lagrangian)** | `:128` |
| | Two extremes of $\beta$ | `:141` |
| | DPI constrains the problem | `:165` |
| **02 — Self-consistent equations** | Optimal encoder, variational proof (full derivation) | `:179-269` |
| | Optimization setup | `:187` |
| | Derived quantities $p(t)$, $p(y\|t)$ | `:196` |
| | **Theorem (IB Optimal Encoder, Tishby et al.)** | `:206` |
| | Proof — variational derivative (Lagrangian + both partials + stationarity eq.) | `:216` |
| | Proof — isolate $p(t\|x)$ (log-isolate, add/subtract $\log p(y\|x)$, KL split) | `:228` |
| | Proof — conclusion (back-substitution, fold constant, exponentiate) | `:238` |
| | Self-consistency (three coupled equations) | `:248` |
| | Reading the encoder (Gibbs interpretation) | `:260` |
| **03 — IB as rate-distortion** | Log-loss distortion, R(D) equivalence (full proofs) | `:272-337` |
| | Recall — rate-distortion | `:281` |
| | **Lemma (Relevance Decomposition)** | `:291` |
| | Proof of relevance decomposition (cross-entropy split, tower property, full) | `:302` |
| | **Theorem (IB-RD Equivalence)** | `:318` |
| | Proof — explicit substitution of Relevance Decomposition | `:320-326` |
| | Why log-loss is natural | `:330` |
| **04 — The information plane** | DPI bounds, IB curve, phase transitions, DNN layers | `:340-475` |
| | **Definition (Information Plane)** | `:349` |
| | DPI constrains the region | `:377` |
| | The IB curve (optimal frontier) | `:391` |
| | Phase transitions in $\beta$ | `:404` |
| | DNN layers in the plane | `:417` |
| | Toward deep learning | `:439` |
| | The IT perspective | `:455` |

**Key formulas:** IB Lagrangian `:132`; optimal encoder (Gibbs form) `:210`; variational-derivative stationarity `:224`; KL-split identity `:234`; relevance decomposition `:295`; IB-RD equivalence `:322`; IB curve `:393`; DPI chain for DNN `:433`.

### Note (`ib1-foundations-note.html`)
- Why IB, not just rate-distortion `:29`
- Sufficiency and minimal sufficient statistics `:35`
- Full variational derivative for $I(X;T)$ and $I(T;Y)$ (term-by-term telescoping, more granular than the deck's compressed result) `:50`
- KL decomposition step — now a pointer to the deck proof (`ib1-foundations.html:231-234`), no longer re-derived `:65`
- Blahut-Arimoto iteration for IB `:68`
- Relevance decomposition proof detail — now a pointer to the deck proof (`ib1-foundations.html:302-314`), no longer re-derived `:85`
- Properties of log-loss distortion `:88`
- Properties of the IB curve `:101`
- Phase transitions and critical $\beta_1$ `:109`
- DPI monotonicity caveat (deterministic layers, continuous variables) `:115`
- Connection to Lecture 2 `:120`

---

## ib2-deep-learning.html — IB and Deep Learning

| Section | Slide content | Line |
|---|---|---|
| Title / Contents | | `:22, :34` |
| **01 — DNN as Markov chain** | IT motivation, layer representations, DPI, information plane | `:61-112` |
| | Why IT for deep learning? | `:69` |
| | Layer representations (Markov chain) — **`fig/dnn.png`** | `:81` |
| | DPI for every layer | `:91` |
| | Layers in the information plane | `:102` |
| **02 — Information plane hypothesis** | Fitting-then-compressing, generalization | `:115-266` |
| | **Conjecture (Shwartz-Ziv and Tishby, 2017)** | `:125` |
| | The fitting phase | `:135` |
| | The compression phase | `:146` |
| | Why SGD noise compresses — drift vs diffusion, ⚠ ReLU caveat (Saxe) | `:158` |
| | Information plane in training — **`information_plane.png`** | `:178` |
| | Watch: optimization in the plane — **clickable YouTube thumbnail (new tab)** | `:187` |
| | Why compression might help (intuition) | `:207` |
| | **Theorem (MI Generalization Bound, Xu–Raginsky, 2017)** | `:222` |
| | Reading the bound — $I(S;W)$, memorize vs forget | `:230` |
| | Two bottlenecks — $I(X;T)$ vs $I(S;W)$ (Achille–Soatto) | `:248` |
| **03 — Variational Information Bottleneck** | Tractable IB for neural networks (full proof of rate bound) | `:268-374` |
| | The tractability problem | `:277` |
| | **Lemma (Rate Upper Bound)** | `:289` |
| | Proof — log-ratio split, underbrace-labeled $I(X;T)$ identification, tower-property collapse | `:294-297` |
| | Lower bound on $I(T;Y)$ (BA recall) | `:302` |
| | **Definition (VIB, Alemi et al., 2017)** | `:315` |
| | VIB architecture (Gaussian encoder) | `:324` |
| | Connection to the VAE | `:332` |
| | What $\beta$ controls | `:362` |
| **04 — The debate** | What survives scrutiny | `:377-485` |
| | The estimation problem (binning) | `:386` |
| | Activation function dependence (Saxe et al.) | `:395` |
| | What does not survive | `:408` |
| | What survives | `:418` |
| | IT implications for deep learning | `:429` |
| | The IB arc (five-tool connection table) | `:440` |
| | Summary | `:478` |

**Figures:** `fig/dnn.png` (encoder–decoder Markov chain) and `information_plane.png` (3-panel training trajectory) + clickable YouTube thumbnail (opens in new tab) — all from Shwartz-Ziv and Tishby, arXiv:1703.00810.

**Key formulas:** DPI chain `:96`; Shwartz-Ziv conjecture `:126`; MI generalization bound (Xu–Raginsky) `:224`; rate upper bound `:291`; rate-bound proof (full) `:295-297`; BA lower bound `:307`; VIB objective `:317`; VIB = VAE with classifier decoder `:332`.

### Note (`ib2-deep-learning-note.html`)
- DPI for deterministic functions `:25`
- ReLU subtlety `:39`
- Original Shwartz-Ziv experimental setup `:50`
- SGD noise argument `:58`
- Xu-Raginsky generalization bound `:68`
- Rate upper bound — proof now on the deck slide (`ib2-deep-learning.html:294-297`); note adds why the bound is loose, the slack term's meaning, and the tightness condition `:68`
- Why $r(t) = \mathcal{N}(0,I)$ (closed-form KL) `:73`
- Connection to Barber-Agakov `:77`
- VIB vs $\beta$-VAE `:82`
- Reparameterization trick `:90`
- Saxe et al. detailed experiments `:99`
- Binning critique `:107`
- Geometric compression `:111`
- Current consensus `:115`
