#!/usr/bin/env python3
"""Inline-SVG bar charts for lec13 S40a, S40b and S41 (package p5).

Usage: python3 p5-bars.py {s40a|s40b|s41}  -> prints the <svg> markup pasted into the deck.

Inputs (exact pinned values, not re-derived):
  AgentDojo (Debenedetti et al., arXiv 2406.13352v3) Table 5, GPT-4o, fixed "important message" attack.
    Clean (benign) utility, % of 97 user tasks; utility under attack and targeted ASR, % of 629 security cases.
  Nasr, Carlini et al. (arXiv 2510.09023v1) Table 7, Gemini-2.5 Pro rows: static (fixed) ASR and
    search-attack ASR, % of the 80-case attack subset.
Bar lengths use the full-precision table values; the printed labels use the deck's rounding (one decimal
for Table 5, integers for Table 7).
"""
import sys
from decimal import Decimal, ROUND_HALF_UP

BLUE, RED, GRAY, LRED = "#003876", "#d94040", "#6b7280", "#f4c7c7"

# AgentDojo Table 5 (GPT-4o): (clean utility, utility under attack, targeted ASR)
T5 = {
    "No defense":         (69.0, 50.01, 57.69),
    "Delimiting":         (72.66, 55.64, 41.65),
    "Repeat prompt":      (85.53, 67.25, 27.82),
    "Detector":           (41.49, 21.14, 7.95),
    "Tool filter":        (73.13, 56.28, 6.84),
}
# Nasr et al. Table 7, Gemini-2.5 Pro: (fixed/static ASR, search-attack ASR)
T7 = [
    ("No defense", 30, 100),
    ("Spotlighting", 28, 99),
    ("Prompt sandwiching", 21, 95),
    ("Prompt Guard", 26, 94),
    ("MELON", 0, 89),
]


def r1(v):
    """Round half up to one decimal, as the deck's baseline table did (41.65 -> 41.7, 67.25 -> 67.3)."""
    return str(Decimal(str(v)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))


HALO = 'stroke="#fff" stroke-width="6" paint-order="stroke"'


def esc(s):
    return s.replace("&", "&amp;")


def s40(rows):
    # viewBox 1080 wide, drawn at 1080 px -> 1 unit = 1 px.
    # Panels i=0,1,2 (clean utility, utility under attack, attack success) start at X0_i = 225 + 290*i.
    # Bar length = 2.1 * value (100 % -> 210 units). Row r bar: y = 84 + 64*r, height 38.
    # Dashed line at the no-defense value: x = X0_i + 2.1 * v_none_i.
    heads = [("Clean utility", "higher = better", BLUE),
             ("Utility under attack", "higher = better", BLUE),
             ("Attack success", "lower = better", RED)]
    S, X0, DX, Y0, RH, BH = 2.1, 225, 290, 84, 64, 38
    H = Y0 + RH * len(rows) + 6
    label = "; ".join(f"{n}: clean utility {r1(T5[n][0])}, utility under attack {r1(T5[n][1])}, "
                      f"attack success {r1(T5[n][2])} percent" for n in rows)
    out = [f'<svg viewBox="0 0 1080 {H}" style="width:100%;display:block;" role="img" '
           f'aria-label="Bar chart, AgentDojo GPT-4o. {label}">']
    base = T5["No defense"]
    for i, (h, sub, col) in enumerate(heads):
        x0 = X0 + DX * i
        out.append(f'<text x="{x0}" y="28" font-size="25" font-weight="700" fill="{col}">{h}</text>')
        out.append(f'<text x="{x0}" y="58" font-size="21" fill="{GRAY}">{sub}</text>')
        out.append(f'<line x1="{x0}" y1="{Y0-8}" x2="{x0}" y2="{H-4}" stroke="{GRAY}" stroke-width="2"/>')
    for i in range(3):
        x = round(X0 + DX * i + S * base[i], 2)
        out.append(f'<line x1="{x}" y1="{Y0-8}" x2="{x}" y2="{H-4}" stroke="{GRAY}" stroke-width="2" stroke-dasharray="6 5"/>')
    for r, name in enumerate(rows):
        y = Y0 + RH * r
        vals = T5[name]
        is_base = name == "No defense"
        out.append(f'<text x="205" y="{y+28}" font-size="25" text-anchor="end" font-weight="700" '
                   f'fill="{GRAY if is_base else "#222"}">{esc(name)}</text>')
        for i, v in enumerate(vals):
            x0 = X0 + DX * i
            col = GRAY if is_base else heads[i][2]
            w = round(S * v, 2)
            out.append(f'<rect x="{x0}" y="{y}" width="{w}" height="{BH}" fill="{col}"/>')
            # White backing so the dashed no-defense line never runs through a value label
            # (label width estimated at 14 units per character for 23-unit bold digits).
            lbl = r1(v)
            out.append(f'<rect x="{round(x0 + w + 4, 2)}" y="{y+5}" width="{14*len(lbl)+8}" height="30" fill="#fff"/>')
            out.append(f'<text x="{round(x0 + w + 8, 2)}" y="{y+28}" font-size="23" fill="{col}" '
                       f'font-weight="700" {HALO}>{r1(v)}</text>')
    out.append('</svg>')
    return "\n".join(out)


def s41():
    # viewBox 1080 wide, drawn at 1080 px. Bars start at X0 = 270; length = 7.0 * ASR (100 % -> 700 units).
    # Row r: fixed bar y = 52 + 58*r, search bar y + 25; bar height 22.
    S, X0, Y0, RH, BH = 7.0, 270, 52, 58, 22
    H = Y0 + RH * len(T7)
    label = "; ".join(f"{n}: fixed {f}, search {q} percent" for n, f, q in T7)
    out = [f'<svg viewBox="0 0 1080 {H}" style="width:100%;display:block;" role="img" '
           f'aria-label="Bar chart, attack success on Gemini-2.5 Pro. {label}">']
    out.append(f'<rect x="{X0}" y="6" width="34" height="22" fill="{LRED}" stroke="{RED}" stroke-width="2"/>')
    out.append(f'<text x="{X0+44}" y="25" font-size="23" fill="#222">fixed attack</text>')
    out.append(f'<rect x="{X0+250}" y="6" width="34" height="22" fill="{RED}"/>')
    out.append(f'<text x="{X0+294}" y="25" font-size="23" fill="#222">search attack</text>')
    out.append(f'<line x1="{X0}" y1="{Y0-6}" x2="{X0}" y2="{H-4}" stroke="{GRAY}" stroke-width="2"/>')
    for r, (name, fixed, search) in enumerate(T7):
        y = Y0 + RH * r
        out.append(f'<text x="255" y="{y+33}" font-size="25" text-anchor="end" font-weight="700" fill="#222">{name}</text>')
        wf, ws = S * fixed, S * search
        if fixed > 0:
            out.append(f'<rect x="{X0}" y="{y}" width="{wf:g}" height="{BH}" fill="{LRED}" stroke="{RED}" stroke-width="2"/>')
        out.append(f'<text x="{X0 + wf + 8:g}" y="{y+19}" font-size="22" fill="{RED}" {HALO}>{fixed}</text>')
        out.append(f'<rect x="{X0}" y="{y+25}" width="{ws:g}" height="{BH}" fill="{RED}"/>')
        out.append(f'<text x="{X0 + ws + 8:g}" y="{y+44}" font-size="22" font-weight="700" fill="{RED}" {HALO}>{search}</text>')
    out.append('</svg>')
    return "\n".join(out)


if __name__ == "__main__":
    which = sys.argv[1]
    if which == "s40a":
        print(s40(["No defense", "Delimiting", "Repeat prompt"]))
    elif which == "s40b":
        print(s40(["No defense", "Detector", "Tool filter"]))
    elif which == "s41":
        print(s41())
