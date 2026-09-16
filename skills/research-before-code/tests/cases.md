# Test cases — `research-before-code`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Stop the agent from treating its training data as a sufficient specification. The default failure is not laziness, it is confidence: an agent that has seen a thousand `next-auth` examples will write a plausible authentic…
WHEN     the agent selects and executes the `research-before-code` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: A one-line typo fix or a rename with compiler verification

```text
GIVEN    A task that looks like a match but is the excluded case: A one-line typo fix or a rename with compiler verification
WHEN     the agent considers the `research-before-code` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: Purely local refactoring whose correctness is proved by the existing t…

```text
GIVEN    A task that looks like a match but is the excluded case: Purely local refactoring whose correctness is proved by the existing test suite
WHEN     the agent considers the `research-before-code` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: Throwaway spikes explicitly labelled as disposable (but say so in the …

```text
GIVEN    A task that looks like a match but is the excluded case: Throwaway spikes explicitly labelled as disposable (but say so in the output)
WHEN     the agent considers the `research-before-code` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: "I'll use X because it's popular" with no source, no version, no licen…

```text
GIVEN    A situation that invites the anti-pattern: "I'll use X because it's popular" with no source, no version, no license check
WHEN     the agent applies `research-before-code`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: Researching the framework but not the version's breaking changes

```text
GIVEN    A situation that invites the anti-pattern: Researching the framework but not the version's breaking changes
WHEN     the agent applies `research-before-code`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
