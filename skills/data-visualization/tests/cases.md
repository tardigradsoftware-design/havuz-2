# Test cases — `data-visualization`

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
GIVEN    A task inside this skill's stated purpose: Answer a question about data in the shortest honest path from question to perception. A chart is an argument; the encoding choices are the rhetoric, and most "misleading chart" problems are rhetoric applied without disclosure.
WHEN     the agent executes `data-visualization` end to end on that task
THEN     and before delivery these specific conditions hold: "Question stated; chart type chosen from the question, not from the data shape"; "Sequential/diverging/categorical scale matched to the data type"; "No animation on routine data updates"
FAIL IF  "Question stated; chart type chosen from the question, not from the data shape" is false, or "No animation on routine data updates" is false, or "Sequential/diverging/categorical scale matched to the data type" is false
```

## Case 2 — Declines: When a single number answers the question — show the number,

```text
GIVEN    A task that looks like a match but is this skill's excluded case: When a single number answers the question — show the number, not a chart of one point
WHEN     the agent considers `data-visualization` for that task
THEN     the skill is not selected, because this task is the excluded case "When a single number answers the question — show the number, not a chart of one point", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "When a single number answers the question — show the number, not a chart of one point"; or `data-visualization` is declined without naming that exclusion
```

## Case 3 — Declines: When a table answers it better (few categories, exact values needed,

```text
GIVEN    A task that looks like a match but is this skill's excluded case: When a table answers it better (few categories, exact values needed, comparison of many attributes at once)
WHEN     the agent considers `data-visualization` for that task
THEN     the skill is not selected, because this task is the excluded case "When a table answers it better (few categories, exact values needed, comparison of many attributes at once)", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "When a table answers it better (few categories, exact values needed, comparison of many attributes at once)"; or `data-visualization` is declined without naming that exclusion
```

## Case 4 — Declines: Decoration: a chart whose purpose is to fill space is a slop signal (X1/L6)

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Decoration: a chart whose purpose is to fill space is a slop signal (X1/L6)
WHEN     the agent considers `data-visualization` for that task
THEN     the skill is not selected, because this task is the excluded case "Decoration: a chart whose purpose is to fill space is a slop signal (X1/L6)", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Decoration: a chart whose purpose is to fill space is a slop signal (X1/L6)"; or `data-visualization` is declined without naming that exclusion
```

## Case 5 — Detects: TRUNCATED BAR AXIS

```text
GIVEN    A run of this skill in which the known failure mode is present: TRUNCATED BAR AXIS
WHEN     the agent executes `data-visualization` and reaches the point where this failure occurs
THEN     "TRUNCATED BAR AXIS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A 2% difference rendered as a 5× visual difference."
FAIL IF  "TRUNCATED BAR AXIS" appears in the work and is reported as complete — specifically "A 2% difference rendered as a 5× visual difference."
```

## Case 6 — Detects: PIE WITH 12 SLICES

```text
GIVEN    A run of this skill in which the known failure mode is present: PIE WITH 12 SLICES
WHEN     the agent executes `data-visualization` and reaches the point where this failure occurs
THEN     "PIE WITH 12 SLICES" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Unreadable, and the comparison is false precision."
FAIL IF  "PIE WITH 12 SLICES" appears in the work and is reported as complete — specifically "Unreadable, and the comparison is false precision."
```

## Case 7 — Detects: RAINBOW ON CATEGORIES

```text
GIVEN    A run of this skill in which the known failure mode is present: RAINBOW ON CATEGORIES
WHEN     the agent executes `data-visualization` and reaches the point where this failure occurs
THEN     "RAINBOW ON CATEGORIES" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Implies an order that does not exist."
FAIL IF  "RAINBOW ON CATEGORIES" appears in the work and is reported as complete — specifically "Implies an order that does not exist."
```

## Case 8 — Detects: RED/GREEN ONLY

```text
GIVEN    A run of this skill in which the known failure mode is present: RED/GREEN ONLY
WHEN     the agent executes `data-visualization` and reaches the point where this failure occurs
THEN     "RED/GREEN ONLY" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Invisible to ~8% of men."
FAIL IF  "RED/GREEN ONLY" appears in the work and is reported as complete — specifically "Invisible to ~8% of men."
```

## Case 9 — Detects: MEAN WITHOUT SPREAD

```text
GIVEN    A run of this skill in which the known failure mode is present: MEAN WITHOUT SPREAD
WHEN     the agent executes `data-visualization` and reaches the point where this failure occurs
THEN     "MEAN WITHOUT SPREAD" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Bimodal or long-tailed data presented as a single number. MISSING n A dramatic percentage on five observations."
FAIL IF  "MEAN WITHOUT SPREAD" appears in the work and is reported as complete — specifically "Bimodal or long-tailed data presented as a single number. MISSING n A dramatic percentage on five observations."
```

## Case 10 — Detects: CHERRY-PICKED WINDOW

```text
GIVEN    A run of this skill in which the known failure mode is present: CHERRY-PICKED WINDOW
WHEN     the agent executes `data-visualization` and reaches the point where this failure occurs
THEN     "CHERRY-PICKED WINDOW" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "The trend that appears depends entirely on the unstated start date. PERCENT VS PERCENT POINT "Up 50%" when the change was 2 points on a 4% base."
FAIL IF  "CHERRY-PICKED WINDOW" appears in the work and is reported as complete — specifically "The trend that appears depends entirely on the unstated start date. PERCENT VS PERCENT POINT "Up 50%" when the change was 2 points on a 4% base."
```

## Case 11 — Detects: 3D AND PICTOGRAMS

```text
GIVEN    A run of this skill in which the known failure mode is present: 3D AND PICTOGRAMS
WHEN     the agent executes `data-visualization` and reaches the point where this failure occurs
THEN     "3D AND PICTOGRAMS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Area/volume encoding that overstates differences."
FAIL IF  "3D AND PICTOGRAMS" appears in the work and is reported as complete — specifically "Area/volume encoding that overstates differences."
```

## Case 12 — Detects: TOO MANY MARKS

```text
GIVEN    A run of this skill in which the known failure mode is present: TOO MANY MARKS
WHEN     the agent executes `data-visualization` and reaches the point where this failure occurs
THEN     "TOO MANY MARKS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "40 lines, a 20-entry legend, and no readable insight."
FAIL IF  "TOO MANY MARKS" appears in the work and is reported as complete — specifically "40 lines, a 20-entry legend, and no readable insight."
```

## Case 13 — Detects: NO EMPTY/ZERO STATES

```text
GIVEN    A run of this skill in which the known failure mode is present: NO EMPTY/ZERO STATES
WHEN     the agent executes `data-visualization` and reaches the point where this failure occurs
THEN     "NO EMPTY/ZERO STATES" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Blank chart on empty data; indistinguishable from failure."
FAIL IF  "NO EMPTY/ZERO STATES" appears in the work and is reported as complete — specifically "Blank chart on empty data; indistinguishable from failure."
```

## Case 14 — Detects: CLIENT-SIDE AGGREGATION

```text
GIVEN    A run of this skill in which the known failure mode is present: CLIENT-SIDE AGGREGATION
WHEN     the agent executes `data-visualization` and reaches the point where this failure occurs
THEN     "CLIENT-SIDE AGGREGATION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "100k rows shipped to the browser to draw one line. ANIMATION ON EVERY UPDATE The value change is obscured by the transition."
FAIL IF  "CLIENT-SIDE AGGREGATION" appears in the work and is reported as complete — specifically "100k rows shipped to the browser to draw one line. ANIMATION ON EVERY UPDATE The value change is obscured by the transition."
```

## Case 15 — Detects: DEFAULT LIBRARY THEME

```text
GIVEN    A run of this skill in which the known failure mode is present: DEFAULT LIBRARY THEME
WHEN     the agent executes `data-visualization` and reaches the point where this failure occurs
THEN     "DEFAULT LIBRARY THEME" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Every dashboard looks the same, and off-system colours break contrast."
FAIL IF  "DEFAULT LIBRARY THEME" appears in the work and is reported as complete — specifically "Every dashboard looks the same, and off-system colours break contrast."
```

## Case 16 — Detects: NO TEXT ALTERNATIVE

```text
GIVEN    A run of this skill in which the known failure mode is present: NO TEXT ALTERNATIVE
WHEN     the agent executes `data-visualization` and reaches the point where this failure occurs
THEN     "NO TEXT ALTERNATIVE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "The only copy of a number is inside a canvas element."
FAIL IF  "NO TEXT ALTERNATIVE" appears in the work and is reported as complete — specifically "The only copy of a number is inside a canvas element."
```

## Case 17 — Avoids: A 12-slice pie chart

```text
GIVEN    A situation that invites the anti-pattern "A 12-slice pie chart"
WHEN     the agent applies `data-visualization` in that situation
THEN     "A 12-slice pie chart" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A 12-slice pie chart" appears in the output; or it is absent by accident, with nothing in `data-visualization` having ruled it out
```

## Case 18 — Avoids: A bar chart starting at 95 instead of 0

```text
GIVEN    A situation that invites the anti-pattern "A bar chart starting at 95 instead of 0"
WHEN     the agent applies `data-visualization` in that situation
THEN     "A bar chart starting at 95 instead of 0" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A bar chart starting at 95 instead of 0" appears in the output; or it is absent by accident, with nothing in `data-visualization` having ruled it out
```

## Case 19 — Avoids: Red/green status colours with no icon or label

```text
GIVEN    A situation that invites the anti-pattern "Red/green status colours with no icon or label"
WHEN     the agent applies `data-visualization` in that situation
THEN     "Red/green status colours with no icon or label" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Red/green status colours with no icon or label" appears in the output; or it is absent by accident, with nothing in `data-visualization` having ruled it out
```

## Case 20 — Avoids: "Average response time: 120 ms" with no distribution and no n

```text
GIVEN    A situation that invites the anti-pattern "Average response time: 120 ms" with no distribution and no n"
WHEN     the agent applies `data-visualization` in that situation
THEN     "Average response time: 120 ms" with no distribution and no n" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Average response time: 120 ms" with no distribution and no n" appears in the output; or it is absent by accident, with nothing in `data-visualization` having ruled it out
```

## Case 21 — Avoids: Revenue "up 300%" from 1 to 4 units

```text
GIVEN    A situation that invites the anti-pattern "Revenue "up 300%" from 1 to 4 units"
WHEN     the agent applies `data-visualization` in that situation
THEN     "Revenue "up 300%" from 1 to 4 units" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Revenue "up 300%" from 1 to 4 units" appears in the output; or it is absent by accident, with nothing in `data-visualization` having ruled it out
```

## Case 22 — Avoids: Two y-axes with unrelated units on one frame

```text
GIVEN    A situation that invites the anti-pattern "Two y-axes with unrelated units on one frame"
WHEN     the agent applies `data-visualization` in that situation
THEN     "Two y-axes with unrelated units on one frame" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Two y-axes with unrelated units on one frame" appears in the output; or it is absent by accident, with nothing in `data-visualization` having ruled it out
```

## Case 23 — Avoids: Shipping 100k points to render a trend line

```text
GIVEN    A situation that invites the anti-pattern "Shipping 100k points to render a trend line"
WHEN     the agent applies `data-visualization` in that situation
THEN     "Shipping 100k points to render a trend line" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Shipping 100k points to render a trend line" appears in the output; or it is absent by accident, with nothing in `data-visualization` having ruled it out
```

## Case 24 — Avoids: A canvas chart with no table, no alt text and no keyboard access

```text
GIVEN    A situation that invites the anti-pattern "A canvas chart with no table, no alt text and no keyboard access"
WHEN     the agent applies `data-visualization` in that situation
THEN     "A canvas chart with no table, no alt text and no keyboard access" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A canvas chart with no table, no alt text and no keyboard access" appears in the output; or it is absent by accident, with nothing in `data-visualization` having ruled it out
```

## Case 25 — Avoids: The library's default colour palette in a product with a design system

```text
GIVEN    A situation that invites the anti-pattern "The library's default colour palette in a product with a design system"
WHEN     the agent applies `data-visualization` in that situation
THEN     "The library's default colour palette in a product with a design system" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "The library's default colour palette in a product with a design system" appears in the output; or it is absent by accident, with nothing in `data-visualization` having ruled it out
```

## Case 26 — Avoids: An empty chart that renders as blank white space

```text
GIVEN    A situation that invites the anti-pattern "An empty chart that renders as blank white space"
WHEN     the agent applies `data-visualization` in that situation
THEN     "An empty chart that renders as blank white space" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "An empty chart that renders as blank white space" appears in the output; or it is absent by accident, with nothing in `data-visualization` having ruled it out
```
