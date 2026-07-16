#!/usr/bin/env python3
"""
lint-deck.py — validate a deck HTML against the talks design system.

Checks:
  1. Expected <link>/<script> references to reference/colors_and_type.css,
     reference/deck.css, reference/deck.js are present.
  2. Classes used in the body are all defined in reference/deck.css or
     reference/colors_and_type.css (minus a small allow-list).
  3. No hardcoded colors in inline style="..." attributes — prefer var(--…).
  4. Literal '<' inside $…$/$$…$$ math (breaks KaTeX for every later slide). [error]
  5. Single-backslash KaTeX delimiters in the onload handler ('\(' instead
     of '\\('). [error]
  6. Banned type overrides: .tiny anywhere; .small on <p>/<li>; inline
     font-size on prose tags (p, li, h1-h3).
  7. '$…$' inside SVG <text> (KaTeX skips SVG — renders literally).
  8. Per-deck .page-num injector (duplicate page numbers; .slide-num is canonical).
  9. Mid-sentence em/en-dash or ' -- ' in prose outside .cite lines.
 10. Adjacent .math-block divs with no margin override (~60 px dead space).

Checks 6-10 are skipped for -note.html and .standalone.html files.
Rules: DESIGN_SYSTEM.md (priorities, citations) and GOTCHAS.md (symptoms).

Exit codes: 0 clean, 1 warnings, 2 errors.

Usage:
  scripts/lint-deck.py <file.html> [<file.html> ...]
  scripts/lint-deck.py --all
"""

from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSS_DECK = ROOT / "reference" / "deck.css"
CSS_TYPE = ROOT / "reference" / "colors_and_type.css"
JS_SRC   = ROOT / "reference" / "deck.js"

ALLOW_CLASSES = {
    "katex", "katex-display", "katex-html", "katex-mathml",
    "active", "deck", "filled", "no-footer",
}

ALLOW_INLINE_COLORS = {
    "transparent", "inherit", "currentcolor", "none",
}


def extract_classes(*css_sources: str) -> set[str]:
    out: set[str] = set()
    for css in css_sources:
        out.update(re.findall(r"\.([A-Za-z_][A-Za-z0-9_-]*)", css))
    return out


def classes_used(body: str) -> set[str]:
    tokens: set[str] = set()
    for attr in re.findall(r'class="([^"]+)"', body):
        tokens.update(attr.split())
    return tokens


def style_attr_colors(body: str) -> list[tuple[int, str]]:
    hits: list[tuple[int, str]] = []
    pat = re.compile(r"(#[0-9A-Fa-f]{3,8}\b|rgb[a]?\([^\)]+\)|hsl[a]?\([^\)]+\))")
    for m in re.finditer(r'style="([^"]+)"', body):
        offset = m.start(1)
        for c in pat.finditer(m.group(1)):
            val = c.group(0)
            if val.lower() in ALLOW_INLINE_COLORS:
                continue
            ln = body.count("\n", 0, offset + c.start()) + 1
            hits.append((ln, val))
    return hits


def _line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def strip_blocks(html: str) -> str:
    """Blank out <script>/<style> blocks and HTML comments, preserving offsets."""
    def blank(m: re.Match) -> str:
        return re.sub(r"[^\n]", " ", m.group(0))
    out = re.sub(r"<script\b.*?</script>", blank, html, flags=re.S | re.I)
    out = re.sub(r"<style\b.*?</style>", blank, out, flags=re.S | re.I)
    out = re.sub(r"<!--.*?-->", blank, out, flags=re.S)
    return out


def math_segments(text: str) -> list[tuple[int, str]]:
    """(offset, content) for every $$…$$ and $…$ span, display math first."""
    segs: list[tuple[int, str]] = []
    consumed = []
    for m in re.finditer(r"\$\$(.+?)\$\$", text, re.S):
        segs.append((m.start(1), m.group(1)))
        consumed.append((m.start(), m.end()))
    def in_display(pos: int) -> bool:
        return any(a <= pos < b for a, b in consumed)
    for m in re.finditer(r"\$([^$\n]{1,300}?)\$", text):
        if not in_display(m.start()):
            segs.append((m.start(1), m.group(1)))
    return segs


def check_math_literal_lt(text: str) -> list[str]:
    hits = []
    for off, seg in math_segments(text):
        # HTML lexer eats '<' only when *immediately* followed by a letter (or /!?);
        # '$R < H$' with spaces is safe.
        m = re.search(r"<[a-zA-Z/!?]", seg)
        if m:
            hits.append(f"line~{_line_of(text, off + m.start())}: literal '<' inside math — use &lt; "
                        f"(garbles every later slide; GOTCHAS → 'Equation broken on page N')")
    return hits


def check_katex_delimiters(html: str) -> list[str]:
    if "renderMathInElement" not in html:
        return []
    if re.search(r"left:\s*'\\\(", html) and not re.search(r"left:\s*'\\\\\(", html):
        return ["KaTeX delimiters single-escaped ('\\(' not '\\\\(') — parenthesized prose renders "
                "as math (GOTCHAS → 'KaTeX delimiter escape bug'); match reference/deck-skeleton.html"]
    return []


BODY_REM = 1.5  # flag prose shrunk below ~body size (1.55rem); enlarging is allowed


def _rem_value(css_size: str) -> float | None:
    m = re.match(r"([\d.]+)\s*(rem|em|px)", css_size.strip())
    if not m:
        return None
    v = float(m.group(1))
    return v / 16 if m.group(2) == "px" else v


def check_tiny(body: str) -> list[int]:
    return [_line_of(body, m.start())
            for m in re.finditer(r'<[a-z0-9]+\b[^>]*class="[^"]*\btiny\b', body)]


def check_small_prose(body: str) -> list[int]:
    return [_line_of(body, m.start())
            for m in re.finditer(r'<(?:p|li)\b[^>]*class="[^"]*\bsmall\b', body)]


def check_shrunk_prose(body: str) -> list[int]:
    hits = []
    for m in re.finditer(r'<(?:p|li|h[123])\b[^>]*style="[^"]*font-size:\s*([^;"]+)', body):
        rem = _rem_value(m.group(1))
        if rem is not None and rem < BODY_REM:
            hits.append(_line_of(body, m.start()))
    return hits


def check_svg_text_math(body: str) -> list[int]:
    return [_line_of(body, m.start())
            for m in re.finditer(r"<text\b[^>]*>[^<]*\$", body)]


def check_page_num_injector(html: str) -> list[str]:
    if re.search(r"page-num", html):
        return ["per-deck 'page-num' found — duplicate page numbers; keep only the canonical "
                ".slide-num (GOTCHAS → 'Duplicate page numbers')"]
    return []


def check_dashes(body: str) -> list[int]:
    hits = []
    for i, line in enumerate(body.split("\n"), start=1):
        if 'class="cite' in line:
            continue
        if re.search(r"( — | – | -- )", line):
            hits.append(i)
    return hits


def check_adjacent_math_blocks(body: str) -> list[int]:
    hits = []
    pat = re.compile(
        r'(<div class="math-block"[^>]*>)(?:(?!</div>).)*?</div>\s*(<div class="math-block"[^>]*>)',
        re.S,
    )
    for m in pat.finditer(body):
        if "margin" in m.group(1) or "margin" in m.group(2):
            continue
        hits.append(_line_of(body, m.start()))
    return hits


def _agg(warnings: list[str], lines: list[int], msg: str) -> None:
    if not lines:
        return
    ex = ", ".join(f"line~{ln}" for ln in lines[:3])
    more = f" (+{len(lines) - 3} more)" if len(lines) > 3 else ""
    warnings.append(f"{msg}: {ex}{more}")


def lint_one(path: Path, defined_classes: set[str]) -> int:
    html = path.read_text()
    rel = path.relative_to(ROOT) if ROOT in path.parents else path
    errors: list[str] = []
    warnings: list[str] = []

    is_standalone = path.name.endswith(".standalone.html")
    is_note = path.name.endswith(("-note.html", "-notes.html"))
    # Companion pages (exam sheets, speaker scripts, figure exports) aren't
    # decks — only math-rendering and class/color checks apply to them.
    is_deck = 'class="deck"' in html

    if is_deck and not is_standalone and not is_note:
        # Expect canonical <link>/<script> refs.
        required = [
            (r'href="[^"]*colors_and_type\.css"',  "colors_and_type.css link"),
            (r'href="[^"]*deck\.css"',             "deck.css link"),
            (r'src="[^"]*deck\.js"',               "deck.js script"),
        ]
        for pat, name in required:
            if not re.search(pat, html):
                errors.append(f"missing expected {name}")

    body_match = re.search(r"<body[^>]*>(.*?)</body>", html, re.S)
    body = body_match.group(1) if body_match else ""

    # Include classes defined inside the deck's own <style> blocks.
    local_styles = "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", html, re.S))
    all_defined = defined_classes | extract_classes(local_styles)

    used = classes_used(body)
    unknown = {c for c in used if c not in all_defined and c not in ALLOW_CLASSES}
    if unknown:
        warnings.append(f"unknown classes (define in reference/deck.css or remove): {sorted(unknown)}")

    hits = style_attr_colors(body)
    if hits:
        ex = "; ".join(f"line~{ln}: {v}" for ln, v in hits[:5])
        warnings.append(
            f"hardcoded colors in inline style= ({len(hits)} occurrence(s)); prefer var(--…). e.g. {ex}"
        )

    # Math-rendering breakers (apply to decks and notes alike).
    clean = strip_blocks(html)
    errors.extend(check_math_literal_lt(clean))
    errors.extend(check_katex_delimiters(html))

    # Style checks — decks only (notes are prose; standalones are build artifacts).
    if is_deck and not is_standalone and not is_note and body_match:
        # Blank everything outside <body> so reported line numbers are file-accurate.
        b0, b1 = body_match.start(1), body_match.end(1)
        clean_body = re.sub(r"[^\n]", " ", clean[:b0]) + clean[b0:b1]
        _agg(warnings, check_tiny(clean_body),
             ".tiny is banned everywhere (Priority 0)")
        _agg(warnings, check_small_prose(clean_body),
             ".small on <p>/<li> prose is banned (Priority 0; move to -note.html)")
        _agg(warnings, check_shrunk_prose(clean_body),
             f"inline font-size < {BODY_REM}rem on prose (Priority 0 — de-emphasis is by color, not size)")
        _agg(warnings, check_svg_text_math(clean_body),
             "'$…$' inside SVG <text> renders literally — use an HTML span overlay (GOTCHAS)")
        warnings.extend(check_page_num_injector(html))
        _agg(warnings, check_dashes(clean_body),
             "mid-sentence dash in prose — colon/comma/parens instead (Priority 1)")
        _agg(warnings, check_adjacent_math_blocks(clean_body),
             'adjacent .math-block divs w/o margin override — merge into one aligned block or '
             'style="margin: 8px 0;" (DESIGN_SYSTEM → Stacked equations)')

    if not errors and not warnings:
        print(f"ok    {rel}")
        return 0

    status = "ERROR " if errors else "warn  "
    print(f"{status}{rel}")
    for e in errors:
        print(f"  [error] {e}")
    for w in warnings:
        print(f"  [warn ] {w}")
    return 2 if errors else 1


def discover() -> list[Path]:
    paths: list[Path] = [ROOT / "reference" / "deck-skeleton.html"]
    skip_dirs = {"notes", "figs", "latex", "old", "overleaf"}
    content_dirs = [ROOT / "courses", ROOT / "talks"]
    for cdir in content_dirs:
        if not cdir.is_dir():
            continue
        for html in sorted(cdir.rglob("*.html")):
            if html.name.endswith(".standalone.html"):
                continue
            if any(part in skip_dirs for part in html.relative_to(cdir).parts):
                continue
            paths.append(html)
    return [p for p in paths if p.exists()]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()

    if not CSS_DECK.exists() or not JS_SRC.exists() or not CSS_TYPE.exists():
        sys.exit("error: canonical reference files missing")

    defined = extract_classes(CSS_DECK.read_text(), CSS_TYPE.read_text())

    if args.all:
        targets = discover()
    else:
        if not args.files:
            ap.error("pass one or more HTML files, or --all")
        targets = [Path(f).resolve() for f in args.files]

    worst = 0
    for t in targets:
        if not t.exists():
            print(f"ERROR {t}: does not exist")
            worst = max(worst, 2)
            continue
        worst = max(worst, lint_one(t, defined))
    return worst


if __name__ == "__main__":
    raise SystemExit(main())
