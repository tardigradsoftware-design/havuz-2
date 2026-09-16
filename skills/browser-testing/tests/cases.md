# Test cases — `browser-testing`

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
GIVEN    A task inside this skill's stated purpose: Prove that a **user can complete a task** in a real browser, and keep that proof stable as the implementation changes. Browser tests are the most expensive and most brittle level of the pyramid — so they must be few, critical,
WHEN     the agent executes `browser-testing` end to end on that task
THEN     and before delivery these specific conditions hold: "Journey list ranked and bounded (5–15); everything else tested at a lower level"; "Assertions on user-observable outcomes and the side effects that matter"; "For agent-driven runs: bounded steps/time/cost/origins, logged and attributable,"
FAIL IF  "Journey list ranked and bounded (5–15); everything else tested at a lower level" is false, or "For agent-driven runs: bounded steps/time/cost/origins, logged and attributable," is false, or "Assertions on user-observable outcomes and the side effects that matter" is false
```

## Case 2 — Declines: Business logic that can be tested as a unit — 10× faster and 10× more…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Business logic that can be tested as a unit — 10× faster and 10× more informative
WHEN     the agent considers `browser-testing` for that task
THEN     the skill is not selected, because this task is the excluded case "Business logic that can be tested as a unit — 10× faster and 10× more informative", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Business logic that can be tested as a unit — 10× faster and 10× more informative"; or `browser-testing` is declined without naming that exclusion
```

## Case 3 — Declines: API contract checks — test the contract directly, not through a browser

```text
GIVEN    A task that looks like a match but is this skill's excluded case: API contract checks — test the contract directly, not through a browser
WHEN     the agent considers `browser-testing` for that task
THEN     the skill is not selected, because this task is the excluded case "API contract checks — test the contract directly, not through a browser", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "API contract checks — test the contract directly, not through a browser"; or `browser-testing` is declined without naming that exclusion
```

## Case 4 — Declines: Exhaustive coverage of every page and every field

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Exhaustive coverage of every page and every field
WHEN     the agent considers `browser-testing` for that task
THEN     the skill is not selected, because this task is the excluded case "Exhaustive coverage of every page and every field", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Exhaustive coverage of every page and every field"; or `browser-testing` is declined without naming that exclusion
```

## Case 5 — Declines: As the primary test level.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: As the primary test level.
WHEN     the agent considers `browser-testing` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "An E2E-heavy suite is slow, flaky and tells you that something broke without telling you what."
FAIL IF  the skill is run on a task where "As the primary test level.", and the consequence that exclusion states follows — "An E2E-heavy suite is slow, flaky and tells you that something broke without telling you what."; or `browser-testing` is declined without naming that exclusion
```

## Case 6 — Detects: SLEEP-BASED WAITS

```text
GIVEN    A run of this skill in which the known failure mode is present: SLEEP-BASED WAITS
WHEN     the agent executes `browser-testing` and reaches the point where this failure occurs
THEN     "SLEEP-BASED WAITS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Works on a fast machine, fails in CI. The classic flake."
FAIL IF  "SLEEP-BASED WAITS" appears in the work and is reported as complete — specifically "Works on a fast machine, fails in CI. The classic flake."
```

## Case 7 — Detects: FRAGILE SELECTORS

```text
GIVEN    A run of this skill in which the known failure mode is present: FRAGILE SELECTORS
WHEN     the agent executes `browser-testing` and reaches the point where this failure occurs
THEN     "FRAGILE SELECTORS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Class-name and nth-child selectors break on every styling change."
FAIL IF  "FRAGILE SELECTORS" appears in the work and is reported as complete — specifically "Class-name and nth-child selectors break on every styling change."
```

## Case 8 — Detects: SHARED MUTABLE STATE

```text
GIVEN    A run of this skill in which the known failure mode is present: SHARED MUTABLE STATE
WHEN     the agent executes `browser-testing` and reaches the point where this failure occurs
THEN     "SHARED MUTABLE STATE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Test B depends on test A's data; parallel execution breaks both."
FAIL IF  "SHARED MUTABLE STATE" appears in the work and is reported as complete — specifically "Test B depends on test A's data; parallel execution breaks both."
```

## Case 9 — Detects: UI-BASED SETUP

```text
GIVEN    A run of this skill in which the known failure mode is present: UI-BASED SETUP
WHEN     the agent executes `browser-testing` and reaches the point where this failure occurs
THEN     "UI-BASED SETUP" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Ten clicks of setup before the one behaviour under test."
FAIL IF  "UI-BASED SETUP" appears in the work and is reported as complete — specifically "Ten clicks of setup before the one behaviour under test."
```

## Case 10 — Detects: REAL THIRD PARTIES

```text
GIVEN    A run of this skill in which the known failure mode is present: REAL THIRD PARTIES
WHEN     the agent executes `browser-testing` and reaches the point where this failure occurs
THEN     "REAL THIRD PARTIES" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Tests fail because an analytics endpoint changed."
FAIL IF  "REAL THIRD PARTIES" appears in the work and is reported as complete — specifically "Tests fail because an analytics endpoint changed."
```

## Case 11 — Detects: OVER-BROAD E2E

```text
GIVEN    A run of this skill in which the known failure mode is present: OVER-BROAD E2E
WHEN     the agent executes `browser-testing` and reaches the point where this failure occurs
THEN     "OVER-BROAD E2E" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Business logic tested only through the browser: slow and uninformative."
FAIL IF  "OVER-BROAD E2E" appears in the work and is reported as complete — specifically "Business logic tested only through the browser: slow and uninformative."
```

## Case 12 — Detects: RETRY AS A FIX

```text
GIVEN    A run of this skill in which the known failure mode is present: RETRY AS A FIX
WHEN     the agent executes `browser-testing` and reaches the point where this failure occurs
THEN     "RETRY AS A FIX" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Auto-retry hiding a real concurrency defect."
FAIL IF  "RETRY AS A FIX" appears in the work and is reported as complete — specifically "Auto-retry hiding a real concurrency defect."
```

## Case 13 — Detects: SNAPSHOT-ONLY VISUALS

```text
GIVEN    A run of this skill in which the known failure mode is present: SNAPSHOT-ONLY VISUALS
WHEN     the agent executes `browser-testing` and reaches the point where this failure occurs
THEN     "SNAPSHOT-ONLY VISUALS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Pixel diffs on dynamic content; every run needs a human to bless it."
FAIL IF  "SNAPSHOT-ONLY VISUALS" appears in the work and is reported as complete — specifically "Pixel diffs on dynamic content; every run needs a human to bless it."
```

## Case 14 — Detects: NO FAILURE ARTIFACTS

```text
GIVEN    A run of this skill in which the known failure mode is present: NO FAILURE ARTIFACTS
WHEN     the agent executes `browser-testing` and reaches the point where this failure occurs
THEN     "NO FAILURE ARTIFACTS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Test failed" with no trace, screenshot or console output."
FAIL IF  "NO FAILURE ARTIFACTS" appears in the work and is reported as complete — specifically "Test failed" with no trace, screenshot or console output."
```

## Case 15 — Detects: AGENT SELF-REPORT

```text
GIVEN    A run of this skill in which the known failure mode is present: AGENT SELF-REPORT
WHEN     the agent executes `browser-testing` and reaches the point where this failure occurs
THEN     "AGENT SELF-REPORT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Believing the agent's claim that the task succeeded."
FAIL IF  "AGENT SELF-REPORT" appears in the work and is reported as complete — specifically "Believing the agent's claim that the task succeeded."
```

## Case 16 — Detects: UNBOUNDED AGENT

```text
GIVEN    A run of this skill in which the known failure mode is present: UNBOUNDED AGENT
WHEN     the agent executes `browser-testing` and reaches the point where this failure occurs
THEN     "UNBOUNDED AGENT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A browser-driving agent with no step, time or origin limit."
FAIL IF  "UNBOUNDED AGENT" appears in the work and is reported as complete — specifically "A browser-driving agent with no step, time or origin limit."
```

## Case 17 — Avoids: `await page.waitForTimeout(3000)`

```text
GIVEN    A situation that invites the anti-pattern "`await page.waitForTimeout(3000)`"
WHEN     the agent applies `browser-testing` in that situation
THEN     "`await page.waitForTimeout(3000)`" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`await page.waitForTimeout(3000)`" appears in the output; or it is absent by accident, with nothing in `browser-testing` having ruled it out
```

## Case 18 — Avoids: `page.locator('.css-1a2b3c >> nth=2')`

```text
GIVEN    A situation that invites the anti-pattern "`page.locator('.css-1a2b3c >> nth=2')`"
WHEN     the agent applies `browser-testing` in that situation
THEN     "`page.locator('.css-1a2b3c >> nth=2')`" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`page.locator('.css-1a2b3c >> nth=2')`" appears in the output; or it is absent by accident, with nothing in `browser-testing` having ruled it out
```

## Case 19 — Avoids: Clicking through signup to test a settings toggle

```text
GIVEN    A situation that invites the anti-pattern "Clicking through signup to test a settings toggle"
WHEN     the agent applies `browser-testing` in that situation
THEN     "Clicking through signup to test a settings toggle" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Clicking through signup to test a settings toggle" appears in the output; or it is absent by accident, with nothing in `browser-testing` having ruled it out
```

## Case 20 — Avoids: Hitting a live payment provider in CI

```text
GIVEN    A situation that invites the anti-pattern "Hitting a live payment provider in CI"
WHEN     the agent applies `browser-testing` in that situation
THEN     "Hitting a live payment provider in CI" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Hitting a live payment provider in CI" appears in the output; or it is absent by accident, with nothing in `browser-testing` having ruled it out
```

## Case 21 — Avoids: `retries: 5` in the config as a flake strategy

```text
GIVEN    A situation that invites the anti-pattern "`retries: 5` in the config as a flake strategy"
WHEN     the agent applies `browser-testing` in that situation
THEN     "`retries: 5` in the config as a flake strategy" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`retries: 5` in the config as a flake strategy" appears in the output; or it is absent by accident, with nothing in `browser-testing` having ruled it out
```

## Case 22 — Avoids: One test with 20 assertions across 6 pages

```text
GIVEN    A situation that invites the anti-pattern "One test with 20 assertions across 6 pages"
WHEN     the agent applies `browser-testing` in that situation
THEN     "One test with 20 assertions across 6 pages" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "One test with 20 assertions across 6 pages" appears in the output; or it is absent by accident, with nothing in `browser-testing` having ruled it out
```

## Case 23 — Avoids: Visual snapshots of a page containing the current date

```text
GIVEN    A situation that invites the anti-pattern "Visual snapshots of a page containing the current date"
WHEN     the agent applies `browser-testing` in that situation
THEN     "Visual snapshots of a page containing the current date" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Visual snapshots of a page containing the current date" appears in the output; or it is absent by accident, with nothing in `browser-testing` having ruled it out
```

## Case 24 — Avoids: Accepting "the agent said it worked" without a trace

```text
GIVEN    A situation that invites the anti-pattern "Accepting "the agent said it worked" without a trace"
WHEN     the agent applies `browser-testing` in that situation
THEN     "Accepting "the agent said it worked" without a trace" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Accepting "the agent said it worked" without a trace" appears in the output; or it is absent by accident, with nothing in `browser-testing` having ruled it out
```
