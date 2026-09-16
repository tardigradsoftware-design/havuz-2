# Test cases — `release-engineering`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Make upgrading **predictable for the consumer**. A version number is a promise about what changed and what will not break; a changelog is the evidence; a deprecation policy is how you keep the promise while still moving.…
WHEN     the agent selects and executes the `release-engineering` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: An internal, single-consumer service with no version contract — coordi…

```text
GIVEN    A task that looks like a match but is the excluded case: An internal, single-consumer service with no version contract — coordinate directly instead
WHEN     the agent considers the `release-engineering` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: Continuous deployment of a SaaS frontend where there is no consumer-in…

```text
GIVEN    A task that looks like a match but is the excluded case: Continuous deployment of a SaaS frontend where there is no consumer-installable artifact
WHEN     the agent considers the `release-engineering` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Avoids: Bumping MINOR for a change you know will break someone

```text
GIVEN    A situation that invites the anti-pattern: Bumping MINOR for a change you know will break someone
WHEN     the agent applies `release-engineering`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 5 — Avoids: A changelog entry reading "misc improvements and bug fixes"

```text
GIVEN    A situation that invites the anti-pattern: A changelog entry reading "misc improvements and bug fixes"
WHEN     the agent applies `release-engineering`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
