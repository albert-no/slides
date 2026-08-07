# Talks design system

Normative rules and recipes for slide decks. **Audience**: academic conference talks and master-level lectures. **Mode**: math-heavy — rigorous theorem statement, rigorous proof, plus a high-level intuition pass. **Visual**: minimal — short abstract phrases, never full sentences. Applies to custom HTML decks and the Marp template; when they disagree, `reference/deck.css` wins.

**Division of labor.** This file is the canonical *how to author* reference. `GOTCHAS.md` is the *symptom → cause → fix* debugging reference. When both cover a topic, this file is canonical. Read this file when writing or editing; go to GOTCHAS when something looks wrong.

**Source files.** `reference/colors_and_type.css` (font-face + CSS tokens), `reference/deck.css` (engine + components), `reference/deck.js` (scale / nav / footer injection). Decks `<link>` to these — never duplicate.

**Reference target.** Kangwook Lee's BLISS deck (<https://kangwooklee.com/talks/2026_03_BLISS/bliss_seminar.html>; captures in `reference/kangwook1.png`–`kangwook4.png`) is the minimum acceptable visual weight. If a deck renders smaller, suspect a per-deck `<style>` shadowing the canonical tokens — see GOTCHAS.

---

## Quick reference

| What I want to do | Where to look |
|---|---|
| Start a new deck / order the slides | Deck anatomy |
| Pick a deck to imitate for a genre | Deck anatomy → Exemplars |
| Predict overflow before rendering | Priorities → Vertical budget |
| Verify a deck when Chrome/poppler/python3 are missing | Verifying without the toolchain |
| Map "page N" to a slide | Conventions → Page numbering |
| Add a content slide | Recipes → Content slide |
| State a theorem rigorously | Math-heavy → Theorem |
| Show a proof rigorously / continue one | Math-heavy → Proof |
| Show proof intuition (color, build-up) | Math-heavy → Intuition + Build-up |
| Bracket a multi-step proof | Math-heavy → Multi-step proof pattern |
| Introduce a parameterized formula (DDIM-style) | Math-heavy → Recipe-first derivation |
| Stack two related equations | Math-heavy → Stacked equations |
| Squeeze math-block margins on a tight proof slide | Math-heavy → Stacked equations → Tight-margin recipe |
| Substitute variables back into a result | Math-heavy → Substitution |
| Label terms in a long equation | Math-heavy → Underbrace labels |
| State a prerequisite before deriving from it | Math-heavy → Recall before derive |
| Inline / display math | Recipes → Math slide |
| Add an exercise next to its content | Recipes → Inline exercise |
| Show an algorithm cleanly | Recipes → Algorithm slide |
| Show code / pseudocode | Recipes → Code / pseudocode block |
| Visualize a chain / dependency | Recipes → Chain diagram |
| Put a figure next to bullets | Recipes → Image + bullets |
| Let a dense figure breathe (own slide) | Recipes → Image-first / description-follows |
| Overlay math labels on an SVG | Recipes → KaTeX overlays on SVG |
| Add a visual (or mark one as TODO) | Visual richness |
| Capture a real paper/blog figure (preferred over redrawing) | Visual richness → Figure-capture protocol |
| No citable figure exists — build an original concept diagram | Visual richness → source 2 (concept diagrams) |
| Move detail off the slide | Companion note files |
| Formal math for a concept-first course | Technical supplement decks |
| Cite a paper (format, venue order, position) | Conventions → Citations |
| Section divider / TOC / Title / Closer | Recipes |
| Diagram with math labels | Recipes → Diagram (HTML + SVG arrows) |
| Make a diagram dominate the slide | Recipes → Diagram dominates |
| Build-up of nearly identical slides | Recipes → Build-up no-fade |
| Recall a definition the audience may have forgotten | Recipes → Recall card |
| Trace a debugging symptom | `GOTCHAS.md` |

---

## Priorities (ranked, non-negotiable)

When rules conflict, lower number wins. These four are the spine of every authoring and editing decision.

### 0. Font sizes — strongest rule

Important content (audience must read it during the talk) → body size. Non-important content → companion `<deck>-note.html` file, *not* shrunk to fit.

- The canonical scale is `reference/deck.css`. Don't redefine `p`, `li`, `h1`, `h2`, `h3`, `.subtitle`, `.cite`, `.small`, `.tiny`, or `.math-block` `font-size` in a deck's inline `<style>`. Don't put inline `style="font-size:…"` on prose.
- `.tiny` is banned everywhere. `.small` on prose (paragraphs, list items, captions, anything inside `.highlight` / `.card` / `.cols` / `.grid-*` / `.math-block` / under a `<table>`) is banned.
- Exactly two on-slide slots permit sub-body text: `<div class="cite">` citations, and `.small` inside a diagram (only when the label is a non-crucial sub-label *and* compression breaks the layout).
- **De-emphasis is by color, not size.** A subordinate aside or takeaway line (`<em>`, `<p class="muted">`) stays at **body size** and renders gray — it is still read during the talk. `.muted` is a *color-only* class (canonical in `reference/deck.css`); never give it a reduced `font-size`, and don't reach for `.small`/`.tiny` to "tone a line down". A line not worth body size belongs in `<deck>-note.html`, not shrunk on the slide.
- Component-internal text (pill labels, token chips, code blocks) stays at its native compact size — these are design tokens, not author overrides.
- When a slide feels cramped, **cut content or split the slide**. There is no slide budget.

### 1. Density — 7×7 rule + abstract phrases

**Hard ceiling: 7×7.** ≤ 7 visual lines per slide, ≤ 7 words per line. Soft target: ≤ 40 words of body text per content slide.

**Phrases, not sentences.** Telegraphic noun phrases. Drop narrative connectors ("this means…", "in other words…", "essentially", "actually"). Drop soft qualifiers ("very", "quite", "fairly"). Speaker narrates; the slide is a visual anchor. This applies to `h2` titles too — short and abstract (3–6 words), not action-title sentences.

**Math is not prose.** A theorem statement, definition, or equation in a `.math-block` doesn't count toward the 40-word ceiling. The ceiling keeps prose lean — math earns its space.

**One claim per line.** When a paragraph, `<li>`, `.highlight`, or `.card` carries multiple distinct claims joined by periods, split each into its own `<p>` (or convert the run to a `<ul>` if there are 3+ short claims). Two assertions that look like one sentence read as one idea — the audience won't track both. This applies inside `.highlight` / `.card` too: separate `<p>` siblings, not concatenated sentences.

**Math-comma-math — anti-pattern.** Starting a clause with math is usually fine. The specific failure is when the *previous* clause also *ended* in math: "For large $N$, $N\sigma^2$ dominates" — the two glyphs sit on either side of the comma and the eye reads them as one continuous expression ($N, N\sigma^2$). Insert a noun in the second clause ("the second term $N\sigma^2$ dominates") or restructure so the boundary isn't math-comma-math.

**Em-dash mid-sentence — anti-pattern.** "X is a sparsifier — pruning emerges" wraps awkwardly at slide font sizes; the dash often orphans alone on a line. Replace with a colon plus `<br>` (one deliberate internal break is allowed by step 2 below) or split into two `<p>` tags. Em-dashes are only safe when part of a technical glyph (`7–8B`, `fill-in-the-middle`) or inside `.cite` lines and `h2` titles like "Proof — MGF bound".

**Numerical anchors next to closed-form formulas.** When a slide states a closed-form `R(D)`, `D(R)`, or any quantity-as-function, pin a concrete number for the running example next to it: `$R(D) = 1 - H_b(D)$, &nbsp;$R(\tfrac14) \approx 0.189$ bits` reads in one glance. The audience reads the formula; the speaker says the number; both belong on the slide.

**When prose visibly wraps, fix in this order:**

1. **Compress.** Most overflow is wordiness, not a layout problem. Collapse to noun phrases.
2. **Split** at a natural sentence/colon/independent-clause boundary into two adjacent `<p>` tags. `<br>` only at a deliberate internal clause break (rare).
3. **Glue inseparable phrases with `&nbsp;`** reactively when the browser visibly breaks one — article+noun (`a&nbsp;dataset`), preposition+object (`in&nbsp;the&nbsp;model`), number+unit (`7B&nbsp;parameters`).
4. **Never break within a phrase.** `<br>` as orphan-shim is banned (see GOTCHAS).

### 2. Overflow — content stays in bounds

Content must fit inside 1280×720 and clear the auto-injected `.brand-footer` at bottom-left (~40 px reserved). Footer collision is overflow even if text is inside the slide rectangle.

When something overflows: compress (Priority 1) → split the slide → move secondary detail to `<deck>-note.html`. **Never** shrink type. **Never** compress vertical rhythm (`margin`, `padding`, `line-height`) on prose. Discipline is upstream — write short phrases from the first draft.

For multi-slide proofs, a "(continued)" `h2` plus a one-line recap is the canonical recovery — see Math-heavy → Proof.

**Visual element budget.** A content slide gets `h2` + `divider` + at most **5 child elements**. A `.math-block` counts as 1 (taller than a prose line). A `<table>` counts by row count (header + N data rows). A `.highlight` counts as 1 regardless of internal `<p>` count. **If a slide carries `.math-block` + `<table>` + `.highlight` together, it's already over budget — split before previewing.** This rule predicts overflow without rendering; honor it at draft time.

**Vertical budget (px arithmetic).** When the element budget is ambiguous, sum the rendered heights. Rule-of-thumb costs (all approximate; canonical numbers are what the browser renders):

| Element | Vertical cost |
|---|---|
| `h2` + `.divider` header block | ~110 px |
| One prose line (`p` / `li` at body size) | ~40 px |
| `.math-block`, single line | ~80 px (equation ~50 px + ~30 px padding/margin) |
| Each additional `aligned` row | +50–60 px |
| `\underbrace` under an equation | +25–30 px per equation |
| `<table>` row (header or data) | ~55 px |
| `.highlight` (one short line) | ~70 px |
| `.card` wrapper | +~30 px over its content |
| Image | by layout: 470 px solo · 380–430 px beside bullets · 320–380 px stacked (see Recipes → Image + bullets) |
| Bottom reserve (`.brand-footer`, plus `.cite` if present) | ~40 px / ~80 px |

Budget available for body content: 720 px − slide padding (56 top + 48 bottom) − header block − bottom reserve ≈ **430–470 px**. Worked example: a 3-line `aligned` block (~200 px) + a 1-line `math-block` (~80 px) + two prose lines (~80 px) + a `.highlight` (~70 px) ≈ 430 px — exactly at the edge, which is why the ceiling is *at most one 3-line `aligned` block + one one-line `math-block` per slide*. Anything beyond that sum: split the slide.

### 3. Empty space — no middle voids

Empty space at the *bottom* of a slide is fine. Empty space *in the middle* is not.

- Don't pad with `<div class="spacer*">`. Trust natural element margins.
- Don't wrap 2–3-line content in `.cols + .card` — `.cols { flex: 1; align-items: stretch }` makes short cards stretch into tall hollow boxes. Use `.grid-2` (no flex stretch) with bare `<h3>` + `<p>` for short dichotomies.
- If a slide is too sparse to hold itself, merge or expand. Never pad.

### Style rules (informed by priorities)

1. **One idea per slide.** And **one exhibit** — one chart, table, diagram, theorem, proof chunk, or equation block per slide. If two seem needed, ask: one comparison (combine) or two points (two slides)?
2. **Speaker narrates; slide is a visual anchor.** Telegraphic phrases over sentences.
3. **Prose emphasis.** `**strong**` → Yonsei Blue. `*em*` → muted gray (never italic — see GOTCHAS). A whole subordinate line → `<p class="muted">` — same gray, still body size (de-emphasis by color, not size; Priority 0).
4. **Key insight** → `<div class="highlight">` (HTML) or `>` blockquote (Marp). Max one per slide.
5. **Math.** Inline `$…$`, display `$$…$$` inside `<div class="math-block">`.
6. **Paper attribution** → `<div class="cite">` footnote at the bottom, never a side card. One dedicated line per citation; two length tiers by slide density. Full rules: Conventions → Citations.
7. **Ghost deck test.** Read only the `h2` titles in sequence. They should outline the lecture arc clearly. If they don't, fix the outline before drafting bodies. Titles stay short and abstract — not full sentences.
8. **Spell out acronyms on first appearance.** The first slide that introduces a method/metric must expand the acronym inline — `SSCD (Self-Supervised Copy Detection)`, `RTA (Random Token Addition)`, `MV / RV / TV (Matching / Retrieval / Template Verbatim)`. After that, the bare acronym is fine. Applies to per-deck acronyms; canonical ones the audience already knows (LLM, MIA, DP, KL, MSE) don't need expansion. The expansion goes in the slide body where the term first appears, not in a separate glossary slide.
9. **Visual-first — aim for a visual on every slide (default).** Prefer a diagram, figure, chart, schematic, or worked-math block over a text-only slide. When drafting, ask "what's the picture?" before "what are the bullets?". Full policy: **Visual richness**. This does not override rule 1 — visual-rich means *a* visual, not a collage.
10. **Self-contained slides (independent modules).** In a multi-lecture course where slides may be reordered or reused, each slide must stand on its own. Drop forward/backward course references — no "next week", "previously", "(Wk N)", "see Lecture 3", "as we saw". State the point on the slide itself. The only place a week index belongs is a syllabus / course-map slide.

---

## Verifying without the toolchain (no-render fallback)

The canonical verification loop is: headless Chrome → PDF → `pdftoppm` → PNG → visual read (`/audit-and-edit-deck`), plus `python3 scripts/lint-deck.py` / `find-wordy.py` / `outline-lint.py`. **Always prefer that pipeline when it works.** Some agent environments have none of it — no Chrome, no poppler, no `python3`, and no way to install anything (no sudo, no package manager, no alternative rasterizer like `mutool`, `convert`, `magick`, or `gs`). Confirm absence first (`command -v google-chrome pdftoppm python3 mutool convert gs`); only then use this fallback.

1. **Slide map by grep, never memory.** `grep -n 'class="slide' <deck>.html` lists every `.slide` div in document order. "Page N" = the Nth match, counting from 1 at the title slide (Conventions → Page numbering). Build the map fresh into your scratchpad, and rebuild it after every insertion/removal — never trust remembered or previously-quoted line numbers.
2. **Overflow by arithmetic, not rendering.** Apply the Priority 2 vertical-budget table to every slide you touch: sum the px costs of the body elements; anything past ~430–470 px must be split *now*, not "checked later". The element budget (≤5 children; `.math-block` + `<table>` + `.highlight` = over budget) is the fast pre-filter.
3. **Lint by targeted grep**, replacing `lint-deck.py`:
   - **Balanced divs:** `grep -o '<div' <deck>.html | wc -l` vs `grep -o '</div>' <deck>.html | wc -l`. A mismatch is a structural break — bisect slide by slide.
   - **Literal `<` inside math** (garbles every later slide): `grep -nE '\$[^$]*<[a-zA-Z]' <deck>.html` and `grep -nE '\$\$[^$]*<[a-zA-Z]' <deck>.html`. Replace hits with `&lt;`.
   - **KaTeX delimiter escape:** `grep -c "'\\\\(" <deck>.html` must be ≥ 1 (double-backslash delimiters in the onload handler; see GOTCHAS).
   - **Unknown classes:** extract the deck's `class="…"` names and cross-check against `reference/deck.css`, the deck's own `<style>`, *and* `reference/deck.js` (`no-footer` is an engine class that lives only in JS).
   - **Banned type:** `grep -n 'class="[^"]*tiny' <deck>.html`; `.small` on prose; inline `font-size` on `p`/`li`/`h2`/`h3`.
   - **Mid-sentence dashes:** `grep -nE ' — | -- | – ' <deck>.html` — should hit only `.cite` lines and `h2` titles.
   - **`$` inside SVG `<text>`:** grep the SVG regions for `$` — KaTeX never renders there.
4. **OUTLINE checks without `outline-lint.py`:** for each `file:line` pointer you touched, `sed -n '<N>p' <file>` and confirm the line still holds the claimed content.
5. **Flag the caveat.** This fallback cannot catch visual overlap, squashed math spacing (`\!` pulling glyphs together), drifted SVG overlays, or genuine rendering surprises. When you ship work verified only this way, say so explicitly to the user and recommend a real screenshot audit (`/audit-and-edit-deck`) once the tooling is available.

---

## Deck anatomy

Canonical slide order for a full deck:

1. **Title slide** (`.title-slide`) — logo, `.pill` talk-type, h1, subtitle, speaker line.
2. **TOC** (`.toc-list`) — required when the deck has **3+ sections**; skip for short talks (≲15 slides) and technical supplements.
3. **Sections** — `.section-slide.left` numbered divider, then that section's content slides. Use the centered `.bg-accent` variant only for dramatic interludes / statement slides, not structural breaks.
4. **Recap** (optional, math decks) — the equation-chain recap (Math-heavy → Multi-step proof pattern), not a re-bulleted outline.
5. **Closer** — `.end-slide` Q&A, tagged `no-footer`.

Section dividers and the TOC must agree: same section names, same order, numbered `01`-style. The ghost-deck test (Style rule 7) applies to the whole arc.

**Slide-count norms** (each `<div class="slide">` counts, including title/TOC/dividers; build-up progressions inflate the count — a 5-slide build-up is one idea):

| Format | Slides | Shipped anchor |
|---|---|---|
| 5-min conference video | ~10 | `talks/icml2026/` (9) |
| Invited / conference talk (30–45 min) | 30–40 | `talks/kics260521dllm/` (35), `talks/math260624dllm/` (32) |
| Graduate lecture (~75 min) | 35–70 | `diffusion2-ddpm` (35), `watermark` (38), `lossy1-foundations` (67, heavy build-ups) |
| Undergrad lecture (90 min, concept-first) | 60–90 | `trustworthy-ai/lec02` (85) |
| Technical supplement | 4–25, proportionate to the math | `lec02tech` (22) |

### Exemplars — deck to imitate per genre

| Genre | Imitate |
|---|---|
| Math-heavy graduate lecture (theorem/proof/intuition) | `courses/privacy/lectures/02-generative/diffusion2-ddpm.html` |
| Undergrad concept-first lecture | `courses/trustworthy-ai/lec02-privacy-dp.html` |
| Inline HTML+SVG concept diagrams | `courses/trustworthy-ai/lec01-introduction.html`, `lec02-privacy-dp.html` |
| Diagram with math labels (HTML boxes + SVG arrows) | `courses/privacy/lectures/01-dp/dp8-fl.html` (`.fl4-*`, `.ldp-*`, `.rdm-*`) |
| Research / invited talk | `talks/kics260521dllm/kics260521dllm.html` |
| 5-min recorded video | `talks/icml2026/icml2026.html` |
| Technical supplement | `courses/trustworthy-ai/lec02tech.html` |
| Speaker-script note file | any `courses/trustworthy-ai/lecNN-*-note.html` |
| Minimum acceptable visual weight | Kangwook BLISS captures (`reference/kangwook1.png`–`kangwook4.png`) |

Before drafting a new deck, open the exemplar for its genre and match its rhythm — section length, exhibit density, build-up pacing. Budget each planned slide against the Vertical budget (Priority 2) at draft time, not after.

---

## Tokens

### Color

| Token | Value | Generic use |
|---|---|---|
| `--yonsei-blue` | `#003876` | Primary accent: `strong`, dividers, list bullets, h2 underline. |
| `--blue-light` | `#1a5296` | Secondary accent: cards, pill outlines. |
| `--accent` | `#005baa` | Tertiary; use sparingly. |
| `--charcoal` | `#1a1a1a` | Body text. |
| `--gray-text` | `#666666` | Muted (`em`, `.cite`, subtitles). AA at ≥14px. |
| `--slate` | `#e8ecf0` | Borders, table rules. |
| `--light` / `--subtle` | `#f4f6f9` | Card / math-block / divider-slide background. |
| `--white` | `#FFFFFF` | Slide background. |
| `--success` | `#2e8b57` | `ul.check`, `.token-safe`. |
| `--warn` | `#d94040` | `.token-eos`. |

**Color in math contexts** (one role per color, applied consistently across the deck):

| Color | Math meaning |
|---|---|
| `--yonsei-blue` | What's being introduced / the active step / the term to focus on |
| `--charcoal` | Established / given / already proved |
| `--gray-text` | Future / not yet proven / parenthetical aside |
| `--success` | Equality that closes a chain / final claim |
| `--warn` | Counterexample / where standard argument breaks |

Never recolor for decoration. Pick once, apply consistently — color carries semantic load only when it's stable.

### Typography

`'Yonsei', 'Noto Sans', Arial, sans-serif`. Yonsei TTFs declared via `@font-face` in `colors_and_type.css`. No italic face exists — see GOTCHAS.

| Role | Size | Weight | Line height |
|---|---|---|---|
| `h1` | 3.6rem (4rem on title, 4.2rem on left-section) | 700 | 1.08 |
| `h2` | 2.7rem | 700 | 1.12 |
| `h3` | 1.85rem | 700 | 1.22 |
| body `p`, `li` | 1.55rem | 300–400 | 1.5 |
| `.subtitle` | 1.75rem (1.9rem on title) | 300 | — |
| `.cite` | 0.85rem | — | — |
| `.small` | 1.15rem | — | (gated — see Priority 0) |
| `.tiny` | 0.95rem | — | (banned — see Priority 0) |
| `.muted` | = body (inherits) | 300–400 | gray aside — **color only, never a size step** |
| `.code-block` | 1.25rem | 500 (kw 700, fn 600) | 1.6 |

`text-wrap: balance` on `h1`/`h2`/`h3`/`.subtitle`; `text-wrap: pretty` on `p`/`li`/`.small`/`.tiny`. Don't override.

### Spacing & misc

- Slide padding `56px 72px 48px` (title slide `72px 88px`). Don't change — anchors print layout.
- Border radius: `12px` (card), `10px` (diagram-box), `8px` (math-block, highlight, pre), `6px` (token), `3.667em` (pill).
- Spacers (`.spacer-sm`/`.spacer`/`.spacer-lg`) — almost never useful. See Priority 3.
- Viewport: fixed 1280×720, scaled via JS `transform`. Same for `@page` print size.
- Motion: `fadeIn` 0.4s on every direct child of `.slide.active`, staggered 0.06–0.30s. Disabled in print. Don't override, except per-deck no-fade on build-up sequences (Recipes → Build-up no-fade). **No other animation language** — proof build-ups use multi-slide progressions, not CSS keyframes (Math-heavy → Build-up).

---

## Components

Every class below is defined in `reference/deck.css`. Reuse — don't invent.

**Containers** — `.slide`, `.title-slide`, `.section-slide`, `.section-slide.left`, `.end-slide`.

**Backgrounds** — `.bg-light` (subtle gray), `.bg-accent` (Yonsei blue, white text, inverts component defaults; reserve for section dividers and statement slides).

**Building blocks** — `.card`, `.highlight` (max one per slide), `.pill` / `.pill-fill`, `.divider`, `.math-block`, `.code-block` (with `.kw` / `.fn` / `.cm` / `.str` for syntax tokens), `.diagram-flow` / `.diagram-box` (full slide width only — never inside a column; see GOTCHAS), `.cite` (+ per-deck `.cite-left` / `.cite-right` escape hatches), `.brand-footer` (auto-injected).

**Token chips** — `.token-mask` / `-gen` / `-fixed` / `-eos` / `-safe` / `-pad` / `-pad2` / `-pad3`.

**Layout** — `.cols`, `.col-2-3` / `.col-1-3`, `.grid-2`, `.grid-3`.

**Lists** — `ul` (default blue dot), `ul.check` (green ✓), `ul.arrow` (blue →), `ul.num` (numbered badge).

**TOC slide** — `.toc-list` / `.toc-item` / `.toc-num` / `.toc-rule` / `.toc-label` / `.toc-sub`.

**Engine UI** (auto-injected by `deck.js`, hidden in print) — `.progress-bar`, `.slide-num`. The `no-footer` class is consumed by `deck.js` (skips brand-footer injection), not CSS — don't "clean it up".

For exact CSS — padding, border, hover, `.bg-accent` inversion — read `reference/deck.css`. Don't paraphrase here.

---

## Math-heavy talks (theorem / proof / intuition)

The repo's primary mode. Three slide types and one pairing pattern.

### Theorem

Rigorous statement. Assumptions, claim, citation. Use a `.card` with an inline label (`<h3>Theorem N (Author, Year).</h3>`) and place the assertion in a `.math-block`.

```html
<div class="slide">
  <h2>Concentration of empirical mean</h2><div class="divider"></div>
  <div class="card">
    <h3>Theorem (Hoeffding, 1963).</h3>
    <p>Let $X_1, \dots, X_n$ be independent with $X_i \in [a_i, b_i]$. For $t > 0$:</p>
    <div class="math-block">$$\Pr\!\left[\bar X_n - \mathbb{E}\bar X_n \ge t\right] \le \exp\!\left(-\tfrac{2 n^2 t^2}{\sum_i (b_i - a_i)^2}\right).$$</div>
  </div>
  <div class="cite">Hoeffding, "Probability Inequalities for Sums of Bounded Random Variables", JASA 1963.</div>
</div>
```

### Proof

Rigorous derivation, one logical step per visual line. Multi-slide if it doesn't fit at body size — never shrink (Priority 0).

**Continuation slides.** The lead line names both the continuation *and* the move that continues, in the template:

```
Proof (continued) — <short paraphrase of the continuing step>
```

e.g. `<h2>Proof (continued) — Divide by the marginal</h2>`, `<h2>Proof (continued) — Optimize the free parameter</h2>`. Below the `h2`, one brief recap line of where the chain stands, then the new math. Don't ship a bare `Proof (continued)` heading — the paraphrase is what lets a reader landing mid-proof reorient.

```html
<div class="slide">
  <h2>Proof — MGF bound</h2><div class="divider"></div>
  <div class="math-block">$$\Pr[\bar X_n - \mathbb{E}\bar X_n \ge t]
    = \Pr\!\left[e^{s n (\bar X_n - \mathbb{E}\bar X_n)} \ge e^{snt}\right]
    \le e^{-snt}\, \mathbb{E}\!\left[e^{s n (\bar X_n - \mathbb{E}\bar X_n)}\right].$$</div>
  <p>Markov, then independence, then optimize $s > 0$. <em>(next: bound each factor)</em></p>
</div>
```

### Intuition

High-level picture. One visual metaphor; speaker narrates the geometry. This is where color and (controlled) build-up pay off.

```html
<div class="slide">
  <h2>Why concentration is exponential</h2><div class="divider"></div>
  <div class="cols">
    <div>
      <p><strong>Each $X_i$:</strong> small wiggle.</p>
      <p><strong>Average of $n$:</strong> wiggles cancel.</p>
      <p><strong>Rate:</strong> exponential, not polynomial.</p>
    </div>
    <div><!-- HTML+SVG sketch of tail decay --></div>
  </div>
</div>
```

### Pairing pattern

For results the audience must really understand:

1. **Intuition** (1 slide) — picture, geometry, why we should expect the result.
2. **Theorem** (1 slide) — rigorous statement.
3. **Proof** (1–N slides) — rigorous derivation.
4. **Discussion** (optional) — what's tight, what generalizes.

For results the audience just needs to know exists, theorem-only is fine; cite the proof.

### Build-up for proof intuition (controlled "animation")

Auto-cycling animation is banned for talks (speaker loses pacing — see GOTCHAS). For proof intuition, use **progressive slides** instead: duplicate the slide N times; on slide $k$, color the first $k$ steps with Yonsei Blue (active/established) and the remaining steps with `--gray-text` (upcoming). Speaker advances at their own pace; the audience sees the build-up animation would have given, without the loop.

```html
<!-- Step k of N for the same idea slide -->
<div class="slide">
  <h2>Why Hoeffding works (2 of 4)</h2><div class="divider"></div>
  <ol class="num">
    <li style="color:var(--charcoal)">Markov on the moment-generating function</li>
    <li style="color:var(--yonsei-blue)"><strong>Independence factors the MGF ← here</strong></li>
    <li style="color:var(--gray-text)">Bound each factor (Hoeffding's lemma)</li>
    <li style="color:var(--gray-text)">Optimize the free parameter $s$</li>
  </ol>
</div>
```

Use the math-context color table above. One color = one role across the whole deck. Tag the sequence with the no-fade class (Recipes → Build-up no-fade) so advancing doesn't flash.

### Stacked equations belong in one block

Two related equations stacked vertically → single `<div class="math-block">` with `\begin{aligned}`, **not** two adjacent `math-block` divs. Adjacent blocks introduce too much vertical gap; the eye reads them as separate ideas instead of two lines of one chain.

```html
<!-- yes: tight stacking -->
<div class="math-block">$$\begin{aligned}
  X^{(0)} &= X, \\
  X^{(n)} &= X^{(n-1)} + Z^{(n)}.
\end{aligned}$$</div>

<!-- no: too much gap, reads as two unrelated equations -->
<div class="math-block">$$X^{(0)} = X.$$</div>
<div class="math-block">$$X^{(n)} = X^{(n-1)} + Z^{(n)}.$$</div>
```

**Exception**: when the second equation is a *key conclusion* deserving its own moment (final result, closing claim), promote it to its own `math-block` so it lands separately from the working math above. The visual gap then becomes signal, not noise.

**Tight-margin recipe (scoped margin reduction).** Each `.math-block` carries ~30 px of vertical padding/margin; two adjacent blocks ≈ 60 px of dead space, often exactly what pushes a closing `.highlight` or the footer clearance over the edge. When a slide is tight *specifically because of math-block chrome* (typical on dense proof slides), reduce the margins — at the narrowest scope that covers the problem:

1. **One slide, one or two blocks:** inline `style="margin: 8px 0;"` on each affected `.math-block`.
2. **Several flagged slides in one deck:** define a scoped per-deck class in the deck's `<style>` and tag only those slides:

   ```html
   <style>
     .d3-tight .math-block { margin: 8px 0; }
   </style>
   <div class="slide d3-tight">…</div>
   ```

Never touch the global `.math-block` rule in `reference/deck.css`, and never apply the tight class deck-wide by default — margin reduction is a targeted rescue for proof-math slides, not a new baseline. If the slide is still over budget after tightening, split it (Priority 2).

### Multi-step proof pattern

For derivations that span 4+ logical steps, bracket the sequence. Definitions precede roadmaps; recap is a chained equation, not a re-listed bullet summary.

1. **Setup** — define variables and the problem (one slide).
2. **Outline** — show the *target* (e.g., the Bayes formula we're about to simplify) in a `math-block`, followed by an `<ol>` of the step labels. This previews the path.
3. **Step 1 … Step k** — one logical step per slide, body math at body size. Continuation slides use the `Proof (continued) — <paraphrase>` template above.
4. **Recap** — a single `aligned` block showing the unified equation chain, with each step labeled above its relation symbol via `\stackrel{(k)}{=}` or `\stackrel{(k)}{\approx}`. Don't reuse the bulleted outline as a recap — outline previews step *labels*, recap shows the equation *chain*.

```html
<!-- Recap form -->
<div class="math-block">$$\begin{aligned}
  P_{X|Y}(x|y)
    &= \frac{P_{Y|X}(y|x)\,P_X(x)}{P_Y(y)} \\
    &\stackrel{(1)}{\approx}\; \tfrac{P_{Y|X}\,[P_X(y) + P'_X(y)(x-y)]}{P_Y(y)} \\
    &\stackrel{(2)}{\approx}\; P_{Y|X}\!\left[1 + \tfrac{P'_X(y)}{P_X(y)}(x-y)\right] \\
    &\stackrel{(3)}{\approx}\; \cdots \\
    &\stackrel{(4)}{=}\; \mathcal{N}(\mu_*, \sigma^2)(x).
\end{aligned}$$</div>
```

**Recap label choice — descriptive over numeric.** Numeric `\stackrel{(k)}{=}` cross-references step slides — useful when the steps were big and named. But when the *algebraic move* on a relation symbol is itself non-obvious (e.g., "split $g^2/2 = g^2 - g^2/2$", "use $\partial p = (\partial \log p)\,p$", "factor $-\partial_x$"), label that move directly so the recap is self-contained:

```latex
\partial_t p_t
  &\stackrel{(\text{FFP})}{=}\; -\partial_x(f\,p_t) + \tfrac{g^2}{2}\,\partial_x^2 p_t \\
  &\stackrel{(\text{split})}{=}\; -\partial_x(f\,p_t) + g^2\,\partial_x^2 p_t - \tfrac{g^2}{2}\,\partial_x^2 p_t \\
  &\stackrel{(\partial p\,=\,\partial\log p\cdot p)}{=}\; \cdots
```

Use `\text{...}` to keep the label in upright Roman; keep each label under ~25 characters so it doesn't widen the relation symbol's column. Mix-and-match is fine — numeric where a step needs a callback, descriptive where the move is the explanation.

### Recipe-first derivation

When introducing a parameterized formula whose specific shape isn't obvious (DDIM's $\mu_n = \sqrt{\bar\alpha_n}\,X^{(0)} + \sqrt{1-\bar\alpha_n-\sigma^2}\,\epsilon_{n+1}$, score-network reparameterizations, …), don't open with the formula and prove that it works. Open with a **recipe** carrying named unknowns, **derive the unknowns** from the property you want, then **read off** the resulting parameterization.

Three-slide arc:

1. **Recipe.** State the construction with placeholders for the unknown coefficients. Use `\underbrace` to label each ingredient (signal / recycled / fresh, or whatever the decomposition is). Identify what you'll determine.
2. **Constraint.** Impose the property you actually want (variance budget, marginal match, normalization). One equation per unknown ⇒ solve. Surface the *free* parameters explicitly.
3. **Read-off.** Substitute the solved coefficients back; convert from the recipe to the standard form (e.g., the conditional density).

The student sees *why* the formula has its specific shape — every coefficient came from a constraint, none was hand-picked. Reverse order ("here's the formula, now let's verify it has the right marginal") teaches the algebra but obscures the design intent. Don't apply when the formula has a clean independent motivation (Bayes' rule, KL, an established theorem) — recipe-first is for parameterizations whose form is otherwise opaque.

### Substitution

When applying an abstract result by relabeling variables, show the abstract form first, then the substitution arrow, then the concrete form. Don't jump straight to the substituted form — the reader loses sight of which result you're invoking.

```html
<p>Step 4 result, with $X = \tilde X^{(n-1)}$ and $Y = \tilde X^{(n)}$:</p>
<div class="math-block">$$X\,|\,Y \;\sim\; \mathcal{N}(Y + \sigma^2\partial_y \log P_X(Y),\; \sigma^2).$$</div>
<p>Substitute $X \to \tilde x^{(n-1)}$, $Y \to \tilde x^{(n)}$:</p>
<div class="math-block">$$\tilde x^{(n-1)} = \tilde x^{(n)} + \sigma^2\,\partial \log P_{X^{(n)}}(\tilde x^{(n)}) + \tilde z^{(n)}.$$</div>
```

### Underbrace labels

Use `\underbrace{...}_{\text{name}}` to label parts of a long equation in place. **Label the per-term operand, not the whole sum**: a `\sum_n` over labeled terms is more useful than a single label on the whole sum, because the label names the per-step object the reader will reason about later.

```latex
%% yes: sum is outside, each summand labeled
\sum_{n=2}^{N} \underbrace{\bigl(-\log\tfrac{p_\theta}{q}\bigr)}_{L_{n-1}}

%% no: wrong abstraction level — `\sum L_{n-1}` is not the natural object
\underbrace{-\sum_{n=2}^{N} \log\tfrac{p_\theta}{q}}_{\sum L_{n-1}}
```

Budget note: each underbrace adds ~25–30 px below the equation baseline — count it in the Vertical budget (a common hidden-cost overflow; see GOTCHAS).

### Recall before derive

When deriving B from A, state A first as a self-contained fact (own paragraph + `math-block`), *then* derive B. Don't refer to A in a trailing parenthetical or "where …, known in closed form since $A$" clause — that hides the prerequisite under the consequence and the reader has to re-parse.

```html
<!-- yes: A first, B derived from it -->
<p>Conditional forward marginal (closed form):</p>
<div class="math-block">$$q(X^{(n)}|X^{(0)}) = \mathcal{N}(\sqrt{\bar α_n}\,X^{(0)},\; 1-\bar α_n).$$</div>
<p>Hence the reverse posterior is also Gaussian:</p>
<div class="math-block">$$q(X^{(n-1)}|X^{(n)}, X^{(0)}) = \mathcal{N}(\mu_n, \beta_n).$$</div>

<!-- no: prerequisite tucked in a trailing clause -->
<p>The reverse posterior is Gaussian:</p>
<div class="math-block">$$q(\cdots) = \mathcal{N}(\mu_n, \beta_n),$$</div>
<p>where $\mu_n$ uses the conditional score, known in closed form since $q(X^{(n)}|X^{(0)}) = \mathcal{N}(\ldots)$.</p>
```

---

## Conventions

### Page numbering

The on-screen `slide-num` indicator (and any user reference to "page N") counts **every** `<div class="slide">` element in document order — title slide, TOC, section dividers, content slides, recap, end-slide all included. `deck.js` enumerates them with `querySelectorAll('.slide')` and shows `(current+1) / total`. When the user says "page 23", count from 1 starting at the title.

When you edit, match slides by content (`<h2>` text, distinctive class), not position — slide numbers shift the moment you insert or remove anything. Treat the page number as a navigation hint, not a stable identifier. Without the render toolchain, build the page↔slide map with `grep -n 'class="slide' <deck>.html` (Verifying without the toolchain).

**One indicator only — the bold `.slide-num`.** The canonical page number is the bold `.slide-num` (`deck.js` injects/updates it; styled `position: fixed; bottom-right; font-weight: 700`). Do **not** also add a per-deck `<script>` that injects a second `.page-num` element on each slide (some older decks copied one from a sibling) — two indicators render as duplicate page numbers. If a deck has both, delete the `.page-num` injector script and its `.page-num` / `.title-slide .page-num` CSS; keep the bold `.slide-num`. (The on-screen indicator is hidden in print/PDF by `@media print`, which is expected.)

### Citations

`<div class="cite">…</div>` format: `Authors (in venue order), "Title", Venue YYYY` — no arXiv ID unless explicitly requested. Use the **venue's** author order (PMLR / NeurIPS / JMLR / journal proceedings page), not arXiv's, since they sometimes differ. `et al.` is acceptable for 4+ authors after first reference; spell out all authors on the first slide that introduces a paper.

```html
<!-- yes -->
<div class="cite">Isik, Weissman, and No, "An Information-Theoretic Justification for Model Pruning", AISTATS 2022.</div>

<!-- no: arXiv-only attribution -->
<div class="cite">Isik et al., arXiv:2102.08329.</div>
```

**One dedicated line per citation.** Each citation must render on a single line of the slide (`.cite` is centered, capped at 60% width). If a slide cites two papers, each gets its own line — joined inside one `.cite` with `<br>`, or as two adjacent `.cite` blocks. Never let a citation wrap mid-title.

```html
<div class="cite">
  Hoffmann et al., "Training Compute-Optimal LLMs" (Chinchilla), NeurIPS 2022.<br>
  Carlini et al., "Quantifying Memorization Across Neural Language Models", ICLR 2023.
</div>
```

**Two length tiers** by slide density:

- **Theorem / lemma slide** — full citation: `Author et al., "Title", Venue YYYY.`
- **Abstract-bullet slide** — short form: `Author et al., NameOrAcronym, Venue YYYY.` (e.g., `Rafailov et al., DPO, NeurIPS 2023.`). Use when the slide is dense and the full title would wrap.

**Position rule.** The citation lives at the **bottom** of the slide. The constraints, in priority order:

1. Citation stays inside the slide rectangle (no horizontal clipping).
2. Citation does not overlap body text or images above.
3. Citation does not overlap the auto-injected `.brand-footer` at bottom-left (~28 px from corner, ~180 px wide).

When the default centered 60% cap forces a wrap, escape hatches — pick the lightest that satisfies the three constraints:

- `class="cite cite-left"` — left-aligned, full-width (capped at 92%), `bottom: 48px` so it clears the brand footer. Use when the citation is long but the slide isn't dense on the right.
- `class="cite cite-right"` — right-aligned, full-width (capped at 92%), `bottom: 18px`. Use only when the slide's lower-left region must stay clear (rare).

Both classes live in the deck's local `<style>`; copy the definitions from any deck that already uses them. Default centered cite is still the preferred form.

**Figure citations.** When a slide shows a captured paper figure, cite the figure number: `Author et al., Venue YYYY — Figure N.` (Visual richness → Figure-capture protocol.)

---

## Recipes

**Title slide**
```html
<div class="slide title-slide active">
  <img class="title-logo" src="../reference/kor-eng2.png" alt="Yonsei University">
  <div class="pill pill-fill">Talk type</div>
  <h1>Title</h1>
  <div class="divider"></div>
  <p class="subtitle">Subtitle</p>
  <p>Speaker · Affiliation · Date</p>
</div>
```

**Content slide**
```html
<div class="slide">
  <h2>Heading</h2><div class="divider"></div>
  <p>Phrase with <strong>blue accent</strong> and <em>muted aside</em>.</p>
  <div class="highlight">Key insight (one max).</div>
</div>
```

**Three-pillar / comparison**
```html
<div class="grid-3">
  <div class="card" style="text-align:center;"><h3>①</h3><p>…</p></div>
  …×3
</div>
```
For short 2-column dichotomies use `.grid-2` with bare `<h3>` + `<p>` (no `.card` wrapper — Priority 3).

**Math slide**
```html
<p>Setup with inline $x_t$.</p>
<div class="math-block">$$\mathcal{L} = \mathbb{E}[-\log p_\theta(x_0)]$$</div>
```
Use `$$…$$` for `\begin{cases}` and `\begin{align}`. Inline `$\displaystyle …$` with `nowrap` is fragile — see GOTCHAS.

**Code / pseudocode block**
```html
<div class="code-block"><span class="cm"># Membership inference, simplest form</span>
<span class="kw">def</span> <span class="fn">attack</span>(model, x, τ):
    return model.<span class="fn">loss</span>(x) <span class="kw">&lt;</span> τ      <span class="cm"># member if loss is small</span>
</div>
```
Tokens: `.kw` (keyword, blue, 700), `.fn` (function name, accent, 600), `.cm` (comment, gray), `.str` (string, green, 600). Renders at 1.25rem / weight 500 — large and thick enough for the back row. Pseudocode is fine; full Python listings rarely fit (move to the note file). Note the escaped `&lt;` — literal `<` anywhere in content is an HTML hazard (see GOTCHAS for the math case).

**Paper-overview slide** (citation as footnote, not card)
```html
<div class="cite">Author(s), "Paper Title", Venue Year</div>
```
One citation per line (Conventions → Citations). Don't wrap the title in `<em>` (gray-on-gray is mud). Don't build a 2-column layout with a paper-title card — see GOTCHAS.

**Image + bullets** (figure on the left, supporting bullets on the right)
```html
<div class="slide">
  <h2>Heading</h2><div class="divider"></div>
  <div class="grid-2" style="grid-template-columns:auto 1fr;gap:40px;align-items:start;">
    <div style="display:flex;justify-content:center;">
      <img src="figure.png" alt="…" style="max-height:470px;width:auto;display:block;">
    </div>
    <div>
      <ul>
        <li>First phrase<br>continuation</li>
        …
      </ul>
    </div>
  </div>
  <div class="cite">Author et al., Name, Venue Year.</div>
</div>
```
Notes:
- **`align-items: start`** — keep bullets top-aligned; `center` floats short bullet lists midway down a tall figure (looks like an empty void on top).
- **Image height ceiling by layout**:
  - **Side column with bullets** (figure left, ≤4 short bullets right): `max-height: 380–430px`.
  - **Stacked (bullets below image)** with **1–3 short bullets** below: `max-height: 380px`.
  - **Stacked with 4+ bullets** or a `.highlight` below: `max-height: 320–340px` — past that, bullets push into the `.cite` and brand footer.
  - **Single-figure slide** (only `h2 + divider + img + cite`, no bullets): `max-height: 470px`.
  - When `max-height` is at the lower end and the image still feels small, prefer the **Image-first / description-follows** pattern below rather than removing bullets to enlarge the image.
- **`<br>` inside `<li>`** is allowed for clean wrap-control next to a narrow column (Priority 1 step 2: one deliberate internal break).
- Figure stays in the talk folder (`<talk>/figs/<file>.png`); `bundle.py` inlines local `<img>` references as data URIs.

**Image-first / description-follows.** When a single image+bullets slide overflows — image cramped, bullets clipping the brand footer, or both — split into two consecutive slides: a full-bleed image slide with at most one orienting sentence, then a follow-up "Reading the plot" slide that carries the bullets. Lets the image breathe at `max-height: 460–500px` while keeping the analysis at body size. Use when the figure is information-dense (multi-panel plots, eigenvalue distributions, qualitative comparison grids).

```html
<!-- Slide A: image first -->
<div class="slide">
  <h2>Eigenvalue Concentration — Stable Diffusion</h2><div class="divider"></div>
  <div style="display:flex;justify-content:center;margin:6px 0;">
    <img src="figs/sail-eigen.png" alt="…" style="max-width:100%;height:auto;max-height:480px;display:block;">
  </div>
  <div class="cite cite-left">Author et al., Venue YYYY — Figure N.</div>
</div>

<!-- Slide B: description follows -->
<div class="slide">
  <h2>Reading the SD Eigenvalue Plots</h2><div class="divider"></div>
  <ul class="arrow" style="line-height:1.7;">
    <li><strong>Exact Mem:</strong> heavy negative-eigenvalue tail …</li>
    <li><strong>Non Mem:</strong> eigenvalues near zero …</li>
    …
  </ul>
  <div class="highlight"><p>One-line takeaway here.</p></div>
</div>
```

Don't apply when the figure is simple (single plot, simple schematic) — one slide handles it. Reach for the split *after* the image-height ceilings above can't fit; before then, just tighten the bullets or shrink the image.

**Section divider (left, numbered)**
```html
<div class="slide section-slide left">
  <div class="section-num">02</div>
  <h1>Controllability</h1>
  <div class="divider"></div>
  <p class="subtitle">Masking schedules, guided remasking, safety</p>
</div>
```
`.section-slide` (centered, `.bg-accent`) for dramatic interludes; `.left` for structural part breaks inside a long talk.

**TOC slide**
```html
<h2>Contents</h2><div class="divider"></div>
<div class="toc-list">
  <div class="toc-item">
    <div class="toc-num">01</div>
    <div class="toc-rule"></div>
    <div><div class="toc-label">Section name</div><div class="toc-sub">Subtitle</div></div>
  </div>
  …×4
</div>
```

**Closer**
```html
<div class="slide end-slide no-footer">
  <div class="big-word">Q&amp;A</div>
  <p class="big-word-sub">Thank you.</p>
</div>
```

**Diagram with math labels.** Build structure in HTML (flex/grid + divs), use SVG only for arrows. Reference: `.fl4-*` / `.ldp-*` / `.rdm-*` in `courses/privacy/lectures/01-dp/dp8-fl.html`. Never put `$…$` inside SVG `<text>` — KaTeX skips it (see GOTCHAS).

**Algorithm slide.** A single styled box, centered. Don't pad with a right-column auxiliary diagram — the algorithm is the exhibit (empty space below is fine; Priority 3). Per-deck define `.<deck>-algo` once if reused (background `--light`, left border 3px `--yonsei-blue`, padding `16px 22px`, radius `0 10px 10px 0`). Algorithms always live in this styled box — never `.code-block`.

Use a counter-based `::before` for step numbers — default `<ol>` markers render too small and lack the visual weight needed at slide font sizes. Pad the step body left so the number visibly precedes the text:

```css
.<deck>-algo ol { margin: 0; padding-left: 0; list-style: none; counter-reset: step; }
.<deck>-algo ol li {
  counter-increment: step;
  padding: 8px 0 8px 56px;
  position: relative;
  line-height: 1.45;
}
.<deck>-algo ol li::before {
  content: counter(step) ".";
  position: absolute; left: 12px; top: 8px;
  font-weight: 700; color: var(--yonsei-blue);
  width: 36px; text-align: right;
}
.<deck>-algo ol li + li { border-top: 1px solid var(--slate); }
```

```html
<div class="slide">
  <h2>Training Algorithm</h2><div class="divider"></div>
  <div class="d2-algo" style="max-width:880px; margin:36px auto 22px;">
    <ol>
      <li>Sample $X^{(0)} \sim p_{\text{data}}$.</li>
      <li>Sample $\epsilon \sim \mathcal{N}(0,1)$.</li>
      <li>Form $X^{(n)} = \sqrt{\bar α_n}\,X^{(0)} + \sqrt{1-\bar α_n}\,\epsilon$.</li>
      <li>Gradient step on $\|\epsilon - \epsilon_\theta(X^{(n)}, n)\|^2$.</li>
    </ol>
  </div>
  <p style="text-align:center;">Caption (e.g., weighting choice).</p>
</div>
```

`max-width` ≈ 880px for compact algorithms, ≈ 1040px when a step carries long math. Caption below, centered. Add a side diagram only if it conveys real new information beyond the algorithm.

**Build-up no-fade.** When several consecutive slides differ only by a single value (Lloyd–Max iteration, Bayes-step coloring, table-cell update), the engine's per-element fadeIn (`animation: fadeIn 0.4s ease both` with 0.06–0.30s stagger) makes navigation feel like a flash on every click. Disable it on those slides only with a per-deck class:

```html
<style>
.<deck>-no-fade.active > * { animation: none !important; }
</style>

<div class="slide <deck>-no-fade">…</div>
<div class="slide <deck>-no-fade">…</div>
```

Result: consecutive build-up slides feel like a single animated frame change. Keep the fade-in on every other slide where it helps the eye land. Complements (does not replace) the multi-slide proof build-up — see Math-heavy → Build-up.

**Recall card.** When a slide depends on a definition the audience saw 5+ slides ago (typical-set definition, AEP, KKT, a specific lemma), lead with a small recall card. Cheaper than asking the audience to remember:

```html
<div class="card" style="padding: 10px 16px; margin-bottom: 10px;">
  <p><strong>Recall (typical set).</strong> $T_\varepsilon^{(n)}(P) = \{z^n : |\hat P_{z^n}(a) - P(a)| &lt; \varepsilon \;\forall a\}$. <strong>AEP:</strong> $|T_\varepsilon^{(n)}(P)| \doteq 2^{nH(P)}$.</p>
</div>
<p>Now we use this to count Hamming-ball volumes…</p>
```

Use only when the dependency is non-obvious. Don't pile up Recall cards — one per slide max. (Note the `&lt;` — literal `<` inside math garbles rendering; see GOTCHAS.)

**Diagram dominates.** When the user says "make the diagram much larger" or the slide is essentially "this picture, plus one short caption", check three things in order:

1. Does the SVG carry a `style="max-width: <small>"` constraint? Remove it. (`max-width` belongs on the wrapper `<div>`, not the SVG itself.)
2. Is the layout `.cols` (two equal-width children)? Switch to `.cols` with `.col-1-3` (text) + `.col-2-3` (diagram) so the diagram gets 2/3 of the slide.
3. Is the SVG viewBox unnecessarily small (e.g. `220×130`)? Bump to `~400×240` so labels render at readable absolute pixel sizes — labels at `1.0–1.4rem` need a viewBox where `font-size` math lands in a sensible scale relative to the SVG's content.

```html
<div class="slide">
  <h2>Setup and Statement</h2><div class="divider"></div>
  <div class="cols">
    <div class="col-1-3"><!-- text + math --></div>
    <div class="col-2-3"><!-- big SVG with HTML overlays --></div>
  </div>
</div>
```

For pure single-diagram slides, drop the cols entirely and center the SVG with `max-width: ~960px; margin: 24px auto`.

**KaTeX overlays on SVG.** KaTeX skips SVG `<text>` nodes — math labels go in absolute-positioned HTML spans on top of the SVG. Recommended sizes:

- Axis labels (`$X_1$`, `$X_2$`, `$\widehat X^n$`): `font-size: 1.3–1.4rem; font-weight: 700;`
- Threshold / index labels (`$\tau_i$`, `$\hat x_j$`): `font-size: 1.0–1.1rem; font-weight: 600;`
- Annotation labels (atom mass, density names): `font-size: 1.1–1.4rem; font-weight: 600;`

Position via `left: %; top: %;` computed against the viewBox: for viewBox `W × H` and SVG coord `(x, y)`, `left = x/W·100%`, `top = y/H·100%`. Use `transform: translate(-50%, -50%)` for centered labels, `transform: translate(-100%, -50%)` for right-aligned (typical for y-axis labels).

```html
<div style="position: relative; width: 100%; max-width: 1040px; margin: 18px auto;">
  <svg viewBox="0 0 400 240" style="display: block; width: 100%;">…</svg>
  <span style="position: absolute; left: 50%; top: 87%;
               transform: translate(-50%, -50%);
               font-size: 1.1rem;">$\hat x = 0$</span>
</div>
```

**Never** put `max-width` on the SVG — put it on the wrapper instead, otherwise labels and SVG drift apart. Give the wrapper `width: 100%` alongside `max-width`, or it collapses to the SVG's intrinsic width (see GOTCHAS). If the wrapper hosts overlay spans, pin its height to the viewBox aspect ratio so `top: %` lands where you computed.

**Inline exercise.** Plain `<p><strong>Exercise.</strong> …</p>` placed next to the related content (definition, theorem, formula). Optional `<em>Hint:</em>` clause. **Don't** create a trailing "Check It Yourself" slide; **don't** introduce per-deck `.exercise-list` styling — the standalone exercise slide pattern was retired.

```html
<div class="math-block">$$f(x) = \tfrac{1}{\pi}\,\tfrac{\gamma}{x^2+\gamma^2}.$$</div>
<p><strong>Exercise.</strong> Verify $\int_{-\infty}^{\infty} f(x)\,dx = 1$.</p>
```

If a slide is already at element budget and the exercise would push past the footer, move it to the *sibling slide that introduces the fact the exercise verifies* — not the slide that uses the fact.

**Chain / dependency diagram.** Inline flex row of math glyphs joined by token-colored arrows. Active edge in `--yonsei-blue`, sleeping edges in `--gray-text`. Place adjacent to the claim it supports (e.g. a Markov-chain illustration above the Markov identity). For longer chains use ellipsis nodes (`$\cdots$`) in `--gray-text`.

```html
<div style="display:flex; justify-content:center; align-items:center; gap:14px; margin:18px 0; font-size:1.55rem;">
  <span>$X^{(0)}$</span>
  <span style="color:var(--gray-text);">$\to$</span>
  <span>$\cdots$</span>
  <span style="color:var(--gray-text);">$\to$</span>
  <span>$X^{(n-1)}$</span>
  <span style="color:var(--yonsei-blue); font-weight:700;">$\to$</span>
  <span>$X^{(n)}$</span>
  <span style="color:var(--gray-text);">$\to$</span>
  <span>$X^{(N)}$</span>
</div>
```

For boxed nodes (more visual weight), use `.diagram-flow` + `.diagram-box` instead — at **full slide width only**, never inside `.cols`/`.grid-*` (see GOTCHAS). For a plain inline chain, the bare flex above is lighter and fits more nodes.

---

## Visual richness — figures, diagrams & TODO-marks

**Policy: target visually rich slides.** A deck of bullet lists is a failure mode. Every content slide should aim to carry an *exhibit* — a diagram, schematic, chart, figure, table, or worked-math block — with text reduced to a short framing line. Bare bullets are a fallback, never the goal.

**Three sources of visuals, in priority order:**

1. **Real paper / public figures — preferred whenever a citable source exists.** If a paper or well-known blog post already has the figure that makes the point (panda→gibbon, the CLIP Figure 1 similarity grid, a COMPAS bar chart, a BadNets trigger), **capture and reuse it with an explicit citation** rather than redrawing it as an original diagram — the real figure is more credible and faster to produce correctly. Follow the **Figure-capture protocol** below. Reuse figures already vetted in sibling decks (e.g. `courses/privacy/lectures/03-memorization/figs/`) rather than re-fetching.
2. **Inline HTML + SVG concept diagrams** — for ideas that have no single canonical source figure to capture (a mechanism you're explaining in your own words, a comparison across multiple papers, a made-up worked example). Build structure in HTML/SVG (boxes, circles, arrows, overlapping bell curves, 2×2 grids, flows, pipelines, trees). Plain-text labels in SVG `<text>` — KaTeX skips SVG, so never put `$…$` inside `<text>` (see GOTCHAS). One semantic color per role (Yonsei blue = focus, gray = context, `--warn` red = the bad case). Shipped examples to imitate: overlapping-distribution "indistinguishability" curves, a knowledge×timing 2×2 map, a layered trust stack, a randomized-response coin tree, a Laplace-noise bell, a federated-learning fan-in, a linkage Venn (`courses/trustworthy-ai/lec01-introduction.html`, `lec02-privacy-dp.html`).
3. **TODO-marks** — when you *want* a real figure or a richer diagram but can't produce it now (no network, fiddly crop, needs design time), **do not ship a bare slide**. Leave a marker on the slide where the visual belongs:

   ```html
   <!-- TODO real figure: <what to show>, <source paper / Fig N> -->
   ```

   These are first-class authoring debt, not silent omissions. `grep -rn "TODO real figure"` finds every slide still missing its intended visual.

**When there's a well-known figure for the idea, capture it — don't redraw it.** If you catch yourself building an original HTML+SVG diagram to express a concept that a specific, identifiable paper or blog post already illustrates (e.g. the CLIP paper's Figure 1 image×caption grid with positives on the diagonal), stop and capture the real figure instead (source 1), with an explicit citation per the **Figure-capture protocol**. Only fall back to an original concept diagram (source 2) when no clean source figure exists to capture, or the source panel itself is unsuitable to show as-is (e.g. it reproduces extracted private training data — see "Prefer methodology figures" below).

**Make diagrams big.** Concept SVGs are routinely drawn too small. Full-width single-diagram slides: wrapper `max-width: 820–920px`, SVG `<text>` `font-size: 15–20` (viewBox units), bold for primary labels. Diagrams paired with bullets in a grid column: `max-width: 360–440px`, `font-size: 13–16`. Bump **both** the wrapper width and the font-size numbers — a wider wrapper alone leaves labels proportionally small (GOTCHAS → "Concept SVG renders too small"). See Recipes → Diagram dominates.

**Still one exhibit per slide.** Visual-rich means *a* strong visual per slide, not a collage. Two visuals ⇒ two slides (Style rule 1). Empty space *below* a centered diagram is fine; middle voids are not (Priority 3).

### Figure-capture protocol (third-party papers)

When pulling a real figure from an arXiv/venue paper into a deck, follow this protocol so the slide is clean and the legal posture defensible:

- **Crop the main figure caption out.** The "Figure N: …" line is for the paper reader, not the audience — the speaker narrates the figure, and the caption pushes it off the slide. Keep subcaption labels `(a)`, `(b)` only when the speaker references them.
- **Cite the source figure number** in `.cite`: `Author et al., Venue YYYY — Figure N.`
- **Prefer methodology figures** (plots, schematics, algorithm diagrams) over panels that reproduce extracted training images or other third-party copyrighted content. For those panels, describe the example in text with a strong attribution rather than embedding the panel.
- **Crop tightly, with headroom.** Drop page headers ("Published as a conference paper at…"), running titles, and adjacent figure/table content the slide doesn't reference — but leave a few px of headroom on every side (tabs and axis titles sit a few px outside the apparent bounding box; see GOTCHAS). Typical flow: `pdftoppm -r 200 paper.pdf prefix`, then crop with `sips --cropToHeightWidth H W --cropOffset Y X` or PIL — eyeball the offsets, iterate twice, then **Read the resulting `figs/*.png` directly** to confirm (never trust a possibly-cached in-slide render).
- **Render at ≥180 DPI** when extracting via `pdftoppm`; lower DPI looks pixelated when the slide scales up on a projector.
- **Store under `<talk>/figs/`.** `bundle.py` inlines `.png`/`.jpg`/`.svg`/`.webp`/`.gif` from any path relative to the deck.
- **Downsample to ~1200 px max width before bundling** (`sips --resampleWidth 1200 figs/big.png --out figs/big.png`). Full-res captures (2000–3500 px) base64-bloat the standalone bundle past 50 MB (see GOTCHAS). The authoring source is unaffected; downsample before distributing.

---

## Companion note files

When detail is worth recording but doesn't fit on the slide (full-sentence explanations, derivations the proof slide skipped, secondary examples, "FYI" context), put it in `<deck>/<deck>-note.html` — one section per slide, in slide order, headed by the slide's title. Plain HTML so KaTeX `$…$` / `$$…$$` works the same as in the deck. The note file does not use the `.deck` / `.slide` engine; a simple `<article>` per slide is enough.

For lectures, the note file is also the natural home for the **expanded proof** when the slide carries the abbreviated version.

**Migration check (trim → note).** Whenever you trim detail off a deck slide on the grounds that "it belongs in the note file" — a proof step, a secondary derivation, an FYI aside — open the paired `-note.html` and verify the content is actually there. If it isn't, migrate the trimmed material into the note file *in the same edit*. Deleting from the deck on the assumption it was already covered silently destroys content.

**Speaker-script variant.** A common, useful note form for lectures is a per-slide *script*: one `<article>` per slide in deck order, `<h2>` = the slide's title, then 1–2 sentences of what to actually say, then a `Key takeaway:` line (a blue `.kt` span). This pairs one-to-one with slides and doubles as the deck's outline-of-record. Keep each entry brief (≤ ~50 words of script).

Not a paper draft, not a transcript. The speaker's reading companion.

## Technical supplement decks (concept-first split)

For a course pitched below the math's native level (e.g. an undergrad survey over graduate-rigor topics), split each lecture in two: the **main deck** stays concept-first — motivation, pictures, at most **one glanceable formula per concept** — and a sibling **`<deck>tech.html`** holds the formal version (multi-line derivations, algorithm boxes, definition cards with quantifiers, test statistics). The supplement is optional, shown only to students who want the equations. Established across the 15-deck `courses/trustworthy-ai/` course (`lecNNtech.html`).

Rules that keep the split clean:

- **Stay/move rule.** *Stays* in the main deck: one short single-expression formula an audience reads at a glance (`‖δ‖ ≤ ε`, a one-line rate equality). *Moves* to the supplement: anything multi-line; algorithm boxes with math; formal-definition cards with quantifiers; Hessians, sums-over-subsets, expectations-with-penalty, likelihood ratios, z-statistics.
- **No back-references.** When you move a formula out, leave a one-line plain-English statement so the main slide still stands alone (Style rule 10). Do **not** point the main slide at the supplement — both decks are self-contained; the supplement is discoverable via `OUTLINE.md`, not via cross-refs.
- **Structure.** Mirror the parent's `<head>`/`<style>` (so `.def-card`/`.ta-algo`/`.cite-left` resolve). Title slide labelled "Lecture NN · Technical Supplement", a "When to Use This" framing slide, then the formal content under the Math-heavy patterns above, then a closer. Proportionate length — rich where the topic has real math, honestly short (4–6 slides) where it doesn't; never padded.
- Register every supplement in the leaf `OUTLINE.md` under a "Technical supplements" table.

---

## OUTLINE.md (per-folder index)

Every folder carries an `OUTLINE.md`: root navigator, folder overview, leaf subfolder. Leaf files list every deck's section table with `file:line` pointers and every named theorem/lemma/key formula with its line number. They are the canonical map for finding "where does proof X live" without grepping.

### Read-side rule — consult before writing

**Before writing or substantively rewriting any slide content, read the relevant `OUTLINE.md` files.** The cost is a few seconds; the reward is avoiding redefinition, contradiction, or duplication. Two scenarios trigger this:

1. **In-track continuity (same lecture series).** When extending a multi-deck series — e.g., writing `privacy/lectures/04-mia/mia3-theory.html` — open `privacy/lectures/04-mia/OUTLINE.md` and `privacy/OUTLINE.md` first. Confirm what notation, definitions, attacks, theorems, and benchmarks earlier decks already established. Do not redefine $(\varepsilon, \delta)$-DP if `privacy/lectures/01-dp/dp4-approximate-dp.html` (or the capstone `dp8-fl.html`) covered it; refer back via a brief "Recall (Lecture X)" instead. Conversely, if a prerequisite has *not* been covered, decide whether to (a) add a one-slide recap, (b) point students to the prior deck, or (c) defer the topic. Skipping this check produces decks that talk past each other.

2. **Cross-folder reuse (same topic, different track).** When writing on a topic that may already live elsewhere — diffusion (`infotheory/lectures/07-diffusion/` vs `privacy/lectures/02-generative/` vs `dllm` talks), DP (`privacy/lectures/01-dp/` vs `privacy/lectures/04-mia/mia1-foundations.html`), MI bounds (`infotheory/lectures/05-mi/` vs anywhere CLIP/InfoNCE comes up) — open the **root `OUTLINE.md` quick-lookup table** and the relevant leaf files in the *other* folder. Decide explicitly: reuse the derivation as-is, adapt to the new framing, link via "see also", or deliberately contradict (with rationale). Do not rederive a theorem in track B that already has a clean statement and proof in track A's notes — link to `<file>:<line>` instead.

When the OUTLINE entries you find are too coarse to answer the question, descend into the cited `<file>:<line>` and confirm. The OUTLINE points; it does not replace reading the deck.

### Write-side rule — keep outlines accurate

**Maintenance rule (non-negotiable):** any slide edit that changes a section boundary, line range, or named theorem location requires the corresponding `OUTLINE.md` line numbers to be updated *in the same change*. Adding a slide → add the entry. Removing a slide → remove it. Renaming a section → rename it everywhere it is cited (leaf, folder, root quick-lookup). Bulk renumbering after a multi-slide insertion is part of the edit, not a follow-up.

If you cannot locate a topic from the OUTLINE files, the OUTLINE files are stale — fix them, don't work around them. Stale outlines are worse than no outlines because they mislead. `python3 scripts/outline-lint.py` mechanically verifies every cited `file:line` (file exists, line within range) — run it after any edit that shifts line numbers; it cannot check that the line still holds the *claimed* content, so spot-check after big restructures. Without `python3`, spot-check by hand (`sed -n '<N>p' <file>` — see Verifying without the toolchain).

When creating a new deck, add a stub entry in the leaf `OUTLINE.md` before writing the deck (file path + topic line). Cross-references to other decks (in the root quick-lookup table) get added when the relevant content is actually present.

---

## Extension checklist

Before adding a new component:

1. Is it a styled variation of an existing component? Use inline `style=` (with `var(--…)`, never hardcoded colors — except SVG presentation attributes, which can't take `var()`; see GOTCHAS).
2. One-off on a single slide? Keep it inline.
3. Reused in ≥2 decks? Add it to `reference/deck.css` first, then this doc, then use it.

New components must document: name, purpose, default + `.bg-accent` appearance, an example, token dependencies. Candidates worth adding when you've reused the pattern enough to feel friction: `.theorem`, `.proof-step`, `.intuition-callout`. Until then, the recipes above using existing `.card` / `.math-block` / `.highlight` are the canonical form.

---

For pitfalls and debugging (italic prose collapse, KaTeX delimiter escape, cascading math breakage, the headless-print shrink artifact, etc.), see **`GOTCHAS.md`** — organized symptom-first so you can search by what you're seeing.
