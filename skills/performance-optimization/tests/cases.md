# Test cases — `performance-optimization`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Make a system faster by finding where the time actually goes and changing that. The discipline is the skill: measure, localise, change one thing, re-measure, keep or revert. Optimising from intuition is a net loss — it c…
WHEN     the agent selects and executes the `performance-optimization` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: Nothing has been measured

```text
GIVEN    A task that looks like a match but is the excluded case: Establish the baseline first; a complaint of "slow" is not a measurement.
WHEN     the agent considers the `performance-optimization` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: The problem is a correctness bug that manifests as slowness — a lock, …

```text
GIVEN    A task that looks like a match but is the excluded case: The problem is a correctness bug that manifests as slowness — a lock, a retry loop, a leaked
WHEN     the agent considers the `performance-optimization` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: The workload being measured is not production-shaped: empty tables, on…

```text
GIVEN    A task that looks like a match but is the excluded case: The workload being measured is not production-shaped: empty tables, one user, warm caches, a laptop.
WHEN     the agent considers the `performance-optimization` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Detects: Optimised the wrong layer

```text
GIVEN    A run in which the known failure mode is present — Optimised the wrong layer
WHEN     the agent executes `performance-optimization` and reaches the point where this failure occurs
THEN     the failure is detected by "the delta is inside the noise floor" and the documented response is applied: go back to step 4; the localisation was wrong
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 6 — Detects: Benchmark measured warmup

```text
GIVEN    A run in which the known failure mode is present — Benchmark measured warmup
WHEN     the agent executes `performance-optimization` and reaches the point where this failure occurs
THEN     the failure is detected by "the first runs dominate" and the documented response is applied: discard warmup, then measure steady state
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 7 — Detects: Improvement in the lab, not in the field

```text
GIVEN    A run in which the known failure mode is present — Improvement in the lab, not in the field
WHEN     the agent executes `performance-optimization` and reaches the point where this failure occurs
THEN     the failure is detected by "RUM percentiles unmoved" and the documented response is applied: lab conditions differ from users; re-measure on field data
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 8 — Avoids: OPTIMISING FROM A GUESS

```text
GIVEN    A situation that invites the anti-pattern: The most common failure, and invisible in the diff.
WHEN     the agent applies `performance-optimization`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 9 — Avoids: MEASURING THE AVERAGE

```text
GIVEN    A situation that invites the anti-pattern: The tail is the user experience; a good mean with a p99 at 20× is a bad
WHEN     the agent applies `performance-optimization`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
