# researchintro2609/ — Finding a Research Project (Sep 2026)

One deck, one seminar session. Audience is **first-year graduate students with no
prior research experience**: they have finished technical coursework and are taking
LLM / agent / RL courses, so the vocabulary is there and the notion of "a project"
is not. The deliverable being described is **a semester project, not a paper** —
nontrivial, but below workshop-paper scale (slide 15 places the bar explicitly).

| Deck | Slides | Companion |
|---|---|---|
| `researchintro2609.html` | 58 | none |

## The through-line

The whole deck runs on one analogy, stated on slide 6 and never dropped: **a project
is a new artwork**. Each section pairs the artist's version of a discipline with the
researcher's, in that order — art first, research second. Keep that pairing when
editing; the art slide is the intuition and the research slide is the payload, and a
research slide without its art twin loses the argument.

Extra CSS local to this deck (`:20-38`): `.ri-steps` (numbered step list, adapted
from `sangnam2-what-is-learning.html`'s `.sn-recipe`), `.ri-label` (museum wall-card
panel), `.ri-fig` (centred SVG wrapper), `.cite-left` (left-aligned citation).

Visually rich by construction: ~21 inline SVG exhibits, no captured figures. Art
movements are drawn as an SVG timeline rather than reproduced — the canonical works
(Picasso, Duchamp) are not public domain, and the dates carry a hedging citation.

## Sections

| Part | Topic | Line |
|---|---|---|
| Title / Contents | | `:41-84` |
| **01** — The Analogy | what a project is, and the four things it is not | `:85-376` |
| | Two Kinds of Question (2×2: homework / assigned / tutorial / yours) | `:126` |
| | Project as Artwork — the central analogy | `:157` |
| | What an artwork owes → what a project owes | `:185`, `:208` |
| | Four failures: paint-by-numbers, forgery, reprint, doodle | `:223`, `:257` |
| | The four triviality tests: single prompt · existing repo · swapped dataset · rerun | `:271`, `:297`, `:313`, `:334` |
| | Where the Bar Sits — prompt / homework / **project** / workshop / conference | `:351` |
| **02** — Survey | art history, and why a literature map is not a list | `:377-668` |
| | Movements Answer Constraints (art timeline, 1870s–1960s) | `:400` |
| | Our Field Has Movements (2012 AlexNet → now agents/embodiment) | `:456` |
| | Each Wave Removed a Blocker | `:492` |
| | Why Physical AI, Now — the open column | `:506` |
| | Mapping the Frontier — settled / contested / blocked | `:561` |
| | How to Survey — five concrete moves | `:581` |
| | A Survey Is a Map, not a list | `:621` |
| | Timing the Wave — too early / the window / too late | `:642` |
| **03** — Nontriviality | the question you never stop asking | `:669-884` |
| | The artist's running question → yours | `:677`, `:691` |
| | The Two-Day Test (Albert's tip, rendered as a branch) | `:727` |
| | The Escalation Ladder: task → problem → research question | `:752` |
| | Worked escalations: fine-tune · RAG bot · RL agent | `:775`, `:790`, `:805` |
| | Find the Bottleneck; Shrink the Claim | `:820`, `:848` |
| | Five Questions Before Committing | `:869` |
| **04** — Justification | the wall label, and the skeptic | `:885-1043` |
| | Every Artwork Has a Label → Your Project's Wall Label (5 lines) | `:893`, `:907` |
| | The Positioning Sentence ("Unlike X, which assumes Y, we…") | `:921` |
| | The Skeptic in the Room — four questions, as speech bubbles | `:940` |
| | "Isn't This Just X?" — the four-move answer | `:983` |
| | The Smallest Convincing Experiment; A Negative Result Counts | `:998`, `:1024` |
| **05** — Working Habit | what to do over the next month | `:1044-1238` |
| | Read More Than Feels Reasonable (skim 20 / read 3 / reproduce 1) | `:1052` |
| | GPT as Accelerator, Not Author | `:1075` |
| | A Sketchbook of Bad Ideas | `:1100` |
| | The Weekly Loop; Four Weeks to a Topic | `:1129`, `:1154` |
| | Traps That Catch Everyone | `:1184` |
| | One Page Before Any Code — the actual assignment | `:1200` |
| | Three Questions to Carry: is it new · is it hard · can I say why | `:1216` |
| Closer — "Start reading" | | `:1239` |

## Notes for future edits

- The **one-page brief** (`:1200`) is the concrete ask the seminar ends on. If the
  seminar's assignment changes, that slide and the closer (`:1239`) change together.
- Slides 35–37 are the only worked examples, and they are deliberately drawn from
  the courses the audience is taking now (fine-tuning, RAG, RL). Swap the domain
  before swapping the structure — all three follow task → *and then?* → problem →
  question.
- The deck has no dated claims except the ML timeline (`:456`); refresh its right
  end when "now" moves.
