# Test cases — `dont-reinvent-the-wheel`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Before writing a non-trivial component, prove that writing it is the right choice. The default should be **adopt**, and **build** should require an argument. This is not "always use a library". Hand-rolling is correct wh…
WHEN     the agent selects and executes the `dont-reinvent-the-wheel` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: Genuinely novel domain logic that has no prior art (your business rule…

```text
GIVEN    A task that looks like a match but is the excluded case: Genuinely novel domain logic that has no prior art (your business rules)
WHEN     the agent considers the `dont-reinvent-the-wheel` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: Thin glue under 30 lines where a dependency would cost more than it sa…

```text
GIVEN    A task that looks like a match but is the excluded case: Thin glue under 30 lines where a dependency would cost more than it saves
WHEN     the agent considers the `dont-reinvent-the-wheel` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: A hard constraint already rules out third-party code (air-gapped, lice…

```text
GIVEN    A task that looks like a match but is the excluded case: A hard constraint already rules out third-party code (air-gapped, licensing,
WHEN     the agent considers the `dont-reinvent-the-wheel` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: "I'll just write a quick JWT verifier" — escalate instead

```text
GIVEN    A situation that invites the anti-pattern: "I'll just write a quick JWT verifier" — escalate instead
WHEN     the agent applies `dont-reinvent-the-wheel`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: Adding lodash for one function the runtime already has

```text
GIVEN    A situation that invites the anti-pattern: Adding lodash for one function the runtime already has
WHEN     the agent applies `dont-reinvent-the-wheel`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
