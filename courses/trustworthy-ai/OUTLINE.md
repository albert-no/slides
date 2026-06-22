# trustworthy-ai/ — Trustworthy AI course

General-audience graduate course (15 weeks × 1.5 hr). Students come from mixed
bachelor backgrounds, many non-engineering, with basic Python/Colab experience.
**Mode:** concepts + intuition first, light technical detail, minimal proofs.
Each lecture: a **formal definition → short history → 2025–26 frontier**, plus an
optional **Colab demo** students can run themselves (no homework, nothing to submit).

All lecture decks live flat in this folder (`lecNN-*.html`). Arc climbs the
**trust stack**: data → model → output → society. Real paper figures (cropped +
cited) live in `figs/`; `bundle.py` inlines them. Concept diagrams are inline SVG.

## Modules

| Module | Weeks | Theme |
|---|---|---|
| 0. Foundations | 1 | What "trustworthy" means, threat-model thinking |
| 1. Privacy & Data | 2–5 | What models leak about their training data |
| 2. Reliability | 6–7 | Can you believe the answer, and see why |
| 3. Security | 8–11 | How models are attacked, train- and inference-time |
| 4. Provenance & Fairness | 12–14 | Watermarking, fairness, accountability |
| 5. Synthesis | 15 | Governance, frontier, demo showcase |

## Lecture index

| Wk | File | Topic | Status |
|---|---|---|---|
| 1 | `lec01-introduction.html` | Introduction & threat-model thinking | **drafted** (47 sl) |
| 2 | `lec02-privacy-dp.html` | Privacy & differential privacy | **drafted** (93 sl) |
| 3 | `lec03-mia.html` | Membership inference attacks | **drafted** (59 sl) |
| 4 | `lec04-memorization.html` | Memorization & training-data extraction | **drafted** (59 sl) |
| 5 | `lec05-unlearning.html` | Machine unlearning | **drafted** (58 sl) |
| 6 | `lec06-hallucination.html` | Hallucination, calibration & reliability | **drafted** (58 sl) |
| 7 | `lec07-interpretability.html` | Interpretability & explainability | **drafted** (57 sl) |
| 8 | `lec08-adversarial.html` | Adversarial examples (attack + defense) | **drafted** (56 sl) |
| 9 | `lec09-poisoning.html` | Data poisoning & backdoors | **drafted** (55 sl) |
| 10 | `lec10-jailbreak.html` | Jailbreaks & LLM safety | **drafted** (54 sl) |
| 11 | `lec11-prompt-injection.html` | Prompt injection & agentic safety | **drafted** (58 sl) |
| 12 | `lec12-watermark.html` | Watermarking, deepfakes & provenance | **drafted** (55 sl) |
| 13 | `lec13-fairness-defs.html` | Fairness I — definitions & impossibility | **drafted** (54 sl) |
| 14 | `lec14-fairness-mitigation.html` | Fairness II — mitigation & accountability | **drafted** (54 sl) |
| 15 | `lec15-governance.html` | Governance, frontier & demo showcase | **drafted** (53 sl) |

Every deck has a companion **speaker script** `lecNN-…-note.html` (one entry per slide:
title + 1–2 sentence script + **Key takeaway**). Scripts also exist for lec 1–2.

## Backup / swap-in materials (not in the 15-week core)

Optional decks for substitution or extra sessions. Each has a `-note.html` script.

| File | Topic | Slots in where | Status |
|---|---|---|---|
| `backup-sycophancy.html` | Sycophancy, manipulation & persuasion | merge into Wk 6, or standalone | **drafted** (38 sl) |
| `backup-copyright.html` | Copyright, consent & data provenance | pairs with Wk 4 (memorization) | **drafted** (45 sl) |
| `backup-agentic-autonomy.html` | Agentic autonomy risks beyond injection | expands Wk 11 | **drafted** (47 sl) |
| `backup-model-stealing.html` | Model stealing / extraction attacks | swap for Wk 9, or standalone | **drafted** (51 sl) |

**Draft note:** lec 3–15 + backups were generated in one parallel pass (each ~50–60
slides, lint-clean, with SVG concept diagrams + cited papers and `<!-- TODO real
figure -->` markers where a paper figure would strengthen a slide). They have NOT yet
had the per-slide screenshot audit or real-image pass that lec 1–2 received — treat as
solid first drafts to review and expand.

## Cross-folder reuse

This course is the **light, general-audience** pass over topics treated rigorously
elsewhere. Reuse / differentiate against:

- **DP** (Wk 2) ↔ `courses/privacy/lectures/01-dp/` (8-deck rigorous series). Lec 2
  is intuition-only; it points students to the privacy course for the formal treatment.
- **MIA** (Wk 3) ↔ `courses/privacy/lectures/04-mia/` (5 lectures + notes).
- **Memorization** (Wk 4) ↔ `courses/privacy/lectures/03-memorization/`.
- **Unlearning** (Wk 5) ↔ `courses/privacy/lectures/05-unlearning/` and the ICML
  position talk `talks/icml2026/`.
- **Watermark** (Wk 12) ↔ `courses/privacy/lectures/06-watermark/`.

When drafting a stub, read the corresponding leaf `OUTLINE.md` there first and
**compress, don't re-derive** — link back rather than restating proofs.

---

## lec01-introduction.html

**Topic:** What "trustworthy" means; AI fails differently than software; the five
trust dimensions; threat-model thinking (knowledge × timing); the 15-week map; how
demos work. Sets the vocabulary used all term.

### Sections (47 slides, ~35–40 min)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:27`, `:39` | |
| **01 — Why Trust?** | 3–12 | `:69` | Bias/COMPAS `:91` · Amazon · Mata v. Avianca · chatbots · memorization · deepfakes · prompt injection |
| **02 — How AI Fails Differently** | 13–21 | `:206` | SW vs learned · failure in weights · **panda→gibbon image** `:244` · three sources · black box · **six trust dimensions** `:296` |
| **03 — Threat-Model Thinking** | 22–31 | `:325` | **What is a threat model (+adversary SVG)** `:333` · house analogy · white/black-box · train/inference · **attack map 2×2 (SVG)** `:425` · medical-LLM worked example |
| **04 — Trust Stack & Course Map** | 32–41 | `:491` | **trust stack (layered SVG)** `:499` · **4-module 15-week timeline (SVG)** `:523` · module previews · week-by-week · 2025–26 themes |
| **05 — How We'll Work** | 42–46 | `:639` | concepts not proofs · hands-on demos · the goal |
| Closer | 47 | — | |

**Visuals:** real image — panda→gibbon adversarial example (`figs/panda-gibbon.png`,
Goodfellow et al. 2015) `:244`. SVG — adversary↔system threat diagram `:333`,
attack-map 2×2 `:425`, layered trust-stack `:499`, 15-week module timeline `:523`.
**Key framing:** threat model = *who* / *what they know* (white/black-box) / *what they
can do* (train/inference-time); the 2×2 locates every attack. Examples-first: real
incidents in §01 anchor the six trust dimensions. Citations use `.cite-left`. Page
number: bold `.slide-num` only.

---

## lec02-privacy-dp.html

**Topic:** Why models leak and anonymization fails; the differential-privacy idea
(presence barely changes output); the formal $(\varepsilon,\delta)$-DP definition;
the budget $\varepsilon$; randomized response; noise-by-sensitivity; DP-SGD;
privacy–utility tradeoff; federated learning; private foundation models (2025–26).
Intuition pass — points to the privacy course for rigor.

### Sections (93 slides, full 90 min)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:33`, `:45` | |
| **01 — The Privacy Problem** | 3–16 | `:78` | **GPT-2 extraction image** `:112` · Secret Sharer · "repeat poem" · **diffusion copy image (Ann)** `:158` · 3 kinds of leak · **Sweeney 87% Venn (SVG)** `:224` · Netflix de-anon `:245` |
| **02 — How Leakage Is Measured** | 17–29 | `:271` | membership inference · **MIA loss-overlap (SVG)** · shadow models (Shokri) · model inversion · **extraction-scales duplication image** `:362` · deep leakage · NYT v. OpenAI · Italy ban |
| **03 — Differential Privacy** | 30–52 | `:442` | two-worlds · **$(\varepsilon,\delta)$-DP definition** `:527` · budget $\varepsilon$ · post-processing · **statistical indistinguishability + heights (SVG)** `:637-` · what DP does/doesn't |
| **04 — Achieving DP: Add Randomness** | 53–65 | `:731` | **Randomized response + coin-tree (SVG)** `:765` · recover-the-rate worked example · local vs central DP · RAPPOR/Apple · **Laplace mechanism + noise bell (SVG)** `:844` · sensitivity |
| **05 — Private Machine Learning** | 66–79 | `:905` | **DP-SGD** (clip+noise) · privacy accountant · utility cost · **federated learning (SVG)** · Gboard · deep leakage · secure aggregation |
| **06 — Frontier 2025–26** | 80–89 | `:1087` | private fine-tuning (Yu, Li 2022) · private synthetic data · web-scale puzzle · privacy auditing · unlearning preview · Apple PCC · EU AI Act |
| Wrap (deeper / demos / takeaways) | 90–92 | — | "see also" privacy course |
| Closer | 93 | — | `$\varepsilon$` |

**Key definitions / citations:**
- $(\varepsilon,\delta)$-DP — `:497` — Dwork, McSherry, Nissim, Smith, TCC 2006.
- **Statistical indistinguishability** (heights example, Korea/Japan Gaussians) — `:607-651` — replaced the composition slides per design choice; the "many samples break it" slide folds in the composition intuition (repeated queries erode privacy).
- Randomized response — `:722` — Warner, JASA 1965.
- DP-SGD — `:877` — Abadi et al., ACM CCS 2016.
- De-anonymization — `:222` — Narayanan & Shmatikov, IEEE S&P 2008.

**Real images** (`figs/`, cropped + cited per GOTCHAS): GPT-2 extraction `figs/gpt2-extraction.png`
(Carlini et al. 2021, Fig 1) `:112`; Stable-Diffusion copy `figs/calrini-ann.png` (Carlini et al.
2023 / Somepalli et al. 2023) `:158`; duplication histogram `figs/carlini_duplicates.png` (Carlini
et al. 2023, Fig 5) `:362`. **SVG figures:** Sweeney linkage Venn `:224`, MIA loss-overlap,
height-distribution overlap, randomized-response coin tree `:765`, Laplace noise bell `:844`,
federated learning. Citations use `.cite-left`. Page number: bold `.slide-num` only.
**Forward refs:** extraction (Wk 4), MIA (Wk 3), unlearning (Wk 5). Intuition pass —
points to `courses/privacy/lectures/01-dp/` for rigor.
