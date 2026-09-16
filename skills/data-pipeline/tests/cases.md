# Test cases — `data-pipeline`

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
GIVEN    A task inside this skill's stated purpose: Move and transform data so that the result is correct, re-runnable and diagnosable. Pipelines fail in predictable ways — a partial run, a schema change upstream, a late record,
WHEN     the agent executes `data-pipeline` end to end on that task
THEN     the workflow runs in its stated order — "MAKE EVERY STAGE IDEMPOTENT" through to "PLAN THE RECOVERY BEFORE THE FAILURE"; and before delivery these specific conditions hold: "every stage is idempotent and safe to re-run"; "backfill is a parameterisation of the normal path"; "the recovery procedure is written down"
FAIL IF  "every stage is idempotent and safe to re-run" is false, or "the recovery procedure is written down" is false, or the result is delivered before "PLAN THE RECOVERY BEFORE THE FAILURE" has run
```

## Case 2 — Declines: A single synchronous request path.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: A single synchronous request path.
WHEN     the agent considers `data-pipeline` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "That is application logic, not a pipeline."
FAIL IF  the skill is run on a task where "A single synchronous request path.", and the consequence that exclusion states follows — "That is application logic, not a pipeline."; or `data-pipeline` is declined without naming that exclusion
```

## Case 3 — Declines: The volume is small and the transformation is trivial.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The volume is small and the transformation is trivial.
WHEN     the agent considers `data-pipeline` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "A cron job and a script are the right answer; a pipeline framework adds failure modes."
FAIL IF  the skill is run on a task where "The volume is small and the transformation is trivial.", and the consequence that exclusion states follows — "A cron job and a script are the right answer; a pipeline framework adds failure modes."; or `data-pipeline` is declined without naming that exclusion
```

## Case 4 — Declines: Nothing downstream depends on correctness guarantees.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Nothing downstream depends on correctness guarantees.
WHEN     the agent considers `data-pipeline` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Then the cost of the discipline is not justified."
FAIL IF  the skill is run on a task where "Nothing downstream depends on correctness guarantees.", and the consequence that exclusion states follows — "Then the cost of the discipline is not justified."; or `data-pipeline` is declined without naming that exclusion
```

## Case 5 — Declines: The real problem is the source system's data quality.

```text
GIVEN    A task that looks like a match but is this skill's excluded case: The real problem is the source system's data quality.
WHEN     the agent considers `data-pipeline` for that task
THEN     the skill is not selected, and what is done instead is what this exclusion names: "Fix it there; a pipeline cannot repair an unrecorded fact."
FAIL IF  the skill is run on a task where "The real problem is the source system's data quality.", and the consequence that exclusion states follows — "Fix it there; a pipeline cannot repair an unrecorded fact."; or `data-pipeline` is declined without naming that exclusion
```

## Case 6 — Detects: A re-run duplicated data

```text
GIVEN    A run of this skill in which the known failure mode is present: A re-run duplicated data
WHEN     the agent executes `data-pipeline` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "the stage is not idempotent" — and the response applied is the documented one: "deduplicate on a stable key with a unique constraint"
FAIL IF  "A re-run duplicated data" reaches the output because "the stage is not idempotent" was never checked; or it is caught but the response taken is not "deduplicate on a stable key with a unique constraint"
```

## Case 7 — Detects: Wrong results three stages downstream

```text
GIVEN    A run of this skill in which the known failure mode is present: Wrong results three stages downstream
WHEN     the agent executes `data-pipeline` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "no validation at the boundary where the schema changed" — and the response applied is the documented one: "validate at every hop, not only at ingestion"
FAIL IF  "Wrong results three stages downstream" reaches the output because "no validation at the boundary where the schema changed" was never checked; or it is caught but the response taken is not "validate at every hop, not only at ingestion"
```

## Case 8 — Detects: Partial result published

```text
GIVEN    A run of this skill in which the known failure mode is present: Partial result published
WHEN     the agent executes `data-pipeline` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "the stage wrote before validating" — and the response applied is the documented one: "write to staging, publish only on success"
FAIL IF  "Partial result published" reaches the output because "the stage wrote before validating" was never checked; or it is caught but the response taken is not "write to staging, publish only on success"
```

## Case 9 — Detects: Bad rows silently dropped

```text
GIVEN    A run of this skill in which the known failure mode is present: Bad rows silently dropped
WHEN     the agent executes `data-pipeline` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "no reject count in the metrics" — and the response applied is the documented one: "count, log and report rejects; make skipping explicit"
FAIL IF  "Bad rows silently dropped" reaches the output because "no reject count in the metrics" was never checked; or it is caught but the response taken is not "count, log and report rejects; make skipping explicit"
```

## Case 10 — Detects: Late data lost

```text
GIVEN    A run of this skill in which the known failure mode is present: Late data lost
WHEN     the agent executes `data-pipeline` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "no lateness policy" — and the response applied is the documented one: "state the window and the action for records past it"
FAIL IF  "Late data lost" reaches the output because "no lateness policy" was never checked; or it is caught but the response taken is not "state the window and the action for records past it"
```

## Case 11 — Detects: Backfill behaved differently

```text
GIVEN    A run of this skill in which the known failure mode is present: Backfill behaved differently
WHEN     the agent executes `data-pipeline` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "a separate script" — and the response applied is the documented one: "parameterise the normal path by date range"
FAIL IF  "Backfill behaved differently" reaches the output because "a separate script" was never checked; or it is caught but the response taken is not "parameterise the normal path by date range"
```

## Case 12 — Detects: Source rate-limited or pool exhausted

```text
GIVEN    A run of this skill in which the known failure mode is present: Source rate-limited or pool exhausted
WHEN     the agent executes `data-pipeline` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "parallelism unbounded" — and the response applied is the documented one: "bound workers; sum pools against the source ceiling"
FAIL IF  "Source rate-limited or pool exhausted" reaches the output because "parallelism unbounded" was never checked; or it is caught but the response taken is not "bound workers; sum pools against the source ceiling"
```

## Case 13 — Detects: Nobody noticed a row-count collapse

```text
GIVEN    A run of this skill in which the known failure mode is present: Nobody noticed a row-count collapse
WHEN     the agent executes `data-pipeline` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "no ratio alert" — and the response applied is the documented one: "alert on rows-in versus rows-out ratios"
FAIL IF  "Nobody noticed a row-count collapse" reaches the output because "no ratio alert" was never checked; or it is caught but the response taken is not "alert on rows-in versus rows-out ratios"
```

## Case 14 — Detects: Cannot reprocess after a bug

```text
GIVEN    A run of this skill in which the known failure mode is present: Cannot reprocess after a bug
WHEN     the agent executes `data-pipeline` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "the raw layer was overwritten" — and the response applied is the documented one: "keep immutable raw; transform in staging"
FAIL IF  "Cannot reprocess after a bug" reaches the output because "the raw layer was overwritten" was never checked; or it is caught but the response taken is not "keep immutable raw; transform in staging"
```

## Case 15 — Detects: Cost doubled silently

```text
GIVEN    A run of this skill in which the known failure mode is present: Cost doubled silently
WHEN     the agent executes `data-pipeline` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "no per-run cost metric" — and the response applied is the documented one: "record cost per run and alert on drift"
FAIL IF  "Cost doubled silently" reaches the output because "no per-run cost metric" was never checked; or it is caught but the response taken is not "record cost per run and alert on drift"
```

## Case 16 — Detects: Tests passed, production failed

```text
GIVEN    A run of this skill in which the known failure mode is present: Tests passed, production failed
WHEN     the agent executes `data-pipeline` and reaches the point where this failure occurs
THEN     the failure is caught by its documented detection signal — "inputs were empty or tiny" — and the response applied is the documented one: "test with real-shaped data and the edge cases"
FAIL IF  "Tests passed, production failed" reaches the output because "inputs were empty or tiny" was never checked; or it is caught but the response taken is not "test with real-shaped data and the edge cases"
```

## Case 17 — Avoids: A PIPELINE THAT CANNOT BE RE-RUN

```text
GIVEN    A situation that invites the anti-pattern "A PIPELINE THAT CANNOT BE RE-RUN", whose stated consequence is: Then it cannot be recovered, and recovery is the common case.
WHEN     the agent applies `data-pipeline` in that situation
THEN     "A PIPELINE THAT CANNOT BE RE-RUN" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Then it cannot be recovered, and recovery is the common case."
FAIL IF  "A PIPELINE THAT CANNOT BE RE-RUN" appears in the output — that is, "Then it cannot be recovered, and recovery is the common case."; or it is absent by accident, with nothing in `data-pipeline` having ruled it out
```

## Case 18 — Avoids: VALIDATION ONLY AT INGESTION

```text
GIVEN    A situation that invites the anti-pattern "VALIDATION ONLY AT INGESTION", whose stated consequence is: The schema change that matters arrives mid-stream.
WHEN     the agent applies `data-pipeline` in that situation
THEN     "VALIDATION ONLY AT INGESTION" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The schema change that matters arrives mid-stream."
FAIL IF  "VALIDATION ONLY AT INGESTION" appears in the output — that is, "The schema change that matters arrives mid-stream."; or it is absent by accident, with nothing in `data-pipeline` having ruled it out
```

## Case 19 — Avoids: SILENT ROW DROPPING

```text
GIVEN    A situation that invites the anti-pattern "SILENT ROW DROPPING", whose stated consequence is: The most expensive failure mode: the output looks correct and is incomplete.
WHEN     the agent applies `data-pipeline` in that situation
THEN     "SILENT ROW DROPPING" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The most expensive failure mode: the output looks correct and is incomplete."
FAIL IF  "SILENT ROW DROPPING" appears in the output — that is, "The most expensive failure mode: the output looks correct and is incomplete."; or it is absent by accident, with nothing in `data-pipeline` having ruled it out
```

## Case 20 — Avoids: OVERWRITING THE RAW LAYER

```text
GIVEN    A situation that invites the anti-pattern "OVERWRITING THE RAW LAYER", whose stated consequence is: A transformation bug becomes permanent data loss.
WHEN     the agent applies `data-pipeline` in that situation
THEN     "OVERWRITING THE RAW LAYER" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "A transformation bug becomes permanent data loss."
FAIL IF  "OVERWRITING THE RAW LAYER" appears in the output — that is, "A transformation bug becomes permanent data loss."; or it is absent by accident, with nothing in `data-pipeline` having ruled it out
```

## Case 21 — Avoids: BACKFILL AS A SEPARATE SCRIPT

```text
GIVEN    A situation that invites the anti-pattern "BACKFILL AS A SEPARATE SCRIPT", whose stated consequence is: A second pipeline with its own bugs and no tests.
WHEN     the agent applies `data-pipeline` in that situation
THEN     "BACKFILL AS A SEPARATE SCRIPT" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "A second pipeline with its own bugs and no tests."
FAIL IF  "BACKFILL AS A SEPARATE SCRIPT" appears in the output — that is, "A second pipeline with its own bugs and no tests."; or it is absent by accident, with nothing in `data-pipeline` having ruled it out
```

## Case 22 — Avoids: CHECK-THEN-INSERT DEDUPLICATION

```text
GIVEN    A situation that invites the anti-pattern "CHECK-THEN-INSERT DEDUPLICATION", whose stated consequence is: Two concurrent runs both pass the check; use a unique constraint.
WHEN     the agent applies `data-pipeline` in that situation
THEN     "CHECK-THEN-INSERT DEDUPLICATION" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Two concurrent runs both pass the check; use a unique constraint."
FAIL IF  "CHECK-THEN-INSERT DEDUPLICATION" appears in the output — that is, "Two concurrent runs both pass the check; use a unique constraint."; or it is absent by accident, with nothing in `data-pipeline` having ruled it out
```

## Case 23 — Avoids: UNBOUNDED PARALLELISM

```text
GIVEN    A situation that invites the anti-pattern "UNBOUNDED PARALLELISM", whose stated consequence is: The source's rate limit or connection ceiling is the real constraint.
WHEN     the agent applies `data-pipeline` in that situation
THEN     "UNBOUNDED PARALLELISM" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "The source's rate limit or connection ceiling is the real constraint."
FAIL IF  "UNBOUNDED PARALLELISM" appears in the output — that is, "The source's rate limit or connection ceiling is the real constraint."; or it is absent by accident, with nothing in `data-pipeline` having ruled it out
```

## Case 24 — Avoids: ALERTING ONLY ON FAILURE

```text
GIVEN    A situation that invites the anti-pattern "ALERTING ONLY ON FAILURE", whose stated consequence is: A stage that succeeds with a tenth of its rows is worse than one that fails.
WHEN     the agent applies `data-pipeline` in that situation
THEN     "ALERTING ONLY ON FAILURE" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "A stage that succeeds with a tenth of its rows is worse than one that fails."
FAIL IF  "ALERTING ONLY ON FAILURE" appears in the output — that is, "A stage that succeeds with a tenth of its rows is worse than one that fails."; or it is absent by accident, with nothing in `data-pipeline` having ruled it out
```

## Case 25 — Avoids: TESTING WITH EMPTY INPUTS

```text
GIVEN    A situation that invites the anti-pattern "TESTING WITH EMPTY INPUTS", whose stated consequence is: Everything passes.
WHEN     the agent applies `data-pipeline` in that situation
THEN     "TESTING WITH EMPTY INPUTS" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Everything passes."
FAIL IF  "TESTING WITH EMPTY INPUTS" appears in the output — that is, "Everything passes."; or it is absent by accident, with nothing in `data-pipeline` having ruled it out
```

## Case 26 — Avoids: NO COST VISIBILITY

```text
GIVEN    A situation that invites the anti-pattern "NO COST VISIBILITY", whose stated consequence is: Growth becomes a bill before it becomes a ticket.
WHEN     the agent applies `data-pipeline` in that situation
THEN     "NO COST VISIBILITY" is absent from the output, and the work shows it was ruled out for the reason this skill gives: "Growth becomes a bill before it becomes a ticket."
FAIL IF  "NO COST VISIBILITY" appears in the output — that is, "Growth becomes a bill before it becomes a ticket."; or it is absent by accident, with nothing in `data-pipeline` having ruled it out
```
