# Test cases — `database-design`

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
GIVEN    A task inside this skill's stated purpose: Design a schema where **the database prevents the bad state**, queries are fast at the volume you will actually reach, and changes can be applied and rolled back without downtime.
WHEN     the agent executes `database-design` end to end on that task
THEN     and before delivery these specific conditions hold: "Read patterns listed with selectivity and expected volume before indexing"; "EXPLAIN ANALYZE run on production-scale data for every hot query"; "Vector search built on a relational source of truth with filters and re-ranking"
FAIL IF  "Read patterns listed with selectivity and expected volume before indexing" is false, or "Vector search built on a relational source of truth with filters and re-ranking" is false, or "EXPLAIN ANALYZE run on production-scale data for every hot query" is false
```

## Case 2 — Declines: A local cache or scratch file — use the simplest store that works

```text
GIVEN    A task that looks like a match but is this skill's excluded case: A local cache or scratch file — use the simplest store that works
WHEN     the agent considers `database-design` for that task
THEN     the skill is not selected, because this task is the excluded case "A local cache or scratch file — use the simplest store that works", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "A local cache or scratch file — use the simplest store that works"; or `database-design` is declined without naming that exclusion
```

## Case 3 — Declines: Tuning a query whose real problem is an N+1 in application code

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Tuning a query whose real problem is an N+1 in application code
WHEN     the agent considers `database-design` for that task
THEN     the skill is not selected, because this task is the excluded case "Tuning a query whose real problem is an N+1 in application code", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Tuning a query whose real problem is an N+1 in application code"; or `database-design` is declined without naming that exclusion
```

## Case 4 — Detects: CONSTRAINT-FREE SCHEMA

```text
GIVEN    A run of this skill in which the known failure mode is present: CONSTRAINT-FREE SCHEMA
WHEN     the agent executes `database-design` and reaches the point where this failure occurs
THEN     "CONSTRAINT-FREE SCHEMA" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Integrity lives in application code and is bypassed by the second writer."
FAIL IF  "CONSTRAINT-FREE SCHEMA" appears in the work and is reported as complete — specifically "Integrity lives in application code and is bypassed by the second writer."
```

## Case 5 — Detects: FLOAT MONEY

```text
GIVEN    A run of this skill in which the known failure mode is present: FLOAT MONEY
WHEN     the agent executes `database-design` and reaches the point where this failure occurs
THEN     "FLOAT MONEY" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Rounding errors in financial data. Never."
FAIL IF  "FLOAT MONEY" appears in the work and is reported as complete — specifically "Rounding errors in financial data. Never."
```

## Case 6 — Detects: TIMESTAMP WITHOUT TZ

```text
GIVEN    A run of this skill in which the known failure mode is present: TIMESTAMP WITHOUT TZ
WHEN     the agent executes `database-design` and reaches the point where this failure occurs
THEN     "TIMESTAMP WITHOUT TZ" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Ambiguous instants across DST and deployments."
FAIL IF  "TIMESTAMP WITHOUT TZ" appears in the work and is reported as complete — specifically "Ambiguous instants across DST and deployments."
```

## Case 7 — Detects: MISSING FK

```text
GIVEN    A run of this skill in which the known failure mode is present: MISSING FK
WHEN     the agent executes `database-design` and reaches the point where this failure occurs
THEN     "MISSING FK" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Orphan rows discovered during a report, months later."
FAIL IF  "MISSING FK" appears in the work and is reported as complete — specifically "Orphan rows discovered during a report, months later."
```

## Case 8 — Detects: INDEX GUESSWORK

```text
GIVEN    A run of this skill in which the known failure mode is present: INDEX GUESSWORK
WHEN     the agent executes `database-design` and reaches the point where this failure occurs
THEN     "INDEX GUESSWORK" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Indexes added for hypothetical queries; the real query still scans."
FAIL IF  "INDEX GUESSWORK" appears in the work and is reported as complete — specifically "Indexes added for hypothetical queries; the real query still scans."
```

## Case 9 — Detects: PLAN ON TINY DATA

```text
GIVEN    A run of this skill in which the known failure mode is present: PLAN ON TINY DATA
WHEN     the agent executes `database-design` and reaches the point where this failure occurs
THEN     "PLAN ON TINY DATA" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Performance verified on a development database of 500 rows."
FAIL IF  "PLAN ON TINY DATA" appears in the work and is reported as complete — specifically "Performance verified on a development database of 500 rows."
```

## Case 10 — Detects: OFFSET PAGINATION

```text
GIVEN    A run of this skill in which the known failure mode is present: OFFSET PAGINATION
WHEN     the agent executes `database-design` and reaches the point where this failure occurs
THEN     "OFFSET PAGINATION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Multi-second deep pages and duplicate rows under concurrent writes."
FAIL IF  "OFFSET PAGINATION" appears in the work and is reported as complete — specifically "Multi-second deep pages and duplicate rows under concurrent writes."
```

## Case 11 — Detects: LONG-RUNNING TRANSACTION

```text
GIVEN    A run of this skill in which the known failure mode is present: LONG-RUNNING TRANSACTION
WHEN     the agent executes `database-design` and reaches the point where this failure occurs
THEN     "LONG-RUNNING TRANSACTION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Locks held across an HTTP call; the whole table stalls."
FAIL IF  "LONG-RUNNING TRANSACTION" appears in the work and is reported as complete — specifically "Locks held across an HTTP call; the whole table stalls."
```

## Case 12 — Detects: SOFT DELETE EVERYWHERE

```text
GIVEN    A run of this skill in which the known failure mode is present: SOFT DELETE EVERYWHERE
WHEN     the agent executes `database-design` and reaches the point where this failure occurs
THEN     "SOFT DELETE EVERYWHERE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Every query needs a filter somebody will forget once."
FAIL IF  "SOFT DELETE EVERYWHERE" appears in the work and is reported as complete — specifically "Every query needs a filter somebody will forget once."
```

## Case 13 — Detects: IRREVERSIBLE MIGRATION

```text
GIVEN    A run of this skill in which the known failure mode is present: IRREVERSIBLE MIGRATION
WHEN     the agent executes `database-design` and reaches the point where this failure occurs
THEN     "IRREVERSIBLE MIGRATION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "No way back after a failed deploy."
FAIL IF  "IRREVERSIBLE MIGRATION" appears in the work and is reported as complete — specifically "No way back after a failed deploy."
```

## Case 14 — Detects: SHARED-TABLE TENANCY

```text
GIVEN    A run of this skill in which the known failure mode is present: SHARED-TABLE TENANCY
WHEN     the agent executes `database-design` and reaches the point where this failure occurs
THEN     "SHARED-TABLE TENANCY" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "No RLS; one missing WHERE clause leaks a customer's data."
FAIL IF  "SHARED-TABLE TENANCY" appears in the work and is reported as complete — specifically "No RLS; one missing WHERE clause leaks a customer's data."
```

## Case 15 — Detects: JSONB AS A SCHEMA

```text
GIVEN    A run of this skill in which the known failure mode is present: JSONB AS A SCHEMA
WHEN     the agent executes `database-design` and reaches the point where this failure occurs
THEN     "JSONB AS A SCHEMA" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Unqueryable, unconstrainable, undocumented data at the core."
FAIL IF  "JSONB AS A SCHEMA" appears in the work and is reported as complete — specifically "Unqueryable, unconstrainable, undocumented data at the core."
```

## Case 16 — Avoids: `price FLOAT`

```text
GIVEN    A situation that invites the anti-pattern "`price FLOAT`"
WHEN     the agent applies `database-design` in that situation
THEN     "`price FLOAT`" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`price FLOAT`" appears in the output; or it is absent by accident, with nothing in `database-design` having ruled it out
```

## Case 17 — Avoids: `created_at TIMESTAMP` with no time zone

```text
GIVEN    A situation that invites the anti-pattern "`created_at TIMESTAMP` with no time zone"
WHEN     the agent applies `database-design` in that situation
THEN     "`created_at TIMESTAMP` with no time zone" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`created_at TIMESTAMP` with no time zone" appears in the output; or it is absent by accident, with nothing in `database-design` having ruled it out
```

## Case 18 — Avoids: A uniqueness rule enforced only by `SELECT … then INSERT`

```text
GIVEN    A situation that invites the anti-pattern "A uniqueness rule enforced only by `SELECT … then INSERT`"
WHEN     the agent applies `database-design` in that situation
THEN     "A uniqueness rule enforced only by `SELECT … then INSERT`" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A uniqueness rule enforced only by `SELECT … then INSERT`" appears in the output; or it is absent by accident, with nothing in `database-design` having ruled it out
```

## Case 19 — Avoids: `ORDER BY created_at LIMIT 50 OFFSET 100000`

```text
GIVEN    A situation that invites the anti-pattern "`ORDER BY created_at LIMIT 50 OFFSET 100000`"
WHEN     the agent applies `database-design` in that situation
THEN     "`ORDER BY created_at LIMIT 50 OFFSET 100000`" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`ORDER BY created_at LIMIT 50 OFFSET 100000`" appears in the output; or it is absent by accident, with nothing in `database-design` having ruled it out
```

## Case 20 — Avoids: An HTTP call inside `BEGIN … COMMIT`

```text
GIVEN    A situation that invites the anti-pattern "An HTTP call inside `BEGIN … COMMIT`"
WHEN     the agent applies `database-design` in that situation
THEN     "An HTTP call inside `BEGIN … COMMIT`" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "An HTTP call inside `BEGIN … COMMIT`" appears in the output; or it is absent by accident, with nothing in `database-design` having ruled it out
```

## Case 21 — Avoids: `tenant_id` in the table but no row-level security

```text
GIVEN    A situation that invites the anti-pattern "`tenant_id` in the table but no row-level security"
WHEN     the agent applies `database-design` in that situation
THEN     "`tenant_id` in the table but no row-level security" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`tenant_id` in the table but no row-level security" appears in the output; or it is absent by accident, with nothing in `database-design` having ruled it out
```

## Case 22 — Avoids: Adding an index because a query felt slow, without reading the plan

```text
GIVEN    A situation that invites the anti-pattern "Adding an index because a query felt slow, without reading the plan"
WHEN     the agent applies `database-design` in that situation
THEN     "Adding an index because a query felt slow, without reading the plan" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Adding an index because a query felt slow, without reading the plan" appears in the output; or it is absent by accident, with nothing in `database-design` having ruled it out
```

## Case 23 — Avoids: A migration that drops a column in the same release that stops writing it

```text
GIVEN    A situation that invites the anti-pattern "A migration that drops a column in the same release that stops writing it"
WHEN     the agent applies `database-design` in that situation
THEN     "A migration that drops a column in the same release that stops writing it" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A migration that drops a column in the same release that stops writing it" appears in the output; or it is absent by accident, with nothing in `database-design` having ruled it out
```

## Case 24 — Avoids: Storing the whole domain model in one JSONB column

```text
GIVEN    A situation that invites the anti-pattern "Storing the whole domain model in one JSONB column"
WHEN     the agent applies `database-design` in that situation
THEN     "Storing the whole domain model in one JSONB column" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Storing the whole domain model in one JSONB column" appears in the output; or it is absent by accident, with nothing in `database-design` having ruled it out
```
