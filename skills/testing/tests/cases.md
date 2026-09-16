# Test cases — `testing`

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
GIVEN    A task inside this skill's stated purpose: Produce tests that **fail when the behaviour is wrong and for no other reason**. Coverage percentages, test counts and green CI badges are outputs of that property, not substitutes for it.
WHEN     the agent executes `testing` end to end on that task
THEN     and before delivery these specific conditions hold: "Level chosen as the lowest that can prove the property"; "The inner loop runs in seconds; CI fails fast in level order"; "Escaped defects analysed and the strategy updated"
FAIL IF  "Level chosen as the lowest that can prove the property" is false, or "Escaped defects analysed and the strategy updated" is false, or "The inner loop runs in seconds; CI fails fast in level order" is false
```

## Case 2 — Declines: Testing framework internals or language semantics — test your use of them

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Testing framework internals or language semantics — test your use of them
WHEN     the agent considers `testing` for that task
THEN     the skill is not selected, because this task is the excluded case "Testing framework internals or language semantics — test your use of them", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Testing framework internals or language semantics — test your use of them"; or `testing` is declined without naming that exclusion
```

## Case 3 — Declines: Exhaustive getter/setter coverage to inflate a metric

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Exhaustive getter/setter coverage to inflate a metric
WHEN     the agent considers `testing` for that task
THEN     the skill is not selected, because this task is the excluded case "Exhaustive getter/setter coverage to inflate a metric", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Exhaustive getter/setter coverage to inflate a metric"; or `testing` is declined without naming that exclusion
```

## Case 4 — Declines: Snapshot tests as the primary strategy for logic (they assert "unchanged",

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Snapshot tests as the primary strategy for logic (they assert "unchanged", not "correct")
WHEN     the agent considers `testing` for that task
THEN     the skill is not selected, because this task is the excluded case "Snapshot tests as the primary strategy for logic (they assert "unchanged", not "correct")", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Snapshot tests as the primary strategy for logic (they assert "unchanged", not "correct")"; or `testing` is declined without naming that exclusion
```

## Case 5 — Declines: Throwaway spikes — but delete the spike before it becomes production code

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Throwaway spikes — but delete the spike before it becomes production code
WHEN     the agent considers `testing` for that task
THEN     the skill is not selected, because this task is the excluded case "Throwaway spikes — but delete the spike before it becomes production code", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Throwaway spikes — but delete the spike before it becomes production code"; or `testing` is declined without naming that exclusion
```

## Case 6 — Detects: IMPLEMENTATION MIRRORING

```text
GIVEN    A run of this skill in which the known failure mode is present: IMPLEMENTATION MIRRORING
WHEN     the agent executes `testing` and reaches the point where this failure occurs
THEN     "IMPLEMENTATION MIRRORING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Tests derived from the code assert the code equals itself."
FAIL IF  "IMPLEMENTATION MIRRORING" appears in the work and is reported as complete — specifically "Tests derived from the code assert the code equals itself."
```

## Case 7 — Detects: ASSERTION-FREE TESTS

```text
GIVEN    A run of this skill in which the known failure mode is present: ASSERTION-FREE TESTS
WHEN     the agent executes `testing` and reaches the point where this failure occurs
THEN     "ASSERTION-FREE TESTS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "It didn't throw" is not a property."
FAIL IF  "ASSERTION-FREE TESTS" appears in the work and is reported as complete — specifically "It didn't throw" is not a property."
```

## Case 8 — Detects: SNAPSHOT AS ORACLE

```text
GIVEN    A run of this skill in which the known failure mode is present: SNAPSHOT AS ORACLE
WHEN     the agent executes `testing` and reaches the point where this failure occurs
THEN     "SNAPSHOT AS ORACLE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Snapshots bless whatever the code did, including the bug."
FAIL IF  "SNAPSHOT AS ORACLE" appears in the work and is reported as complete — specifically "Snapshots bless whatever the code did, including the bug."
```

## Case 9 — Detects: FLAKE TOLERANCE

```text
GIVEN    A run of this skill in which the known failure mode is present: FLAKE TOLERANCE
WHEN     the agent executes `testing` and reaches the point where this failure occurs
THEN     "FLAKE TOLERANCE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Re-running until green hides real concurrency defects."
FAIL IF  "FLAKE TOLERANCE" appears in the work and is reported as complete — specifically "Re-running until green hides real concurrency defects."
```

## Case 10 — Detects: OVER-MOCKING

```text
GIVEN    A run of this skill in which the known failure mode is present: OVER-MOCKING
WHEN     the agent executes `testing` and reaches the point where this failure occurs
THEN     "OVER-MOCKING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Mocking so much that the test proves the mock, not the system."
FAIL IF  "OVER-MOCKING" appears in the work and is reported as complete — specifically "Mocking so much that the test proves the mock, not the system."
```

## Case 11 — Detects: E2E GRAVITY

```text
GIVEN    A run of this skill in which the known failure mode is present: E2E GRAVITY
WHEN     the agent executes `testing` and reaches the point where this failure occurs
THEN     "E2E GRAVITY" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Everything tested at the top: slow, flaky, uninformative failures."
FAIL IF  "E2E GRAVITY" appears in the work and is reported as complete — specifically "Everything tested at the top: slow, flaky, uninformative failures."
```

## Case 12 — Detects: TESTS NOT REVIEWED

```text
GIVEN    A run of this skill in which the known failure mode is present: TESTS NOT REVIEWED
WHEN     the agent executes `testing` and reaches the point where this failure occurs
THEN     "TESTS NOT REVIEWED" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Production code reviewed carefully; tests merged unread."
FAIL IF  "TESTS NOT REVIEWED" appears in the work and is reported as complete — specifically "Production code reviewed carefully; tests merged unread."
```

## Case 13 — Detects: COVERAGE THEATRE

```text
GIVEN    A run of this skill in which the known failure mode is present: COVERAGE THEATRE
WHEN     the agent executes `testing` and reaches the point where this failure occurs
THEN     "COVERAGE THEATRE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "High line coverage, no boundary or error-path coverage."
FAIL IF  "COVERAGE THEATRE" appears in the work and is reported as complete — specifically "High line coverage, no boundary or error-path coverage."
```

## Case 14 — Detects: SINGLE-RUN EVALS

```text
GIVEN    A run of this skill in which the known failure mode is present: SINGLE-RUN EVALS
WHEN     the agent executes `testing` and reaches the point where this failure occurs
THEN     "SINGLE-RUN EVALS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "One sample of a stochastic system treated as a result."
FAIL IF  "SINGLE-RUN EVALS" appears in the work and is reported as complete — specifically "One sample of a stochastic system treated as a result."
```

## Case 15 — Detects: JUDGE UNVALIDATED

```text
GIVEN    A run of this skill in which the known failure mode is present: JUDGE UNVALIDATED
WHEN     the agent executes `testing` and reaches the point where this failure occurs
THEN     "JUDGE UNVALIDATED" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "An LLM judge scoring outputs it was never calibrated against."
FAIL IF  "JUDGE UNVALIDATED" appears in the work and is reported as complete — specifically "An LLM judge scoring outputs it was never calibrated against."
```

## Case 16 — Avoids: `expect(true).toBe(true)` and its many disguises

```text
GIVEN    A situation that invites the anti-pattern "`expect(true).toBe(true)` and its many disguises"
WHEN     the agent applies `testing` in that situation
THEN     "`expect(true).toBe(true)` and its many disguises" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`expect(true).toBe(true)` and its many disguises" appears in the output; or it is absent by accident, with nothing in `testing` having ruled it out
```

## Case 17 — Avoids: A test that fails only when run after another test

```text
GIVEN    A situation that invites the anti-pattern "A test that fails only when run after another test"
WHEN     the agent applies `testing` in that situation
THEN     "A test that fails only when run after another test" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A test that fails only when run after another test" appears in the output; or it is absent by accident, with nothing in `testing` having ruled it out
```

## Case 18 — Avoids: Mocking the database and then being surprised by a SQL error in production

```text
GIVEN    A situation that invites the anti-pattern "Mocking the database and then being surprised by a SQL error in production"
WHEN     the agent applies `testing` in that situation
THEN     "Mocking the database and then being surprised by a SQL error in production" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Mocking the database and then being surprised by a SQL error in production" appears in the output; or it is absent by accident, with nothing in `testing` having ruled it out
```

## Case 19 — Avoids: Sleeping instead of waiting for a condition

```text
GIVEN    A situation that invites the anti-pattern "Sleeping instead of waiting for a condition"
WHEN     the agent applies `testing` in that situation
THEN     "Sleeping instead of waiting for a condition" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Sleeping instead of waiting for a condition" appears in the output; or it is absent by accident, with nothing in `testing` having ruled it out
```

## Case 20 — Avoids: Snapshot-testing a timestamp

```text
GIVEN    A situation that invites the anti-pattern "Snapshot-testing a timestamp"
WHEN     the agent applies `testing` in that situation
THEN     "Snapshot-testing a timestamp" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Snapshot-testing a timestamp" appears in the output; or it is absent by accident, with nothing in `testing` having ruled it out
```

## Case 21 — Avoids: Testing the framework: "does React render a div"

```text
GIVEN    A situation that invites the anti-pattern "Testing the framework: "does React render a div"
WHEN     the agent applies `testing` in that situation
THEN     "Testing the framework: "does React render a div" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Testing the framework: "does React render a div" appears in the output; or it is absent by accident, with nothing in `testing` having ruled it out
```

## Case 22 — Avoids: One E2E test covering fourteen assertions so nobody can tell what broke

```text
GIVEN    A situation that invites the anti-pattern "One E2E test covering fourteen assertions so nobody can tell what broke"
WHEN     the agent applies `testing` in that situation
THEN     "One E2E test covering fourteen assertions so nobody can tell what broke" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "One E2E test covering fourteen assertions so nobody can tell what broke" appears in the output; or it is absent by accident, with nothing in `testing` having ruled it out
```

## Case 23 — Avoids: Running an agent eval once and reporting the number

```text
GIVEN    A situation that invites the anti-pattern "Running an agent eval once and reporting the number"
WHEN     the agent applies `testing` in that situation
THEN     "Running an agent eval once and reporting the number" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Running an agent eval once and reporting the number" appears in the output; or it is absent by accident, with nothing in `testing` having ruled it out
```
