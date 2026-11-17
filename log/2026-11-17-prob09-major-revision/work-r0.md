# work-r0 — setup proposal (planning query, no implementation)

- Branch: `2026-11-17-prob09-major-revision`, created from baseline `b20ab73ac7e74e9489d379cf9caad7565f17e31e`. This commit adds only this tracked record: copies of `job.md`, `requests.md` and `evidence.md`, plus this report. No deck, note or Markdown file has changed. `plan-v1.md` has not been copied, because no pointer has announced it.
- ID-only commit: not made. It waits for the plan-v2 work order.

## Finding

The baseline cannot get a pure attribute-only ID commit for the note:
- The deck has 113 slides and no `data-slide-id` attributes.
- The HTML note has 11 chapter `<section>`s with 58 `<h3>` subsections and no `<article>` elements. There is nothing in the note to attach slide IDs to.
- The note's `<style>` has no `article` or `section` rules, so adding wrapper elements does not change how the note renders.

## Proposal: two setup commits, both mechanical, before any substantive edit

**Commit A: note-structure preparation. Tags only, every word kept.**
- Touches only `prob09-monte-carlo-note.html`.
- Adds 113 `<article>` wrappers with no attributes, one per baseline slide, in slide order.
- Assigns each existing block to the article of the first slide it explains. A block is a chapter `<h2>` with its intro, or an `<h3>` subsection.
- A slide with no dedicated text gets an empty `<article></article>`. That adds no words and renders nothing.
- No text, formula, heading, anchor or class changes. No block is reordered. If a note block is out of slide order, it stays where it is, goes into the article of the nearest preceding slide, and is listed in the report.
- The `<section>` chapter wrappers stay. Articles nest inside them and never cross a chapter boundary.
- Checks:
  - (1) Stripping all `<article>` and `</article>` tags reproduces the baseline file byte for byte, apart from the whitespace the wrappers add. I will run a normalized-whitespace comparison and report it.
  - (2) The visible text and the KaTeX source sequence are identical to baseline.
  - (3) A render at 1280 px and at 430 px shows no visual change.
- The block-to-slide assignment is a judgement call, so I report it in full as the trail `h2/h3 heading → baseline slide → S-ID`.

**Commit B: the contract's ID-only commit. Attributes only.**
- Adds `data-slide-id="S01"`…`"S113"` to the 113 deck slides and the same IDs to the 113 note articles, in one commit.
- Check: removing every ` data-slide-id="…"` reproduces commit A byte for byte, for both files.
- `job.md` records commit B as `id commit`. Content review diffs against it, so `git diff <id commit> <sha>` shows no ID or wrapper noise.

**Accessible Markdown edition (`prob09-monte-carlo-note.md`).** The contract requires IDs only on deck slides and HTML note articles. I propose leaving the Markdown untouched in A and B. It gets its new structure in the substantive build, mirroring the final articles. If you want ID markers there too, I can add them in A as HTML comments (`<!-- S01 -->`, invisible when rendered). That is a planning decision.

**After setup.** The substantive build rewrites the articles to the final slide sequence, using the Message → Reading → script/details → sources hierarchy. Splits follow the ID rules (`S07a`; new slides take `S114`+). `work-r1` will carry the full baseline-to-final mapping.

## Plan issues (decision needed from slides-review)

1. **Contract reading.** The contract says IDs are added "in a commit that changes nothing else". I read A + B together as satisfying it: A adds structure only and no IDs, and B is attribute-only. No contract relaxation is needed, because B alone meets the ID-only rule. If you read the contract as forbidding any preparatory commit, the alternative is a deck-only ID commit with note articles introduced in the build. That breaks the "same commit" rule, so it would need Albert's explicit exception. I do not recommend it.
2. **Markdown edition.** Leave it untouched in setup (my default), or add comment ID markers in commit A.
3. **Empty articles.** Some baseline slides will get empty articles. They are temporary scaffolding for pairing and are filled in the build. Please confirm that plan-v2 does not expect setup to write any note text.

## Checks run

- Structure counts read from the baseline files: 113 slides, 0 `data-slide-id`, 11 `<section>`, 58 `<h3>`, 0 `<article>`, no article/section CSS in the note.
- No lint or render was run, because no source file changed.
