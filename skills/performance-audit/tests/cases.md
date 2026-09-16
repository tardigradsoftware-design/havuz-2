# Test cases — `performance-audit`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Make a system meet a **stated budget on a stated workload for a stated population**, using measurement to decide where to spend effort. Performance work without a budget is entertainment; performance work without measure…
WHEN     the agent selects and executes the `performance-audit` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: Optimising a path nobody uses (measure traffic first — the profile dec…

```text
GIVEN    A task that looks like a match but is the excluded case: Optimising a path nobody uses (measure traffic first — the profile decides)
WHEN     the agent considers the `performance-audit` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: Micro-optimising code whose cost is dominated by a network call

```text
GIVEN    A task that looks like a match but is the excluded case: Micro-optimising code whose cost is dominated by a network call
WHEN     the agent considers the `performance-audit` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: Before correctness: a fast wrong answer is worse

```text
GIVEN    A task that looks like a match but is the excluded case: Before correctness: a fast wrong answer is worse
WHEN     the agent considers the `performance-audit` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: "The average response time is 120 ms" as the whole report

```text
GIVEN    A situation that invites the anti-pattern: "The average response time is 120 ms" as the whole report
WHEN     the agent applies `performance-audit`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: Adding a cache layer before checking whether the query has an index

```text
GIVEN    A situation that invites the anti-pattern: Adding a cache layer before checking whether the query has an index
WHEN     the agent applies `performance-audit`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
