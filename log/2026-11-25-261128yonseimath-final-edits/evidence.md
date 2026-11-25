# Evidence — append-only

Focused verification for a local author revision; no new literature survey. Checked 2026-11-25. Evidence IDs are scoped to this job; unchanged note-source references from the preceding polish need not be renumbered.

## E01 — Author's requested scope and biographical self-report
- Label: author-supplied information / viewpoint.
- Source: C01–C06, Albert message26. Original personal-reflection wording is also recorded in the initial draft job requests and the preceding polish evidenceE11, both available at baseline0bf4927.
- Claims: completed Yonsei science-gifted program 심화반/사사반; SNU 전기공학부/수리과학부 double major; Stanford MS/PhD EE; former Hongik 전자전기공학부 assistant professor; currently Yonsei 인공지능학과 associate professor. Use only these five items and omit years. No invented start date, childhood anecdote or assertion that this program caused the entire career.
- C05 directly replaces the prior growth interpretation with fixed-perimeter rectangle area; C04/C06 delete text rather than add explanations. Latest direct instruction governs.

## E02 — Public faculty profile
- Label: published self-authored institutional profile, verified current page.
- Source: Albert No, AI-ISL, https://ai-isl.yonsei.ac.kr/albert-no.html , profile heading, “Education” and “Work experience,” opened2026-11-25.
- Supports: Associate Professor, Department of Artificial Intelligence, Yonsei University; Stanford PhD and MS in Electrical Engineering; Seoul National University BS in Electrical Engineering and Mathematical Science (Double Major); past Hongik assistant professorship. The page also lists another Hongik rank and an industry role, but those are deliberately omitted per C01, not added to the requested selective introduction.
- The landing page does not list gifted-program 심화반/사사반 or the Hongik department's Korean name; those are supported by the author's explicit self-report E01. Past assistant professorship is not a claim about his last Hongik rank. No career years in the slide or introductory note narrative. The event date and dates in scientific citations elsewhere are outside this deletion request.

## E03 — AM–GM as maximum rectangle area at fixed perimeter
- Label: published inequality plus our elementary geometric interpretation/calculation.
- Mathematical source: Boyd & Vandenberghe, Convex Optimization,2004, §3.1.8–3.1.9, printedpp77–78, https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf . This precise source and log/AM–GM equivalence were verified in the preceding jobs (polish evidenceE10/E12 at the frozen baseline); no theorem/version change.
- For a rectangle with positive sidesa,b, perimeterP=2(a+b), areaA=ab. Holding P fixed holds a+b fixed. Setm=(a+b)/2: the square of sidem has the same perimeter4m=2(a+b), and area m²≥ab, with equality exactlya=b. Equivalently m²−ab=(a−b)²/4≥0. The main claim must say “직사각형”: a square is not the maximum-area shape among all plane figures at a given perimeter.
- Exhibit: one concise symbolic comparison of a non-square rectangle and a square with the SAME perimeter, not a numerical exercise. If a=2,b=8,m=5 are convenient internal drawing inputs, both perimeters are20 and areas16/25; do not display these numbers. Use one common isotropic length scale so the area comparison is faithful. Final geometry/code path and parameters are to be recorded in work-r1; optional existing local generator `talks/261128yonseimath/figs/generate-figures.py`, output path decided by slides.
- One glanceable formula `ab ≤ ((a+b)/2)^2` is enough if useful; no proof chain, growth terminology or general isoperimetric theorem. The following Jensen main exhibit remains unchanged; its note only needs the outgoing growth-language bridge replaced by the rectangle-area bridge.

## E04 — Meaning of the added problem/idea labels and unchanged evidence
- Label: author-supplied framing, grounded in the preceding sourced mechanism.
- C02/C03 explicitly connect AI-assisted experimentation back to “LLM이 생성한 문장에 표식남기기” and “의도적인 통계 삽입”. Here the latter means deliberately biasing generation so the resulting text has a detectable statistical property; it does not mean literally printing statistics/numbers in the sentence or claiming an infallible detector.
- Supporting mechanism: Kirchenbauer et al., “A Watermark for Large Language Models,” ICML2023, §3.1 Algorithm2, https://proceedings.mlr.press/v202/kirchenbauer23a/kirchenbauer23a.pdf ; already verified and implemented in preceding polish evidenceE06/E12. This job changes framing, not the algorithm or demonstration data.
- All unrelated factual exhibits and source qualifications carry forward from `log/2026-11-25-261128yonseimath-polish/evidence.md` at baseline0bf4927. No new benchmarks, quantitative claims or claims of an actually conducted AI experiment are authorized by this request.
