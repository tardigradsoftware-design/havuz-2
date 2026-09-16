# Test cases — `database-optimization`

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
GIVEN    A task inside this skill's stated purpose: Make the database faster by finding the actual cause from measured evidence and applying the narrowest change that addresses it.
WHEN     the agent executes `database-optimization` end to end on that task
THEN     the workflow runs in its stated order — "RANK BY TOTAL TIME, NOT BY WORST CASE" through to "RECORD IT"; and before delivery these specific conditions hold: "the target query was selected by total time, not by worst case"; "at most one change was made at a time"; "the before/after plans and the delta are recorded"
FAIL IF  "the target query was selected by total time, not by worst case" is false, or "the before/after plans and the delta are recorded" is false, or the result is delivered before "RECORD IT" has run
```

## Case 2 — Declines: Nothing has been measured.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Nothing has been measured.
WHEN     the agent considers `database-optimization` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Establish the baseline and confirm the database is the layer first — see performance-optimization. Optimising a query that accounts for 4% of request time is a net loss."
FAIL IF  the skill is run on a task where "Nothing has been measured.", and the consequence that exclusion states follows — "Establish the baseline and confirm the database is the layer first — see performance-optimization."; or `database-optimization` is declined without naming that exclusion
```

## Case 3 — Declines: The slowness is in the application: N+1 queries are an application bug,

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The slowness is in the application: N+1 queries are an application bug, and the fix is the query pattern, not an index.
WHEN     the agent considers `database-optimization` for that task
THEN     the skill is not selected, because this task is the excluded case "The slowness is in the application: N+1 queries are an application bug, and the fix is the query pattern, not an index.", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "The slowness is in the application: N+1 queries are an application bug, and the fix is the query pattern, not an index."; or `database-optimization` is declined without naming that exclusion
```

## Case 4 — Declines: The dataset is empty or tiny in the test environment.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The dataset is empty or tiny in the test environment.
WHEN     the agent considers `database-optimization` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Everything is fast with no data; measure against production-shaped volume."
FAIL IF  the skill is run on a task where "The dataset is empty or tiny in the test environment.", and the consequence that exclusion states follows — "Everything is fast with no data; measure against production-shaped volume."; or `database-optimization` is declined without naming that exclusion
```

## Case 5 — Declines: The real constraint is a lock, a long transaction or connection-pool…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The real constraint is a lock, a long transaction or connection-pool exhaustion.
WHEN     the agent considers `database-optimization` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Those are concurrency problems, and an index will not touch them."
FAIL IF  the skill is run on a task where "The real constraint is a lock, a long transaction or connection-pool exhaustion.", and the consequence that exclusion states follows — "Those are concurrency problems, and an index will not touch them."; or `database-optimization` is declined without naming that exclusion
```

## Case 6 — Detects: Index added, planner ignores it

```text
GIVEN    A run of this skill in which the known failure mode is present: Index added, planner ignores it
WHEN     the agent executes `database-optimization` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "plan unchanged after the index exists" — and the response applied is the documented one: "check the predicate shape, column order, statistics and whether the table is small enough that a seq scan is correct"
FAIL IF  "Index added, planner ignores it" reaches the output because "plan unchanged after the index exists" was never checked; or it is caught but the response taken is not "check the predicate shape, column order, statistics and whether the table is small enough that a seq scan is correct"
```

## Case 7 — Detects: Index helps reads, writes regress

```text
GIVEN    A run of this skill in which the known failure mode is present: Index helps reads, writes regress
WHEN     the agent executes `database-optimization` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "insert/update latency rose after the change" — and the response applied is the documented one: "measure the write cost; consider a partial index, or drop it and fix the query instead"
FAIL IF  "Index helps reads, writes regress" reaches the output because "insert/update latency rose after the change" was never checked; or it is caught but the response taken is not "measure the write cost; consider a partial index, or drop it and fix the query instead"
```

## Case 8 — Detects: Plan good in dev, bad in production

```text
GIVEN    A run of this skill in which the known failure mode is present: Plan good in dev, bad in production
WHEN     the agent executes `database-optimization` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "different row counts, cardinality or skew" — and the response applied is the documented one: "reproduce with production-shaped data; never trust a dev plan"
FAIL IF  "Plan good in dev, bad in production" reaches the output because "different row counts, cardinality or skew" was never checked; or it is caught but the response taken is not "reproduce with production-shaped data; never trust a dev plan"
```

## Case 9 — Detects: Statistics stale after a bulk load

```text
GIVEN    A run of this skill in which the known failure mode is present: Statistics stale after a bulk load
WHEN     the agent executes `database-optimization` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "estimates far below actuals" — and the response applied is the documented one: "ANALYZE; consider autovacuum tuning for high-churn tables"
FAIL IF  "Statistics stale after a bulk load" reaches the output because "estimates far below actuals" was never checked; or it is caught but the response taken is not "ANALYZE; consider autovacuum tuning for high-churn tables"
```

## Case 10 — Detects: CONCURRENTLY left an INVALID index

```text
GIVEN    A run of this skill in which the known failure mode is present: CONCURRENTLY left an INVALID index
WHEN     the agent executes `database-optimization` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "`pg_index.indisvalid = false`" — and the response applied is the documented one: "drop and recreate; it is not used and still costs space and write time"
FAIL IF  "CONCURRENTLY left an INVALID index" reaches the output because "`pg_index.indisvalid = false`" was never checked; or it is caught but the response taken is not "drop and recreate; it is not used and still costs space and write time"
```

## Case 11 — Detects: Optimised the wrong query

```text
GIVEN    A run of this skill in which the known failure mode is present: Optimised the wrong query
WHEN     the agent executes `database-optimization` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "total time unchanged after the fix" — and the response applied is the documented one: "re-rank by total_exec_time; the worst-case query was not the expensive one"
FAIL IF  "Optimised the wrong query" reaches the output because "total time unchanged after the fix" was never checked; or it is caught but the response taken is not "re-rank by total_exec_time; the worst-case query was not the expensive one"
```

## Case 12 — Detects: Fix works, then stops

```text
GIVEN    A run of this skill in which the known failure mode is present: Fix works, then stops
WHEN     the agent executes `database-optimization` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "plan flips after a data distribution change" — and the response applied is the documented one: "pin the shape with a query rewrite rather than relying on planner luck; add a regression test with volume"
FAIL IF  "Fix works, then stops" reaches the output because "plan flips after a data distribution change" was never checked; or it is caught but the response taken is not "pin the shape with a query rewrite rather than relying on planner luck; add a regression test with volume"
```

## Case 13 — Detects: Vacuum blocked by a long transaction

```text
GIVEN    A run of this skill in which the known failure mode is present: Vacuum blocked by a long transaction
WHEN     the agent executes `database-optimization` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "table bloat grows, xmin horizon held" — and the response applied is the documented one: "set `idle_in_transaction_session_timeout`; find and kill the holder"
FAIL IF  "Vacuum blocked by a long transaction" reaches the output because "table bloat grows, xmin horizon held" was never checked; or it is caught but the response taken is not "set `idle_in_transaction_session_timeout`; find and kill the holder"
```

## Case 14 — Avoids: ADDING AN INDEX ON A GUESS

```text
GIVEN    A situation that invites the anti-pattern "ADDING AN INDEX ON A GUESS", whose stated consequence is: The most common form of this work and the least effective. Read the plan first.
WHEN     the agent applies `database-optimization` in that situation
THEN     "ADDING AN INDEX ON A GUESS" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The most common form of this work and the least effective. Read the plan first."
FAIL IF  "ADDING AN INDEX ON A GUESS" appears in the output — that is, "The most common form of this work and the least effective. Read the plan first."; or it is absent by accident, with nothing in `database-optimization` having ruled it out
```

## Case 15 — Avoids: INDEXING EVERY FOREIGN KEY

```text
GIVEN    A situation that invites the anti-pattern "INDEXING EVERY FOREIGN KEY", whose stated consequence is: Some are never filtered or joined on; each is a write cost and a vacuum cost.
WHEN     the agent applies `database-optimization` in that situation
THEN     "INDEXING EVERY FOREIGN KEY" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Some are never filtered or joined on; each is a write cost and a vacuum cost."
FAIL IF  "INDEXING EVERY FOREIGN KEY" appears in the output — that is, "Some are never filtered or joined on; each is a write cost and a vacuum cost."; or it is absent by accident, with nothing in `database-optimization` having ruled it out
```

## Case 16 — Avoids: OPTIMISING THE SLOWEST QUERY

```text
GIVEN    A situation that invites the anti-pattern "OPTIMISING THE SLOWEST QUERY", whose stated consequence is: Rank by total time. A rarely-run slow query is usually not the problem.
WHEN     the agent applies `database-optimization` in that situation
THEN     "OPTIMISING THE SLOWEST QUERY" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Rank by total time. A rarely-run slow query is usually not the problem."
FAIL IF  "OPTIMISING THE SLOWEST QUERY" appears in the output — that is, "Rank by total time. A rarely-run slow query is usually not the problem."; or it is absent by accident, with nothing in `database-optimization` having ruled it out
```

## Case 17 — Avoids: TESTING AGAINST AN EMPTY TABLE

```text
GIVEN    A situation that invites the anti-pattern "TESTING AGAINST AN EMPTY TABLE", whose stated consequence is: The planner's decisions are a function of the data.
WHEN     the agent applies `database-optimization` in that situation
THEN     "TESTING AGAINST AN EMPTY TABLE" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The planner's decisions are a function of the data."
FAIL IF  "TESTING AGAINST AN EMPTY TABLE" appears in the output — that is, "The planner's decisions are a function of the data."; or it is absent by accident, with nothing in `database-optimization` having ruled it out
```

## Case 18 — Avoids: SELECT * EVERYWHERE

```text
GIVEN    A situation that invites the anti-pattern "SELECT * EVERYWHERE", whose stated consequence is: Defeats index-only scans and pulls TOAST data unnecessarily.
WHEN     the agent applies `database-optimization` in that situation
THEN     "SELECT * EVERYWHERE" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Defeats index-only scans and pulls TOAST data unnecessarily."
FAIL IF  "SELECT * EVERYWHERE" appears in the output — that is, "Defeats index-only scans and pulls TOAST data unnecessarily."; or it is absent by accident, with nothing in `database-optimization` having ruled it out
```

## Case 19 — Avoids: OFFSET PAGINATION ON A LARGE SET

```text
GIVEN    A situation that invites the anti-pattern "OFFSET PAGINATION ON A LARGE SET", whose stated consequence is: It scans and discards. Keyset pagination is not optional at scale.
WHEN     the agent applies `database-optimization` in that situation
THEN     "OFFSET PAGINATION ON A LARGE SET" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "It scans and discards. Keyset pagination is not optional at scale."
FAIL IF  "OFFSET PAGINATION ON A LARGE SET" appears in the output — that is, "It scans and discards. Keyset pagination is not optional at scale."; or it is absent by accident, with nothing in `database-optimization` having ruled it out
```

## Case 20 — Avoids: A WRAPPER ORM QUERY NOBODY HAS READ

```text
GIVEN    A situation that invites the anti-pattern "A WRAPPER ORM QUERY NOBODY HAS READ", whose stated consequence is: The generated SQL is what runs. Log it and read it.
WHEN     the agent applies `database-optimization` in that situation
THEN     "A WRAPPER ORM QUERY NOBODY HAS READ" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The generated SQL is what runs. Log it and read it."
FAIL IF  "A WRAPPER ORM QUERY NOBODY HAS READ" appears in the output — that is, "The generated SQL is what runs. Log it and read it."; or it is absent by accident, with nothing in `database-optimization` having ruled it out
```

## Case 21 — Avoids: NON-CONCURRENT INDEX BUILDS IN PRODUCTION

```text
GIVEN    A situation that invites the anti-pattern "NON-CONCURRENT INDEX BUILDS IN PRODUCTION", whose stated consequence is: A write lock for the duration of the build is an outage.
WHEN     the agent applies `database-optimization` in that situation
THEN     "NON-CONCURRENT INDEX BUILDS IN PRODUCTION" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "A write lock for the duration of the build is an outage."
FAIL IF  "NON-CONCURRENT INDEX BUILDS IN PRODUCTION" appears in the output — that is, "A write lock for the duration of the build is an outage."; or it is absent by accident, with nothing in `database-optimization` having ruled it out
```

## Case 22 — Avoids: KEEPING A CHANGE INSIDE THE NOISE

```text
GIVEN    A situation that invites the anti-pattern "KEEPING A CHANGE INSIDE THE NOISE", whose stated consequence is: Revert it. Plausibility is not evidence.
WHEN     the agent applies `database-optimization` in that situation
THEN     "KEEPING A CHANGE INSIDE THE NOISE" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Revert it. Plausibility is not evidence."
FAIL IF  "KEEPING A CHANGE INSIDE THE NOISE" appears in the output — that is, "Revert it. Plausibility is not evidence."; or it is absent by accident, with nothing in `database-optimization` having ruled it out
```

## Case 23 — Avoids: NO RECORD OF WHY THE INDEX EXISTS

```text
GIVEN    A situation that invites the anti-pattern "NO RECORD OF WHY THE INDEX EXISTS", whose stated consequence is: It will never be removed, and nobody will know whether it still matters.
WHEN     the agent applies `database-optimization` in that situation
THEN     "NO RECORD OF WHY THE INDEX EXISTS" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "It will never be removed, and nobody will know whether it still matters."
FAIL IF  "NO RECORD OF WHY THE INDEX EXISTS" appears in the output — that is, "It will never be removed, and nobody will know whether it still matters."; or it is absent by accident, with nothing in `database-optimization` having ruled it out
```
