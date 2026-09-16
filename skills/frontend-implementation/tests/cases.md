# Test cases — `frontend-implementation`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Turn an approved design into code that stays correct under real content, real networks and real devices. This skill assumes the design exists — if it does not, run [`frontend-design`](../frontend-design/SKILL.md) first. …
WHEN     the agent selects and executes the `frontend-implementation` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: Producing the visual design itself — frontend-design

```text
GIVEN    A task that looks like a match but is the excluded case: Producing the visual design itself — frontend-design
WHEN     the agent considers the `frontend-implementation` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: Defining the token/component system — design-systems

```text
GIVEN    A task that looks like a match but is the excluded case: Defining the token/component system — design-systems
WHEN     the agent considers the `frontend-implementation` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: Backend concerns except at the contract boundary — see api-design / ba…

```text
GIVEN    A task that looks like a match but is the excluded case: Backend concerns except at the contract boundary — see api-design / backend-engineering
WHEN     the agent considers the `frontend-implementation` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: `useEffect(() => { fetch(...) }, [])` with no cache, abort or error ha…

```text
GIVEN    A situation that invites the anti-pattern: `useEffect(() => { fetch(...) }, [])` with no cache, abort or error handling
WHEN     the agent applies `frontend-implementation`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: A modal built from a `<div>` with `onClick` on the backdrop

```text
GIVEN    A situation that invites the anti-pattern: A modal built from a `<div>` with `onClick` on the backdrop
WHEN     the agent applies `frontend-implementation`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
