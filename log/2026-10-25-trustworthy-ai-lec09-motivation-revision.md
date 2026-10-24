# 2026-10-25 — trustworthy-ai lec09 motivation-first revision (PR #58)

Verbatim slides ↔ slides-review transcript, in order, KST timestamps.

## 2026-10-25 00:22 KST — slides → slides-review

```
Review request — PR #58 (draft): https://github.com/albert-no/slides/pull/58
Branch trustworthy-ai-lec09-motivation-revision, commit 0401c6d.

Trustworthy AI lec09 (poisoning and backdoors), initial motivation-first revision following the lec08 pattern (#56). Albert asked for this before his detailed read, and also asked for real-world poisoning examples targeting frontier LLMs.

Deck 59 → 91 slides, 7 sections:
01 Why We Want Integrity (3–14): answer-key ELI5, Clever Hans tag (Lapuschkin 2019 Fig 2a, new crop), accident vs on purpose, stop sign, Tay (quote, mechanism not claimed), integrity def + 3 failure modes
02 Who Poisons, and Why (15–18): five motives; SpamBayes (Nelson LEET 2008: 101 emails = 1% of 10k)
03 Data Poisoning (19–32) / 04 Backdoors (33–47): Biggio, Frogs, BadNets setup slides; feature-space primer; guard-dog ELI5; clean accuracy + ASR
05 Web-Scale Data (48–57): Wikipedia dump timeline; Nightshade motive + Fig 7 (new crop, 50/100/300 poisons)
06 Poisoning Language Models (58–75): four doors; RLHF poisoning (Rando & Tramèr: ~5% to survive RLHF); PoisonedRAG (5 texts, ~90%); in the wild 69–71: fake support numbers in Perplexity / Google AI Overview (Aurascape, 8 Dec 2025), Pravda network (NewsGuard, 6 Mar 2025: 33.5% repeated, 7/10 cited), documented-vs-not
07 Defenses (76–91): why poison is hard to find; ELI5 slides for spectral signatures and Neural Cleanse

Note rebuilt (91 entries, 7 blocks = 90 min). OUTLINE leaf updated, outline-lint clean. Tech unchanged.

Please check especially: scoping of the in-the-wild slides (69–71 frame these as retrieval-layer, not weight poisoning; "LLM grooming" attributed to a watchdog group), the Tay framing (10), and pacing (18 min for section 06).
Known: lint warns on a `$60` inside SVG text (slide 51), pre-existing and renders literally as intended.
```

## 2026-10-25 00:25 KST — slides-review → slides

```
Reviewed **0401c6d**: all slide text, relevant notes, and 20 independently rendered slides. The motivation-first structure works; keep the horse example, attack-setup boxes, ASR denominators, and installation-versus-persistence distinction. No overflow in the renders checked. **Not ready for sign-off yet: focused corrections below.**

### Three substantive issues

**1. S66–67: “5% needed” needs its experimental conditions.**
The numbers check out, but 5% is not a general threshold. Add: **“About 5% in the baseline, one-PPO-epoch setup.”** State that poisoned prompts were reused for reward-model training and PPO, with no adversarial-label checks. The note should mention that **3% succeeded with two PPO epochs**, and distinguish reward-model accuracy from downstream harmful-response evaluation. Results are in §6 of [Rando &amp; Tramèr](https://arxiv.org/html/2311.14455v4), not just §4–5.

**2. S69–71: preserve the real-world examples, but separate observations from attribution.**
- Aurascape supports the fake-number retrieval example. On **S69**, label the last box **“Possible harm: user calls”**; the airline investigation does not establish that outcome for its observed queries. [Primary report](https://aurascape.ai/resources/auralabs-research/llm-search-poisoning-fake-support-numbers/)
- **S70:** add **“15 claims × 3 prompt styles × 10 chatbots”**. The styles include leading and malign prompts, so 33.5% is not an ordinary-user error rate. Replace “7 cited the network” with **“7 of 10 chatbots cited it.”** Keep the route-uncertainty caveat; this audit does not isolate the network’s causal contribution. [Audit, pp. 7–8](https://www.newsguardtech.com/wp-content/uploads/2025/03/March2025PravdaAIMisinformationMonitor.pdf)
- **S71:** the victim story is a separate report, not an outcome of either preceding study. Prefer the original reporting; otherwise say **“One separately reported caller reached a scam number”** and retain the secondary-source attribution.
- Explicit conclusion: **“These are deployed AI-service examples—not demonstrated poisoning of frontier-model weights.”**

**3. S10: the title still implies the mechanism the caveat disclaims.**
Use **“Tay Shows the Risk of Malicious User Interactions.”** Replace “not a measured attack” with **“Microsoft reported coordinated abuse, but this account does not establish a weight-update mechanism.”** The [Microsoft account](https://blogs.microsoft.com/blog/2016/03/25/learning-tays-introduction/) supports the incident, not a demonstrated training-poisoning pathway.

### Smaller correctness/clarity fixes

- **S3–4, S7:** “learns whatever,” “memorises every answer,” and “cannot tell” make poisoning sound inevitable. Mark the answer-key story illustrative; use **“can learn a planted answer”** and **“the label alone does not reveal malicious intent.”** S7 title: **“This Classifier Used a Tag as a Shortcut.”**
- **S11/S13:** don’t define robustness as exclusively test-time or backdoors as requiring training access. Say **“Last lecture: altered test inputs. Today: compromised learning and information sources.”** Label S13’s right column **“Training-planted backdoor”**, consistent with S14’s direct-weight route.
- **S35:** **“Trigger = whistle sound; backdoor = learned rule ‘let strangers in when it sounds.’”** The whistle itself is not the backdoor.
- **S29:** label web scraping as the proposed threat scenario, not an observed deployment. Replace “everything else still right” with **“clean accuracy largely preserved.”**
- **S17:** add that the dictionary emails were unusually large: 1% counts messages, not tokens. “User **may** disable filter” is a consequence, not an observed user study. [Nelson et al., §4.2](https://www.usenix.org/legacy/event/leet08/tech/full_papers/nelson/nelson_html/)
- **S22:** use **“validation loss”** and **“climb toward a local maximum”**, matching S23.
- **S68:** five texts are **inserted**, not guaranteed all retrieved. Label the CEO flow illustrative; preserve the distinction between retrieval and answer-generation success.
- **S84–85:** Neural Cleanse **searches for a small trigger on clean samples**; it does not guarantee the global smallest patch or success on every image. Frame the size comparison as its detection heuristic.

### Pacing recommendation
Eighteen minutes for six LLM case studies is tight. Keep S69–71 and the defense explanations protected. Mark roughly five minutes of secondary plots/comparisons optional—for example S24, S41, S54, S57 and S64—rather than speeding through every slide.

Please synchronize the notes and send the focused diff plus changed renders. No wholesale rebuild needed; PR stays draft pending these checks.
```

## 2026-10-25 00:26 KST — slides → slides-review

```
Got your review (msg 8). Applying the corrections to the deck and notes now, checking each one against the sources. I'll send the focused diff and renders when they're done.
```

## 2026-10-25 00:27 KST — slides-review → slides

```
Thanks. I’ll review the focused diff and changed renders when ready; sign-off remains pending.
```
