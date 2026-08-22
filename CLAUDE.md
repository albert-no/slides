# Talks repo

Slide decks for academic talks — conference presentations and master-level lectures. **Math-heavy**: rigorous statement, rigorous proof, high-level intuition. **Minimal design**: short abstract phrases, never full sentences (7×7 rule).

Two formats: **custom HTML** (`<talk>/<talk>.html`, preferred) — single page, one `.active` slide, scaled to viewport by JS, linking `reference/` for CSS/JS/fonts/logo. And **Marp markdown** — copy `template.md`, run `marp <file>.md --pdf`.

## Reading budget (read this first)

These docs are reference material, not briefing material. Reading them cover-to-cover is the single largest avoidable cost in this repo — in 2026-07/08 it burned ~2.2M tokens, more than every screenshot audit combined.

| Doc | How to enter it |
|---|---|
| `DESIGN_SYSTEM.md` (§1–§12) | **Never read whole.** Its section index gives every section's line range and literal `offset=…, limit=…` — read §1, then the one section your task needs, using those arguments. |
| `GOTCHAS.md` (§1–§9) | **Never read whole.** `grep` your symptom, or jump to a category with its index `Read` arguments. |
| `OUTLINE.md` | Read the leaf for the folder you're editing. Root only for cross-folder lookup. |
| `reference/deck.css` | Authoritative for any class's real behavior. Grep the selector. |

Three hard rules:

1. **Enter by section, never whole.** Open the doc's index block (the first ~20 lines), take the `offset`/`limit` for the section you need, and read exactly that. A whole-file read of `DESIGN_SYSTEM.md` costs ~6k tokens against ~500–1.5k for a section; of `GOTCHAS.md`, ~4.7k against ~600. Read each section at most once per session — re-opening one you already read is a bug. If a range looks wrong, `python3 scripts/doc-index-lint.py --fix`; do not read the whole file to find your place.
2. **Screenshot audits render at `-r 60`.** A full-deck pass is ~480 tokens/slide at 60 DPI and ~1,330 at 150 — 3× for detail the audit doesn't check. `-r 150` is for a *single* page where fine text is genuinely in question.
3. **Re-read only what changed.** The full-deck read happens exactly once per audit; every later pass re-renders and re-reads only the slides edited since.

## Non-negotiables

The four ranked priorities in `DESIGN_SYSTEM.md` §1 govern every authoring and editing decision: **0** font sizes · **1** density · **2** overflow (with the vertical-budget px table) · **3** empty space. Never shrink type to make content fit — split the slide.

**Default to visually rich slides.** Every content slide should carry a diagram, figure, chart, or SVG; text-only bullets are a fallback. When a real figure can't be made now, leave `<!-- TODO real figure: … -->` rather than shipping bare bullets. Keep slides self-contained — no "next week" / "(Wk N)" cross-references.

## Task → entry point

| Task | Start |
|---|---|
| New deck | `scripts/new-talk.sh`, then DESIGN_SYSTEM §2 (anatomy, slide-count norms, exemplars). Add an `OUTLINE.md` stub immediately. |
| Edit / add slides | Leaf `OUTLINE.md` first, then DESIGN_SYSTEM §7 patterns → copy the exemplar's markup. |
| Fix overflow | DESIGN_SYSTEM §1 → Priority 2 (vertical budget); GOTCHAS §3. |
| Visual audit | `/audit-and-edit-deck` — on explicit request only. |
| Add a visual / capture a figure | DESIGN_SYSTEM §8 — capture a real figure with citation before redrawing one. |
| Theorem / proof / build-up | DESIGN_SYSTEM §5. |
| Debug a rendering symptom | `grep` your symptom in `GOTCHAS.md`. |
| Distribute | `python3 scripts/bundle.py <talk>/<talk>.html`. |

## Visual identity

White background. Yonsei Blue (`#003876`) accent. Yonsei TTFs (`reference/fonts/`) with Noto Sans fallback. Yonsei emblem (`reference/kor-eng2.png`) top-right on the title slide.

## Repo layout

```
courses/<course>/<topic>/<deck>.html   semester-long lecture series
talks/<name>/<deck>.html               standalone research presentations
reference/                             canonical CSS/JS/fonts/logo — single source of truth
  colors_and_type.css  @font-face + tokens
  deck.css             slide engine + components
  deck.js              scale / nav / progress / brand-footer
  deck-skeleton.html   starter (cloned by new-talk.sh)
scripts/
  new-talk.sh    scaffold a deck (--course for lectures)
  bundle.py      → <name>.standalone.html for distribution (gitignored)
  lint-deck.py   canonical-CSS + mechanical style validation
  find-wordy.py  flag prose over the 7×7 word ceiling
  find-dense.py  flag over-stuffed slides
  outline-lint.py verify OUTLINE.md file:line pointers
  doc-index-lint.py verify/regenerate the section index in the reference docs
OUTLINE.md       per-folder content index (root / topic / leaf)
backup/          dated snapshots of docs before major rewrites
```

Only authoring source and image assets are committed. `*.standalone.html` is a build artifact.

## Editing workflow

1. Edit `<talk>/<talk>.html`.
2. Preview in Chrome (`reference/` must be alongside — it is).
3. `python3 scripts/lint-deck.py <deck>.html` (or `--all`). Errors (`<` inside math, KaTeX delimiter escape) break rendering — fix immediately. Warnings are Priority-0/1 violations.
4. `python3 scripts/find-wordy.py <deck>.html` after drafting prose-heavy slides; `find-dense.py` for over-stuffed ones.
5. **Update `OUTLINE.md`** — any added/removed slide, renamed section, changed line range, or added/removed cited theorem, in the *same* edit. Line numbers are read as authoritative pointers. Verify with `python3 scripts/outline-lint.py`. Full rule: DESIGN_SYSTEM §10.
6. Distribute: `python3 scripts/bundle.py <talk>/<talk>.html`.

**Edited `DESIGN_SYSTEM.md` or `GOTCHAS.md`?** Run `python3 scripts/doc-index-lint.py --fix` in the same change — any inserted or deleted line shifts the section index, and a stale index sends the next reader to the wrong lines. The linter exits 2 when it is out of date.

**If the toolchain is missing** — attempt the real tools first. Only when `command -v google-chrome pdftoppm python3 mutool convert gs` is empty and nothing installs, use DESIGN_SYSTEM §11 (grep slide map, budget arithmetic, targeted-grep lint). Say so explicitly in your report: that fallback cannot catch visual overlap, squashed math spacing, or drifted SVG overlays.

## Screenshot audit (on request)

`lint-deck.py` catches structural issues, not visual ones. For overflow / overlap / line breaks, use **`/audit-and-edit-deck`** (see `.claude/commands/audit-and-edit-deck.md`):

```
/audit-and-edit-deck <deck>.html    # one deck
/audit-and-edit-deck <folder>/      # every deck in the folder
/audit-and-edit-deck                # the single deck in cwd
```

It renders each slide to PNG via headless Chrome + `pdftoppm -r 60`, reads them, and fixes issues — splitting slides when needed, never shrinking type. Trigger phrases that should invoke it even without the slash form: *"audit this slide"*, *"screenshot check"*, *"visual audit"*, *"check for overflow/overlap"*, *"render check"*, *"layout check"*. Not part of the standard workflow — explicit request only.

## Outlines

Three tiers: **root** (folder map + topic→location lookup), **folder** (subfolder map + cross-deck pointers), **leaf** (per-deck section table with line numbers, key theorems, paired-note summary).

**Read the relevant outline before writing slides.** Two checks: **series continuity** — scan the leaf for earlier decks in the series so you refer back instead of redefining; **cross-folder reuse** — when a topic may live in another track (diffusion in `infotheory/` vs `privacy/`; DP in `01-dp/` vs `04-mia/`), check the root lookup table first, then the other leaf. Reuse, link, or differentiate — explicitly. Full rules: DESIGN_SYSTEM §10.

New deck → add its stub to the leaf `OUTLINE.md` *immediately*, before writing slides.

## Companion files

A deck may carry a `<deck>-note.html` speaker script and, where the audience sits below the math's level, a `<deck>tech.html` technical supplement holding the formal math. Both in DESIGN_SYSTEM §9 — including the **migration check** (content trimmed "because it belongs in the note" must actually land there in the same edit). Register supplements in the leaf `OUTLINE.md`.

## Agent workflow

- **One agent at a time.** A slide series is revised sequentially, one deck to completion before the next. Never launch parallel agents on the same series — a killed parallel wave is pure duplicate cost.
- **Audit incrementally** — see Reading budget rule 3.
- **Subagents inherit these rules.** A subagent doing deck work reads by section too; delegation doesn't reset the reading budget.

## Print-to-PDF

`reference/deck.css` has an `@media print { @page { size: 1280px 720px; margin: 0 } … }` block. Open in Chrome → `Cmd+P` → Save as PDF, margins **None**, headers/footers **off**, background graphics **on**.
