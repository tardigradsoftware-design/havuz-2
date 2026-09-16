# Test cases — `data-pipeline`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Move and transform data so that the result is correct, re-runnable and diagnosable. Pipelines fail in predictable ways — a partial run, a schema change upstream, a late record, a silent type coercion — and the design tha…
WHEN     the agent selects and executes the `data-pipeline` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: A single synchronous request path

```text
GIVEN    A task that looks like a match but is the excluded case: That is application logic, not a pipeline.
WHEN     the agent considers the `data-pipeline` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: The volume is small and the transformation is trivial

```text
GIVEN    A task that looks like a match but is the excluded case: A cron job and a script are the right answer;
WHEN     the agent considers the `data-pipeline` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: Nothing downstream depends on correctness guarantees

```text
GIVEN    A task that looks like a match but is the excluded case: Then the cost of the discipline is not justified.
WHEN     the agent considers the `data-pipeline` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Detects: A re-run duplicated data

```text
GIVEN    A run in which the known failure mode is present — A re-run duplicated data
WHEN     the agent executes `data-pipeline` and reaches the point where this failure occurs
THEN     the failure is detected by "the stage is not idempotent" and the documented response is applied: deduplicate on a stable key with a unique constraint
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 6 — Detects: Wrong results three stages downstream

```text
GIVEN    A run in which the known failure mode is present — Wrong results three stages downstream
WHEN     the agent executes `data-pipeline` and reaches the point where this failure occurs
THEN     the failure is detected by "no validation at the boundary where the schema changed" and the documented response is applied: validate at every hop, not only at ingestion
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 7 — Detects: Partial result published

```text
GIVEN    A run in which the known failure mode is present — Partial result published
WHEN     the agent executes `data-pipeline` and reaches the point where this failure occurs
THEN     the failure is detected by "the stage wrote before validating" and the documented response is applied: write to staging, publish only on success
FAIL IF  the failure goes unnoticed, or is noticed but the response is not the documented one
```

## Case 8 — Avoids: A PIPELINE THAT CANNOT BE RE-RUN

```text
GIVEN    A situation that invites the anti-pattern: Then it cannot be recovered, and recovery is the common case.
WHEN     the agent applies `data-pipeline`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 9 — Avoids: VALIDATION ONLY AT INGESTION

```text
GIVEN    A situation that invites the anti-pattern: The schema change that matters arrives mid-stream.
WHEN     the agent applies `data-pipeline`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
