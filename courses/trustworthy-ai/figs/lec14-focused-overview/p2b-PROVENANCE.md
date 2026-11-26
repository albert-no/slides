# P2b asset provenance (job 2026-11-27-lec14-focused-overview)

Retrieved 2026-11-27 by direct HTTP from https://arxiv.org/html/2605.12798v2 (arXiv HTML of v2, dated 10 Nov 2026).

## p2b-askin-bars.py → inline SVGs on S74a and S74b

- Source: Askin, Ustaomeroglu, Nayak, Joshi, Qu & Joe-Wong, "Examining the Impact of Data and Training Methods on Emergent and Subliminal Misalignment", arXiv 2605.12798v2 (preprint). Metadata: https://arxiv.org/abs/2605.12798v2
- S74a inputs: Table 1 ("Qwen3-14B: narrow-eval EM rate (%) across training channels, aggregated by the teacher's misaligned task"), column "Avg.": SFT 27.1, OPD 38.9. Rows Teacher (50.6) and OPTD (39.7) not drawn. Table 1 has no untrained-learner row.
- S74b inputs: Table 10 ("Narrow-eval EM rate (%) for filtered and unfiltered OPD after three epochs"), column "Llama" (Llama-3.1-8B-Instruct): OPD (Filtered) 39.6, OPD (Unfiltered) 39.3. Other columns (Qwen 37.6/36.8, OLMo 33.8/34.4) not drawn. Filter details from App. E.2.4: online Gemini-2.5-Flash, coherence > 60 and alignment > 60, kept 80–85% of samples, learning rate 1e-4.
- Metric (§2): EM rate = % of responses that a Gemini-2.5-Flash judge scores alignment < 30 and coherence > 50 (0–100 scales).
- Commands: `python3 -I p2b-askin-bars.py s74a` and `python3 -I p2b-askin-bars.py s74b` (each prints the SVG pasted into the slide).
- Transformation: linear scaling only (6.4 viewBox units per percentage point; zero-based 0–100% axis). The two charts are separate SVGs for different models/tables; nothing is averaged, combined or connected. No uncertainty drawn: the tables report none.
- Plain-language labels: SFT = "Teacher-written answers / learner copies them"; OPD = "Teacher scores learner tokens / learner writes"; filtered/unfiltered OPD = "Judge filter on" / "No filter".
- Values checked against evidence.md E16: identical.

## Own illustrative diagrams (no data) — S73a, S73b, S73c, S75a

Inline SVG schematics drawn for this lecture (not paper figures); labelled "Illustrative" in each cite line. The S73a/b example prompt and tokens and the S73b/c score-bar heights are invented and carry no data. They render the on-policy distillation setup described in Askin et al. §2 and §4 ("the teacher only scores the sampled tokens").
