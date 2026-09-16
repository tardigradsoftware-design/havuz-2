# Test cases — `prompt-engineering`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Change model behaviour deliberately and measurably. The skill is not writing clever instructions — it is specifying the behaviour, building a set of cases that shows whether the behaviour occurred, changing one thing, an…
WHEN     the agent selects and executes the `prompt-engineering` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: The failure is a capability limit rather than a specification problem

```text
GIVEN    A task that looks like a match but is the excluded case: If the model cannot do the
WHEN     the agent considers the `prompt-engineering` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: The failure is retrieval: the model does not have the information

```text
GIVEN    A task that looks like a match but is the excluded case: Fix the retrieval, not the prompt.
WHEN     the agent considers the `prompt-engineering` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: The output is non-deterministic and there is no evaluation set

```text
GIVEN    A task that looks like a match but is the excluded case: Build the set first; a single
WHEN     the agent considers the `prompt-engineering` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Detects: Improved the target, regressed another case

```text
GIVEN    A run in which the known failure mode is present — Improved the target, regressed another case
WHEN     the agent executes `prompt-engineering` and reaches the point where this failure occurs
THEN     the failure is detected by "full-set pass rate fell" and the documented response is applied: revert; the change was too broad — narrow it
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 6 — Detects: Improvement inside the noise floor

```text
GIVEN    A run in which the known failure mode is present — Improvement inside the noise floor
WHEN     the agent executes `prompt-engineering` and reaches the point where this failure occurs
THEN     the failure is detected by "run-to-run spread exceeds the delta" and the documented response is applied: more runs, or a bigger change; do not claim the improvement
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 7 — Detects: Works on one model, fails on another

```text
GIVEN    A run in which the known failure mode is present — Works on one model, fails on another
WHEN     the agent executes `prompt-engineering` and reaches the point where this failure occurs
THEN     the failure is detected by "no model version recorded with the prompt" and the documented response is applied: record model and version; re-measure per model
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 8 — Avoids: EDITING BY VIBE

```text
GIVEN    A situation that invites the anti-pattern: Changing a prompt because one output looked wrong, with no set and no baseline.
WHEN     the agent applies `prompt-engineering`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 9 — Avoids: ONE-EXAMPLE TUNING

```text
GIVEN    A situation that invites the anti-pattern: Optimising until a single case works, which usually breaks three others.
WHEN     the agent applies `prompt-engineering`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
