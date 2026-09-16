# Test cases — `reasoning-strategies`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Match the reasoning strategy to the structure of the task and pay for only as much of it as the task needs. The strategies differ by orders of magnitude in cost, and the popular default — always ask the model to think st…
WHEN     the agent selects and executes the `reasoning-strategies` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: The model lacks the information

```text
GIVEN    A task that looks like a match but is the excluded case: That is a retrieval problem; a strategy will not supply facts.
WHEN     the agent considers the `reasoning-strategies` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: The output format is the problem

```text
GIVEN    A task that looks like a match but is the excluded case: Fix the format with a schema and validation.
WHEN     the agent considers the `reasoning-strategies` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: The task is a single deterministic operation

```text
GIVEN    A task that looks like a match but is the excluded case: Call a function.
WHEN     the agent considers the `reasoning-strategies` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Detects: Strategy chosen by fashion

```text
GIVEN    A run in which the known failure mode is present — Strategy chosen by fashion
WHEN     the agent executes `reasoning-strategies` and reaches the point where this failure occurs
THEN     the failure is detected by "cost is high and accuracy is not" and the documented response is applied: re-measure the cheapest strategy that fits the structure
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 6 — Detects: CoT added by default

```text
GIVEN    A run in which the known failure mode is present — CoT added by default
WHEN     the agent executes `reasoning-strategies` and reaches the point where this failure occurs
THEN     the failure is detected by "neutral or negative delta on a reasoning-tuned model" and the documented response is applied: remove it; keep only measured interventions
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 7 — Detects: Chain produced, answer still wrong

```text
GIVEN    A run in which the known failure mode is present — Chain produced, answer still wrong
WHEN     the agent executes `reasoning-strategies` and reaches the point where this failure occurs
THEN     the failure is detected by "failure not localised" and the documented response is applied: find the first incorrect intermediate step
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 8 — Avoids: ALWAYS THINK STEP BY STEP

```text
GIVEN    A situation that invites the anti-pattern: The default that the evidence does not support across models and tasks.
WHEN     the agent applies `reasoning-strategies`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 9 — Avoids: REASONING INSTEAD OF RETRIEVAL

```text
GIVEN    A situation that invites the anti-pattern: Asking a model to reason its way to a fact it does not have produces
WHEN     the agent applies `reasoning-strategies`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
