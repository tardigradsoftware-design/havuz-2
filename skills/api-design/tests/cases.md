# Test cases — `api-design`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Design an interface whose **first consumer is not its last**, and where adding capability does not break existing callers. An API is a promise made in public; the cost of a bad one is paid by everyone who integrates, for…
WHEN     the agent selects and executes the `api-design` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: Internal function signatures within one module — apply taste, not a sp…

```text
GIVEN    A task that looks like a match but is the excluded case: Internal function signatures within one module — apply taste, not a specification
WHEN     the agent considers the `api-design` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: A one-off script's CLI, unless others will automate against it

```text
GIVEN    A task that looks like a match but is the excluded case: A one-off script's CLI, unless others will automate against it
WHEN     the agent considers the `api-design` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: Where an existing platform API dictates the shape — conform to it deli…

```text
GIVEN    A task that looks like a match but is the excluded case: Where an existing platform API dictates the shape — conform to it deliberately
WHEN     the agent considers the `api-design` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: `GET /api/deleteUser?id=1`

```text
GIVEN    A situation that invites the anti-pattern: `GET /api/deleteUser?id=1`
WHEN     the agent applies `api-design`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: Returning `200 OK` with `{"error": "not found"}`

```text
GIVEN    A situation that invites the anti-pattern: Returning `200 OK` with `{"error": "not found"}`
WHEN     the agent applies `api-design`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
