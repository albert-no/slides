#!/usr/bin/env python3
"""Source-derived audit bars for lec12 S47 and S48 (package p56).

Deterministic re-expression of published table values (evidence E02/E21, E11, E23).
No stochastic inputs, no interpolation, no curve digitisation. Prints two inline
SVG fragments that are pasted into courses/trustworthy-ai/lec12-fairness.html.

Inputs
  S47  Buolamwini & Gebru, FAT* 2018 (PMLR 81), printed p9, Table 4, "Error Rate"
       rows (1 - TPR, %), PPB benchmark (n = 1,270), audit of May 2017.
       Subgroup order DF, DM, LF, LM; vendor order Microsoft, Face++, IBM.
       NOT Table 5 (South-African subset).
  S48  Same May 2017 DF values vs Raji & Buolamwini, AIES 2019, Tables 1-2,
       August 2018 DF error: Microsoft 1.52, Face++ 4.1, IBM 16.97 (shown to 1 dp).
Parameters
  viewBox width 1080 = rendered width 1080 px (1:1), so font-size = rendered px.
  Linear y scale: SCALE px per percentage point from baseline BASE_Y.

Usage: python3 p56_plot_values_audits.py [s47|s48]
"""
import sys

VENDORS = ["Microsoft", "Face++", "IBM"]
SUBGROUPS = ["DF", "DM", "LF", "LM"]
SUB_NAMES = {"DF": "darker female", "DM": "darker male",
             "LF": "lighter female", "LM": "lighter male"}
# Table 4 error rates (%), Gender Shades, May 2017 audit.
TABLE4 = {
    "Microsoft": {"DF": 20.8, "DM": 6.0, "LF": 1.7, "LM": 0.0},
    "Face++":    {"DF": 34.5, "DM": 0.7, "LF": 9.8, "LM": 0.8},
    "IBM":       {"DF": 34.7, "DM": 12.0, "LF": 7.1, "LM": 0.3},
}
# Actionable Auditing, Aug 2018 DF error (%), exact as printed.
AUG2018_DF = {"Microsoft": 1.52, "Face++": 4.1, "IBM": 16.97}

COLORS = {"DF": "#d94040", "DM": "#e8a0a0", "LF": "#003876", "LM": "#8aa4c8"}
BEFORE, AFTER = "#9aa0a6", "#003876"
SCALE, BASE_Y = 5.0, 262
CENTERS = [245, 570, 895]

# Checks against the evidence entries (E02/E21, E11).
assert [TABLE4[v]["DF"] for v in VENDORS] == [20.8, 34.5, 34.7]
assert sum(sum(r.values()) for r in TABLE4.values()) == 128.4
assert AUG2018_DF == {"Microsoft": 1.52, "Face++": 4.1, "IBM": 16.97}


def fmt(x):
    return f"{x:.1f}"


def bar(x, w, val, color):
    h = max(val * SCALE, 2.0)  # 0.0 drawn as a 2-px stub so it stays visible
    return (f'<rect x="{x:.0f}" y="{BASE_Y - h:.1f}" width="{w}" height="{h:.1f}" fill="{color}"/>'
            f'<text x="{x + w / 2:.0f}" y="{BASE_Y - h - 8:.1f}" font-size="22" fill="#1a1a1a" '
            f'text-anchor="middle">{fmt(val)}</text>')


def s47():
    w, gap = 60, 10
    out = ['<svg viewBox="0 0 1080 332" class="p56-chart" role="img" '
           'aria-label="Gender Shades Table 4 error rates by vendor and subgroup">']
    for i, s in enumerate(SUBGROUPS):  # legend
        lx = 110 + i * 245
        out.append(f'<rect x="{lx}" y="10" width="24" height="24" fill="{COLORS[s]}"/>'
                   f'<text x="{lx + 32}" y="30" font-size="24" fill="#1a1a1a">{s} {SUB_NAMES[s]}</text>')
    for c, v in zip(CENTERS, VENDORS):
        x0 = c - (4 * w + 3 * gap) / 2
        for j, s in enumerate(SUBGROUPS):
            x = x0 + j * (w + gap)
            out.append(bar(x, w, TABLE4[v][s], COLORS[s]))
            out.append(f'<text x="{x + w / 2:.0f}" y="290" font-size="22" fill="#444" '
                       f'text-anchor="middle">{s}</text>')
        out.append(f'<text x="{c}" y="326" font-size="26" font-weight="700" fill="#1a1a1a" '
                   f'text-anchor="middle">{v}</text>')
    out.append(f'<line x1="90" y1="{BASE_Y}" x2="1060" y2="{BASE_Y}" stroke="#777" stroke-width="2"/>')
    out.append('<text x="40" y="170" font-size="22" fill="#555" text-anchor="middle" '
               'transform="rotate(-90 40 170)">error (%)</text>')
    out.append('</svg>')
    return "".join(out)


def s48():
    w, gap = 96, 14
    out = ['<svg viewBox="0 0 1080 332" class="p56-chart" role="img" '
           'aria-label="Error on darker-skinned women, May 2017 vs Aug 2018">']
    out.append(f'<rect x="300" y="10" width="24" height="24" fill="{BEFORE}"/>'
               '<text x="332" y="30" font-size="24" fill="#1a1a1a">May 2017 audit</text>'
               f'<rect x="580" y="10" width="24" height="24" fill="{AFTER}"/>'
               '<text x="612" y="30" font-size="24" fill="#1a1a1a">Aug 2018 re-audit</text>')
    for c, v in zip(CENTERS, VENDORS):
        x0 = c - (2 * w + gap) / 2
        out.append(bar(x0, w, TABLE4[v]["DF"], BEFORE))
        out.append(bar(x0 + w + gap, w, AUG2018_DF[v], AFTER))
        out.append(f'<text x="{x0 + w / 2:.0f}" y="290" font-size="22" fill="#444" text-anchor="middle">2017</text>'
                   f'<text x="{x0 + w + gap + w / 2:.0f}" y="290" font-size="22" fill="#444" '
                   'text-anchor="middle">2018</text>')
        out.append(f'<text x="{c}" y="326" font-size="26" font-weight="700" fill="#1a1a1a" '
                   f'text-anchor="middle">{v}</text>')
    out.append(f'<line x1="90" y1="{BASE_Y}" x2="1060" y2="{BASE_Y}" stroke="#777" stroke-width="2"/>')
    out.append('<text x="40" y="170" font-size="22" fill="#555" text-anchor="middle" '
               'transform="rotate(-90 40 170)">DF error (%)</text>')
    out.append('</svg>')
    return "".join(out)


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "s47"
    print({"s47": s47, "s48": s48}[which]())
