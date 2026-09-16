# Test cases — `seo-audit`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Determine whether the pages that should be found **can be crawled, rendered, indexed and ranked**, and fix the highest-impact blocker first. Most "SEO problems" are one of four things: the page cannot be crawled, the con…
WHEN     the agent selects and executes the `seo-audit` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: An app behind authentication with no public pages — technical SEO is m…

```text
GIVEN    A task that looks like a match but is the excluded case: An app behind authentication with no public pages — technical SEO is mostly irrelevant
WHEN     the agent considers the `seo-audit` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: As a substitute for content quality: no technical fix compensates for …

```text
GIVEN    A task that looks like a match but is the excluded case: As a substitute for content quality: no technical fix compensates for a page nobody wants
WHEN     the agent considers the `seo-audit` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: To chase algorithm rumours; audit what is observable and documented

```text
GIVEN    A task that looks like a match but is the excluded case: To chase algorithm rumours; audit what is observable and documented
WHEN     the agent considers the `seo-audit` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: Recommending changes based on a ranking factor nobody can document

```text
GIVEN    A situation that invites the anti-pattern: Recommending changes based on a ranking factor nobody can document
WHEN     the agent applies `seo-audit`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: A single-page app returning the same HTML shell for every route

```text
GIVEN    A situation that invites the anti-pattern: A single-page app returning the same HTML shell for every route
WHEN     the agent applies `seo-audit`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
