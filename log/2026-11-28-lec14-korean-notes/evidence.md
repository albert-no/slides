# Evidence register — Korean companions

Scope: faithful explanation of the already reviewed lecture at `3dd5a996afc0c89f47573cf9bbb330336a097948`. No fresh literature survey. Original papers remain the evidence; the prior plan is not evidence. The inherited source/version/figure details are in the paired note articles and in `log/2026-11-27-lec14-focused-overview/evidence.md` **at this exact commit**, E01–E26. Preserve that register's corrections, not superseded shorthand.

## E01 — frozen lecture and course inventory
- Source: `3dd5a996afc0c89f47573cf9bbb330336a097948`, main/backup decks and English notes, leaf OUTLINE and prior final review.
- Claim: main59, backup52, paired stable IDs, tech14; three main stories and85+5minutes. This is a curricular inventory, not an empirical result.
- Limits: the old lecture title can change; the empirical argument and ordering do not. Korean prose must not turn a bounded experimental result into a deployment guarantee.

## E02 — Project Vend
- Primary sources: https://www.anthropic.com/research/project-vend-1 (27 June2025; setup, Fig.2, Selling at a loss); https://www.anthropic.com/research/project-vend-2 (18 December2025; The numbers, What changed?). Inherited register E02–E03.
- Published author reports: one bounded office shop, experimental email/physical human work; later changes co-occurred. Purchase approval is a documented setup fact, not an isolated causal explanation for improvement.
- The commercial-evidence check, spending cap and planted-loss test are illustrative design inferences, not reported experimental remedies. Label them accordingly.

## E03 — narrow training and hidden transfer
- Betley et al., Nature649 (2026), https://pmc.ncbi.nlm.nih.gov/articles/PMC12804084/ ; Fig.1 and corrected section heading in inherited E14. Cloud et al., Nature652 (2026), https://pmc.ncbi.nlm.nih.gov/articles/PMC13083239/ ; Figs.1/2 setup,4a preference,3a distinct outcomes,5a model pairs and Methods. Inherited E04–E05,E14–E16,E23.
- Published results, not evidence of intention or feelings. Separate direct insecure-code tuning, animal-biased teacher numbers, and insecure-code-teacher numbers. Format filters and off-task evaluation are different stages.
- Keep Cloud's retained-coherent-answer denominator and separate TruthfulQA score. Do not silently equate the paper's textual about10% with the roughly.08 plotted bar, or conflate question variants.

## E04 — teacher-scored training and recovery
- Askin et al., arXiv2605.12798v2 (preprint), https://arxiv.org/html/2605.12798v2 ; §2,§4, Tables1/10, Figs.5/25, App.E.2.4/E.3. Inherited E06–E07,E16,E26.
- Published preprint results: Qwen27.1/38.9 are post-training evaluations; Llama filtered39.6/unfiltered39.3 are not a significant improvement/worsening claim. 3epochs are passes through training data, not3rounds of conversation.
- OPD: learner writes tokens; teacher supplies token likelihood/log-probability information; an independent judge evaluates later alignment. Scores are not correctness labels. In recovery the teacher is aligned and trajectories receive no extra misalignment filtering; OPD remains learner-generated. Recovery in two tested models is not a general cure.

## E05 — control and adaptive attack evaluation
- Greenblatt et al., AI Control, ICML2024, https://arxiv.org/html/2312.06942v5 ; Fig.1, Tables1–2, §2–3, App.B. Ge-Wang et al., arXiv2606.06529v1, https://arxiv.org/html/2606.06529v1 ; Fig.1A/B, Eq.1, Table2,§4.4,App.A. Inherited E08–E09,E18,E24.
- Published results within different constructed testbeds. Greenblatt: resampled simulated5000-problem runs,15/62% whole-run no-backdoor probability under tested attacks, not accuracy; trusted models are assumed, protected audit is simulated. Preserve audit-budget setup and exceptions in details.
- Ge-Wang: caught/(caught + successful uncaught); unsuccessful uncaught attempts excluded. Retrospective abort policy/threshold choice gives an upper bound, not live deployment evidence or a directly comparable score.

## E06 — optional backup evidence
- Inherited exact backup notes and E10–E13,E17,E23–E25 list primary sources/versions for METR/RepliBench, scheming/sandbagging, MAST/multi-agent spread/collusion, control variants, persuasion/companions, and B6 follow-ups.
- Published studies plus illustrative examples. Preserve every source's setup, assumptions and inference limits. The annotated-failure shares are not deployment frequencies; component pass@10 is not full replication; persuasion effects are not durable behavioral effects; usage associations are not randomized causal effects.
- B6: van der Weijden https://arxiv.org/html/2609.12586v1 (preference reproduction varies); Yanagisawa https://arxiv.org/html/2609.22215v1 (preference/style mitigation, harmful transfer not reliably induced); Nief https://arxiv.org/abs/2606.00831v2 (author revision notice checked2026-11-27). Date that last status rather than pretending it was freshly surveyed. Do not teach the critique as settled debunking.

## E07 — conceptual prerequisites already in the course
- Source: exact baseline lec01,lec07,lec09,lec10,lec13 and their notes/leaf OUTLINE; inherited E21–E22 course-overlap audit. Curricular definitions, not new results.
- Re-explain locally in Korean only what is needed: model/output/system distinctions; token/prediction/weight update; prompt vs training; teacher vs learner vs judge; controls vs AI control; monitor vs audit vs enforcement; empirical outcome vs inference.
- Prior-deck links are optional follow-up, never a substitute for the new guide's explanation. Do not re-teach all previous studies or add prior lectures to the required flow.

## E08 — original pedagogical analogies/calculations
- Label: illustrative example / our calculation, not a published result.
- Any new toy price/word-choice/counting example must say it is made up and show its assumptions; it cannot be used as evidence of efficacy, prevalence or a hidden mechanism.
- Prefer qualitative examples with no invented empirical percentages. The same term/role must mean the same thing across both Korean documents and the source lecture.
