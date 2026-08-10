# Pitfalls and lessons learned

Issues that have eaten debugging time. Search here before re-debugging — by symptom, not by topic.

**Division of labor**: this file is *symptom → cause → fix/pointer* for debugging. Normative authoring rules live in `DESIGN_SYSTEM.md` — when the two overlap, DESIGN_SYSTEM is canonical. At generation time read DESIGN_SYSTEM; come here when something looks wrong.

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

Symptom: a math-block on page N renders as raw `$$…$$` or random italics, **and every slide after page N is also garbled**.

Cause: KaTeX runs with `throwOnError: false`; a parse failure corrupts the auto-render walker's cursor for the rest of the document. Most common trigger: **literal `<` inside math parsed by the HTML lexer as a tag start** — `X_{<i}`, `\sum_{i<j}`, `0<D\le\sigma^2` — which silently swallows everything until the next `>`.

Diagnosis: `python3 scripts/lint-deck.py <deck>.html` errors on it, or grep:
```
grep -nE '\$[^$]*<[a-zA-Z]' <deck>.html
grep -nE '\$\$[^$]*<[a-zA-Z]' <deck>.html
```
Replace matched `<` with `&lt;`. Rarer triggers, same cascade: unbalanced `\begin{aligned}/\end{aligned}`, missing `&` alignment markers, a stray `$` in prose opening a phantom math span, mismatched `{}` — scan the math-blocks above the first visibly-broken slide.

### Parenthesized text renders as italic math → KaTeX delimiter escape bug

Symptom: `(learned or heuristic)` renders as italic `learnedorheuristic`; `[M]` in a token chip slants at the wrong height.

Cause: the KaTeX handler lives inside an HTML `onload="…"` attribute, so delimiter strings pass through HTML *and* JS string parsing and need **double** backslashes. With single `'\('` the JS parser eats the escape, leaving bare `(`, `)`, `[`, `]` as delimiters — every parenthesized phrase becomes inline math.

```html
<!-- correct: double backslash -->
{left:'\\(',right:'\\)',display:false},
{left:'\\[',right:'\\]',display:true}
```

Fix: match `reference/deck-skeleton.html` exactly. Audit: `grep -c "'\\\\(" *.html` — every deck should report ≥ 1.

### `$g_1$` shows as literal text → label is in SVG `<text>`

Symptom: math inside a diagram renders as literal `$g_1$`.

Cause: KaTeX auto-render does not descend into SVG text nodes.

Fix: build diagram structure in HTML (flex/grid divs), SVG only for arrows — patterns `.fl4-*` (slide 4), `.ldp-*` (slide 9), `.rdm-*` (slide 30) in `courses/privacy/lectures/01-dp/dp8-fl.html`. Math over a full SVG → absolute-positioned HTML spans: DESIGN_SYSTEM → Recipes → KaTeX overlays on SVG.

### Greek letters in table headers turn capital → `text-transform: uppercase` on `<th>`

Symptom: `$\gamma$` renders as Γ, `$\varepsilon$` as E, `$k\varepsilon$` as "KE" — in `<th>` cells only.

Cause: canonical `th` styling applies `text-transform: uppercase`, which reaches into the KaTeX spans.

Fix, in preference order: plain-word headers ("epsilon", "budget") with symbols defined in a `.muted` line above the table; move the math parameterization out of the header row; or wrap in `<span style="text-transform:none">…</span>`. `<td>` cells are unaffected.

### Italic prose collapses spaces → Yonsei has no italic face

Symptom: italic phrases read glued together ("all positions" → "allpositions").

Cause: the Yonsei TTFs are all `font-style: normal` and Noto Sans is loaded without italics; the browser synthesizes an oblique (~12° skew) with broken kerning/spacing.

Fix:
- Never `<i>` or `font-style: italic`. Canonical CSS sets `em` to `font-style: normal; color: var(--gray-text)` — the inline muted look, still body size. Whole subordinate line → `<p class="muted">`. Emphasis → `<strong>` (Yonsei Blue).
- In KaTeX, English words/phrases go inside `\text{…}` — bare words in math mode render as italic letter-runs with zero inter-word spacing. Single-letter identifiers staying italic is correct math typography.
- If *non-math* prose still renders italic, suspect the delimiter-escape bug above.

### Standalone bundle renders raw `$...$` strings

Symptom: `<deck>.standalone.html` shows literal `$...$` while the source deck renders fine.

Cause (fixed): `bundle.py`'s old `onload` regex treated either quote type as terminator, truncating the KaTeX config at the first inner `'`. Now `onload=(?:"([^"]*)"|'([^']*)')`.

Verify after bundling:
```
chrome --headless --dump-dom <standalone>.html | grep -c 'class="katex"'
```
should be ≥ 1 for any math deck.

---

## Fonts & canonical tokens

### Fonts look small → canonical tokens were shadowed

Symptom: a deck's body/headings render smaller than the Kangwook reference (`reference/kangwook*.png`) or a sibling deck.

Cause: a per-deck `<style>` redefined `p`, `li`, `h2`, `h3`, `.small`, `.tiny`, `.subtitle`, or `.math-block` `font-size`, shadowing `reference/deck.css`.

Fix: delete the override. Component-scoped sizes (`.sr-box p`, `.paper-card .desc`) at `1.05–1.35rem` are fine; canonical tokens are off-limits (DESIGN_SYSTEM → Priority 0).

### `.muted` takeaway / aside lines render tiny

Symptom: a gray `<p class="muted">` aside renders below body size — banned by Priority 0.

Cause (fixed): canonical `.muted` once set `font-size: var(--fs-small)` (0.9rem), so decks using `.muted` for color inherited the shrink.

Fix: canonical `.muted` is now **color-only** (`color: var(--gray-text)`, no `font-size`) — muted lines inherit body size. Never add a `font-size` to `.muted` in a deck `<style>`; a line not worth body size moves to `<deck>-note.html`. After any future change here, re-audit dense muted-bearing slides — grown lines can overflow.

### `.code-block` looks small or thin

Symptom: pseudocode unreadable from the back row — small, light, faded comments.

Cause (fixed): early decks defined `.code-block` inline at `font-size: 0.85rem`, default weight, `'Courier New'`, `#999` comments. Canonical `reference/deck.css` now sets 1.25rem / weight 500, `Menlo`/`Consolas` first, `var(--gray-text)` comments.

Fix: never redefine `.code-block` in a deck `<style>`; delete any old inline definition so the canonical version takes over.

---

## Overflow & the vertical budget

The px arithmetic lives in DESIGN_SYSTEM → Priority 2 → **Vertical budget**. Entries here are the recurring ways the budget gets blown.

### Aligned line-count budget

Symptom: two math-blocks plus 2–3 prose lines clip the brand footer.

Cause: each `aligned` line ≈ 50–60 px; each `math-block` adds ~30 px padding/margin.

Fix: at most **one 3-line `aligned` block + one one-line `math-block`** per content slide; a derivation with two 3-line steps gets two slides. Don't shrink type or squeeze rhythm. On proof slides tight specifically from math-block chrome, the scoped Tight-margin recipe (DESIGN_SYSTEM → Math-heavy → Stacked equations) reclaims ~2×22 px.

### Underbrace labels eat ~30 px of vertical budget

Symptom: two stacked math-blocks + `.highlight` overflow even though the element count fits the budget.

Cause: each `\underbrace{…}_{label}` adds ~25–30 px below the baseline — two underbraced equations ≈ 60 px of hidden cost.

Fix: budget underbraced equations at ~110 px, not ~80 px. If it doesn't fit: inline one equation into its prose line (`Variances add: $(1-\bar\alpha-\sigma^2) + \sigma^2 = 1-\bar\alpha$.`) or drop one underbrace pair and let the speaker name the terms.

### Stacked-equation gap → collapse to one `aligned`

Symptom: two related equations in adjacent `math-block`s read as separate ideas; or (inverse) a key conclusion is buried as the last row of an `aligned` block.

Fix: related lines → one `math-block` with `\begin{aligned}`; a key conclusion → its own block. Rule + the scoped margin-reduction recipe: DESIGN_SYSTEM → Math-heavy → Stacked equations.

### Footer collision via trailing exercise

Symptom: a trailing `<p><strong>Exercise.</strong> …</p>` clips the brand footer on a slide already carrying 2 math-blocks + 2–3 paragraphs.

Fix: move the exercise to the sibling slide that *introduces* the fact it verifies (e.g. a matched-variance KL exercise belongs on `L_{n-1}: Match Each Reverse Step`, not the summary slide that uses the fact). DESIGN_SYSTEM → Recipes → Inline exercise.

### `\begin{cases}` clipped at right edge

Symptom: the right column of a `cases` environment ("otherwise") is cut off.

Cause: the block was inline `$\displaystyle …$` inside a container with `white-space: nowrap; overflow-x: auto`.

Fix: use `$$…$$` in a plain `.math-block`; shorten case labels (`m \in \text{top-}k`, `\text{else}` instead of `\text{otherwise}`). Still too wide → cut a bullet from the slide (Priority 2).

### Wide single-line math-block clips at right edge

Symptom: a one-line `.math-block` passes the right slide boundary.

Cause: `\quad`/`\qquad`-joined fragments, quantifier preambles (`\forall S, \forall x`), verbose `\text{…}` annotations.

Fix:
- Drop universal quantifiers implicit from context.
- Join definitions with `,`/`\quad`, not `\qquad`: `D_1 = D \cup \{x\}, \quad D_0 = D \setminus \{x\}`.
- Drop side annotations the speaker can narrate (`(loss on $x$)`).
- Cut always-true terms (`(\bar D - 0)/s` → `\bar D / s`).
- Still wide → two `.math-block`s on consecutive lines, or split the slide.

### Tables with KaTeX in cells overflow horizontally

Symptom: a multi-column `<table>` with math in cells (`$\max_c f_\theta(x)_c$`) passes the right edge.

Fix: cap at **2 columns** when cells carry KaTeX (a 3rd column usually duplicates one of the others — merge or drop it); cap at ~6 rows (header + 5) — more → split the table or move rows to the note file. A table is one exhibit: adding `.math-block` + `.highlight` around it breaks the element budget (DESIGN_SYSTEM → Priority 2).

### Tall image collides with `.cite` + brand footer

Symptom: a portrait figure at `max-height: 540px` overlaps the citation or clips the footer.

Cause: `.cite` (bottom: 18px, centered) and `.brand-footer` (bottom: 18px, left) are absolutely positioned — the flex column doesn't reserve space for them.

Fix: with a figure AND a `.cite`, cap the image at `max-height: 470px` (~80 px clearance). Use `align-items: start` on the wrapping `.grid-2` — with `center`, bullets float halfway down the tall figure (void above, misaligned tops). Recipe: DESIGN_SYSTEM → Recipes → Image + bullets.

---

## Prose & line breaks

### Full-sentence prose → rewrite to noun phrases

Symptom: bullets read like paper paragraphs; the speaker re-reads the slide.

Fix: drop narrative connectors ("This means that X" → "X"; delete "as we will see", "it is important to note"); cut soft qualifiers ("essentially", "actually", "basically", "indeed", "very", "quite", "fairly"); compress to noun phrases ("The attack achieves high precision, meaning most positive predictions are correct" → "High precision: most positives correct"); keep all technical specifics (variables, numbers, dates, author names, math). A wordy deck typically compresses 40–60% without content loss. Then strip residual `class="small"` / `class="tiny"` / inline `font-size` (Priority 0).

### Em-dashes break lines awkwardly → use colons / commas / parens

Symptom: `"X — Y"` wraps with the dash orphaned at a line edge.

Cause: em/en-dashes and `--` are strong wrap points at slide font sizes.

Fix: rewrite the connector — rule in DESIGN_SYSTEM → Priority 1 ("Em-dash mid-sentence"). `lint-deck.py` flags them; manual audit: `grep -nE ' — | -- | – ' <deck>.html` should be ~empty outside `.cite` lines and `h2` titles.

### Dangling single words at end of line

Fix order: 1. trust `text-wrap: pretty`/`balance` (already canonical); 2. remove em-dashes; 3. shorten or restructure the phrase; 4. glue with `&nbsp;` (`in &lt;2&nbsp;years`) sparingly; 5. **never** `<br>` as orphan-shim — a deliberate internal clause break is a different, permitted use (DESIGN_SYSTEM → Priority 1).

### `<br>` after a hyphen orphans the hyphen

Symptom: `Neyman-<br>Pearson` renders as `Neyman-` / `Pearson`.

Fix: keep the compound on one line (let the box grow) or rename hyphen-free (`ML-as-a-Service` → `Cloud ML APIs`).

### Math-comma-math collision

Symptom: "For large $N$, $N\sigma^2$ dominates" reads as one expression spanning the comma.

Cause: not math-after-comma in general — specifically the previous clause *ends* in math and the next *begins* with math.

Fix: insert a noun in the second clause or restructure the boundary — DESIGN_SYSTEM → Priority 1 ("Math-comma-math"). Prose-then-math ("the noise floor $N\sigma^2$…") is fine; don't churn those.

### "Three ingredients:" → that prose belongs in the title

Symptom: `<h2>The Attack Setup</h2>` + `<p>Three ingredients:</p>` + `.grid-3` — the paragraph does the title's job.

Fix: fold the count into the title (`<h2>Three Ingredients</h2>`), delete the paragraph. Same for "Three steps:", "Common test statistics:".

### Description duplicates diagram equations

Symptom: a diagram label reads `$g_i = \nabla\ell(\theta; D_i)$` and the adjacent description restates the same equation.

Fix: one artifact owns the math, the other owns the narrative ("local gradient").

---

## Citations

### Citation order: venue, not arXiv

Symptom: user corrects the author order of a citation.

Cause: arXiv listings sometimes differ from the official venue ordering.

Fix: use the venue's listing (PMLR page, NeurIPS proceedings, journal TOC). Format: `Authors (in venue order), "Title", Venue YYYY` — no arXiv ID unless explicitly requested. Unsure → ask.

### Citation wraps to two lines

Symptom: a `.cite` wraps mid-title, or several `;`-joined papers blur into a gray blob.

Cause: `.cite` is centered and capped at 60% width.

Fix: one dedicated line per citation; short form on dense slides; `.cite-left` / `.cite-right` escape hatches when the centered cap forces a wrap. Full rules: DESIGN_SYSTEM → Conventions → Citations.

### Paper-title cards steal half the slide → use `.cite`

Symptom: a paper-overview slide gives ~50% of its area to a right-column card holding just title + venue.

Fix: delete the card; `<div class="cite">Author(s), "Title", Venue Year</div>` at the bottom. No `<em>` around the title (gray-on-gray is mud). Keep the author `.pill` as a section label; the `.cite` appears only on the paper-overview slide, not every slide of the section.

---

## Diagrams & SVG

### SVG `max-width` silently shrinks the diagram

Symptom: "make the diagram larger" but the SVG already has `width="100%"`.

Cause: `<svg style="max-width: 240px">` caps rendered size regardless of column width.

Fix: remove `max-width` from the SVG; constrain the wrapper `<div>` instead — overlay spans are positioned in `%` of the wrapper, so wrapper-level sizing keeps labels aligned.

### Wrapper with `max-width` only collapses to SVG intrinsic width

Symptom: an SVG with `width: 100%` renders only a few hundred px wide; overlay labels bunch in a tiny region.

Cause: the wrapper has `max-width: 1040px` but no `width`; inside `.slide` (flex column, `align-items: center`) it sizes to content, falling back to the SVG's intrinsic width.

Fix: give the wrapper `width: 100%` alongside `max-width`:

```html
<!-- yes -->
<div style="position: relative; width: 100%; max-width: 1040px; margin: 18px auto;">
```

With overlay spans over a fixed-viewBox SVG, also pin the wrapper `height: NNNpx` to match the viewBox aspect ratio, so `top: 86%` lands at `y = 0.86 · viewBoxH`.

### Concept SVG renders too small / labels unreadable

Cause: wrapper `max-width` too low and/or SVG `<text>` `font-size` too small; widening the wrapper alone leaves labels proportionally small.

Fix: bump BOTH. Full-width diagram slides: wrapper `max-width: 820–920px`, `<text>` `font-size: 15–20` (viewBox units). Grid-column diagrams beside bullets: `max-width: 360–440px`, `font-size: 13–16`. Primary labels bold. DESIGN_SYSTEM → Visual richness ("Make diagrams big").

### `.diagram-flow` inside `.cols` or `.grid-*` wraps ugly

Symptom: 3+ `.diagram-box` in a narrow column wrap into cramped 2-line rectangles.

Cause: `.diagram-flow` is `display: flex; flex-wrap: wrap`; `<br>` inside labels stacks boxes taller.

Fix: `.diagram-flow` at full slide width only (bullets go above or below, full width); single-line labels (`Genomic DBs`, no `<br>`); 4+ boxes that don't fit one line → vertical layout or split the slide.

---

## Proof & structure drift

### Outline ≠ Recap

Symptom: near-identical bulleted slides before and after a proof's steps.

Cause: the outline previews step *labels*; the recap must show the equation *chain*.

Fix: recap = one `aligned` block with `\stackrel{(k)}{=}` labels — DESIGN_SYSTEM → Math-heavy → Multi-step proof pattern. Continuation slides use `Proof (continued) — <paraphrase>`.

### Underbrace level mismatch

Symptom: `\underbrace{\sum_n -\log\frac{p_\theta}{q}}_{\sum L_{n-1}}` — the label sits at the wrong abstraction level.

Fix: pull `\sum` outside the underbrace and label each summand — example in DESIGN_SYSTEM → Math-heavy → Underbrace labels.

### Algorithm slides drift → start centered, no side diagram

Symptom: an algorithm slide sprouts a redundant right-column flow diagram to fill space.

Fix: a single styled box, centered; empty space below is fine (Priority 3). DESIGN_SYSTEM → Recipes → Algorithm slide.

### Animation in live talks waits for the audience

Symptom: the speaker pauses awkwardly for an animation loop to come around.

Cause: SMIL `animateMotion` / CSS keyframes dictate pacing instead of the speaker.

Fix: static diagrams with numbered badges (①②③④); proof build-ups → multi-slide progressions (recolor one step per copy, upcoming steps in `--gray-text`) — DESIGN_SYSTEM → Math-heavy → Build-up. Auto-cycling is acceptable only for self-paced web decks.

### Build-up slides flash on every advance

Symptom: a 4–7-slide build-up flickers on each click.

Cause: the engine's `.slide.active > * { animation: fadeIn 0.4s ease both }` restaggers every child on entry.

Fix: per-deck `.<deck>-no-fade.active > * { animation: none !important }` on the build-up slides only — DESIGN_SYSTEM → Recipes → Build-up no-fade.

### Trimmed slide detail vanished → note file never received it

Symptom: content trimmed from a slide "because it belongs in the note file" isn't in the note file — it's gone.

Cause: the trim was made on assumption; the note file was never opened.

Fix: confirm-or-migrate in the same edit — DESIGN_SYSTEM → Companion note files → Migration check. Recover past losses from `git log -p -- <deck>.html`.

---

## Engine, navigation & audit false alarms

### "Page N" — what counts

Symptom: the user's "page 9" is a section divider; the slide they mean is page 10.

Cause: `deck.js` counts `document.querySelectorAll('.slide')` — title, TOC, dividers, content, recap, end-slide all included, shown as `(current+1) / total`. Users mentally skip dividers.

Fix: re-confirm the target by content (`h2` text), not number. Build a scratchpad map with `grep -n 'class="slide' <deck>.html` (Nth match = page N, title = 1); rebuild after every insertion/removal.

### Duplicate page numbers → per-deck `.page-num` injector clashes with `.slide-num`

Symptom: two page numbers per slide.

Cause: the deck has both the canonical `.slide-num` (from `deck.js`) and an old per-deck `.page-num` injector script copied from a sibling.

Fix: keep `.slide-num`; delete the injector script and its `.page-num` / `.title-slide .page-num` CSS. DESIGN_SYSTEM → Conventions → Page numbering.

### Slide-num invisible despite being in the DOM

Symptom: `#slideNum` holds the correct text but nothing shows bottom-right.

Cause: it was a child of the transformed `.deck`, so it got scaled/clipped with the slides.

Fix (canonical): `deck.js` reparents `#slideNum` to `<body>`; `.slide-num` is `position: fixed; bottom: 12px; right: 22px; font-size: 1.2rem; font-weight: 700; color: var(--charcoal); z-index: 9999;`. Don't move it back inside `.deck`.

### Stale `data-screen-label`

Symptom: a slide's `data-screen-label` says "Slide 7 — Forward process" after rearrangement.

Fix: keep the labels in sync when inserting/removing slides. Confusing during audits, not fatal.

### Brand footer drifts → a slide opted out of `inset: 0`

Symptom: the wordmark moves or disappears on specific slides.

Cause: an inline `style="position:relative"` on the slide breaks the canonical `.slide` rule (`position: absolute; inset: 0`).

Fix: remove the inline override — absolutely-positioned children already anchor to the slide.

### Bottom-left is reserved for the brand footer

`deck.js` injects `.brand-footer` at `bottom: 18px; left: 28px` on every content slide. Anchor decorative content to `right`/`top` edges; leave ~40 px clear at bottom-left.

### `.no-footer` looks undefined but is a deck.js engine class

Symptom: an audit flags `no-footer` as unknown (it appears in no CSS file) and removes it → the wordmark reappears on end slides.

Cause: `no-footer` is consumed by `reference/deck.js` (the footer injector skips tagged slides), not by CSS.

Fix: leave it. Check `deck.js` as well as `deck.css` before deleting "unknown" classes.

### Hex colors inside SVG attributes are house style, not violations

Symptom: an audit flags `fill="#003876"` / `stroke="#d94040"` as hardcoded colors.

Cause: SVG presentation attributes can't take `var()` — only `style="fill: var(--…)"` can. Reference decks use hex there; `lint-deck.py` passes them. The hardcoded-color rule targets HTML inline `style=`, not SVG attributes.

Fix: keep hex values matched to tokens: `#003876` = `--yonsei-blue`, `#d94040` = `--warn`, `#2e8b57` = `--success`, `#666`/`#6b7280` = grays, `#e8ecf0` = `--slate`/light fill.

### Empty bottom half of slide is not a layout bug

Symptom: a sparse slide leaves 200+ px empty at the bottom; the user says "use the space".

Cause: `.slide` is a flex column with `justify-content: flex-start` — sparse content sits at the top.

Fix order: 1. add structural content that closes the slide (a summarizing math-block, a `.highlight` takeaway, a recall card) — usually what the user actually wants; 2. `justify-content: center` only when the content is genuinely complete; 3. never spacers or fake `<br>` rows (Priority 3 — including trailing pseudo-padding).

---

## Toolchain: headless rendering, figures & bundling

**No toolchain at all?** If Chrome, `pdftoppm`, and `python3` are confirmed absent and uninstallable, verify with the grep-based fallback (DESIGN_SYSTEM → **Verifying without the toolchain**), flag the caveat in your report, and recommend a real audit later.

### Image slide shrinks to ~55% in headless print only → print snapshot fired before images laid out

Symptom: in a 50+-slide deck, a raster-figure slide renders at ~55% scale, anchored top-left, in headless `--print-to-pdf` (and thus in `/audit-and-edit-deck` screenshots) — but is perfect in the browser and in manual `Cmd+P`.

Cause: NOT the slide's border/bytes/DPI/cache/markup (each isolation-tested and eliminated). Headless Chrome takes the print snapshot before every `<img>` finishes layout; an unlaid-out image reports a wrong intrinsic size and Chrome scales the `@page` to fit. A short `--virtual-time-budget` makes it worse.

Fix (render flags, not slide edits):

```bash
"…/Google Chrome" --headless=new --incognito --user-data-dir=/tmp/fresh-$RANDOM \
  --virtual-time-budget=30000 --run-all-compositor-stages-before-draw \
  --print-to-pdf=deck.pdf --print-to-pdf-no-header "file://$(realpath deck.html)"
```

**Do not "fix" the slide.** Confirm in manual `Cmd+P` first; if clean there, it's this artifact. When an audit report flags a whole-slide shrink on an image slide, re-render with these flags before touching the deck.

### Math prints in serif fallback (tofu `⋅`, plain-R `\mathbb{R}`) in headless render → fonts never fetched

Symptom: headless PDF shows all math in a Times-like serif; `\cdot` renders as tofu, `\mathbb{R}` as a plain italic R. Deterministic, immune to `--virtual-time-budget`. Tell-tale: `pdffonts deck.pdf` lists only `LiberationSerif`/`LiberationSans` — no `KaTeX_*` faces.

Cause: browsers load fonts lazily per glyph on the *visible* slide; a deck whose title slide has no math never requests the KaTeX faces. `@media print` exposes all slides at once and the snapshot races the fetches. More budget doesn't help — the fonts are `unloaded`, not `loading`.

Fix (canonical): `reference/deck.js` force-loads every declared `FontFace` at init (`document.fonts.forEach(f => f.load())`), so `document.fonts.ready` genuinely covers them. Decks bypassing canonical `deck.js` must wire the same one-liner. Don't edit slide math. Diagnostics: `pdffonts` on the output, or `document.fonts.forEach(f => f.status)` via `--dump-dom`.

### Headless-Chrome render shows a stale image after you re-crop a figure

Symptom: you re-cropped `figs/foo.png` and re-rendered, but the slide still shows the old crop.

Cause: Chrome caches `file://` images in a warm profile.

Fix:

```bash
pkill -f "Google Chrome.*headless"
"…/Google Chrome" --headless=new --incognito --user-data-dir=/tmp/fresh-$RANDOM --disk-cache-size=1 \
  --virtual-time-budget=10000 --print-to-pdf=deck.pdf --print-to-pdf-no-header "file://$(realpath deck.html)"
```

When in doubt, Read the source `figs/*.png` directly — the file on disk is ground truth.

### Re-cropped paper figure still clipped → crop with headroom, then verify the file

Symptom: a crop cuts off a label tab or axis title.

Cause: the crop box hugged the visible content too tightly — tabs and axis titles sit a few px outside the apparent bounding box.

Fix: leave a few px headroom on every side; render the source page at `-r 150`+, crop with PIL/`sips`, then **Read the resulting `figs/*.png`** (never trust a possibly-cached in-slide render); re-cite the figure number. Full protocol: DESIGN_SYSTEM → Visual richness → **Figure-capture protocol**.

### Standalone bundle bloat from full-resolution paper captures

Symptom: `bundle.py` output exceeds ~10 MB, sometimes 40–60 MB.

Cause: full-resolution captures (`pdftoppm -r 220`+, 2000–3500 px wide) bloat ~33% under base64; five such figures push a deck past 50 MB.

Fix:
- Downsample to ~1200 px max width before bundling (slides render figures at 600–960 px anyway):

  ```bash
  sips --resampleWidth 1200 figs/big-figure.png --out figs/big-figure.png
  ```

- The authoring source is unaffected — downsample only before distributing.
- Re-run `python3 scripts/bundle.py <talk>/<talk>.html` and confirm the figure still reads sharply at projector zoom.

### WebP works in `bundle.py`, but convert when you want a `.png` file

`bundle.py` inlines `.webp` natively (alongside `.png`, `.jpg`, `.svg`, `.gif`). When you need an actual `.png` (external preview, Slack upload, Marp PDF pipeline):

```bash
sips -s format png input.webp --out input.png
```

Built into macOS — no ImageMagick needed.
