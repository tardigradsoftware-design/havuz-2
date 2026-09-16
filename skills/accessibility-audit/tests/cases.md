# Test cases — `accessibility-audit`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Establish, with evidence, whether people using assistive technology can complete the actual tasks on a page — and produce a remediation list ordered by the barrier's severity, not by how easy it is to fix. **Automated to…
WHEN     the agent selects and executes the `accessibility-audit` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: As the only accessibility activity — designing accessibly beats auditi…

```text
GIVEN    A task that looks like a match but is the excluded case: As the only accessibility activity — designing accessibly beats auditing later
WHEN     the agent considers the `accessibility-audit` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: On a prototype with no users (but keep the token-level decisions corre…

```text
GIVEN    A task that looks like a match but is the excluded case: On a prototype with no users (but keep the token-level decisions correct anyway)
WHEN     the agent considers the `accessibility-audit` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: To produce a compliance badge without testing real tasks

```text
GIVEN    A task that looks like a match but is the excluded case: To produce a compliance badge without testing real tasks
WHEN     the agent considers the `accessibility-audit` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: "We ran Lighthouse and got 100"

```text
GIVEN    A situation that invites the anti-pattern: "We ran Lighthouse and got 100"
WHEN     the agent applies `accessibility-audit`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: `aria-label="button"` on an unlabelled icon control

```text
GIVEN    A situation that invites the anti-pattern: `aria-label="button"` on an unlabelled icon control
WHEN     the agent applies `accessibility-audit`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
