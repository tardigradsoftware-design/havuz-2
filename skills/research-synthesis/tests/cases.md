# Test cases — `research-synthesis`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Turn N investigations into **one answer a decision-maker can act on**, without losing the provenance of any claim or hiding any disagreement. Synthesis is not summarisation. A summary compresses what was said; a synthesi…
WHEN     the agent selects and executes the `research-synthesis` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: A single well-sourced fact — cite it directly

```text
GIVEN    A task that looks like a match but is the excluded case: A single well-sourced fact — cite it directly
WHEN     the agent considers the `research-synthesis` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: Before the research exists: synthesis without inputs produces plausibl…

```text
GIVEN    A task that looks like a match but is the excluded case: Before the research exists: synthesis without inputs produces plausible fiction
WHEN     the agent considers the `research-synthesis` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: When the decision-maker needs the raw material, not your interpretatio…

```text
GIVEN    A task that looks like a match but is the excluded case: When the decision-maker needs the raw material, not your interpretation — provide both
WHEN     the agent considers the `research-synthesis` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: "Sources suggest that…" with no named source

```text
GIVEN    A situation that invites the anti-pattern: "Sources suggest that…" with no named source
WHEN     the agent applies `research-synthesis`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: A confidence level attached to the report rather than to individual cl…

```text
GIVEN    A situation that invites the anti-pattern: A confidence level attached to the report rather than to individual claims
WHEN     the agent applies `research-synthesis`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
