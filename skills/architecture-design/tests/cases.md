# Test cases — `architecture-design`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Produce an architecture whose decisions were made explicitly, are written down, and can be argued with — rather than one assembled from defaults and framework conventions. The deliverable is not a diagram; it is a set of…
WHEN     the agent selects and executes the `architecture-design` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: The change is local and reversible — a function, a component, an inter…

```text
GIVEN    A task that looks like a match but is the excluded case: The change is local and reversible — a function, a component, an internal module boundary.
WHEN     the agent considers the `architecture-design` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: The real question is build vs adopt for one capability

```text
GIVEN    A task that looks like a match but is the excluded case: Use dont-reinvent-the-wheel and
WHEN     the agent considers the `architecture-design` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: Performance is the question and nothing has been measured

```text
GIVEN    A task that looks like a match but is the excluded case: Profile first; architecture decisions
WHEN     the agent considers the `architecture-design` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Detects: Requirements were adjectives

```text
GIVEN    A run in which the known failure mode is present — Requirements were adjectives
WHEN     the agent executes `architecture-design` and reaches the point where this failure occurs
THEN     the failure is detected by "no percentile, rate or target appears in the document" and the documented response is applied: stop and obtain numbers; do not design against "fast"
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 6 — Detects: Boundaries follow the org chart, not the data

```text
GIVEN    A run in which the known failure mode is present — Boundaries follow the org chart, not the data
WHEN     the agent executes `architecture-design` and reaches the point where this failure occurs
THEN     the failure is detected by "one entity written by three services" and the documented response is applied: re-cut along data ownership; accept the reorganisation cost
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 7 — Detects: Consistency assumed uniform

```text
GIVEN    A run in which the known failure mode is present — Consistency assumed uniform
WHEN     the agent executes `architecture-design` and reaches the point where this failure occurs
THEN     the failure is detected by ""the system is strongly consistent" applied to analytics too" and the documented response is applied: assign per data type; state staleness budgets
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 8 — Avoids: DIAGRAM-FIRST DESIGN

```text
GIVEN    A situation that invites the anti-pattern: Boxes and arrows without the decisions behind them. The diagram is the
WHEN     the agent applies `architecture-design`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 9 — Avoids: RESUME-DRIVEN ARCHITECTURE

```text
GIVEN    A situation that invites the anti-pattern: Adopting a technology because it is interesting rather than because a
WHEN     the agent applies `architecture-design`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
