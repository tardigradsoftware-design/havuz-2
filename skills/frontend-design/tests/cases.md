# Test cases — `frontend-design`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Produce an interface that looks **designed** rather than **generated**. The difference is not decoration; it is that every visual property traces to a decision about the content and the user's task. The failure this skil…
WHEN     the agent selects and executes the `frontend-design` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: Implementing an already-approved design — use frontend-implementation

```text
GIVEN    A task that looks like a match but is the excluded case: Implementing an already-approved design — use frontend-implementation
WHEN     the agent considers the `frontend-design` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: Data-dense internal tooling where the answer is "use the component lib…

```text
GIVEN    A task that looks like a match but is the excluded case: Data-dense internal tooling where the answer is "use the component library defaults"
WHEN     the agent considers the `frontend-design` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: Anything where the visual system already exists and is documented — ex…

```text
GIVEN    A task that looks like a match but is the excluded case: Anything where the visual system already exists and is documented — extend it, don't redesign it
WHEN     the agent considers the `frontend-design` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: Hero + three equal cards + testimonial strip as the default answer to …

```text
GIVEN    A situation that invites the anti-pattern: Hero + three equal cards + testimonial strip as the default answer to "landing page"
WHEN     the agent applies `frontend-design`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: Gradient text on a headline

```text
GIVEN    A situation that invites the anti-pattern: Gradient text on a headline
WHEN     the agent applies `frontend-design`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
