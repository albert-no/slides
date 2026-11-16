#!/usr/bin/env python3
"""Inline-SVG generator for lec12 Section 02 (package P2): counted lending examples.

Usage:  python3 criteria_examples.py ../../lec12-fairness.html
Rewrites every block between <!--p2gen:NAME--> and <!--/p2gen:NAME--> in the deck.
Deterministic; no random inputs.

Inputs (evidence.md E08/E09, job 2026-11-16-lec12-fairness-clarity; first set up in
job 2026-11-10-lec12-visual-motivation as E13/E03/E14):
  E13  synthetic lending population, 10 applicants per group, (TP, FP, FN, TN):
       A = (3, 1, 3, 3)   B = (1, 3, 1, 5)
  E03  separate illustrative population: 10 repaid + 10 did-not-repay per group,
       8/10 selected among repaid (TPR .8), 2/10 among did-not-repay (FPR .2)
  S18  illustrative: 10 people scored 0.7 per group, 7 repaid (existing slide counts)
  E14  calibrated three-score example, (people, repaid) per score:
       A: .2 -> (10, 2), .6 -> (10, 6), .9 -> (20, 18)
       B: .2 -> (10, 2), .6 -> (20, 12), .9 -> (10, 9)   cutoff > .5

Encoding (shared vocabulary, all packages):
  filled circle = would repay (Y = 1, stipulated), hollow circle = would not repay (Y = 0)
  Yonsei-blue box around a person = approved (selected, Y-hat = 1); no box = denied
  gray "?" = outcome unknown (real records: denied applicants are never observed)
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
        label = title if isinstance(title, str) else f"Group {name}"
        body.append(T((lz0 + rz1) / 2, 30, label, 28, BLUE if not dim else GRAY, weight=700))
    if headers:
        body.append(T((lz0 + lz1) / 2, 70, "approved", 22, BLUE, weight=700))
        body.append(T((rz0 + rz1) / 2, 70, "denied", 22, GRAY))
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


PX_A, PX_B = 226, 672


def row_labels(x=208):
    return [T(x, ROW1 + 8, "would repay", 26, INK, "end", 700),
            T(x, ROW2 + 8, "would not repay", 26, INK, "end", 700)]


def cohort(shadeA=None, shadeB=None, dimB=False, notesA=(), notesB=(), maxw=1060):
    nlines = max(len(notesA), len(notesB))
    h = ROW2 + 30 + 34 * nlines + (8 if nlines else 0)
    body = row_labels()
    body.append(cohort_panel(PX_A, "A", E13["A"], shadeA, False, notesA))
    body.append(cohort_panel(PX_B, "B", E13["B"], shadeB, dimB, notesB))
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
    """mode: 'buckets' (shade each bucket), 'selected' (box + shade buckets above .5,
    dim the denied .2 bucket), 'one' (shade the .6 bucket only), None."""
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
        denied = mode == "selected" and s < 0.5
        grp = [person(x + BSLOT * (c + .5), ys[r], k < pos, sel, box=BSLOT - 5, r=11)
               for k in range(n) for r, c in [divmod(k, 10)]]
        body.append(f'<g opacity="0.3">{"".join(grp)}</g>' if denied else "".join(grp))
        if ann:
            yc = sum(ys) / len(ys)
            if denied:
                body.append(T(x + w + 14, yc + 9, "denied", 26, GRAY, "start", 700))
            else:
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
    """notes: list of lines; each line is a list of (x, text)."""
    body = bucket_labels()
    body.append(bucket_panel(160, "A", E14["A"], mode))
    body.append(bucket_panel(640, "B", E14["B"], mode))
    h = BROWS[0.2][0] + 30
    if mode == "selected":
        body += cutoff_line(150, 1060)
    for line in notes or []:
        for xa, txt in line:
            body.append(T(xa, h + 26, txt, 26, BLUE, weight=700))
        h += 36
    if notes:
        h += 4
    return svg(1100, h, body, maxw)


# ---- S20a: one population, three windows (group A of E13) ---------------------
# applicant order is arbitrary but fixed; counts = group A: 6 would repay (3 approved),
# 4 would not repay (1 approved)
S20A_ORDER = [(1, 1), (0, 0), (1, 0), (1, 1), (0, 1), (1, 0), (0, 0), (1, 1), (1, 0), (0, 0)]


def windows_map():
    assert sum(r for r, a in S20A_ORDER) == 6 and sum(a for r, a in S20A_ORDER) == 4
    assert sum(r and a for r, a in S20A_ORDER) == 3
    body = [T(250, 54, "10 applicants", 26, INK, "end", 700)]
    slot = 52
    x0 = 280
    for i, (r, a) in enumerate(S20A_ORDER):
        body.append(person(x0 + slot * (i + .5), 46, r, a, box=40, r=14))
    specs = [("everyone", lambda r: True), ("would repay", lambda r: r == 1),
             ("would not repay", lambda r: r == 0)]
    ww, wgap, wy0, wy1 = 344, 26, 126, 236
    cx_pop = x0 + 5 * slot
    for j, (name, keep) in enumerate(specs):
        wx = 6 + j * (ww + wgap)
        sub = [(r, a) for r, a in S20A_ORDER if keep(r)]
        body.append(shade(wx, wy0, wx + ww, wy1))
        body.append(T(wx + ww / 2, wy0 + 34, f"{j + 1} · {name}", 26, BLUE, weight=700))
        s2 = 32
        sx = wx + ww / 2 - len(sub) * s2 / 2
        for k, (r, a) in enumerate(sub):
            body.append(person(sx + s2 * (k + .5), wy0 + 76, r, a, box=28, r=10))
        n_app = sum(a for r, a in sub)
        body.append(T(wx + ww / 2, wy1 + 34, f"{n_app} of {len(sub)} approved", 26, INK, weight=700))
        body.append(f'<line x1="{cx_pop}" y1="80" x2="{wx + ww / 2}" y2="{wy0 - 6}" stroke="{GRAY}" '
                    f'stroke-width="2.5" marker-end="url(#c12p2-arr)"/>')
    defs = (f'<defs><marker id="c12p2-arr" markerUnits="userSpaceOnUse" markerWidth="14" markerHeight="12" '
            f'refX="14" refY="6" orient="auto"><path d="M0,0 L14,6 L0,12 Z" fill="{GRAY}"/></marker></defs>')
    return svg(1100, wy1 + 50, [defs] + body, 1080)


# ---- S12a: decision versus outcome flow -----------------------------------------
def box(x, y, w, h, lines, fill="#fff", stroke=BLUE, dash=None, color=INK, size=26, bold_first=True):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="3"{d}/>']
    n = len(lines)
    for i, ln in enumerate(lines):
        yy = y + h / 2 + (i - (n - 1) / 2) * (size + 8) + size * 0.35
        out.append(T(x + w / 2, yy, ln, size, color, weight=700 if (bold_first and i == 0) else None))
    return "".join(out)


def arrow(x1, y1, x2, y2, color=GRAY, dash=None, mid="c12p2-arr2"):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="3"{d} '
            f'marker-end="url(#{mid})"/>')


def decision_flow():
    defs = (f'<defs><marker id="c12p2-arr2" markerUnits="userSpaceOnUse" markerWidth="16" markerHeight="14" '
            f'refX="16" refY="7" orient="auto"><path d="M0,0 L16,7 L0,14 Z" fill="{GRAY}"/></marker></defs>')
    b = [defs]
    b.append(box(10, 50, 200, 90, ["Applicant", "income, history"]))
    b.append(box(290, 50, 300, 90, ["Model", "predicts repayment"]))
    b.append(box(680, 6, 410, 74, ["Ŷ = 1: approved", "= selected"], fill="#e6ecf4"))
    b.append(box(680, 110, 410, 74, ["Ŷ = 0: denied", "= not selected"]))
    b.append(arrow(210, 95, 286, 95))
    b.append(arrow(590, 82, 676, 46))
    b.append(arrow(590, 108, 676, 146))
    b.append(box(290, 218, 300, 74, ["Y: would repay?", "the actual outcome"], stroke=GRAY, dash="9 6"))
    b.append(f'<path d="M110,140 L110,255 L286,255" fill="none" stroke="{GRAY}" stroke-width="3" '
             f'stroke-dasharray="9 6" marker-end="url(#c12p2-arr2)"/>')
    b.append(T(620, 247, "can differ from Ŷ:", 26, RED, "start", 700))
    b.append(T(620, 281, "a prediction, not a promise", 26, RED, "start", 700))
    return svg(1100, 300, b, 1080)


# ---- S12b: stipulated table versus observed records (group A) ------------------
def unknown_glyph(cx, cy, r=14):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#f0f0f0" stroke="{GRAY}" stroke-width="2.5" '
            f'stroke-dasharray="4 3"/>' + T(cx, cy + 8, "?", 24, GRAY, weight=700))


def missing_outcomes():
    g = E13["A"]
    body = row_labels()
    body.append(cohort_panel(PX_A, "A", g, None, False, [("all 10 outcomes stipulated", BLUE)],
                             title="Teaching example"))
    # real-records panel: approved zone as observed; denied zone unknown
    x = PX_B
    lz1 = x + 3 * SLOT
    rz0, rz1 = lz1 + GAP, lz1 + GAP + 5 * SLOT
    half = (ROW2 - ROW1) / 2
    b = [T((x + rz1) / 2, 30, "Real loan records", 28, BLUE, weight=700),
         T((x + lz1) / 2, 70, "approved", 22, BLUE, weight=700),
         T((rz0 + rz1) / 2, 70, "denied", 22, GRAY)]
    xm = lz1 + GAP / 2
    b.append(f'<line x1="{xm}" y1="{ROW1-half+8}" x2="{xm}" y2="{ROW2+half-8}" stroke="{GRAY}" '
             f'stroke-width="2" stroke-dasharray="4 5"/>')
    for i in range(g["TP"]):
        b.append(person(x + SLOT * (i + .5), ROW1, True, True, box=SLOT - 8, r=SLOT * 0.29))
    for i in range(g["FP"]):
        b.append(person(x + SLOT * (i + .5), ROW2, False, True, box=SLOT - 8, r=SLOT * 0.29))
    nden = g["FN"] + g["TN"]
    b.append(f'<rect x="{rz0 - 4}" y="{ROW1 - half + 4}" width="{rz1 - rz0 + 8}" height="{ROW2 - ROW1 + 2 * half - 8}" '
             f'rx="10" fill="#f4f4f4" stroke="{GRAY}" stroke-width="2"/>')
    per_row = (nden + 1) // 2
    for k in range(nden):
        r, c = divmod(k, per_row)
        b.append(unknown_glyph(rz0 + (rz1 - rz0) * (c + .5) / per_row, ROW1 if r == 0 else ROW2))
    b.append(T((x + rz1) / 2, ROW2 + half + 34, f"{nden} denied: outcome unknown", 26, RED, weight=700))
    body.append("".join(b))
    h = ROW2 + 30 + 34 + 8
    return svg(1100, h, body, 1060)


# ---- S79 / S80 table icons: 2 x 2 (rows would / would not repay; cols approved / denied)
def icon(shades, numer="box"):
    """shades: list of cell-rect specs among 'all', 'top', 'bot', 'left'."""
    cw, ch, x0, y0 = 46, 34, 4, 4
    out = []
    rects = {"all": (0, 0, 2, 2), "top": (0, 0, 2, 1), "bot": (0, 1, 2, 1), "left": (0, 0, 1, 2)}
    for sname in shades:
        c, r, w, h = rects[sname]
        pad = 2
        out.append(f'<rect x="{x0 + c*cw + pad}" y="{y0 + r*ch + pad}" width="{w*cw - 2*pad}" '
                   f'height="{h*ch - 2*pad}" rx="6" fill="{SHADE_FILL}" stroke="{SHADE_STROKE}" '
                   f'stroke-width="2" stroke-dasharray="5 3"/>')
    for r in (0, 1):
        for c in (0, 1):
            cx, cy = x0 + c * cw + cw / 2, y0 + r * ch + ch / 2
            out.append(person(cx, cy, r == 0, c == 0, box=26, r=9))
    out.append(f'<line x1="{x0 + cw}" y1="{y0 + 4}" x2="{x0 + cw}" y2="{y0 + 2*ch - 4}" stroke="{GRAY}" '
               f'stroke-width="1.5" stroke-dasharray="3 3"/>')
    W, H = 2 * cw + 8, 2 * ch + 8
    return (f'<svg class="c12p2-icon" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
            f'aria-hidden="true">{"".join(out)}</svg>')


# ---- S81: precision averages the approved score mix (E14 selected buckets) -----
def selected_mix():
    PX = 20   # px per person
    x0, bh = 190, 64
    body = []
    rows = [("A", 6), ("B", 150)]
    for name, y in rows:
        d = E14[name]
        n9, p9 = d[0.9]
        n6, p6 = d[0.6]
        body.append(T(170, y + bh / 2 + 9, f"Group {name}", 28, BLUE, "end", 700))
        w9, w6 = n9 * PX, n6 * PX
        body.append(f'<rect x="{x0}" y="{y}" width="{w9}" height="{bh}" fill="{BLUE}"/>')
        body.append(f'<rect x="{x0 + w9}" y="{y}" width="{w6}" height="{bh}" fill="#c9d7ea"/>')
        body.append(f'<rect x="{x0}" y="{y}" width="{w9 + w6}" height="{bh}" fill="none" stroke="{BLUE}" stroke-width="3"/>')
        body.append(T(x0 + w9 / 2, y + bh / 2 + 9, f"{n9} at 0.9", 26, "#fff", weight=700))
        body.append(T(x0 + w9 + w6 / 2, y + bh / 2 + 9, f"{n6} at 0.6", 26, INK, weight=700))
        body.append(T(x0 + w9 / 2, y + bh + 34, f"{p9} repay", 26, INK))
        body.append(T(x0 + w9 + w6 / 2, y + bh + 34, f"{p6} repay", 26, INK))
        tot_n, tot_p = n9 + n6, p9 + p6
        body.append(T(x0 + 30 * PX + 30, y + bh / 2 + 9,
                      f"{tot_p}/{tot_n} = {float(F(tot_p, tot_n)):.1f}", 30, BLUE, "start", 700))
    return svg(1100, 150 + bh + 46, body, 1080)


# ---- S20b: same-score bucket vs selected cohort (group A, E14) -----------------
def score_vs_selection():
    body = bucket_labels(140)
    body.append(bucket_panel(160, "A", E14["A"], "one", title="Calibration: one score", ann=False))
    body.append(bucket_panel(660, "A", E14["A"], "selected", title="Precision: the approved", ann=False))
    body += [T(160 + 180, 345, "6/10 would repay at 0.6", 26, BLUE, weight=700),
             T(660 + 180, 345, "24/30 would repay above 0.5", 26, BLUE, weight=700)]
    body += [f'<line x1="650" y1="{CUT_Y}" x2="1030" y2="{CUT_Y}" stroke="{BLUE}" stroke-width="3" stroke-dasharray="10 6"/>',
             T(640, CUT_Y + 8, "cutoff 0.5", 22, BLUE, "end", 700)]
    return svg(1100, 362, body, 1080)


FIGS = {
    "S20a": windows_map,
    "S12a": decision_flow,
    "S12b": missing_outcomes,
    "S13a": lambda: cohort(shadeA="all", dimB=True, notesA=[("4 of 10 approved", BLUE)]),
    "S13b": lambda: cohort(shadeA="pos", dimB=True, notesA=[("3 of 6 would-repay approved", BLUE)]),
    "S13c": lambda: cohort(shadeA="neg", dimB=True, notesA=[("1 of 4 would-not-repay approved", BLUE)]),
    "S13d": lambda: cohort(shadeA="sel", dimB=True, notesA=[("3 of 4 approved would repay", BLUE)]),
    "S79-sel": lambda: icon(["all"]),
    "S79-tpr": lambda: icon(["top"]),
    "S79-fpr": lambda: icon(["bot"]),
    "S79-ppv": lambda: icon(["left"]),
    "S14": lambda: cohort(shadeA="all", shadeB="all",
                          notesA=[("4/10 approved", BLUE), ("3 of 4 approved would repay", INK)],
                          notesB=[("4/10 approved", BLUE), ("1 of 4 approved would repay", RED)]),
    "S15": lambda: cohort(shadeA="pos", shadeB="pos",
                          notesA=[("TPR 3/6 = 1/2", BLUE), ("FPR 1/4", RED)],
                          notesB=[("TPR 1/2", BLUE), ("FPR 3/8", RED)]),
    "S16": lambda: rows10([("A · would repay", 10, 8, 10, "TPR 8/10", True),
                           ("A · would not repay", 0, 2, 10, "FPR 2/10", True),
                           ("B · would repay", 10, 8, 10, "TPR 8/10", True),
                           ("B · would not repay", 0, 2, 10, "FPR 2/10", True)],
                          maxw=1060, label_w=280, gap_after={1}),
    "S80-dp": lambda: icon(["all"]),
    "S80-eop": lambda: icon(["top"]),
    "S80-eod": lambda: icon(["top", "bot"]),
    "S18": lambda: rows10([("A · scored 0.7", 7, 0, 10, "7/10 would repay", True),
                           ("B · scored 0.7", 7, 0, 10, "7/10 would repay", True)],
                          maxw=1000, label_w=230, row_h=66),
    "S19a": lambda: buckets("buckets", notes=[[(340, "40 people"), (820, "40 people")]]),
    "S19b": lambda: buckets("selected", notes=[[(340, "30 approved"), (820, "30 approved")],
                                               [(340, "18 + 6 = 24 would repay"), (820, "9 + 12 = 21 would repay")]]),
    "S81": selected_mix,
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
