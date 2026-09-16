# Test cases — `refactoring`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Improve the internal structure of code while its **observable behaviour is provably unchanged**. The discipline is what makes it safe: small steps, verification after each, and no behavioural change mixed in. Refactoring…
WHEN     the agent selects and executes the `refactoring` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: Without tests and without the budget to write characterisation tests f…

```text
GIVEN    A task that looks like a match but is the excluded case: Without tests and without the budget to write characterisation tests first
WHEN     the agent considers the `refactoring` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: On code about to be deleted

```text
GIVEN    A task that looks like a match but is the excluded case: On code about to be deleted
WHEN     the agent considers the `refactoring` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: As a way to avoid a difficult feature (refactoring as procrastination)

```text
GIVEN    A task that looks like a match but is the excluded case: As a way to avoid a difficult feature (refactoring as procrastination)
WHEN     the agent considers the `refactoring` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: "I refactored it" as a description of a 3,000-line diff with no tests

```text
GIVEN    A situation that invites the anti-pattern: "I refactored it" as a description of a 3,000-line diff with no tests
WHEN     the agent applies `refactoring`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: Renaming a method and changing its behaviour in the same commit

```text
GIVEN    A situation that invites the anti-pattern: Renaming a method and changing its behaviour in the same commit
WHEN     the agent applies `refactoring`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
