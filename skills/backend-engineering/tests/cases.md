# Test cases — `backend-engineering`

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
GIVEN    A task inside this skill's stated purpose: Produce server-side code whose behaviour is **predictable under concurrency, partial failure and load**. Backend defects are rarely logic errors in the happy path;
WHEN     the agent executes `backend-engineering` end to end on that task
THEN     and before delivery these specific conditions hold: "Consistency requirements stated per operation before implementation"; "Queues: idempotent consumers, DLQ + alert, bounded concurrency, no poison loop"; "Load test run at ≥2× expected peak with an injected dependency failure"
FAIL IF  "Consistency requirements stated per operation before implementation" is false, or "Load test run at ≥2× expected peak with an injected dependency failure" is false, or "Queues: idempotent consumers, DLQ + alert, bounded concurrency, no poison loop" is false
```

## Case 2 — Declines: A single-user local script with no concurrency and no network

```text
GIVEN    A task that looks like a match but is this skill's excluded case: A single-user local script with no concurrency and no network
WHEN     the agent considers `backend-engineering` for that task
THEN     the skill is not selected, because this task is the excluded case "A single-user local script with no concurrency and no network", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "A single-user local script with no concurrency and no network"; or `backend-engineering` is declined without naming that exclusion
```

## Case 3 — Declines: Pure API contract design — see api-design

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Pure API contract design — see api-design
WHEN     the agent considers `backend-engineering` for that task
THEN     the skill is not selected, because this task is the excluded case "Pure API contract design — see api-design", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Pure API contract design — see api-design"; or `backend-engineering` is declined without naming that exclusion
```

## Case 4 — Declines: Schema and query design in depth — see database-design

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Schema and query design in depth — see database-design
WHEN     the agent considers `backend-engineering` for that task
THEN     the skill is not selected, because this task is the excluded case "Schema and query design in depth — see database-design", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Schema and query design in depth — see database-design"; or `backend-engineering` is declined without naming that exclusion
```

## Case 5 — Detects: CHECK-THEN-ACT RACE

```text
GIVEN    A run of this skill in which the known failure mode is present: CHECK-THEN-ACT RACE
WHEN     the agent executes `backend-engineering` and reaches the point where this failure occurs
THEN     "CHECK-THEN-ACT RACE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Two concurrent requests both pass the uniqueness check. Fix: a unique constraint and handle the violation."
FAIL IF  "CHECK-THEN-ACT RACE" appears in the work and is reported as complete — specifically "Two concurrent requests both pass the uniqueness check. Fix: a unique constraint and handle the violation."
```

## Case 6 — Detects: UNBOUNDED FAN-OUT

```text
GIVEN    A run of this skill in which the known failure mode is present: UNBOUNDED FAN-OUT
WHEN     the agent executes `backend-engineering` and reaches the point where this failure occurs
THEN     "UNBOUNDED FAN-OUT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "One request triggers 500 downstream calls. Fix: batch and bound."
FAIL IF  "UNBOUNDED FAN-OUT" appears in the work and is reported as complete — specifically "One request triggers 500 downstream calls. Fix: batch and bound."
```

## Case 7 — Detects: RETRY STORM

```text
GIVEN    A run of this skill in which the known failure mode is present: RETRY STORM
WHEN     the agent executes `backend-engineering` and reaches the point where this failure occurs
THEN     "RETRY STORM" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Every layer retries; a small outage becomes a 10× load event. Fix: retry budget, jitter, circuit breaking, retry only idempotent ops."
FAIL IF  "RETRY STORM" appears in the work and is reported as complete — specifically "Every layer retries; a small outage becomes a 10× load event. Fix: retry budget, jitter, circuit breaking, retry only idempotent ops."
```

## Case 8 — Detects: TIMEOUT LADDER INVERSION

```text
GIVEN    A run of this skill in which the known failure mode is present: TIMEOUT LADDER INVERSION
WHEN     the agent executes `backend-engineering` and reaches the point where this failure occurs
THEN     "TIMEOUT LADDER INVERSION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Inner timeout longer than outer → work continues after the client left."
FAIL IF  "TIMEOUT LADDER INVERSION" appears in the work and is reported as complete — specifically "Inner timeout longer than outer → work continues after the client left."
```

## Case 9 — Detects: SILENT PARTIAL FAILURE

```text
GIVEN    A run of this skill in which the known failure mode is present: SILENT PARTIAL FAILURE
WHEN     the agent executes `backend-engineering` and reaches the point where this failure occurs
THEN     "SILENT PARTIAL FAILURE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "200 returned though a downstream write failed."
FAIL IF  "SILENT PARTIAL FAILURE" appears in the work and is reported as complete — specifically "200 returned though a downstream write failed."
```

## Case 10 — Detects: LOG STARVATION

```text
GIVEN    A run of this skill in which the known failure mode is present: LOG STARVATION
WHEN     the agent executes `backend-engineering` and reaches the point where this failure occurs
THEN     "LOG STARVATION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "No request id; debugging is archaeology."
FAIL IF  "LOG STARVATION" appears in the work and is reported as complete — specifically "No request id; debugging is archaeology."
```

## Case 11 — Detects: SECRET IN LOGS

```text
GIVEN    A run of this skill in which the known failure mode is present: SECRET IN LOGS
WHEN     the agent executes `backend-engineering` and reaches the point where this failure occurs
THEN     "SECRET IN LOGS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Tokens and PII in structured logs, shipped to a third party."
FAIL IF  "SECRET IN LOGS" appears in the work and is reported as complete — specifically "Tokens and PII in structured logs, shipped to a third party."
```

## Case 12 — Detects: HEALTH CHECK LYING

```text
GIVEN    A run of this skill in which the known failure mode is present: HEALTH CHECK LYING
WHEN     the agent executes `backend-engineering` and reaches the point where this failure occurs
THEN     "HEALTH CHECK LYING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Readiness 200 while the database is unreachable."
FAIL IF  "HEALTH CHECK LYING" appears in the work and is reported as complete — specifically "Readiness 200 while the database is unreachable."
```

## Case 13 — Detects: LONG-LOCKED TRANSACTION

```text
GIVEN    A run of this skill in which the known failure mode is present: LONG-LOCKED TRANSACTION
WHEN     the agent executes `backend-engineering` and reaches the point where this failure occurs
THEN     "LONG-LOCKED TRANSACTION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A network call inside a transaction holding row locks."
FAIL IF  "LONG-LOCKED TRANSACTION" appears in the work and is reported as complete — specifically "A network call inside a transaction holding row locks."
```

## Case 14 — Detects: CONFIG DRIFT

```text
GIVEN    A run of this skill in which the known failure mode is present: CONFIG DRIFT
WHEN     the agent executes `backend-engineering` and reaches the point where this failure occurs
THEN     "CONFIG DRIFT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Behaviour differs per environment because config is not validated at boot."
FAIL IF  "CONFIG DRIFT" appears in the work and is reported as complete — specifically "Behaviour differs per environment because config is not validated at boot."
```

## Case 15 — Detects: QUEUE POISON LOOP

```text
GIVEN    A run of this skill in which the known failure mode is present: QUEUE POISON LOOP
WHEN     the agent executes `backend-engineering` and reaches the point where this failure occurs
THEN     "QUEUE POISON LOOP" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "One bad message retried forever, blocking the partition."
FAIL IF  "QUEUE POISON LOOP" appears in the work and is reported as complete — specifically "One bad message retried forever, blocking the partition."
```

## Case 16 — Avoids: `if not exists: insert` with no unique constraint

```text
GIVEN    A situation that invites the anti-pattern "`if not exists: insert` with no unique constraint"
WHEN     the agent applies `backend-engineering` in that situation
THEN     "`if not exists: insert` with no unique constraint" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`if not exists: insert` with no unique constraint" appears in the output; or it is absent by accident, with nothing in `backend-engineering` having ruled it out
```

## Case 17 — Avoids: Retrying a non-idempotent POST on timeout

```text
GIVEN    A situation that invites the anti-pattern "Retrying a non-idempotent POST on timeout"
WHEN     the agent applies `backend-engineering` in that situation
THEN     "Retrying a non-idempotent POST on timeout" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Retrying a non-idempotent POST on timeout" appears in the output; or it is absent by accident, with nothing in `backend-engineering` having ruled it out
```

## Case 18 — Avoids: A 30 s database timeout behind a 2 s client timeout

```text
GIVEN    A situation that invites the anti-pattern "A 30 s database timeout behind a 2 s client timeout"
WHEN     the agent applies `backend-engineering` in that situation
THEN     "A 30 s database timeout behind a 2 s client timeout" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A 30 s database timeout behind a 2 s client timeout" appears in the output; or it is absent by accident, with nothing in `backend-engineering` having ruled it out
```

## Case 19 — Avoids: `SELECT *` on a table with a TEXT column, unpaginated, in a loop

```text
GIVEN    A situation that invites the anti-pattern "`SELECT *` on a table with a TEXT column, unpaginated, in a loop"
WHEN     the agent applies `backend-engineering` in that situation
THEN     "`SELECT *` on a table with a TEXT column, unpaginated, in a loop" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`SELECT *` on a table with a TEXT column, unpaginated, in a loop" appears in the output; or it is absent by accident, with nothing in `backend-engineering` having ruled it out
```

## Case 20 — Avoids: Returning 200 with a partially-applied batch

```text
GIVEN    A situation that invites the anti-pattern "Returning 200 with a partially-applied batch"
WHEN     the agent applies `backend-engineering` in that situation
THEN     "Returning 200 with a partially-applied batch" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Returning 200 with a partially-applied batch" appears in the output; or it is absent by accident, with nothing in `backend-engineering` having ruled it out
```

## Case 21 — Avoids: An unbounded in-memory queue "just for now"

```text
GIVEN    A situation that invites the anti-pattern "An unbounded in-memory queue "just for now"
WHEN     the agent applies `backend-engineering` in that situation
THEN     "An unbounded in-memory queue "just for now" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "An unbounded in-memory queue "just for now" appears in the output; or it is absent by accident, with nothing in `backend-engineering` having ruled it out
```

## Case 22 — Avoids: Logging the full request body on an auth endpoint

```text
GIVEN    A situation that invites the anti-pattern "Logging the full request body on an auth endpoint"
WHEN     the agent applies `backend-engineering` in that situation
THEN     "Logging the full request body on an auth endpoint" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Logging the full request body on an auth endpoint" appears in the output; or it is absent by accident, with nothing in `backend-engineering` having ruled it out
```

## Case 23 — Avoids: A liveness probe that queries the database

```text
GIVEN    A situation that invites the anti-pattern "A liveness probe that queries the database"
WHEN     the agent applies `backend-engineering` in that situation
THEN     "A liveness probe that queries the database" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A liveness probe that queries the database" appears in the output; or it is absent by accident, with nothing in `backend-engineering` having ruled it out
```

## Case 24 — Avoids: Business rules enforced only in the frontend

```text
GIVEN    A situation that invites the anti-pattern "Business rules enforced only in the frontend"
WHEN     the agent applies `backend-engineering` in that situation
THEN     "Business rules enforced only in the frontend" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Business rules enforced only in the frontend" appears in the output; or it is absent by accident, with nothing in `backend-engineering` having ruled it out
```
