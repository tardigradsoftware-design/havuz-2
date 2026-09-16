# Test cases — `evidence-validation`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Assign every claim a **confidence level backed by a checkable procedure**, and refuse to promote ungradeable material into the knowledge base. Validation is not "does this look right". It is: *what would have to be true …
WHEN     the agent selects and executes the `evidence-validation` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: Statements about this repository's own contents — read the file

```text
GIVEN    A task that looks like a match but is the excluded case: Statements about this repository's own contents — read the file
WHEN     the agent considers the `evidence-validation` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: Pure preferences ("I like this layout") — label them opinion and move …

```text
GIVEN    A task that looks like a match but is the excluded case: Pure preferences ("I like this layout") — label them opinion and move on
WHEN     the agent considers the `evidence-validation` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: Re-validating something already validated today with an unchanged sour…

```text
GIVEN    A task that looks like a match but is the excluded case: Re-validating something already validated today with an unchanged source:
WHEN     the agent considers the `evidence-validation` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: Accepting a claim because it matches what you already believed

```text
GIVEN    A situation that invites the anti-pattern: Accepting a claim because it matches what you already believed
WHEN     the agent applies `evidence-validation`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: Recording a number with no measurement method

```text
GIVEN    A situation that invites the anti-pattern: Recording a number with no measurement method
WHEN     the agent applies `evidence-validation`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
