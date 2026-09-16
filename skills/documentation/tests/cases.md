# Test cases — `documentation`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Answer a specific reader's specific question at the moment they have it, in a form they can act on. Documentation fails in two directions: it does not exist, or it exists and is wrong — and wrong documentation is worse t…
WHEN     the agent selects and executes the `documentation` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: To document code that should be deleted or made self-explanatory

```text
GIVEN    A task that looks like a match but is the excluded case: To document code that should be deleted or made self-explanatory
WHEN     the agent considers the `documentation` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: To produce volume: a docs site nobody reads is maintenance debt with e…

```text
GIVEN    A task that looks like a match but is the excluded case: To produce volume: a docs site nobody reads is maintenance debt with extra steps
WHEN     the agent considers the `documentation` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: As a substitute for a readable API or a good error message

```text
GIVEN    A task that looks like a match but is the excluded case: As a substitute for a readable API or a good error message
WHEN     the agent considers the `documentation` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: "Simply run the following command" — for a reader who has never seen t…

```text
GIVEN    A situation that invites the anti-pattern: "Simply run the following command" — for a reader who has never seen the tool
WHEN     the agent applies `documentation`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: A README whose first paragraph is three adjectives

```text
GIVEN    A situation that invites the anti-pattern: A README whose first paragraph is three adjectives
WHEN     the agent applies `documentation`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
