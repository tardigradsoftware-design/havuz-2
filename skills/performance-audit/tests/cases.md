# Test cases — `performance-audit`

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
GIVEN    A task inside this skill's stated purpose: Make a system meet a **stated budget on a stated workload for a stated population**, using measurement to decide where to spend effort. Performance work without a budget is entertainment; performance work without measurement is guesswork.
WHEN     the agent executes `performance-audit` end to end on that task
THEN     and before delivery these specific conditions hold: "Numeric budgets agreed per metric before measuring (latency p50/p95/p99, throughput, CWV, resources, cost)"; "N+1, index, cache, payload and waterfall checks run explicitly"; "Re-measurement scheduled"
FAIL IF  "Numeric budgets agreed per metric before measuring (latency p50/p95/p99, throughput, CWV, resources, cost)" is false, or "Re-measurement scheduled" is false, or "N+1, index, cache, payload and waterfall checks run explicitly" is false
```

## Case 2 — Declines: Optimising a path nobody uses (measure traffic first — the profile decides)

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Optimising a path nobody uses (measure traffic first — the profile decides)
WHEN     the agent considers `performance-audit` for that task
THEN     the skill is not selected, because this task is the excluded case "Optimising a path nobody uses (measure traffic first — the profile decides)", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Optimising a path nobody uses (measure traffic first — the profile decides)"; or `performance-audit` is declined without naming that exclusion
```

## Case 3 — Declines: Micro-optimising code whose cost is dominated by a network call

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Micro-optimising code whose cost is dominated by a network call
WHEN     the agent considers `performance-audit` for that task
THEN     the skill is not selected, because this task is the excluded case "Micro-optimising code whose cost is dominated by a network call", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Micro-optimising code whose cost is dominated by a network call"; or `performance-audit` is declined without naming that exclusion
```

## Case 4 — Declines: Before correctness: a fast wrong answer is worse

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Before correctness: a fast wrong answer is worse
WHEN     the agent considers `performance-audit` for that task
THEN     the skill is not selected, because this task is the excluded case "Before correctness: a fast wrong answer is worse", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Before correctness: a fast wrong answer is worse"; or `performance-audit` is declined without naming that exclusion
```

## Case 5 — Declines: When the real complaint is a UX/design problem misreported as "slow"

```text
GIVEN    A task that looks like a match but is this skill's excluded case: When the real complaint is a UX/design problem misreported as "slow"
WHEN     the agent considers `performance-audit` for that task
THEN     the skill is not selected, because this task is the excluded case "When the real complaint is a UX/design problem misreported as "slow", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "When the real complaint is a UX/design problem misreported as "slow"; or `performance-audit` is declined without naming that exclusion
```

## Case 6 — Detects: NO BUDGET

```text
GIVEN    A run of this skill in which the known failure mode is present: NO BUDGET
WHEN     the agent executes `performance-audit` and reaches the point where this failure occurs
THEN     "NO BUDGET" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Optimising without a target; never finishes, never proves anything."
FAIL IF  "NO BUDGET" appears in the work and is reported as complete — specifically "Optimising without a target; never finishes, never proves anything."
```

## Case 7 — Detects: MEAN-BASED REVIEW

```text
GIVEN    A run of this skill in which the known failure mode is present: MEAN-BASED REVIEW
WHEN     the agent executes `performance-audit` and reaches the point where this failure occurs
THEN     "MEAN-BASED REVIEW" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Averages hide the p99 users who are complaining."
FAIL IF  "MEAN-BASED REVIEW" appears in the work and is reported as complete — specifically "Averages hide the p99 users who are complaining."
```

## Case 8 — Detects: LAB-ONLY EVIDENCE

```text
GIVEN    A run of this skill in which the known failure mode is present: LAB-ONLY EVIDENCE
WHEN     the agent executes `performance-audit` and reaches the point where this failure occurs
THEN     "LAB-ONLY EVIDENCE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A Lighthouse score improved; real users saw nothing. OPTIMISE THE COLD PATH Improving a function that runs twice per day."
FAIL IF  "LAB-ONLY EVIDENCE" appears in the work and is reported as complete — specifically "A Lighthouse score improved; real users saw nothing. OPTIMISE THE COLD PATH Improving a function that runs twice per day."
```

## Case 9 — Detects: GUESS-DRIVEN FIXING

```text
GIVEN    A run of this skill in which the known failure mode is present: GUESS-DRIVEN FIXING
WHEN     the agent executes `performance-audit` and reaches the point where this failure occurs
THEN     "GUESS-DRIVEN FIXING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Rewriting the module that "feels slow" without a profile."
FAIL IF  "GUESS-DRIVEN FIXING" appears in the work and is reported as complete — specifically "Rewriting the module that "feels slow" without a profile."
```

## Case 10 — Detects: PARTIAL VERIFICATION

```text
GIVEN    A run of this skill in which the known failure mode is present: PARTIAL VERIFICATION
WHEN     the agent executes `performance-audit` and reaches the point where this failure occurs
THEN     "PARTIAL VERIFICATION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Measuring a different workload than the baseline."
FAIL IF  "PARTIAL VERIFICATION" appears in the work and is reported as complete — specifically "Measuring a different workload than the baseline."
```

## Case 11 — Detects: REGRESSION BLINDNESS

```text
GIVEN    A run of this skill in which the known failure mode is present: REGRESSION BLINDNESS
WHEN     the agent executes `performance-audit` and reaches the point where this failure occurs
THEN     "REGRESSION BLINDNESS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Fixing latency while raising error rate or memory. PREMATURE ABSTRACTION Caching, queues and microservices added before measurement."
FAIL IF  "REGRESSION BLINDNESS" appears in the work and is reported as complete — specifically "Fixing latency while raising error rate or memory. PREMATURE ABSTRACTION Caching, queues and microservices added before measurement."
```

## Case 12 — Detects: ONE-SHOT EFFORT

```text
GIVEN    A run of this skill in which the known failure mode is present: ONE-SHOT EFFORT
WHEN     the agent executes `performance-audit` and reaches the point where this failure occurs
THEN     "ONE-SHOT EFFORT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "No CI gate; the budget is re-breached in the next release."
FAIL IF  "ONE-SHOT EFFORT" appears in the work and is reported as complete — specifically "No CI gate; the budget is re-breached in the next release."
```

## Case 13 — Detects: VENDOR METRIC TRUST

```text
GIVEN    A run of this skill in which the known failure mode is present: VENDOR METRIC TRUST
WHEN     the agent executes `performance-audit` and reaches the point where this failure occurs
THEN     "VENDOR METRIC TRUST" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Accepting a provider's benchmark without the measurement method."
FAIL IF  "VENDOR METRIC TRUST" appears in the work and is reported as complete — specifically "Accepting a provider's benchmark without the measurement method."
```

## Case 14 — Avoids: "The average response time is 120 ms" as the whole report

```text
GIVEN    A situation that invites the anti-pattern "The average response time is 120 ms" as the whole report"
WHEN     the agent applies `performance-audit` in that situation
THEN     "The average response time is 120 ms" as the whole report" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "The average response time is 120 ms" as the whole report" appears in the output; or it is absent by accident, with nothing in `performance-audit` having ruled it out
```

## Case 15 — Avoids: Adding a cache layer before checking whether the query has an index

```text
GIVEN    A situation that invites the anti-pattern "Adding a cache layer before checking whether the query has an index"
WHEN     the agent applies `performance-audit` in that situation
THEN     "Adding a cache layer before checking whether the query has an index" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Adding a cache layer before checking whether the query has an index" appears in the output; or it is absent by accident, with nothing in `performance-audit` having ruled it out
```

## Case 16 — Avoids: Scaling out to fix an N+1

```text
GIVEN    A situation that invites the anti-pattern "Scaling out to fix an N+1"
WHEN     the agent applies `performance-audit` in that situation
THEN     "Scaling out to fix an N+1" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Scaling out to fix an N+1" appears in the output; or it is absent by accident, with nothing in `performance-audit` having ruled it out
```

## Case 17 — Avoids: Optimising a Lighthouse score instead of the user experience

```text
GIVEN    A situation that invites the anti-pattern "Optimising a Lighthouse score instead of the user experience"
WHEN     the agent applies `performance-audit` in that situation
THEN     "Optimising a Lighthouse score instead of the user experience" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Optimising a Lighthouse score instead of the user experience" appears in the output; or it is absent by accident, with nothing in `performance-audit` having ruled it out
```

## Case 18 — Avoids: Citing a vendor benchmark whose method is not published

```text
GIVEN    A situation that invites the anti-pattern "Citing a vendor benchmark whose method is not published"
WHEN     the agent applies `performance-audit` in that situation
THEN     "Citing a vendor benchmark whose method is not published" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Citing a vendor benchmark whose method is not published" appears in the output; or it is absent by accident, with nothing in `performance-audit` having ruled it out
```

## Case 19 — Avoids: Rewriting a service because it "feels slow"

```text
GIVEN    A situation that invites the anti-pattern "Rewriting a service because it "feels slow"
WHEN     the agent applies `performance-audit` in that situation
THEN     "Rewriting a service because it "feels slow" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Rewriting a service because it "feels slow" appears in the output; or it is absent by accident, with nothing in `performance-audit` having ruled it out
```

## Case 20 — Avoids: Measuring a warm cache and reporting it as cold-start performance

```text
GIVEN    A situation that invites the anti-pattern "Measuring a warm cache and reporting it as cold-start performance"
WHEN     the agent applies `performance-audit` in that situation
THEN     "Measuring a warm cache and reporting it as cold-start performance" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Measuring a warm cache and reporting it as cold-start performance" appears in the output; or it is absent by accident, with nothing in `performance-audit` having ruled it out
```

## Case 21 — Avoids: Shipping a performance fix with no CI gate, then re-regressing next sprint

```text
GIVEN    A situation that invites the anti-pattern "Shipping a performance fix with no CI gate, then re-regressing next sprint"
WHEN     the agent applies `performance-audit` in that situation
THEN     "Shipping a performance fix with no CI gate, then re-regressing next sprint" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Shipping a performance fix with no CI gate, then re-regressing next sprint" appears in the output; or it is absent by accident, with nothing in `performance-audit` having ruled it out
```
