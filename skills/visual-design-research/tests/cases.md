# Test cases — `visual-design-research`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Replace "make it look good" with a **written, defensible visual direction** derived from real references. Design quality is mostly a research problem: agents produce generic output because they skip the step where a huma…
WHEN     the agent selects and executes the `visual-design-research` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: A brand book already exists — read it, do not research around it

```text
GIVEN    A task that looks like a match but is the excluded case: A brand book already exists — read it, do not research around it
WHEN     the agent considers the `visual-design-research` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: Extending an existing product surface: research the product, not the i…

```text
GIVEN    A task that looks like a match but is the excluded case: Extending an existing product surface: research the product, not the internet
WHEN     the agent considers the `visual-design-research` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: Purely functional internal tooling

```text
GIVEN    A task that looks like a match but is the excluded case: Purely functional internal tooling
WHEN     the agent considers the `visual-design-research` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: "Let's do a dark, minimal, modern look" with no references and no reas…

```text
GIVEN    A situation that invites the anti-pattern: "Let's do a dark, minimal, modern look" with no references and no reasoning
WHEN     the agent applies `visual-design-research`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: A moodboard of 40 screenshots and no written analysis

```text
GIVEN    A situation that invites the anti-pattern: A moodboard of 40 screenshots and no written analysis
WHEN     the agent applies `visual-design-research`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
