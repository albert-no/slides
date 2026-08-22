#!/usr/bin/env python3
"""
doc-index-lint.py — keep the section-entry index in the reference docs honest.

`DESIGN_SYSTEM.md` and `GOTCHAS.md` are reference material that must be read by
section, never cover to cover (CLAUDE.md → Reading budget). A prose rule saying
so was ignored 91 times in 2026-07/08, because grepping for a section is more
work than reading the file. So each doc carries a generated index giving every
section's exact line range and ready-to-paste Read arguments:

  <!-- doc-index:start -->
  | § | Section | When you need it | Lines | Read |
  ...
  <!-- doc-index:end -->

The "When you need it" column is hand-written and preserved across regeneration,
keyed by section number. Everything else is derived from the `^## ` headings.

A stale index is worse than none — it sends the reader to the wrong lines — so
this script is the guard:

  [error] index block missing or malformed
  [error] a section is missing from the index, or listed but no longer exists
  [error] a line range or Read argument is out of date
  [warn ] a section has no hand-written "when you need it" text

Exit codes: 0 clean, 1 warnings, 2 errors.

Usage:
  scripts/doc-index-lint.py             # check the default docs
  scripts/doc-index-lint.py --fix       # rewrite the indexes in place
  scripts/doc-index-lint.py <file.md> [...] [--fix]
"""

from __future__ import annotations
import argparse
import pathlib
import re
import sys

DEFAULT_DOCS = ["DESIGN_SYSTEM.md", "GOTCHAS.md"]
START = "<!-- doc-index:start -->"
END = "<!-- doc-index:end -->"
HEADING = re.compile(r"^## (?:(\d+)\.\s*)?(.+?)\s*$")
ROW = re.compile(r"^\|\s*(\d+)\s*\|(.*)\|(.*)\|(.*)\|(.*)\|\s*$")


def sections(lines: list[str]) -> list[tuple[int, str, int]]:
    """[(number, title, start_line_1indexed)] for numbered `## N. Title` headings."""
    out = []
    for i, line in enumerate(lines, start=1):
        m = HEADING.match(line)
        if m and m.group(1):
            out.append((int(m.group(1)), m.group(2), i))
    return out


def ranges(lines: list[str]) -> list[tuple[int, str, int, int]]:
    """[(number, title, start, end)] — a section runs to the line before the next."""
    secs = sections(lines)
    out = []
    for idx, (num, title, start) in enumerate(secs):
        end = secs[idx + 1][2] - 1 if idx + 1 < len(secs) else len(lines)
        while end > start and not lines[end - 1].strip():
            end -= 1
        out.append((num, title, start, end))
    return out


def existing_notes(lines: list[str]) -> dict[int, str]:
    """Hand-written 'when you need it' text, keyed by section number."""
    notes: dict[int, str] = {}
    inside = False
    for line in lines:
        if line.strip() == START:
            inside = True
            continue
        if line.strip() == END:
            break
        if inside:
            m = ROW.match(line)
            if m:
                notes[int(m.group(1))] = m.group(3).strip()
    return notes


def render(rs: list[tuple[int, str, int, int]], notes: dict[int, str]) -> list[str]:
    body = [
        START,
        "",
        "| § | Section | When you need it | Lines | Read |",
        "|---|---|---|---|---|",
    ]
    for num, title, start, end in rs:
        note = notes.get(num, "")
        body.append(
            f"| {num} | {title} | {note} | {start}–{end} | "
            f"`offset={start}, limit={end - start + 1}` |"
        )
    body += ["", END]
    return body


def splice(lines: list[str], block: list[str]) -> list[str] | None:
    try:
        i = next(n for n, l in enumerate(lines) if l.strip() == START)
        j = next(n for n, l in enumerate(lines) if l.strip() == END)
    except StopIteration:
        return None
    if j < i:
        return None
    return lines[:i] + block + lines[j + 1:]


def process(path: pathlib.Path, fix: bool) -> tuple[int, list[str]]:
    """Returns (worst severity 0/1/2, messages)."""
    lines = path.read_text().splitlines()
    if START not in [l.strip() for l in lines]:
        return 2, [f"[error] {path}: no {START} block — add one where the index belongs"]

    notes = existing_notes(lines)
    msgs: list[str] = []

    # The index sits inside the file, so writing it shifts the very line numbers
    # it reports. Iterate to a fixed point (converges once the block stops
    # changing height).
    current = lines
    for _ in range(10):
        rs = ranges(current)
        nxt = splice(current, render(rs, notes))
        if nxt is None:
            return 2, [f"[error] {path}: malformed doc-index block (start/end out of order)"]
        if nxt == current:
            break
        current = nxt
    else:
        return 2, [f"[error] {path}: index line numbers did not converge"]

    for num, title, _, _ in ranges(current):
        if not notes.get(num):
            msgs.append(f"[warn ] {path}: §{num} {title} — no 'when you need it' text")

    stale = [n for n in notes if n not in {r[0] for r in ranges(current)}]
    for n in stale:
        msgs.append(f"[error] {path}: index lists §{n}, which no longer exists")

    if current != lines:
        if fix:
            path.write_text("\n".join(current) + "\n")
            msgs.insert(0, f"[fixed] {path}: index regenerated ({len(ranges(current))} sections)")
            sev = 2 if stale else (1 if any(m.startswith("[warn") for m in msgs) else 0)
            return sev if stale else 0, msgs
        msgs.insert(0, f"[error] {path}: index is stale — run scripts/doc-index-lint.py --fix")
        return 2, msgs

    sev = 2 if stale else (1 if msgs else 0)
    if not msgs:
        msgs.append(f"ok    {path} ({len(ranges(current))} sections)")
    return sev, msgs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("docs", nargs="*", default=None)
    ap.add_argument("--fix", action="store_true", help="rewrite indexes in place")
    args = ap.parse_args()

    root = pathlib.Path(__file__).resolve().parent.parent
    docs = [pathlib.Path(d) for d in (args.docs or [root / d for d in DEFAULT_DOCS])]

    worst = 0
    for d in docs:
        if not d.exists():
            print(f"[error] {d}: not found")
            worst = 2
            continue
        sev, msgs = process(d, args.fix)
        worst = max(worst, sev)
        for m in msgs:
            print(m)
    return worst


if __name__ == "__main__":
    sys.exit(main())
