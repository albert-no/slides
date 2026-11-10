#!/usr/bin/env python3
"""Reweighing toy example for lec12 S37/S38 (evidence E08).

Kamiran and Calders (KAIS 33, 2012, Sec. 5.2): weight of a (group, label)
cell = independence-expected share / observed share.

Inputs (baseline toy, 100 training examples):
    group A: 20 positive, 30 negative
    group B: 40 positive, 10 negative
Outputs: exact weights (3/2, 2/3, 3/4, 2), weighted cells (30, 20, 30, 20),
positive share 60% in each weighted group, and two inline SVG fragments:
    reweighing-s37.svg  one cell (A, positive): same 20 examples, weight 3/2
    reweighing-s38.svg  recorded vs weighted counts, stacked bars
No random inputs. Run:  python3 reweighing.py [outdir]
"""
from fractions import Fraction as F
import os
import sys

COUNTS = {("A", "+"): 20, ("A", "-"): 30, ("B", "+"): 40, ("B", "-"): 10}
BLUE = "#003876"
INK = "#1a1a1a"
GRAY = "#4b5563"


def weights(counts):
    n = sum(counts.values())
    groups = sorted({g for g, _ in counts})
    labels = sorted({y for _, y in counts})
    pg = {g: F(sum(counts[(g, y)] for y in labels), n) for g in groups}
    py = {y: F(sum(counts[(g, y)] for g in groups), n) for y in labels}
    w = {}
    for (g, y), c in counts.items():
        if c == 0:
            raise ValueError(f"empty cell {(g, y)}: reweighing cannot repair it")
        w[(g, y)] = pg[g] * py[y] / F(c, n)
    return n, pg, py, w


def check(n, pg, py, w):
    assert n == 100
    assert w == {("A", "+"): F(3, 2), ("A", "-"): F(2, 3),
                 ("B", "+"): F(3, 4), ("B", "-"): F(2)}
    wc = {k: COUNTS[k] * w[k] for k in COUNTS}
    assert wc == {("A", "+"): 30, ("A", "-"): 20, ("B", "+"): 30, ("B", "-"): 20}
    for g in "AB":
        assert wc[(g, "+")] / (wc[(g, "+")] + wc[(g, "-")]) == F(3, 5)
    assert sum(wc.values()) == n
    return wc


def frac(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def marker(mid, color):
    # userSpaceOnUse: tip at refX so the line end touches the target.
    return (f'<marker id="{mid}" markerUnits="userSpaceOnUse" markerWidth="22" '
            f'markerHeight="22" refX="20" refY="11" orient="auto">'
            f'<path d="M0,0 L20,11 L0,22 Z" fill="{color}"/></marker>')


def svg_s37():
    """Cell (A, +): observed 20 of 100, expected 0.5 * 0.6 = 30 of 100."""
    W, H = 1130, 250
    o = [f'<svg class="p4-fig" viewBox="0 0 {W} {H}" role="img" '
         f'aria-label="Twenty recorded positive examples of group A; each gets weight 1.5, '
         f'so the same twenty examples count as 30 of 100" xmlns="http://www.w3.org/2000/svg">',
         f'<defs>{marker("p4-ar-s37", GRAY)}</defs>']
    # left: 20 dots r=15, 2 rows x 10, pitch 40
    lx, top = 30, 110
    o.append(f'<text x="{lx + 190}" y="34" font-size="26" font-weight="700" fill="{INK}" '
             f'text-anchor="middle">Recorded: 20 of 100</text>')
    o.append(f'<text x="{lx + 190}" y="70" font-size="22" fill="{GRAY}" '
             f'text-anchor="middle">observed share 20%</text>')
    for r in range(2):
        for c in range(10):
            o.append(f'<circle cx="{lx + 10 + c * 40}" cy="{top + r * 44}" r="15" fill="{BLUE}"/>')
    # arrow
    ax1, ax2, ay = 440, 590, top + 22
    o.append(f'<line x1="{ax1}" y1="{ay}" x2="{ax2}" y2="{ay}" stroke="{GRAY}" '
             f'stroke-width="4" marker-end="url(#p4-ar-s37)"/>')
    o.append(f'<text x="{(ax1 + ax2) / 2}" y="{ay - 18}" font-size="28" font-weight="700" '
             f'fill="{BLUE}" text-anchor="middle">× 1.5 each</text>')
    # right: same 20 dots, area x1.5 (radius x sqrt 1.5)
    rr = round(15 * 1.5 ** 0.5, 1)
    rx = 620
    o.append(f'<text x="{rx + 230}" y="34" font-size="26" font-weight="700" fill="{INK}" '
             f'text-anchor="middle">Same 20 people count as 30</text>')
    o.append(f'<text x="{rx + 230}" y="70" font-size="22" fill="{GRAY}" '
             f'text-anchor="middle">expected share if independent: 30%</text>')
    for r in range(2):
        for c in range(10):
            o.append(f'<circle cx="{rx + 20 + c * 46}" cy="{top + r * 48}" r="{rr}" fill="{BLUE}"/>')
    o.append(f'<text x="{W / 2}" y="{H - 12}" font-size="22" fill="{GRAY}" text-anchor="middle">'
             f'Filled dot = recorded positive label (group A). Labels stay as recorded.</text>')
    o.append('</svg>')
    return "\n".join(o)


def svg_s38(w, wc):
    W, H = 1130, 400
    unit = 5          # px per (weighted) example
    base = 330        # bar baseline
    bw = 130
    o = [f'<svg class="p4-fig" viewBox="0 0 {W} {H}" role="img" '
         f'aria-label="Recorded counts: group A 20 positive 30 negative, group B 40 positive 10 negative. '
         f'Weighted counts: both groups 30 positive 20 negative" xmlns="http://www.w3.org/2000/svg">',
         f'<defs>{marker("p4-ar-s38", GRAY)}</defs>']

    def bar(x, pos, neg, wpos=None, wneg=None):
        hp, hn = pos * unit, neg * unit
        yp = base - hp
        yn = yp - hn
        s = [f'<rect x="{x}" y="{yp}" width="{bw}" height="{hp}" fill="{BLUE}"/>',
             f'<text x="{x + bw / 2}" y="{yp + hp / 2 + 10}" font-size="28" font-weight="700" '
             f'fill="#fff" text-anchor="middle">{frac(F(pos))}</text>',
             f'<rect x="{x + 1.5}" y="{yn + 1.5}" width="{bw - 3}" height="{hn - 3}" fill="#fff" '
             f'stroke="{BLUE}" stroke-width="3"/>',
             f'<text x="{x + bw / 2}" y="{yn + hn / 2 + 10}" font-size="28" font-weight="700" '
             f'fill="{BLUE}" text-anchor="middle">{frac(F(neg))}</text>']
        if wpos is not None:
            s.append(f'<text x="{x + bw + 12}" y="{yp + hp / 2 + 9}" font-size="24" '
                     f'font-weight="700" fill="{GRAY}">× {frac(wpos)}</text>')
            s.append(f'<text x="{x + bw + 12}" y="{yn + hn / 2 + 9}" font-size="24" '
                     f'font-weight="700" fill="{GRAY}">× {frac(wneg)}</text>')
        return s

    def under(x, g, share):
        return [f'<text x="{x + bw / 2}" y="{base + 34}" font-size="26" font-weight="700" '
                f'fill="{INK}" text-anchor="middle">Group {g}</text>',
                f'<text x="{x + bw / 2}" y="{base + 64}" font-size="22" fill="{GRAY}" '
                f'text-anchor="middle">{share}% positive</text>']

    # left panel: recorded
    xa, xb = 40, 240
    o.append(f'<text x="{(xa + xb + bw) / 2}" y="40" font-size="26" font-weight="700" '
             f'fill="{INK}" text-anchor="middle">Recorded counts</text>')
    o += bar(xa, COUNTS[("A", "+")], COUNTS[("A", "-")])
    o += bar(xb, COUNTS[("B", "+")], COUNTS[("B", "-")])
    o += under(xa, "A", 40) + under(xb, "B", 80)
    o.append(f'<line x1="{xa - 15}" y1="{base}" x2="{xb + bw + 15}" y2="{base}" stroke="#9ca3af" stroke-width="2"/>')
    # arrow between panels (vertical middle of bars)
    ay = base - 125
    o.append(f'<line x1="430" y1="{ay}" x2="575" y2="{ay}" stroke="{GRAY}" stroke-width="4" '
             f'marker-end="url(#p4-ar-s38)"/>')
    o.append(f'<text x="502" y="{ay - 18}" font-size="24" font-weight="700" fill="{GRAY}" '
             f'text-anchor="middle">reweigh</text>')
    # right panel: weighted, with weights to the right of each segment
    xa2, xb2 = 610, 870
    o.append(f'<text x="{(xa2 + xb2 + bw) / 2}" y="40" font-size="26" font-weight="700" '
             f'fill="{BLUE}" text-anchor="middle">Weighted counts</text>')
    o += bar(xa2, wc[("A", "+")], wc[("A", "-")], w[("A", "+")], w[("A", "-")])
    o += bar(xb2, wc[("B", "+")], wc[("B", "-")], w[("B", "+")], w[("B", "-")])
    o += under(xa2, "A", 60) + under(xb2, "B", 60)
    o.append(f'<line x1="{xa2 - 15}" y1="{base}" x2="{xb2 + bw + 15}" y2="{base}" stroke="#9ca3af" stroke-width="2"/>')
    o.append('</svg>')
    return "\n".join(o)


def main():
    n, pg, py, w = weights(COUNTS)
    wc = check(n, pg, py, w)
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
    for k in sorted(w):
        print(k, "weight", frac(w[k]), "weighted count", frac(wc[k]))
    with open(os.path.join(out, "reweighing-s37.svg"), "w") as f:
        f.write(svg_s37() + "\n")
    with open(os.path.join(out, "reweighing-s38.svg"), "w") as f:
        f.write(svg_s38(w, wc) + "\n")


if __name__ == "__main__":
    main()
