#!/usr/bin/env python3
"""Inline-SVG generator for lec12 S29, S32a, S32b, S33 (package p3).

Illustrative construction (evidence E15, our calculation): 60 synthetic people
per group, scores 0.2 or 0.8, flagged if score > 0.5.
  Group A: 30 at 0.8 (24 recorded positive, 6 negative); 30 at 0.2 (6 pos, 24 neg)
  Group B:  5 at 0.8 ( 4 recorded positive, 1 negative); 55 at 0.2 (11 pos, 44 neg)
All rates below are computed from these integers with exact fractions.

Usage: python3 calibrated_errors.py s29|s32a|s32b|s33   (prints one <svg>)
The SVG viewBox width is 1080 and the slide renders it at 1080 px, so
font-size values are rendered pixels.
"""
import sys
from fractions import Fraction as F

GROUPS = {
    "A": {"high": (24, 6), "low": (6, 24)},   # (recorded positive, recorded negative)
    "B": {"high": (4, 1), "low": (11, 44)},
}
SCORE = {"high": F(4, 5), "low": F(1, 5)}

BLUE, GRAY, INK, RED = "#003876", "#6b7280", "#1a1a1a", "#d94040"
DOT_FILL = "#374151"


def counts(g):
    (hp, hn), (lp, ln) = GROUPS[g]["high"], GROUPS[g]["low"]
    return dict(TP=hp, FP=hn, FN=lp, TN=ln, N=hp + hn + lp + ln, pos=hp + lp, neg=hn + ln, high=hp + hn)


def check():
    for g in GROUPS:
        c = counts(g)
        assert c["N"] == 60
        for b in ("high", "low"):
            p, n = GROUPS[g][b]
            assert F(p, p + n) == SCORE[b], (g, b)  # calibrated within group
    a, b = counts("A"), counts("B")
    assert F(a["pos"], 60) == F(1, 2) and F(b["pos"], 60) == F(1, 4)
    assert F(a["TP"], a["high"]) == F(b["TP"], b["high"]) == F(4, 5)          # PPV
    assert F(a["FP"], a["neg"]) == F(1, 5) and F(b["FP"], b["neg"]) == F(1, 45)  # FPR
    assert F(a["FN"], a["pos"]) == F(1, 5) and F(b["FN"], b["pos"]) == F(11, 15)  # FNR
    assert F(a["high"], 60) == F(1, 2) and F(b["high"], 60) == F(1, 12)          # score mix


def t(x, y, s, size=24, fill=INK, anchor="start", weight=400):
    return (f'<text x="{x:g}" y="{y:g}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')


def dots(x0, y0, n_filled, n_total, per_row, step, r):
    out = []
    for i in range(n_total):
        cx, cy = x0 + step * (i % per_row), y0 + step * (i // per_row)
        if i < n_filled:
            out.append(f'<circle cx="{cx:g}" cy="{cy:g}" r="{r}" fill="{DOT_FILL}"/>')
        else:
            out.append(f'<circle cx="{cx:g}" cy="{cy:g}" r="{r}" fill="#fff" stroke="{GRAY}" stroke-width="2"/>')
    return out


def s29():
    # Two cohorts of 60, recorded positives filled; shaded rect = whole group (denominator).
    out = ['<svg viewBox="0 0 1080 330" role="img" aria-label="Group A: 30 of 60 recorded positive; group B: 15 of 60">']
    for k, (g, x) in enumerate((("A", 52), ("B", 612))):
        c = counts(g)
        out.append(f'<rect x="{x}" y="58" width="416" height="262" rx="10" fill="#e5e7eb" stroke="{GRAY}" stroke-width="1.5"/>')
        out.append(t(x, 40, f"Group {g}", 28, BLUE, weight=700))
        out.append(t(x + 416, 40, f"{c['pos']} of 60 positive = {float(F(c['pos'], 60)):.2f}", 26, BLUE, "end", 700))
        out += dots(x + 28, 89, c["pos"], 60, 10, 40, 14)
    out.append("</svg>")
    return "\n".join(out)


def s32a():
    out = ['<svg viewBox="0 0 1080 340" role="img" aria-label="Score buckets: A 24 of 30 and 6 of 30 positive; B 4 of 5 and 11 of 55 positive">']
    out.append(t(395, 26, "score 0.8 (above 0.5): flagged", 24, BLUE, "middle", 700))
    out.append(t(845, 26, "score 0.2: not flagged", 24, GRAY, "middle", 700))
    rows = (("A", 44, 112), ("B", 170, 166))  # (group, box top, box height)
    for g, top, h in rows:
        out.append(t(8, top + h / 2 - 4, f"Group {g}", 28, BLUE, weight=700))
        out.append(t(8, top + h / 2 + 28, "60 people", 22, GRAY))
        for b, bx in (("high", 180), ("low", 630)):
            p, n = GROUPS[g][b]
            if b == "high":
                out.append(f'<rect x="{bx}" y="{top}" width="430" height="{h}" rx="10" fill="{BLUE}" fill-opacity="0.08" stroke="{BLUE}" stroke-width="3"/>')
            else:
                out.append(f'<rect x="{bx}" y="{top}" width="430" height="{h}" rx="10" fill="#f3f4f6" stroke="{GRAY}" stroke-width="1.5"/>')
            out += dots(bx + 33, top + 26, p, p + n, 15, 26, 9)
            out.append(t(bx + 215, top + h - 16, f"{p} of {p + n} positive = {float(SCORE[b]):.1f}", 24, INK, "middle", 700))
    out.append("</svg>")
    return "\n".join(out)


def s32b():
    a, b = counts("A"), counts("B")
    blocks = (
        ("PPV (precision): positives among flagged", (a["TP"], a["high"]), (b["TP"], b["high"]), "equal", "#2e8b57"),
        ("FPR: flagged among recorded negatives", (a["FP"], a["neg"]), (b["FP"], b["neg"]), "unequal", RED),
        ("FNR: not flagged among recorded positives", (a["FN"], a["pos"]), (b["FN"], b["pos"]), "unequal", RED),
    )
    X0, W = 60, 500
    out = ['<svg viewBox="0 0 1080 380" role="img" aria-label="PPV 24/30 vs 4/5; FPR 6/30 vs 1/45; FNR 6/30 vs 11/15">']
    for k, (head, fa, fb, verdict, vcol) in enumerate(blocks):
        y = 128 * k
        out.append(t(0, y + 26, head, 26, INK, weight=700))
        out.append(t(1076, y + 84, verdict, 26, vcol, "end", 700))
        for j, (g, (num, den)) in enumerate((("A", fa), ("B", fb))):
            by = y + 40 + 40 * j
            fr = F(num, den)
            out.append(t(0, by + 25, g, 26, BLUE, weight=700))
            out.append(f'<rect x="{X0}" y="{by}" width="{W}" height="32" fill="#e5e7eb" stroke="{GRAY}" stroke-width="1.5"/>')
            out.append(f'<rect x="{X0}" y="{by}" width="{float(fr) * W:.1f}" height="32" fill="{BLUE}" fill-opacity="0.85"/>')
            approx = "=" if (fr * 100).denominator == 1 else "≈"
            out.append(t(X0 + W + 20, by + 25, f"{num} / {den} {approx} {float(fr):.2f}", 26, INK, weight=700))
    out.append("</svg>")
    return "\n".join(out)


def s33():
    X0, W = 170, 700
    out = ['<svg viewBox="0 0 1080 240" role="img" aria-label="Score mix: A 30 of 60 at 0.8, B 5 of 60 at 0.8">']
    for g, y in (("A", 30), ("B", 150)):
        c = counts(g)
        hw = W * c["high"] / 60
        out.append(t(0, y + 44, f"Group {g}", 28, BLUE, weight=700))
        out.append(f'<rect x="{X0}" y="{y}" width="{hw:.2f}" height="66" fill="{BLUE}" fill-opacity="0.85"/>')
        out.append(f'<rect x="{X0 + hw:.2f}" y="{y}" width="{W - hw:.2f}" height="66" fill="#e5e7eb" stroke="{GRAY}" stroke-width="1.5"/>')
        if hw > 200:
            out.append(t(X0 + hw / 2, y + 42, f"{c['high']} at 0.8 (flagged)", 26, "#fff", "middle", 700))
        else:
            out.append(t(X0, y - 10, f"{c['high']} at 0.8 (flagged)", 24, BLUE, weight=700))
        out.append(t(X0 + hw + (W - hw) / 2, y + 42, f"{60 - c['high']} at 0.2", 26, INK, "middle", 700))
        share = F(c["high"], 60)
        out.append(t(X0 + W + 20, y + 44, f"{share.numerator}/{share.denominator} high", 28, BLUE, weight=700))
    out.append("</svg>")
    return "\n".join(out)


if __name__ == "__main__":
    check()
    print({"s29": s29, "s32a": s32a, "s32b": s32b, "s33": s33}[sys.argv[1]]())
