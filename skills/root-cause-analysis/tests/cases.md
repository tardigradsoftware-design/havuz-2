# Test cases — `root-cause-analysis`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Identify the cause whose removal prevents recurrence — not the nearest thing that looked wrong. The discipline is hypothesis-driven: reproduce, predict, test, eliminate. A fix applied to a symptom produces a system that …
WHEN     the agent selects and executes the `root-cause-analysis` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: The bug is obvious, local and reproducible, and the fix is one line

```text
GIVEN    A task that looks like a match but is the excluded case: Fix it; a full analysis is
WHEN     the agent considers the `root-cause-analysis` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: Nothing can be reproduced and no telemetry exists

```text
GIVEN    A task that looks like a match but is the excluded case: Restore observability first — analysis without
WHEN     the agent considers the `root-cause-analysis` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: The goal is attribution of blame

```text
GIVEN    A task that looks like a match but is the excluded case: A blame-oriented analysis produces defensive reports and hidden
WHEN     the agent considers the `root-cause-analysis` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Detects: Fixed the symptom, it recurred

```text
GIVEN    A run in which the known failure mode is present — Fixed the symptom, it recurred
WHEN     the agent executes `root-cause-analysis` and reaches the point where this failure occurs
THEN     the failure is detected by "the reproduction still fails in a new shape" and the documented response is applied: return to step 4; the cause was not identified
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 6 — Detects: No reproduction

```text
GIVEN    A run in which the known failure mode is present — No reproduction
WHEN     the agent executes `root-cause-analysis` and reaches the point where this failure occurs
THEN     the failure is detected by "hypotheses cannot be tested" and the documented response is applied: restore observability before analysing
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 7 — Detects: One hypothesis, pursued to confirmation

```text
GIVEN    A run in which the known failure mode is present — One hypothesis, pursued to confirmation
WHEN     the agent executes `root-cause-analysis` and reaches the point where this failure occurs
THEN     the failure is detected by "no alternatives were written" and the documented response is applied: generate at least three, including an uncomfortable one
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 8 — Avoids: FIXING THE FIRST PLAUSIBLE THING

```text
GIVEN    A situation that invites the anti-pattern: The most common failure, and invisible in the diff.
WHEN     the agent applies `root-cause-analysis`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 9 — Avoids: ONE HYPOTHESIS

```text
GIVEN    A situation that invites the anti-pattern: Confirmation follows, and the cause survives.
WHEN     the agent applies `root-cause-analysis`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
