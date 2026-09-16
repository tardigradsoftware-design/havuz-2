# Test cases — `security-audit`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Find the defects that matter, in the order they matter, with a recommendation an engineer can execute today. A security audit is not a list of everything that could theoretically go wrong; it is a ranked set of **exploit…
WHEN     the agent selects and executes the `security-audit` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: As a substitute for a penetration test on a system where one is requir…

```text
GIVEN    A task that looks like a match but is the excluded case: As a substitute for a penetration test on a system where one is required
WHEN     the agent considers the `security-audit` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: On code with no attack surface (a pure local script with no inputs) — …

```text
GIVEN    A task that looks like a match but is the excluded case: On code with no attack surface (a pure local script with no inputs) — say so and skip
WHEN     the agent considers the `security-audit` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: To generate a long list of theoretical findings with no exploitability…

```text
GIVEN    A task that looks like a match but is the excluded case: To generate a long list of theoretical findings with no exploitability analysis:
WHEN     the agent considers the `security-audit` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: Client-side "admin only" rendering as an authorisation control

```text
GIVEN    A situation that invites the anti-pattern: Client-side "admin only" rendering as an authorisation control
WHEN     the agent applies `security-audit`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: `WHERE user_id = ?` present on one query and absent on its three sibli…

```text
GIVEN    A situation that invites the anti-pattern: `WHERE user_id = ?` present on one query and absent on its three siblings
WHEN     the agent applies `security-audit`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
