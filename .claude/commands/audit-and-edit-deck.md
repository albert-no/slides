# /audit-and-edit-deck

Visually audit one or more decks by rendering every slide to PNG and checking for overflow, overlap, awkward line breaks, and other layout flaws that the static lint cannot catch. Then fix the issues found.

This is the **visual** counterpart to `/audit-deck` (static-analysis only). When the user says "audit this slide" / "screenshot check" / "look for overflow" / similar, this is the right command.

## Inputs

A path argument — either a single HTML file or a folder.

- **File** (`<path>/<deck>.html`): audit that one deck.
- **Folder** (`<folder>/`): audit every `*.html` file directly in the folder whose name doesn't end in `-note.html`, `-standalone.html`, or `.standalone.html`. Skip the `reference/` folder. Process one deck at a time.

If no path is given, default to the single `.html` deck under the current working directory (excluding notes / standalones). If the directory contains multiple decks, ask which one.

## Workflow (per deck)

1. **Render the deck to PDF** via headless Chrome:
   ```bash
   mkdir -p /tmp/<basename>-shots && cd /tmp/<basename>-shots
   rm -f deck.pdf slide-*.png
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
     --headless --disable-gpu --no-sandbox \
     --print-to-pdf=deck.pdf --print-to-pdf-no-header \
     "file://$(realpath <deck>.html)"
   ```
2. **Split into PNGs** (one per slide) via poppler:
   ```bash
   pdftoppm -png -r 100 deck.pdf slide
   ```
   If `pdftoppm` is missing, instruct the user to `brew install poppler`. Do not silently skip.
3. **Read each `slide-NN.png`** with the `Read` tool and inspect for:
   - **Figure or text overflow** past the 1280×720 slide rectangle.
   - **Brand-footer collision** — `.brand-footer` lives at bottom-left (~40 px reserved). A `.highlight`, `.cite`, or trailing prose ending inside that region counts as overlap.
   - **Text-on-figure / figure-on-figure overlap** — SVG labels positioned on top of arrows or other elements; HTML overlays drifting onto chart strokes.
   - **Inappropriate line breaks** — math glyphs split across lines, captions wrapping mid-phrase, lone widows, em-dash orphans.
   - **Squashed math spacing** — `\!` negative thin space pulling commas/labels into adjacent glyphs; literal `\#`/`\&` leftover from LaTeX escapes in HTML prose.
4. **Fix issues in place.** Priority order:
   1. Compress prose to noun phrases (Priority 1).
   2. Combine adjacent `math-block` divs into one `aligned` block (saves ~30 px vertical).
   3. Trim redundant intro/outro lines, `→ Part X` cross-references, or duplicated framing.
   4. **Split the slide** into two consecutive slides — preferred over cramming.
   - **Never shrink type.** Priority 0 in `DESIGN_SYSTEM.md` is non-negotiable.
5. **Re-render** the affected pages (`pdftoppm -f <N> -l <M>`) and re-read to confirm the fix.
6. After all fixes, run `python3 scripts/lint-deck.py <deck>` once and report.
7. **Update `OUTLINE.md`** if any slide was added, split, removed, or reordered (line numbers must stay accurate).

## Folder mode

When the argument is a folder, run the per-deck workflow above against each matching `.html` file in sequence. Use a separate `/tmp/<basename>-shots/` directory per deck to avoid mixing PNGs. Report each deck's findings under a heading; do not interleave.

## Output

After all fixes are committed to the file(s):

- One-paragraph summary of what was wrong and how it was fixed.
- Bullet list of slides modified (with slide-number references).
- Note if any slide was split into multiple slides (and the new total slide count).
- Final lint status.

If no issues found, say so explicitly — don't fabricate findings.

## Do not

- Shrink type, compress vertical rhythm, or pad with `.tiny` / `.small` to make content fit. Split the slide instead.
- Silently skip slides because the tool errored. Surface the error.
- Edit `-note.html` companion files unless the user explicitly asks.
- Touch the canonical `reference/` files.
