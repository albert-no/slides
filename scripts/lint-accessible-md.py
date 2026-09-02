#!/usr/bin/env python3
"""Validate the screen-reader Markdown editions of the course notes.

Usage:  python3 scripts/lint-accessible-md.py <file.md> [...]
        python3 scripts/lint-accessible-md.py --all

These files are read by a blind student through a Markdown-to-braille/speech
converter, so they must be plain ASCII (outside nothing -- LaTeX included),
have balanced math delimiters, a clean heading hierarchy, no leftover HTML,
and no references to things only a sighted reader can see.
"""
import re
import sys
import glob

VISUAL = re.compile(
    r"\b(the slides?|the deck|on the slide|as shown|shown below|see (the )?figure"
    r"|the figure (above|below|on)|the (plot|diagram|picture) (above|below))\b",
    re.I,
)
HTMLISH = re.compile(r"&[a-z]+;|&#\d+;|</?(p|div|span|em|strong|ul|li|ol|section|code|a|br|h[1-6])\b|\\\(|\\\[")


def check(path):
    errs, warns = [], []
    raw = open(path, "rb").read()
    try:
        text = raw.decode("ascii")
    except UnicodeDecodeError:
        text = raw.decode("utf-8")
        for i, line in enumerate(text.splitlines(), 1):
            if any(ord(c) > 127 for c in line):
                bad = "".join(sorted({c for c in line if ord(c) > 127}))
                errs.append(f"{path}:{i}: non-ASCII character(s) {bad!r}")

    if text.count("$$") % 2:
        errs.append(f"{path}: odd number of '$$' display-math delimiters")
    if text.replace("$$", "").count("$") % 2:
        errs.append(f"{path}: odd number of inline '$' delimiters")

    prev = 0
    seen_h1 = False
    for i, line in enumerate(text.splitlines(), 1):
        m = re.match(r"(#+)\s", line)
        if m:
            lvl = len(m.group(1))
            if lvl == 1:
                if seen_h1:
                    warns.append(f"{path}:{i}: second level-1 heading")
                seen_h1 = True
            if prev and lvl > prev + 1:
                errs.append(f"{path}:{i}: heading jumps from h{prev} to h{lvl}")
            prev = lvl
        if HTMLISH.search(line):
            errs.append(f"{path}:{i}: leftover HTML/TeX-HTML markup: {line.strip()[:70]}")
        if VISUAL.search(line):
            warns.append(f"{path}:{i}: visual reference: {VISUAL.search(line).group(0)}")
        if re.search(r"\bslide\s+\d+", line, re.I):
            warns.append(f"{path}:{i}: points at a slide number")
    if not seen_h1:
        errs.append(f"{path}: no level-1 title heading")
    return errs, warns


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 1
    if args == ["--all"]:
        args = sorted(glob.glob("courses/deepmath/*/*-note.md"))
        if not args:
            args = sorted(glob.glob("*/*-note.md"))
    n_err = 0
    for path in args:
        errs, warns = check(path)
        for e in errs:
            print("ERROR  " + e)
        for w in warns:
            print("warn   " + w)
        n_err += len(errs)
        if not errs and not warns:
            lines = sum(1 for _ in open(path))
            print(f"ok     {path} ({lines} lines)")
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main())
