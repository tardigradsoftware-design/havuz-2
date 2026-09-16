# Test cases — `backend-engineering`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Produce server-side code whose behaviour is **predictable under concurrency, partial failure and load**. Backend defects are rarely logic errors in the happy path; they are races, retries, timeouts, unbounded queries and…
WHEN     the agent selects and executes the `backend-engineering` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: A single-user local script with no concurrency and no network

```text
GIVEN    A task that looks like a match but is the excluded case: A single-user local script with no concurrency and no network
WHEN     the agent considers the `backend-engineering` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: Pure API contract design — see api-design

```text
GIVEN    A task that looks like a match but is the excluded case: Pure API contract design — see api-design
WHEN     the agent considers the `backend-engineering` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: Schema and query design in depth — see database-design

```text
GIVEN    A task that looks like a match but is the excluded case: Schema and query design in depth — see database-design
WHEN     the agent considers the `backend-engineering` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: `if not exists: insert` with no unique constraint

```text
GIVEN    A situation that invites the anti-pattern: `if not exists: insert` with no unique constraint
WHEN     the agent applies `backend-engineering`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: Retrying a non-idempotent POST on timeout

```text
GIVEN    A situation that invites the anti-pattern: Retrying a non-idempotent POST on timeout
WHEN     the agent applies `backend-engineering`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
