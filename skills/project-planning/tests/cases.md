# Test cases — `project-planning`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Convert an ambiguous goal into a sequence of steps, each with an **observable completion condition**, so progress is verifiable continuously and failure is detected early rather than at the end. The two planning failures…
WHEN     the agent selects and executes the `project-planning` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: A single well-understood change — do it

```text
GIVEN    A task that looks like a match but is the excluded case: A single well-understood change — do it
WHEN     the agent considers the `project-planning` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: Genuine exploration where the goal is to learn what the problem is (ti…

```text
GIVEN    A task that looks like a match but is the excluded case: Genuine exploration where the goal is to learn what the problem is (timebox a spike instead,
WHEN     the agent considers the `project-planning` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: When the plan will be discarded: planning has a cost; spend it where s…

```text
GIVEN    A task that looks like a match but is the excluded case: When the plan will be discarded: planning has a cost; spend it where sequencing matters
WHEN     the agent considers the `project-planning` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: A Gantt chart of layers with no demonstrable milestone until the end

```text
GIVEN    A situation that invites the anti-pattern: A Gantt chart of layers with no demonstrable milestone until the end
WHEN     the agent applies `project-planning`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: "Should take about a day" with no basis, no range and no confidence

```text
GIVEN    A situation that invites the anti-pattern: "Should take about a day" with no basis, no range and no confidence
WHEN     the agent applies `project-planning`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
