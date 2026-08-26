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

50 slides. Almost no notation: only $x$, $y$, $f$, $g$, and one squared-error line.
Every content slide carries an exhibit — four captured figures, ten inline SVG
diagrams, three tables, three mock UI cards.

| Part | Topic | Line |
|---|---|---|
| Title / This Session | | `:45-79` |
| **01** — A model is a function | six products, one shape | `:81-318` |
| | Six Products, One Machine (card grid) | `:89` |
| | Sorting Photographs (`cifar10.png`) | `:103` |
| | Reading a Review (이동진 / 기생충 mock card) | `:115` |
| | Guessing the Next Word (SVG probability bars) | `:142` |
| | Translating a Sentence | `:166` |
| | Forecasting a Price (`price-chart.png`) | `:186` |
| | Spotting a Defect (SVG conveyor + camera) | `:197` |
| | Scoring an Application (SVG applicant → gauge) | `:231` |
| | Always the Same Shape (SVG function box) | `:265` |
| | **Two Letters for the Afternoon** — $y = f(x)$ | `:286` |
| | What Changes, What Stays | `:300` |
| **02** — Everything becomes numbers | photos, sentences, customers as lists | `:320-412` |
| | A Photo Is a Grid of Numbers (`mnist-vector.png`) | `:328` |
| | How Long Is That List? (784 → 36M table) | `:339` |
| | A Word Is a Point in Space (`word-embeddings.png`) | `:352` |
| | A Customer Is a Row (churn table) | `:363` |
| | Three Shapes of Answer (number / label / distribution) | `:376` |
| | Why This Matters Commercially | `:399` |
| **03** — Where the function comes from | rules out, data in | `:414-706` |
| | The Old Way — Write the Rules (SVG rule tree) | `:422` |
| | What Defines the Digit Zero? | `:449` |
| | Why Rules Run Out | `:463` |
| | Learning, Defined in 1959 (**Arthur Samuel**) | `:484` |
| | The Function We Wish We Had (ideal $f$, dashed box) | `:495` |
| | We Only See Examples — $(x_i, y_i)$ | `:518` |
| | **Training Builds a Look-Alike** — $g \approx f$ | `:532` |
| | Which Look-Alikes Are Allowed? — $g(x)=ax+b$ | `:554` |
| | "Close" Everywhere Is Impossible | `:569` |
| | "Close" on Our Examples | `:582` |
| | Scoring a Single Guess — $(92-85)^2$ | `:595` |
| | Averaging Over Everyone (squared-error loss in words) | `:609` |
| | **The Recipe** — examples · family · loss · search | `:623` |
| | Searching Means Turning Dials (SVG knobs) | `:640` |
| | Somebody Made Those Labels | `:660` |
| | The Model Inherits Your Data (bias table) | `:675` |
| | Two Flavours of Answer (classification vs regression) | `:688` |
| **04** — Reading the recipe | same three lines, every product | `:708-846` |
| | Recipe — Spam Filter | `:716` |
| | Recipe — Demand Forecast | `:731` |
| | Recipe — Defect Detection | `:746` |
| | Four More, Same Three Lines (table) | `:761` |
| | The Recipe Is the Field | `:774` |
| | Three Questions Left Open (→ Decks 2–4) | `:787` |
| | Patterns, Not Reasons | `:800` |
| | Patterns Go Stale | `:813` |
| | The Afternoon Ahead (roadmap) | `:828` |
| Closer — "A function." | | `:848` |

**Key named items:** Arthur Samuel's 1959 definition of learning; CIFAR-10
(Krizhevsky, 2009); squared error as the first loss.

**Deliberate omissions here:** no optimization, no overfitting yet, no gradient
descent — all three are set up as open questions on `:787` and answered in Decks 2–3.

## Status

Deck 1 complete and linted. Decks 2–4 authored in order, one at a time, each
committed to the PR as it lands.
