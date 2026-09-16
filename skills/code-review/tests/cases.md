# Test cases — `code-review`

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
GIVEN    A task inside this skill's stated purpose: Improve the change **and** the codebase's long-term health, while transferring understanding to a second person. Review is not gatekeeping and not style enforcement — machines enforce style.
WHEN     the agent executes `code-review` end to end on that task
THEN     and before delivery these specific conditions hold: "Intent and acceptance criteria stated before review began"; "Design consistent with existing patterns; no second way of doing the same thing"; "Approval covers only what was actually read"
FAIL IF  "Intent and acceptance criteria stated before review began" is false, or "Approval covers only what was actually read" is false, or "Design consistent with existing patterns; no second way of doing the same thing" is false
```

## Case 2 — Declines: To relitigate an agreed architectural decision — that is an ADR conversation

```text
GIVEN    A task that looks like a match but is this skill's excluded case: To relitigate an agreed architectural decision — that is an ADR conversation
WHEN     the agent considers `code-review` for that task
THEN     the skill is not selected, because this task is the excluded case "To relitigate an agreed architectural decision — that is an ADR conversation", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "To relitigate an agreed architectural decision — that is an ADR conversation"; or `code-review` is declined without naming that exclusion
```

## Case 3 — Declines: To enforce formatting, naming style or import order — automate it

```text
GIVEN    A task that looks like a match but is this skill's excluded case: To enforce formatting, naming style or import order — automate it
WHEN     the agent considers `code-review` for that task
THEN     the skill is not selected, because this task is the excluded case "To enforce formatting, naming style or import order — automate it", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "To enforce formatting, naming style or import order — automate it"; or `code-review` is declined without naming that exclusion
```

## Case 4 — Declines: On a diff so large it cannot be reviewed properly: ask for it to be split…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: On a diff so large it cannot be reviewed properly: ask for it to be split first (rough guide: >400 changed lines of non-generated code loses review quality fast)
WHEN     the agent considers `code-review` for that task
THEN     the skill is not selected, because this task is the excluded case "On a diff so large it cannot be reviewed properly: ask for it to be split first (rough guide: >400 changed lines of non-generated code loses review quality…", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "On a diff so large it cannot be reviewed properly: ask for it to be split first (rough guide: >400 changed lines of non-generated code loses review…"; or `code-review` is declined without naming that exclusion
```

## Case 5 — Detects: RUBBER STAMP

```text
GIVEN    A run of this skill in which the known failure mode is present: RUBBER STAMP
WHEN     the agent executes `code-review` and reaches the point where this failure occurs
THEN     "RUBBER STAMP" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Approval without reading. Common with large diffs and with agent output."
FAIL IF  "RUBBER STAMP" appears in the work and is reported as complete — specifically "Approval without reading. Common with large diffs and with agent output."
```

## Case 6 — Detects: STYLE REVIEW

```text
GIVEN    A run of this skill in which the known failure mode is present: STYLE REVIEW
WHEN     the agent executes `code-review` and reaches the point where this failure occurs
THEN     "STYLE REVIEW" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Fifty comments on formatting, zero on correctness."
FAIL IF  "STYLE REVIEW" appears in the work and is reported as complete — specifically "Fifty comments on formatting, zero on correctness."
```

## Case 7 — Detects: LATE BLOCKING

```text
GIVEN    A run of this skill in which the known failure mode is present: LATE BLOCKING
WHEN     the agent executes `code-review` and reaches the point where this failure occurs
THEN     "LATE BLOCKING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Raising an architectural objection after implementation is complete — that belongs in design review, before code."
FAIL IF  "LATE BLOCKING" appears in the work and is reported as complete — specifically "Raising an architectural objection after implementation is complete — that belongs in design review, before code."
```

## Case 8 — Detects: DIFF-ONLY REVIEW

```text
GIVEN    A run of this skill in which the known failure mode is present: DIFF-ONLY REVIEW
WHEN     the agent executes `code-review` and reaches the point where this failure occurs
THEN     "DIFF-ONLY REVIEW" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Reading changed lines without the surrounding code, so context errors are invisible. Open the file."
FAIL IF  "DIFF-ONLY REVIEW" appears in the work and is reported as complete — specifically "Reading changed lines without the surrounding code, so context errors are invisible. Open the file."
```

## Case 9 — Detects: NITPICK FLOOD

```text
GIVEN    A run of this skill in which the known failure mode is present: NITPICK FLOOD
WHEN     the agent executes `code-review` and reaches the point where this failure occurs
THEN     "NITPICK FLOOD" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Twenty NITs burying one BLOCKER; the author fixes the easy ones."
FAIL IF  "NITPICK FLOOD" appears in the work and is reported as complete — specifically "Twenty NITs burying one BLOCKER; the author fixes the easy ones."
```

## Case 10 — Detects: UNGRADED FEEDBACK

```text
GIVEN    A run of this skill in which the known failure mode is present: UNGRADED FEEDBACK
WHEN     the agent executes `code-review` and reaches the point where this failure occurs
THEN     "UNGRADED FEEDBACK" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "The author cannot tell what must change from what is taste."
FAIL IF  "UNGRADED FEEDBACK" appears in the work and is reported as complete — specifically "The author cannot tell what must change from what is taste."
```

## Case 11 — Detects: TEST-FREE APPROVAL

```text
GIVEN    A run of this skill in which the known failure mode is present: TEST-FREE APPROVAL
WHEN     the agent executes `code-review` and reaches the point where this failure occurs
THEN     "TEST-FREE APPROVAL" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Merging new behaviour with no test, because the diff looked clean. SILENT TEST WEAKENING An assertion removed to make a failing test pass, unremarked."
FAIL IF  "TEST-FREE APPROVAL" appears in the work and is reported as complete — specifically "Merging new behaviour with no test, because the diff looked clean. SILENT TEST WEAKENING An assertion removed to make a failing test pass, unremarked."
```

## Case 12 — Detects: GENERATED-CODE TRUST

```text
GIVEN    A run of this skill in which the known failure mode is present: GENERATED-CODE TRUST
WHEN     the agent executes `code-review` and reaches the point where this failure occurs
THEN     "GENERATED-CODE TRUST" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Skimming vendor/generated diffs, which is where the CVE lives."
FAIL IF  "GENERATED-CODE TRUST" appears in the work and is reported as complete — specifically "Skimming vendor/generated diffs, which is where the CVE lives."
```

## Case 13 — Detects: REVIEW-BY-CI

```text
GIVEN    A run of this skill in which the known failure mode is present: REVIEW-BY-CI
WHEN     the agent executes `code-review` and reaches the point where this failure occurs
THEN     "REVIEW-BY-CI" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Assuming green checks mean the change is right."
FAIL IF  "REVIEW-BY-CI" appears in the work and is reported as complete — specifically "Assuming green checks mean the change is right."
```

## Case 14 — Avoids: "LGTM" with no comments on a 1500-line diff

```text
GIVEN    A situation that invites the anti-pattern "LGTM" with no comments on a 1500-line diff"
WHEN     the agent applies `code-review` in that situation
THEN     "LGTM" with no comments on a 1500-line diff" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "LGTM" with no comments on a 1500-line diff" appears in the output; or it is absent by accident, with nothing in `code-review` having ruled it out
```

## Case 15 — Avoids: `try { … } catch (e) {}` approved because it "handles errors"

```text
GIVEN    A situation that invites the anti-pattern "`try { … } catch (e) {}` approved because it "handles errors"
WHEN     the agent applies `code-review` in that situation
THEN     "`try { … } catch (e) {}` approved because it "handles errors" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`try { … } catch (e) {}` approved because it "handles errors" appears in the output; or it is absent by accident, with nothing in `code-review` having ruled it out
```

## Case 16 — Avoids: A comment that says "consider refactoring" with no direction and no severity

```text
GIVEN    A situation that invites the anti-pattern "A comment that says "consider refactoring" with no direction and no severity"
WHEN     the agent applies `code-review` in that situation
THEN     "A comment that says "consider refactoring" with no direction and no severity" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A comment that says "consider refactoring" with no direction and no severity" appears in the output; or it is absent by accident, with nothing in `code-review` having ruled it out
```

## Case 17 — Avoids: Reviewing only the files you already know

```text
GIVEN    A situation that invites the anti-pattern "Reviewing only the files you already know"
WHEN     the agent applies `code-review` in that situation
THEN     "Reviewing only the files you already know" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Reviewing only the files you already know" appears in the output; or it is absent by accident, with nothing in `code-review` having ruled it out
```

## Case 18 — Avoids: Approving a migration you have not checked for locks

```text
GIVEN    A situation that invites the anti-pattern "Approving a migration you have not checked for locks"
WHEN     the agent applies `code-review` in that situation
THEN     "Approving a migration you have not checked for locks" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Approving a migration you have not checked for locks" appears in the output; or it is absent by accident, with nothing in `code-review` having ruled it out
```

## Case 19 — Avoids: Merging a change that deletes an assertion, unremarked

```text
GIVEN    A situation that invites the anti-pattern "Merging a change that deletes an assertion, unremarked"
WHEN     the agent applies `code-review` in that situation
THEN     "Merging a change that deletes an assertion, unremarked" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Merging a change that deletes an assertion, unremarked" appears in the output; or it is absent by accident, with nothing in `code-review` having ruled it out
```

## Case 20 — Avoids: Formatting comments in a codebase with a formatter configured

```text
GIVEN    A situation that invites the anti-pattern "Formatting comments in a codebase with a formatter configured"
WHEN     the agent applies `code-review` in that situation
THEN     "Formatting comments in a codebase with a formatter configured" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Formatting comments in a codebase with a formatter configured" appears in the output; or it is absent by accident, with nothing in `code-review` having ruled it out
```

## Case 21 — Avoids: Trusting a generated lockfile diff without looking at what changed

```text
GIVEN    A situation that invites the anti-pattern "Trusting a generated lockfile diff without looking at what changed"
WHEN     the agent applies `code-review` in that situation
THEN     "Trusting a generated lockfile diff without looking at what changed" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Trusting a generated lockfile diff without looking at what changed" appears in the output; or it is absent by accident, with nothing in `code-review` having ruled it out
```
