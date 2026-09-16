# Test cases — `ai-safety-evaluation`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Establish, by measurement, what a system does when it is attacked, when it is confused, and when it is asked for something it should decline — and what it declines that it should not. Safety evaluation reports a distribu…
WHEN     the agent selects and executes the `ai-safety-evaluation` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: The system has no model-mediated behaviour

```text
GIVEN    A task that looks like a match but is the excluded case: Conventional testing applies.
WHEN     the agent considers the `ai-safety-evaluation` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: The goal is to produce working attacks against a third-party system yo…

```text
GIVEN    A task that looks like a match but is the excluded case: The goal is to produce working attacks against a third-party system you do not own or are not
WHEN     the agent considers the `ai-safety-evaluation` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: The evaluation will be reported as a safety guarantee

```text
GIVEN    A task that looks like a match but is the excluded case: It is a measurement over a sample; state the
WHEN     the agent considers the `ai-safety-evaluation` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Detects: All categories from a generic list

```text
GIVEN    A run in which the known failure mode is present — All categories from a generic list
WHEN     the agent executes `ai-safety-evaluation` and reaches the point where this failure occurs
THEN     the failure is detected by "categories do not map to this system's capabilities" and the documented response is applied: re-derive from the threat model
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 6 — Detects: No expected behaviour per case

```text
GIVEN    A run in which the known failure mode is present — No expected behaviour per case
WHEN     the agent executes `ai-safety-evaluation` and reaches the point where this failure occurs
THEN     the failure is detected by "results cannot be scored" and the documented response is applied: record refuse/comply/escalate per case before running
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 7 — Detects: Over-refusal unmeasured

```text
GIVEN    A run in which the known failure mode is present — Over-refusal unmeasured
WHEN     the agent executes `ai-safety-evaluation` and reaches the point where this failure occurs
THEN     the failure is detected by "safety looks perfect, usability collapsed" and the documented response is applied: report both rates on every run
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 8 — Avoids: A GENERIC CHECKLIST AS THE EVALUATION

```text
GIVEN    A situation that invites the anti-pattern: Categories that do not map to the system's capabilities test
WHEN     the agent applies `ai-safety-evaluation`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 9 — Avoids: SAFETY WITHOUT OVER-REFUSAL

```text
GIVEN    A situation that invites the anti-pattern: Half the measurement, and the half that hides the usable failure.
WHEN     the agent applies `ai-safety-evaluation`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
