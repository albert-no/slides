# /audit-and-edit-deck

Visually audit one or more decks by rendering every slide to PNG and checking for overflow, overlap, awkward line breaks, and other layout flaws static lint cannot catch — then fix what you find. The **visual** counterpart to `/audit-deck`. Triggered by "audit this slide", "screenshot check", "look for overflow", or similar.

## Inputs

A path — a single HTML file, or a folder (audit every `*.html` directly inside it, skipping `*-note.html`, `*-standalone.html`, `*.standalone.html`, and `reference/`; one deck at a time). No path → the single deck in the cwd; if several, ask which.

## Token budget — binding

A full-deck read is the most expensive routine operation in this repo. These are limits, not suggestions:

- **Render at `-r 60`.** ~480 tokens/slide. `-r 150` is ~1,330 — 3× the cost for typography detail this audit does not check.
- **`-r 150` is single-page only**, via `pdftoppm -f N -l N -r 150`, and only when fine text detail is genuinely in question. Never a full deck.
- **Read the whole deck exactly once**, in step 3. Every later pass re-renders and re-reads **only the pages edited since**.
- **Never re-read an unchanged slide.** If you already have the image in context, you have it.
- **Don't read the reference docs whole.** `DESIGN_SYSTEM.md` §1 is the rule spine; `grep` GOTCHAS by symptom.

State your intended page count and DPI before rendering. If a deck is large enough that one pass at `-r 60` is still heavy, say so and ask before proceeding rather than silently truncating.

## Workflow (per deck)

**0. Toolchain check.** `command -v pdftoppm`; Chrome at the path below or `google-chrome`/`chromium`. Missing → try to install (`brew install poppler`). Confirmed unavailable and uninstallable → do **not** keep forcing the pipeline: say plainly that no visual render is possible here, run the audit via `DESIGN_SYSTEM.md` §11 (slide map by grep, overflow by vertical-budget arithmetic, lint by targeted grep), apply the same fix rules, and flag in the Output that **no visual render was performed**.

**1. Render to PDF.**
```bash
mkdir -p /tmp/<basename>-shots && cd /tmp/<basename>-shots
rm -f deck.pdf slide-*.png
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --incognito --user-data-dir=/tmp/fresh-$RANDOM --disk-cache-size=1 \
  --disable-gpu --no-sandbox \
  --virtual-time-budget=30000 --run-all-compositor-stages-before-draw \
  --print-to-pdf=deck.pdf --print-to-pdf-no-header \
  "file://$(realpath <deck>.html)"
```
`--virtual-time-budget=30000 --run-all-compositor-stages-before-draw` are **required**. Without them a large deck's `<img>` slides can be snapshotted before layout finishes, so Chrome scales the page to ~55% anchored top-left — a **render artifact, not a slide defect**. Seeing a whole-slide shrink on an image slide? Re-render with these flags and confirm in a manual `Cmd+P` before "fixing" anything (GOTCHAS §9).

**2. Split to PNG.** `pdftoppm -png -r 60 deck.pdf slide` — see Token budget. Missing `pdftoppm` → `brew install poppler`; don't silently skip.

**3. Read each `slide-NN.png` once** and inspect for:
- Figure or text overflow past the 1280×720 rectangle.
- **Brand-footer collision** — `.brand-footer` sits bottom-left with ~40 px reserved. A `.highlight`, `.cite`, or trailing prose ending in that region counts as overlap.
- **Text-on-figure / figure-on-figure overlap** — SVG labels over arrows, HTML overlays drifting onto strokes.
- **Bad line breaks** — math split across lines, captions wrapping mid-phrase, widows, em-dash orphans.
- **Squashed math** — `\!` pulling glyphs together; stray `\#`/`\&` from LaTeX escapes.

**4. Fix in place**, in priority order: compress prose to noun phrases → combine adjacent `math-block` divs into one `aligned` (~30 px) → trim redundant intro/outro and cross-references → **split the slide** (preferred over cramming). **Never shrink type** — Priority 0 is non-negotiable.

**5. Verify narrowly.** Re-render only affected pages (`pdftoppm -f N -l M -r 60`) and re-read **only those**. The full-deck read already happened in step 3 and does not repeat.

**6. Lint.** `python3 scripts/lint-deck.py <deck>` once, and report.

**7. Update `OUTLINE.md`** if any slide was added, split, removed, or reordered — line numbers must stay accurate.

## Folder mode

Run the per-deck workflow against each matching file in sequence, a separate `/tmp/<basename>-shots/` per deck. Report each deck under its own heading; don't interleave. The token budget applies **per deck** — it does not amortize across a folder.

## Output

- One-paragraph summary of what was wrong and how it was fixed.
- Slides modified, with numbers.
- Any slide split (and the new total count).
- Final lint status.
- Pages rendered and read, at what DPI — so the cost is visible.
- If the §11 fallback was used: say so explicitly, and which checks replaced the render.

Found nothing? Say so. Don't fabricate findings.

## Do not

- Shrink type, compress vertical rhythm, or pad with `.tiny`/`.small` to make content fit. Split instead.
- Re-read unchanged slides, or render fix-loop pages above `-r 60` without a concrete stated reason.
- Read `DESIGN_SYSTEM.md` or `GOTCHAS.md` cover to cover.
- Silently skip slides because a tool errored. Surface the error.
- Edit `-note.html` companions unless asked, or touch canonical `reference/` files.
