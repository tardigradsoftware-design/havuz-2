# Test cases — `testing`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Produce tests that **fail when the behaviour is wrong and for no other reason**. Coverage percentages, test counts and green CI badges are outputs of that property, not substitutes for it. Two failure modes dominate in p…
WHEN     the agent selects and executes the `testing` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: Testing framework internals or language semantics — test your use of t…

```text
GIVEN    A task that looks like a match but is the excluded case: Testing framework internals or language semantics — test your use of them
WHEN     the agent considers the `testing` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: Exhaustive getter/setter coverage to inflate a metric

```text
GIVEN    A task that looks like a match but is the excluded case: Exhaustive getter/setter coverage to inflate a metric
WHEN     the agent considers the `testing` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: Snapshot tests as the primary strategy for logic (they assert "unchang…

```text
GIVEN    A task that looks like a match but is the excluded case: Snapshot tests as the primary strategy for logic (they assert "unchanged", not "correct")
WHEN     the agent considers the `testing` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: `expect(true).toBe(true)` and its many disguises

```text
GIVEN    A situation that invites the anti-pattern: `expect(true).toBe(true)` and its many disguises
WHEN     the agent applies `testing`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: A test that fails only when run after another test

```text
GIVEN    A situation that invites the anti-pattern: A test that fails only when run after another test
WHEN     the agent applies `testing`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
