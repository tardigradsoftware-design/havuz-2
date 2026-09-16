# Test cases — `seo-audit`

Every clause below is derived from this skill's own body text. Nothing here is a
generic control that would read the same for a different skill:

| Case kind | Derived from | What it asserts |
|---|---|---|
| Applies | Purpose, Workflow step titles, Quality Checklist items | the named checklist conditions hold and the named steps ran |
| Declines | each `When NOT to Use` exclusion | the exclusion is honoured and the alternative it names is used |
| Detects | each `Failure Modes` entry, with its own detection signal and response | the failure is caught by that signal and answered by that response |
| Avoids | each `Anti-Patterns` entry, with the consequence it states | the anti-pattern is absent for the reason this skill gives |

Quoted text is the skill's own wording. A case whose quoted material could be
lifted from another skill is a defect and should be reported, not relaxed.

Regenerate: `python3 scripts/generate-index/generate_skill_tests.py`
Measure distinctness: `python3 scripts/generate-index/generate_skill_tests.py --report`

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):


## Case 1 — Applies to the task it was written for

```text
GIVEN    A task inside this skill's stated purpose: Determine whether the pages that should be found **can be crawled, rendered, indexed and ranked**, and fix the highest-impact blocker first.
WHEN     the agent executes `seo-audit` end to end on that task
THEN     and before delivery these specific conditions hold: "Scope, goals, baseline and access confirmed; server logs obtained where possible"; "Layer 6 performance: Core Web Vitals at field p75, HTTPS with no mixed content,"; "Re-audit scheduled with the metrics that will show whether the fixes worked"
FAIL IF  "Scope, goals, baseline and access confirmed; server logs obtained where possible" is false, or "Re-audit scheduled with the metrics that will show whether the fixes worked" is false, or "Layer 6 performance: Core Web Vitals at field p75, HTTPS with no mixed content," is false
```

## Case 2 — Declines: An app behind authentication with no public pages — technical SEO is mostly…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: An app behind authentication with no public pages — technical SEO is mostly irrelevant
WHEN     the agent considers `seo-audit` for that task
THEN     the skill is not selected, because this task is the excluded case "An app behind authentication with no public pages — technical SEO is mostly irrelevant", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "An app behind authentication with no public pages — technical SEO is mostly irrelevant"; or `seo-audit` is declined without naming that exclusion
```

## Case 3 — Declines: As a substitute for content quality: no technical fix compensates for a page…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: As a substitute for content quality: no technical fix compensates for a page nobody wants
WHEN     the agent considers `seo-audit` for that task
THEN     the skill is not selected, because this task is the excluded case "As a substitute for content quality: no technical fix compensates for a page nobody wants", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "As a substitute for content quality: no technical fix compensates for a page nobody wants"; or `seo-audit` is declined without naming that exclusion
```

## Case 4 — Declines: To chase algorithm rumours; audit what is observable and documented

```text
GIVEN    A task that looks like a match but is this skill's excluded case: To chase algorithm rumours; audit what is observable and documented
WHEN     the agent considers `seo-audit` for that task
THEN     the skill is not selected, because this task is the excluded case "To chase algorithm rumours; audit what is observable and documented", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "To chase algorithm rumours; audit what is observable and documented"; or `seo-audit` is declined without naming that exclusion
```

## Case 5 — Detects: JS-ONLY CONTENT

```text
GIVEN    A run of this skill in which the known failure mode is present: JS-ONLY CONTENT
WHEN     the agent executes `seo-audit` and reaches the point where this failure occurs
THEN     "JS-ONLY CONTENT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Primary content absent from the served HTML. BLOCKED RENDER RESOURCES CSS/JS disallowed in robots.txt, so rendering is incomplete."
FAIL IF  "JS-ONLY CONTENT" appears in the work and is reported as complete — specifically "Primary content absent from the served HTML. BLOCKED RENDER RESOURCES CSS/JS disallowed in robots.txt, so rendering is incomplete."
```

## Case 6 — Detects: CANONICAL CONFLICTS

```text
GIVEN    A run of this skill in which the known failure mode is present: CANONICAL CONFLICTS
WHEN     the agent executes `seo-audit` and reaches the point where this failure occurs
THEN     "CANONICAL CONFLICTS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Sitemap, canonical tag, internal links and redirects disagree."
FAIL IF  "CANONICAL CONFLICTS" appears in the work and is reported as complete — specifically "Sitemap, canonical tag, internal links and redirects disagree."
```

## Case 7 — Detects: NOINDEX INVISIBLE

```text
GIVEN    A run of this skill in which the known failure mode is present: NOINDEX INVISIBLE
WHEN     the agent executes `seo-audit` and reaches the point where this failure occurs
THEN     "NOINDEX INVISIBLE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "noindex on a page whose HTML the crawler cannot fetch."
FAIL IF  "NOINDEX INVISIBLE" appears in the work and is reported as complete — specifically "noindex on a page whose HTML the crawler cannot fetch."
```

## Case 8 — Detects: REDIRECT CHAINS

```text
GIVEN    A run of this skill in which the known failure mode is present: REDIRECT CHAINS
WHEN     the agent executes `seo-audit` and reaches the point where this failure occurs
THEN     "REDIRECT CHAINS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A→B→C→D; each hop costs crawl budget and dilutes signals."
FAIL IF  "REDIRECT CHAINS" appears in the work and is reported as complete — specifically "A→B→C→D; each hop costs crawl budget and dilutes signals."
```

## Case 9 — Detects: SOFT 404S

```text
GIVEN    A run of this skill in which the known failure mode is present: SOFT 404S
WHEN     the agent executes `seo-audit` and reaches the point where this failure occurs
THEN     "SOFT 404S" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "200 responses with no content; the crawler wastes budget and distrusts the site."
FAIL IF  "SOFT 404S" appears in the work and is reported as complete — specifically "200 responses with no content; the crawler wastes budget and distrusts the site."
```

## Case 10 — Detects: DUPLICATE TITLES

```text
GIVEN    A run of this skill in which the known failure mode is present: DUPLICATE TITLES
WHEN     the agent executes `seo-audit` and reaches the point where this failure occurs
THEN     "DUPLICATE TITLES" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "One template, thousands of identical titles."
FAIL IF  "DUPLICATE TITLES" appears in the work and is reported as complete — specifically "One template, thousands of identical titles."
```

## Case 11 — Detects: INDEX BLOAT

```text
GIVEN    A run of this skill in which the known failure mode is present: INDEX BLOAT
WHEN     the agent executes `seo-audit` and reaches the point where this failure occurs
THEN     "INDEX BLOAT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Faceted navigation and parameter URLs generating endless near-duplicates."
FAIL IF  "INDEX BLOAT" appears in the work and is reported as complete — specifically "Faceted navigation and parameter URLs generating endless near-duplicates."
```

## Case 12 — Detects: HREFLANG ERRORS

```text
GIVEN    A run of this skill in which the known failure mode is present: HREFLANG ERRORS
WHEN     the agent executes `seo-audit` and reaches the point where this failure occurs
THEN     "HREFLANG ERRORS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Non-reciprocal or wrong-code annotations silently ignored."
FAIL IF  "HREFLANG ERRORS" appears in the work and is reported as complete — specifically "Non-reciprocal or wrong-code annotations silently ignored."
```

## Case 13 — Detects: STAGING INDEXED

```text
GIVEN    A run of this skill in which the known failure mode is present: STAGING INDEXED
WHEN     the agent executes `seo-audit` and reaches the point where this failure occurs
THEN     "STAGING INDEXED" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A pre-launch mirror competing with production. MIGRATION BLANKET REDIRECT Every old URL → home page; visibility lost permanently."
FAIL IF  "STAGING INDEXED" appears in the work and is reported as complete — specifically "A pre-launch mirror competing with production. MIGRATION BLANKET REDIRECT Every old URL → home page; visibility lost permanently."
```

## Case 14 — Detects: MARKUP OF INVISIBLE CONTENT

```text
GIVEN    A run of this skill in which the known failure mode is present: MARKUP OF INVISIBLE CONTENT
WHEN     the agent executes `seo-audit` and reaches the point where this failure occurs
THEN     "MARKUP OF INVISIBLE CONTENT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Structured data for content not on the page — a policy violation."
FAIL IF  "MARKUP OF INVISIBLE CONTENT" appears in the work and is reported as complete — specifically "Structured data for content not on the page — a policy violation."
```

## Case 15 — Detects: CHECKLIST WITHOUT LOGS

```text
GIVEN    A run of this skill in which the known failure mode is present: CHECKLIST WITHOUT LOGS
WHEN     the agent executes `seo-audit` and reaches the point where this failure occurs
THEN     "CHECKLIST WITHOUT LOGS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Auditing meta tags while the crawler receives 503s."
FAIL IF  "CHECKLIST WITHOUT LOGS" appears in the work and is reported as complete — specifically "Auditing meta tags while the crawler receives 503s."
```

## Case 16 — Detects: RANKING FOLKLORE

```text
GIVEN    A run of this skill in which the known failure mode is present: RANKING FOLKLORE
WHEN     the agent executes `seo-audit` and reaches the point where this failure occurs
THEN     "RANKING FOLKLORE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Acting on undocumented algorithm claims instead of observable mechanics."
FAIL IF  "RANKING FOLKLORE" appears in the work and is reported as complete — specifically "Acting on undocumented algorithm claims instead of observable mechanics."
```

## Case 17 — Avoids: Recommending changes based on a ranking factor nobody can document

```text
GIVEN    A situation that invites the anti-pattern "Recommending changes based on a ranking factor nobody can document"
WHEN     the agent applies `seo-audit` in that situation
THEN     "Recommending changes based on a ranking factor nobody can document" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Recommending changes based on a ranking factor nobody can document" appears in the output; or it is absent by accident, with nothing in `seo-audit` having ruled it out
```

## Case 18 — Avoids: A single-page app returning the same HTML shell for every route

```text
GIVEN    A situation that invites the anti-pattern "A single-page app returning the same HTML shell for every route"
WHEN     the agent applies `seo-audit` in that situation
THEN     "A single-page app returning the same HTML shell for every route" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A single-page app returning the same HTML shell for every route" appears in the output; or it is absent by accident, with nothing in `seo-audit` having ruled it out
```

## Case 19 — Avoids: `robots.txt` disallowing `/assets/` and breaking rendering

```text
GIVEN    A situation that invites the anti-pattern "`robots.txt` disallowing `/assets/` and breaking rendering"
WHEN     the agent applies `seo-audit` in that situation
THEN     "`robots.txt` disallowing `/assets/` and breaking rendering" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`robots.txt` disallowing `/assets/` and breaking rendering" appears in the output; or it is absent by accident, with nothing in `seo-audit` having ruled it out
```

## Case 20 — Avoids: Canonicalising every paginated page to page 1

```text
GIVEN    A situation that invites the anti-pattern "Canonicalising every paginated page to page 1"
WHEN     the agent applies `seo-audit` in that situation
THEN     "Canonicalising every paginated page to page 1" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Canonicalising every paginated page to page 1" appears in the output; or it is absent by accident, with nothing in `seo-audit` having ruled it out
```

## Case 21 — Avoids: Marking up an FAQ that is not on the page

```text
GIVEN    A situation that invites the anti-pattern "Marking up an FAQ that is not on the page"
WHEN     the agent applies `seo-audit` in that situation
THEN     "Marking up an FAQ that is not on the page" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Marking up an FAQ that is not on the page" appears in the output; or it is absent by accident, with nothing in `seo-audit` having ruled it out
```

## Case 22 — Avoids: Redirecting 4,000 retired URLs to the home page during a migration

```text
GIVEN    A situation that invites the anti-pattern "Redirecting 4,000 retired URLs to the home page during a migration"
WHEN     the agent applies `seo-audit` in that situation
THEN     "Redirecting 4,000 retired URLs to the home page during a migration" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Redirecting 4,000 retired URLs to the home page during a migration" appears in the output; or it is absent by accident, with nothing in `seo-audit` having ruled it out
```

## Case 23 — Avoids: Auditing titles while the origin returns 503 to the crawler half the time

```text
GIVEN    A situation that invites the anti-pattern "Auditing titles while the origin returns 503 to the crawler half the time"
WHEN     the agent applies `seo-audit` in that situation
THEN     "Auditing titles while the origin returns 503 to the crawler half the time" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Auditing titles while the origin returns 503 to the crawler half the time" appears in the output; or it is absent by accident, with nothing in `seo-audit` having ruled it out
```

## Case 24 — Avoids: Buying links or generating doorway pages as a "quick win"

```text
GIVEN    A situation that invites the anti-pattern "Buying links or generating doorway pages as a "quick win"
WHEN     the agent applies `seo-audit` in that situation
THEN     "Buying links or generating doorway pages as a "quick win" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Buying links or generating doorway pages as a "quick win" appears in the output; or it is absent by accident, with nothing in `seo-audit` having ruled it out
```

## Case 25 — Avoids: Leaving the staging subdomain indexable after launch

```text
GIVEN    A situation that invites the anti-pattern "Leaving the staging subdomain indexable after launch"
WHEN     the agent applies `seo-audit` in that situation
THEN     "Leaving the staging subdomain indexable after launch" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Leaving the staging subdomain indexable after launch" appears in the output; or it is absent by accident, with nothing in `seo-audit` having ruled it out
```
