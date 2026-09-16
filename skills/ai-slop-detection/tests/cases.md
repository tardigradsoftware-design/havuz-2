# Test cases — `ai-slop-detection`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Give an agent a **falsifiable vocabulary** for "this looks AI-generated", and a mechanical path from detection to fix. "Slop" is not a taste judgement. It is a set of measurable symptoms that appear when an interface is …
WHEN     the agent selects and executes the `ai-slop-detection` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: Internal tools where utility is the only requirement — say so and move…

```text
GIVEN    A task that looks like a match but is the excluded case: Internal tools where utility is the only requirement — say so and move on
WHEN     the agent considers the `ai-slop-detection` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: Deliberately brutalist, maximalist or expressive designs: apply the cr…

```text
GIVEN    A task that looks like a match but is the excluded case: Deliberately brutalist, maximalist or expressive designs: apply the craft checks
WHEN     the agent considers the `ai-slop-detection` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: As a substitute for accessibility-audit — this skill catches visual sm…

```text
GIVEN    A task that looks like a match but is the excluded case: As a substitute for accessibility-audit — this skill catches visual smell, not WCAG failures
WHEN     the agent considers the `ai-slop-detection` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: Adding a gradient to "make it less flat"

```text
GIVEN    A situation that invites the anti-pattern: Adding a gradient to "make it less flat"
WHEN     the agent applies `ai-slop-detection`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: Adding a blurred orb behind the hero for "depth"

```text
GIVEN    A situation that invites the anti-pattern: Adding a blurred orb behind the hero for "depth"
WHEN     the agent applies `ai-slop-detection`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
