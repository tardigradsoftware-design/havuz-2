---
name: migration
version: 1.0.0
description: >-
  Move a live system from one state to another without a big-bang cutover — expand, migrate,
  contract, with dual writes, backfills, feature flags, rehearsed rollback and verifiable parity.
category: coding
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [migration, upgrade, cutover, data-migration, backward-compatibility, rollout]
applies_to: [any]
priority: 84
requires: [project-planning, testing, deployment]
conflicts_with: []
estimated_tokens: 3249
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Expand-migrate-contract
    anchor: "#expand-migrate-contract"
    purpose: implementation
  - heading: Workflow
    anchor: "#workflow"
    purpose: implementation
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "Strangler Fig Application (Martin Fowler)"
    url: https://martinfowler.com/bliki/StranglerFigApplication.html
    type: methodology
    organization: Martin Fowler
    confidence: high
    claim_type: recommendation
    verified_at: 2026-09-15
    note: "Not fetched in this run; verify before citing specifics."
related_skills: [project-planning, testing, deployment, release-engineering, database-design, refactoring]
related_repositories: [flyway/flyway, liquibase/liquibase, golang-migrate/migrate]
tests: 26
---

# Migration

## Purpose

Change a system that is running, has data, and has users — without a moment where it is
broken. The core technique is the same for schema changes, framework upgrades, vendor
switches, data moves and rewrites: **run both, prove parity, move the traffic, remove the old.**

Big-bang cutovers fail because they concentrate every risk into one unrehearsable moment.

## When to Use

```text
□ Database schema changes on a live system
□ Moving data between stores, formats, schemas or tenants
□ Framework or language major-version upgrades
□ Replacing a vendor, a service, a payment provider or an auth system
□ Rewriting a module or an entire application incrementally
□ Any change where "we'll just switch it over on Saturday" is the proposed plan
```

## When NOT to Use

```text
✗ A greenfield system with no data and no users — just change it
✗ A reversible, low-blast-radius change behind a normal deploy
✗ When the honest answer is "delete it": removing a system is a different plan
```

## Inputs

```text
from / to          the exact current state and the exact target state, both versioned
invariants         what must never be wrong during the migration (money, auth, identity, ordering)
data               volume, shape, quality, edge cases, orphan/invalid rows, encoding
consumers          everything that reads or writes the thing being migrated, including reports,
                   analytics, backups, third parties and humans with SQL access
rollback           how far back you can go at each stage, and what it costs
window             allowed downtime (usually none), maintenance windows, deadline
detection          how you will know it is going wrong, in minutes not days
```

## Expand-migrate-contract

The universal shape. Each phase is independently deployable and independently reversible.

```text
PHASE 1 — EXPAND            make the new possible without removing the old
  □ Add the new column/table/endpoint/service alongside the existing one, nullable/optional
  □ No reader depends on it yet; no writer is required to fill it
  □ Backwards compatible by construction: old code paths keep working unchanged
  □ Deploy and verify stability BEFORE any behaviour depends on it
  □ No long locks: use the online/concurrent variant your engine offers for index and
    default additions; adding NOT NULL + default to a large table can lock it

PHASE 2 — MIGRATE           make the new correct and used
  □ DUAL WRITE: every write goes to both old and new. Old remains the source of truth.
    Dual writes must be idempotent, ordered-safe, and must not fail the request when the
    new side fails (log, alert, reconcile) — decide and document which side wins on conflict.
  □ BACKFILL: copy existing data to the new side in batches — resumable, progress-logged,
    bounded transaction size, rate-limited so it does not degrade production, re-runnable
    after interruption, and verified with a reconciliation job that counts and checksums.
  □ SHADOW READ: read both, return the old, compare and log differences. This is the parity
    proof, and it runs on real traffic at real volume. Diff rate must go to ~0 before the
    next step.
  □ SWITCH READS: move reads to the new side, behind a flag, per-tenant or per-percentage,
    with an instant kill switch back to the old.
  □ SWITCH SOURCE OF TRUTH: the new side becomes authoritative; the old becomes the shadow.
    Keep the ability to reverse for a defined period.

PHASE 3 — CONTRACT          remove the old
  □ Stop dual writes only after the old side has been unused for the full observation window
  □ Verify nothing reads the old side: logs, query counts, dependency checks — not assumptions.
    Include reports, analytics exports, backups, cron jobs, other teams' services and
    humans with direct database access.
  □ Rename/alias so the new side takes the old name if consumers depend on it
  □ Drop the old column/table/endpoint in a SEPARATE, later deploy — never in the same
    release that stops writing it
  □ Remove the flags, the shims, the reconciliation jobs and the migration code
  □ Update documentation, runbooks and tests; delete the now-dead migration path
```

Rules that apply throughout:

```text
1. EVERY PHASE IS A SEPARATE DEPLOY. Combining phases removes the rollback boundary.
2. EVERY PHASE IS REVERSIBLE until the last one. The contract phase is the point of no
   return — say so explicitly in the plan and get sign-off before it.
3. FORWARD COMPATIBILITY FIRST. Deployments during a migration are mixed-version: old code
   must work with the new schema and new code with old data. Both directions, tested.
4. FLAGS OVER REDEPLOYS. Every switch is a flag that can be flipped in seconds, per cohort.
5. IDEMPOTENCY. Every step can be re-run safely after a crash, a timeout or a partial failure.
6. RECONCILE CONTINUOUSLY. Counts, checksums, sampled deep comparisons — running during the
   migration, not after it.
7. NOTHING IS DONE UNTIL MEASURED. "The backfill finished" means the reconciliation reports
   parity, not that the job exited 0.
```

## Workflow

```text
INVENTORY → PLAN → REHEARSE → EXPAND → MIGRATE → OBSERVE → CONTRACT → RETROSPECT
```

```text
1 INVENTORY   Enumerate every consumer, every data shape, every edge case. Query the actual
              data for the cases you assume do not exist (NULLs, empty strings, invalid dates,
              orphan FKs, duplicates, unicode, out-of-range values). They exist.
2 PLAN        Write the three phases as separate deploys with gates:
              gate = the measurable condition to proceed (diff rate, backfill completeness,
              error rate, latency, reconciliation parity).
              Include rollback per phase, the observation window, and the stop conditions.
3 REHEARSE    Run the whole migration against a COPY OF PRODUCTION DATA at production volume,
              including the rollback. Time it. A migration rehearsed on 500 rows teaches nothing
              about 50M. Rehearse the failure paths: kill the backfill mid-run, flip the flag
              back, restore from the pre-migration point.
4 EXPAND      Deploy phase 1. Verify stability for a defined period before continuing.
5 MIGRATE     Dual write → backfill → shadow read → switch reads → switch source of truth.
              Each sub-step behind a flag, each with its gate.
6 OBSERVE     Dashboards for: diff rate, error rate, latency, backfill progress, reconciliation
              results, business invariants (totals, balances, counts that must match).
              Alerts on leading indicators. A migration without a diff-rate dashboard is flying blind.
7 CONTRACT    Only after the observation window with zero unexplained diffs. Separate deploy.
              Then a later deploy to drop the old structures.
8 RETROSPECT  Record: what the rehearsal missed, what the edge cases actually were, how long each
              phase took, what the rollback would have cost. File it in gotchas/ or decision-records/.
```

## Data-quality specifics

```text
□ Profile before migrating: distributions, NULL rates, duplicate keys, referential orphans,
  value ranges, encoding. Fix or explicitly accept each anomaly BEFORE the migration,
  not during it.
□ Never migrate and transform and clean in one step. Clean → verify → migrate → verify.
  One change per phase, or you cannot attribute a failure.
□ Preserve the ability to re-run from scratch: the migration is a program, not a one-off script.
□ Keep an audit trail: what changed, when, by which run, with which input snapshot.
□ Timezones, encodings, collations and numeric precision are where silent corruption lives.
  Test them explicitly with adversarial values.
□ Immutable identifiers: never reuse or reassign an ID during a migration.
□ Partial-failure semantics: define what the user sees when a row cannot be migrated
  (skip + report, block + alert, or quarantine). Never silently drop.
```

## Failure Modes

```text
BIG-BANG CUTOVER          One unrehearsable moment holding all the risk.
REHEARSAL ON TOY DATA     Passes on 500 rows; fails on 50M (duration, locks, memory, edge cases).
PHASES IN ONE DEPLOY      No rollback boundary; a failure requires a full revert of everything.
NON-IDEMPOTENT BACKFILL   A crash mid-run leaves a half-migrated, unrecoverable state.
UNBOUNDED BACKFILL        One transaction over the whole table; locks and replication lag.
NO SHADOW READ            Parity assumed instead of measured; differences discovered by users.
PREMATURE CONTRACT        Dropping the old column in the same release that stopped writing it.
FORGOTTEN CONSUMERS       A report, cron job, backup or another team's service still reads the old path.
MIXED-VERSION IGNORANCE   Old code meets the new schema during rollout and breaks.
FLAG WITH NO KILL SWITCH  The switch requires a deploy, not a flip.
NO RECONCILIATION         "It exited successfully" as the parity proof.
MIGRATE + CLEAN AT ONCE   Two changes, one failure, no attribution.
SILENT ROW DROPS          Unmigratable rows skipped with no report.
UNDOCUMENTED POINT OF NO RETURN  The contract phase executed without sign-off.
```

## Quality Checklist

```text
□ From/to states versioned; invariants named; all consumers enumerated (including reports,
  crons, backups, other teams, direct SQL access)
□ Real data profiled; anomalies fixed or explicitly accepted before migrating
□ Three phases planned as separate deploys, each with a measurable gate and a rollback
□ Rehearsed against production-scale data, timed, including rollback and failure paths
□ No long locks: online/concurrent DDL variants used; backfill batched, resumable, rate-limited
□ Dual writes idempotent, conflict-resolved and documented; a failure on the new side does
  not fail the request
□ Shadow read runs on real traffic; diff rate measured and driven to ~0 before switching reads
□ Read switch behind a flag with per-cohort rollout and an instant kill switch
□ Reconciliation (counts, checksums, sampled deep compares) running throughout
□ Business-invariant dashboards and leading-indicator alerts in place
□ Mixed-version compatibility tested in both directions
□ Contract phase only after the observation window; sign-off recorded; point of no return stated
□ Old structures dropped in a later, separate deploy
□ Flags, shims, reconciliation jobs and migration code removed at the end
□ Docs, runbooks and tests updated; retrospective filed
```

## Anti-Patterns

```text
✗ "We'll do it Saturday at 2 a.m. with the team on a call"
✗ Dropping the old column in the same migration that stops writing it
✗ A backfill script run by hand, once, with no log and no resume
✗ Rehearsing on the development database
✗ Declaring success because the job exited 0
✗ Migrating and renaming and re-typing in one step
✗ A feature flag that requires a redeploy to flip
✗ Forgetting the analytics warehouse that reads the table directly
✗ Silently skipping rows that failed validation
```

## References

- [`project-planning`](../project-planning/SKILL.md) · [`deployment`](../deployment/SKILL.md)
- [`release-engineering`](../release-engineering/SKILL.md) · [`database-design`](../database-design/SKILL.md)
- [`refactoring`](../refactoring/SKILL.md) · [`testing`](../testing/SKILL.md)
- [`workflows/release-checklist/`](../../workflows/release-checklist/) · [`patterns/architecture/`](../../patterns/architecture/)
- Strangler Fig — <https://martinfowler.com/bliki/StranglerFigApplication.html>
- [`decision-records/`](../../decision-records/) — record the point of no return

## Related Skills

`project-planning` · `testing` · `deployment` · `release-engineering` · `database-design` ·
`refactoring` · `debugging`

## Evaluation Criteria

```text
1. Zero-downtime: no user-visible outage attributable to the migration (or the planned
   downtime window is met exactly).
2. Parity: reconciliation reports 0 unexplained differences before contract.
3. Reversibility: every phase before contract demonstrably rolled back in rehearsal.
4. Invariant preservation: named business invariants hold continuously through the migration.
5. Rehearsal fidelity: production-scale rehearsal predicted the real duration within a stated margin.
6. Cleanliness: 0 flags, shims or dual-write paths left behind after contract.
```

Test cases in [`tests/`](tests/).
