# Pitfalls and lessons learned

Issues that have eaten time. Search here before re-debugging — by symptom, not by topic.

**Division of labor**: this file is *symptom → cause → fix/pointer* for debugging. The normative authoring rules live in `DESIGN_SYSTEM.md` — when an entry here and DESIGN_SYSTEM overlap, DESIGN_SYSTEM is canonical. At generation time read DESIGN_SYSTEM; come here when something looks wrong.

Entries are grouped into nine categories, most-frequently-hit first:

1. [Math & KaTeX rendering breakage](#math--katex-rendering-breakage)
2. [Fonts & canonical tokens](#fonts--canonical-tokens)
3. [Overflow & the vertical budget](#overflow--the-vertical-budget)
4. [Prose & line breaks](#prose--line-breaks)
5. [Citations](#citations)
6. [Diagrams & SVG](#diagrams--svg)
7. [Proof & structure drift](#proof--structure-drift)
8. [Engine, navigation & audit false alarms](#engine-navigation--audit-false-alarms)
9. [Toolchain: headless rendering, figures & bundling](#toolchain-headless-rendering-figures--bundling)

---

## Math & KaTeX rendering breakage

### Equation broken on page N → all later slides garbled

Symptom: a math-block on page N renders as raw `$$…$$` text or random italicized letters, **and every slide after page N is also garbled**.

Cause: KaTeX runs with `throwOnError: false`, so a parse failure doesn't crash but corrupts the auto-render walker's cursor. The most common single trigger is **literal `<` inside math being parsed by the HTML lexer as the start of a tag** — `X_{<i}`, `\sum_{i<j}`, `0<D\le\sigma^2` — which silently swallows everything until the next `>`. KaTeX never sees the original math.

First-pass diagnosis when the user reports cascading breakage: `python3 scripts/lint-deck.py <deck>.html` errors on literal `<` inside math (and on the delimiter-escape bug below). Manual grep:
```
grep -nE '\$[^$]*<[a-zA-Z]' <deck>.html
grep -nE '\$\$[^$]*<[a-zA-Z]' <deck>.html
```
Replace any matched `<` with `&lt;` inside math expressions.

Other (rarer) triggers: unbalanced `\begin{aligned}/\end{aligned}`, missing `&` alignment markers, a stray `$` in surrounding prose that opens a phantom math span, mismatched `{}`. If grepping for `<` doesn't find the bug, scan the math-blocks above the first visibly-broken slide for these.

### Parenthesized text renders as italic math → KaTeX delimiter escape bug

Symptom: `(learned or heuristic)` renders as italic `learnedorheuristic`; `[M]` in a token chip is slanted at the wrong height.

Cause: the KaTeX `onload` handler must double-escape LaTeX delimiters. The handler lives inside an HTML `onload="…"` attribute, so strings pass through HTML and JS string parsing. With single backslashes (`'\('`), the JS parser eats `\(` as an unrecognized escape, leaving KaTeX with bare `(`, `)`, `[`, `]` as delimiters — every parenthesized phrase becomes inline math.

```html
<!-- correct: double backslash -->
{left:'\\(',right:'\\)',display:false},
{left:'\\[',right:'\\]',display:true}

<!-- wrong: silently broken -->
{left:'\(',right:'\)',display:false},
```

`reference/deck-skeleton.html` has the canonical handler; match it exactly. Audit: `grep -c "'\\\\(" *.html` should be ≥ 1 per deck.

### `$g_1$` shows as literal text → label is in SVG `<text>`

Symptom: math inside a diagram renders as `$g_1$` instead of italic *g* with a subscript.

Cause: KaTeX auto-render walks the HTML DOM but doesn't descend into SVG text nodes.

Fix: build diagram structure in HTML (flex/grid layout, div boxes, CSS-styled circles) with a thin SVG overlay for arrows only. Pattern: `.fl4-*` (slide 4), `.ldp-*` (slide 9), `.rdm-*` (slide 30) in `courses/privacy/lectures/01-dp/dp8-fl.html`. For math labels over a full SVG figure, use absolute-positioned HTML spans — recipe in `DESIGN_SYSTEM.md` → Recipes → KaTeX overlays on SVG.

### Greek letters in table headers turn capital → `text-transform: uppercase` on `<th>`

Symptom: math inside a `<th>` is corrupted — `$\gamma$` shows as Γ, `$\varepsilon$` as E, `$k\varepsilon$` as "KE".

Cause: canonical `th` styling applies `text-transform: uppercase`, and the transform reaches into the KaTeX spans rendered inside the header cell.

Fix (any of, in order of preference): use plain-word column headers ("epsilon", "budget") and state the symbols in a `.muted` paragraph above the table; or move the parameterization out of the header row entirely; or wrap the math in `<span style="text-transform:none">…</span>` inside the `<th>`. Math in `<td>` body cells is unaffected.

### Italic prose collapses spaces → Yonsei has no italic face

Symptom: a phrase rendered with `<i>` or inline `font-style: italic` reads as glued letters (e.g. "all positions" → "allpositions").

Cause: Yonsei TTFs are all `font-style: normal`; Noto Sans is loaded without italic. The browser synthesizes oblique by skewing normal glyphs ~12°, which inherits upright metrics and breaks kerning.

Fix:
- No `<i>`, no inline `font-style: italic`. `em` is globally `font-style: normal; color: var(--gray-text)` — that *is* the inline muted look (body size, inherited). For a whole subordinate line use `<p class="muted">` (the color-only block class — same gray, body size; see "`.muted` … render tiny" below). Use `<strong>` (Yonsei Blue) for emphasis.
- In KaTeX math, English phrases go in `\text{…}`. Bare `all positions` in math mode renders each letter as italic math with zero inter-letter space. Identifier letters stay italic — correct math typography.
- If non-math prose still renders italic, suspect the KaTeX delimiter bug above.

### Standalone bundle renders raw `$...$` strings

Symptom: `<deck>.standalone.html` shows literal math; the authoring source renders fine.

Cause (fixed 2026-04): `scripts/bundle.py` regex `onload=["\']([^"\']+)["\']` treated either quote as terminator, so the KaTeX handler was truncated at the first inner `'`.

Fix in code: regex now uses alternation — `onload=(?:"([^"]*)"|'([^']*)')`. Verify after bundling: `chrome --headless --dump-dom <standalone>.html | grep -c 'class="katex"'` should be ≥ 1 for any math deck.

---

## Fonts & canonical tokens

### Fonts look small → canonical tokens were shadowed

Symptom: body / headings render smaller than the Kangwook reference (`reference/kangwook*.png`) or smaller than a sibling deck.

Cause: a per-deck `<style>` redefined `p`, `li`, `h2`, `h3`, `.small`, `.tiny`, `.subtitle`, or `.math-block` `font-size`. Canonical values in `reference/deck.css` are tuned for back-of-room readability after the JS scale transform.

Fix: delete the override. Component-scoped sizes (e.g. `.sr-box p`, `.paper-card .desc`) at `1.05–1.35rem` are fine; canonical tokens are off-limits.

### `.muted` takeaway / aside lines render tiny

Symptom: a gray `<p class="muted">` takeaway or aside line (e.g. *"Biased data in, biased decisions out"*) renders noticeably smaller than body text — sub-body prose, which Priority 0 bans.

Cause (historical, fixed 2026-06-22): canonical `reference/deck.css` `.muted` set `font-size: var(--fs-small)` (0.9rem — smaller even than `.small`). A deck's local `<style>` that redefined `.muted` for **color only** left that small canonical size in place, so every muted line shrank. `.muted` was undocumented in the type scale, so its size read as deliberate to some, as a violation to others.

Fix (applied repo-wide 2026-06-22): canonical `.muted` is now **color-only** (`color: var(--gray-text)`, no `font-size`), so muted lines inherit body size. De-emphasis is by color, not size (DESIGN_SYSTEM → Priority 0). Do **not** add a `font-size` to `.muted` in a deck's inline `<style>`; if a line is truly not worth body size, move it to `<deck>-note.html`. Distinct from inline `<em>` (also gray, also body size, since it inherits from its `<p>`). When the change grew old small-muted lines, a few dense slides overflowed — re-audit muted-bearing slides after any future change here.

### `.code-block` looks small or thin

Symptom: pseudocode on the slide is hard to read from the back of the room — too small, too light, or comments dissolve into the background.

Cause (historical, fixed 2026-04): early decks defined `.code-block` inline at `font-size: 0.85rem`, default weight, `'Courier New'` (a thin face), and used `#999` for comments (poor contrast on the `--light` background). The class is now canonical in `reference/deck.css` at 1.25rem / weight 500, with `Menlo`/`Consolas` ahead of `Courier New` in the font stack and `var(--gray-text)` for comments.

Fix: do **not** redefine `.code-block` in a deck's inline `<style>` — it's a canonical token. If existing decks still have the old definition, delete it; the canonical version takes over automatically.

---

## Overflow & the vertical budget

The px arithmetic behind all of these lives in `DESIGN_SYSTEM.md` → Priority 2 → **Vertical budget**. These entries are the ways the budget gets blown in practice.

### Aligned line-count budget

Symptom: a slide with two math-blocks plus 2–3 prose lines clips the brand footer.

Cause: each `aligned` line ≈ 50–60 px rendered; each `math-block` adds ~30 px of padding. Full px table: DESIGN_SYSTEM → Priority 2 → **Vertical budget**.

Fix: **at most one 3-line `aligned` block + one one-line `math-block` per content slide**. If two derivation steps both need 3 lines, split the slide. Don't shrink type (Priority 0) and don't squeeze vertical rhythm (Priority 2) — though on proof slides tight *specifically from math-block chrome*, the scoped Tight-margin recipe (DESIGN_SYSTEM → Math-heavy → Stacked equations) legitimately reclaims ~2×22 px.

### Underbrace labels eat ~30 px of vertical budget

Symptom: a slide with two stacked math-blocks plus a `.highlight` overflows past the brand-footer, even though "two math-blocks + highlight" was supposed to fit per the visual element budget.

Cause: each `\underbrace{expression}_{label}` adds the label height *below* the equation baseline — roughly 25–30 px of extra vertical real estate the planner forgot. Two underbraced math-blocks ≈ 60 px of hidden cost. Budgeted in DESIGN_SYSTEM → Priority 2 → **Vertical budget**.

Fix: treat each underbraced equation as ~110 px instead of ~80 px. If two underbraced math-blocks plus a highlight don't fit, inline one of the equations into prose (e.g., `Variances add: $(1-\bar\alpha-\sigma^2) + \sigma^2 = 1-\bar\alpha$.`) or drop one underbrace pair.

### Stacked-equation gap → collapse to one `aligned`

Symptom: two adjacent `math-block` divs feel disconnected; the eye reads them as separate ideas instead of two lines of one chain. Inverse symptom: a single equation that should land as a key conclusion gets buried inside an `aligned` block above.

Cause: `math-block` carries its own padding/margin; back-to-back blocks add up. `aligned` keeps lines tight via row-skip spacing, which is what stacked-but-related equations need.

Fix: one `math-block` with `\begin{aligned}` for related lines; a separate block only for a key conclusion (gap becomes signal). Rule, exception, and the scoped margin-reduction recipe for unavoidable adjacent blocks: DESIGN_SYSTEM → Math-heavy → Stacked equations.

### Footer collision via trailing exercise

Symptom: an inline `<p><strong>Exercise.</strong> …</p>` clips the brand footer, even though the slide previously rendered fine.

Cause: the slide already has 2 math-blocks + 2–3 paragraphs. The exercise paragraph is the straw that breaks the layout.

Fix: move the exercise to the *sibling slide that introduces the fact the exercise verifies*, not the slide that uses the fact. Example: a "matched-variance KL" exercise belongs on the slide where the KL term first appears (`L_{n-1}: Match Each Reverse Step`), not on the next slide that applies it. Pattern documented in `DESIGN_SYSTEM.md` → Recipes → Inline exercise.

### `\begin{cases}` clipped at right edge

Symptom: right column of cases (typically "otherwise") cut off.

Cause: math-block uses `$\displaystyle …$` with `white-space:nowrap; overflow-x:auto`. The forced layout overflows.

Fix: use `$$…$$` (display math) inside a plain `.math-block` — KaTeX sizes naturally. Shorten case labels: `m \in \text{top-}k` instead of long English; `\text{else}` instead of `\text{otherwise}`. If still doesn't fit → cut a bullet (Priority 2).

### Wide single-line math-block clips at right edge

Symptom: a `.math-block` extends past the slide right boundary or pushes the brand footer.

Cause: long single-line equations from `\quad`/`\qquad` separators stacking inseparable fragments, universal-quantifier preambles (`\forall S, \forall x`), or verbose annotations (`\text{(loss on } x\text{)}`).

Fix:
- **Drop universal quantifiers** when implicit from context (most theorem statements).
- **Use `,` not `\qquad`** to separate stacked definitions: `D_1 = D \cup \{x\}, \quad D_0 = D \setminus \{x\}` — not `\qquad`.
- **Drop side annotations** that the speaker can narrate (e.g., `(loss on $x$)` after `T(x) = \ell(f_\theta, x)`).
- **Cut the `- 0`** and similar always-true terms (`(\bar D - 0)/s` → `\bar D / s`).
- If still wide after compression, split into two `.math-block`s on consecutive lines, or split the slide.

### Tables with KaTeX in cells overflow horizontally

Symptom: a multi-column `<table>` with math (e.g., `$\max_c f_\theta(x)_c$`) extends past the slide right edge — sometimes past the slide rectangle entirely.

Cause: KaTeX widens cell content unpredictably; the browser can't compress columns past their math width. A 3rd column is often redundant.

Fix:
- **Cap at 2 columns** when KaTeX is in cells. If a 3rd column duplicates info from the first (e.g., "Signal" describing what "Test Statistic" already implies), merge or drop.
- **Cap at ~6 rows** total (header + 5 data). More → split or move the rest to the note file.
- A table is one exhibit. Adding `.math-block` + `.highlight` on the same slide breaks Priority 2 — see the visual element budget in `DESIGN_SYSTEM.md` → Priority 2.

### Tall image collides with `.cite` + brand footer

Symptom: a portrait figure rendered with `max-height: 540px` overlaps the citation line at the bottom of the slide; the cite text disappears under the image, or the image clips the brand footer.

Cause: `.cite` (bottom:18px, centered) and `.brand-footer` (bottom:18px, left) both sit absolutely positioned at the slide bottom. The flex column inside `.slide` doesn't reserve space for them — a tall image in the flow can extend right over them.

Fix:
- When a slide has both a tall figure AND a `.cite`, cap the image at `max-height: 470px` (leaves ~80 px clear for cite + footer breathing room).
- On the wrapping `.grid-2`, use `align-items: start` rather than `center`. With `center`, a 4-bullet column floats vertically halfway down a 470 px figure — reads as a void above the bullets and the figure-bullet pair stops aligning at the top.
- Image-with-bullets recipe: see DESIGN_SYSTEM → Recipes → Image + bullets.

---

## Prose & line breaks

### Full-sentence prose → rewrite to noun phrases

Symptom: bullets and card bodies read like paragraphs from a paper. Speaker re-reads instead of adding context.

Fix:
- **Drop narrative connectors.** "This means that X" → "X". "In other words, Y" → "Y". Delete "as we will see", "subsequently", "it is important to note".
- **Cut soft qualifiers.** "essentially", "actually", "basically", "indeed", "very", "quite", "fairly".
- **Compress to noun phrases.** "The attack achieves high precision, meaning most positive predictions are correct" → "High precision: most positives correct".
- **Keep technical specifics.** Variables, numbers, dates, author names, math.
- **Target ~40–60% word reduction** when rewriting an existing wordy deck. If you have to shrink the font to keep a bullet on one line, you haven't rewritten it yet.

After compression, strip any residual `class="small"` / `class="tiny"` / inline `font-size` overrides (Priority 0).

### Em-dashes break lines awkwardly → use colons / commas / parens

Symptom: `"X — Y"` wraps with the dash on its own line, or one clause orphans a single word.

Cause: em-dash (`—`), en-dash (`–`), and double-hyphen (`--`) are strong wrap points at slide font sizes.

Fix: rewrite the connector (colon / comma / period / parens) — rule in DESIGN_SYSTEM → Priority 1 ("Em-dash mid-sentence"). `lint-deck.py` flags mid-sentence dashes in prose; manual audit: `grep -nE ' — | -- | – ' <deck>.html` should be ~empty outside `.cite` lines and `h2` titles.

### Dangling single words at end of line

Symptom: a bullet ending in "…in <2 years" wraps "years" or "2 years" alone; an h3 reading "Architectural inductive biases" lands "biases" on line 2.

Fix, in order:
1. **Trust CSS first.** `text-wrap: pretty` / `balance` rebalance most orphans automatically.
2. **Remove em-dashes** in the line — most common structural cause.
3. **Shorten or restructure.** Trim a redundant qualifier, split, or reword.
4. **Glue with `&nbsp;`** — e.g., `in &lt;2&nbsp;years` so the last two tokens wrap together. Sparingly, only for technical phrases that must stay together.
5. **Never use `<br>` as orphan-shim.** Fragile across widths and prints oddly. (Priority 1 step 2 *does* permit `<br>` at a deliberate internal clause boundary inside one sentence — that's a different use.)

### `<br>` after a hyphen orphans the hyphen

Symptom: `Neyman-<br>Pearson` renders as `Neyman-` / `Pearson`. Trailing hyphen reads as a broken syllable.

Fix: keep the compound on one line (let the box grow), or rename to a hyphen-free label (`ML-as-a-Service` → `Cloud ML APIs`).

### Math-comma-math collision

Symptom: a sentence like "For large $N$, $N\sigma^2$ dominates" reads awkwardly during the talk. Listeners parse it as a single run-on math expression `$N, N\sigma^2$` rather than two clauses.

Cause: **not** "math after a comma" in general — math at the start of a clause is usually fine. The failure is *math-comma-math*: when the previous clause ends in a glyph and the next clause also begins with a glyph, they collide visually across the comma. Two adjacent symbols read as one expression.

Fix: insert a noun in the second clause, or restructure so the boundary isn't math-comma-math — rule and examples in DESIGN_SYSTEM → Priority 1 ("Math-comma-math"). If the previous clause ended in prose, math at the start of the next clause is fine — leave it alone.

### "Three ingredients:" → that prose belongs in the title

Symptom: a slide reads `<h2>The Attack Setup</h2>` then `<p>Three ingredients:</p>` then a `.grid-3` with 3 cards. The `<p>` is doing the work the title should do.

Cause: the title was written as a topic label (`"The Attack Setup"`) and the structural prose (`"Three ingredients:"`) was added to introduce the cards. They duplicate function.

Fix: make the structural prose the title — `<h2>Three Ingredients</h2>` — and delete the `<p>`. Saves a line and tightens the ghost-deck arc. Same pattern for `"Three steps:"` → `<h2>Three Steps</h2>`, `"Common test statistics:"` → `<h2>Common Test Statistics</h2>`, etc.

### Description duplicates diagram equations

Symptom: diagram labels show `$g_i = \nabla\ell(\theta; D_i)$` and the description on the other side of the slide repeats the same equation in plain English.

Fix: one artifact owns the math, the other owns the narrative. If the diagram has the equation, the description just says "local gradient".

---

## Citations

### Citation order: venue, not arXiv

Symptom: user corrects you — "the citation should read Author A, Author B, Author C" but you wrote "Author A, Author C, Author B".

Cause: arXiv preprints sometimes list authors in a different order than the official venue (PMLR / NeurIPS proceedings / journal). The arXiv abstract page or Google Scholar entry doesn't always match the canonical proceedings ordering. Authors do reshuffle.

Fix: when adding `.cite`, use the **venue's** listing (PMLR page, NeurIPS proceedings page, journal TOC), not the arXiv abstract page. Default format: `Authors (in venue order), "Title", Venue YYYY` — no arXiv ID unless explicitly requested. If unsure, ask before drafting.

### Citation wraps to two lines

Symptom: a `.cite` block wraps mid-title; the second line orphans a venue or year. Worse when two papers are joined with a `;` — the eye loses where one ends and the next begins.

Cause: `.cite` is centered and capped at 60% slide width. Long titles or two concatenated citations overflow that cap.

Fix: one dedicated line per citation; drop to the short form on dense slides; `.cite-left`/`.cite-right` escape hatches when the cap forces a wrap. Full rule and tiers: DESIGN_SYSTEM → Conventions → Citations.

### Paper-title cards steal half the slide → use `.cite`

Symptom: every paper-overview slide has a 2-column layout with the right column holding paper title + venue, ~50% of the slide for attribution alone.

Fix: delete the card. Replace with `<div class="cite">Author(s), "Title", Venue Year</div>` at the bottom. Don't wrap the title in `<em>` — `em` is gray, and gray-on-gray reads as mud. Keep the author `.pill` at the top as a recurring section label, but add `.cite` only on the paper-overview slide (not every follow-up).

---

## Diagrams & SVG

### SVG `max-width` silently shrinks the diagram

Symptom: the user says "make the diagram much larger", but the SVG already has `width="100%"` so it should fill its container.

Cause: `<svg ... style="max-width: 240px">` (or similar) caps the rendered size regardless of the column width. In a 600-px-wide column the SVG renders at 240 px and looks tiny.

Fix: remove `max-width` from the SVG. If you need to constrain size, put `max-width` on the wrapper `<div>` instead — the SVG inherits the wrapper's width, and the absolute-positioned KaTeX overlay spans (which use `top: %; left: %;` of the wrapper) keep their alignment.

### Wrapper with `max-width` only collapses to SVG intrinsic width

Symptom: an SVG with `style="display: block; width: 100%"` renders at a few hundred px instead of filling its wrapper. Labels positioned `top: %; left: %;` on the wrapper appear bunched in a tiny region.

Cause: the wrapper has `max-width: 1040px; margin: ... auto;` but no explicit `width`. Inside `.slide` (flex column with `align-items: center`), a child with no width sizes to its content; the SVG with `width: 100%` then sizes to the wrapper. The two enter a circular sizing dance and the browser falls back to the SVG's intrinsic dimensions (small).

Fix: put `width: 100%` on the wrapper alongside `max-width`. The wrapper now stretches to the slide's content width, capped at `max-width`, and the SVG fills it.

```html
<!-- yes -->
<div style="position: relative; width: 100%; max-width: 1040px; margin: 18px auto;">

<!-- no — wrapper collapses to SVG intrinsic -->
<div style="position: relative; max-width: 1040px; margin: 18px auto;">
```

If the wrapper hosts absolute-positioned KaTeX overlay spans (`top: %`, `left: %`) on top of an SVG with a fixed `viewBox`, also pin the wrapper's height: `height: NNNpx` matching the viewBox aspect ratio. Otherwise the wrapper height includes margin/padding noise and `top: 86%` no longer lands at SVG `y = 0.86·viewBoxH`.

### Concept SVG renders too small / labels unreadable

Symptom: an inline SVG diagram looks tiny and its labels are hard to read from the back row, even though it "fits" the slide.

Cause: wrapper `max-width` too low and/or `<text>` `font-size` too small for the viewBox. Widening the wrapper alone scales labels up proportionally — they stay small *relative to* the diagram.

Fix: bump BOTH. Full-width concept diagrams: wrapper `max-width: 820–920px`, `<text> font-size: 15–20`. Grid-column diagrams: `max-width: 360–440px`, `font-size: 13–16`. Primary labels bold. Policy in DESIGN_SYSTEM → Visual richness ("Make diagrams big").

### `.diagram-flow` inside `.cols` or `.grid-*` wraps ugly

Symptom: 3+ `.diagram-box` elements inside a 1/2 or 1/3-width column wrap onto multiple rows; combined with `<br>` in box labels (e.g., `Genomic<br>Databases`), boxes become 2-line cramped rectangles.

Cause: `.diagram-flow` is `display: flex; flex-wrap: wrap`. In a narrow container the boxes wrap; the `<br>` inside labels then stacks each box vertically. Result: a 2D mess.

Fix:
- **`.diagram-flow` always goes at full slide width** — never inside `.cols` or `.grid-*` or wrapped in a `.card` that lives in a column.
- Put bullets / prose above (full width), then `.diagram-flow` below (full width). Or vice versa.
- **Single-line labels in `.diagram-box`** — `Genomic DBs` not `Genomic<br>Databases`. If the label genuinely needs a second word, drop the `<br>` and let the box grow horizontally.
- For 4+ boxes that won't fit in one horizontal line at full slide width, switch to a vertical layout (one box per row) or split across slides.

---

## Proof & structure drift

### Outline ≠ Recap

Symptom: two near-identical bulleted slides — one before the steps and one after — both listing the same step labels. The recap adds nothing.

Cause: outline and recap serve different jobs. Outline previews step *labels* (a roadmap); recap shows the equation *chain* (the unified result).

Fix: recap = one `aligned` block with `\stackrel{(k)}{=}` labels — DESIGN_SYSTEM → Math-heavy → Multi-step proof pattern. Continuation slides use the `Proof (continued) — <paraphrase>` lead-in from the same section.

### Underbrace level mismatch

Symptom: an equation labels `\underbrace{\sum_n -\log\frac{p_\theta}{q}}_{\sum L_{n-1}}` — the underbrace covers the whole sum, the label is `\sum L_{n-1}`. The reader has to mentally undo the sum to see what one term is.

Cause: wrong abstraction level. The natural reasoning object is the per-step `L_{n-1}`, not the whole sum.

Fix: pull the `\sum` outside, label each summand — example in DESIGN_SYSTEM → Math-heavy → Underbrace labels.

### Algorithm slides drift → start centered, no side diagram

Symptom: an algorithm slide ends up as a 2-column layout with the algorithm on the left and a hand-drawn flow diagram on the right. The diagram repeats what's in the algorithm and gets cut on the next iteration.

Cause: the algorithm box is short, the slide feels empty, and the natural reflex is to fill the right side.

Fix: single styled box, centered; empty space below is fine. Full recipe (widths, counter CSS): DESIGN_SYSTEM → Recipes → Algorithm slide.

### Animation in live talks waits for the audience

Symptom: speaker is forced to pause for an animation loop.

Cause: SMIL `animateMotion` / CSS keyframe cycles dictate pacing the speaker doesn't control.

Fix: keep diagrams static with ①②③④ badges; speaker narrates the sequence. For **proof intuition build-ups**, use multi-slide progression instead of CSS animation — duplicate the slide N times, recolor one more step into Yonsei Blue per copy, leave upcoming steps in `--gray-text`. Speaker advances at their own pace; the audience gets the same build-up animation would have given, without the loop. Pattern documented in `DESIGN_SYSTEM.md` → Math-heavy → Build-up. Auto-cycling animation is fine only for self-paced web versions.

### Build-up slides flash on every advance

Symptom: a sequence of 4–7 slides differing only by a single quantity (Lloyd–Max iteration, proof-step coloring, table-cell update) feels jumpy / flickery on every click — each child element runs its own 0.06–0.30s staggered fadeIn.

Cause: the engine's `.slide.active > * { animation: fadeIn 0.4s ease both }` rule applies to every slide; identical content fading in from 0 → 1 looks like a flash when the only change between slides is one line of math.

Fix: define a per-deck `.<deck>-no-fade.active > * { animation: none !important }` rule and tag the build-up slides `class="slide <deck>-no-fade"`. Animations remain on every other slide; build-up sequences feel like stop-motion. Pattern documented in `DESIGN_SYSTEM.md` → Recipes → Build-up no-fade.

### Trimmed slide detail vanished → note file never received it

Symptom: after a "move the derivation to the note file" edit, the deck slide is lean but the paired `<deck>-note.html` doesn't contain the trimmed derivation — the content is simply gone.

Cause: the trim was made on the *assumption* the note file already covered it, without opening the note file to check.

Fix: whenever a deck slide is trimmed on "it's in the note" grounds, open the paired `-note.html` in the same edit and either confirm the content is there or migrate it in. Rule: DESIGN_SYSTEM → Companion note files → Migration check. If you find a past trim that lost content, recover it from git history (`git log -p -- <deck>.html`).

---

## Engine, navigation & audit false alarms

### "Page N" — what counts

Symptom: user says "page 9, the Toy Gaussian slide", but page 9 in the deck file is a section divider; the Toy Gaussian slide is page 10.

Cause: `deck.js` enumerates slides as `document.querySelectorAll('.slide')` — title, TOC, section dividers, content, recap, end-slide all count. The on-screen `slide-num` shows this position. Users sometimes mentally skip section dividers when referring to a slide.

Fix: when in doubt, re-confirm by content (h2 text), not number. Don't blindly edit "page N" — verify what's actually there. Add a short slide-number map to your scratchpad before diving in:
```
13: Lloyd-Max Initial
14: Lloyd-Max Step ① iter 1
…
```
Build the map with `grep -n 'class="slide' <deck>.html` (Nth match = page N), and rebuild it after any insertion/removal — see DESIGN_SYSTEM → Verifying without the toolchain.

### Duplicate page numbers → per-deck `.page-num` injector clashes with `.slide-num`

Symptom: two page numbers appear near the bottom of every slide.

Cause: the deck carries BOTH the canonical bold `.slide-num` (injected by `deck.js`) and a per-deck `<script>` at the end of `<body>` that injects a second `.page-num` element on each slide (older decks copied this from a sibling). Two indicators, two numbers.

Fix: keep the canonical bold `.slide-num` only. Delete the per-deck `.page-num` injector script and its `.page-num` / `.title-slide .page-num` CSS. See DESIGN_SYSTEM → Conventions → Page numbering ("One indicator only").

### Slide-num invisible despite being in the DOM

Symptom: `#slideNum` exists with the correct text content (`1 / 34`), but nothing is visible at the bottom-right of the deck.

Cause: prior to fix, `.slide-num` was a child of `.deck`, which carries `transform: translate(-50%, -50%) scale(N)`. Children of a transformed ancestor are clipped/scaled with it, and during the engine's initial scale calculation the slide-num could land outside the visible viewport rectangle even though its CSS position was bottom-right relative to the deck.

Fix (canonical, applied 2026-04): `deck.js` reparents `#slideNum` to `<body>` on init; `.slide-num` is `position: fixed; bottom: 12px; right: 22px; font-size: 1.2rem; font-weight: 700; color: var(--charcoal); z-index: 9999;`. This places the page number at the *true viewport* bottom-right, immune to any deck transform. Don't put `slide-num` back inside `.deck`.

### Stale `data-screen-label`

Symptom: the on-screen slide label says "Slide 7 — Forward process" but the deck has rearranged and slide 7 is now something else.

Fix: keep `data-screen-label` values in sync with actual slide position when inserting or removing slides. Not fatal, just confusing during review.

### Brand footer drifts → a slide opted out of `inset: 0`

Symptom: "Yonsei University" wordmark moves or disappears on specific slides.

Cause: that slide has inline `style="position:relative"`. Canonical `.slide` is `position: absolute; inset: 0` — overriding to `relative` breaks the fill, so the auto-injected `.brand-footer` lands somewhere unpredictable. Children with `position: absolute` already anchor to the slide; you don't need to force `relative`.

Fix: remove the `position:relative`. Anchor decorative content to `right`/`top` and leave bottom-left clear (~40 px) for the footer.

### Bottom-left is reserved for the brand footer

`deck.js` injects `.brand-footer` at `bottom:18px; left:28px` on every content slide. Decorative content absolute-positioned in the bottom-left corner collides with it.

Fix: anchor decorative content (images, floats, overlays) to `right` and/or `top`. Leave ~40 px clear in the bottom-left.

### `.no-footer` looks undefined but is a deck.js engine class

Symptom: an audit flags `class="slide end-slide no-footer"` as an unknown/undefined class — it appears in no CSS file — and someone "cleans it up".

Cause: `no-footer` is consumed by `reference/deck.js` (the brand-footer injector skips slides tagged with it), not by CSS. Every deck's closer uses it. Removing it makes the Yonsei wordmark appear on end slides.

Fix: leave it. When auditing for unknown classes, check `deck.js` as well as `deck.css` before deleting.

### Hex colors inside SVG attributes are house style, not violations

Symptom: an audit flags `fill="#003876"` / `stroke="#d94040"` in inline SVGs as "hardcoded colors" and proposes tokenizing them to `var(--…)`.

Cause: SVG *presentation attributes* (`fill=`, `stroke=`) cannot take CSS `var()` — only `style="fill: var(--…)"` can. The polished reference decks (lec01/lec02 of trustworthy-ai, the dp series) use hex in SVG attributes throughout, and `lint-deck.py` deliberately passes them. The hardcoded-color rule applies to HTML inline `style=` on prose/components, not SVG attribute values.

Fix: keep hex in SVG attributes, matched to the token values (`#003876` = `--yonsei-blue`, `#d94040` = `--warn`, `#2e8b57` = `--success`, `#666`/`#6b7280` = grays, `#e8ecf0` = `--slate`/light fill).

### Empty bottom half of slide is not a layout bug

Symptom: a slide with a sparse body (h2 + 1 paragraph + 1 short list) has 200+ px of empty space at the bottom. User says "use the empty space".

Cause: `.slide` is `display: flex; flex-direction: column;` with default `justify-content: flex-start;` — sparse content sits at top.

Fix, in priority order:
1. **Add structural content** that closes the slide: a math-block summarizing the chain, a `.highlight` capturing the takeaway, a recall card linking back to a prior definition. This is almost always what the user wants — they have a takeaway they hadn't surfaced.
2. Re-balance with `justify-content: center` only when the content is genuinely complete and you want it visually centered.
3. Avoid spacers / fake `<br>` rows (Priority 3 forbids middle voids; this one ban *includes* trailing pseudo-padding to fake balance).

---

## Toolchain: headless rendering, figures & bundling

**No toolchain at all?** If Chrome, `pdftoppm`, and `python3` are all absent and uninstallable (sandboxed container), don't skip verification — use the grep-based fallback: DESIGN_SYSTEM → **Verifying without the toolchain**. Flag the caveat to the user and recommend a real screenshot audit later.

### Image slide shrinks to ~55% in headless print only → print snapshot fired before images laid out

Symptom: in a large deck, a slide with an embedded raster figure renders scaled to ~55% and anchored top-left (wide white margins) in the **headless** `--print-to-pdf` output — and thus in the `/audit-and-edit-deck` screenshot pass. The slide is perfect in the browser, perfect in a manual `Cmd+P` → Save-as-PDF, and perfect when the same slide is rendered in a tiny throwaway deck.

Cause: **NOT the border, the image bytes, the DPI, the cache, or the markup** — all of those were ruled out by isolation (same image + same markup in a 2-slide test prints full-size). The real cause is timing: in a big deck (50+ slides, many KaTeX renders + several images), headless Chrome takes the print snapshot before every `<img>` has finished layout, so an unlaid-out image reports a wrong intrinsic size and Chrome scales the whole `@page` to "fit". A short `--virtual-time-budget` makes it worse.

Fix (render flags, not slide edits — the slide is fine):
```bash
"…/Google Chrome" --headless=new --incognito --user-data-dir=/tmp/fresh-$RANDOM \
  --virtual-time-budget=30000 --run-all-compositor-stages-before-draw \
  --print-to-pdf=deck.pdf --print-to-pdf-no-header "file://$(realpath deck.html)"
```
The `--virtual-time-budget=30000` (30s) + `--run-all-compositor-stages-before-draw` let images finish before the snapshot; the shrunk slide then renders full-size. **Do not "fix" the slide** (removing borders, shrinking the image, splitting) — that's chasing a render artifact. Confirm any suspected print-shrink in a manual Chrome `Cmd+P` first; if that's clean, it's this timing artifact and the deck ships fine. Audit tip: when a screenshot pass flags a whole-slide shrink on an image slide, re-render just that deck with the flags above before editing anything.

### Math prints in serif fallback (tofu `⋅`, plain-R `\mathbb{R}`) in headless render → fonts never fetched

Symptom: in a headless `--print-to-pdf` render, every math expression appears in a Times-like serif instead of KaTeX's Computer Modern; `\cdot` shows as a tofu box, `\mathbb{R}` as a plain italic R. Deck-wide, deterministic across re-renders, immune to `--virtual-time-budget`. Meanwhile another deck with identical head wiring prints true KaTeX fonts every time. `pdffonts deck.pdf` is the tell: only `LiberationSerif`/`LiberationSans` embedded, no `KaTeX_*`.

Cause: browsers fetch web fonts **lazily, per glyph laid out on the visible slide**. On screen only the `.active` slide is laid out, so a deck whose *title slide has no math* never requests any KaTeX face. `@media print` then exposes all slides at once, and the print snapshot races the just-triggered font fetches — fallback rendering gets baked into the PDF. A deck with math on slide 1 pre-loads `KaTeX_Main`/`KaTeX_Math` during normal load and prints fine, which is why the symptom looks deck-specific. (`--virtual-time-budget` doesn't help: at snapshot time the fonts' status is still `unloaded`, not `loading`, so there is nothing for the budget to wait on.)

Fix (canonical, applied 2026-08-09): `reference/deck.js` force-loads every declared `FontFace` at init (`document.fonts.forEach(f => f.load())`), so `document.fonts.ready` — and any virtual-time budget — genuinely covers them. If a deck bypasses canonical `deck.js`, wire the same one-liner in. Do not edit slide math to chase this; the markup is fine. Diagnostic: `pdffonts` on the output, or a `document.fonts.forEach(f => f.status)` probe via `--dump-dom`.

### Headless-Chrome render shows a stale image after you re-crop a figure

Symptom: you re-crop `figs/foo.png`, re-render the deck to PDF, and the slide still shows the OLD crop (e.g. a clipped caption) — even though opening `figs/foo.png` directly shows the corrected image.

Cause: Chrome caches `file://` image resources; a warm/reused profile serves the previous bytes.

Fix: render with a fresh throwaway profile and disabled cache, and kill stale Chrome first:
```bash
pkill -f "Google Chrome.*headless"
"…/Google Chrome" --headless=new --incognito --user-data-dir=/tmp/fresh-$RANDOM --disk-cache-size=1 \
  --virtual-time-budget=10000 --print-to-pdf=deck.pdf --print-to-pdf-no-header "file://$(realpath deck.html)"
```
When in doubt, verify the *source* `figs/*.png` with the Read tool — that's ground truth, not the cached slide render.

### Re-cropped paper figure still clipped → crop with headroom, then verify the file

Symptom: a cropped paper figure cuts off a label tab or an axis title at an edge.

Cause: the crop box hugged the content too tightly (the rounded "Prefix" tab or the "Number of duplicates" axis label sits a few px outside).

Fix: give the crop a few px of headroom on every side; render the source page at `-r 150`+, eyeball the box, crop with PIL/`sips`, then **Read the resulting `figs/*.png` directly** to confirm — do not trust the in-slide render (it may be cached; see above). Then re-cite the source figure number. Full capture protocol (caption cropping, figure-number citation, methodology-figure preference, `figs/` storage, DPI): DESIGN_SYSTEM → Visual richness → **Figure-capture protocol**.

### Standalone bundle bloat from full-resolution paper captures

Symptom: `bundle.py` produces a `<talk>.standalone.html` larger than ~10 MB — sometimes 40–60 MB.

Cause: paper figures captured at full PDF resolution (`pdftoppm -r 220` or higher) commonly land at 2000–3500 px wide. Base64-inlined into the standalone, each one bloats by ~33% over the raw PNG. Five of those in one deck pushes the bundle past 50 MB.

Fix:
- **Downsample paper-figure PNGs to ~1200 px max width** before bundling. They're going to render at 600–960 px on the slide anyway:
  ```bash
  sips --resampleWidth 1200 figs/big-figure.png --out figs/big-figure.png
  ```
- The authoring source (`<talk>/<talk>.html` reading `figs/*.png`) is unaffected — only the bundled distribution shrinks.
- After downsampling, re-run `python3 scripts/bundle.py <talk>/<talk>.html` and confirm slides still look sharp at projector zoom.
- Authoring decks with full-res captures are fine; the rule only applies before distributing the standalone.

### WebP works in `bundle.py`, but convert when you want a `.png` file

`scripts/bundle.py` inlines `.webp` natively (alongside `.png`, `.jpg`, `.svg`, `.gif`) — base64 data URI in the standalone bundle. So a deck with `<img src="cascade.webp">` bundles fine.

When you want an actual `.png` file (e.g., to preview outside the deck, share in a slack thread, or use in a Marp `<file>.md`-derived PDF), convert with macOS's `sips`:
```bash
sips -s format png input.webp --out input.png
```
No external tool needed; works on every recent macOS shell.
