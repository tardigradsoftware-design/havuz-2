# Test cases — `competitive-analysis`

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
GIVEN    A task inside this skill's stated purpose: Produce a comparison that survives contact with a sceptical reader: every cell sourced, every tradeoff named, every "winner" qualified by the constraint that makes it win. The output is never "X is best". It is **"for these constraints, X;
WHEN     the agent executes `competitive-analysis` end to end on that task
THEN     and before delivery these specific conditions hold: "Decision question, constraints and weights agreed before data gathering"; "Tradeoffs and failure modes stated per candidate, not only strengths"; "Re-validation date set; landscape changes tracked"
FAIL IF  "Decision question, constraints and weights agreed before data gathering" is false, or "Re-validation date set; landscape changes tracked" is false, or "Tradeoffs and failure modes stated per candidate, not only strengths" is false
```

## Case 2 — Declines: A question with one acceptable answer already decided — that is a migration…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: A question with one acceptable answer already decided — that is a migration plan
WHEN     the agent considers `competitive-analysis` for that task
THEN     the skill is not selected, because this task is the excluded case "A question with one acceptable answer already decided — that is a migration plan", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "A question with one acceptable answer already decided — that is a migration plan"; or `competitive-analysis` is declined without naming that exclusion
```

## Case 3 — Declines: Comparing things that are not substitutes (a library vs a hosted service vs a…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Comparing things that are not substitutes (a library vs a hosted service vs a pattern) unless you explicitly frame the comparison at the capability level
WHEN     the agent considers `competitive-analysis` for that task
THEN     the skill is not selected, because this task is the excluded case "Comparing things that are not substitutes (a library vs a hosted service vs a pattern) unless you explicitly frame the comparison at the capability level", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Comparing things that are not substitutes (a library vs a hosted service vs a pattern) unless you explicitly frame the comparison at the capability…"; or `competitive-analysis` is declined without naming that exclusion
```

## Case 4 — Declines: When the deciding constraint is unknown: establish it first,

```text
GIVEN    A task that looks like a match but is this skill's excluded case: When the deciding constraint is unknown: establish it first, or the matrix is decoration
WHEN     the agent considers `competitive-analysis` for that task
THEN     the skill is not selected, because this task is the excluded case "When the deciding constraint is unknown: establish it first, or the matrix is decoration", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "When the deciding constraint is unknown: establish it first, or the matrix is decoration"; or `competitive-analysis` is declined without naming that exclusion
```

## Case 5 — Detects: MARKETING MATRIX

```text
GIVEN    A run of this skill in which the known failure mode is present: MARKETING MATRIX
WHEN     the agent executes `competitive-analysis` and reaches the point where this failure occurs
THEN     "MARKETING MATRIX" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Cells filled from vendor homepages."
FAIL IF  "MARKETING MATRIX" appears in the work and is reported as complete — specifically "Cells filled from vendor homepages."
```

## Case 6 — Detects: UNNORMALISED UNITS

```text
GIVEN    A run of this skill in which the known failure mode is present: UNNORMALISED UNITS
WHEN     the agent executes `competitive-analysis` and reaches the point where this failure occurs
THEN     "UNNORMALISED UNITS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Comparing $/month to $/request to "free tier"."
FAIL IF  "UNNORMALISED UNITS" appears in the work and is reported as complete — specifically "Comparing $/month to $/request to "free tier"."
```

## Case 7 — Detects: STALE PRICING

```text
GIVEN    A run of this skill in which the known failure mode is present: STALE PRICING
WHEN     the agent executes `competitive-analysis` and reaches the point where this failure occurs
THEN     "STALE PRICING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Limits and prices from a year ago."
FAIL IF  "STALE PRICING" appears in the work and is reported as complete — specifically "Limits and prices from a year ago."
```

## Case 8 — Detects: MISSING CANDIDATES

```text
GIVEN    A run of this skill in which the known failure mode is present: MISSING CANDIDATES
WHEN     the agent executes `competitive-analysis` and reaches the point where this failure occurs
THEN     "MISSING CANDIDATES" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Only the three loudest options; the boring incumbent never evaluated. NO "DO NOTHING" ROW Building or deferring is never considered."
FAIL IF  "MISSING CANDIDATES" appears in the work and is reported as complete — specifically "Only the three loudest options; the boring incumbent never evaluated. NO "DO NOTHING" ROW Building or deferring is never considered."
```

## Case 9 — Detects: WEIGHTS AFTER SCORING

```text
GIVEN    A run of this skill in which the known failure mode is present: WEIGHTS AFTER SCORING
WHEN     the agent executes `competitive-analysis` and reaches the point where this failure occurs
THEN     "WEIGHTS AFTER SCORING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Criteria weighted to justify a preference already formed."
FAIL IF  "WEIGHTS AFTER SCORING" appears in the work and is reported as complete — specifically "Criteria weighted to justify a preference already formed."
```

## Case 10 — Detects: VENDOR BENCHMARK TRUST

```text
GIVEN    A run of this skill in which the known failure mode is present: VENDOR BENCHMARK TRUST
WHEN     the agent executes `competitive-analysis` and reaches the point where this failure occurs
THEN     "VENDOR BENCHMARK TRUST" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Reproducing a sponsored comparison as fact."
FAIL IF  "VENDOR BENCHMARK TRUST" appears in the work and is reported as complete — specifically "Reproducing a sponsored comparison as fact."
```

## Case 11 — Detects: STAR AS QUALITY

```text
GIVEN    A run of this skill in which the known failure mode is present: STAR AS QUALITY
WHEN     the agent executes `competitive-analysis` and reaches the point where this failure occurs
THEN     "STAR AS QUALITY" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Ranking repositories by stars, ignoring status and license."
FAIL IF  "STAR AS QUALITY" appears in the work and is reported as complete — specifically "Ranking repositories by stars, ignoring status and license."
```

## Case 12 — Detects: REMOVAL COST OMITTED

```text
GIVEN    A run of this skill in which the known failure mode is present: REMOVAL COST OMITTED
WHEN     the agent executes `competitive-analysis` and reaches the point where this failure occurs
THEN     "REMOVAL COST OMITTED" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "The decisive criterion for anything you will depend on for years."
FAIL IF  "REMOVAL COST OMITTED" appears in the work and is reported as complete — specifically "The decisive criterion for anything you will depend on for years."
```

## Case 13 — Detects: PERPETUAL ANALYSIS

```text
GIVEN    A run of this skill in which the known failure mode is present: PERPETUAL ANALYSIS
WHEN     the agent executes `competitive-analysis` and reaches the point where this failure occurs
THEN     "PERPETUAL ANALYSIS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Never recommending because one more option might exist."
FAIL IF  "PERPETUAL ANALYSIS" appears in the work and is reported as complete — specifically "Never recommending because one more option might exist."
```

## Case 14 — Detects: UNQUALIFIED VERDICT

```text
GIVEN    A run of this skill in which the known failure mode is present: UNQUALIFIED VERDICT
WHEN     the agent executes `competitive-analysis` and reaches the point where this failure occurs
THEN     "UNQUALIFIED VERDICT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "X is the best" with no constraint set attached."
FAIL IF  "UNQUALIFIED VERDICT" appears in the work and is reported as complete — specifically "X is the best" with no constraint set attached."
```

## Case 15 — Avoids: A feature matrix with ✓/✗ and no sources

```text
GIVEN    A situation that invites the anti-pattern "A feature matrix with ✓/✗ and no sources"
WHEN     the agent applies `competitive-analysis` in that situation
THEN     "A feature matrix with ✓/✗ and no sources" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A feature matrix with ✓/✗ and no sources" appears in the output; or it is absent by accident, with nothing in `competitive-analysis` having ruled it out
```

## Case 16 — Avoids: Quoting a vendor's "3× faster" with no workload definition

```text
GIVEN    A situation that invites the anti-pattern "Quoting a vendor's "3× faster" with no workload definition"
WHEN     the agent applies `competitive-analysis` in that situation
THEN     "Quoting a vendor's "3× faster" with no workload definition" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Quoting a vendor's "3× faster" with no workload definition" appears in the output; or it is absent by accident, with nothing in `competitive-analysis` having ruled it out
```

## Case 17 — Avoids: Comparing a self-hosted library with a managed service on price alone

```text
GIVEN    A situation that invites the anti-pattern "Comparing a self-hosted library with a managed service on price alone"
WHEN     the agent applies `competitive-analysis` in that situation
THEN     "Comparing a self-hosted library with a managed service on price alone" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Comparing a self-hosted library with a managed service on price alone" appears in the output; or it is absent by accident, with nothing in `competitive-analysis` having ruled it out
```

## Case 18 — Avoids: Ranking GitHub repositories by stars

```text
GIVEN    A situation that invites the anti-pattern "Ranking GitHub repositories by stars"
WHEN     the agent applies `competitive-analysis` in that situation
THEN     "Ranking GitHub repositories by stars" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Ranking GitHub repositories by stars" appears in the output; or it is absent by accident, with nothing in `competitive-analysis` having ruled it out
```

## Case 19 — Avoids: "X is the industry standard" with no evidence of who decided

```text
GIVEN    A situation that invites the anti-pattern "X is the industry standard" with no evidence of who decided"
WHEN     the agent applies `competitive-analysis` in that situation
THEN     "X is the industry standard" with no evidence of who decided" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "X is the industry standard" with no evidence of who decided" appears in the output; or it is absent by accident, with nothing in `competitive-analysis` having ruled it out
```

## Case 20 — Avoids: Omitting removal cost from a five-year dependency decision

```text
GIVEN    A situation that invites the anti-pattern "Omitting removal cost from a five-year dependency decision"
WHEN     the agent applies `competitive-analysis` in that situation
THEN     "Omitting removal cost from a five-year dependency decision" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Omitting removal cost from a five-year dependency decision" appears in the output; or it is absent by accident, with nothing in `competitive-analysis` having ruled it out
```

## Case 21 — Avoids: Presenting a recommendation with no stated conditions

```text
GIVEN    A situation that invites the anti-pattern "Presenting a recommendation with no stated conditions"
WHEN     the agent applies `competitive-analysis` in that situation
THEN     "Presenting a recommendation with no stated conditions" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Presenting a recommendation with no stated conditions" appears in the output; or it is absent by accident, with nothing in `competitive-analysis` having ruled it out
```
