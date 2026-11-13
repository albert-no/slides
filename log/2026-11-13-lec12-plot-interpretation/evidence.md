# Evidence register
Verified 2026-11-13 against the primary sources below, the existing figure crops, and the frozen baseline. Append-only. Plot read-offs are approximate observations, not new statistical estimates or exact tabulated values.

## E01 — Credit-score study and five rules
- Claim: Hardt, Price and Srebro compare profit-optimal thresholds under five constraints on the same credit-score data. Shared threshold aligns raw-score cutoffs; demographic parity equalizes qualification fractions; equal opportunity equalizes qualification among non-defaulters; equalized odds additionally equalizes qualification among defaulters. Unconstrained max-profit optimizes modeled lender utility.
- Source/version: https://arxiv.org/pdf/1610.02413v1 — §7 “Case study: FICO scores”, printed pp16–19, especially Figure 9 on p19; NeurIPS 2016.
- Setup: 301,536 TransUnion TransRisk scores from 2003, four race groups; outcome is any-account 90-day default over the following 18–24 months, not default on a newly granted loan. Modeled cost ratio 82/18 underlies Figure 9. These details belong in notes, not an expanded main-slide statistics list.
- Limit: not observed causal effects of policy changes, social-welfare rankings, or a claim about current lending deployment.
- Label: published result.

## E02 — How to interpret Figure 9
- Claim: Moving a deterministic cutoff right excludes more scores within that group. The shared-threshold row aligns group markers; demographic-parity raw thresholds spread apart. In this example equalized odds uses two thresholds for some groups: reject below, accept above, randomize between. Horizontal segments are not uncertainty intervals and do not mean a 50/50 lottery. A lone marker can be a degenerate interval.
- Source/version: E01, §7 pp17–19, Figure 9 and paragraph beginning “Equalized odds requires…”.
- Setup: Figure 9 left/raw-score panel; group encodings are Asian blue diamonds, White green circles, Hispanic red squares, Black cyan pentagons. Within-group percentile panel is different and is not needed to read raw scores.
- Limit: randomization is needed for the illustrated optimum, not universally for every equalized-odds problem. Threshold position alone does not order overall fairness.
- Label: published result; the direction explanation follows the stated threshold rule.

## E03 — What COMPAS and the audit measure
- Claim: COMPAS is Northpointe's commercial risk-assessment tool. ProPublica's Broward County audit used 2013–14 scores; in that setting scores informed pretrial decisions. Audit flag: scores above 4 (5–10), unlike vendor “High” (8–10). Recorded outcome: new arrest within two years, not a direct measure of all offending.
- Sources/version: https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm — Larson, Mattu, Kirchner and Angwin, 23 May 2016, introduction; “How We Acquired the Data”; “How We Defined Recidivism”; “Analysis”. Also https://arxiv.org/html/1703.00056v1 — Chouldechova, 28 February 2017, §§1, 1.2, 2.1, 5.
- Setup: vendor Low 1–4, Medium 5–7, High 8–10; recidivism-risk scale, not violent-recidivism or failure-to-appear score. COMPAS expands to Correctional Offender Management Profiling for Alternative Sanctions.
- Limit: the audit's binary flag is not an automatic detention decision. Do not describe scores as probabilities, or equate no rearrest with innocence/no offending. Historical case, not current legal advice.
- Label: published result.

## E04 — Populations are not interchangeable
- Claim: Chouldechova's plotted Black/White analysis uses 6,150 records after the paper's filtering (3,696 and 2,454); Figure 2(b) is further restricted to misdemeanor charges. ProPublica uses different cohorts for different analyses. Do not attach one global sample count to every plot.
- Source/version: https://arxiv.org/html/1703.00056v1 §1.2; Figure 2(b), §3.1; ProPublica source in E03, “Analysis”.
- Setup: 2013–14 Broward scores and two-year recorded outcomes. Original paper's group categories are African-American/Caucasian; slide labels Black/White.
- Limit: not representative of all US defendants. Main slides need population identification, not additional sample counts; preserve these distinctions in the notes.
- Label: published result.

## E05 — FPR within prior-count bins
- Claim: In Chouldechova Figure 2(b), gray (Black) point estimates exceed orange (White) in each prior-count bin, including zero priors. FPR's denominator is non-rearrested defendants of the same race and bin, restricted to misdemeanor charges; numerator is those flagged above 4. Whiskers are 95% confidence intervals.
- Source/version: https://arxiv.org/html/1703.00056v1 §3.1 “Conditioning on other covariates”, Figure 2(b); PDF printed p10. Existing crop: courses/trustworthy-ai/figs/chouldechova-fpr-priors-hi.png.
- Setup: bins 0, 1–3, 4–6, 7–10, >10. The zero-prior pair visually reads roughly one in five versus one in ten; optional approximate read-off only, not exact reported percentages.
- Limit: within-bin description is not causal identification or full covariate adjustment. Wide high-prior intervals do not justify claims of significant differences in every bin. Prefer the robust zero-prior comparison over a dramatic high-prior number.
- Label: published result; optional rounded values are visual readings of the published plot.

## E06 — Same decile, not probability calibration
- Claim: Figure 1(a) compares recorded rearrest shares between races within each exact COMPAS decile. The paper describes approximate calibration in the sense of its Definition 1 (across-group outcome agreement at a score). Decile 7 is not a prediction of 70%.
- Source/version: https://arxiv.org/html/1703.00056v1 §§2.1–2.3, Definition 1 / Eq2.1 and Figure 1(a), PDF p6. Existing crop: courses/trustworthy-ai/figs/lec12-visual-motivation/p3-chouldechova-fig1-left.png.
- Setup: gray Black, orange White, 95% confidence intervals. One pair at x=6 contains only people scored 6; both shares visually near 60%, as an approximate read-off. Outcome generally rises across deciles; not strictly monotone in both empirical series.
- Limit: not exact equality, probability-valued calibration, PPV of everyone above 6, or evidence of equal error rates. Figure 1 has FOUR panels; this is the upper-left panel (a), not one of only two panels.
- Label: published result; optional rounded reading is a visual approximation.

## E07 — Cutoff pools multiple deciles
- Claim: Figure 1(b) plots PPV: recorded rearrest among defendants whose score exceeds each cutoff. At cutoff 4 the denominator pools scores 5–10, unlike Figure 1(a)'s single-score population. The paper describes predictive parity for cutoffs 4 or higher; teach this as approximate similarity, not exact equality.
- Source/version: https://arxiv.org/html/1703.00056v1 Definition 2 / Eq2.2, §2.3, Figure 1(b), PDF p6. Existing crop: courses/trustworthy-ai/figs/lec12-visual-motivation/p3-chouldechova-fig1-right.png.
- Setup: x=0–9, one race pair per cutoff, gray Black/orange White, 95% intervals. Cutoff 4 shares visually about 0.63/0.59; optional rough read-offs only. Successive cutoffs select nested, changing populations; cutoff 9 retains only score 10.
- Limit: interval overlap is not a test proving equality; higher PPV alone is not “fairer”. This is Chouldechova's reanalysis illustrating a criterion emphasized by the vendor, not a vendor-produced plot. No logical claim that calibration always implies predictive parity.
- Label: published result; optional rounded readings are visual approximations.

## E08 — Distinguishing the three questions
- Claim: FPR asks who was flagged among the non-rearrested; calibration asks who was rearrested at the same score; PPV asks who was rearrested among everyone above a cutoff. Different denominators allow an error-rate gap and roughly comparable PPV to coexist.
- Source/version: Chouldechova v1, https://arxiv.org/html/1703.00056v1 Definitions 1–3, Eqs2.1–2.4, §2.3 and Figure 1. Prior classroom definitions: baseline S13b/S13c, S19a/b and S20b.
- Setup: same recorded outcome and race comparison, different conditioning populations. Reuse the deck's already taught denominators rather than introducing another formalism.
- Limit: no single criterion establishes overall fairness; this job does not expand the later impossibility theorem or revisit its proof.
- Label: published result / explanatory synthesis of the definitions.

## E09 — “Most important person” is an illustrative question, not a visual ground truth
- Claim: a photograph without role information or an importance criterion does not establish which pictured person is “most important”. The example asks what information a system would need, rather than assigning importance from appearance.
- Source/version: Albert's C05; owner-authored classroom scenario in plan-v2.md, S77. This is reasoning about the specified missing information, not a reported model experiment.
- Setup: one group photograph, no names or role labels supplied; no identified real public figures. All pictured people are treated as equally deserving of respect; “importance” needs an external task-specific criterion.
- Limit: no claim that any particular model selected a person, no fabricated model quote, and no assertion about the pictured people's identities, competence, character, occupation or status. If an actual model test is later proposed, its exact prompt, model, date and unedited response require separate evidence.
- Label: illustrative example. Photograph provenance must be supplied in work-r1; generation or licensed/attributed photo, not an invented documentary event.

## E10 — CEO-generation opening example
- Claim: an image-generation prompt can leave appearance unspecified; the displayed completion chooses a concrete depiction. The chosen output is not, by itself, an estimate of model-wide bias or real-world CEO demographics.
- Source/version: Albert's C05; planned prompt “Generate a photo of a CEO.” (CEO = chief executive officer), S78 in plan-v2.md. No output exists in this evidence entry yet; slides owns producing and documenting the asset.
- Setup: one actual generation with no demographic steering or stereotype-seeking retries; record exact submitted prompt and any exposed revision, tool/model, date, output path and selection rule. Keep the first technically usable result regardless of whether it matches an anticipated stereotype. Report any retries and why.
- Limit: a hand-selected, edited or art-directed portrait cannot be represented as an unmodified result of the short prompt. Do not invent a model name or claim current generators always produce a particular demographic. Generation failure is a plan issue, not license to stage a fake result.
- Label: illustrative example; execution provenance unresolved until the work report.

## E11 — Existing occupation study supplies context, not evidence about a new CEO output
- Claim: the existing lecture source studies neutral occupation prompts using multiple outputs, rather than establishing a distribution from one portrait. It includes “a CEO” in its occupation prompt list; this does not mean an arbitrary CEO image comes from the paper.
- Source/version: Bianchi et al., FAccT 2023, arXiv:2211.03759v2 (7 June 2023), https://arxiv.org/html/2211.03759v2 — §2.2, Appendix B.1/B.2 and C. The source says 100 generated images per occupation and Stable Diffusion v1.4; existing lecture S51a/b already covers that study.
- Setup: prompt template “A photo of the face of [OCCUPATION]”. Figure 3 shows software developer, flight attendant, chef, cook, taxi driver and housekeeper; Appendix Figure A6 shows pilot, firefighter, nurse and therapist. Both source images were inspected. Neither is a CEO-photo source.
- Limit: historical study, not a test of the new demonstration's generator. Opening does not need the later percentages or a new literature survey. If generation is unavailable, propose an honestly attributed published occupation example rather than relabeling another occupation as CEO.
- Label: published result / source-scope check.
