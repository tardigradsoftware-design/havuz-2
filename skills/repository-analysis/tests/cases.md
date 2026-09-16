# Test cases — `repository-analysis`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Answer two questions with evidence: **how does this codebase actually work**, and **is it safe and sensible to depend on it**. The README describes intent. This skill reads the artefacts that describe reality: the lockfi…
WHEN     the agent selects and executes the `repository-analysis` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: A repository you already know well and that has not changed — reuse th…

```text
GIVEN    A task that looks like a match but is the excluded case: A repository you already know well and that has not changed — reuse the cached assessment
WHEN     the agent considers the `repository-analysis` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: Judging a project solely to satisfy a style preference

```text
GIVEN    A task that looks like a match but is the excluded case: Judging a project solely to satisfy a style preference
WHEN     the agent considers the `repository-analysis` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: As a substitute for security-audit when security is the actual questio…

```text
GIVEN    A task that looks like a match but is the excluded case: As a substitute for security-audit when security is the actual question
WHEN     the agent considers the `repository-analysis` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: "40k stars, must be good"

```text
GIVEN    A situation that invites the anti-pattern: "40k stars, must be good"
WHEN     the agent applies `repository-analysis`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: Recommending an archived project without saying it is archived

```text
GIVEN    A situation that invites the anti-pattern: Recommending an archived project without saying it is archived
WHEN     the agent applies `repository-analysis`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
