# /audit-deck

Audit a deck against the talks design system. Produces a report — does not edit. (Static analysis only; for rendered-layout issues — overflow, overlap, line breaks — use `/audit-and-edit-deck`.)

## Inputs
- Target deck path (HTML file). Default to the single `.html` under the current deck folder if none given.

## Workflow

1. **Read canonical references**: `reference/deck.css`, `reference/deck.js`, `DESIGN_SYSTEM.md` (Priorities, Style rules, Deck anatomy).
2. **Run `python3 scripts/lint-deck.py <deck>`** and capture the output verbatim. Optionally run `scripts/find-wordy.py` / `scripts/find-dense.py` for density hot spots.
3. **Inspect every slide** and rate it on:
   - Consistency with the design system (classes used, accent patterns, divider placement).
   - Style priorities from `DESIGN_SYSTEM.md`: one idea per slide, 7×7 density, `**strong**` / `*em*` usage, max one `.highlight`, math in `.math-block`, visual element + vertical budget (Priority 2).
   - Deck anatomy: title → TOC (if 3+ sections) → sections with dividers → closer; ghost-deck test on the `h2` sequence.
   - Visual richness: content slides without an exhibit or a `TODO real figure` marker.
4. **Draft a report** with these sections:
   - **Summary** — pass/fail, total warnings, overall score out of 100.
   - **Token & class coverage** — anything hardcoded, unknown classes (note: hex inside SVG attributes is house style, not a violation — see `GOTCHAS.md`).
   - **Slide-by-slide findings** — only slides with issues: slide number + `h2` text, one-line diagnosis, one-line fix.
   - **Priority actions** — top 3 fixes, ranked by impact.
5. **Offer** to fix the priority actions via `/upgrade-deck` or direct edits, but do not edit without explicit user approval.

## Output format

Keep it tight — no slide-by-slide entry for clean slides. Identify slides by `h2` text as well as number (numbers shift on edits).

## Do not

- Make any edits. This command is read-only.
- Fabricate lint warnings the script didn't actually produce.
- Flag `no-footer` as an unknown class (it's a `deck.js` engine class) or hex in SVG attributes as hardcoded colors.
