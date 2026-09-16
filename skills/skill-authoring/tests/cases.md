# Test cases — `skill-authoring`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Write a skill that an agent can execute under context pressure. A skill is a procedure, not an essay: it states when to use it, when not to, what it needs, what it does, how it fails and how to know it worked — and it fi…
WHEN     the agent selects and executes the `skill-authoring` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: The content is a fact, a reference or an explanation

```text
GIVEN    A task that looks like a match but is the excluded case: That is a knowledge article, not a skill.
WHEN     the agent considers the `skill-authoring` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: The procedure has two independent halves

```text
GIVEN    A task that looks like a match but is the excluded case: That is two skills joined by requires, or a workflow.
WHEN     the agent considers the `skill-authoring` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: Nobody has performed the procedure

```text
GIVEN    A task that looks like a match but is the excluded case: Write it after doing it, or it will describe an intention.
WHEN     the agent considers the `skill-authoring` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Detects: Named for a domain

```text
GIVEN    A run in which the known failure mode is present — Named for a domain
WHEN     the agent executes `skill-authoring` and reaches the point where this failure occurs
THEN     the failure is detected by "every task in that domain matches" and the documented response is applied: rename for the procedure
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 6 — Detects: No negative case

```text
GIVEN    A run in which the known failure mode is present — No negative case
WHEN     the agent executes `skill-authoring` and reaches the point where this failure occurs
THEN     the failure is detected by "the skill is applied to lookalike situations" and the documented response is applied: write "When NOT to Use" naming them
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 7 — Detects: Body over budget

```text
GIVEN    A run in which the known failure mode is present — Body over budget
WHEN     the agent executes `skill-authoring` and reaches the point where this failure occurs
THEN     the failure is detected by "validator warns above 135% of 2500 tokens" and the documented response is applied: move lookup material into references/
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 8 — Avoids: AN ESSAY WITH A FRONTMATTER

```text
GIVEN    A situation that invites the anti-pattern: Explanatory prose an agent must interpret rather than execute.
WHEN     the agent applies `skill-authoring`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 9 — Avoids: DOMAIN-NAMED SKILLS

```text
GIVEN    A situation that invites the anti-pattern: Unselectable, because everything matches.
WHEN     the agent applies `skill-authoring`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
