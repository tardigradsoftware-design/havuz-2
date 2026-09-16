# Test cases — `data-visualization`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Answer a question about data in the shortest honest path from question to perception. A chart is an argument; the encoding choices are the rhetoric, and most "misleading chart" problems are rhetoric applied without discl…
WHEN     the agent selects and executes the `data-visualization` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: When a single number answers the question — show the number, not a cha…

```text
GIVEN    A task that looks like a match but is the excluded case: When a single number answers the question — show the number, not a chart of one point
WHEN     the agent considers the `data-visualization` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: When a table answers it better (few categories, exact values needed, c…

```text
GIVEN    A task that looks like a match but is the excluded case: When a table answers it better (few categories, exact values needed, comparison of many
WHEN     the agent considers the `data-visualization` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: Decoration: a chart whose purpose is to fill space is a slop signal (X…

```text
GIVEN    A task that looks like a match but is the excluded case: Decoration: a chart whose purpose is to fill space is a slop signal (X1/L6)
WHEN     the agent considers the `data-visualization` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: A bar chart starting at 95 instead of 0

```text
GIVEN    A situation that invites the anti-pattern: A bar chart starting at 95 instead of 0
WHEN     the agent applies `data-visualization`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
