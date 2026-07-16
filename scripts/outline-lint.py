#!/usr/bin/env python3
"""
outline-lint.py — verify that OUTLINE.md `file:line` pointers are not stale.

OUTLINE.md files (root / folder / leaf) cite deck locations as
`path/to/deck.html:123`, `deck.html:63-232`, or `deck.html:97, :379, :437`.
Line numbers are read as authoritative pointers (CLAUDE.md → Outlines), so a
stale one is worse than none. This script checks every pointer in every
OUTLINE.md:

  [error] cited file does not exist (tried outline-relative, repo-relative,
          then a unique repo-wide basename search)
  [error] cited line / range end exceeds the file's length
  [warn ] basename matches multiple files (ambiguous — qualify the path)

Placeholder patterns (`-note.html`, `lecNNtech.html`), schemeless URLs, and
historical mentions (pointer followed by retired/renamed/removed/deleted/
legacy within a few words) are ignored.

It cannot verify that a line still holds the *claimed* content — after big
edits, spot-check the cited lines. Exit codes: 0 clean, 1 warnings, 2 errors.

Usage:
  scripts/outline-lint.py            # check every OUTLINE.md in the repo
  scripts/outline-lint.py <OUTLINE.md> [...]
"""

from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EXTS = r"(?:html|tex|md|css|js|py|png|pdf|ipynb)"
# `file.ext:12`, `file.ext:12-34`, plus `, :56` continuations bound to the same file.
PTR = re.compile(
    rf"([A-Za-z0-9_\-./]+\.{EXTS})((?::\d+(?:-\d+)?)(?:,\s*:\d+(?:-\d+)?)*)?"
)
LINEREF = re.compile(r":(\d+)(?:-(\d+))?")

_len_cache: dict[Path, int] = {}


def file_lines(p: Path) -> int:
    if p not in _len_cache:
        _len_cache[p] = p.read_text(errors="replace").count("\n") + 1
    return _len_cache[p]


def skip_cited(cited: str) -> bool:
    if cited.startswith(("http", "www.", "-", ".")):
        return True
    if "NN" in cited or "OUTLINE" in cited:
        return True
    # Schemeless URL: first path segment looks like a domain.
    first = cited.split("/", 1)[0]
    return "/" in cited and "." in first


def resolve(cited: str, outline_dir: Path) -> tuple[Path | None, str | None]:
    """Return (path, warning) — warning set for ambiguous basename hits."""
    for base in (outline_dir, ROOT):
        cand = (base / cited).resolve()
        if cand.is_file():
            return cand, None
    # House style cites paths relative to the sentence's context — accept a
    # unique repo-wide match for the cited tail silently.
    tail = Path(cited).name
    hits = [p for p in ROOT.rglob(tail)
            if ".git" not in p.parts
            and not p.name.endswith(".standalone.html")
            and str(p).endswith(cited.lstrip("./"))]
    if not hits:
        hits = [p for p in ROOT.rglob(tail)
                if ".git" not in p.parts and not p.name.endswith(".standalone.html")]
    if len(hits) > 1:
        # Prefer a unique match under the outline's own folder.
        local = [p for p in hits if p.is_relative_to(outline_dir)]
        if len(local) == 1:
            return local[0], None
    if len(hits) == 1:
        return hits[0], None
    if len(hits) > 1:
        return None, f"ambiguous basename '{cited}' ({len(hits)} matches — qualify the path)"
    return None, None


def lint_outline(outline: Path) -> tuple[int, int]:
    text = outline.read_text()
    rel = outline.relative_to(ROOT)
    errors: list[str] = []
    warnings: list[str] = []

    for m in PTR.finditer(text):
        cited, refs = m.group(1), m.group(2) or ""
        if skip_cited(cited):
            continue
        if re.match(r"[`'\")\s]{0,4}\s*\(?(retired|renamed|removed|deleted|legacy)",
                    text[m.end():m.end() + 16]):
            continue
        ln = text.count("\n", 0, m.start()) + 1
        path, note = resolve(cited, outline.parent)
        if path is None:
            if note:
                warnings.append(f"line {ln}: {note}")
            else:
                errors.append(f"line {ln}: cited file not found: {cited}")
            continue
        total = file_lines(path)
        for r in LINEREF.finditer(refs):
            hi = int(r.group(2) or r.group(1))
            if hi > total:
                errors.append(
                    f"line {ln}: stale pointer {cited}{r.group(0)} — file has only {total} lines"
                )

    if not errors and not warnings:
        print(f"ok    {rel}")
        return 0, 0
    print(f"{'ERROR' if errors else 'warn '} {rel}")
    for e in errors:
        print(f"  [error] {e}")
    for w in warnings:
        print(f"  [warn ] {w}")
    return len(errors), len(warnings)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()

    targets = ([Path(f).resolve() for f in args.files] if args.files
               else sorted(p for p in ROOT.rglob("OUTLINE.md") if ".git" not in p.parts))
    if not targets:
        sys.exit("no OUTLINE.md files found")

    n_err = n_warn = 0
    for t in targets:
        if not t.exists():
            print(f"ERROR {t}: does not exist")
            n_err += 1
            continue
        e, w = lint_outline(t)
        n_err += e
        n_warn += w
    print(f"\n{n_err} stale/missing pointer(s), {n_warn} warning(s) across {len(targets)} OUTLINE.md file(s)")
    return 2 if n_err else (1 if n_warn else 0)


if __name__ == "__main__":
    raise SystemExit(main())
