---
name: performance-review
version: 1.0.0
description: >-
  Establish whether a system meets its budget for its real users — baseline lab and field, profile
  end to end, rank by measured cost, fix in remove-first order, verify with the same method, and
  enforce the budget in CI so the gain does not decay.
trigger: >-
  Latency, throughput or page-load complaints backed by a symptom; a measured regression with a
  known approximate date; capacity planning for a known event; before scaling infrastructure; when
  setting budgets for a new product or redesign.
not_for: >-
  Optimising a path with negligible traffic; a correctness defect (use workflows/bug-investigation
  first — a fast wrong answer is worse); micro-optimisation where cost is dominated by a network
  call; a UX or design problem misreported as "slow".
status: active
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [performance, profiling, latency, core-web-vitals, budgets, workflow]
confidence: high
claim_type: recommendation
evidence_level: cross-checked
estimated_duration: half a day for a focused regression; days for a full system review
stages:
  - id: 1
    name: Agree the budget and the population
    goal: Fix the numbers and who they must hold for, because without them the work has no stopping condition.
    skill: performance-audit
    agent: performance-engineer
    inputs: [product requirements, user analytics, device and network distribution, cost constraints]
    outputs: [numeric budget per metric — latency p50/p95/p99, throughput at an acceptable error rate, Core Web Vitals, resource ceilings, cost per 1k requests; target population segmented by device, network, geography, tenant and data volume]
    exit_gate: Every metric has a number and every number has a named population segment. A global target without segments hides the users actually complaining.
    on_gate_failure: Refuse to proceed. Optimising without a budget never finishes and proves nothing; escalate to the owner for the numbers.
  - id: 2
    name: Capture the baseline
    goal: Measure the current state in both lab and field, with method, environment and date recorded.
    skill: performance-audit
    inputs: [budget, workload shape, target population, test environment]
    outputs: [lab baseline — reproducible controlled runs; field baseline — real-user percentiles by segment; recorded method, environment and date for each]
    exit_gate: Both baselines exist, percentiles are reported by segment rather than as means only, and the method is documented precisely enough that a second engineer could reproduce the numbers.
    max_loops: 2
    on_gate_failure: Add instrumentation before continuing. Without a baseline there is no way to know whether any later change helped.
  - id: 3
    name: Profile and attribute
    goal: Find where the time actually goes, before changing any code.
    skill: performance-audit
    inputs: [baseline, traces, logs, profilers, network waterfall, bundle analysis]
    outputs: [ranked attribution — component, measured cost, share of the budget, evidence; query counts per request; main-thread work; saturation points; network serial dependencies]
    exit_gate: Every budget breach is attributed to a named component with a measured share of cost, and the top items account for the majority of the breach.
    max_loops: 3
    on_gate_failure: Instrument deeper at the boundary of the suspected subsystem. Attributing by intuition leads to optimising the cold path.
  - id: 4
    name: Rank and select
    goal: Decide what to fix, in what order, and explicitly what not to fix.
    skill: performance-audit
    inputs: [ranked attribution, effort estimates, risk of each change]
    outputs: [ordered remediation list by traffic share times per-request cost divided by effort, with the not-fixed items and their reasons]
    exit_gate: The list is ordered by measured impact rather than by ease, the top item is addressed completely before the second begins, and every item below the noise floor is listed as not-fixed with a reason.
    on_gate_failure: Re-rank against traffic data. Effort spent on a path nobody uses is the most common waste in performance work.
  - id: 5
    name: Fix in remove-first order
    goal: Apply the cheapest, highest-yield class of fix before reaching for infrastructure.
    skill: performance-audit
    agent: performance-engineer
    inputs: [ordered remediation list, budget]
    outputs: [changes applied in order — REMOVE work, then do it LESS (cache, batch, dedupe, paginate, lazy-load, split), EARLIER (preload, parallelise, warm pools), CLOSER (CDN, edge, replica), CHEAPER (algorithm, index, keyset, streaming), and only then MORE (scale)]
    exit_gate: Each applied fix references the measured share of cost it addresses, and scaling infrastructure was not chosen while removal or reduction options remained unexhausted.
    max_loops: 4
    on_gate_failure: Return to stage 3. A fix that does not correspond to a measured cost is a guess, and guesses compound.
  - id: 6
    name: Verify with the same method
    goal: Prove the improvement on the same workload, in the same environment, at realistic peak.
    skill: testing
    inputs: [baseline method, budget, workload at 2x expected peak, target segments]
    outputs: [after-measurement by segment, delta per metric, regression check on error rate, memory, cost and correctness, field confirmation]
    exit_gate: The same method and workload as the baseline were used, percentiles by segment are reported, the run covers at least 2x expected peak, and no other metric regressed.
    max_loops: 3
    on_gate_failure: Revert or continue fixing. A latency improvement that raises error rate or cost is a regression, not a win.
  - id: 7
    name: Confirm in the field
    goal: Check that the lab gain appears in real-user data, which is the only evidence about experience.
    skill: performance-audit
    inputs: [field baseline, deployed change, RUM or telemetry data]
    outputs: [field deltas by segment over a defined observation window, with the segments that did not improve identified]
    exit_gate: The affected segments show improvement in field data over the observation window, or the discrepancy between lab and field is explained — usually the lab measured something users do not do.
    max_loops: 2
    on_gate_failure: Re-profile against the field workload shape. A lab-only win is a measurement artefact until real users confirm it.
  - id: 8
    name: Enforce the budget
    goal: Prevent the gain from decaying with the next ten feature merges.
    skill: deployment
    agent: performance-engineer
    inputs: [budget, affected routes and endpoints, CI configuration]
    outputs: [CI budget gates that fail the build on regression, bundle-size gates, Lighthouse or k6 runs on affected routes, dashboards and alerts on p95/p99, review requirement for new endpoints, queries and third-party scripts]
    exit_gate: Budget breaches fail CI rather than being noticed later, dashboards alert on p95 and p99 rather than on means, and a re-measurement date is scheduled.
    on_gate_failure: Add the gate manually for the affected paths. Performance without enforcement is a one-off event, and it decays at the rate of feature addition.
quality_gates:
  - Numeric budget agreed per metric, with a named population segment, before any measurement.
  - Baseline captured in both lab and field, with method, environment and date recorded.
  - Percentiles reported by segment; no mean-only reporting.
  - Cost attributed by trace or profile before any code change.
  - Remediation ranked by measured impact, with not-fixed items and reasons listed.
  - Fixes applied in remove-first order; scaling chosen only after reduction is exhausted.
  - Verification uses the identical method and workload, at 2x or more of expected peak.
  - No regression in error rate, memory, cost or correctness.
  - Field data confirms the lab result for the affected segments.
  - Budgets enforced in CI; dashboards alert on p95/p99.
  - Re-measurement scheduled, because performance decays with feature additions.
artifacts:
  - budget and population definition
  - lab and field baselines with method, environment and date
  - ranked profile attribution with evidence
  - ordered remediation list with not-fixed items and reasons
  - applied changes, each referencing its measured cost share
  - after-verification by segment with regression checks
  - field confirmation over the observation window
  - CI budget gates, dashboards, alerts and re-measurement date
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
sources:
  - title: "web.dev — Core Web Vitals"
    url: https://web.dev/articles/vitals
    type: official-docs
    organization: Google Chrome team
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Metric names and thresholds are revised periodically; verify current values before quoting numbers."
  - title: "Lighthouse"
    url: https://github.com/GoogleChrome/lighthouse
    type: github-repository
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
  - title: "OpenTelemetry"
    url: https://opentelemetry.io/
    type: specification
    organization: CNCF
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
related: [agents/performance-engineer/AGENT.md, skills/performance-audit/SKILL.md, knowledge/performance/]
---

# Workflow: Performance Review

```text
1 BUDGET+POPULATION → 2 BASELINE → 3 PROFILE → 4 RANK → 5 FIX (remove first)
  → 6 VERIFY (same method) → 7 FIELD CONFIRMATION → 8 ENFORCE IN CI
```

## The discipline in one line

**No budget, no audit. No profile, no change. No same-method verification, no claim.**

## Why stage 1 can refuse

A performance request without a number has no stopping condition, so it either never finishes or
stops arbitrarily — and either way it cannot be shown to have helped. Stage 1 exists to convert
"make it faster" into "p99 checkout latency under 400 ms on mid-range Android over 4G, at 50
concurrent users, within the existing infrastructure budget."

## Why the fix order is fixed

```text
REMOVE      Deleting work is free, permanent and cannot regress. Nothing else has those properties.
LESS        Caching, batching, deduplication, pagination, code-splitting — high yield, moderate risk.
EARLIER     Preload, parallelise, warm pools — improves perceived latency more than actual cost.
CLOSER      CDN, edge, replicas — real gains, real operational and cost complexity.
CHEAPER     Algorithms, indexes, keyset pagination, streaming — the classical optimisations.
MORE        Scaling multiplies cost without fixing cause. It is last because it is the only option
            that makes the problem more expensive rather than smaller.
```

Reaching for MORE first is the most expensive possible ordering, and it is the default when no
order is specified.

## Scaling

```text
SINGLE REGRESSION        stages 1 (reuse the existing budget), 2, 3, 5, 6, 8
PRE-LAUNCH BUDGET SET    stages 1, 2, 8 — set the numbers and the gates before there is traffic
CAPACITY PLANNING        stages 1, 2, 3, 6 at projected load — no fixes, only the projection
FULL SYSTEM REVIEW       all stages, all segments
FRONTEND-ONLY            stages 1, 2, 3 (waterfall, bundle, render path), 5, 6, 7, 8
```

## Failure modes specific to this workflow

```text
NO BUDGET              Optimising without a target; the work never finishes and proves nothing.
MEAN-BASED REVIEW      Averages reported while the p99 users are the ones complaining.
LAB-ONLY EVIDENCE      A Lighthouse score improved; real users saw nothing. Stage 7 catches this.
COLD-PATH OPTIMISATION Effort spent on a path whose traffic share is negligible.
GUESS-DRIVEN FIXING    Rewriting the module that feels slow without a profile.
SCALE-FIRST            Adding infrastructure before removing work — the most expensive ordering.
PARTIAL VERIFICATION   Measuring a different workload than the baseline; the comparison is meaningless.
REGRESSION BLINDNESS   Latency improved while error rate, memory or cost regressed.
NO ENFORCEMENT         The budget is re-breached in the next release because nothing gates it.
```

## References

- [`skills/performance-audit/SKILL.md`](../../skills/performance-audit/SKILL.md) — the detailed method and the "where the time goes" catalogue
- [`agents/performance-engineer/AGENT.md`](../../agents/performance-engineer/AGENT.md)
- [`skills/frontend-implementation/SKILL.md`](../../skills/frontend-implementation/SKILL.md) · [`skills/backend-engineering/SKILL.md`](../../skills/backend-engineering/SKILL.md)
- [`skills/database-design/SKILL.md`](../../skills/database-design/SKILL.md) · [`skills/deployment/SKILL.md`](../../skills/deployment/SKILL.md)
- [`knowledge/performance/`](../../knowledge/performance/) · [`knowledge/databases/`](../../knowledge/databases/)
- [`workflows/bug-investigation/WORKFLOW.md`](../bug-investigation/WORKFLOW.md)
