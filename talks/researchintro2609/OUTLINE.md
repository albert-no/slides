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
   slide 5, echoed once on the wall-label slide (`:609`), and otherwise left alone.
   The analogy is a frame, not a running commentary: an earlier 58-slide draft
   paired every research slide with an art twin and was cut for that reason. Do not
   re-add art slides.
2. **Start from what you noticed, then reproduce** (§02). Topics come from your own
   work, an interest, a video, a news story — anything (`:249`). Then: copying a
   known result is not the project, it is the fastest way into one, because
   reproduction is where the gap becomes visible. Slides 13–16 carry this.

Extra CSS local to this deck (`:20-40`): `.ri-steps` (numbered step list, adapted
from `sangnam2-what-is-learning.html`'s `.sn-recipe`), `.ri-label` (wall-card panel),
`.ri-airy` (roomier bullets, used only on slide 5), `.ri-fig` (centred SVG wrapper),
`.cite-left` (left-aligned citation).

Visually rich by construction: 13 inline SVG exhibits, no captured figures.

## Sections

| Part | Topic | Line |
|---|---|---|
| Title / Contents | | `:44-82` |
| **01** — What a Project Is | novel, nontrivial, not a copy | `:83-240` |
| | The Problem Nobody Hands You (2×2: homework / assigned / tutorial / yours) | `:91` |
| | Project as Artwork — the central analogy, two question blocks | `:124` |
| | What a Project Owes — new · nontrivial · defensible | `:152` |
| | Not a Project — four failure rows | `:175` |
| | The Single-Prompt Test | `:189` |
| | Where the Bar Sits — prompt / homework / **project** / workshop / conference | `:215` |
| **02** — Where to Start | from an interest to a real gap | `:241-452` |
| | Topics You Already Have — five everyday sources feed one noticed thing | `:249` |
| | From Interest to Question — three worked conversions | `:289` |
| | Start by Reproducing — reproduce → disagree → the gap is yours | `:302` |
| | What Reproduction Breaks — four findings, four questions | `:330` |
| | A Reproduction Becomes a Project — worked RAG-QA example, 4 steps | `:344` |
| | Three Ways In — break it · move it · measure it | `:359` |
| | Escalating a RAG Bot — task → *and then?* → problem → question | `:382` |
| | The Two-Day Test (Albert's tip, rendered as a branch) | `:397` |
| | Find the Bottleneck | `:422` |
| **03** — Reading the Field | what is open, and why people care | `:453-600` |
| | Where the Field Has Been (2012 AlexNet → now agents/embodiment) | `:461` |
| | Recent Beats Retro — how much room is left, old vs current | `:497` |
| | Recent, at Small Scale — frontier version vs your version | `:522` |
| | How to Survey — five concrete moves | `:537` |
| | Read More Than Feels Reasonable (skim 20 / read 3 / reproduce 1) | `:553` |
| | GPT as Accelerator, Not Author | `:576` |
| **04** — Justify, Then Start | the label, the sentence, the first experiment | `:601-720` |
| | Your Project's Wall Label — question · stakes · difficulty · difference · evidence | `:609` |
| | The Positioning Sentence ("Unlike X, which assumes Y, we…") | `:623` |
| | The Smallest Convincing Experiment | `:642` |
| | Four Weeks to a Topic | `:668` |
| | One Page Before Any Code — the actual assignment | `:698` |
| Closer — "Start reading" | | `:714` |

## Notes for future edits

- The **one-page brief** (`:698`) is the concrete ask the seminar ends on. If the
  seminar's assignment changes, that slide and the closer (`:714`) change together.
- The "Not a Project" table (`:175`) says *reimplement a paper, **and stop***, not
  "reimplement a paper". Reproduction is endorsed in §02; keep the two consistent if
  either is reworded.
- Slide 17 is the one remaining worked escalation (RAG, from the courses the
  audience is taking). The fine-tune and RL versions were cut for repetition
  2026-09-02; keep it to one unless the seminar gets longer.
- **Recency advice (`:497`, `:522`)** is Albert's: an old architecture is fine but a
  harder place to be new, and a recent topic at *small* scale is the better trade.
  The two slides are a pair — the first makes the claim, the second makes it
  affordable.
- The deck has no dated claims except the ML timeline (`:461`); refresh its right
  end when "now" moves.
