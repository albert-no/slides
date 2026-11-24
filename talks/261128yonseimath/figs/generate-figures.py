#!/usr/bin/env python3
"""Geometry-only SVG figures for 261128yonseimath.

Every text label is an HTML overlay in the deck; this script prints the
overlay anchor of each label as a percentage of the SVG viewBox so the deck
can place it. Inputs, parameters and invariants live here (evidence E05,
E19, E20); the asserts fail loudly if an edit breaks one.

Run from anywhere:  python3 talks/261128yonseimath/figs/generate-figures.py
Outputs (next to this file): coins-100.svg, binom-pmf.svg, rectangles.svg,
log-chord.svg.  The probability bars of S11/S13 are HTML; their numbers are
checked here (E20) and printed as bar widths.
"""
from fractions import Fraction
from math import comb, log
from pathlib import Path

OUT = Path(__file__).resolve().parent
BLUE = "#003876"
BLUE_LIGHT = "#5b8cc4"
GRAY = "#8a8a8a"
SLATE = "#e8ecf0"
TAIL = "#d94040"


def write(name, w, h, body):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
           f'width="{w}" height="{h}">\n{body}\n</svg>\n')
    (OUT / name).write_text(svg)
    print(f"wrote {name} ({w}x{h})")


def pct(x, y, w, h):
    return f"left:{100 * x / w:.1f}%; top:{100 * y / h:.1f}%"


# ── E20: lunch toy distribution, before/after the marked-group boost ──────
before = {"김밥": Fraction(40, 100), "라면": Fraction(30, 100),
          "국수": Fraction(20, 100), "샐러드": Fraction(10, 100)}
marked = {"김밥", "샐러드"}
boost = Fraction(3, 2)
raw = {k: p * boost if k in marked else p for k, p in before.items()}
z = sum(raw.values())
after = {k: v / z for k, v in raw.items()}
assert sum(before.values()) == 1 and sum(after.values()) == 1
assert z == Fraction(5, 4)
assert [after[k] for k in before] == [Fraction(48, 100), Fraction(24, 100),
                                      Fraction(16, 100), Fraction(12, 100)]
assert sum(before[k] for k in marked) == Fraction(1, 2)
assert sum(after[k] for k in marked) == Fraction(3, 5)
print("E20 bars (width % of a 50% full-scale track):",
      {k: (float(before[k]) * 200, float(after[k]) * 200) for k in before})

# ── E05: 10x10 coins, exactly 70 heads (rows 1-7) ─────────────────────────
r, step, pad = 15, 38, 22
w = h = pad * 2 + step * 9 + 2 * r
dots, heads = [], 0
for i in range(10):
    for j in range(10):
        cx, cy = pad + r + j * step, pad + r + i * step
        if i < 7:
            heads += 1
            dots.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{BLUE}"/>')
        else:
            dots.append(f'<circle cx="{cx}" cy="{cy}" r="{r - 1.5}" fill="#fff" '
                        f'stroke="{GRAY}" stroke-width="3"/>')
assert heads == 70
write("coins-100.svg", w, h, "\n".join(dots))

# ── E05: exact Binomial(100, 1/2) PMF, tail k >= 70 ───────────────────────
n = 100
pmf = [Fraction(comb(n, k), 2 ** n) for k in range(n + 1)]
assert sum(pmf) == 1
tail = sum(pmf[70:])
assert abs(float(tail) - 0.00003925069822796835) < 1e-18
print(f"P(K>=70) = {float(tail):.20f} = {100 * float(tail):.6f}%")
W, H = 1000, 340
x0, x1, yb, ytop = 40, 960, 295, 20
ymax = 0.09                                   # axis top; peak pmf[50] = 0.0796
bw = (x1 - x0) / (n + 1)
X = lambda k: x0 + (k + 0.5) * bw             # bar centre
Y = lambda p: yb - (yb - ytop) * p / ymax
parts = [f'<rect x="{x0 + 70 * bw:.2f}" y="{ytop}" width="{x1 - x0 - 70 * bw:.2f}" '
         f'height="{yb - ytop}" fill="{TAIL}" fill-opacity="0.10"/>']
for k, p in enumerate(pmf):
    col = TAIL if k >= 70 else BLUE
    top = Y(float(p))
    if yb - top < 0.5:                        # invisible bars: keep a hairline
        top = yb - 0.5
    parts.append(f'<rect x="{X(k) - bw * 0.4:.2f}" y="{top:.2f}" '
                 f'width="{bw * 0.8:.2f}" height="{yb - top:.2f}" fill="{col}"/>')
parts.append(f'<line x1="{x0}" y1="{yb}" x2="{x1}" y2="{yb}" stroke="#444" stroke-width="2"/>')
for k in (0, 50, 70, 100):
    parts.append(f'<line x1="{X(k):.2f}" y1="{yb}" x2="{X(k):.2f}" y2="{yb + 10}" '
                 f'stroke="#444" stroke-width="2"/>')
parts.append(f'<line x1="{X(50):.2f}" y1="{ytop + 6}" x2="{X(50):.2f}" y2="{yb}" '
             f'stroke="{GRAY}" stroke-width="2" stroke-dasharray="6 6"/>')
write("binom-pmf.svg", W, H, "\n".join(parts))
print("pmf ticks:", {k: pct(X(k), yb + 32, W, H) for k in (0, 50, 70, 100)})
print("pmf mean label:", pct(X(50), ytop, W, H),
      " tail label:", pct((x0 + 70 * bw + x1) / 2, ytop + 60, W, H))
print(f"pmf peak {float(pmf[50]):.4f} at y={Y(float(pmf[50])):.1f}")

# ── E19: fixed sum a+b=10 rectangles, unit squares to scale ───────────────
u = 34
rects = [(8, 2), (5, 5)]                       # (width, height) in units
assert all(a + b == 10 for a, b in rects)
assert [a * b for a, b in rects] == [16, 25]
assert all(a * (10 - a) == 25 - (a - 5) ** 2 for a in range(1, 10))
gx = [30, 30 + 8 * u + 140]
W, H = gx[1] + 5 * u + 30, 5 * u + 85
gy = 30
parts = []
for (a, b), x in zip(rects, gx):
    y = gy + (5 - b) * u                       # bottom-align
    for i in range(1, a):
        parts.append(f'<line x1="{x + i * u}" y1="{y}" x2="{x + i * u}" y2="{y + b * u}" stroke="#fff" stroke-width="2"/>')
    for j in range(1, b):
        parts.append(f'<line x1="{x}" y1="{y + j * u}" x2="{x + a * u}" y2="{y + j * u}" stroke="#fff" stroke-width="2"/>')
    fill = BLUE if a == b else BLUE_LIGHT
    parts.insert(0, f'<rect x="{x}" y="{y}" width="{a * u}" height="{b * u}" fill="{fill}"/>')
    parts.append(f'<rect x="{x}" y="{y}" width="{a * u}" height="{b * u}" fill="none" stroke="{BLUE}" stroke-width="3"/>')
    print(f"rect {a}x{b}: top-edge label", pct(x + a * u / 2, y - 16, W, H),
          " side label", pct(x - 14, y + b * u / 2, W, H),
          " below", pct(x + a * u / 2, gy + 5 * u + 32, W, H))
write("rectangles.svg", W, H, "\n".join(parts))

# ── E18/E19: y = ln x on [1, 9], chord (2, ln2)-(8, ln8), compare at x=5 ──
W, H = 1000, 340
xa, xb, ya = 70, 960, 310                     # x in [1,9] -> [xa,xb]; y=0 at ya
sy = 130                                       # px per unit of ln
PX = lambda x: xa + (x - 1) * (xb - xa) / 8
PY = lambda y: ya - y * sy
a, b, m = 2, 8, 5
assert (a + b) / 2 == m
assert abs((log(a) + log(b)) / 2 - log(4)) < 1e-12       # chord midpoint = ln 4
assert log(m) > log(4)                                   # curve above chord at 5
for i in range(1, 600):                                   # and on all of (2, 8)
    t = i / 600
    x = a + t * (b - a)
    assert log(x) > (1 - t) * log(a) + t * log(b)
pts = " ".join(f"{PX(1 + 8 * i / 400):.2f},{PY(log(1 + 8 * i / 400)):.2f}" for i in range(401))
parts = [
    f'<line x1="{xa}" y1="{ya}" x2="{xb}" y2="{ya}" stroke="#444" stroke-width="2"/>',
    f'<line x1="{PX(m):.2f}" y1="{ya}" x2="{PX(m):.2f}" y2="{PY(log(m)):.2f}" stroke="{GRAY}" stroke-width="2" stroke-dasharray="4 6"/>',
    f'<line x1="{PX(a):.2f}" y1="{PY(log(a)):.2f}" x2="{PX(b):.2f}" y2="{PY(log(b)):.2f}" stroke="{GRAY}" stroke-width="4" stroke-dasharray="14 9"/>',
    f'<polyline points="{pts}" fill="none" stroke="{BLUE}" stroke-width="5"/>',
]
for x in (a, m, b):
    parts.append(f'<line x1="{PX(x):.2f}" y1="{ya}" x2="{PX(x):.2f}" y2="{ya + 10}" stroke="#444" stroke-width="2"/>')
for x in (a, b):
    parts.append(f'<circle cx="{PX(x):.2f}" cy="{PY(log(x)):.2f}" r="8" fill="{GRAY}"/>')
parts.append(f'<circle cx="{PX(m):.2f}" cy="{PY(log(m)):.2f}" r="11" fill="{BLUE}"/>')
parts.append(f'<circle cx="{PX(m):.2f}" cy="{PY(log(4)):.2f}" r="10" fill="#fff" stroke="{GRAY}" stroke-width="4"/>')
write("log-chord.svg", W, H, "\n".join(parts))
for name, (x, y) in {"tick a": (PX(a), ya + 30), "tick m": (PX(m), ya + 30),
                     "tick b": (PX(b), ya + 30),
                     "log5 point": (PX(m), PY(log(m))), "log4 point": (PX(m), PY(log(4))),
                     "curve end": (PX(9), PY(log(9))), "chord end": (PX(b), PY(log(b)))}.items():
    print(f"log {name}:", pct(x, y, W, H))
