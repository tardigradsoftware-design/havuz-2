---
name: deployment
version: 1.0.0
description: >-
  Ship code to production safely — build reproducibility, progressive rollout strategies, health
  and readiness semantics, configuration and secrets handling, observability at deploy time, and
  a rehearsed rollback.
category: devops
status: active
confidence: high
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [deployment, ci-cd, rollout, rollback, configuration, observability, devops]
applies_to: [backend, infrastructure, web]
priority: 82
requires: [testing, release-engineering]
conflicts_with: []
estimated_tokens: 2752
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Rollout strategies
    anchor: "#rollout-strategies"
    purpose: decision
  - heading: Workflow
    anchor: "#workflow"
    purpose: implementation
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "The Twelve-Factor App"
    url: https://github.com/heroku/12factor
    type: github-repository
    organization: Heroku
    license: MIT
    confidence: high
    claim_type: recommendation
    verified_at: 2026-09-15
    note: "Config in environment, build/release/run separation, disposability, backing services as attached resources."
  - title: "OpenTelemetry"
    url: https://opentelemetry.io/
    type: specification
    organization: CNCF
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
related_skills: [release-engineering, testing, backend-engineering, security-audit, performance-audit, migration]
related_repositories: [argoproj/argo-cd, fluxcd/flux2, hashicorp/terraform, docker/buildx]
tests: 5
---

# Deployment

## Purpose

Make releasing **boring, frequent and reversible**. The goal is not a successful deploy; it is
a deploy process where a failure is detected in minutes, contained automatically, and rolled
back in seconds — so that shipping often becomes the safest option rather than the risky one.

## When to Use

```text
□ Any change reaching an environment other than a developer's machine
□ Designing or reviewing a CI/CD pipeline
□ Adding a new service, region, environment or runtime
□ After an incident whose root cause was the deploy process itself
□ When releasing has become a scheduled, stressful event
```

## When NOT to Use

```text
✗ Local development iteration — optimise that loop separately (fast, hot-reloading, no gates)
✗ As a substitute for a migration plan when data changes are involved (see migration)
```

## Inputs

```text
artifact         what is being deployed, and how it is built and versioned
environments     dev → preview → staging → production; what differs between them and why
rollback         how to go back, how fast, and what is irreversible (data, schema, external effects)
traffic control  load balancer, DNS, service mesh, feature-flag system — what can steer traffic
observability    what is measured at deploy time, and what triggers an automatic rollback
blast radius     who is affected if this goes wrong, and how quickly they would notice
```

## Rollout strategies

Choose per change, not per project. The choice is determined by **reversibility and blast radius**.

The full detail — every entry with its detection rule, severity and fix direction — lives in [`references/rollout-strategies.md`](references/rollout-strategies.md). Load it when this step is reached rather than keeping it in context for the whole run.

## Workflow

```text
BUILD → VERIFY → RELEASE → ROLLOUT → OBSERVE → SETTLE → (ROLLBACK)
```

### BUILD
```text
□ Reproducible: same commit → same artifact. Pinned base images, pinned toolchain,
  locked dependencies with integrity hashes, no network fetches at build time except
  from a trusted, pinned registry
□ Build once, promote the same artifact through environments. Rebuilding per environment
  means you tested something other than what you shipped
□ Versioned and content-addressed: immutable tag or digest; never `latest` in production
□ Provenance where available: signed artifacts, SBOM, build attestation
□ Secrets never in the image, the repo or the build log
□ Cache deliberately — but a cache that produces a different artifact is a bug
```

### VERIFY
```text
□ Gates in order, failing fast: lint → type-check → unit → integration → contract →
  component → e2e → security scan → dependency/license scan → build → smoke test
□ The artifact is smoke-tested after build, in an environment shaped like production
□ Migrations dry-run against a production-shaped copy
□ The pipeline itself is code, reviewed, and tested; a workflow change is a production change
□ Least-privilege CI credentials, short-lived, scoped per job; no long-lived production keys
□ PR pipelines cannot execute with production credentials or write to protected environments
```

### RELEASE
```text
□ Release notes generated from the change set, with migration notes for breaking changes
□ The deploy is one command or one merge, executable by anyone on the team, at any time
□ Preconditions checked automatically: migration state, config presence, dependency health,
  required approvals, on-call awareness
□ Config and secrets resolved at deploy time from the environment, validated at boot with a
  clear failure message — never baked into the artifact
□ Backwards-compatible config changes deployed before the code that uses them
```

### ROLLOUT
```text
□ Strategy chosen for this change and recorded (see above)
□ Progressive: percentage/cohort steps with dwell time between them, not one jump
□ Health gates between steps: readiness green, error rate flat, latency flat, saturation normal
□ Instant kill switch: traffic back to the previous version in seconds, without a rebuild
□ Announced where humans depend on it; changelog and internal comms updated
□ One change per rollout where possible — a bundled deploy is an undiagnosable deploy
```

### OBSERVE
```text
□ Deploy markers on every dashboard so a metric change can be attributed
□ Watch, per the strategy's dwell time: error rate, p95/p99 latency, saturation, business
  invariants (signups, orders, payments), and the specific metrics the change could affect
□ Logs, metrics and traces flowing from the new version immediately — a deploy without
  telemetry is unverifiable
□ Alerts on leading indicators, tuned so a real regression fires before users escalate
□ Automatic rollback wired to the breach condition
```

### SETTLE
```text
□ Old version retained and runnable until the observation window closes
□ Flags for a fully-released feature scheduled for removal (flag debt is real debt)
□ Temporary shims, dual-writes and compatibility layers removed on a date, not "later"
□ Deploy recorded: what, when, by whom, which strategy, which metrics moved
□ Retrospective when anything surprised you — including near misses
```

### ROLLBACK
```text
□ Trigger: a defined metric breach, or a human decision with a stated reason. Decide the
  triggers BEFORE the deploy — during an incident is too late
□ Roll back first, diagnose second. Restoring service precedes understanding
□ Verify the rollback: the metric recovers, the previous version is serving, no partial state
□ Data written by the bad version is reconciled or quarantined — rollback of code does not
  roll back effects
□ Irreversible changes (schema contraction, deleted data, sent emails, charged payments)
  have a forward-fix plan, not a rollback plan. This is why expansion precedes contraction
□ Post-rollback: the failing change is blocked from re-deploy until the cause is fixed and
  a regression test exists
```

## Failure Modes

```text
REBUILD PER ENVIRONMENT     Staging tested a different artifact than production received.
`latest` IN PRODUCTION      Non-reproducible, non-rollbackable.
CONFIG IN THE ARTIFACT      One build per environment; secrets in images.
UNVALIDATED CONFIG          The app boots, misbehaves, and the error surfaces as a business bug.
SCHEMA WITH CODE            Old instances meet a new schema mid-rollout.
NO MIXED-VERSION TESTING    Rolling update assumes compatibility it never verified.
UNWATCHED CANARY            A percentage rollout with no comparison is a slow rolling update.
HEALTH CHECK LYING          Readiness green while dependencies are broken; or liveness probing
                            dependencies, turning an outage into a restart storm.
NO DEPLOY MARKERS           A regression nobody can attribute to a release.
MANUAL ROLLBACK             Rollback requires a rebuild and 20 minutes.
EFFECT BLINDNESS            Code rolled back; the duplicate payments were not.
FLAG DEBT                   Forty live flags, nobody knows which are still needed.
PIPELINE AS A SNOWFLAKE     CI configuration changed without review, with production credentials.
WEEKEND HERO DEPLOYS        The process is a person, not a pipeline.
```

## Quality Checklist

```text
□ Artifact built once, reproducibly, content-addressed, promoted unchanged through environments
□ Dependencies and base images pinned with integrity hashes; provenance/SBOM where available
□ No secrets in image, repo, logs or build output; config resolved at deploy time
□ Required config validated at boot with actionable failure messages
□ Gates run in order and fail fast; artifact smoke-tested in a production-shaped environment
□ Migrations dry-run against a production-scale copy; schema changes compatible with the
  previous application version
□ Rollout strategy chosen per change, recorded, with progressive steps and dwell time
□ Readiness depends on real dependencies; liveness does not (no restart storms)
□ Instant kill switch verified by rehearsal, not assumed
□ Deploy markers on dashboards; error rate, p99 latency, saturation and business invariants watched
□ Automatic rollback wired to pre-agreed metric breaches
□ Rollback rehearsed end to end, including reconciliation of effects written by the bad version
□ Mixed-version compatibility tested in both directions
□ Old version retained and runnable through the observation window
□ Flags, shims and compatibility layers scheduled for removal with dates
□ CI credentials least-privilege and short-lived; pipeline changes reviewed like production code
□ Every deploy recorded: what, when, who, strategy, metrics moved
```

## Anti-Patterns

```text
✗ `docker pull app:latest` on a production host
✗ A `.env` file baked into the image
✗ Deploying the schema migration in the same release as the code that uses it
✗ A canary at 5% that nobody monitors
✗ A liveness probe that queries the database
✗ "Roll back" meaning "rebuild the previous commit"
✗ Friday evening deploys by one person who knows the steps
✗ A CI workflow with a long-lived production key in a repository secret
✗ Leaving the compatibility shim in place "just in case", forever
```

## References

- [`release-engineering`](../release-engineering/SKILL.md) · [`migration`](../migration/SKILL.md)
- [`backend-engineering`](../backend-engineering/SKILL.md) · [`testing`](../testing/SKILL.md)
- [`security-audit`](../security-audit/SKILL.md) — CI/CD supply chain
- [`workflows/release-checklist/`](../../workflows/release-checklist/) · [`knowledge/devops/`](../../knowledge/devops/)
- [`knowledge/infrastructure/`](../../knowledge/infrastructure/)
- Twelve-Factor — <https://github.com/heroku/12factor> · OpenTelemetry — <https://opentelemetry.io/>

## Related Skills

`release-engineering` · `testing` · `migration` · `backend-engineering` · `security-audit` ·
`performance-audit`

## Evaluation Criteria

```text
1. Deploy frequency: deploys per week (higher is better, given the other metrics hold).
2. Lead time: commit to production (median and p95).
3. Change failure rate: fraction of deploys requiring remediation (target < 5%).
4. Time to restore: median minutes from detection to service restored (target < 15).
5. Reproducibility: the same commit always produces the same artifact digest.
6. Rollback success: 100% of rehearsed rollbacks succeed within the stated time.
7. Attribution: 100% of production regressions traceable to a specific deploy via markers.
```

Test cases in [`tests/`](tests/).
