# Planner brief

Entry point for the agent that plans slide jobs: it researches, writes the plan, and reviews the result. The executor builds the slides. This brief covers **what** a plan must decide. The **how** (markup, CSS, rendering) belongs to the executor. Section numbers point into `DESIGN_SYSTEM.md` (DS). Read by section, never whole: each DS section opens with a `Lines` range in the index at the top of the file. Where this brief and DS disagree, **DS wins**.

## Read before planning

| Need | Read |
|---|---|
| Ranked priorities, density, budget, style rules | DS §1 — always |
| Deck order, slide-count norms, exemplar decks | DS §2 |
| Component names (vocabulary only) | DS §4 |
| Concept-first vs rigorous; theorem/proof/build-up | DS §5 |
| Page numbers, cross-deck references, citation format | DS §6 |
| Figures: sourcing, size, takeaway title, key | DS §8 |
| Speaker notes and technical supplements | DS §9 |
| Series continuity, OUTLINE.md | DS §10, then the leaf `OUTLINE.md` of the target folder |
| Rhythm to imitate | the DS §2 exemplar deck for the genre |

Skip `GOTCHAS.md`, `.claude/`, `reference/` and the workflow parts of `CLAUDE.md`: they are implementation detail for the executor.

## Rules a plan must respect

**Priorities (DS §1), lower wins:** 0 font size, 1 density, 2 overflow, 3 empty space. Type is never shrunk to make content fit. A packed slide splits into *steps*, each with its own point. There is no slide budget.

**Density (DS §1 Priority 1).** At most 7 lines × 7 words per slide, about 40 words of body prose, phrases not sentences. There are four bounded exceptions: a takeaway title on a finding slide, a one-line definition, a plot key, and a qualifier the claim needs. A necessary qualifier is never cut for space.

**Capacity (DS §1 Priority 2).** One title plus at most 5 body elements. A table costs one element per row. Equation block + table + highlight on one slide is already over. At most one 3-line equation block plus one 1-line equation per slide. If a planned slide carries more than this, plan two slides.

**Style rules (DS §1, rules 1–13).** The ones plans most often break:
- One idea and one exhibit per slide. Prose and exhibit use the same words in the same order.
- Every slide states its point. A finding slide's title is its takeaway; any other content slide gets a one-line "Point:".
- General before specific: motivation before the first case, a concept before the attack that uses it.
- Ghost-deck test: the `h2` titles alone must outline the arc. Plan titles first.
- Spell out acronyms on first use. An unfamiliar case or term gets one line saying what it is and why it matters, with sourced dates and versions.
- A question the author asked gets a short explicit answer **on the slide**, not only in the note.
- Self-contained slides: no "next week", "as we saw", "see Lecture 3". No placeholders.

**Audience mode (DS §5).** State it per deck. Concept-first: example → intuition → precise qualified claim, with formal math in the note or `tech.html` (DS §9 stay/move rule). Rigorous: the intuition → theorem → proof pairing, multi-slide proofs, a recap chain for proofs of 4+ steps. The author's latest instruction on mode wins.

**Visuals (DS §8).** Every content slide has an exhibit. For each slide, name the picture before the bullets. Source order:
1. a real paper figure, identified by paper and Figure N
2. an original diagram, only when no canonical figure exists
3. a TODO mark naming the wanted figure and its source

When reading the figure is the task, it gets the whole slide, a takeaway title, and a key covering axes, direction of "better", and encodings. The method comes before its result. A table comparing magnitudes becomes bars.

**Deck anatomy (DS §2).** Title → Contents (3+ sections) → numbered section dividers → content → one optional closing summary → closer. Divider names match Contents. The DS §2 slide-count norms are a target, not a contract.

**Citations (DS §6).** Venue author order, one line per citation, `Author et al., Venue YYYY — Figure N.` for figures. How a source was handled (cropped, redrawn, truncated) goes in the cite line. Sections are named by their exact heading.

**Companions (DS §9).** Anything moved off a slide must land in `<deck>-note.html` (one article per slide) or `<deck>tech.html`. The plan says which.

**Continuity (DS §10).** Check the leaf `OUTLINE.md` for what earlier decks defined. For each prerequisite, decide explicitly: reuse via a Recall card, adapt, or defer. Don't redefine.

**Facts.** Every factual claim, number, date, version, figure and quote in the plan carries a source (URL plus page, section, table or figure). The executor won't correct facts from memory. It flags unsourced facts rather than guessing.

## Plan format

The job contract `log/PIPELINE.md` defines the job files and the full plan format, and wins over this section. In short:

1. **Header.** Deck path(s), audience mode, base commit, and a baseline map from current page numbers to `h2` titles. The author's request goes verbatim in `requests.md`.
2. **Slide IDs.** Use stable IDs (`S07`, plus the current `h2` for an existing slide) as the key. Keep the page trail for the author's comments (comment → baseline page and title → slide ID), but never key a change by page number: splits renumber every later page. A split of `S07` gives `S07a`, `S07b`.
3. **Work packages.** Contiguous, disjoint slide ranges with their note and tech sections. Mark dependencies between packages, e.g. "S12 reuses the S09 diagram". Each package must be editable without touching another package's slides.
4. **Per slide:**
   - point (one line)
   - proposed title
   - exhibit, and what it must show
   - facts with sources
   - what moves to the note or tech file
   - the author comment it answers, if any
   - acceptance check (what a reviewer verifies)
5. **Shared surfaces, separately.** Contents slide, section dividers, recap/closer, cross-slide references, OUTLINE entries. The executor edits these once, after merging the packages.

**Stay out of:** markup, class names beyond the DS §4 vocabulary, CSS, px values, font sizes, file line numbers, figure crop coordinates, and a fixed final slide count. If a planned slide can't meet DS §1 without shrinking type, the executor splits it or moves content to the note, and reports the deviation. Plans should leave room for that.

## Review checklist

- Each author comment is answered on the slide where it was raised, or explicitly declined with a reason.
- Ghost-deck test passes. Contents and dividers agree.
- No slide over the DS §1 density or capacity limits; no shrunk type.
- Figure slides: takeaway title, key, legible labels on the render (DS §8 acceptance check).
- Every trimmed item is present in the note or tech file.
- Citations follow DS §6, and facts match the plan's sources.
- `OUTLINE.md` updated. The slide count agrees in all four places (DS §10).
