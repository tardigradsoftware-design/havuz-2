# Test cases — `skill-curation`

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
GIVEN    A task inside this skill's stated purpose: Decide what enters the active corpus, at what confidence, and what must be refused. Curation is the control that keeps a growing knowledge base trustworthy: without it, volume rises while average confidence falls,
WHEN     the agent executes `skill-curation` end to end on that task
THEN     the workflow runs in its stated order — "CHECK THE EXCLUSION POLICY FIRST" through to "RECORD THE DECISION"; and before delivery these specific conditions hold: "the exclusion policy was checked before quality"; "duplication was searched for and merges were preferred over duplicates"; "derived views were regenerated, not hand-edited"
FAIL IF  "the exclusion policy was checked before quality" is false, or "derived views were regenerated, not hand-edited" is false, or the result is delivered before "RECORD THE DECISION" has run
```

## Case 2 — Declines: The content is being written for the first time.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The content is being written for the first time.
WHEN     the agent considers `skill-curation` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Author it, then curate it; self-curation of unreviewed material is a weaker control."
FAIL IF  the skill is run on a task where "The content is being written for the first time.", and the consequence that exclusion states follows — "Author it, then curate it; self-curation of unreviewed material is a weaker control."; or `skill-curation` is declined without naming that exclusion
```

## Case 3 — Declines: The question is whether a claim is true rather than whether it belongs here.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The question is whether a claim is true rather than whether it belongs here.
WHEN     the agent considers `skill-curation` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "That is evidence-validation and fact-checking."
FAIL IF  the skill is run on a task where "The question is whether a claim is true rather than whether it belongs here.", and the consequence that exclusion states follows — "That is evidence-validation and fact-checking."; or `skill-curation` is declined without naming that exclusion
```

## Case 4 — Declines: The entry is generated output with no human review.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The entry is generated output with no human review.
WHEN     the agent considers `skill-curation` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Generated content is not admitted; it is a draft."
FAIL IF  the skill is run on a task where "The entry is generated output with no human review.", and the consequence that exclusion states follows — "Generated content is not admitted; it is a draft."; or `skill-curation` is declined without naming that exclusion
```

## Case 5 — Declines: A legal question exceeds the policy: escalate rather than decide.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: A legal question exceeds the policy: escalate rather than decide.
WHEN     the agent considers `skill-curation` for that task
THEN     the skill is not selected, because this task is the excluded case "A legal question exceeds the policy: escalate rather than decide.", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "A legal question exceeds the policy: escalate rather than decide."; or `skill-curation` is declined without naming that exclusion
```

## Case 6 — Detects: Excluded content admitted

```text
GIVEN    A run of this skill in which the known failure mode is present: Excluded content admitted
WHEN     the agent executes `skill-curation` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "the policy check was skipped" — and the response applied is the documented one: "refuse and record; public reachability is not permission"
FAIL IF  "Excluded content admitted" reaches the output because "the policy check was skipped" was never checked; or it is caught but the response taken is not "refuse and record; public reachability is not permission"
```

## Case 7 — Detects: Unlicensed content vendored

```text
GIVEN    A run of this skill in which the known failure mode is present: Unlicensed content vendored
WHEN     the agent executes `skill-curation` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "license: null and a copy in the tree" — and the response applied is the documented one: "remove the copy; keep a linked summary with attribution"
FAIL IF  "Unlicensed content vendored" reaches the output because "license: null and a copy in the tree" was never checked; or it is caught but the response taken is not "remove the copy; keep a linked summary with attribution"
```

## Case 8 — Detects: Source does not support the claim

```text
GIVEN    A run of this skill in which the known failure mode is present: Source does not support the claim
WHEN     the agent executes `skill-curation` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "re-reading it does not back the statement" — and the response applied is the documented one: "re-grade or remove the claim"
FAIL IF  "Source does not support the claim" reaches the output because "re-reading it does not back the statement" was never checked; or it is caught but the response taken is not "re-grade or remove the claim"
```

## Case 9 — Detects: Unreachable source admitted as verified

```text
GIVEN    A run of this skill in which the known failure mode is present: Unreachable source admitted as verified
WHEN     the agent executes `skill-curation` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "the URL was never reached" — and the response applied is the documented one: "quarantine as UNVERIFIED with a re-grade note"
FAIL IF  "Unreachable source admitted as verified" reaches the output because "the URL was never reached" was never checked; or it is caught but the response taken is not "quarantine as UNVERIFIED with a re-grade note"
```

## Case 10 — Detects: Duplicate entries diverge

```text
GIVEN    A run of this skill in which the known failure mode is present: Duplicate entries diverge
WHEN     the agent executes `skill-curation` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "two entries, different content" — and the response applied is the documented one: "merge with an alias; keep one authoritative version"
FAIL IF  "Duplicate entries diverge" reaches the output because "two entries, different content" was never checked; or it is caught but the response taken is not "merge with an alias; keep one authoritative version"
```

## Case 11 — Detects: Conflict resolved silently

```text
GIVEN    A run of this skill in which the known failure mode is present: Conflict resolved silently
WHEN     the agent executes `skill-curation` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "the minority source disappeared" — and the response applied is the documented one: "record both with the precedence reasoning"
FAIL IF  "Conflict resolved silently" reaches the output because "the minority source disappeared" was never checked; or it is caught but the response taken is not "record both with the precedence reasoning"
```

## Case 12 — Detects: Window set from the source's prestige

```text
GIVEN    A run of this skill in which the known failure mode is present: Window set from the source's prestige
WHEN     the agent executes `skill-curation` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "a 2026 framework default given 12 months" — and the response applied is the documented one: "set the window from the claim class"
FAIL IF  "Window set from the source's prestige" reaches the output because "a 2026 framework default given 12 months" was never checked; or it is caught but the response taken is not "set the window from the claim class"
```

## Case 13 — Detects: Broken internal links

```text
GIVEN    A run of this skill in which the known failure mode is present: Broken internal links
WHEN     the agent executes `skill-curation` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "validator reports them" — and the response applied is the documented one: "fix before admitting; a broken link is a retrieval failure"
FAIL IF  "Broken internal links" reaches the output because "validator reports them" was never checked; or it is caught but the response taken is not "fix before admitting; a broken link is a retrieval failure"
```

## Case 14 — Detects: Index hand-edited

```text
GIVEN    A run of this skill in which the known failure mode is present: Index hand-edited
WHEN     the agent executes `skill-curation` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "overwritten on regeneration" — and the response applied is the documented one: "edit the data or curation file, then regenerate"
FAIL IF  "Index hand-edited" reaches the output because "overwritten on regeneration" was never checked; or it is caught but the response taken is not "edit the data or curation file, then regenerate"
```

## Case 15 — Detects: Disposition not recorded

```text
GIVEN    A run of this skill in which the known failure mode is present: Disposition not recorded
WHEN     the agent executes `skill-curation` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "nobody knows why an entry is absent" — and the response applied is the documented one: "record refusals with reasons"
FAIL IF  "Disposition not recorded" reaches the output because "nobody knows why an entry is absent" was never checked; or it is caught but the response taken is not "record refusals with reasons"
```

## Case 16 — Avoids: CURATING BY VOLUME

```text
GIVEN    A situation that invites the anti-pattern "CURATING BY VOLUME", whose stated consequence is: Admitting everything and grading nothing; average confidence falls as the corpus grows.
WHEN     the agent applies `skill-curation` in that situation
THEN     "CURATING BY VOLUME" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Admitting everything and grading nothing; average confidence falls as the corpus grows."
FAIL IF  "CURATING BY VOLUME" appears in the output — that is, "Admitting everything and grading nothing; average confidence falls as the corpus grows."; or it is absent by accident, with nothing in `skill-curation` having ruled it out
```

## Case 17 — Avoids: SKIPPING THE POLICY CHECK BECAUSE THE CONTENT IS POPULAR

```text
GIVEN    A situation that invites the anti-pattern "SKIPPING THE POLICY CHECK BECAUSE THE CONTENT IS POPULAR", whose stated consequence is: Popularity does not launder provenance, and a leaked prompt is excluded at any star count.
WHEN     the agent applies `skill-curation` in that situation
THEN     "SKIPPING THE POLICY CHECK BECAUSE THE CONTENT IS POPULAR" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Popularity does not launder provenance, and a leaked prompt is excluded at any star count."
FAIL IF  "SKIPPING THE POLICY CHECK BECAUSE THE CONTENT IS POPULAR" appears in the output — that is, "Popularity does not launder provenance, and a leaked prompt is excluded at any star count."; or it is absent by accident, with nothing in `skill-curation` having ruled it out
```

## Case 18 — Avoids: TREATING license: null AS A LOW SCORE

```text
GIVEN    A situation that invites the anti-pattern "TREATING license: null AS A LOW SCORE", whose stated consequence is: It is a hard override: reference only, never redistribute.
WHEN     the agent applies `skill-curation` in that situation
THEN     "TREATING license: null AS A LOW SCORE" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "It is a hard override: reference only, never redistribute."
FAIL IF  "TREATING license: null AS A LOW SCORE" appears in the output — that is, "It is a hard override: reference only, never redistribute."; or it is absent by accident, with nothing in `skill-curation` having ruled it out
```

## Case 19 — Avoids: DELETING UNVERIFIABLE CONTENT

```text
GIVEN    A situation that invites the anti-pattern "DELETING UNVERIFIABLE CONTENT", whose stated consequence is: Quarantine keeps the reasoning that prevents the same wrong claim being re-adopted; deletion loses it.
WHEN     the agent applies `skill-curation` in that situation
THEN     "DELETING UNVERIFIABLE CONTENT" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Quarantine keeps the reasoning that prevents the same wrong claim being re-adopted; deletion loses it."
FAIL IF  "DELETING UNVERIFIABLE CONTENT" appears in the output — that is, "Quarantine keeps the reasoning that prevents the same wrong claim being re-adopted; deletion loses it."; or it is absent by accident, with nothing in `skill-curation` having ruled it out
```

## Case 20 — Avoids: HIDING A CONFLICT

```text
GIVEN    A situation that invites the anti-pattern "HIDING A CONFLICT", whose stated consequence is: Suppressing the minority view destroys what a later reader needs to re-decide.
WHEN     the agent applies `skill-curation` in that situation
THEN     "HIDING A CONFLICT" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Suppressing the minority view destroys what a later reader needs to re-decide."
FAIL IF  "HIDING A CONFLICT" appears in the output — that is, "Suppressing the minority view destroys what a later reader needs to re-decide."; or it is absent by accident, with nothing in `skill-curation` having ruled it out
```

## Case 21 — Avoids: GRADING THE PUBLISHER INSTEAD OF THE CLAIM

```text
GIVEN    A situation that invites the anti-pattern "GRADING THE PUBLISHER INSTEAD OF THE CLAIM", whose stated consequence is: A prestigious source can carry an unverified claim.
WHEN     the agent applies `skill-curation` in that situation
THEN     "GRADING THE PUBLISHER INSTEAD OF THE CLAIM" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "A prestigious source can carry an unverified claim."
FAIL IF  "GRADING THE PUBLISHER INSTEAD OF THE CLAIM" appears in the output — that is, "A prestigious source can carry an unverified claim."; or it is absent by accident, with nothing in `skill-curation` having ruled it out
```

## Case 22 — Avoids: SETTING THE WINDOW FROM PRESTIGE

```text
GIVEN    A situation that invites the anti-pattern "SETTING THE WINDOW FROM PRESTIGE", whose stated consequence is: Recency is a property of the claim, not the publisher.
WHEN     the agent applies `skill-curation` in that situation
THEN     "SETTING THE WINDOW FROM PRESTIGE" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Recency is a property of the claim, not the publisher."
FAIL IF  "SETTING THE WINDOW FROM PRESTIGE" appears in the output — that is, "Recency is a property of the claim, not the publisher."; or it is absent by accident, with nothing in `skill-curation` having ruled it out
```

## Case 23 — Avoids: HAND-EDITING GENERATED FILES

```text
GIVEN    A situation that invites the anti-pattern "HAND-EDITING GENERATED FILES", whose stated consequence is: The change is silently lost on the next regeneration.
WHEN     the agent applies `skill-curation` in that situation
THEN     "HAND-EDITING GENERATED FILES" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The change is silently lost on the next regeneration."
FAIL IF  "HAND-EDITING GENERATED FILES" appears in the output — that is, "The change is silently lost on the next regeneration."; or it is absent by accident, with nothing in `skill-curation` having ruled it out
```

## Case 24 — Avoids: NO RECORDED REFUSALS

```text
GIVEN    A situation that invites the anti-pattern "NO RECORDED REFUSALS", whose stated consequence is: The same content is proposed again next quarter.
WHEN     the agent applies `skill-curation` in that situation
THEN     "NO RECORDED REFUSALS" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The same content is proposed again next quarter."
FAIL IF  "NO RECORDED REFUSALS" appears in the output — that is, "The same content is proposed again next quarter."; or it is absent by accident, with nothing in `skill-curation` having ruled it out
```
