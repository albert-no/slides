# Evidence register (append-only)

Survey cutoff / checked: 2026-11-26 Asia/Seoul. Repository sources are fixed at `467cf0630d25ec9929c9e1e87cea901224637487` (B). `courses/trustworthy-ai/` abbreviated as COURSE below. The course is the reuse map, not independent proof of its public factual claims. Public sources below were reopened for this plan. No measurements or figures have been generated for this job. Any future generated exhibit must record inputs and the repo regeneration path here before review.

## E01 — Course spine and semester survey
- Claim: lec01 supplies the overview argument; lec02–14 refine evidence and distinctions rather than imposing a fourteen-topic mini-course.
- Source/version: B, `COURSE/OUTLINE.md`, Modules, Lecture index, and relevant lecture sections; all 14 main-deck title sequences, with selected bodies/paired notes read. Immutable base URL: https://github.com/albert-no/slides/tree/467cf0630d25ec9929c9e1e87cea901224637487/courses/trustworthy-ai . Detailed reuse ledger below.
- Setup: current main, including the Nov15 notes accuracy pass, Nov16 fairness, Nov20 injection and Nov22 agentic-finale revisions. Main page counts 46/69/70/65/68/75/75/101/91/88/74/87/65/51.
- Does not establish: that every dated claim in the old overview is current; new talk deliberately omits unverified frontier incidents, statistics and legal timelines.
- Label: illustrative example (editorial synthesis of the course; not an empirical result).

### Lecture-by-lecture evidence map
| Lecture / exact file | Selected current locations | Reuse / deliberately omit |
|---|---|---|
| 01 `lec01-introduction.html` | pp4–6 capability/stakes; pp8–28 cases; pp34–40 system/threat framing; pp44–45 boardroom questions | Main argument and most case families. Drop course map, teaching logistics, technical threat grid, redundant taxonomy, speculative/current-statistics detours. |
| 02 `lec02-privacy-dp.html` | pp6–22 privacy questions; p40 limits; p67 boardroom | Input exposure versus learned data; no differential-privacy mechanism, epsilon, coins or numerical guarantee. |
| 03 `lec03-mia.html` | pp5–10 membership as sensitive information; pp58–62 evaluation cautions | Privacy backdrop in notes only. No separate membership-inference lesson, ROC or base-rate exercise. |
| 04 `lec04-memorization.html` | pp18–26 GPT-2/divergence; pp49–55 mitigation | One memorable extraction example with public-web-data qualification. No extraction recipes or model-size plot. |
| 05 `lec05-unlearning.html` | pp8–16 deletion goals; pp48–61 removal vs suppression | One file-deletion versus learned-influence picture, no method or legal-rights lecture. |
| 06 `lec06-hallucination.html` | pp4–11 unreliable fluent answers; pp50,54,58–61 abstention/grounding | Mata + verify important answers. No calibration, conformal prediction, entropy, bounds. |
| 07 `lec07-alignment-failures.html` | pp23–27 sycophancy; pp29–30 gaming; pp70–72 synthesis | Deployed GPT-4o rollback and plain-language target/proxy gap; no RLHF/DPO, scheming rates or consciousness/motive claims. |
| 08 `lec08-adversarial.html` | pp4–18 ordinary vs adversarial input; pp85–90 physical setting | One stop-sign laboratory example. No gradients, perturbation norms, attacks or certificates. |
| 09 `lec09-poisoning.html` | pp4–18 integrity/entry points; pp33–47 backdoors | One upstream manipulation concept; preserve training-time vs read-time distinction. No BadNets metrics, algorithm or poisoning recipe. |
| 10 `lec10-jailbreak.html` | pp4–13 refusal and threat; pp58–67 evaluation; pp84–85 limits | Brief distinction from prompt injection; benchmark claims need setup. No jailbreak payloads, search or architecture. |
| 11 `lec11-synthetic-media.html` | pp7,10–12 deepfake/origin; pp58–64,70–72 provenance | Deepfake payment case, origin is not truth; no token/watermark math, detector rankings or unverified 2026 product/legal claims. |
| 12 `lec12-fairness.html` | pp7–8 (S04a/b) health cost proxy; p53 harm first; p75 (S47) Gender Shades; p84 (S54a) need | Updated proxy explanation + subgroup gap. No COMPAS denominator lesson, incompatible metrics or fairness optimization. |
| 13 `lec13-prompt-injection.html` | pp4–6,19–20 input/authority; pp27–28 GitHub demo; pp51–60 boundary/approval | Opening and later return; exact actor/permission map; do not equate approval with proof. No attack strings or CaMeL architecture. |
| 14 `lec14-agentic-threats.html` | p7 autonomy dials; p15 capability ≠ safe runtime; pp31–35 multi-agent evidence; pp45,50 evaluation/synthesis | Delegation, propagation, bounded evidence, human stop. No long-task fits, loss curves, collusion speculation or lab-to-world extrapolation. |

## E02 — Albert's real use case
- Claim: as Vice Dean (부원장/인융대학원), Albert uses agents to turn recurring graduate-school paperwork emails into a private manual; updated weekly; read-only mail summarization, his manual approval, then a separate coding agent.
- Source/version/locator: Albert message 12, 2026-11-26, requests C11–C16 (first-person account, no external URL).
- Setup: only the workflow he stated. Illustrations of calendars, inboxes, manual pages and approval are synthetic.
- Does not establish: actual deployment permissions were independently audited; specific paperwork types, metrics/time savings, a breach, or a code-review gate after coding. Extra safeguards must be called recommendations, not facts about his setup.
- Label: illustrative example grounded in author testimony (not a published result).

## E03 — Trust is contextual, not a single score
- Claim: assess the task, affected people/data, delegated authority, evidence and response owner; capability alone is not sufficient for safe delegation.
- Sources: B lec01 pp5–6,35–40,45; lec14 pp7,15,45,50. Public basis: https://arxiv.org/html/2503.18813v2 §§3–5,9; E07–E15 illustrate different failure types.
- Setup: editorial synthesis/recommendations, not a measured formula or universal assurance framework. The familiar rising-capability/rising-risk diagram, if used, is conceptual, not data.
- Does not establish: risk rises monotonically with intelligence, every agent is dangerous, or a particular checklist certifies safety.
- Label: illustrative example / editorial synthesis.

## E04 — Prompt injection and enforced authority boundaries
- Claim: untrusted source text can redirect an agent; control and action arguments both matter. Separating models is not by itself a complete security boundary.
- Primary: Debenedetti et al., *Defeating Prompt Injections by Design*, arXiv 2503.18813v2 (24 Jun 2025), https://arxiv.org/html/2503.18813v2 , §2 (including “Is Dual LLM of Willison enough?”), Figs1–2, §3.1, §9.2–9.3. B lec13 pp51–60.
- Setup: published research design and evaluation with defined policies/threat model; no numerical result imported into this talk.
- Does not establish: that Albert's summarize→approve→code system is CaMeL, that summaries are sanitized, or that prompt injection is solved. Incorrect permitted content and human fatigue remain relevant.
- Label: published result, plus explicitly identified design recommendations.

## E05 — Agent handoffs can propagate untrusted instructions
- Claim: adding another agent does not make inherited text authoritative; attacks can travel through agent-to-agent messages.
- Primary: Lee and Tiwari, *Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems*, arXiv 2410.07283v1 (9 Oct 2024), https://arxiv.org/abs/2410.07283 , abstract and Fig2. B lec14 pp32–35.
- Setup: constructed multi-agent applications and simulations. Main uses an illustrative two-agent arrow diagram, no rates.
- Does not establish: deployment-wide spread, real victims, or an attack on Albert.
- Label: published result (preprint; simulated/constructed setting).

## E06 — The GitHub incident is a research demonstration
- Claim: a malicious public issue caused a broadly authorized agent to disclose private-repository information in a public pull request.
- Primary: Invariant Labs, 26 May 2025, https://invariantlabs.ai/blog/mcp-github-vulnerability , “Attack Setup”, “Attack Demonstration”, “Mitigations”. B lec13 pp27–28 (S23/S24).
- Setup: authors' demo account; Claude Desktop/Claude 4 Opus, GitHub integration, one user's public/private repos. Default per-call confirmations versus “Always Allow” must not be conflated.
- Does not establish: GitHub itself was breached, another user's private repo was read without permission, all MCP systems leak, or current patch status. Date and “research demonstration” remain visible.
- Label: published result (researcher demonstration).

## E07 — Invented legal citations had real consequences
- Claim: lawyers submitted and stood by nonexistent ChatGPT-produced authorities; the court sanctioned the lawyers/firm.
- Primary: *Mata v. Avianca*, 678 F.Supp.3d 443, S.D.N.Y., 22 Jun 2023, opinion beginning printed p448 and conclusion pp467–469. Court opinion reproduced at https://hvbba.org/wp-content/uploads/2025/09/8-PANEL-THREE-Mata-v-Avianca-Inc.pdf (PDF pp6 and20; publisher headnotes not the evidence). B lec01 p14, lec06 p6.
- Setup: a particular case and professional gatekeeping failure. No numeric sanction needed on slide.
- Does not establish: a model hallucination rate or a general rule that AI use is prohibited. The underlying injury claim's merits/dismissal are a separate issue.
- Label: published result (judicial decision).

## E08 — Air Canada's chatbot gave incorrect policy advice
- Claim: the chatbot said bereavement fares could be claimed retroactively; the tribunal found negligent misrepresentation and responsibility for website information.
- Primary: *Moffatt v. Air Canada*, 2024 BCCRT149, 14 Feb 2024, paras2–6,27–31; original decision PDF mirrored at https://longangz.com/ai/case-documents/canada-moffatt-air-canada/source-1.pdf . B lec01 p16.
- Setup: one British Columbia small-claims decision, not an international legal rule. No damages number needed.
- Does not establish: which model/architecture powered the chatbot; do not call it a proven LLM hallucination. Main lesson is that an automated answer can become a consequential customer promise.
- Label: published result (tribunal decision).

## E09 — Agreeableness can be a product failure
- Claim: OpenAI reported that its 25 Apr 2025 GPT-4o update became excessively agreeable and began rolling it back on 28 Apr.
- Primaries: https://openai.com/index/sycophancy-in-gpt-4o/ (29 Apr2025); https://openai.com/index/expanding-on-sycophancy/ (2 May2025), opening and “What went wrong in training the April 25th model update”. B lec07 pp26–27.
- Setup: vendor's retrospective account of a deployed update. Use one product/rollback picture, not reward training detail.
- Does not establish: every current assistant behaves this way, or an independent causal audit of the reward changes.
- Label: published result (vendor self-report).

## E10 — A target can reward the wrong behavior
- Claim: satisfying a literal scoring rule can miss the intended goal.
- Primary: Krakovna et al., DeepMind, *Specification gaming: the flip side of AI ingenuity*, 21 Apr2020, definition/Lego and CoastRunners examples, https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/ . B lec07 pp29–30.
- Setup: illustrative executive analogy: optimizing ticket-closure speed is not the same as resolving customers' problems. Clearly label invented example; no company or metric invented as a real incident.
- Does not establish: intent, consciousness, or that every rewarded system games its score.
- Label: illustrative example motivated by published cases.

## E11 — Models can reproduce training information
- Claim: Carlini et al. extracted memorized public-web text, including identifying information, from GPT-2.
- Primary: USENIX Security2021, *Extracting Training Data from Large Language Models*, https://www.usenix.org/system/files/sec21-carlini-extracting.pdf , abstract and Fig1, PDFp2 / printedp2633. B lec01 p11 and lec04 pp19–22.
- Setup: research extraction, public-web training data, not a raid on an enterprise inbox. Prefer the source's already-redacted Fig1; never expose new personal information.
- Does not establish: all prompts train all products, arbitrary records are extractable, or current assistants have the same vulnerability.
- Label: published result.

## E12 — Removing a file differs from removing learned influence
- Claim: deleting a source record or suppressing an output does not by itself establish removal of its contribution to a trained model.
- Primary: Bourtoule et al., *Machine Unlearning*, arXiv1912.03817v3 (15 Dec2020; IEEE S&P2021), https://arxiv.org/abs/1912.03817 , abstract/introduction; B lec05 pp8–16,48–61.
- Setup: a model trained using the data. Main picture distinguishes training from a lookup/search index; notes distinguish file/index/log/backup deletion and model influence.
- Does not establish: every email supplied to an agent was used for training, deletion is impossible, or a legal compliance conclusion.
- Label: published result, conceptual adaptation.

## E13 — Predicting cost is not the same as identifying need
- Claim: in the studied healthcare allocation algorithm, Black patients at a given score had greater illness burden; cost was an inadequate proxy for health need.
- Primary: Obermeyer, Powers, Vogeli and Mullainathan, Science366 (2019), pp447–453, Figs1/3 and discussion; https://www.ftc.gov/system/files/documents/public_events/1548288/privacycon-2020-ziad_obermeyer.pdf . B lec12 pp7–8,84 (S04a/b,S54a).
- Setup: a studied US commercial allocation system; no numeric disparity needed. Use a cost→score→care allocation diagram, not dense rates.
- Does not establish: a sole cause such as avoiding bills, intentional discrimination by the algorithm, or all clinical AI being biased identically.
- Label: published result.

## E14 — Averages can hide uneven errors
- Claim: Gender Shades found markedly different error rates across intersectional groups in three commercial gender-classification systems.
- Primary: Buolamwini and Gebru, FAT*2018, https://proceedings.mlr.press/v81/buolamwini18a.html , abstract; paper Table4. B lec12 p75 (S47) is the corrected main-deck reuse source, not lec01's compressed extrema.
- Setup: May2017 audit, 1,270-face PPB benchmark, binary gender labels as output by tested systems. A simple source-backed within-one-vendor comparison or group map; exact table values must be rechecked if plotted.
- Does not establish: identity/face-recognition accuracy, vendor training-data causes, or current product performance.
- Label: published result.

## E15 — Deepfake video accompanied a large payment fraud
- Claim: Hong Kong authorities described a Jan2024 fraud using a prerecorded fake conference; reported losses about HK$200 million.
- Primary: Hong Kong Government / Secretary for Security, “LCQ9: Combating frauds involving deepfake”, 26 Jun2024, reply(1), January-case paragraphs: https://www.info.gov.hk/gia/general/202406/26/P2024062600192p.htm . B lec01 p28/lec11 p7 nominate this case.
- Setup: official historical report. The conference was prerecorded, not an interactive live digital-twin conversation; payment instructions continued through messaging. Use HK$200m, not a newly converted amount.
- Does not establish: current recovery/investigation status. The primary does not name Arup; say “Hong Kong company” unless a separate company confirmation is verified. No authentic-call footage has been obtained; any reenactment is labelled schematic.
- Label: published result (official incident report).

## E16 — Provenance and truth answer different questions
- Claim: content credentials can document origin/history; they cannot alone establish whether a depicted event or claim is true. Missing credentials do not prove fakery.
- Primary: C2PA Explainer v2.2, https://spec.c2pa.org/specifications/specifications/2.2/explainer/Explainer.html , §§7.1.2,7.2.1–7.2.3. B lec11 pp11,58–64,71.
- Setup: version-pinned standards explanation, not a current support/adoption claim. Main uses origin-history vs factual-verification paths; no cryptography/watermark mechanism.
- Does not establish: full edit history always survives, a detector is a verdict, or an authentic source always tells the truth.
- Label: published result (technical specification/explainer).

## E17 — Physical manipulation can fool a classifier in experiments
- Claim: specially designed stop-sign perturbations fooled tested road-sign classifiers in physical-world experiments.
- Primary: Eykholt et al., CVPR2018 / arXiv1707.08945v5, https://arxiv.org/abs/1707.08945 , Fig1 and lab/drive-by tests. B lec01 p19, lec08 pp85–90; existing `COURSE/figs/eykholt-stopsign.png` is the reuse candidate.
- Setup: controlled classifier tests, not a deployed autonomous car crash; no attack success percentages required.
- Does not establish: ordinary stickers defeat every car, a road deployment attack, or actual casualties.
- Label: published result.

## E18 — Attacks can enter during learning or while reading
- Claim: malicious training modifications and instructions in retrieved content act at different stages; a hidden learned trigger is not the same thing as prompt injection.
- Primary for backdoors: Gu, Dolan-Gavitt and Garg, *BadNets*, arXiv1708.06733v2, https://arxiv.org/abs/1708.06733 , abstract/introduction and traffic-sign example. Prompt-injection side: E04/E06. B lec09 pp13–14,34–47 and lec13 pp7–9.
- Setup: two labelled conceptual pathways, not an attack procedure; no numerical claims or copied payload.
- Does not establish: every suspicious source is training data, every retrieval error is poisoning, or a current deployed backdoor.
- Label: published result, conceptual comparison.

## E19 — Selection and verification decisions
- Selected public cases: E07/E08/E09/E13/E15 are real decisions, deployed-product self-report or actual incident reporting. E06/E11/E14/E17 are explicitly research demonstrations/audits. Do not market the latter as real victims.
- EchoLeak was read in current lec01/lec13; not selected for this draft because primary research page was inaccessible in this pass and MSRC web extraction was JavaScript-only. Its conceptual lesson is already covered by Albert's email story and E06, so no need to import an unverified patch/victim-status claim.
- The court/tribunal originals were read in rehosted primary-document PDFs; notes should identify that status, not cite a blog paraphrase as the judgment.
- Current lecture1 legal timelines, counts, autonomous incident and schematic trend lines are deliberately not promoted into current empirical facts. No attempt to survey current regulation.
- Label: unresolved for omitted unverified claims; selection record only, not slide content.

## E20 — Exact subgroup values for the planned Gender Shades exhibit
- Claim: in the historical IBM result, error differed substantially across the four audited groups; the overall rate concealed that variation.
- Primary/version/locator: Buolamwini and Gebru, FAT*2018, https://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf , PDFp9, Table4, IBM Error Rate row. Reopened and checked 2026-11-26. IBM overall12.1%; darker female34.7%, darker male12.0%, lighter female7.1%, lighter male0.3%. These are already error rates, not FPR values or numbers converted from a different table.
- Setup: same IBM system and full PPB benchmark, 1,270 faces; historical gender classification with binary labels, not identity recognition. Darker = Fitzpatrick IV–VI, lighter = I–III. Do not mix in Table5's South African subset. Prefer four simple bars without adding an overall-average comparison to the slide; overall12.1% can live in the note.
- Does not establish: current product performance, the cause of the gap, or population-wide prevalence.
- Label: published result. No new experiment or calculation. If slides generates a chart asset, provide its source inputs and regeneration-code path in work-r1; slides-review will append that provenance before approval. An inline chart may instead identify its exact reproducible source location.

## E21 — S25 chart provenance, independently checked in round1
- Claim/source: E20's IBM Table4 error rates, rechecked against the original PMLR PDF on 2026-11-26. All four values and the note-only overall12.1% agree.
- Reproduction: `talks/261202YonseifutureAI/261202YonseifutureAI.html`, S25 (lines916–927 at 731bec116bf1e2b9c8e696f89798aa0b1c6b0178), contains the source-input comment and inline chart. Inputs in order: 34.7,12.0,7.1,0.3 percent. Shared zero, axis0–40%,15px per percentage point; widths520.5,180,106.5,4.5px. The HTML is the regeneration source; no separate generated chart or script. Citation explicitly says redrawn.
- Setup/limits: same historical system/test, not a current ranking or new experiment; source grouping/limits remain E20. No new empirical calculation.
- Label: published result, faithful redrawing.

## E22 — S22 Fig1 provenance and consent limit
- Claim/source: Carlini et al., USENIX Security2021, https://www.usenix.org/system/files/sec21-carlini-extracting.pdf , Fig1, PDFp2/printedp2633, as in E11.
- Reproduction: `talks/261202YonseifutureAI/figs/p5-carlini-fig1.png`; capture PDFp2 at200dpi with pdftoppm crop x925,y700,width595,height570. Independent recapture is byte-identical, SHA256 `65acae932356cc37607508707cf9ebedc2247b6121b978d4e9bd0097efcfce4e`. Caption removed, figure/redactions unchanged; full top and Fax line retained. Compared source image and rendered slide.
- Limits: the study demonstrates extraction of identifying public-web training text. It does not establish the depicted person's individual consent history. Do not turn the general privacy concern into a factual claim that this person never consented.
- Label: published result; reproduction verified2026-11-26.

## E23 — S30 Fig1 provenance and experiment scope
- Source: Eykholt et al., CVPR2018, https://arxiv.org/pdf/1707.08945v5 , Fig1/caption and introduction on PDFp2; §4.2 experimental design.
- Asset: `talks/261202YonseifutureAI/figs/p3-eykholt-fig1.png` is byte-identical to baseline-course `courses/trustworthy-ai/figs/eykholt-fig1-stopsign.png`, SHA256 `8e2de05eb9685e4db526a914b5d344d8dcd5c43060af16a4b846689d8cece8d1`. Compared with source PDFp2: left ordinary real graffiti; right designed physical perturbation. Slide adds panel labels; caption cropped. No data repainting.
- Experiment: lab and drive-by camera tests of classifiers, including capture from a moving vehicle; not an autonomous-car crash report. Introduction explicitly gives Speed Limit45 as a targeted wrong class, but that label need not be added to the executive slide.
- Limits: no deployed-car safety conclusion or independently established statement about injuries. Keep the positive description of what was tested, rather than claiming there was no car on a road.
- Label: published result; figure/scope verified2026-11-26.

## E24 — Content credentials need not identify a human creator
- Clarifies E16. Primary/version/locator: C2PA Explainer v2.2, https://spec.c2pa.org/specifications/specifications/2.2/explainer/Explainer.html , §2 and §§7.2.1–7.2.5, especially §7.2.4 “Does provenance have to include the identity of the creator of a piece of media?”. Checked2026-11-26.
- Claim: credentials can carry recorded origin/edit assertions; human or organizational identity is not inherent in the core specification, though extensions can add identity information. History may be incomplete. Verification of a record does not independently establish the truth of its assertions or the depicted event.
- Setup/limits: same pinned explanatory standard as E16, not a claim about current adoption. Do not promise that any credential tells the viewer who made the file or provides its complete history. No technical mechanism needs to enter the talk.
- Label: published result (standards explainer).
