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
| `sangnam3-training-and-classification.html` | Gradient descent as downhill-in-fog · threshold lines · soft thresholding → **logistic regression is linear regression plus a squash** · deep learning |
| sangnam4-frontier-and-risks *(planned)* | Diffusion · text-to-image/video · LLMs · **RLVR** · AI in mathematics · the incident column |
| `figs/` | Figures captured from the source PDF and from cited papers/press |

Captured so far: `cifar10.png` (CIFAR-10 sample grid), `mnist-vector.png` (digit as
pixel matrix), `word-embeddings.png` (words as points), `price-chart.png` (BTC/KRW
candlesticks with moving averages), and fourteen plots lifted from the source PDF
for Deck 2 — `f-hw-scatter`, `f-hw-fit`, `f-curve-linear`, `f-curve-quad`,
`f-D-linear`, `f-DD-linear`, `f-D-poly7`, `f-DD-poly7`, `f-more-data`,
`f-triptych`, `f-val-poly6`, `f-val-quad`, `f-aug-dog`, `f-aug-digit`.

Added for Deck 3, again cropped from the source PDF: `f-gd-small-lr`,
`f-gd-large-lr`, `f-gd-contour`, `f-gd-init`, `f-landscape` (losslandscape.com),
`f-clf-boundary`, `f-clf-many`, `f-clf-none`, `f-soft-guess`, `f-prec-recall`
(Wikipedia), `f-roc` (Wikipedia), `f-overkill`, `f-superres` (SRGAN),
`f-detection` (Faster R-CNN). The sigmoid on `:557` is inline SVG — the source
page could not be cropped without title bleed.

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

## sangnam3-training-and-classification.html

58 slides. Tracks source pp. 58–132: gradient descent (pp. 59–77), classification
and the decision line (pp. 84–99), soft thresholding and logistic regression
(pp. 103–112), precision/recall/ROC (pp. 118–124), and the deep-learning bridge
(pp. 125–132). Notation stays at a weighted sum, one squared-error line, and one
sigmoid definition — no derivatives, no updates rule, no matrices.

Fourteen exhibits are captured figures; the remaining twenty-one are inline SVG.

| Part | Topic | Line |
|---|---|---|
| Title / This Session | | `:48-87` |
| **01** — Downhill in the fog | searching a space you cannot see | `:88-320` |
| | Two Dials, One Score (squared-error loss, deck-2 callback) | `:96` |
| | The High-School Answer (SVG parabola, slope $=0$) | `:109` |
| | No Formula for a Billion Dials (2 / a million / billions) | `:128` |
| | Standing on a Hillside in Fog (`f-landscape`) | `:143` |
| | All You Can Feel Is the Slope (SVG hiker in fog) | `:154` |
| | **Look, Step, Repeat** — names *gradient descent* | `:176` |
| | Steps Too Small (`f-gd-small-lr`) | `:193` |
| | Steps Too Large (`f-gd-large-lr`) | `:204` |
| | The Step Size Is a Choice — names *learning rate* | `:215` |
| | Two Dials at Once (`f-gd-contour`, two step sizes) | `:234` |
| | Where You Start Matters (`f-gd-init`, two valleys) | `:245` |
| | The Ground Is Not a Bowl (SVG plateau / local / deeper) | `:258` |
| | Too Much Data for One Step — names *stochastic gradient descent* | `:278` |
| | Downhill Search in Five Lines | `:306` |
| **02** — Drawing the line | when the answer is a label | `:321-492` |
| | Number or Label? (regression vs classification) | `:329` |
| | Two Clouds, One Line (`f-clf-boundary`) | `:350` |
| | **Still a Weighted Sum** — $s(x)=w_1x_1+\cdots+w_dx_d+b$ | `:361` |
| | Counting Mistakes (SVG, 2 on the wrong side) | `:377` |
| | A Score With No Slope (SVG staircase) | `:405` |
| | Many Lines Work (`f-clf-many`) | `:431` |
| | Prefer the Widest Gap (SVG corridor, **Cortes and Vapnik, 1995**) | `:442` |
| | Sometimes No Line Works (`f-clf-none`) | `:468` |
| | Then Allow a Few Mistakes (penalty per violation) | `:479` |
| **03** — Soft answers | a line, plus a squash | `:493-725` |
| | Hard Answer, Soft Answer (churn verdict vs churn risk) | `:501` |
| | Probably Red, Certainly Blue (`f-soft-guess`) | `:522` |
| | Distance Is Confidence (SVG, distance from the line) | `:532` |
| | Squash It Into a Probability (SVG sigmoid) | `:556` |
| | **Logistic Regression** — $g(x)=\sigma(w_1x_1+\cdots+b)$, $\sigma(s)=1/(1+e^{-s})$ | `:580` |
| | **A Line Plus a Squash** (SVG chain: columns → weighted sum → squash → 0.72) | `:596` |
| | Scoring a Probability (penalty table) | `:624` |
| | Confident and Wrong Is Expensive (SVG $-\log p$, names *cross-entropy*) | `:639` |
| | Now the Score Has a Slope (why classifiers output probabilities) | `:661` |
| | More Than Two Labels (`cifar10.png`, Krizhevsky 2009) | `:675` |
| | One Score per Label, Then Normalise (SVG bars, names *softmax*) | `:686` |
| **04** — Reading the errors | which mistake is cheaper? | `:726-838` |
| | Where to Put the Threshold (SVG slider) | `:734` |
| | Two Ways to Be Wrong (false alarm / miss) | `:754` |
| | **Precision and Recall** (`f-prec-recall`) | `:775` |
| | Which Mistake Is Cheaper? (screening / spam / fraud / loans) | `:793` |
| | Sweep the Threshold (`f-roc`, area under the curve) | `:806` |
| | **Accuracy Is a Trap** — 99.9% by always saying "fine" | `:826` |
| **05** — Stacking the boxes | where deep learning comes in | `:839-1058` |
| | Straight Lines Run Out (SVG ring inside a ring) | `:847` |
| | **Stack the Boxes** (SVG layered network) | `:872` |
| | Same Four Lines (only the family changed) | `:901` |
| | Any Shape, In Principle (**Cybenko, 1989; Hornik, 1991**) | `:918` |
| | Depth Buys Reuse (SVG pixels → edges → parts → car) | `:936` |
| | Sharper Pictures (`f-superres`, **Ledig et al., CVPR 2017**) | `:966` |
| | Finding Things in a Photo (`f-detection`, **Ren et al., NeurIPS 2015**) | `:981` |
| | Filling In a Blank (SVG masked sentence — language-model training) | `:1000` |
| | You Might Not Need It (`f-overkill`) | `:1027` |
| | Today in Five Lines | `:1046` |
| Closer — "Take the slope. Then squash it." | | `:1059` |

**Key named items:** gradient descent; learning rate; stochastic gradient descent;
local minima; the zero-one loss and its missing slope; support vector machine
(Cortes and Vapnik, 1995); sigmoid; logistic regression; cross-entropy; softmax;
precision, recall and ROC/AUC; universal approximation (Cybenko, 1989; Hornik,
1991); SRGAN (Ledig et al., CVPR 2017); Faster R-CNN (Ren et al., NeurIPS 2015).

**Deliberate omissions here:** no gradient formulas or update rule (Albert's brief:
high-level only), no momentum/RMSProp/ADAM/LR-schedule block (source pp. 78–83), no
perceptron/LP/duality/hinge/kernel chain (source pp. 90–102, reduced to `:442` and
`:479`), and no KL-divergence formalism behind cross-entropy — replaced by the
penalty table on `:624` and the curve on `:639`.

## Status

Decks 1–3 complete, linted, and screenshot-audited. Deck 4 is next; decks are
authored one at a time, each committed as it lands.
