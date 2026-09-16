# Test cases — `database-optimization`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Make the database faster by finding the actual cause from measured evidence and applying the narrowest change that addresses it. Not "add an index" — which is a guess — but "this query does a sequential scan over 4M rows…
WHEN     the agent selects and executes the `database-optimization` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: Nothing has been measured

```text
GIVEN    A task that looks like a match but is the excluded case: Establish the baseline and confirm the database is the layer first — see
WHEN     the agent considers the `database-optimization` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: The slowness is in the application: N+1 queries are an application bug…

```text
GIVEN    A task that looks like a match but is the excluded case: The slowness is in the application: N+1 queries are an application bug, and the fix is the query
WHEN     the agent considers the `database-optimization` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: The dataset is empty or tiny in the test environment

```text
GIVEN    A task that looks like a match but is the excluded case: Everything is fast with no data; measure against
WHEN     the agent considers the `database-optimization` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Detects: Index added, planner ignores it

```text
GIVEN    A run in which the known failure mode is present — Index added, planner ignores it
WHEN     the agent executes `database-optimization` and reaches the point where this failure occurs
THEN     the failure is detected by "plan unchanged after the index exists" and the documented response is applied: check the predicate shape, column order, statistics and whether the table is small enough that a seq scan is correct
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 6 — Detects: Index helps reads, writes regress

```text
GIVEN    A run in which the known failure mode is present — Index helps reads, writes regress
WHEN     the agent executes `database-optimization` and reaches the point where this failure occurs
THEN     the failure is detected by "insert/update latency rose after the change" and the documented response is applied: measure the write cost; consider a partial index, or drop it and fix the query instead
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 7 — Detects: Plan good in dev, bad in production

```text
GIVEN    A run in which the known failure mode is present — Plan good in dev, bad in production
WHEN     the agent executes `database-optimization` and reaches the point where this failure occurs
THEN     the failure is detected by "different row counts, cardinality or skew" and the documented response is applied: reproduce with production-shaped data; never trust a dev plan
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 8 — Avoids: ADDING AN INDEX ON A GUESS

```text
GIVEN    A situation that invites the anti-pattern: The most common form of this work and the least effective. Read
WHEN     the agent applies `database-optimization`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 9 — Avoids: INDEXING EVERY FOREIGN KEY

```text
GIVEN    A situation that invites the anti-pattern: Some are never filtered or joined on; each is a write cost and a
WHEN     the agent applies `database-optimization`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
