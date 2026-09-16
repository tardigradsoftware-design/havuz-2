# Test cases — `performance-optimization`

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
GIVEN    A task inside this skill's stated purpose: Make a system faster by finding where the time actually goes and changing that. The discipline is the skill: measure, localise, change one thing, re-measure, keep or revert.
WHEN     the agent executes `performance-optimization` end to end on that task
THEN     the workflow runs in its stated order — "DEFINE THE TARGET AS A NUMBER AND A PERCENTILE" through to "COMMIT THE BENCHMARK"; and before delivery these specific conditions hold: "the target is a number with a percentile"; "exactly one change was made"; "the benchmark is committed and re-runnable"
FAIL IF  "the target is a number with a percentile" is false, or "the benchmark is committed and re-runnable" is false, or the result is delivered before "COMMIT THE BENCHMARK" has run
```

## Case 2 — Declines: Nothing has been measured.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Nothing has been measured.
WHEN     the agent considers `performance-optimization` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Establish the baseline first; a complaint of "slow" is not a measurement."
FAIL IF  the skill is run on a task where "Nothing has been measured.", and the consequence that exclusion states follows — "Establish the baseline first; a complaint of "slow" is not a measurement."; or `performance-optimization` is declined without naming that exclusion
```

## Case 3 — Declines: The problem is a correctness bug that manifests as slowness — a lock,

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The problem is a correctness bug that manifests as slowness — a lock, a retry loop, a leaked connection.
WHEN     the agent considers `performance-optimization` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Diagnose it as a bug."
FAIL IF  the skill is run on a task where "The problem is a correctness bug that manifests as slowness — a lock, a retry loop, a leaked connection.", and the consequence that exclusion states follows — "Diagnose it as a bug."; or `performance-optimization` is declined without naming that exclusion
```

## Case 4 — Declines: The workload being measured is not production-shaped: empty tables, one user,

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The workload being measured is not production-shaped: empty tables, one user, warm caches, a laptop.
WHEN     the agent considers `performance-optimization` for that task
THEN     the skill is not selected, because this task is the excluded case "The workload being measured is not production-shaped: empty tables, one user, warm caches, a laptop.", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "The workload being measured is not production-shaped: empty tables, one user, warm caches, a laptop."; or `performance-optimization` is declined without naming that exclusion
```

## Case 5 — Declines: The cost is external and immutable — a third-party API's latency,

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The cost is external and immutable — a third-party API's latency, the speed of light to a distant region.
WHEN     the agent considers `performance-optimization` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Architecture or vendor change applies, not optimisation."
FAIL IF  the skill is run on a task where "The cost is external and immutable — a third-party API's latency, the speed of light to a distant region.", and the consequence that exclusion states follows — "Architecture or vendor change applies, not optimisation."; or `performance-optimization` is declined without naming that exclusion
```

## Case 6 — Detects: Optimised the wrong layer

```text
GIVEN    A run of this skill in which the known failure mode is present: Optimised the wrong layer
WHEN     the agent executes `performance-optimization` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "the delta is inside the noise floor" — and the response applied is the documented one: "go back to step 4; the localisation was wrong"
FAIL IF  "Optimised the wrong layer" reaches the output because "the delta is inside the noise floor" was never checked; or it is caught but the response taken is not "go back to step 4; the localisation was wrong"
```

## Case 7 — Detects: Benchmark measured warmup

```text
GIVEN    A run of this skill in which the known failure mode is present: Benchmark measured warmup
WHEN     the agent executes `performance-optimization` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "the first runs dominate" — and the response applied is the documented one: "discard warmup, then measure steady state"
FAIL IF  "Benchmark measured warmup" reaches the output because "the first runs dominate" was never checked; or it is caught but the response taken is not "discard warmup, then measure steady state"
```

## Case 8 — Detects: Improvement in the lab, not in the field

```text
GIVEN    A run of this skill in which the known failure mode is present: Improvement in the lab, not in the field
WHEN     the agent executes `performance-optimization` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "RUM percentiles unmoved" — and the response applied is the documented one: "lab conditions differ from users; re-measure on field data"
FAIL IF  "Improvement in the lab, not in the field" reaches the output because "RUM percentiles unmoved" was never checked; or it is caught but the response taken is not "lab conditions differ from users; re-measure on field data"
```

## Case 9 — Detects: Tail improved, median regressed

```text
GIVEN    A run of this skill in which the known failure mode is present: Tail improved, median regressed
WHEN     the agent executes `performance-optimization` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "p50 rose while p99 fell" — and the response applied is the documented one: "report both; decide which the budget covers"
FAIL IF  "Tail improved, median regressed" reaches the output because "p50 rose while p99 fell" was never checked; or it is caught but the response taken is not "report both; decide which the budget covers"
```

## Case 10 — Detects: Caching introduced a correctness bug

```text
GIVEN    A run of this skill in which the known failure mode is present: Caching introduced a correctness bug
WHEN     the agent executes `performance-optimization` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "stale or inconsistent data reported" — and the response applied is the documented one: "the cache layer needs an invalidation design and a stated staleness budget"
FAIL IF  "Caching introduced a correctness bug" reaches the output because "stale or inconsistent data reported" was never checked; or it is caught but the response taken is not "the cache layer needs an invalidation design and a stated staleness budget"
```

## Case 11 — Detects: Parallelised an N+1

```text
GIVEN    A run of this skill in which the known failure mode is present: Parallelised an N+1
WHEN     the agent executes `performance-optimization` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "N parallel queries instead of N sequential" — and the response applied is the documented one: "fix the query pattern first, then parallelise independent work"
FAIL IF  "Parallelised an N+1" reaches the output because "N parallel queries instead of N sequential" was never checked; or it is caught but the response taken is not "fix the query pattern first, then parallelise independent work"
```

## Case 12 — Detects: Profile looked cheap but the request was slow

```text
GIVEN    A run of this skill in which the known failure mode is present: Profile looked cheap but the request was slow
WHEN     the agent executes `performance-optimization` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "time is off-CPU" — and the response applied is the documented one: "use off-CPU or wall-clock profiling"
FAIL IF  "Profile looked cheap but the request was slow" reaches the output because "time is off-CPU" was never checked; or it is caught but the response taken is not "use off-CPU or wall-clock profiling"
```

## Case 13 — Detects: Resource cost ignored

```text
GIVEN    A run of this skill in which the known failure mode is present: Resource cost ignored
WHEN     the agent executes `performance-optimization` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "memory or connection use rose" — and the response applied is the documented one: "measure resource utilisation as part of the result, not only latency"
FAIL IF  "Resource cost ignored" reaches the output because "memory or connection use rose" was never checked; or it is caught but the response taken is not "measure resource utilisation as part of the result, not only latency"
```

## Case 14 — Avoids: OPTIMISING FROM A GUESS

```text
GIVEN    A situation that invites the anti-pattern "OPTIMISING FROM A GUESS", whose stated consequence is: The most common failure, and invisible in the diff.
WHEN     the agent applies `performance-optimization` in that situation
THEN     "OPTIMISING FROM A GUESS" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The most common failure, and invisible in the diff."
FAIL IF  "OPTIMISING FROM A GUESS" appears in the output — that is, "The most common failure, and invisible in the diff."; or it is absent by accident, with nothing in `performance-optimization` having ruled it out
```

## Case 15 — Avoids: MEASURING THE AVERAGE

```text
GIVEN    A situation that invites the anti-pattern "MEASURING THE AVERAGE", whose stated consequence is: The tail is the user experience; a good mean with a p99 at 20× is a bad system for the users in the tail.
WHEN     the agent applies `performance-optimization` in that situation
THEN     "MEASURING THE AVERAGE" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The tail is the user experience; a good mean with a p99 at 20× is a bad system for the users in the tail."
FAIL IF  "MEASURING THE AVERAGE" appears in the output — that is, "The tail is the user experience; a good mean with a p99 at 20× is a bad system for the users in the tail."; or it is absent by accident, with nothing in `performance-optimization` having ruled it out
```

## Case 16 — Avoids: CACHING AS THE FIRST RESPONSE

```text
GIVEN    A situation that invites the anti-pattern "CACHING AS THE FIRST RESPONSE", whose stated consequence is: It is second or third, and it introduces a correctness problem that outlives the performance gain.
WHEN     the agent applies `performance-optimization` in that situation
THEN     "CACHING AS THE FIRST RESPONSE" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "It is second or third, and it introduces a correctness problem that outlives the performance gain."
FAIL IF  "CACHING AS THE FIRST RESPONSE" appears in the output — that is, "It is second or third, and it introduces a correctness problem that outlives the performance gain."; or it is absent by accident, with nothing in `performance-optimization` having ruled it out
```

## Case 17 — Avoids: PROFILING AN EMPTY DATABASE

```text
GIVEN    A situation that invites the anti-pattern "PROFILING AN EMPTY DATABASE", whose stated consequence is: Everything is fast with no data.
WHEN     the agent applies `performance-optimization` in that situation
THEN     "PROFILING AN EMPTY DATABASE" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Everything is fast with no data."
FAIL IF  "PROFILING AN EMPTY DATABASE" appears in the output — that is, "Everything is fast with no data."; or it is absent by accident, with nothing in `performance-optimization` having ruled it out
```

## Case 18 — Avoids: BENCHMARKING WITHOUT WARMUP

```text
GIVEN    A situation that invites the anti-pattern "BENCHMARKING WITHOUT WARMUP", whose stated consequence is: You are measuring class loading, JIT compilation and cold caches.
WHEN     the agent applies `performance-optimization` in that situation
THEN     "BENCHMARKING WITHOUT WARMUP" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "You are measuring class loading, JIT compilation and cold caches."
FAIL IF  "BENCHMARKING WITHOUT WARMUP" appears in the output — that is, "You are measuring class loading, JIT compilation and cold caches."; or it is absent by accident, with nothing in `performance-optimization` having ruled it out
```

## Case 19 — Avoids: OPTIMISING THE DEMO PATH

```text
GIVEN    A situation that invites the anti-pattern "OPTIMISING THE DEMO PATH", whose stated consequence is: The slow path is the large tenant, the old data or the unusual query shape.
WHEN     the agent applies `performance-optimization` in that situation
THEN     "OPTIMISING THE DEMO PATH" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The slow path is the large tenant, the old data or the unusual query shape."
FAIL IF  "OPTIMISING THE DEMO PATH" appears in the output — that is, "The slow path is the large tenant, the old data or the unusual query shape."; or it is absent by accident, with nothing in `performance-optimization` having ruled it out
```

## Case 20 — Avoids: PREMATURE OPTIMISATION OF COLD CODE

```text
GIVEN    A situation that invites the anti-pattern "PREMATURE OPTIMISATION OF COLD CODE", whose stated consequence is: Effort spent on a path executed twice a day.
WHEN     the agent applies `performance-optimization` in that situation
THEN     "PREMATURE OPTIMISATION OF COLD CODE" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Effort spent on a path executed twice a day."
FAIL IF  "PREMATURE OPTIMISATION OF COLD CODE" appears in the output — that is, "Effort spent on a path executed twice a day."; or it is absent by accident, with nothing in `performance-optimization` having ruled it out
```

## Case 21 — Avoids: KEEPING A CHANGE INSIDE THE NOISE

```text
GIVEN    A situation that invites the anti-pattern "KEEPING A CHANGE INSIDE THE NOISE", whose stated consequence is: Plausibility is not evidence.
WHEN     the agent applies `performance-optimization` in that situation
THEN     "KEEPING A CHANGE INSIDE THE NOISE" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Plausibility is not evidence."
FAIL IF  "KEEPING A CHANGE INSIDE THE NOISE" appears in the output — that is, "Plausibility is not evidence."; or it is absent by accident, with nothing in `performance-optimization` having ruled it out
```

## Case 22 — Avoids: NO COMMITTED BENCHMARK

```text
GIVEN    A situation that invites the anti-pattern "NO COMMITTED BENCHMARK", whose stated consequence is: The regression returns within a quarter and nobody can prove it.
WHEN     the agent applies `performance-optimization` in that situation
THEN     "NO COMMITTED BENCHMARK" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The regression returns within a quarter and nobody can prove it."
FAIL IF  "NO COMMITTED BENCHMARK" appears in the output — that is, "The regression returns within a quarter and nobody can prove it."; or it is absent by accident, with nothing in `performance-optimization` having ruled it out
```
