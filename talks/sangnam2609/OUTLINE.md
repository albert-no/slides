# sangnam2609/ — Sangnam AI Leader (Sep 2026)

Three-part talk over **two days**, for the Sangnam Institute of Management
"AI Leader" executive program. Audience is business executives; technical level is
**freshman undergraduate** — no calculus, no linear algebra, no derivations.
Concepts, pictures, and stories.

| Slot | Deck | Slides |
|---|---|---|
| **Day 1, part 1** (1 h) | `sangnam1-ai-today.html` | 64 |
| **Day 1, part 2** (1 h) | `sangnam2-what-is-learning.html` | 53 |
| **Day 2** (1.5 h) | `sangnam3-linear-regression-and-overfitting.html` | 32 |
| | `sangnam4-training-and-classification.html` | 37 |
| | `sangnam5-frontier.html` | 28 |

Day 1 is story then foundations; Day 2 is the machinery, and its three decks run
back to back with no repeated setup. Parts 3–5 were trimmed from 167 slides to 97
to fit 90 minutes — the cut list is at the bottom of this file, and every cut slide
is recoverable from git history (`git log --oneline talks/sangnam2609/`).

Parts 2–5 were rewritten (not ported) from Albert's source deck
(상남경영원 AI Leader 26-1, 141 pages). Deliberately absent from the whole
series: normal equations and the closed-form least-squares solve, cross-validation,
regularization, the momentum/RMSProp/ADAM/LR-schedule block, and the
perceptron/LP/margin/SVM/hinge/kernel chain.

## Where a topic lives

| Topic | Deck |
|---|---|
| What AI can do today, and what it costs | Part 1 |
| AI in mathematics (conjectures, Erdős problems, IMO) | Part 1 `:447-696` |
| Copyright and the lawsuits | Part 1 `:801-921` |
| The July 2026 Hugging Face / OpenAI incident | Part 1 `:922-1138` |
| Regulation, power, and what to ask on Monday | Part 1 `:1139-1231` |
| $y = f(x)$, features, labels, the four-line recipe | Part 2 |
| Loss, fitting, overfitting, validation | Part 3 |
| Gradient descent, classification, probabilities, deep nets | Part 4 |
| Self-supervision, diffusion, next-word, RLVR, hallucination | Part 5 |

Applications are Part 1's job and mechanisms are Part 5's. Part 1 shows generated
images and video and says nothing about how; Part 5 explains diffusion and shows no
new showcase. Keep that split when editing either.

---

## sangnam1-ai-today.html — Day 1, part 1

64 slides. Every claim on a dated public source; every figure publicly licensed and
cited on-slide. Ten captured figures, the rest inline SVG, tables, and cards.
Extra CSS local to this deck: `.sn-a` (accent inline link to a video or source) at
`:42-44`, `.sn-side` (photo beside bullets) at `:60-65`, `.sn-quote` (attributed
blockquote) at `:67-73`.

| Part | Topic | Line |
|---|---|---|
| Title / This Session | | `:79-118` |
| **01** — Three years, one curve | how fast this actually moved | `:119-255` |
| | Ten Years Ago in Seoul (`f-leesedol.jpg`) | `:127` |
| | The Move Nobody Played (`f-alphago-board.png`) | `:143` |
| | A Billion People a Week (adoption numbers) | `:174` |
| | The Tasks Are Getting Longer (`f-metr.png`, METR TH 1.1) | `:210` |
| | This Hour, Two Columns (the deck's own frame) | `:237` |
| **02** — What it can already do | code, pictures, science, mathematics, work | `:256-800` |
| | The Benchmark Nobody Believed (SWE-bench 2 → 94%) | `:293` |
| | What the Companies Say (Nadella / Pichai / Benioff) | `:319` |
| | What It Still Cannot Do (four concrete failures) | `:332` |
| | Type a Sentence, Get a Photograph (`f-sd-astronaut.jpg`) | `:347` |
| | Now It Moves · And It Has a Soundtrack (`f-sora-*.jpg`, both link the clip) | `:359, :372` |
| | You Cannot Tell Any More (the $25M Arup deepfake call) | `:389` |
| | Two Hundred Million Proteins (`f-alphafold2.png`) | `:415` |
| | No Driver, Paying Passengers (`f-waymo.jpg`) | `:431` |
| | **An Eighty-Seven-Year-Old Guess** — Jacobian/Keller, in plain words | `:447` |
| | Disproved in 216 Characters | `:478` |
| | What Is an Erdős Problem? (1,220 catalogued, 47% solved) | `:506` |
| | Erdős Problems Are Falling (#397, #728, #729, #1196, #1051) | `:532` |
| | Gold at the Olympiad (IMO 2025, 35/42) | `:547` |
| | Hard to Find, Easy to Check | `:568` |
| | Ten Results in One Report (why each matters) · Two Thousand Dollars of Tokens | `:591, :607` |
| | Proof a Computer Can Check (Lean) · Not Yet Peer-Reviewed | `:626, :652` |
| | What a Mathematician Warns (Tao's long tail) | `:678` |
| | Four Thousand Support Roles · The Young Are Hit First (`f-canaries.png`) | `:738, :759` |
| | Reading That Plot Too · Tasks, Not Jobs | `:770, :786` |
| **03** — Who owns the training data | the lawsuits, and the first big bill | `:801-921` |
| | Every Model Ate a Library | `:809` |
| | **The First Big Bill** — Bartz v. Anthropic, $1.5B | `:835` |
| | What the Judge Actually Said (Alsup, both halves) | `:856` |
| | The Rest of the Docket (four named cases) · Or Sign a Deal Instead | `:875, :889` |
| **04** — When it goes wrong | two incidents from this summer | `:922-1138` |
| | The Other Column (same capability, pointed elsewhere) | `:930` |
| | July 2026: An Attack Nobody Ordered (timeline) | `:949` |
| | Two and a Half Days Inside · It Came Back After the Fix | `:963, :990` |
| | Found Out Sideways (the revoke request that gave it away) | `:1016` |
| | Two Sentences Worth Keeping (Hobbhahn, Wildeford) | `:1033` |
| | A Second Case, a Different Lab (UK AISI, 122/19/1) | `:1050` |
| | Fifty-Nine Percent, or Three (harness, not model) | `:1076` |
| | Made-Up Citations, Real Sanctions (1,598 filings) | `:1118` |
| **05** — Society is behind | rules, power, Monday morning | `:1139-1231` |
| | Two Curves, Different Slopes | `:1147` |
| | Korea's Rules Arrived in January (AI Basic Act) | `:1168` |
| | The Power Bill (`f-datacenter.jpg`, IEA) | `:1184` |
| | What to Ask on Monday · Today in Six Lines | `:1200, :1217` |
| Closer — "Extraordinary. / And unfinished." | | `:1232` |

Post-cutoff facts (2026 events) are the fragile part of this deck. Before delivery,
re-check: adoption numbers `:174`, SWE-bench `:293`, the Erdős counts `:506` and the
Erdős table `:532`, the OpenAI report `:591`, the settlement's final approval `:835`,
the AISI incident numbers `:1050`, the scheming figures `:1076`, and the hallucination
count `:1118`.

---

## sangnam2-what-is-learning.html — Day 1, part 2

53 slides. Almost no notation: only $x$, $y$, $f$, $g$, and one squared-error line.
Every content slide carries an exhibit — four captured figures, thirteen inline SVG
diagrams, three tables, three mock UI cards.

| Part | Topic | Line |
|---|---|---|
| Title / This Session | | `:44-79` |
| **01** — A model is a function | six products, one shape | `:80-318` |
| | Six Products, One Machine (card grid) | `:88` |
| | Sorting Photographs (`cifar10.png`) | `:102` |
| | Reading a Review (이동진 / 기생충 mock card) | `:114` |
| | Guessing the Next Word (SVG probability bars) | `:141` |
| | Translating a Sentence · Forecasting a Price (`price-chart.png`) | `:165, :185` |
| | Spotting a Defect · Scoring an Application | `:196, :230` |
| | Always the Same Shape (SVG function box) | `:264` |
| | **Two Letters for the Whole Course** — $y = f(x)$ | `:285` |
| | What Changes, What Stays | `:299` |
| **02** — Everything becomes numbers | photos, sentences, customers as lists | `:319-444` |
| | A Photo Is a Grid of Numbers (`mnist-vector.png`) | `:327` |
| | How Long Is That List? (784 → 36M table) | `:338` |
| | A Word Is a Point in Space (`word-embeddings.png`) | `:351` |
| | A Customer Is a Row (churn table) | `:362` |
| | **Naming the Parts, Six Times** — $x$/$y$ per product | `:375` |
| | Three Shapes of Answer · Why This Matters Commercially | `:407, :430` |
| **03** — Where the function comes from | rules out, data in | `:445-804` |
| | The Old Way — Write the Rules (SVG rule tree) | `:453` |
| | What Defines the Digit Zero? · Why Rules Run Out | `:480, :494` |
| | **Learning, Defined in 1959** (Samuel) | `:515` |
| | Three Words: Function, Data, Loss | `:526` |
| | The Function We Wish We Had · We Only See Examples | `:552, :575` |
| | Training Builds a Look-Alike | `:589` |
| | Which Look-Alikes Are Allowed? (function class) | `:623` |
| | What $a\,x + b$ Looks Like (scatter + fitted line, $a$/$b$ labelled) | `:638` |
| | "Close" Everywhere Is Impossible → on Our Examples | `:666, :679` |
| | Scoring a Single Guess · Averaging Over Everyone | `:692, :706` |
| | **The Recipe** — the four lines the series returns to | `:720` |
| | Searching Means Turning Dials | `:737` |
| | Somebody Made Those Labels · The Model Inherits Your Data | `:757, :772` |
| | Two Flavours of Answer (regression / classification) | `:785` |
| **04** — Reading the recipe | same three lines, every product | `:805-944` |
| | Recipe — Spam · Demand · Defect | `:813, :828, :843` |
| | Four More, Same Three Lines · The Recipe Is the Field | `:858, :871` |
| | Three Questions Left Open | `:884` |
| | Patterns, Not Reasons · Patterns Go Stale | `:897, :910` |
| | **Day 2: What Comes Next** (roadmap to Parts 3–5) | `:925` |
| Closer — "A function." | | `:945` |

`:720` is the load-bearing slide of the whole series: Parts 3, 4 and 5 all open by
pointing at the recipe. Do not reword it without following through.

---

## sangnam3-linear-regression-and-overfitting.html — Day 2, part 3

32 slides. Twelve captured plots from the source PDF carry sections 01–03; the rest
is inline SVG and two tables. No closed-form solve anywhere — training is search.

| Part | Topic | Line |
|---|---|---|
| Title / This Session | | `:47-78` |
| **01** — Fitting a line | two dials, one score | `:79-270` |
| | The Recipe, Unchanged (bridge from Part 2) | `:87` |
| | Heights and Weights (`f-hw-scatter.png`) | `:103` |
| | The Job: Height In, Weight Out | `:114` |
| | A Family of Straight Lines · Which of These Is Best? | `:141, :163` |
| | Measure Every Miss (`f-hw-fit.png`) | `:187` |
| | **One Number for the Whole Dataset** — mean squared error | `:216` |
| | Training Is Turning the Dials · What the Dials Tell You | `:229, :252` |
| **02** — More columns, more shapes | features do the bending | `:271-366` |
| | Many Inputs, Same Shape (columns → weights → one number) | `:279` |
| | A Straight Line Cannot Bend (`f-curve-linear.png`) | `:321` |
| | Give It a Curved Column (`f-curve-quad.png`) | `:332` |
| | You Can Always Add Columns (sets up overfitting) | `:343` |
| **03** — Overfitting | memorising is not learning | `:367-580` |
| | Ten Points, One Line (`f-D-linear.png`) | `:375` |
| | A Curve Through Every Point (`f-D-poly7.png`) | `:386` |
| | Three Fits, Same Data (`f-triptych.png`) | `:397` |
| | **Two Ways to Be Wrong** — bias and variance | `:408` |
| | More Data Tames It (`f-more-data.png`) | `:427` |
| | You Cannot Just Look · Hold Some Data Back | `:438, :462` |
| | Perfect on Train, Lost Elsewhere (`f-val-poly6.png`) | `:483` |
| | Train, Validation, Test | `:494` |
| | The Classic Picture (train vs validation vs model size) | `:517` |
| | Prefer the Simpler Story (Occam) · If You Are Overfitting | `:540, :569` |
| | Today in Four Lines | `:581` |
| Closer — "Fit the pattern, not the noise." | | `:593` |

---

## sangnam4-training-and-classification.html — Day 2, part 4

37 slides. Opens on the linear-regression loss and reframes fitting as
minimisation; then gradient descent as downhill-in-fog, then classification, then
one sentence of deep learning: stack the same box. Nine captured figures.

| Part | Topic | Line |
|---|---|---|
| Title / This Session | | `:47-86` |
| **01** — Downhill in the fog | searching a space you cannot see | `:87-294` |
| | **The Score, Written Out** — the MSE this deck minimises | `:95` |
| | Fitting Is Finding a Minimum (contour rings in the $a,b$ plane) | `:121` |
| | The Only Question Training Asks (dials / score / smallest) | `:148` |
| | The High-School Answer (slope = 0) | `:164` |
| | No Formula for a Billion Dials | `:183` |
| | Standing on a Hillside in Fog (`f-landscape.png`) | `:198` |
| | All You Can Feel Is the Slope | `:209` |
| | **Look, Step, Repeat** — the loop | `:231` |
| | The Step Size Is a Choice (learning rate) | `:248` |
| | Too Much Data for One Step (mini-batches) | `:267` |
| **02** — Drawing the line | classification as a sign test | `:295-345` |
| | Number or Label? · Two Clouds, One Line (`f-clf-boundary.png`) | `:303, :324` |
| | Sometimes No Line Works (`f-clf-none.png`) | `:335` |
| **03** — Soft answers | probabilities, and the slope they restore | `:346-475` |
| | Hard Answer, Soft Answer · Distance Is Confidence | `:354, :375` |
| | Squash It Into a Probability (inline sigmoid SVG) | `:399` |
| | **Logistic Regression** — a line plus a squash | `:423` |
| | Scoring a Probability | `:439` |
| | Now the Score Has a Slope (step vs smooth, in one plot) | `:454` |
| **04** — Reading the errors | thresholds and the metrics that matter | `:476-555` |
| | Where to Put the Threshold · Two Ways to Be Wrong | `:484, :504` |
| | Precision and Recall (`f-prec-recall.png`) | `:525` |
| | Accuracy Is a Trap (class imbalance) | `:543` |
| **05** — Stacking the boxes | deep learning in four slides | `:556-696` |
| | Straight Lines Run Out · Stack the Boxes | `:564, :589` |
| | Same Four Lines (the recipe, unchanged) | `:618` |
| | Depth Buys Reuse (pixels → edges → parts → car) | `:635` |
| | You Might Not Need It (`f-overkill.png`) | `:665` |
| | Today in Five Lines | `:684` |
| Closer — "Take the slope. Then squash it." | | `:697` |

---

## sangnam5-frontier.html — Day 2, part 5

28 slides. The closing deck: what the same recipe does once the labels are gone.
Mechanism only — the showcase moved to Part 1. Ends on hallucination, deliberately.

| Part | Topic | Line |
|---|---|---|
| Title / This Session | | `:61-92` |
| **01** — Learning without labels | the bottleneck, removed | `:93-172` |
| | Labels Are the Bottleneck | `:101` |
| | **The Answer Key Is Inside the Data** — self-supervision | `:123` |
| | No Labels at All (`f-clusters.png`) | `:145` |
| | Which Line of the Recipe Changed | `:156` |
| **02** — Machines that make things | from recognising to creating | `:173-361` |
| | Recognise, or Create · Learning What Typical Looks Like | `:181, :208` |
| | Sampling Is the Product | `:234` |
| | Start From Static (`f-diffusion-samples.png`) | `:250` |
| | Add Noise Until Nothing Is Left (`f-noise-strip.png`) | `:261` |
| | **Then Learn to Undo One Step** — diffusion, in one slide | `:281` |
| | A Prompt Steers the Undoing · Video Is the Same Trick | `:311, :339` |
| **03** — Machines that talk | next word, then verified reward | `:362-590` |
| | Next Word, Over and Over | `:370` |
| | One Loss, Trillions of Words | `:393` |
| | Predicting Text Is Not Obeying | `:416` |
| | First: Show It Good Answers → Then: Which of These Two? | `:439, :461` |
| | Some Answers Can Be Checked | `:487` |
| | **The Checker Becomes the Teacher** — RLVR | `:503` |
| | Think Longer, Do Better | `:531` |
| | Confident, and Sometimes Wrong | `:555` |
| | Today in Five Lines | `:575` |
| Closer — "Powerful. Not yet trustworthy." | | `:591` |

---

## Figures

`figs/` holds 41 files. Captured from the source PDF for Parts 3–4: `f-hw-scatter`,
`f-hw-fit`, `f-curve-linear`, `f-curve-quad`, `f-D-linear`, `f-D-poly7`,
`f-more-data`, `f-triptych`, `f-val-poly6`, `f-val-quad`, `f-gd-contour`,
`f-clf-boundary`, `f-clf-none`, `f-overkill`. Third-party, cited on-slide:
`f-landscape` (losslandscape.com), `f-prec-recall` (Wikipedia), `f-clusters`,
`f-diffusion-samples` (Stability.ai), `f-noise-strip` (Song et al. 2021).

Part 1 additions, all licence-checked with the licence named on the slide:
`f-leesedol.jpg` (LG Electronics, CC BY 2.0), `f-alphago-board.png` (CC BY-SA 4.0),
`f-metr.png` (METR, CC BY), `f-sd-astronaut.jpg` (SDXL, public domain),
`f-sora-tokyo.jpg` and `f-sora-mammoth.jpg` (public domain), `f-alphafold2.png`
(CC BY-SA 4.0), `f-waymo.jpg` (Dllu, CC BY 4.0), `f-canaries.png` (Stanford Digital
Economy Lab), `f-datacenter.jpg` (CC BY-SA 3.0).

Orphaned by the Day 2 trim, kept so the cut slides can be restored:
`f-aug-dog`, `f-aug-digit`, `f-gd-small-lr`, `f-gd-large-lr`, `f-gd-init`,
`f-clf-many`, `f-soft-guess`, `f-roc`, `f-superres`, `f-detection`, `f-semisup`,
`f-augviews`, `f-gensamples`, `f-gan`, `f-D-linear`/`f-DD-*` variants.

## What the Day 2 trim removed

Part 3: "why squared", "the fitted line", the section-01 summary, the business
table, "still a weighted sum", the two point-nudge stability slides, "the lesson",
the generalisation definition, the rules of thumb, both augmentation slides, and all
of section 04 — double descent, the three dials, scaling laws, balance, the data
wall, the commercial framing. "The Classic Picture" was kept and moved into
section 03.

Part 4: the too-small/too-large step pictures, two dials at once,
where you start, "not a bowl", the section-01 recap, "still a weighted sum", the
maximum-margin chain (many lines / widest gap / allow mistakes), "probably red,
certainly blue", the line-plus-squash diagram, the penalty curve, multi-class and
softmax, "which mistake is cheaper", the threshold sweep and ROC curves, universal
approximation, and the three application showcases. Cut later, on review: "Counting
Mistakes" and "A Score With No Slope" — the staircase point now lives on the one
slide that needs it, "Now the Score Has a Slope" (`:454`).

Part 3, on review: "Two Inputs Instead of One" (the flat-sheet picture).

Part 5: sections 04 and 05 (now Part 1), "a few labels, many photos", "two views",
"segments nobody named", "made-up photographs", the GAN detour, "where this already
pays", "scale bought new behaviour", "where verification is easy". Two slides were
dropped rather than moved: the 0.77 / 12% auditor-capability slide and the old
five-line recap.
