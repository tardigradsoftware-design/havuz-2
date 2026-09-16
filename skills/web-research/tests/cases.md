# Test cases — `web-research`

Every clause below is derived from this skill's own body text. Nothing here is a
generic control that would read the same for a different skill:

| Case kind | Derived from | What it asserts |
|---|---|---|
| Applies | Purpose, Workflow step titles, Quality Checklist items | the named checklist conditions hold and the named steps ran |
| Declines | each `When NOT to Use` exclusion | the exclusion is honoured and the alternative it names is used |
| Detects | each `Failure Modes` entry, with its own detection signal and response | the failure is caught by that signal and answered by that response |
| Avoids | each `Anti-Patterns` entry, with the consequence it states | the anti-pattern is absent for the reason this skill gives |

Quoted text is the skill's own wording. A case whose quoted material could be
lifted from another skill is a defect and should be reported, not relaxed.

Regenerate: `python3 scripts/generate-index/generate_skill_tests.py`
Measure distinctness: `python3 scripts/generate-index/generate_skill_tests.py --report`

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):


## Case 1 — Applies to the task it was written for

```text
GIVEN    A task inside this skill's stated purpose: Answer a question with an **evidence set**, not with an impression. The unit of output is a ranked, dated, cited claim list with explicit confidence and an explicit statement of what remains unknown.
WHEN     the agent executes `web-research` end to end on that task
THEN     and before delivery these specific conditions hold: "Question framed to a checkable answer"; "Every citation has URL + publisher + page date + verified_at"; "Output would let someone else re-run the search and reach the same conclusion"
FAIL IF  "Question framed to a checkable answer" is false, or "Output would let someone else re-run the search and reach the same conclusion" is false, or "Every citation has URL + publisher + page date + verified_at" is false
```

## Case 2 — Declines: Questions answerable from the repository itself — read the code first

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Questions answerable from the repository itself — read the code first
WHEN     the agent considers `web-research` for that task
THEN     the skill is not selected, because this task is the excluded case "Questions answerable from the repository itself — read the code first", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Questions answerable from the repository itself — read the code first"; or `web-research` is declined without naming that exclusion
```

## Case 3 — Declines: Questions answerable from this knowledge base — check indexes/topics.md first

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Questions answerable from this knowledge base — check indexes/topics.md first
WHEN     the agent considers `web-research` for that task
THEN     the skill is not selected, because this task is the excluded case "Questions answerable from this knowledge base — check indexes/topics.md first", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Questions answerable from this knowledge base — check indexes/topics.md first"; or `web-research` is declined without naming that exclusion
```

## Case 4 — Declines: Opinion questions dressed as fact questions ("what's the best framework?") —…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Opinion questions dressed as fact questions ("what's the best framework?") — use competitive-analysis and answer with tradeoffs, not a verdict
WHEN     the agent considers `web-research` for that task
THEN     the skill is not selected, because this task is the excluded case "Opinion questions dressed as fact questions ("what's the best framework?") — use competitive-analysis and answer with tradeoffs, not a verdict", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Opinion questions dressed as fact questions ("what's the best framework?") — use competitive-analysis and answer with tradeoffs, not a verdict"; or `web-research` is declined without naming that exclusion
```

## Case 5 — Declines: Anything requiring authenticated access you do not have

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Anything requiring authenticated access you do not have
WHEN     the agent considers `web-research` for that task
THEN     the skill is not selected, because this task is the excluded case "Anything requiring authenticated access you do not have", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Anything requiring authenticated access you do not have"; or `web-research` is declined without naming that exclusion
```

## Case 6 — Detects: FIRST-RESULT BIAS

```text
GIVEN    A run of this skill in which the known failure mode is present: FIRST-RESULT BIAS
WHEN     the agent executes `web-research` and reaches the point where this failure occurs
THEN     "FIRST-RESULT BIAS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "The top hit becomes the answer. Fix: ≥3 opened sources, ≥2 independent."
FAIL IF  "FIRST-RESULT BIAS" appears in the work and is reported as complete — specifically "The top hit becomes the answer. Fix: ≥3 opened sources, ≥2 independent."
```

## Case 7 — Detects: ENGAGEMENT RANKING

```text
GIVEN    A run of this skill in which the known failure mode is present: ENGAGEMENT RANKING
WHEN     the agent executes `web-research` and reaches the point where this failure occurs
THEN     "ENGAGEMENT RANKING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Assuming search order reflects correctness. Fix: rank by precedence yourself."
FAIL IF  "ENGAGEMENT RANKING" appears in the work and is reported as complete — specifically "Assuming search order reflects correctness. Fix: rank by precedence yourself."
```

## Case 8 — Detects: UNDATED DOCS

```text
GIVEN    A run of this skill in which the known failure mode is present: UNDATED DOCS
WHEN     the agent executes `web-research` and reaches the point where this failure occurs
THEN     "UNDATED DOCS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Reading v4 docs while installing v6. Fix: record the doc's version."
FAIL IF  "UNDATED DOCS" appears in the work and is reported as complete — specifically "Reading v4 docs while installing v6. Fix: record the doc's version."
```

## Case 9 — Detects: ECHO CHAMBER

```text
GIVEN    A run of this skill in which the known failure mode is present: ECHO CHAMBER
WHEN     the agent executes `web-research` and reaches the point where this failure occurs
THEN     "ECHO CHAMBER" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Three blogs restating one changelog counted as three sources."
FAIL IF  "ECHO CHAMBER" appears in the work and is reported as complete — specifically "Three blogs restating one changelog counted as three sources."
```

## Case 10 — Detects: SNIPPET RESEARCH

```text
GIVEN    A run of this skill in which the known failure mode is present: SNIPPET RESEARCH
WHEN     the agent executes `web-research` and reaches the point where this failure occurs
THEN     "SNIPPET RESEARCH" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Answering from the search snippet without opening the page."
FAIL IF  "SNIPPET RESEARCH" appears in the work and is reported as complete — specifically "Answering from the search snippet without opening the page."
```

## Case 11 — Detects: INFINITE RESEARCH

```text
GIVEN    A run of this skill in which the known failure mode is present: INFINITE RESEARCH
WHEN     the agent executes `web-research` and reaches the point where this failure occurs
THEN     "INFINITE RESEARCH" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "No budget, no stopping rule. Fix: declare budget in FRAME."
FAIL IF  "INFINITE RESEARCH" appears in the work and is reported as complete — specifically "No budget, no stopping rule. Fix: declare budget in FRAME."
```

## Case 12 — Detects: HALLUCINATED URL

```text
GIVEN    A run of this skill in which the known failure mode is present: HALLUCINATED URL
WHEN     the agent executes `web-research` and reaches the point where this failure occurs
THEN     "HALLUCINATED URL" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Citing a plausible-looking URL that was never fetched. Fix: never write a URL you did not open; the validator greps for this."
FAIL IF  "HALLUCINATED URL" appears in the work and is reported as complete — specifically "Citing a plausible-looking URL that was never fetched. Fix: never write a URL you did not open; the validator greps for this."
```

## Case 13 — Detects: SILENT UNCERTAINTY

```text
GIVEN    A run of this skill in which the known failure mode is present: SILENT UNCERTAINTY
WHEN     the agent executes `web-research` and reaches the point where this failure occurs
THEN     "SILENT UNCERTAINTY" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Presenting medium-confidence findings as settled."
FAIL IF  "SILENT UNCERTAINTY" appears in the work and is reported as complete — specifically "Presenting medium-confidence findings as settled."
```

## Case 14 — Avoids: Citing a URL that was never fetched

```text
GIVEN    A situation that invites the anti-pattern "Citing a URL that was never fetched"
WHEN     the agent applies `web-research` in that situation
THEN     "Citing a URL that was never fetched" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Citing a URL that was never fetched" appears in the output; or it is absent by accident, with nothing in `web-research` having ruled it out
```

## Case 15 — Avoids: "According to the documentation" with no link and no version

```text
GIVEN    A situation that invites the anti-pattern "According to the documentation" with no link and no version"
WHEN     the agent applies `web-research` in that situation
THEN     "According to the documentation" with no link and no version" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "According to the documentation" with no link and no version" appears in the output; or it is absent by accident, with nothing in `web-research` having ruled it out
```

## Case 16 — Avoids: Treating an AI-written medium.com post as a primary source

```text
GIVEN    A situation that invites the anti-pattern "Treating an AI-written medium.com post as a primary source"
WHEN     the agent applies `web-research` in that situation
THEN     "Treating an AI-written medium.com post as a primary source" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Treating an AI-written medium.com post as a primary source" appears in the output; or it is absent by accident, with nothing in `web-research` having ruled it out
```

## Case 17 — Avoids: Answering "what's best" with a single product name

```text
GIVEN    A situation that invites the anti-pattern "Answering "what's best" with a single product name"
WHEN     the agent applies `web-research` in that situation
THEN     "Answering "what's best" with a single product name" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Answering "what's best" with a single product name" appears in the output; or it is absent by accident, with nothing in `web-research` having ruled it out
```

## Case 18 — Avoids: Ignoring the CHANGELOG when the question is about a behaviour change

```text
GIVEN    A situation that invites the anti-pattern "Ignoring the CHANGELOG when the question is about a behaviour change"
WHEN     the agent applies `web-research` in that situation
THEN     "Ignoring the CHANGELOG when the question is about a behaviour change" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Ignoring the CHANGELOG when the question is about a behaviour change" appears in the output; or it is absent by accident, with nothing in `web-research` having ruled it out
```

## Case 19 — Avoids: Stopping at the first source that agrees with the initial hypothesis

```text
GIVEN    A situation that invites the anti-pattern "Stopping at the first source that agrees with the initial hypothesis"
WHEN     the agent applies `web-research` in that situation
THEN     "Stopping at the first source that agrees with the initial hypothesis" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Stopping at the first source that agrees with the initial hypothesis" appears in the output; or it is absent by accident, with nothing in `web-research` having ruled it out
```
