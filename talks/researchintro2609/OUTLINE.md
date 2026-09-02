# researchintro2609/ — Finding a Research Project (Sep 2026)

One deck, one seminar session. Audience is **first-year graduate students with no
prior research experience**: they have finished technical coursework and are taking
LLM / agent / RL courses, so the vocabulary is there and the notion of "a project"
is not. The deliverable being described is **a semester project, not a paper** —
nontrivial, but below workshop-paper scale (slide 9 places the bar explicitly).

| Deck | Slides | Companion |
|---|---|---|
| `researchintro2609.html` | 33 | none |

## The through-line

Two ideas carry the deck, in this order:

1. **A project is a new artwork** — new, nontrivial, defensible. Stated once on
   slide 5, echoed once on the wall-label slide (`:596`), and otherwise left alone.
   The analogy is a frame, not a running commentary: an earlier 58-slide draft
   paired every research slide with an art twin and was cut for that reason. Do not
   re-add art slides.
2. **Start by reproducing** (§02). Copying a known result is not the project; it is
   the fastest way into one, because reproduction is where the gap becomes visible.
   Slides 11–13 carry this and are the spine of the deck's practical advice.

Extra CSS local to this deck (`:20-40`): `.ri-steps` (numbered step list, adapted
from `sangnam2-what-is-learning.html`'s `.sn-recipe`), `.ri-label` (wall-card panel),
`.ri-airy` (roomier bullets, used only on slide 5), `.ri-fig` (centred SVG wrapper),
`.cite-left` (left-aligned citation).

Visually rich by construction: 12 inline SVG exhibits, no captured figures.

## Sections

| Part | Topic | Line |
|---|---|---|
| Title / Contents | | `:44-82` |
| **01** — What a Project Is | novel, nontrivial, not a copy | `:83-240` |
| | The Problem Nobody Hands You (2×2: homework / assigned / tutorial / yours) | `:92` |
| | Project as Artwork — the central analogy, two question blocks | `:125` |
| | What a Project Owes — new · nontrivial · defensible | `:153` |
| | Not a Project — four failure rows | `:176` |
| | The Single-Prompt Test | `:190` |
| | Where the Bar Sits — prompt / homework / **project** / workshop / conference | `:216` |
| **02** — Where to Start | reproduce, then find what breaks | `:241-426` |
| | Start by Reproducing — reproduce → disagree → the gap is yours | `:250` |
| | What Reproduction Breaks — four findings, four questions | `:278` |
| | A Reproduction Becomes a Project — worked RAG-QA example, 4 steps | `:292` |
| | Three Ways In — break it · move it · measure it | `:307` |
| | Worked escalations: fine-tune · RAG bot · RL agent | `:330`, `:345`, `:360` |
| | The Two-Day Test (Albert's tip, rendered as a branch) | `:375` |
| | Find the Bottleneck | `:400` |
| **03** — Reading the Field | what is open, and why people care | `:427-586` |
| | Where the Field Has Been (2012 AlexNet → now agents/embodiment) | `:436` |
| | Why Physical AI, Now — the open column | `:472` |
| | Mapping the Frontier — settled / contested / blocked | `:504` |
| | How to Survey — five concrete moves | `:524` |
| | Read More Than Feels Reasonable (skim 20 / read 3 / reproduce 1) | `:540` |
| | GPT as Accelerator, Not Author | `:563` |
| **04** — Justify, Then Start | the label, the sentence, the first experiment | `:587-706` |
| | Your Project's Wall Label — question · stakes · difficulty · difference · evidence | `:596` |
| | The Positioning Sentence ("Unlike X, which assumes Y, we…") | `:610` |
| | The Smallest Convincing Experiment | `:629` |
| | Four Weeks to a Topic | `:655` |
| | One Page Before Any Code — the actual assignment | `:685` |
| Closer — "Start reading" | | `:700` |

## Notes for future edits

- The **one-page brief** (`:685`) is the concrete ask the seminar ends on. If the
  seminar's assignment changes, that slide and the closer (`:700`) change together.
- The "Not a Project" table (`:176`) says *reimplement a paper, **and stop***, not
  "reimplement a paper". Reproduction is endorsed in §02; keep the two consistent if
  either is reworded.
- Slides 15–17 are the worked escalations, deliberately drawn from the courses the
  audience is taking now (fine-tuning, RAG, RL). Swap the domain before swapping the
  structure — all three follow task → *and then?* → problem → question.
- The deck has no dated claims except the ML timeline (`:436`); refresh its right
  end when "now" moves.
