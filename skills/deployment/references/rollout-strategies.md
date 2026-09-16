---
id: rollout-strategies
title: "Progressive rollout strategies compared by cost, reversal speed and use case"
domain: devops
summary: >-
  Rolling, blue/green, canary, feature flag, shadow, immutable and recreate strategies with their costs and selection rules — extracted from the skill so the skill body stays inside its context budget.
status: active
confidence: medium
claim_type: recommendation
evidence_level: practitioner-experience
tags: [reference, devops]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related_skills: [deployment]
---

# Progressive rollout strategies compared by cost, reversal speed and use case

Reference material for [`deployment`](../SKILL.md), extracted so the skill body stays
within its context budget. Load this file only when the step that needs it is reached.


Choose per change, not per project. The choice is determined by **reversibility and blast radius**.

```text
ROLLING UPDATE      Replace instances gradually. Default for stateless services.
                    Cost: two versions run simultaneously → mixed-version compatibility required.
                    Reversal: redeploy the previous version; minutes.
                    Use when: the change is backwards compatible and low-risk.

BLUE/GREEN          Two full environments; switch traffic atomically.
                    Cost: double infrastructure during the window; database shared or migrated
                    in a compatible way.
                    Reversal: flip traffic back; seconds — the fastest reversal available.
                    Use when: you need instant rollback and can afford the capacity.

CANARY              Route a small percentage (or a chosen cohort) to the new version; compare
                    metrics against the control; expand or roll back automatically.
                    Requires: comparable cohorts, enough traffic for statistical signal, and
                    metrics that detect the failure modes you care about.
                    Cost: analysis infrastructure; a canary that nobody watches is a rolling update.
                    Use when: risk is real and traffic volume allows detection.

FEATURE FLAG        Deploy the code dark; enable the behaviour per user/tenant/percentage.
                    Separates DEPLOYMENT from RELEASE — the single highest-value practice here.
                    Cost: flag debt (flags must be removed), branching complexity, testing both states.
                    Use when: the behaviour is riskier than the code, or the release must be
                    coordinated with something outside engineering.

SHADOW / DARK       Run the new implementation alongside the old, compare outputs, serve the old.
                    Use when: correctness parity must be proven on real traffic (see migration).

IMMUTABLE INFRA     Never patch running instances; replace them from a versioned image.
                    This is a property, not a strategy — apply it always.

RECREATE            Stop the old, start the new. Downtime by definition.
                    Use when: stateful singletons that cannot run two versions, and only with
                    a maintenance window and sign-off.
```

Rules:

```text
1. Deployment ≠ release. Ship code dark, release behaviour deliberately. This decouples
   "is the build healthy" from "is the feature working", and it is what makes frequent
   deploys safe.
2. Mixed-version compatibility is mandatory for every strategy except recreate. Old instances
   must work with new ones and with the shared data store throughout the rollout.
3. Database changes are not deployed with application code. Expand first (see migration);
   the schema must be compatible with the previous application version at all times.
4. Reversal must be rehearsed, not assumed. A rollback path never tested is a hypothesis.
5. Automatic rollback on a breached metric beats a human noticing at 3 a.m.
```
