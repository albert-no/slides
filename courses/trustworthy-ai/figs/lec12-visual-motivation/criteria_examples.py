#!/usr/bin/env python3
"""Inline-SVG generator for lec12 Section 02 (package P2): counted lending examples.

Usage:  python3 criteria_examples.py ../../lec12-fairness.html
Rewrites every block between <!--p2gen:NAME--> and <!--/p2gen:NAME--> in the deck.
Deterministic; no random inputs.

Inputs (evidence.md, job 2026-11-10-lec12-visual-motivation):
  E13  synthetic lending population, 10 applicants per group, (TP, FP, FN, TN):
       A = (3, 1, 3, 3)   B = (1, 3, 1, 5)
  E03  separate illustrative population: 10 repaid + 10 did-not-repay per group,
       8/10 selected among repaid (TPR .8), 2/10 among did-not-repay (FPR .2)
  S18  illustrative: 10 people scored 0.7 per group, 7 repaid (existing slide counts)
  E14  calibrated three-score example, (people, repaid) per score:
       A: .2 -> (10, 2), .6 -> (10, 6), .9 -> (20, 18)
       B: .2 -> (10, 2), .6 -> (20, 12), .9 -> (10, 9)   cutoff > .5

Encoding (shared vocabulary, all packages):
  filled circle = recorded repaid (Y = 1), hollow circle = did not repay (Y = 0)
  Yonsei-blue box around a person = selected (loan approved, Y-hat = 1)
  yellow shaded region with dashed border = the denominator of the rate shown
"""
import re
import sys
from fractions import Fraction as F

BLUE = "#003876"
INK = "#1a1a1a"
GRAY = "#666666"
SHADE_FILL = "#fbe7a1"
SHADE_STROKE = "#b07d00"
RED = "#d94040"

# ---- data -----------------------------------------------------------------
E13 = {"A": dict(TP=3, FP=1, FN=3, TN=3), "B": dict(TP=1, FP=3, FN=1, TN=5)}
E14 = {"A": {0.2: (10, 2), 0.6: (10, 6), 0.9: (20, 18)},
       "B": {0.2: (10, 2), 0.6: (20, 12), 0.9: (10, 9)}}


def check():
    a, b = E13["A"], E13["B"]
    for g in (a, b):
        assert sum(g.values()) == 10
    rates = {}
    for k, g in E13.items():
        rates[k] = dict(sel=F(g["TP"] + g["FP"], 10), tpr=F(g["TP"], g["TP"] + g["FN"]),
                        fpr=F(g["FP"], g["FP"] + g["TN"]), ppv=F(g["TP"], g["TP"] + g["FP"]))
    assert rates["A"] == dict(sel=F(4, 10), tpr=F(1, 2), fpr=F(1, 4), ppv=F(3, 4))
    assert rates["B"] == dict(sel=F(4, 10), tpr=F(1, 2), fpr=F(3, 8), ppv=F(1, 4))
    for k, g in E14.items():
        for s, (n, pos) in g.items():
            assert F(pos, n) == F(s).limit_denominator(10)  # calibrated bucket
        sel_n = sum(n for s, (n, p) in g.items() if s > 0.5)
        sel_p = sum(p for s, (n, p) in g.items() if s > 0.5)
        assert sel_n == 30 and sum(n for n, p in g.values()) == 40
        assert F(sel_p, sel_n) == (F(4, 5) if k == "A" else F(7, 10))


# ---- primitives -----------------------------------------------------------
def T(x, y, s, size=24, fill=INK, anchor="middle", weight=None):
    w = f' font-weight="{weight}"' if weight else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}"{w}>{s}</text>'


def person(cx, cy, repaid, selected, box=40, r=14):
    out = []
    if selected:
        h = box / 2
        out.append(f'<rect x="{cx-h}" y="{cy-h}" width="{box}" height="{box}" rx="7" '
                   f'fill="{BLUE}" fill-opacity="0.14" stroke="{BLUE}" stroke-width="4"/>')
    if repaid:
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{INK}"/>')
    else:
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r-1.5}" fill="#fff" stroke="{INK}" stroke-width="3"/>')
    return "".join(out)


def shade(x0, y0, x1, y1):
    return (f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" rx="10" fill="{SHADE_FILL}" '
            f'stroke="{SHADE_STROKE}" stroke-width="2.5" stroke-dasharray="8 5"/>')


def svg(w, h, body, maxw):
    return (f'<svg class="p2-fig" viewBox="0 0 {w} {h}" style="width:100%;max-width:{maxw}px;" '
            f'role="img">{"".join(body)}</svg>')


# ---- E13 cohort: two rows (repaid / did not repay) x two zones (selected / not) ----
SLOT, GAP, ROW1, ROW2 = 48, 24, 112, 172


def cohort_panel(x, name, g, shade_mode, dim, notes, slot=SLOT, row1=ROW1, row2=ROW2,
                 headers=True, title=True):
    """Left zone: 3 selected slots; right zone: 5 not-selected slots."""
    out = []
    lz0, lz1 = x, x + 3 * slot
    rz0, rz1 = lz1 + GAP, lz1 + GAP + 5 * slot
    half = (row2 - row1) / 2
    if shade_mode:
        p = 6
        top, mid, bot = row1 - half + 4, (row1 + row2) / 2, row2 + half - 4
        if shade_mode == "all":
            out.append(shade(lz0 - p, top, rz1 + p, bot))
        if shade_mode in ("pos", "both"):
            out.append(shade(lz0 - p, top, rz1 + p, mid - 3))
        if shade_mode in ("neg", "both"):
            out.append(shade(lz0 - p, mid + 3, rz1 + p, bot))
        if shade_mode == "sel":
            out.append(shade(lz0 - p, top, lz1 + p, bot))
    body = []
    if title:
        body.append(T((lz0 + rz1) / 2, 30, f"Group {name}", 28, BLUE if not dim else GRAY, weight=700))
    if headers:
        body.append(T((lz0 + lz1) / 2, 70, "selected", 22, BLUE, weight=700))
        body.append(T((rz0 + rz1) / 2, 70, "not selected", 22, GRAY))
    # dashed zone divider
    xm = lz1 + GAP / 2
    body.append(f'<line x1="{xm}" y1="{row1-half+8}" x2="{xm}" y2="{row2+half-8}" stroke="{GRAY}" '
                f'stroke-width="2" stroke-dasharray="4 5"/>')

    def zone(x0, n, y, repaid, selected):
        return [person(x0 + slot * (i + .5), y, repaid, selected, box=slot - 8, r=slot * 0.29)
                for i in range(n)]
    body += zone(lz0, g["TP"], row1, True, True)
    body += zone(rz0, g["FN"], row1, True, False)
    body += zone(lz0, g["FP"], row2, False, True)
    body += zone(rz0, g["TN"], row2, False, False)
    for i, (txt, col) in enumerate(notes):
        body.append(T((lz0 + rz1) / 2, row2 + half + 34 + 34 * i, txt, 26, col, weight=700))
    op = ' opacity="0.28"' if dim else ""
    out.append(f'<g{op}>{"".join(body)}</g>')
    return "".join(out)


def cohort(shadeA=None, shadeB=None, dimB=False, notesA=(), notesB=(), maxw=1060):
    nlines = max(len(notesA), len(notesB))
    h = ROW2 + 30 + 34 * nlines + (8 if nlines else 0)
    body = [T(178, ROW1 + 8, "repaid", 26, INK, "end", 700),
            T(178, ROW2 + 8, "did not repay", 26, INK, "end", 700)]
    body.append(cohort_panel(200, "A", E13["A"], shadeA, False, notesA))
    body.append(cohort_panel(660, "B", E13["B"], shadeB, dimB, notesB))
    return svg(1100, h, body, maxw)


# ---- E03 separate population: rows of 10 ------------------------------------
def rows10(rows, maxw=1000, label_w=300, notes_x=None, slot=48, row_h=58, gap_after=None, ann=True):
    """rows: list of (label, n_repaid_filled, n_selected, total, note, shaded)."""
    gap_after = gap_after or set()
    body, y = [], 34
    x0 = label_w + 20
    notes_x = notes_x or x0 + 10 * slot + 30
    for i, (label, n_fill, n_sel, total, note, shaded) in enumerate(rows):
        if shaded:
            body.append(shade(x0 - 6, y - row_h / 2 + 4, x0 + total * slot + 6, y + row_h / 2 - 4))
        body.append(T(label_w, y + 8, label, 26, INK, "end", 700))
        for k in range(total):
            body.append(person(x0 + slot * (k + .5), y, k < n_fill, k < n_sel, box=slot - 8, r=slot * 0.29))
        if note and ann:
            body.append(T(notes_x, y + 9, note, 26, BLUE, "start", 700))
        y += row_h + (22 if i in gap_after else 0)
    h = y - row_h / 2 + 8
    return svg(maxw, h, body, maxw)


# ---- E14 buckets ---------------------------------------------------------------
BSLOT = 36
BROWS = {0.9: (74, 110), 0.6: (164, 200), 0.2: (290,)}
CUT_Y = 245


def bucket_panel(x, name, data, mode, show=(0.9, 0.6, 0.2), title=None, ann=True):
    """mode: 'buckets' (shade each bucket), 'selected' (box + shade buckets above .5),
    'one' (shade the .6 bucket only), None."""
    out, body = [], []
    w = 10 * BSLOT
    if mode == "selected":
        out.append(shade(x - 6, BROWS[0.9][0] - 20, x + w + 6, BROWS[0.6][-1] + 20))
    for s in show:
        n, pos = data[s]
        ys = BROWS[s]
        if mode == "buckets" or (mode == "one" and s == 0.6):
            out.append(shade(x - 6, ys[0] - 20, x + w + 6, ys[-1] + 20))
        sel = mode == "selected" and s > 0.5
        for k in range(n):
            r, c = divmod(k, 10)
            body.append(person(x + BSLOT * (c + .5), ys[r], k < pos, sel, box=BSLOT - 5, r=11))
        if ann:
            yc = sum(ys) / len(ys)
            body.append(T(x + w + 14, yc + 9, f"{pos}/{n}", 26, INK, "start", 700))
    body.append(T(x + w / 2, 30, title or f"Group {name}", 28, BLUE, weight=700))
    return "".join(out) + "".join(body)


def bucket_labels(x=140):
    b = [T(x, sum(BROWS[s]) / len(BROWS[s]) + 8, f"score {s}", 26, INK, "end", 700) for s in BROWS]
    return b


def cutoff_line(x0, x1, label_x=140):
    return [f'<line x1="{x0}" y1="{CUT_Y}" x2="{x1}" y2="{CUT_Y}" stroke="{BLUE}" stroke-width="3" stroke-dasharray="10 6"/>',
            T(label_x, CUT_Y + 8, "cutoff 0.5", 22, BLUE, "end", 700)]


def buckets(mode, notes=None, maxw=1080):
    body = bucket_labels()
    body.append(bucket_panel(160, "A", E14["A"], mode))
    body.append(bucket_panel(640, "B", E14["B"], mode))
    h = BROWS[0.2][0] + 30
    if mode == "selected":
        body += cutoff_line(150, 1060)
    if notes:
        for i, (xa, txt) in enumerate(notes):
            body.append(T(xa, h + 26, txt, 26, BLUE, weight=700))
        h += 40
    return svg(1100, h, body, maxw)


# ---- S20a denominator map: three mini cohorts (group A) -----------------------
def denominator_map():
    body = []
    specs = [("Demographic parity", "all", "out of everyone", "selection rate"),
             ("Equal opportunity", "pos", "out of repaid", "TPR"),
             ("Equalized odds", "both", "out of repaid, and", "out of did not repay")]
    slot = 38
    pw = 8 * slot + GAP
    for i, (name, mode, l1, l2) in enumerate(specs):
        x = 18 + i * (pw + 30)
        body.append(T(x + pw / 2, 30, name, 28, BLUE, weight=700))
        body.append(cohort_panel(x, "A", E13["A"], mode, False, [], slot=slot, row1=82, row2=134,
                                 headers=False, title=False))
        body.append(T(x + pw / 2, 196, l1, 26, INK, weight=700))
        body.append(T(x + pw / 2, 228, l2, 26, INK if mode == "both" else GRAY,
                      weight=700 if mode == "both" else None))
    return svg(1100, 244, body, 1080)


# ---- S20b: same-score bucket vs selected cohort (group A, E14) -----------------
def score_vs_selection():
    body = bucket_labels(140)
    body.append(bucket_panel(160, "A", E14["A"], "one", title="Calibration: one score", ann=False))
    body.append(bucket_panel(660, "A", E14["A"], "selected", title="Predictive parity: the selected", ann=False))
    body += [T(160 + 180, 345, "6/10 repaid at score 0.6", 26, BLUE, weight=700),
             T(660 + 180, 345, "24/30 repaid above 0.5", 26, BLUE, weight=700)]
    body += [f'<line x1="650" y1="{CUT_Y}" x2="1030" y2="{CUT_Y}" stroke="{BLUE}" stroke-width="3" stroke-dasharray="10 6"/>',
             T(640, CUT_Y + 8, "cutoff 0.5", 22, BLUE, "end", 700)]
    return svg(1100, 362, body, 1080)


FIGS = {
    "S12": lambda: cohort(),
    "S13a": lambda: cohort(shadeA="all", dimB=True, notesA=[("4 of 10 selected", BLUE)]),
    "S13b": lambda: cohort(shadeA="pos", dimB=True, notesA=[("3 of 6 repayers selected", BLUE)]),
    "S13c": lambda: cohort(shadeA="neg", dimB=True, notesA=[("1 of 4 non-repayers selected", BLUE)]),
    "S13d": lambda: cohort(shadeA="sel", dimB=True, notesA=[("3 of 4 selected repaid", BLUE)]),
    "S14": lambda: cohort(shadeA="all", shadeB="all",
                          notesA=[("4/10 selected", BLUE), ("3 of 4 selected repaid", INK)],
                          notesB=[("4/10 selected", BLUE), ("1 of 4 selected repaid", RED)]),
    "S15": lambda: cohort(shadeA="pos", shadeB="pos",
                          notesA=[("TPR 3/6 = 1/2", BLUE), ("FPR 1/4", RED)],
                          notesB=[("TPR 1/2", BLUE), ("FPR 3/8", RED)]),
    "S16": lambda: rows10([("A · repaid", 10, 8, 10, "TPR 8/10", True),
                           ("A · did not repay", 0, 2, 10, "FPR 2/10", True),
                           ("B · repaid", 10, 8, 10, "TPR 8/10", True),
                           ("B · did not repay", 0, 2, 10, "FPR 2/10", True)],
                          maxw=1060, label_w=250, gap_after={1}),
    "S18": lambda: rows10([("A · score 0.7", 7, 0, 10, "7/10 repaid", True),
                           ("B · score 0.7", 7, 0, 10, "7/10 repaid", True)],
                          maxw=1000, label_w=230, row_h=66),
    "S19a": lambda: buckets("buckets", notes=[(340, "40 people"), (820, "40 people")]),
    "S19b": lambda: buckets("selected", notes=[(340, "PPV 24/30 = 0.8"), (820, "PPV 21/30 = 0.7")]),
    "S20a": denominator_map,
    "S20b": score_vs_selection,
}


def main(path):
    check()
    html = open(path, encoding="utf-8").read()
    for name, fn in FIGS.items():
        pat = re.compile(rf"(<!--p2gen:{name}-->).*?(<!--/p2gen:{name}-->)", re.S)
        html, n = pat.subn(lambda m: m.group(1) + fn() + m.group(2), html)
        assert n == 1, (name, n)
    open(path, "w", encoding="utf-8").write(html)


if __name__ == "__main__":
    main(sys.argv[1])
