# /new-slide

Add one or more slides to an existing deck, strictly following the talks design system.

## Inputs
- Target deck path (HTML file).
- Topic, structure, and any specific components desired (cards, math, table, diagram, etc.).

## Workflow (follow every time)

1. **Read `DESIGN_SYSTEM.md` §1 Priorities**, then **only** the numbered section matching the slide type (§5 math, §7 patterns, §8 visuals). Take the `offset`/`limit` for each from the doc's index block — never read the file whole. The 4 priorities and the vertical budget apply at draft time, not after preview. For a class's exact behavior, grep its selector in `reference/deck.css` — the source of truth.
2. **Read the leaf `OUTLINE.md`** of the deck's folder (read-side rule in `DESIGN_SYSTEM.md` §10): confirm what earlier decks in the series already define, and check the root `OUTLINE.md` quick-lookup table if the topic may live in another folder. Refer back; don't redefine.
3. **Open the target deck** and find the insertion point. Match slides by `<h2>` content, not slide number (numbers shift on insertion).
4. **Draft the new slide(s)** using only classes defined in `reference/deck.css` (or the deck's own local `<style>`). If a desired pattern is not in the system, do **not** invent ad-hoc classes — compose existing ones with inline `style=` (use `var(--…)`, never hardcoded colors) or stop and propose a design-system extension (DESIGN_SYSTEM §12).
5. **Insert**, then verify:
   - No new classes outside the canonical set + the deck's local `<style>`.
   - One `.highlight` per slide max; one exhibit per slide.
   - Math in `.math-block` (display) or inline `$…$`; no `<` literal inside math (use `&lt;`).
   - Slide fits the vertical budget (Priority 2) — split rather than shrink.
   - Every content slide aims to carry a visual, or a `<!-- TODO real figure: … -->` marker (DESIGN_SYSTEM §8).
6. **Run `python3 scripts/lint-deck.py <deck>`** and fix any warnings. Optionally `python3 scripts/find-wordy.py <deck>` to catch over-long prose.
7. **Update the leaf `OUTLINE.md`** (and parent/root if a new topic or cross-reference appeared) — line numbers must stay accurate (write-side rule).

## Output

Summarize which slides were added, the recipes used, and the lint result. Do not re-paste the full file; show only the new slide markup (diff-style) so the user can eyeball it before refreshing Chrome.

## Do not

- Edit `reference/deck.css` or `reference/deck.js` from this command — canonical changes are their own explicit task.
- Hardcode colors or typography values inline. Use CSS variables (`var(--…)`). Exception: hex in SVG *attributes* (`fill=`/`stroke=`) is house style — see `GOTCHAS.md`.
- Remove the deck's `<link>`s to `reference/colors_and_type.css` / `reference/deck.css` or the `reference/deck.js` script tag — decks link to canonical sources, never duplicate them. Don't add any other external stylesheet beyond the existing KaTeX CDN links.
- Shrink type or use `.tiny` / `.small` on prose to make content fit (Priority 0).
