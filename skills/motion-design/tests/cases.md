# Test cases — `motion-design`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Make change **legible**. Motion exists to answer three questions a static frame cannot: where did this come from, what just happened, and what is related to what. Everything else is decoration, and decoration that moves …
WHEN     the agent selects and executes the `motion-design` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: To make a page "feel alive" — that is the slop signal (M1/M3 in ai-slo…

```text
GIVEN    A task that looks like a match but is the excluded case: To make a page "feel alive" — that is the slop signal (M1/M3 in ai-slop-detection)
WHEN     the agent considers the `motion-design` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: On data that updates continuously (dashboards, logs, tickers) — motion…

```text
GIVEN    A task that looks like a match but is the excluded case: On data that updates continuously (dashboards, logs, tickers) — motion obscures the value
WHEN     the agent considers the `motion-design` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: Entrance animations on content the user came to read

```text
GIVEN    A task that looks like a match but is the excluded case: Entrance animations on content the user came to read
WHEN     the agent considers the `motion-design` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: Entrance animations on every card, staggered, on page load, for no rea…

```text
GIVEN    A situation that invites the anti-pattern: Entrance animations on every card, staggered, on page load, for no reason
WHEN     the agent applies `motion-design`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: A logo that animates on load

```text
GIVEN    A situation that invites the anti-pattern: A logo that animates on load
WHEN     the agent applies `motion-design`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
