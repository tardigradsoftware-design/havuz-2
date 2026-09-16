# Test cases — `web-research`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Answer a question with an **evidence set**, not with an impression. The unit of output is a ranked, dated, cited claim list with explicit confidence and an explicit statement of what remains unknown.
WHEN     the agent selects and executes the `web-research` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: Questions answerable from the repository itself — read the code first

```text
GIVEN    A task that looks like a match but is the excluded case: Questions answerable from the repository itself — read the code first
WHEN     the agent considers the `web-research` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: Questions answerable from this knowledge base — check indexes/topics.m…

```text
GIVEN    A task that looks like a match but is the excluded case: Questions answerable from this knowledge base — check indexes/topics.md first
WHEN     the agent considers the `web-research` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: Opinion questions dressed as fact questions ("what's the best framewor…

```text
GIVEN    A task that looks like a match but is the excluded case: Opinion questions dressed as fact questions ("what's the best framework?") —
WHEN     the agent considers the `web-research` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: Citing a URL that was never fetched

```text
GIVEN    A situation that invites the anti-pattern: Citing a URL that was never fetched
WHEN     the agent applies `web-research`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: "According to the documentation" with no link and no version

```text
GIVEN    A situation that invites the anti-pattern: "According to the documentation" with no link and no version
WHEN     the agent applies `web-research`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
