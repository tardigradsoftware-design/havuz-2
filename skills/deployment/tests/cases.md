# Test cases — `deployment`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Make releasing **boring, frequent and reversible**. The goal is not a successful deploy; it is a deploy process where a failure is detected in minutes, contained automatically, and rolled back in seconds — so that shippi…
WHEN     the agent selects and executes the `deployment` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: Local development iteration — optimise that loop separately (fast, hot…

```text
GIVEN    A task that looks like a match but is the excluded case: Local development iteration — optimise that loop separately (fast, hot-reloading, no gates)
WHEN     the agent considers the `deployment` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: As a substitute for a migration plan when data changes are involved (s…

```text
GIVEN    A task that looks like a match but is the excluded case: As a substitute for a migration plan when data changes are involved (see migration)
WHEN     the agent considers the `deployment` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Avoids: `docker pull app:latest` on a production host

```text
GIVEN    A situation that invites the anti-pattern: `docker pull app:latest` on a production host
WHEN     the agent applies `deployment`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 5 — Avoids: A `.env` file baked into the image

```text
GIVEN    A situation that invites the anti-pattern: A `.env` file baked into the image
WHEN     the agent applies `deployment`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
