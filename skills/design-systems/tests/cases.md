# Test cases — `design-systems`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Move consistency from a review activity to a structural property. A design system is not a component library; it is the **decision layer** (tokens) plus the **implementation layer** (components) plus the **rules** for ho…
WHEN     the agent selects and executes the `design-systems` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: A single page, a prototype, a one-off landing site — use tokens lightl…

```text
GIVEN    A task that looks like a match but is the excluded case: A single page, a prototype, a one-off landing site — use tokens lightly, skip governance
WHEN     the agent considers the `design-systems` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: Before any design exists: a system codifies decisions, it does not mak…

```text
GIVEN    A task that looks like a match but is the excluded case: Before any design exists: a system codifies decisions, it does not make them
WHEN     the agent considers the `design-systems` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: As a substitute for shipping: an unpublished component nobody uses is …

```text
GIVEN    A task that looks like a match but is the excluded case: As a substitute for shipping: an unpublished component nobody uses is worse than none
WHEN     the agent considers the `design-systems` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: `--blue-500` used in a component instead of `--action-primary-bg`

```text
GIVEN    A situation that invites the anti-pattern: `--blue-500` used in a component instead of `--action-primary-bg`
WHEN     the agent applies `design-systems`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: A `<Button variant="custom" style={{...}} />` escape hatch

```text
GIVEN    A situation that invites the anti-pattern: A `<Button variant="custom" style={{...}} />` escape hatch
WHEN     the agent applies `design-systems`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
