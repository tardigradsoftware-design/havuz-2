# Test cases — `debugging`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Find the **root cause**, not the nearest place to put a `try`. Debugging is a search problem with a hypothesis-driven strategy; trial-and-error is the same search with no strategy, and it costs more while producing fixes…
WHEN     the agent selects and executes the `debugging` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: A known, understood defect with an agreed fix — implement it

```text
GIVEN    A task that looks like a match but is the excluded case: A known, understood defect with an agreed fix — implement it
WHEN     the agent considers the `debugging` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: A feature request described as a bug

```text
GIVEN    A task that looks like a match but is the excluded case: A feature request described as a bug
WHEN     the agent considers the `debugging` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: Cosmetic preference changes

```text
GIVEN    A task that looks like a match but is the excluded case: Cosmetic preference changes
WHEN     the agent considers the `debugging` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: `try { … } catch { /* ignore */ }`

```text
GIVEN    A situation that invites the anti-pattern: `try { … } catch { /* ignore */ }`
WHEN     the agent applies `debugging`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: Adding `await sleep(500)` to fix a race

```text
GIVEN    A situation that invites the anti-pattern: Adding `await sleep(500)` to fix a race
WHEN     the agent applies `debugging`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
