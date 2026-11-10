#!/usr/bin/env python3
"""Random-mixture illustration for lec12 S75 (evidence E17).

Original teaching illustration of the reductions output (E10), not an
Agarwal et al. result. Two hypothetical classifiers with selection
probabilities by group:
    h1: A 0.8, B 0.4
    h2: A 0.2, B 0.6
A fair coin, flipped independently of group, picks h1 or h2 per decision.
Expected selection = 0.5*h1 + 0.5*h2 = (0.5, 0.5).
No utility/error numbers; no optimality or convergence claim; finite
observed counts need not be exactly equal. Not score averaging.
No random inputs. Run:  python3 reductions_mix.py [outdir]
"""
from fractions import Fraction as F
import os
import sys

H = {"h1": {"A": F(8, 10), "B": F(4, 10)},
     "h2": {"A": F(2, 10), "B": F(6, 10)}}
P = {"h1": F(1, 2), "h2": F(1, 2)}
BLUE = "#003876"
INK = "#1a1a1a"
GRAY = "#4b5563"
TRACK = "#e5e7eb"


def mixture():
    mix = {g: sum(P[h] * H[h][g] for h in H) for g in "AB"}
    assert sum(P.values()) == 1
    assert mix == {"A": F(1, 2), "B": F(1, 2)}
    return mix


def pct(x):
    return f"{round(100 * x)}%"


def marker(mid, color):
    return (f'<marker id="{mid}" markerUnits="userSpaceOnUse" markerWidth="22" '
            f'markerHeight="22" refX="20" refY="11" orient="auto">'
            f'<path d="M0,0 L20,11 L0,22 Z" fill="{color}"/></marker>')


def bars(x, y, rates, barlen=200):
    """Two rows (A, B) of selection bars starting at (x, y)."""
    s = []
    for i, g in enumerate("AB"):
        yy = y + i * 52
        s.append(f'<text x="{x}" y="{yy + 24}" font-size="26" font-weight="700" fill="{INK}">{g}</text>')
        s.append(f'<rect x="{x + 36}" y="{yy}" width="{barlen}" height="32" fill="{TRACK}"/>')
        s.append(f'<rect x="{x + 36}" y="{yy}" width="{float(rates[g]) * barlen:.0f}" height="32" fill="{BLUE}"/>')
        s.append(f'<text x="{x + 36 + barlen + 12}" y="{yy + 25}" font-size="26" font-weight="700" '
                 f'fill="{INK}">{pct(rates[g])}</text>')
    return s


def svg(mix):
    W, Hh = 1130, 400
    o = [f'<svg class="p4-fig" viewBox="0 0 {W} {Hh}" role="img" '
         f'aria-label="A fair coin that ignores group picks classifier h1 (selects 80% of A, 40% of B) '
         f'or h2 (20% of A, 60% of B); expected selection is 50% in both groups" '
         f'xmlns="http://www.w3.org/2000/svg">',
         f'<defs>{marker("p4-ar-mix", GRAY)}</defs>']
    # coin box
    cx0, cy0, cw, ch = 4, 140, 230, 120
    o.append(f'<rect x="{cx0}" y="{cy0}" width="{cw}" height="{ch}" rx="14" fill="#fff" '
             f'stroke="{GRAY}" stroke-width="3"/>')
    o.append(f'<text x="{cx0 + cw / 2}" y="{cy0 + 50}" font-size="26" font-weight="700" '
             f'fill="{INK}" text-anchor="middle">Fair coin</text>')
    o.append(f'<text x="{cx0 + cw / 2}" y="{cy0 + 88}" font-size="22" fill="{GRAY}" '
             f'text-anchor="middle">ignores group</text>')
    # classifier cards
    kx, kw, kh = 330, 400, 160
    cards = {"h1": 10, "h2": 230}
    for h, ky in cards.items():
        o.append(f'<rect x="{kx}" y="{ky}" width="{kw}" height="{kh}" rx="14" fill="#fff" '
                 f'stroke="{BLUE}" stroke-width="3"/>')
        o.append(f'<text x="{kx + 20}" y="{ky + 38}" font-size="26" font-weight="700" '
                 f'fill="{BLUE}">Classifier {h}: selects</text>')
        o += bars(kx + 24, ky + 56, H[h])
        # coin -> card arrow: from coin right edge to card left edge
        y1 = cy0 + (35 if h == "h1" else ch - 35)
        y2 = ky + kh / 2
        o.append(f'<line x1="{cx0 + cw}" y1="{y1}" x2="{kx - 2}" y2="{y2}" stroke="{GRAY}" '
                 f'stroke-width="4" marker-end="url(#p4-ar-mix)"/>')
        o.append(f'<text x="{(cx0 + cw + kx) / 2 - 8}" y="{(y1 + y2) / 2 + (-16 if h == "h1" else 34)}" '
                 f'font-size="26" font-weight="700" fill="{GRAY}" text-anchor="middle">½</text>')
    # result box
    rx0, ry0, rw, rh = 830, 110, 296, 180
    o.append(f'<rect x="{rx0}" y="{ry0}" width="{rw}" height="{rh}" rx="14" fill="#eef2f7" '
             f'stroke="{BLUE}" stroke-width="3"/>')
    o.append(f'<text x="{rx0 + rw / 2}" y="{ry0 + 40}" font-size="26" font-weight="700" '
             f'fill="{BLUE}" text-anchor="middle">Expected selection</text>')
    o += bars(rx0 + 18, ry0 + 70, mix, barlen=160)
    for h, ky in cards.items():
        y1 = ky + kh / 2
        y2 = ry0 + (45 if h == "h1" else rh - 45)
        o.append(f'<line x1="{kx + kw}" y1="{y1}" x2="{rx0 - 2}" y2="{y2}" stroke="{GRAY}" '
                 f'stroke-width="4" marker-end="url(#p4-ar-mix)"/>')
    o.append('</svg>')
    return "\n".join(o)


def main():
    mix = mixture()
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
    print("expected selection", {g: str(v) for g, v in mix.items()})
    with open(os.path.join(out, "reductions-mix-s75.svg"), "w") as f:
        f.write(svg(mix) + "\n")


if __name__ == "__main__":
    main()
