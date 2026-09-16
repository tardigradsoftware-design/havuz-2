# Test cases — `competitive-analysis`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Produce a comparison that survives contact with a sceptical reader: every cell sourced, every tradeoff named, every "winner" qualified by the constraint that makes it win. The output is never "X is best". It is **"for th…
WHEN     the agent selects and executes the `competitive-analysis` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: A question with one acceptable answer already decided — that is a migr…

```text
GIVEN    A task that looks like a match but is the excluded case: A question with one acceptable answer already decided — that is a migration plan
WHEN     the agent considers the `competitive-analysis` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: Comparing things that are not substitutes (a library vs a hosted servi…

```text
GIVEN    A task that looks like a match but is the excluded case: Comparing things that are not substitutes (a library vs a hosted service vs a pattern)
WHEN     the agent considers the `competitive-analysis` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: When the deciding constraint is unknown: establish it first, or the ma…

```text
GIVEN    A task that looks like a match but is the excluded case: When the deciding constraint is unknown: establish it first, or the matrix is decoration
WHEN     the agent considers the `competitive-analysis` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: A feature matrix with ✓/✗ and no sources

```text
GIVEN    A situation that invites the anti-pattern: A feature matrix with ✓/✗ and no sources
WHEN     the agent applies `competitive-analysis`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: Quoting a vendor's "3× faster" with no workload definition

```text
GIVEN    A situation that invites the anti-pattern: Quoting a vendor's "3× faster" with no workload definition
WHEN     the agent applies `competitive-analysis`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
