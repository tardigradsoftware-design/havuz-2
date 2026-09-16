# Test cases — `evidence-validation`

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
GIVEN    A task inside this skill's stated purpose: Assign every claim a **confidence level backed by a checkable procedure**, and refuse to promote ungradeable material into the knowledge base. Validation is not "does this look right".
WHEN     the agent executes `evidence-validation` end to end on that task
THEN     and before delivery these specific conditions hold: "Claim written exactly, with version and date scope"; "Independent corroboration found, or its absence stated"; "Re-verification date set from the freshness policy"
FAIL IF  "Claim written exactly, with version and date scope" is false, or "Re-verification date set from the freshness policy" is false, or "Independent corroboration found, or its absence stated" is false
```

## Case 2 — Declines: Statements about this repository's own contents — read the file

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Statements about this repository's own contents — read the file
WHEN     the agent considers `evidence-validation` for that task
THEN     the skill is not selected, because this task is the excluded case "Statements about this repository's own contents — read the file", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Statements about this repository's own contents — read the file"; or `evidence-validation` is declined without naming that exclusion
```

## Case 3 — Declines: Pure preferences ("I like this layout") — label them opinion and move on

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Pure preferences ("I like this layout") — label them opinion and move on
WHEN     the agent considers `evidence-validation` for that task
THEN     the skill is not selected, because this task is the excluded case "Pure preferences ("I like this layout") — label them opinion and move on", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Pure preferences ("I like this layout") — label them opinion and move on"; or `evidence-validation` is declined without naming that exclusion
```

## Case 4 — Declines: Re-validating something already validated today with an unchanged source:…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Re-validating something already validated today with an unchanged source: reuse the existing verified_at instead of burning budget
WHEN     the agent considers `evidence-validation` for that task
THEN     the skill is not selected, because this task is the excluded case "Re-validating something already validated today with an unchanged source: reuse the existing verified_at instead of burning budget", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Re-validating something already validated today with an unchanged source: reuse the existing verified_at instead of burning budget"; or `evidence-validation` is declined without naming that exclusion
```

## Case 5 — Detects: PRESTIGE TRANSFER

```text
GIVEN    A run of this skill in which the known failure mode is present: PRESTIGE TRANSFER
WHEN     the agent executes `evidence-validation` and reaches the point where this failure occurs
THEN     "PRESTIGE TRANSFER" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "It's from Stanford, so the specific number is right." Prestige grades the publisher, not the measurement."
FAIL IF  "PRESTIGE TRANSFER" appears in the work and is reported as complete — specifically "It's from Stanford, so the specific number is right." Prestige grades the publisher, not the measurement."
```

## Case 6 — Detects: DATE CONFUSION

```text
GIVEN    A run of this skill in which the known failure mode is present: DATE CONFUSION
WHEN     the agent executes `evidence-validation` and reaches the point where this failure occurs
THEN     "DATE CONFUSION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Using the crawl date as the publication date."
FAIL IF  "DATE CONFUSION" appears in the work and is reported as complete — specifically "Using the crawl date as the publication date."
```

## Case 7 — Detects: SCOPE CREEP

```text
GIVEN    A run of this skill in which the known failure mode is present: SCOPE CREEP
WHEN     the agent executes `evidence-validation` and reaches the point where this failure occurs
THEN     "SCOPE CREEP" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Source says "in our benchmark on task X"; you record "in general"."
FAIL IF  "SCOPE CREEP" appears in the work and is reported as complete — specifically "Source says "in our benchmark on task X"; you record "in general"."
```

## Case 8 — Detects: VERSION DRIFT

```text
GIVEN    A run of this skill in which the known failure mode is present: VERSION DRIFT
WHEN     the agent executes `evidence-validation` and reaches the point where this failure occurs
THEN     "VERSION DRIFT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Source describes v4; you apply it to v6."
FAIL IF  "VERSION DRIFT" appears in the work and is reported as complete — specifically "Source describes v4; you apply it to v6."
```

## Case 9 — Detects: SINGLE-SOURCE STACK

```text
GIVEN    A run of this skill in which the known failure mode is present: SINGLE-SOURCE STACK
WHEN     the agent executes `evidence-validation` and reaches the point where this failure occurs
THEN     "SINGLE-SOURCE STACK" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Building a plan on one medium-confidence claim without flagging it. CONFIDENCE INFLATION Labelling a model-generated statement `high` because it sounds right."
FAIL IF  "SINGLE-SOURCE STACK" appears in the work and is reported as complete — specifically "Building a plan on one medium-confidence claim without flagging it. CONFIDENCE INFLATION Labelling a model-generated statement `high` because it sounds right."
```

## Case 10 — Detects: CHECKLIST THEATRE

```text
GIVEN    A run of this skill in which the known failure mode is present: CHECKLIST THEATRE
WHEN     the agent executes `evidence-validation` and reaches the point where this failure occurs
THEN     "CHECKLIST THEATRE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Filling the form without actually resolving the URL."
FAIL IF  "CHECKLIST THEATRE" appears in the work and is reported as complete — specifically "Filling the form without actually resolving the URL."
```

## Case 11 — Detects: OVER-VALIDATION

```text
GIVEN    A run of this skill in which the known failure mode is present: OVER-VALIDATION
WHEN     the agent executes `evidence-validation` and reaches the point where this failure occurs
THEN     "OVER-VALIDATION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Re-verifying a stable specification every day and burning the budget."
FAIL IF  "OVER-VALIDATION" appears in the work and is reported as complete — specifically "Re-verifying a stable specification every day and burning the budget."
```

## Case 12 — Avoids: Accepting a claim because it matches what you already believed

```text
GIVEN    A situation that invites the anti-pattern "Accepting a claim because it matches what you already believed"
WHEN     the agent applies `evidence-validation` in that situation
THEN     "Accepting a claim because it matches what you already believed" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Accepting a claim because it matches what you already believed" appears in the output; or it is absent by accident, with nothing in `evidence-validation` having ruled it out
```

## Case 13 — Avoids: Recording a number with no measurement method

```text
GIVEN    A situation that invites the anti-pattern "Recording a number with no measurement method"
WHEN     the agent applies `evidence-validation` in that situation
THEN     "Recording a number with no measurement method" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Recording a number with no measurement method" appears in the output; or it is absent by accident, with nothing in `evidence-validation` having ruled it out
```

## Case 14 — Avoids: Citing an aggregator when the primary source is reachable

```text
GIVEN    A situation that invites the anti-pattern "Citing an aggregator when the primary source is reachable"
WHEN     the agent applies `evidence-validation` in that situation
THEN     "Citing an aggregator when the primary source is reachable" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Citing an aggregator when the primary source is reachable" appears in the output; or it is absent by accident, with nothing in `evidence-validation` having ruled it out
```

## Case 15 — Avoids: Letting a conflict disappear by choosing the more convenient side

```text
GIVEN    A situation that invites the anti-pattern "Letting a conflict disappear by choosing the more convenient side"
WHEN     the agent applies `evidence-validation` in that situation
THEN     "Letting a conflict disappear by choosing the more convenient side" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Letting a conflict disappear by choosing the more convenient side" appears in the output; or it is absent by accident, with nothing in `evidence-validation` having ruled it out
```

## Case 16 — Avoids: Marking model output as `fact`

```text
GIVEN    A situation that invites the anti-pattern "Marking model output as `fact`"
WHEN     the agent applies `evidence-validation` in that situation
THEN     "Marking model output as `fact`" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Marking model output as `fact`" appears in the output; or it is absent by accident, with nothing in `evidence-validation` having ruled it out
```

## Case 17 — Avoids: Validating the source but not the claim's scope

```text
GIVEN    A situation that invites the anti-pattern "Validating the source but not the claim's scope"
WHEN     the agent applies `evidence-validation` in that situation
THEN     "Validating the source but not the claim's scope" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Validating the source but not the claim's scope" appears in the output; or it is absent by accident, with nothing in `evidence-validation` having ruled it out
```
