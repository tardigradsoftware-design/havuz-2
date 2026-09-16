# Test cases — `browser-testing`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Prove that a **user can complete a task** in a real browser, and keep that proof stable as the implementation changes. Browser tests are the most expensive and most brittle level of the pyramid — so they must be few, cri…
WHEN     the agent selects and executes the `browser-testing` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: Business logic that can be tested as a unit — 10× faster and 10× more …

```text
GIVEN    A task that looks like a match but is the excluded case: Business logic that can be tested as a unit — 10× faster and 10× more informative
WHEN     the agent considers the `browser-testing` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: API contract checks — test the contract directly, not through a browse…

```text
GIVEN    A task that looks like a match but is the excluded case: API contract checks — test the contract directly, not through a browser
WHEN     the agent considers the `browser-testing` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: Exhaustive coverage of every page and every field

```text
GIVEN    A task that looks like a match but is the excluded case: Exhaustive coverage of every page and every field
WHEN     the agent considers the `browser-testing` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: `await page.waitForTimeout(3000)`

```text
GIVEN    A situation that invites the anti-pattern: `await page.waitForTimeout(3000)`
WHEN     the agent applies `browser-testing`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: `page.locator('.css-1a2b3c >> nth=2')`

```text
GIVEN    A situation that invites the anti-pattern: `page.locator('.css-1a2b3c >> nth=2')`
WHEN     the agent applies `browser-testing`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
