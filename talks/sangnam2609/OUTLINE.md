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
| `sangnam2-linear-regression-and-overfitting.html` | Loss and training on a straight line · overfitting · model size · amount of data · **scaling laws** |
| sangnam3-training-and-classification *(planned)* | Gradient descent as downhill-in-fog · threshold lines · soft thresholding → **logistic regression is linear regression plus a squash** · deep learning |
| sangnam4-frontier-and-risks *(planned)* | Diffusion · text-to-image/video · LLMs · **RLVR** · AI in mathematics · the incident column |
| `figs/` | Figures captured from the source PDF and from cited papers/press |

Captured so far: `cifar10.png` (CIFAR-10 sample grid), `mnist-vector.png` (digit as
pixel matrix), `word-embeddings.png` (words as points), `price-chart.png` (BTC/KRW
candlesticks with moving averages), and fourteen plots lifted from the source PDF
for Deck 2 — `f-hw-scatter`, `f-hw-fit`, `f-curve-linear`, `f-curve-quad`,
`f-D-linear`, `f-DD-linear`, `f-D-poly7`, `f-DD-poly7`, `f-more-data`,
`f-triptych`, `f-val-poly6`, `f-val-quad`, `f-aug-dog`, `f-aug-digit`.

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

## sangnam2-linear-regression-and-overfitting.html

52 slides. Tracks source pp. 26–57, minus the closed-form solve (pp. 29–32, 35–39),
cross-validation (p. 55) and regularization (p. 56); section 04 is new material,
added on Albert's brief ("model size, amount of data, possibly scaling laws").
Notation stays at $ax + b$, one squared-error line, and a weighted sum — no
derivatives, no matrices, no normal equations.

Fourteen of the twenty-one exhibits are Albert's own matplotlib plots, cropped out
of the source PDF; the rest are inline SVG.

| Part | Topic | Line |
|---|---|---|
| Title / This Session | | `:48-83` |
| **01** — Fitting a line | one input, two dials | `:84-317` |
| | The Recipe, Unchanged (deck-1 callback) | `:92` |
| | Heights and Weights (`f-hw-scatter`) | `:108` |
| | The Job: Height In, Weight Out (SVG function box) | `:119` |
| | **A Family of Straight Lines** — $\mathcal{G}=\{g_{a,b}(x)=ax+b\}$ | `:146` |
| | Which of These Is Best? (SVG, three candidates) | `:168` |
| | Measure Every Miss (SVG residuals) | `:192` |
| | Why Square the Gaps? | `:221` |
| | **One Number for the Whole Dataset** — mean squared error | `:235` |
| | Training Is Turning the Dials (SVG bowl) | `:248` |
| | The Winning Line (`f-hw-fit`) | `:271` |
| | What the Dials Tell You (slope as business quantity) | `:282` |
| | Linear Regression, Complete (four-line recipe) | `:301` |
| **02** — More columns, more shapes | many inputs, curved columns | `:318-439` |
| | Two Inputs Instead of One (SVG plane) | `:326` |
| | Many Inputs, Same Shape — $g(x)=w_1x_1+\cdots+w_dx_d+b$ | `:350` |
| | A Table You Already Have (churn table) | `:364` |
| | A Straight Line Cannot Bend (`f-curve-linear`) | `:379` |
| | Give It a Curved Column (`f-curve-quad`) | `:390` |
| | **Still a Weighted Sum** — $z_1=x$, $z_2=x^2$ | `:401` |
| | You Can Always Add Columns (powers / products / transforms) | `:416` |
| **03** — Overfitting | the one failure mode to recognise | `:440-724` |
| | Ten Points, One Line (`f-D-linear`) | `:448` |
| | Nudge One Point (`f-DD-linear`) | `:459` |
| | A Curve Through Every Point (`f-D-poly7`) | `:470` |
| | Nudge One Point Again (`f-DD-poly7`) | `:481` |
| | **Memorising Is Not Learning** | `:492` |
| | Three Fits, Same Data (`f-triptych`) | `:511` |
| | Two Ways to Be Wrong (bias / variance, in words) | `:522` |
| | More Data Tames It (`f-more-data`) | `:541` |
| | You Cannot Just Look (2 columns vs 2,000) | `:552` |
| | **Hold Some Data Back** (SVG 80/20 split) | `:576` |
| | Perfect on Train, Lost Elsewhere (`f-val-poly6`) | `:597` |
| | When the Two Scores Agree (`f-val-quad`) | `:608` |
| | Train, Validation, Test | `:619` |
| | Prefer the Simpler Story (**Occam's razor**, SVG 2 vs 40 dials) | `:642` |
| | **Reading the Two Numbers** (diagnosis table) | `:671` |
| | If You Are Overfitting (more data · simpler family · augment · generate) | `:686` |
| | A Shifted Dog Is Still a Dog (`f-aug-dog`) | `:698` |
| | But It Depends on Your Data (`f-aug-digit`, mirrored '2') | `:712` |
| **04** — Model, data, compute | new material, not in the source | `:725-890` |
| | The Classic Picture (SVG U-curve) | `:733` |
| | Then the Curve Broke (SVG **double descent**) | `:756` |
| | Three Dials | `:776` |
| | **Scaling Laws** (SVG straight line on a log plot) | `:799` |
| | Balance the Dials (**Chinchilla**, Hoffmann et al. 2022) | `:820` |
| | Compute Is Buyable, Data Is Not | `:840` |
| | What This Means for You | `:854` |
| | Today in Five Lines | `:878` |
| Closer — "Fit the pattern, not the noise." | | `:891` |

**Key named items:** mean squared error; bias-variance trade-off; train/validation/test
split; Occam's razor; double descent; scaling laws; Hoffmann et al., "Training
Compute-Optimal Large Language Models" (2022).

**Deliberate omissions here:** no closed-form least-squares solve, no
cross-validation, no regularization (all three cut on Albert's instruction).
Gradient descent is named only as "turning the dials" — the mechanism lands in Deck 3.

## Status

Decks 1 and 2 complete, linted, and screenshot-audited. Decks 3–4 authored in
order, one at a time, each committed as it lands.
