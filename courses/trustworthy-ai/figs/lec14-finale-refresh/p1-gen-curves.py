#!/usr/bin/env python3
"""Print the SVG path data for two lec14 schematic curves (P1, 2026-11-22).

S06: P(all n steps right) = 0.95**n for n = 0..20 (illustrative arithmetic,
     independent steps, no recovery). Mapping: X = 80 + 25.5 n, Y = 340 - 300 p.
S09: schematic decreasing logistic success curve, p(x) = 1 / (1 + exp((x - 575) / 70))
     for x = 110..1040 step 10. Mapping: Y = 270 - 230 p. Not fitted to any data.

Usage: python3 p1-gen-curves.py
"""
import math

def s06():
    pts = []
    for n in range(21):
        p = 0.95 ** n
        pts.append(f"{80 + 25.5 * n:.1f},{340 - 300 * p:.1f}")
    return "M" + " L".join(pts), 0.95 ** 20

def s09():
    pts = []
    for x in range(110, 1041, 10):
        p = 1 / (1 + math.exp((x - 575) / 70))
        pts.append(f"{x},{270 - 230 * p:.1f}")
    return "M" + " L".join(pts)

if __name__ == "__main__":
    path, end = s06()
    print("S06 path:", path)
    print("S06 endpoint p =", round(end, 4))
    print("S09 path:", s09())
