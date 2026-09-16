---
name: data-pipeline
version: 1.0.0
description: >-
  Design and operate a data pipeline that can be trusted: make every stage idempotent and re-runnable, fail loudly at the boundary, validate the schema at each hop, and make the backfill and the late-arriving-data cases first-class.
category: data
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [data-pipeline, etl, idempotency, schema-validation, backfill, observability, batch, streaming]
applies_to: [any]
priority: 5
requires: []
conflicts_with: []
estimated_tokens: 2241
sections:
  - heading: "Purpose"
    anchor: "#purpose"
    purpose: overview
  - heading: "When to Use"
    anchor: "#when-to-use"
    purpose: when-to-use
  - heading: "When NOT to Use"
    anchor: "#when-not-to-use"
    purpose: pitfalls
  - heading: "Workflow"
    anchor: "#workflow"
    purpose: implementation
  - heading: "Failure Modes"
    anchor: "#failure-modes"
    purpose: pitfalls
  - heading: "Quality Checklist"
    anchor: "#quality-checklist"
    purpose: checklist
  - heading: "Anti-Patterns"
    anchor: "#anti-patterns"
    purpose: pitfalls
  - heading: "References"
    anchor: "#references"
    purpose: references
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
sources:
  - title: "The Twelve-Factor App"
    url: https://github.com/heroku/12factor
    type: github-repository
    organization: "Heroku"
    license: MIT
    claim_type: recommendation
    confidence: high
    verified_at: 2026-09-15
    note: "Backing services as attached resources and disposability are what make at-least-once delivery, and therefore stage idempotency, unavoidable."
  - title: "dbt-core"
    url: https://github.com/dbt-labs/dbt-core
    type: github-repository
    organization: "dbt Labs"
    license: Apache-2.0
    claim_type: recommendation
    confidence: high
    verified_at: 2026-09-15
    note: "A maintained transformation framework whose staging/mart layering and test-on-every-model convention is the pattern in steps 3 and 5."
  - title: "Apache Airflow documentation"
    url: https://airflow.apache.org/docs/
    type: official-docs
    organization: "Apache Software Foundation"
    license: Apache-2.0
    claim_type: recommendation
    confidence: high
    verified_at: 2026-09-15
    note: "Scheduling, retries and backfill semantics; the operational assumptions in steps 1, 7 and 12."
related_skills: [rag-pipeline, database-design, migration, deployment, data-visualization]
related_repositories: []
tests: 26
---
# Data Pipeline

## Purpose

Move and transform data so that the result is correct, re-runnable and diagnosable. Pipelines fail in
predictable ways — a partial run, a schema change upstream, a late record, a silent type coercion — and
the design that survives them treats re-running, validation and observability as primary requirements
rather than additions.

## When to Use

```text
✓ data moves between systems on a schedule or an event
✓ a transformation must be reproducible and auditable
✓ an existing pipeline produces occasional wrong results that are hard to diagnose
✓ a backfill or a historical reprocessing is required
```

## When NOT to Use

```text
✗ A single synchronous request path. That is application logic, not a pipeline.
✗ The volume is small and the transformation is trivial. A cron job and a script are the right answer;
  a pipeline framework adds failure modes.
✗ Nothing downstream depends on correctness guarantees. Then the cost of the discipline is not justified.
✗ The real problem is the source system's data quality. Fix it there; a pipeline cannot repair an
  unrecorded fact.
```

## Workflow

```text
1. MAKE EVERY STAGE IDEMPOTENT.   Re-running a stage on the same input produces the same output and no
   duplicate effect. Write absolute state rather than deltas where the domain allows; otherwise deduplicate
   on a stable key with a unique constraint, not a check-then-insert. A pipeline that cannot be safely
   re-run cannot be recovered, and recovery is the common case.

2. DEFINE THE STAGE BOUNDARIES AND THEIR CONTRACTS.   Each stage reads a defined input, writes a defined
   output, and the two are validated. Boundaries are where failures become visible; a pipeline with one
   giant stage has one failure mode and no diagnosis.

3. VALIDATE THE SCHEMA AT EVERY HOP.   Not only at ingestion. Required fields, types, ranges, enum values,
   nullability, and the row count against an expected band. A schema change upstream that is not caught at
   the boundary becomes a silent wrong answer three stages later, where it is undiagnosable.

4. FAIL LOUDLY AND STOP.   A stage that encounters invalid data halts the pipeline and alerts, rather than
   dropping rows, coercing types or writing a partial result. Deciding to skip bad rows is a legitimate
   design choice — but it must be explicit, logged, counted and reported, never a default.

5. SEPARATE THE RAW, STAGING AND MART LAYERS.   Keep the immutable raw copy: it is the only way to
   reprocess after a transformation bug is fixed. Transform in staging, publish to the mart. A pipeline
   that overwrites its input cannot be replayed.

6. HANDLE LATE AND OUT-OF-ORDER DATA EXPLICITLY.   Watermarks, event time versus processing time, and a
   stated lateness window. Decide what happens to a record that arrives after the window: restated,
   quarantined or dropped — and record which.

7. MAKE BACKFILL A FIRST-CLASS OPERATION.   A parameterised date range, re-runnable, with the same code
   path as the normal run. A backfill implemented as a separate script is a second pipeline with its own
   bugs and no tests.

8. CONTROL CONCURRENCY AND PARTITIONING.   Partition by the natural key so runs do not contend; bound
   parallelism so the pipeline does not exhaust the source's connection limit or rate quota. Sum the
   connection pools across workers and compare against the source's ceiling.

9. OBSERVE EVERY STAGE.   Rows in, rows out, rows rejected and why, duration, bytes, cost, and the
   watermark. A stage whose row count changes unexpectedly is the earliest available signal, and it is
   cheap. Alert on the ratio, not only on failure.

10. MAKE THE COST VISIBLE.   Query cost, compute cost and storage growth per run. A pipeline whose cost
   doubles silently after a data growth is an operational surprise that arrives as a bill.

11. TEST WITH REAL-SHAPED DATA.   Empty and tiny inputs pass everything. Include the edge cases that
   actually occur: nulls in a required field, duplicate keys, unicode, extreme values, an empty partition,
   a partial upstream failure, and a re-run mid-stage.

12. PLAN THE RECOVERY BEFORE THE FAILURE.   How a failed run is restarted, how a partial write is rolled
   back or made idempotent, how a bad transformation is reverted and reprocessed from raw, and who is
   paged. Written down and rehearsed.
```

## Failure Modes

| Failure | Detection | Response |
|---|---|---|
| A re-run duplicated data | the stage is not idempotent | deduplicate on a stable key with a unique constraint |
| Wrong results three stages downstream | no validation at the boundary where the schema changed | validate at every hop, not only at ingestion |
| Partial result published | the stage wrote before validating | write to staging, publish only on success |
| Bad rows silently dropped | no reject count in the metrics | count, log and report rejects; make skipping explicit |
| Late data lost | no lateness policy | state the window and the action for records past it |
| Backfill behaved differently | a separate script | parameterise the normal path by date range |
| Source rate-limited or pool exhausted | parallelism unbounded | bound workers; sum pools against the source ceiling |
| Nobody noticed a row-count collapse | no ratio alert | alert on rows-in versus rows-out ratios |
| Cannot reprocess after a bug | the raw layer was overwritten | keep immutable raw; transform in staging |
| Cost doubled silently | no per-run cost metric | record cost per run and alert on drift |
| Tests passed, production failed | inputs were empty or tiny | test with real-shaped data and the edge cases |

## Quality Checklist

```text
□ every stage is idempotent and safe to re-run
□ stage boundaries and their contracts are defined
□ the schema is validated at every hop, not only at ingestion
□ invalid data halts the pipeline, or skipping is explicit, counted and reported
□ raw, staging and mart layers are separated, and raw is immutable
□ late and out-of-order data has a stated window and action
□ backfill is a parameterisation of the normal path
□ parallelism is bounded and connection pools are summed against the source ceiling
□ every stage reports rows in, out, rejected, duration and cost
□ alerts fire on ratio anomalies, not only on failure
□ tests use real-shaped data including the edge cases that occur
□ the recovery procedure is written down
```

## Anti-Patterns

```text
✗ A PIPELINE THAT CANNOT BE RE-RUN.   Then it cannot be recovered, and recovery is the common case.
✗ VALIDATION ONLY AT INGESTION.   The schema change that matters arrives mid-stream.
✗ SILENT ROW DROPPING.   The most expensive failure mode: the output looks correct and is incomplete.
✗ OVERWRITING THE RAW LAYER.   A transformation bug becomes permanent data loss.
✗ BACKFILL AS A SEPARATE SCRIPT.   A second pipeline with its own bugs and no tests.
✗ CHECK-THEN-INSERT DEDUPLICATION.   Two concurrent runs both pass the check; use a unique constraint.
✗ UNBOUNDED PARALLELISM.   The source's rate limit or connection ceiling is the real constraint.
✗ ALERTING ONLY ON FAILURE.   A stage that succeeds with a tenth of its rows is worse than one that fails.
✗ TESTING WITH EMPTY INPUTS.   Everything passes.
✗ NO COST VISIBILITY.   Growth becomes a bill before it becomes a ticket.
```

## References

- [`knowledge/backend/idempotency.md`](../../knowledge/backend/idempotency.md) — the patterns behind stage idempotency
- [`knowledge/databases/consistency-models.md`](../../knowledge/databases/consistency-models.md) · [`postgres-gotchas.md`](../../knowledge/databases/postgres-gotchas.md) · [`indexing-strategy.md`](../../knowledge/databases/indexing-strategy.md)
- [`knowledge/data-engineering/vector-search.md`](../../knowledge/data-engineering/vector-search.md) — the embedding-ingestion case
- [`knowledge/architecture/system-design-checklist.md`](../../knowledge/architecture/system-design-checklist.md) — failure modes and observability sections
- [`skills/rag-pipeline/SKILL.md`](../rag-pipeline/SKILL.md) · [`skills/database-design/SKILL.md`](../database-design/SKILL.md) · [`skills/migration/SKILL.md`](../migration/SKILL.md) · [`skills/deployment/SKILL.md`](../deployment/SKILL.md)
- [`patterns/data/`](../../patterns/data/) · [`anti-patterns/data/`](../../anti-patterns/data/) · [`failure-modes/`](../../failure-modes/)
- dbt — <https://github.com/dbt-labs/dbt-core> · Apache Airflow — <https://airflow.apache.org/docs/> · Dagster — <https://docs.dagster.io/>
