#!/usr/bin/env python3
"""Geometry-only SVG figures for 261128yonseimath.

Every text label is an HTML overlay in the deck; this script prints the
overlay anchor of each label as a percentage of the SVG viewBox so the deck
can place it. Inputs, parameters and invariants live here (evidence E06,
E08, E09, E10 of job 2026-11-25-261128yonseimath-polish); the asserts fail
loudly if an edit breaks one.

Run from anywhere:  python3 talks/261128yonseimath/figs/generate-figures.py
Outputs (next to this file): coins-100.svg, binom-pmf.svg, log-chord.svg,
image-all-odd.png, watermark-demo-data.js.  The probability bars of S11/S13
are HTML; their numbers are checked here and printed as bar widths.

Input image-original-gray.png (S25) is committed. It was made once from NASA
GSFC Scientific Visualization Studio, "Blue Marble 2002" (svs.gsfc.nasa.gov/30614),
file blue_marble_modis_north_america_print.jpg (1024x574, sha256 cd67492d...0eba):
  mutool draw -F pgm -c gray -w 1024 -h 574 -o bm.pgm blue_marble_..._print.jpg
then stored losslessly as 8-bit grayscale PNG at the same size.
"""
import struct
import zlib
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


# ── E06: lunch toy distribution (S11), green-group boost (S12 step 1, S13) ─
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
print("E06 bars (width % of a 50% full-scale track):",
      {k: (float(before[k]) * 200, float(after[k]) * 200) for k in before})

# ── E09: 10x10 coins, exactly 70 heads (rows 1-7) ─────────────────────────
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

# ── E09: exact Binomial(100, 1/2) PMF, tail k >= 70 ───────────────────────
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

# ── E10: y = ln x on [1, 9], chord (2, ln2)-(8, ln8), compare at x=5 ──
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


# ── E06/E07: S12 left-to-right demo, every step green x1.5 then renormalise ─
# Illustrative numbers, not a model trace. Each step: (context-dependent)
# candidates with base %, which are green, and which one is selected.
DEMO_PREFIX = "오늘 점심은"
DEMO_STEPS = [
    ([("김밥을", 40, 1), ("라면을", 30, 0), ("국수를", 20, 0), ("샐러드를", 10, 1)], "김밥을"),
    ([("친구와", 40, 0), ("혼자", 30, 1), ("가족과", 20, 1), ("급하게", 10, 0)], "친구와"),
    ([("나눠", 40, 1), ("함께", 30, 0), ("맛있게", 20, 0), ("같이", 10, 1)], "나눠"),
    ([("먹었다.", 40, 1), ("먹으며", 30, 0), ("먹고", 20, 0), ("가졌다.", 10, 1)], "먹었다."),
]
steps_js, picked_green = [], []
for cands, pick in DEMO_STEPS:
    base = {w: Fraction(p, 100) for w, p, _ in cands}
    green = {w for w, _, g in cands if g}
    assert sum(base.values()) == 1 and sum(base[w] for w in green) == Fraction(1, 2)
    raw = {w: p * boost if w in green else p for w, p in base.items()}
    after_d = {w: v / sum(raw.values()) for w, v in raw.items()}
    assert sum(after_d.values()) == 1 and sum(after_d[w] for w in green) == Fraction(3, 5)
    assert all(v > 0 for v in after_d.values())          # red never becomes impossible
    assert all((v * 100).denominator == 1 for v in after_d.values())  # exact integer %
    picked_green.append(pick in green)
    steps_js.append("  {cands: [" + ", ".join(
        f'{{w: "{w}", p0: {p}, p1: {int(after_d[w] * 100)}, g: {"true" if g else "false"}}}'
        for w, p, g in cands) + f'], pick: "{pick}"}}')
assert not all(picked_green) and any(picked_green)       # at least one red pick
(OUT / "watermark-demo-data.js").write_text(
    "/* Generated by generate-figures.py: do not edit by hand. Illustrative values (E06/E07). */\n"
    f'window.YM_DEMO = {{prefix: "{DEMO_PREFIX}", steps: [\n' + ",\n".join(steps_js) + "\n]};\n")
print("wrote watermark-demo-data.js; picks green:", picked_green)


# ── E08: S25 image parity: every even 8-bit value x -> x+1, lossless PNG ───
def read_gray_png(path):
    d = path.read_bytes()
    assert d[:8] == b"\x89PNG\r\n\x1a\n"
    i, idat = 8, b""
    while i < len(d):
        n, = struct.unpack(">I", d[i:i + 4]); t = d[i + 4:i + 8]; body = d[i + 8:i + 8 + n]
        if t == b"IHDR":
            w, h, depth, ctype = struct.unpack(">IIBB", body[:10])
            assert depth == 8 and ctype == 0 and body[12] == 0, "need 8-bit gray, no interlace"
        elif t == b"IDAT":
            idat += body
        i += 12 + n
    raw, rows, prev = zlib.decompress(idat), [], bytearray(w)
    for y in range(h):
        f, line = raw[y * (w + 1)], bytearray(raw[y * (w + 1) + 1:(y + 1) * (w + 1)])
        for x in range(w):
            a_ = line[x - 1] if x else 0; b_ = prev[x]; c_ = prev[x - 1] if x else 0
            if f == 1: line[x] = (line[x] + a_) & 255
            elif f == 2: line[x] = (line[x] + b_) & 255
            elif f == 3: line[x] = (line[x] + (a_ + b_) // 2) & 255
            elif f == 4:
                pa, pb, pc = abs(b_ - c_), abs(a_ - c_), abs(a_ + b_ - 2 * c_)
                line[x] = (line[x] + (a_ if pa <= pb and pa <= pc else b_ if pb <= pc else c_)) & 255
        rows.append(bytes(line)); prev = line
    return w, h, b"".join(rows)


def write_gray_png(path, w, h, px):
    def chunk(t, b):
        return struct.pack(">I", len(b)) + t + b + struct.pack(">I", zlib.crc32(t + b) & 0xffffffff)
    raw = b"".join(b"\x00" + px[y * w:(y + 1) * w] for y in range(h))
    path.write_bytes(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 0, 0, 0, 0))
                     + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))


w0, h0, orig = read_gray_png(OUT / "image-original-gray.png")
assert (w0, h0) == (1024, 574)
odd = bytes(v | 1 for v in orig)                      # even x -> x+1, odd unchanged; 254 -> 255
write_gray_png(OUT / "image-all-odd.png", w0, h0, odd)
w1, h1, back = read_gray_png(OUT / "image-all-odd.png")
assert (w1, h1) == (w0, h0) and back == odd           # lossless round trip
assert all(v & 1 for v in back)
maxdiff = max(abs(p - q) for p, q in zip(orig, back))
assert maxdiff == 1
n_px = w0 * h0
print(f"S25 parity: {w0}x{h0}, odd before {sum(v & 1 for v in orig) / n_px:.4%}, "
      f"after {sum(v & 1 for v in back) / n_px:.4%}, changed {sum(p != q for p, q in zip(orig, back))} px, "
      f"max |diff| {maxdiff}")
