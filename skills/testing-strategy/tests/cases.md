# Test cases — `testing-strategy`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Decide what the suite must prove, and at which level each thing can be proved. The question is never "do we have tests" but "which failure modes are covered by which level" — because each level has a class of bug it is t…
WHEN     the agent selects and executes the `testing-strategy` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: A single failing test needs fixing

```text
GIVEN    A task that looks like a match but is the excluded case: That is debugging, not strategy.
WHEN     the agent considers the `testing-strategy` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: Nothing has shipped and the domain is unknown

```text
GIVEN    A task that looks like a match but is the excluded case: Write tests against what you have learned; a strategy
WHEN     the agent considers the `testing-strategy` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: The goal is a coverage number

```text
GIVEN    A task that looks like a match but is the excluded case: Coverage measures execution, not assertion, and a quota produces tests
WHEN     the agent considers the `testing-strategy` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Detects: A failure mode has no level

```text
GIVEN    A run in which the known failure mode is present — A failure mode has no level
WHEN     the agent executes `testing-strategy` and reaches the point where this failure occurs
THEN     the failure is detected by "it is absent from the mapping" and the documented response is applied: assign one, or record the acceptance with a reason
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 6 — Detects: Effort concentrated at the wrong level

```text
GIVEN    A run in which the known failure mode is present — Effort concentrated at the wrong level
WHEN     the agent executes `testing-strategy` and reaches the point where this failure occurs
THEN     the failure is detected by "e2e suite is the primary net; slow, brittle, imprecise" and the documented response is applied: move assertions down to the level that diagnoses them
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 7 — Detects: Tests coupled to call structure

```text
GIVEN    A run in which the known failure mode is present — Tests coupled to call structure
WHEN     the agent executes `testing-strategy` and reaches the point where this failure occurs
THEN     the failure is detected by "failures on correct refactors" and the documented response is applied: assert outcomes, not call counts
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 8 — Avoids: AN E2E SUITE AS THE SAFETY NET

```text
GIVEN    A situation that invites the anti-pattern: Slow, brittle, imprecise; failures need a human to diagnose, so
WHEN     the agent applies `testing-strategy`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 9 — Avoids: COVERAGE AS A TARGET

```text
GIVEN    A situation that invites the anti-pattern: A quota produces tests that execute lines without checking behaviour, which is
WHEN     the agent applies `testing-strategy`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
