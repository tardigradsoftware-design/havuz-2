# Test cases — `code-review`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Improve the change **and** the codebase's long-term health, while transferring understanding to a second person. Review is not gatekeeping and not style enforcement — machines enforce style. A reviewer's unique value is …
WHEN     the agent selects and executes the `code-review` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: To relitigate an agreed architectural decision — that is an ADR conver…

```text
GIVEN    A task that looks like a match but is the excluded case: To relitigate an agreed architectural decision — that is an ADR conversation
WHEN     the agent considers the `code-review` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: To enforce formatting, naming style or import order — automate it

```text
GIVEN    A task that looks like a match but is the excluded case: To enforce formatting, naming style or import order — automate it
WHEN     the agent considers the `code-review` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: On a diff so large it cannot be reviewed properly: ask for it to be sp…

```text
GIVEN    A task that looks like a match but is the excluded case: On a diff so large it cannot be reviewed properly: ask for it to be split first
WHEN     the agent considers the `code-review` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: "LGTM" with no comments on a 1500-line diff

```text
GIVEN    A situation that invites the anti-pattern: "LGTM" with no comments on a 1500-line diff
WHEN     the agent applies `code-review`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: `try { … } catch (e) {}` approved because it "handles errors"

```text
GIVEN    A situation that invites the anti-pattern: `try { … } catch (e) {}` approved because it "handles errors"
WHEN     the agent applies `code-review`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
