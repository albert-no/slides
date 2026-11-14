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

# Panels for S25/S26a/S26b (round 2). Source: Chouldechova, arXiv:1703.00056v1, vector figures.
# Plot panel only, 300 dpi; tick labels, axis titles, panel titles and legend lie outside the crop
# and are restated outside the image in the slide SVG. Usage: sh crops.sh ... after setting Q.
# Q=/path/to/1703.00056v1.pdf
# pdftoppm -r 300 -f 6 -l 6 -x 431 -y 617 -W 790 -H 679 -png -singlefile "$Q" chouldechova-fig1a-panel    # Fig 1(a) calibration
# pdftoppm -r 300 -f 6 -l 6 -x 1444 -y 623 -W 788 -H 671 -png -singlefile "$Q" chouldechova-fig1b-panel   # Fig 1(b) predictive parity
# pdftoppm -r 300 -f 10 -l 10 -x 1408 -y 396 -W 823 -H 458 -png -singlefile "$Q" chouldechova-fig2b-panel # Fig 2(b) FPR by priors, misdemeanor
# External tick positions come from pdftotext -bbox tick-label centres on the same pages.
