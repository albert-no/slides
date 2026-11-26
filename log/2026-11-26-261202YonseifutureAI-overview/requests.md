# Requests (append-only)

Source: Albert No, #claw-slides-review, message 12, 2026-11-26 14:44 Asia/Seoul. Each block is verbatim; segmentation only.

## C01
> I will be giving a talk to general audience about trustworthy AI.

## C02
> Create 261202YonseifutureAI folder in talks.

## C03
> Create a slide deck and note html files.

## C04
> Check the contents of trustworthy AI course and generate slides deck for 45minutes (40-50 slides)

## C05
> The slide deck should mainly rely on the very first overview lecture but should drop all technical details.

## C06
> And also check the lec02 to lec14 since I updated the slide deck a lot during the semester.

## C07
> I want extremely high level overview.

## C08
> The audience is CEO-level seniors so they may want the concept and idea instead of technical details.

## C09
> In that sense, drop all the detailed explanations, use diagrams but no explanations (you can add main message in text but use text descriptions sparingly).

## C10
> Add more real-world examples.

## C11
> In the beginning of the talk, I want to start from introducing how I use agents.

## C12
> One of my main usage is build automatic manual (private webpage for me) based on email

## C13
> I am a Vice Dean of Graduate school of computing (부원장/인융대학원) and have a lot of paper works. A lot of them are seasonal (once in a semester or so) and I often forgot how I did it last time. So I build automatic manual

## C14
> I let agent to read my email related to graduate school of computing, and record how I did the paperwork. Update manual weekly.

## C15
> In order to do so, the agent may have to read my email, then it runs LLM. It is vulnerable to so-called prompt injection attack (briefly introduce prompt injection here). If one agent can read and write a code (GitHub) then it is not safe.

## C16
> And I have separate agents: one who can only read my email (not write) summarize the contents, then I approve it manually so that the coding agent write a code to build a manual.

## C17
> We can discuss more about prompt injection in detail in later slides.I think this is perfect motivational example, then move on to the regular flow of the talk (LLM becomes more powerful, and the actual risk is getting higher, etc).

## C18
Source: Albert No, #claw-slides-review, message 14, 2026-11-26 14:57 Asia/Seoul.

> sounds good go ahead

Decision: approves the preceding stages 1–3 scope, evidence/case direction, 46-slide title arc and 45-minute allocation; authorizes build after stage-4 specification. Not a merge order.

## C19
Same source as C18.

> english please

Decision: English main deck and English companion notes; supersedes the proposed Korean language in plan-v1.


## C20
Source: Albert No, #claw-slides-review, message 22, 2026-11-26 22:50 Asia/Seoul. Page numbers refer to the 46-page PR82 head `753041e2bfe1ed77592613cd4ff73ff615810176` (deck content approved at `07f519cec547faa37cba901c8f5f0da07125360d`).

> page 7 code repository (Github) → Private webpage

## C21
Same source as C20.

> what is page 20 about? make the point much clearer

## C22
Same source as C20.

> what is page 21 about? make the point much clearer

## C23
Same source as C20.

> Github is too technical. I like Reddit example (including page 33)

## C24
Same source as C20.

> drop page 27

Decision: these five comments authorize the targeted plan-v3 revision on the existing PR82 branch, not a new deck or a merge. Interpret the Reddit example as the Comet/Reddit demonstration already in updated course lec13, pp29–30 (stable S25/S26 there); replace the GitHub teaching case rather than merely renaming its platform. No conflict between comments: C20 changes the private destination in Albert's illustration, while C23 changes the independent research example.
