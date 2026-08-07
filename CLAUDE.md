# Talks repo

Slide decks for academic talks — conference presentations and master-level lectures. **Math-heavy**: rigorous theorem statement, rigorous proof, plus a high-level intuition pass. **Minimal visual design**: short abstract phrases, not full sentences (7×7 rule). Two authoring formats:

- **Custom HTML** (`<talk>/<talk>.html`) — preferred. Single-page deck, one `.active` slide visible at a time, scaled to viewport via JS. Links to `reference/` for CSS/JS/fonts/logo.
- **Marp markdown** — copy `template.md`, run `marp <file>.md --pdf`.

## Which doc to read when

- **Authoring or editing slides** → **`DESIGN_SYSTEM.md`**. Start at its **Quick reference** table (task → section). It is the canonical rules doc; when it and GOTCHAS.md overlap, it wins.
- **Debugging a rendering symptom** → **`GOTCHAS.md`**. Organized symptom-first under nine categories (Math & KaTeX rendering breakage; Fonts & canonical tokens; Overflow & the vertical budget; Prose & line breaks; Citations; Diagrams & SVG; Proof & structure drift; Engine, navigation & audit false alarms; Toolchain: headless rendering, figures & bundling). Search there before debugging from scratch.
- **Finding existing content** (a theorem, a prior definition, a reusable figure) → the three-tier `OUTLINE.md` system (see "Outlines" below).

Non-negotiable across all work: the four ranked priorities in `DESIGN_SYSTEM.md` → **Priorities (ranked, non-negotiable)** — 0 font sizes, 1 density, 2 overflow (with the **Vertical budget** px table), 3 empty space.

## Common tasks → where to start

| Task | Start here |
|---|---|
| New deck | `scripts/new-talk.sh` (below), then `DESIGN_SYSTEM.md` → **Deck anatomy** (slide order, slide-count norms, **Exemplars** — which shipped deck to imitate per genre). Budget every planned slide against the **Vertical budget** at draft time. Add an `OUTLINE.md` stub immediately. |
| Edit / add slides | Read the relevant outlines first (Outlines below), then `DESIGN_SYSTEM.md` recipes; follow the Editing workflow below. |
| Fix overflow on a slide | `DESIGN_SYSTEM.md` → Priorities → **2. Overflow** (+ Vertical budget); `GOTCHAS.md` → **Overflow & the vertical budget**. Never shrink type. |
| Visual audit ("check page 12", overflow/overlap) | `/audit-and-edit-deck` (below, on request only). |
| Add a visual / capture a paper figure | `DESIGN_SYSTEM.md` → **Visual richness** (incl. **Concept, not copy** and **Figure-capture protocol**). |
| Distribute a deck | `python3 scripts/bundle.py` (Editing workflow step 6). |

**Default to visually rich slides.** Every content slide should aim to carry a diagram, figure, chart, or SVG — text-only bullets are a fallback, not the goal. When a real figure or richer diagram can't be made now, leave a `<!-- TODO real figure: … -->` marker rather than shipping bare bullets. Keep each slide self-contained (no "next week"/"(Wk N)" cross-references). Full policy: `DESIGN_SYSTEM.md` → **Visual richness**.

## Visual identity

White background. Yonsei Blue (`#003876`) accent. Yonsei TTFs (`reference/fonts/`) with Noto Sans fallback. Yonsei emblem (`reference/kor-eng2.png`) in the title-slide top-right.

## Repo layout

```
courses/                    semester-long lecture series
  <course>/<topic>/<deck>.html    e.g. courses/infotheory/lectures/01-entropy/entropy1-entropy-kl.html
talks/                      standalone research presentations
  <name>/<deck>.html              e.g. talks/icml2026/icml2026.html
reference/                  canonical CSS/JS/fonts/logo (single source of truth)
  colors_and_type.css       @font-face + CSS tokens
  deck.css                  slide engine + components
  deck.js                   scale / nav / progress / brand-footer
  deck-skeleton.html        starter (cloned by new-talk.sh)
  fonts/                    Yonsei{Light,Bold,Body,Logo}.TTF
  kor-eng2.{png,pdf}        Yonsei emblem
scripts/
  new-talk.sh               scaffold a new deck (--course for lectures)
  bundle.py                 produce <name>.standalone.html for distribution
  lint-deck.py              validate against canonical CSS + mechanical style
                            rules (banned .tiny/.small-on-prose, shrunk font-size,
                            '<' inside math, KaTeX delimiter escape, $ in SVG
                            text, page-num injector, mid-sentence dashes,
                            adjacent math-blocks)
  find-wordy.py             flag <p>/<li> over the word ceiling (7×7 rule)
  find-dense.py             flag slides with too many words/bullets/paragraphs
  outline-lint.py           verify OUTLINE.md file:line pointers aren't stale
OUTLINE.md                  per-folder content index — root, every topic folder,
                            and every leaf subfolder. See "Outlines" below.
```

Only the authoring source (and its image assets) are committed. `<talk>.standalone.html` is a build artifact (gitignored). `bundle.py` base64-inlines local `<img>` references (`.png`, `.jpg`, `.svg`, `.webp`, `.gif`) into the standalone file.

## Creating a new talk

```bash
scripts/new-talk.sh <talk-name>                    # → talks/<name>/<name>.html
scripts/new-talk.sh --course infotheory <talk-name> # → courses/infotheory/<name>/<name>.html
```

For Marp, copy `template.md` and run `marp <file>.md --pdf`.

## Editing workflow

1. Edit `<talk>/<talk>.html`.
2. Open the file in Chrome to preview (`reference/` must be alongside, which it is in this repo).
3. `python3 scripts/lint-deck.py <deck>.html` (or `--all`) catches unknown classes, hardcoded colors, and the mechanical style rules (see `scripts/` listing above). Errors (`<` inside math, KaTeX delimiter escape) break rendering — fix immediately; warnings are Priority-0/1 violations.
4. After drafting prose-heavy slides, `python3 scripts/find-wordy.py <deck>.html` flags bullets over the word ceiling — compress to noun phrases before previewing. `scripts/find-dense.py` flags over-stuffed slides.
5. **Update `OUTLINE.md`.** Whenever you add a slide, remove a slide, rename a section, change a section's line range, or add/remove a theorem the outline cites, update the leaf-subfolder `OUTLINE.md`. If the change introduces a new topic, file, or cross-reference, also update the parent folder's `OUTLINE.md` and the root `OUTLINE.md` quick-lookup table. Line numbers must stay accurate — outlines are read as authoritative pointers. Verify with `python3 scripts/outline-lint.py`. Full rule: `DESIGN_SYSTEM.md` → **OUTLINE.md (per-folder index)** → Write-side rule.
6. To distribute: `python3 scripts/bundle.py <talk>/<talk>.html` produces `<talk>.standalone.html` — single self-contained file (~4 MB, gitignored), no network deps.

### If the toolchain is missing

Steps 2–5 assume Chrome, `pdftoppm`, and `python3` exist. **Attempt the real tools first** — they are the canonical verification loop. If a tool is *confirmed* missing and uninstallable (`command -v google-chrome pdftoppm python3 mutool convert gs` all come up empty), fall back to `DESIGN_SYSTEM.md` → **Verifying without the toolchain (no-render fallback)**: slide map by grep, overflow by Vertical-budget arithmetic, lint checks by targeted grep, outline pointers by `sed -n '<N>p'`. When you ship work verified only that way, **say so explicitly** in your report and recommend a real render/audit once tooling is available — the fallback cannot catch visual overlap, squashed math spacing, or drifted SVG overlays.

## Screenshot audit (on request)

The lint script catches structural issues (unknown classes, hardcoded colors) but not visual ones (overflow, overlap, awkward line breaks). For visual audits, use the **`/audit-and-edit-deck`** slash command (see `.claude/commands/audit-and-edit-deck.md`).

```
/audit-and-edit-deck <deck>.html      # audit one deck
/audit-and-edit-deck <folder>/        # audit every deck under the folder
/audit-and-edit-deck                  # default to the single deck in the cwd
```

The command renders each slide to PNG via headless Chrome + `pdftoppm`, reads the images, and fixes overflow, overlap, line-break, and squashed-math issues — splitting slides when needed, never shrinking type. (If the render toolchain is unavailable, the command itself falls back to the no-render method and says so.)

Trigger phrases that should invoke `/audit-and-edit-deck` even if the user doesn't type the slash form: *"audit this slide"*, *"screenshot check"*, *"visual audit"*, *"check for overflow/overlap"*, *"render check"*, *"layout check"*. Not part of the standard editing workflow above — only on explicit request.

## Outlines

Each folder has an `OUTLINE.md`. Three tiers:

- **Root** (`/OUTLINE.md`): folder map + topic→location quick-lookup table.
- **Folder** (`<topic>/OUTLINE.md`): subfolder map + cross-deck pointers.
- **Leaf** (`<topic>/<sub>/OUTLINE.md`): per-deck section table with line numbers, key theorems with line numbers, paired-note summary.

**Read outlines before writing slides** (full rule: `DESIGN_SYSTEM.md` → **OUTLINE.md (per-folder index)** → Read-side rule). Two checks:

- **Series continuity.** When working on a deck, scan the leaf `OUTLINE.md` for earlier decks in the same series — and the parent folder's `OUTLINE.md` for adjacent topics — to see what has already been defined or proved. Refer back; don't redefine.
- **Cross-folder reuse.** When the topic you're writing on may live in another folder (diffusion in `courses/infotheory/` vs `courses/privacy/`; DP in `courses/privacy/lectures/01-dp/` vs `courses/privacy/lectures/04-mia/`; MI bounds in `courses/infotheory/lectures/05-mi/` vs anywhere CLIP comes up), check the root `OUTLINE.md` quick-lookup table first, then the relevant leaf file. Reuse, link, or differentiate — explicit choice.

When a new deck is created (via `scripts/new-talk.sh` or by hand), add a stub for it in the leaf `OUTLINE.md` *immediately* — even before writing slides — so the deck is discoverable.

## Companion files (lectures)

A deck may carry a `<deck>-note.html` speaker script and, when the audience is pitched below the math's level, an optional `<deck>tech.html` technical supplement holding the formal math the main deck keeps as a picture. Both are documented in `DESIGN_SYSTEM.md` (→ **Companion note files** — including the **Migration check**: content trimmed from a slide "because it belongs in the note" must actually land in the note file in the same edit — and **Technical supplement decks**). Register supplements in the leaf `OUTLINE.md`.

## Print-to-PDF

`reference/deck.css` includes an `@media print { @page { size: 1280px 720px; margin: 0 } … }` block.

1. Open the deck in Chrome (`<talk>.html` or `<talk>.standalone.html`).
2. `Cmd+P` → Save as PDF.
3. Margins **None**. Headers/footers **off**. Background graphics **on**.
