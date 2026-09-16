# Test cases — `project-planning`

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
GIVEN    A task inside this skill's stated purpose: Convert an ambiguous goal into a sequence of steps, each with an **observable completion condition**, so progress is verifiable continuously and failure is detected early rather than at the end.
WHEN     the agent executes `project-planning` end to end on that task
THEN     and before delivery these specific conditions hold: "Outcomes written as 3–7 observable statements, agreed with the requester"; "Estimates as three-point ranges with a stated basis and confidence level"; "Estimate-vs-actual recorded and reviewed"
FAIL IF  "Outcomes written as 3–7 observable statements, agreed with the requester" is false, or "Estimate-vs-actual recorded and reviewed" is false, or "Estimates as three-point ranges with a stated basis and confidence level" is false
```

## Case 2 — Declines: A single well-understood change — do it

```text
GIVEN    A task that looks like a match but is this skill's excluded case: A single well-understood change — do it
WHEN     the agent considers `project-planning` for that task
THEN     the skill is not selected, because this task is the excluded case "A single well-understood change — do it", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "A single well-understood change — do it"; or `project-planning` is declined without naming that exclusion
```

## Case 3 — Declines: Genuine exploration where the goal is to learn what the problem is (timebox a…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Genuine exploration where the goal is to learn what the problem is (timebox a spike instead, and plan the follow-up)
WHEN     the agent considers `project-planning` for that task
THEN     the skill is not selected, because this task is the excluded case "Genuine exploration where the goal is to learn what the problem is (timebox a spike instead, and plan the follow-up)", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Genuine exploration where the goal is to learn what the problem is (timebox a spike instead, and plan the follow-up)"; or `project-planning` is declined without naming that exclusion
```

## Case 4 — Declines: When the plan will be discarded: planning has a cost;

```text
GIVEN    A task that looks like a match but is this skill's excluded case: When the plan will be discarded: planning has a cost; spend it where sequencing matters
WHEN     the agent considers `project-planning` for that task
THEN     the skill is not selected, because this task is the excluded case "When the plan will be discarded: planning has a cost; spend it where sequencing matters", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "When the plan will be discarded: planning has a cost; spend it where sequencing matters"; or `project-planning` is declined without naming that exclusion
```

## Case 5 — Detects: NOUN LIST

```text
GIVEN    A run of this skill in which the known failure mode is present: NOUN LIST
WHEN     the agent executes `project-planning` and reaches the point where this failure occurs
THEN     "NOUN LIST" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Auth, DB, API, UI" — no order, no gates, no outcomes."
FAIL IF  "NOUN LIST" appears in the work and is reported as complete — specifically "Auth, DB, API, UI" — no order, no gates, no outcomes."
```

## Case 6 — Detects: HORIZONTAL SLICING

```text
GIVEN    A run of this skill in which the known failure mode is present: HORIZONTAL SLICING
WHEN     the agent executes `project-planning` and reaches the point where this failure occurs
THEN     "HORIZONTAL SLICING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Layer-by-layer delivery; nothing demonstrable for weeks."
FAIL IF  "HORIZONTAL SLICING" appears in the work and is reported as complete — specifically "Layer-by-layer delivery; nothing demonstrable for weeks."
```

## Case 7 — Detects: LATE DE-RISKING

```text
GIVEN    A run of this skill in which the known failure mode is present: LATE DE-RISKING
WHEN     the agent executes `project-planning` and reaches the point where this failure occurs
THEN     "LATE DE-RISKING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "The riskiest item scheduled last, when there is no time left to react."
FAIL IF  "LATE DE-RISKING" appears in the work and is reported as complete — specifically "The riskiest item scheduled last, when there is no time left to react."
```

## Case 8 — Detects: HIDDEN UNKNOWN

```text
GIVEN    A run of this skill in which the known failure mode is present: HIDDEN UNKNOWN
WHEN     the agent executes `project-planning` and reaches the point where this failure occurs
THEN     "HIDDEN UNKNOWN" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "TBD" in a plan, with no owner, budget or decision attached."
FAIL IF  "HIDDEN UNKNOWN" appears in the work and is reported as complete — specifically "TBD" in a plan, with no owner, budget or decision attached."
```

## Case 9 — Detects: OPTIMISM AS PLAN

```text
GIVEN    A run of this skill in which the known failure mode is present: OPTIMISM AS PLAN
WHEN     the agent executes `project-planning` and reaches the point where this failure occurs
THEN     "OPTIMISM AS PLAN" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Quoting the optimistic number and treating the pessimistic as noise. EFFORT = CALENDAR Ignoring review latency and third-party response time."
FAIL IF  "OPTIMISM AS PLAN" appears in the work and is reported as complete — specifically "Quoting the optimistic number and treating the pessimistic as noise. EFFORT = CALENDAR Ignoring review latency and third-party response time."
```

## Case 10 — Detects: NO STOP CONDITION

```text
GIVEN    A run of this skill in which the known failure mode is present: NO STOP CONDITION
WHEN     the agent executes `project-planning` and reaches the point where this failure occurs
THEN     "NO STOP CONDITION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Continuing a blocked or worthless task because stopping was never defined."
FAIL IF  "NO STOP CONDITION" appears in the work and is reported as complete — specifically "Continuing a blocked or worthless task because stopping was never defined."
```

## Case 11 — Detects: PLAN ABANDONMENT

```text
GIVEN    A run of this skill in which the known failure mode is present: PLAN ABANDONMENT
WHEN     the agent executes `project-planning` and reaches the point where this failure occurs
THEN     "PLAN ABANDONMENT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "The detailed plan diverges from reality on day 2 and is never updated."
FAIL IF  "PLAN ABANDONMENT" appears in the work and is reported as complete — specifically "The detailed plan diverges from reality on day 2 and is never updated."
```

## Case 12 — Detects: SILENT RE-PLAN

```text
GIVEN    A run of this skill in which the known failure mode is present: SILENT RE-PLAN
WHEN     the agent executes `project-planning` and reaches the point where this failure occurs
THEN     "SILENT RE-PLAN" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Scope changes without the constraint conversation that should follow."
FAIL IF  "SILENT RE-PLAN" appears in the work and is reported as complete — specifically "Scope changes without the constraint conversation that should follow."
```

## Case 13 — Detects: INTEGRATION AS A FOOTNOTE

```text
GIVEN    A run of this skill in which the known failure mode is present: INTEGRATION AS A FOOTNOTE
WHEN     the agent executes `project-planning` and reaches the point where this failure occurs
THEN     "INTEGRATION AS A FOOTNOTE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "The hardest task assumed to be "wiring it up". BUFFER SMearing Padding inside every task so nobody can see or trade the total."
FAIL IF  "INTEGRATION AS A FOOTNOTE" appears in the work and is reported as complete — specifically "The hardest task assumed to be "wiring it up". BUFFER SMearing Padding inside every task so nobody can see or trade the total."
```

## Case 14 — Detects: NO RETROSPECTIVE

```text
GIVEN    A run of this skill in which the known failure mode is present: NO RETROSPECTIVE
WHEN     the agent executes `project-planning` and reaches the point where this failure occurs
THEN     "NO RETROSPECTIVE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Estimate-vs-actual never recorded, so nothing improves."
FAIL IF  "NO RETROSPECTIVE" appears in the work and is reported as complete — specifically "Estimate-vs-actual never recorded, so nothing improves."
```

## Case 15 — Avoids: A Gantt chart of layers with no demonstrable milestone until the end

```text
GIVEN    A situation that invites the anti-pattern "A Gantt chart of layers with no demonstrable milestone until the end"
WHEN     the agent applies `project-planning` in that situation
THEN     "A Gantt chart of layers with no demonstrable milestone until the end" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A Gantt chart of layers with no demonstrable milestone until the end" appears in the output; or it is absent by accident, with nothing in `project-planning` having ruled it out
```

## Case 16 — Avoids: "Should take about a day" with no basis, no range and no confidence

```text
GIVEN    A situation that invites the anti-pattern "Should take about a day" with no basis, no range and no confidence"
WHEN     the agent applies `project-planning` in that situation
THEN     "Should take about a day" with no basis, no range and no confidence" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Should take about a day" with no basis, no range and no confidence" appears in the output; or it is absent by accident, with nothing in `project-planning` having ruled it out
```

## Case 17 — Avoids: The riskiest integration scheduled in the final week

```text
GIVEN    A situation that invites the anti-pattern "The riskiest integration scheduled in the final week"
WHEN     the agent applies `project-planning` in that situation
THEN     "The riskiest integration scheduled in the final week" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "The riskiest integration scheduled in the final week" appears in the output; or it is absent by accident, with nothing in `project-planning` having ruled it out
```

## Case 18 — Avoids: "TBD: caching strategy" left in an approved plan

```text
GIVEN    A situation that invites the anti-pattern "TBD: caching strategy" left in an approved plan"
WHEN     the agent applies `project-planning` in that situation
THEN     "TBD: caching strategy" left in an approved plan" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "TBD: caching strategy" left in an approved plan" appears in the output; or it is absent by accident, with nothing in `project-planning` having ruled it out
```

## Case 19 — Avoids: A plan written once and never updated after reality diverged

```text
GIVEN    A situation that invites the anti-pattern "A plan written once and never updated after reality diverged"
WHEN     the agent applies `project-planning` in that situation
THEN     "A plan written once and never updated after reality diverged" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A plan written once and never updated after reality diverged" appears in the output; or it is absent by accident, with nothing in `project-planning` having ruled it out
```

## Case 20 — Avoids: An autonomous agent with no stop condition and no escalation trigger

```text
GIVEN    A situation that invites the anti-pattern "An autonomous agent with no stop condition and no escalation trigger"
WHEN     the agent applies `project-planning` in that situation
THEN     "An autonomous agent with no stop condition and no escalation trigger" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "An autonomous agent with no stop condition and no escalation trigger" appears in the output; or it is absent by accident, with nothing in `project-planning` having ruled it out
```

## Case 21 — Avoids: Buffer distributed invisibly across twenty tasks

```text
GIVEN    A situation that invites the anti-pattern "Buffer distributed invisibly across twenty tasks"
WHEN     the agent applies `project-planning` in that situation
THEN     "Buffer distributed invisibly across twenty tasks" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Buffer distributed invisibly across twenty tasks" appears in the output; or it is absent by accident, with nothing in `project-planning` having ruled it out
```

## Case 22 — Avoids: Declaring a milestone complete because the tasks are done,

```text
GIVEN    A situation that invites the anti-pattern "Declaring a milestone complete because the tasks are done,"
WHEN     the agent applies `project-planning` in that situation
THEN     "Declaring a milestone complete because the tasks are done," is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Declaring a milestone complete because the tasks are done," appears in the output; or it is absent by accident, with nothing in `project-planning` having ruled it out
```
