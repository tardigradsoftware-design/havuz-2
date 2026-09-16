# Test cases — `migration`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Change a system that is running, has data, and has users — without a moment where it is broken. The core technique is the same for schema changes, framework upgrades, vendor switches, data moves and rewrites: **run both,…
WHEN     the agent selects and executes the `migration` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: A greenfield system with no data and no users — just change it

```text
GIVEN    A task that looks like a match but is the excluded case: A greenfield system with no data and no users — just change it
WHEN     the agent considers the `migration` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: A reversible, low-blast-radius change behind a normal deploy

```text
GIVEN    A task that looks like a match but is the excluded case: A reversible, low-blast-radius change behind a normal deploy
WHEN     the agent considers the `migration` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: When the honest answer is "delete it": removing a system is a differen…

```text
GIVEN    A task that looks like a match but is the excluded case: When the honest answer is "delete it": removing a system is a different plan
WHEN     the agent considers the `migration` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: "We'll do it Saturday at 2 a.m

```text
GIVEN    A situation that invites the anti-pattern: with the team on a call"
WHEN     the agent applies `migration`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: Dropping the old column in the same migration that stops writing it

```text
GIVEN    A situation that invites the anti-pattern: Dropping the old column in the same migration that stops writing it
WHEN     the agent applies `migration`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
