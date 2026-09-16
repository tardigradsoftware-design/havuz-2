# Test cases — `refactoring`

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
GIVEN    A task inside this skill's stated purpose: Improve the internal structure of code while its **observable behaviour is provably unchanged**. The discipline is what makes it safe: small steps, verification after each, and no behavioural change mixed in.
WHEN     the agent executes `refactoring` end to end on that task
THEN     and before delivery these specific conditions hold: "Current behaviour and intent understood before changing structure"; "No behaviour change mixed in; bugs found during refactoring filed separately and fixed after"; "Review confirms the new structure helps the next change, not just this one"
FAIL IF  "Current behaviour and intent understood before changing structure" is false, or "Review confirms the new structure helps the next change, not just this one" is false, or "No behaviour change mixed in; bugs found during refactoring filed separately and fixed after" is false
```

## Case 2 — Declines: Without tests and without the budget to write characterisation tests first

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Without tests and without the budget to write characterisation tests first
WHEN     the agent considers `refactoring` for that task
THEN     the skill is not selected, because this task is the excluded case "Without tests and without the budget to write characterisation tests first", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Without tests and without the budget to write characterisation tests first"; or `refactoring` is declined without naming that exclusion
```

## Case 3 — Declines: On code about to be deleted

```text
GIVEN    A task that looks like a match but is this skill's excluded case: On code about to be deleted
WHEN     the agent considers `refactoring` for that task
THEN     the skill is not selected, because this task is the excluded case "On code about to be deleted", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "On code about to be deleted"; or `refactoring` is declined without naming that exclusion
```

## Case 4 — Declines: As a way to avoid a difficult feature (refactoring as procrastination)

```text
GIVEN    A task that looks like a match but is this skill's excluded case: As a way to avoid a difficult feature (refactoring as procrastination)
WHEN     the agent considers `refactoring` for that task
THEN     the skill is not selected, because this task is the excluded case "As a way to avoid a difficult feature (refactoring as procrastination)", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "As a way to avoid a difficult feature (refactoring as procrastination)"; or `refactoring` is declined without naming that exclusion
```

## Case 5 — Declines: On code you do not understand yet — understand first;

```text
GIVEN    A task that looks like a match but is this skill's excluded case: On code you do not understand yet — understand first; refactoring an unfamiliar system destroys the accumulated intent you cannot see
WHEN     the agent considers `refactoring` for that task
THEN     the skill is not selected, because this task is the excluded case "On code you do not understand yet — understand first; refactoring an unfamiliar system destroys the accumulated intent you cannot see", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "On code you do not understand yet — understand first; refactoring an unfamiliar system destroys the accumulated intent you cannot see"; or `refactoring` is declined without naming that exclusion
```

## Case 6 — Declines: Bundled with a feature in one commit: the reviewer cannot tell which change…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Bundled with a feature in one commit: the reviewer cannot tell which change caused a regression
WHEN     the agent considers `refactoring` for that task
THEN     the skill is not selected, because this task is the excluded case "Bundled with a feature in one commit: the reviewer cannot tell which change caused a regression", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Bundled with a feature in one commit: the reviewer cannot tell which change caused a regression"; or `refactoring` is declined without naming that exclusion
```

## Case 7 — Detects: NO SAFETY NET

```text
GIVEN    A run of this skill in which the known failure mode is present: NO SAFETY NET
WHEN     the agent executes `refactoring` and reaches the point where this failure occurs
THEN     "NO SAFETY NET" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Restructuring uncovered code and hoping."
FAIL IF  "NO SAFETY NET" appears in the work and is reported as complete — specifically "Restructuring uncovered code and hoping."
```

## Case 8 — Detects: BIG-BANG REFACTOR

```text
GIVEN    A run of this skill in which the known failure mode is present: BIG-BANG REFACTOR
WHEN     the agent executes `refactoring` and reaches the point where this failure occurs
THEN     "BIG-BANG REFACTOR" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A 3,000-line commit that cannot be reviewed or bisected."
FAIL IF  "BIG-BANG REFACTOR" appears in the work and is reported as complete — specifically "A 3,000-line commit that cannot be reviewed or bisected."
```

## Case 9 — Detects: BEHAVIOUR SMUGGLING

```text
GIVEN    A run of this skill in which the known failure mode is present: BEHAVIOUR SMUGGLING
WHEN     the agent executes `refactoring` and reaches the point where this failure occurs
THEN     "BEHAVIOUR SMUGGLING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A "pure refactor" that quietly fixes a bug — now nobody knows what changed."
FAIL IF  "BEHAVIOUR SMUGGLING" appears in the work and is reported as complete — specifically "A "pure refactor" that quietly fixes a bug — now nobody knows what changed."
```

## Case 10 — Detects: DEBUGGING FORWARD

```text
GIVEN    A run of this skill in which the known failure mode is present: DEBUGGING FORWARD
WHEN     the agent executes `refactoring` and reaches the point where this failure occurs
THEN     "DEBUGGING FORWARD" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A red test after a step, answered by editing the test or pushing on."
FAIL IF  "DEBUGGING FORWARD" appears in the work and is reported as complete — specifically "A red test after a step, answered by editing the test or pushing on."
```

## Case 11 — Detects: REWRITE AS REFACTOR

```text
GIVEN    A run of this skill in which the known failure mode is present: REWRITE AS REFACTOR
WHEN     the agent executes `refactoring` and reaches the point where this failure occurs
THEN     "REWRITE AS REFACTOR" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Cleaning up" that discards accumulated intent and edge-case handling."
FAIL IF  "REWRITE AS REFACTOR" appears in the work and is reported as complete — specifically "Cleaning up" that discards accumulated intent and edge-case handling."
```

## Case 12 — Detects: TASTE-ONLY CHURN

```text
GIVEN    A run of this skill in which the known failure mode is present: TASTE-ONLY CHURN
WHEN     the agent executes `refactoring` and reaches the point where this failure occurs
THEN     "TASTE-ONLY CHURN" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Restructuring to a personal preference with no maintainability argument."
FAIL IF  "TASTE-ONLY CHURN" appears in the work and is reported as complete — specifically "Restructuring to a personal preference with no maintainability argument."
```

## Case 13 — Detects: PROCRASTINATION

```text
GIVEN    A run of this skill in which the known failure mode is present: PROCRASTINATION
WHEN     the agent executes `refactoring` and reaches the point where this failure occurs
THEN     "PROCRASTINATION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Endless refactoring to avoid shipping a feature."
FAIL IF  "PROCRASTINATION" appears in the work and is reported as complete — specifically "Endless refactoring to avoid shipping a feature."
```

## Case 14 — Detects: ABANDONED MID-FLIGHT

```text
GIVEN    A run of this skill in which the known failure mode is present: ABANDONED MID-FLIGHT
WHEN     the agent executes `refactoring` and reaches the point where this failure occurs
THEN     "ABANDONED MID-FLIGHT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Half-migrated structure left in place — worse than either endpoint."
FAIL IF  "ABANDONED MID-FLIGHT" appears in the work and is reported as complete — specifically "Half-migrated structure left in place — worse than either endpoint."
```

## Case 15 — Detects: UNMEASURED PERFORMANCE

```text
GIVEN    A run of this skill in which the known failure mode is present: UNMEASURED PERFORMANCE
WHEN     the agent executes `refactoring` and reaches the point where this failure occurs
THEN     "UNMEASURED PERFORMANCE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A structure that is cleaner and 4× slower on the hot path."
FAIL IF  "UNMEASURED PERFORMANCE" appears in the work and is reported as complete — specifically "A structure that is cleaner and 4× slower on the hot path."
```

## Case 16 — Detects: TOOLING AVOIDANCE

```text
GIVEN    A run of this skill in which the known failure mode is present: TOOLING AVOIDANCE
WHEN     the agent executes `refactoring` and reaches the point where this failure occurs
THEN     "TOOLING AVOIDANCE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Hand-editing what an automated refactor would do correctly."
FAIL IF  "TOOLING AVOIDANCE" appears in the work and is reported as complete — specifically "Hand-editing what an automated refactor would do correctly."
```

## Case 17 — Avoids: "I refactored it" as a description of a 3,000-line diff with no tests

```text
GIVEN    A situation that invites the anti-pattern "I refactored it" as a description of a 3,000-line diff with no tests"
WHEN     the agent applies `refactoring` in that situation
THEN     "I refactored it" as a description of a 3,000-line diff with no tests" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "I refactored it" as a description of a 3,000-line diff with no tests" appears in the output; or it is absent by accident, with nothing in `refactoring` having ruled it out
```

## Case 18 — Avoids: Renaming a method and changing its behaviour in the same commit

```text
GIVEN    A situation that invites the anti-pattern "Renaming a method and changing its behaviour in the same commit"
WHEN     the agent applies `refactoring` in that situation
THEN     "Renaming a method and changing its behaviour in the same commit" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Renaming a method and changing its behaviour in the same commit" appears in the output; or it is absent by accident, with nothing in `refactoring` having ruled it out
```

## Case 19 — Avoids: Deleting the `if` that looked redundant and was handling a production edge…

```text
GIVEN    A situation that invites the anti-pattern "Deleting the `if` that looked redundant and was handling a production edge case"
WHEN     the agent applies `refactoring` in that situation
THEN     "Deleting the `if` that looked redundant and was handling a production edge case" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Deleting the `if` that looked redundant and was handling a production edge case" appears in the output; or it is absent by accident, with nothing in `refactoring` having ruled it out
```

## Case 20 — Avoids: Loosening an assertion so the refactor could pass

```text
GIVEN    A situation that invites the anti-pattern "Loosening an assertion so the refactor could pass"
WHEN     the agent applies `refactoring` in that situation
THEN     "Loosening an assertion so the refactor could pass" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Loosening an assertion so the refactor could pass" appears in the output; or it is absent by accident, with nothing in `refactoring` having ruled it out
```

## Case 21 — Avoids: A half-finished strangler migration left running for a year

```text
GIVEN    A situation that invites the anti-pattern "A half-finished strangler migration left running for a year"
WHEN     the agent applies `refactoring` in that situation
THEN     "A half-finished strangler migration left running for a year" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A half-finished strangler migration left running for a year" appears in the output; or it is absent by accident, with nothing in `refactoring` having ruled it out
```

## Case 22 — Avoids: Restructuring a module you have read once

```text
GIVEN    A situation that invites the anti-pattern "Restructuring a module you have read once"
WHEN     the agent applies `refactoring` in that situation
THEN     "Restructuring a module you have read once" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Restructuring a module you have read once" appears in the output; or it is absent by accident, with nothing in `refactoring` having ruled it out
```

## Case 23 — Avoids: Refactoring generated or vendored code

```text
GIVEN    A situation that invites the anti-pattern "Refactoring generated or vendored code"
WHEN     the agent applies `refactoring` in that situation
THEN     "Refactoring generated or vendored code" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Refactoring generated or vendored code" appears in the output; or it is absent by accident, with nothing in `refactoring` having ruled it out
```
