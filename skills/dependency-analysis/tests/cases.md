# Test cases — `dependency-analysis`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Know exactly what your project depends on, what each dependency costs you, and what happens when one of them changes, is compromised, or dies. Most projects have never enumerated their transitive graph — and that graph i…
WHEN     the agent selects and executes the `dependency-analysis` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: A throwaway script with a couple of well-known dependencies

```text
GIVEN    A task that looks like a match but is the excluded case: A throwaway script with a couple of well-known dependencies
WHEN     the agent considers the `dependency-analysis` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: As a reason to remove all dependencies — zero-dependency is not automa…

```text
GIVEN    A task that looks like a match but is the excluded case: As a reason to remove all dependencies — zero-dependency is not automatically safer,
WHEN     the agent considers the `dependency-analysis` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Avoids: `npm audit` output pasted into a ticket with no triage

```text
GIVEN    A situation that invites the anti-pattern: `npm audit` output pasted into a ticket with no triage
WHEN     the agent applies `dependency-analysis`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 5 — Avoids: Depending on a git branch or a mutable tag in production

```text
GIVEN    A situation that invites the anti-pattern: Depending on a git branch or a mutable tag in production
WHEN     the agent applies `dependency-analysis`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
