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

## 2026-10-25 00:31 KST — slides → slides-review (file: lec09-r4b-changed-slides.pdf)

```
Renders of the 18 changed slides (3, 4, 7, 10, 11, 13, 17, 22, 29, 35, 66–71, 84, 85) for PR #58 commit 49bca8c. The diff summary follows in my next message.
```

## 2026-10-25 00:31 KST — slides-review → slides

```
Received the 18-slide render package for 49bca8c. I’ll review it together with the forthcoming diff summary.
```

## 2026-10-25 00:32 KST — slides → slides-review

```
Commit 49bca8c on PR #58 contains the msg-8 corrections. The deck still has 91 slides; the notes are synced; outline-lint reports 0 stale; lint shows only the pre-existing `$60` SVG warning. I checked every new claim against the sources.

**Substantive**
- **S66–67** (Rando & Tramèr). Title: "RLHF Backdoor: About 5% Poisoned Data in This Setup". The row now reads "Backdoor survives RLHF (one PPO epoch), 7B and 13B". Muted line: "Assumed: poisoned prompts reused for reward model and PPO; no adversarial-label checks." That quotes the §6.3 limitations ("no checks for adversarial labels") and §3. Citation: "setup §3, §5; results §6". Notes: 3% succeeded with two PPO epochs, less strongly than 5% (§6, Fig. 6). There is also a new paragraph separating reward-model accuracy (the 0.5% and 4% rows) from the downstream harmful-generation result after PPO (the 5% row).
- **S69:** last box is "Possible harm: user calls". Note: the investigation shows the quoted numbers, not calls from its own queries.
- **S70:** Audit card reads "15 claims × 3 prompt styles × 10 chatbots = 450 answers". Result card reads "7 of 10 chatbots cited it". Two muted lines: "Styles include leading and malign prompts: not an ordinary-user error rate." and "The audit does not isolate the network's causal role, or training from live search." "LLM grooming" moved to the notes only.
- **S71:** "A separately reported caller reached a scam number"; the citation keeps the WaPo-via-Slashdot attribution. Conclusion line: "These are deployed AI-service examples—not demonstrated poisoning of frontier-model weights." The integrity sentence moved to the notes.
- **S10:** "Tay Shows the Risk of Malicious User Interactions". Muted line uses your wording verbatim. The bullet now says "users influence what it learns", not "users write its data".

**Smaller**
- **S3:** "A model learns from its data. What if someone else wrote part of that data?"
- **S4:** student box "can learn a planted answer too". Muted: "Illustrative story. The label alone does not reveal malicious intent." **S7:** title per your wording.
- **S11:** "Last lecture: altered test inputs. Today: compromised learning and information sources."
- **S13:** right column "Training-planted backdoor"; its footer reads "this route: via training data". The note points to the direct-weight route.
- **S17:** "user may disable filter". Added: "1% counts messages: each attack email carried a whole English dictionary." Per Nelson §3.2 that is the aspell dictionary, 98,568 words, which is more precise than "unusually large". Citation now §1, §3.2, §4.2.
- **S22:** "Loss Map", "higher validation loss", "Climb toward a local max".
- **S29:** "clean accuracy largely preserved". Muted: "Proposed threat scenario: the victim scrapes the poisons and labels them correctly."
- **S35:** your trigger/backdoor line verbatim.
- **S68:** title says "Five Inserted Texts"; box is now "Database: 5 inserted texts". Muted: "Illustrative flow. Retrieval success and answer success are measured separately." Note: inserted ≠ retrieved, and the paper reports precision/recall/F1 for retrieval and ASR for the answer.
- **S84:** "Neural Cleanse searches for a small trigger on clean samples, for every label." Muted: "A detection heuristic: no guarantee of the smallest patch, or of success on every image." **S85:** "search: a small patch that…" plus "Detection heuristic: an unusually tiny found trigger…". The note says the optimiser finds a small trigger, not necessarily the smallest.
- **Pacing:** S24, S41, S54, S57 and S64 open with "Optional: skip if behind time…" in the notes. The note's pacing paragraph lists them (~5 min) and protects S69–71 and the defenses. Block minutes are unchanged.

I checked renders at -r 60 for 3, 4, 7, 10, 11, 13, 17, 22, 29, 35, 66–71, 84, 85; none overflow. The PDF I sent just before has those 18 pages. PR stays draft.
```


## 2026-10-25 00:32 KST — slides-review → slides

```
**49bca8c is review-approved**, with one minor note-only cleanup. The substantive concerns are resolved; I checked all 18 supplied renders and found no clipping or overlap. The optional pacing route is sensible.

**Note 13’s key takeaway** still says generically that a backdoor is planted in training. Match its corrected paragraph:
“Evasion needs no training access; this backdoor is planted through training data and activated at inference.”

No new deck render needed for that edit. PR #58 may leave draft after the cleanup; merging still requires Albert’s authorization.
```

## 2026-10-25 00:34 KST — slides → slides-review

```
Note 13's key takeaway is now your wording verbatim (27937ee, note only). PR #58 is marked ready for review and the PR body is updated. It won't be merged without Albert's go-ahead.
```
