# Test cases — `database-design`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Design a schema where **the database prevents the bad state**, queries are fast at the volume you will actually reach, and changes can be applied and rolled back without downtime. The most expensive mistake is not a slow…
WHEN     the agent selects and executes the `database-design` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: A local cache or scratch file — use the simplest store that works

```text
GIVEN    A task that looks like a match but is the excluded case: A local cache or scratch file — use the simplest store that works
WHEN     the agent considers the `database-design` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: Tuning a query whose real problem is an N+1 in application code

```text
GIVEN    A task that looks like a match but is the excluded case: Tuning a query whose real problem is an N+1 in application code
WHEN     the agent considers the `database-design` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Avoids: `created_at TIMESTAMP` with no time zone

```text
GIVEN    A situation that invites the anti-pattern: `created_at TIMESTAMP` with no time zone
WHEN     the agent applies `database-design`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
