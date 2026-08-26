# sangnam2609/ — Sangnam AI Leader, Week 3: introduction to machine learning (Sep 2026)

3–4 hour introductory talk for the **Sangnam Institute of Management "AI Leader"**
executive program. Audience is business executives; examples are business-flavored,
technical level is **freshman undergraduate** — no calculus, no linear algebra, no
derivations. High-level overview: concepts, pictures, and stories.

Rewritten (not ported) from Albert's source deck (상남경영원 AI Leader 26-1, week 3)
(141 pages). Deliberately dropped from the source: normal equations and the
closed-form least-squares solve, cross-validation, regularization, the
momentum/RMSProp/ADAM/LR-schedule block, and the perceptron/LP/margin/SVM/hinge/kernel
chain (reduced to a single "widest gap" intuition slide in Deck 3).

Roughly one hour is reserved for the closing frontier-and-risks block: recent
advances (diffusion, RLVR, AI-assisted mathematics) paired with recent failures
(agent containment breaches, scheming/sabotage evaluations).

Four decks, one per ~50-minute block. Merge later if desired.

## Files

| Deck | Topic |
|---|---|
| `sangnam1-what-is-learning.html` | A model is a function · everything becomes numbers · rules out, data in · the four-line recipe |
| sangnam2-linear-regression-and-overfitting *(planned)* | Loss and training on a straight line · overfitting · model size · amount of data · **scaling laws** |
| sangnam3-training-and-classification *(planned)* | Gradient descent as downhill-in-fog · threshold lines · soft thresholding → **logistic regression is linear regression plus a squash** · deep learning |
| sangnam4-frontier-and-risks *(planned)* | Diffusion · text-to-image/video · LLMs · **RLVR** · AI in mathematics · the incident column |
| `figs/` | Figures captured from the source PDF and from cited papers/press |

Captured so far: `cifar10.png` (CIFAR-10 sample grid), `mnist-vector.png` (digit as
pixel matrix), `word-embeddings.png` (words as points), `price-chart.png` (BTC/KRW
candlesticks with moving averages).

---

## sangnam1-what-is-learning.html

52 slides. Almost no notation: only $x$, $y$, $f$, $g$, and one squared-error line.
Every content slide carries an exhibit — four captured figures, twelve inline SVG
diagrams, three tables, three mock UI cards.

Tracks source pp. 1–25 beat for beat: the six products (pp. 2–7), the function box
(p. 8), the three ingredients (p. 9), the $x$/$y$ second pass (pp. 11–17),
rule-based versus data-based (p. 18), Samuel (p. 19), expert $f$ versus model $g$
(p. 20), the setup (p. 21), classification versus regression (p. 22), "approximate
well?" (pp. 23–24), and the recipe (p. 25).

| Part | Topic | Line |
|---|---|---|
| Title / This Session | | `:44-79` |
| **01** — A model is a function | six products, one shape | `:80-318` |
| | Six Products, One Machine (card grid) | `:88` |
| | Sorting Photographs (`cifar10.png`) | `:102` |
| | Reading a Review (이동진 / 기생충 mock card) | `:114` |
| | Guessing the Next Word (SVG probability bars) | `:141` |
| | Translating a Sentence | `:165` |
| | Forecasting a Price (`price-chart.png`) | `:185` |
| | Spotting a Defect (SVG conveyor + camera) | `:196` |
| | Scoring an Application (SVG applicant → gauge) | `:230` |
| | Always the Same Shape (SVG function box) | `:264` |
| | **Two Letters for the Afternoon** — $y = f(x)$ | `:285` |
| | What Changes, What Stays | `:299` |
| **02** — Everything becomes numbers | photos, sentences, customers as lists | `:319-444` |
| | A Photo Is a Grid of Numbers (`mnist-vector.png`) | `:327` |
| | How Long Is That List? (784 → 36M table) | `:338` |
| | A Word Is a Point in Space (`word-embeddings.png`) | `:351` |
| | A Customer Is a Row (churn table) | `:362` |
| | **Naming the Parts, Six Times** — $x$/$y$ per product | `:375` |
| | Three Shapes of Answer (number / label / distribution) | `:407` |
| | Why This Matters Commercially | `:430` |
| **03** — Where the function comes from | rules out, data in | `:445-776` |
| | The Old Way — Write the Rules (SVG rule tree) | `:453` |
| | What Defines the Digit Zero? | `:480` |
| | Why Rules Run Out | `:494` |
| | Learning, Defined in 1959 (**Arthur Samuel**) | `:515` |
| | **Three Words: Function, Data, Loss** (SVG chain) | `:526` |
| | The Function We Wish We Had (ideal $f$, dashed box) | `:552` |
| | We Only See Examples — $(x_i, y_i)$ | `:575` |
| | **Training Builds a Look-Alike** — expert $f$ ≈ model $g$ | `:589` |
| | Which Look-Alikes Are Allowed? — $g(x)=ax+b$ | `:623` |
| | "Close" Everywhere Is Impossible | `:638` |
| | "Close" on Our Examples | `:651` |
| | Scoring a Single Guess — $(92-85)^2$ | `:664` |
| | Averaging Over Everyone (squared-error loss in words) | `:678` |
| | **The Recipe** — examples · family · loss · search | `:692` |
| | Searching Means Turning Dials (SVG knobs) | `:709` |
| | Somebody Made Those Labels | `:729` |
| | The Model Inherits Your Data (bias table) | `:744` |
| | Two Flavours of Answer (classification vs regression) | `:757` |
| **04** — Reading the recipe | same three lines, every product | `:777-916` |
| | Recipe — Spam Filter | `:785` |
| | Recipe — Demand Forecast | `:800` |
| | Recipe — Defect Detection | `:815` |
| | Four More, Same Three Lines (table) | `:830` |
| | The Recipe Is the Field | `:843` |
| | Three Questions Left Open (→ Decks 2–4) | `:856` |
| | Patterns, Not Reasons | `:869` |
| | Patterns Go Stale | `:882` |
| | The Afternoon Ahead (roadmap) | `:897` |
| Closer — "A function." | | `:917` |

**Key named items:** Arthur Samuel's 1959 definition of learning; CIFAR-10
(Krizhevsky, 2009); squared error as the first loss.

**Deliberate omissions here:** no optimization, no overfitting yet, no gradient
descent — all three are set up as open questions on `:856` and answered in Decks 2–3.

## Status

Deck 1 complete and linted. Decks 2–4 authored in order, one at a time, each
committed to the PR as it lands.
