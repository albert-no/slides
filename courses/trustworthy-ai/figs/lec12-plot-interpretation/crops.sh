#!/bin/sh
# Crops for lec12 S21a/S21b (job 2026-11-13-lec12-plot-interpretation).
# Source: Hardt, Price & Srebro, arXiv:1610.02413v1 (NeurIPS 2016), PDF page 19,
# Figure 9 left panel "FICO score thresholds (raw)". Unmodified pixel crops of the
# vector PDF at 300 dpi; same x range and scale in every crop, rows selected only.
# Usage: sh crops.sh /path/to/1610.02413v1.pdf
P="$1"
c() { pdftoppm -r 300 -f 19 -l 19 -x 352 -y "$2" -W 900 -H "$3" -png -singlefile "$P" "$1"; }
c hardt-fig9-raw-profit-single 397 285   # legend + Max profit + Single threshold rows (title omitted)
c hardt-fig9-raw-demography    954 232   # Demography row + x axis
c hardt-fig9-raw-opp-odds      686 264   # Opportunity + Equal odds rows
c hardt-fig9-raw-axis         1092  80   # x axis only
