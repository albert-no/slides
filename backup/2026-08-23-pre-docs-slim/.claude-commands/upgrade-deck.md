# /upgrade-deck

Interactively pull a deck back in line with the current design system: strip per-deck overrides of canonical tokens, verify the canonical links and KaTeX handler, and propose structural updates (TOC slide, left-numbered section dividers, end-slide, `no-footer` tags) where appropriate.

## Inputs
- Target deck path (HTML file).

## Workflow

1. **Read canonical references first**: `reference/deck.css`, `reference/deck.js`, `DESIGN_SYSTEM.md` (Deck anatomy + Priorities).
2. **Check canonical wiring**: the deck must `<link>` `reference/colors_and_type.css` and `reference/deck.css`, and load `reference/deck.js` (relative path per depth — `../../reference/` for talks, `../../../../reference/` for course lectures). If the deck inlines copies of canonical CSS/JS instead, propose replacing them with links.
3. **Override audit** — list per-deck `<style>` rules that shadow canonical tokens, each with a one-line rationale for removal (see `GOTCHAS.md` for symptoms):
   - Redefinitions of `p`, `li`, `h1`–`h3`, `.subtitle`, `.cite`, `.small`, `.tiny`, `.math-block`, `.muted`, `.code-block` font sizes.
   - A `font-size` on `.muted` (canonical is color-only).
   - A per-deck `.page-num` injector script / CSS (duplicate page numbers — keep only the canonical `.slide-num`).
4. **KaTeX handler check**: delimiters in the `onload` handler must be double-escaped (`{left:'\\(', …}`) and match `reference/deck-skeleton.html`. Single-backslash delimiters silently break parenthesized prose (GOTCHAS → "KaTeX delimiter escape bug").
5. **Structural audit** — list candidates for upgrade against DESIGN_SYSTEM → Deck anatomy, each with a one-line rationale:
   - Is there a Contents slide (required at 3+ sections)? If not, propose one matching the deck's section structure.
   - Are `.section-slide` instances using the left-numbered variant for structural breaks?
   - Does the deck end with a `.end-slide` Q&A closer tagged `no-footer`?
6. **Confirm each proposal with the user** — apply one at a time, show the diff, wait for approval.
7. **Re-lint**: `python3 scripts/lint-deck.py <deck>` → zero warnings is the goal.
8. **Update `OUTLINE.md`** if slides were added/removed/reordered.

## Reversibility

Each structural edit is one `Edit` call, so the user can ask to revert specific changes by referencing them. Git is the backstop.

## Output

After each phase, print a short status line:
```
[wiring]   canonical links ok · KaTeX handler ok
[override] removed .muted font-size, deleted .page-num injector → accepted
[propose]  add Contents slide → accepted
[propose]  convert section dividers (3 instances) → 2 accepted, 1 skipped
[lint]     0 warnings, 0 errors
```

## Do not

- Bulk-edit without user approval, even for small changes. The point of this command is interactivity.
- Alter slide content (prose, math, diagrams) without being asked. Only structural/style changes.
- Introduce new CSS classes — those belong in a `reference/deck.css` edit, documented per DESIGN_SYSTEM → Extension checklist.
- Touch the canonical `reference/` files from this command.
