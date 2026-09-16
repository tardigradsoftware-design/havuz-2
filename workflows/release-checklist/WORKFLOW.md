---
name: release-checklist
version: 1.0.0
description: >-
  Take a change from merged to production and settled — version and changelog discipline, reproducible
  build, progressive rollout with health gates, instant rollback rehearsed, observation against
  leading indicators, and cleanup of flags and shims afterwards.
trigger: >-
  Any change reaching production or a published artifact; a scheduled release train; a hotfix under
  time pressure; a major version with breaking changes; or a release whose rollback path has never
  been exercised.
not_for: >-
  Local development iteration; a data migration, which needs workflows/../migration discipline on top
  of this one; a change with no consumer and no environment beyond a developer machine.
status: active
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [release, deployment, versioning, changelog, rollback, rollout, workflow]
confidence: high
claim_type: recommendation
evidence_level: practitioner-experience
estimated_duration: 30 minutes for a routine patch; days for a major version with a migration guide
stages:
  - id: 1
    name: Classify the change
    goal: Determine the version bump, the risk class and the rollout strategy the change actually requires.
    skill: release-engineering
    inputs: [commits and PRs since the last release, public-surface definition, breaking-change list]
    outputs: [change classification per item — breaking, feature, fix, deprecation, security; derived SemVer bump; risk class; chosen rollout strategy]
    exit_gate: Every change is classified against the written public-surface definition, the version bump follows from the classification rather than from preference, and any breaking change forces a MAJOR bump without exception.
    max_loops: 2
    on_gate_failure: Resolve the classification dispute before releasing. A SemVer lie destroys consumer trust more thoroughly than any bug.
  - id: 2
    name: Prepare the release notes
    goal: Tell the consumer whether they need to act, and exactly what to do if they do.
    skill: documentation
    inputs: [classified changes, migration requirements, deprecation timers]
    outputs: [CHANGELOG entry grouped Added/Changed/Deprecated/Removed/Fixed/Security, with before-and-after code for every breaking change; migration guide for a MAJOR release]
    exit_gate: Every entry answers "do I need to do anything?", every breaking change has a migration path with code, every deprecation names its removal version and date, and no entry reads "various fixes" or "improvements".
    max_loops: 2
    on_gate_failure: Rewrite. A changelog that is a git log with headings forces every consumer to read the diff.
  - id: 3
    name: Verify the gates
    goal: Confirm the artifact is correct before it is built for release, not after.
    skill: testing
    agent: qa-engineer
    inputs: [the release candidate, full test suite, security and dependency scans]
    outputs: [green gate results in order — lint, type-check, unit, integration, contract, component, e2e, security scan, dependency and license scan; smoke test of the built artifact in a production-shaped environment; migration dry-run against a production-scale copy]
    exit_gate: All gates pass in order with fail-fast behaviour, the built artifact has been smoke-tested rather than only the source, and migrations have been dry-run at production scale.
    max_loops: 3
    on_gate_failure: Do not release. A hotfix under pressure still requires the gates that apply to its risk class; the reduced set is recorded, not assumed.
  - id: 4
    name: Build reproducibly
    goal: Produce one artifact, immutable and promotable, that is identical to what was tested.
    skill: deployment
    inputs: [the verified commit, pinned dependencies, base images, toolchain]
    outputs: [content-addressed artifact with an immutable tag or digest, SBOM, signature where available, recorded build inputs]
    exit_gate: The artifact is built once and promoted unchanged through environments; dependencies and base images are pinned with integrity hashes; no secret appears in the image, the repository or the build log; and the same commit reproduces the same digest.
    max_loops: 2
    on_gate_failure: Fix the build. Rebuilding per environment means the tested artifact and the shipped artifact are different things.
  - id: 5
    name: Confirm rollback before rollout
    goal: Know how to go back, how fast, and what cannot be undone — before there is a reason to need it.
    skill: deployment
    inputs: [artifact, previous version, migration state, external effects]
    outputs: [documented rollback procedure with its measured duration, the instant kill switch verified, the list of irreversible effects with their forward-fix plans, and a rehearsal record]
    exit_gate: The previous version is retained and runnable, the kill switch has been exercised rather than assumed, and every irreversible effect — schema contraction, deleted data, sent messages, charged payments — has a forward-fix plan instead of a rollback plan.
    max_loops: 2
    on_gate_failure: Do not roll out. A rollback path never tested is a hypothesis, and it is tested during the incident if not before.
  - id: 6
    name: Deploy configuration first
    goal: Land the backwards-compatible prerequisites so the code deploy is not also a configuration deploy.
    skill: deployment
    inputs: [required configuration, feature flags in their off state, schema expansions]
    outputs: [configuration applied and validated, flags created dark, schema expanded compatibly with the previous application version]
    exit_gate: Every required configuration value is present and validated at boot with an actionable failure message; flags exist in their off state; and the schema remains compatible with the currently running version.
    on_gate_failure: Fix configuration before deploying code. An app that boots with missing configuration and fails later produces a business bug instead of a deploy failure.
  - id: 7
    name: Roll out progressively
    goal: Expose the change to a small, comparable cohort first and expand only on evidence.
    skill: deployment
    inputs: [artifact, rollout strategy, traffic controls, health gates]
    outputs: [rollout steps with dwell time per step, health-gate results at each step — readiness green, error rate flat, latency flat, saturation normal, business invariants holding]
    exit_gate: Each step passes its health gate before the next begins, mixed-version compatibility holds throughout, and the rollout can be halted at any step by flipping the kill switch.
    max_loops: 3
    on_gate_failure: Halt and roll back. A canary nobody compares is a slow rolling update, and a breached gate is a decision already made.
  - id: 8
    name: Observe against leading indicators
    goal: Detect a problem from telemetry before users report it.
    skill: deployment
    agent: performance-engineer
    inputs: [dashboards, deploy markers, alerts, business invariant metrics]
    outputs: [observation record over the dwell window — error rate, p95 and p99 latency, saturation, business invariants, and the specific metrics this change could affect; deploy marker attribution confirmed]
    exit_gate: The observation window has elapsed with metrics flat or improved, deploy markers make attribution possible, and alerts fired on nothing that required action.
    max_loops: 2
    on_gate_failure: Roll back first, diagnose second. Restoring service precedes understanding; the artifact and telemetry remain for analysis afterwards.
  - id: 9
    name: Publish and announce
    goal: Make the release discoverable and upgradeable by its consumers.
    skill: release-engineering
    inputs: [published artifact, changelog, migration guide, support window]
    outputs: [immutable tag, registry publication verified by a clean-environment install, versioned documentation published, announcement with the migration guide, updated support window and EOL dates]
    exit_gate: The published artifact has been installed and exercised from a clean environment, the tag is immutable, the documentation states which version it describes, and the support window is published with dates.
    max_loops: 2
    on_gate_failure: Re-publish. Assuming the upload succeeded because CI was green is how consumers discover the release first.
  - id: 10
    name: Settle and clean up
    goal: Close the release rather than leaving it half-finished, and learn from it.
    skill: release-engineering
    agent: skill-curator
    inputs: [rollout record, observation data, flags and shims inventory, incidents and near misses]
    outputs: [fully-released flags scheduled for removal with dates, temporary shims and compatibility layers dated for deletion, release record — what, when, by whom, which strategy, which metrics moved, retrospective with the estimate-versus-actual delta and any surprise]
    exit_gate: Every flag and shim has a removal date rather than an indefinite lifetime, the release record is complete, and any surprise is captured as a gotcha, a failure mode or a gate improvement.
    on_gate_failure: File the removal dates at minimum. Flag debt is real debt, and forty live flags nobody understands is a future incident.
quality_gates:
  - Every change classified against the written public-surface definition; breaking changes force MAJOR.
  - Changelog answers "do I need to act?" per entry; every breaking change has migration code.
  - All gates pass in order; the built artifact is smoke-tested, not only the source.
  - Migrations dry-run against a production-scale copy; schema stays compatible with the running version.
  - Artifact built once, reproducibly, content-addressed, promoted unchanged; no secrets in image or logs.
  - Rollback rehearsed and timed before rollout; irreversible effects have forward-fix plans.
  - Configuration validated at boot and deployed before the code that uses it.
  - Progressive rollout with health gates at every step; mixed-version compatibility verified.
  - Kill switch exercised, not assumed.
  - Observation window elapsed with metrics flat or improved; deploy markers enable attribution.
  - Published artifact verified by a clean-environment install; documentation versioned.
  - Flags and shims carry removal dates; release record and retrospective filed.
artifacts:
  - change classification and derived version bump
  - CHANGELOG entry and migration guide
  - gate results and artifact smoke test
  - content-addressed artifact with SBOM and signature
  - rollback procedure with measured duration and rehearsal record
  - configuration and flag prerequisites
  - rollout record with per-step health gates
  - observation record with deploy-marker attribution
  - published tag, verified install and versioned documentation
  - flag and shim removal schedule, release record and retrospective
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
sources:
  - title: "Semantic Versioning 2.0.0"
    url: https://semver.org/
    type: specification
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
  - title: "Keep a Changelog"
    url: https://keepachangelog.com/en/1.1.0/
    type: methodology
    confidence: high
    claim_type: recommendation
    verified_at: 2026-09-15
  - title: "The Twelve-Factor App"
    url: https://github.com/heroku/12factor
    type: github-repository
    license: MIT
    confidence: high
    claim_type: recommendation
    verified_at: 2026-09-15
related: [skills/release-engineering/SKILL.md, skills/deployment/SKILL.md, skills/migration/SKILL.md, agents/qa-engineer/AGENT.md]
---

# Workflow: Release Checklist

```text
1 CLASSIFY → 2 RELEASE NOTES → 3 GATES → 4 BUILD → 5 CONFIRM ROLLBACK
  → 6 CONFIG FIRST → 7 PROGRESSIVE ROLLOUT → 8 OBSERVE → 9 PUBLISH → 10 SETTLE
```

## The idea that makes releases boring

**Deployment is not release.** Ship the code dark, then release the behaviour deliberately behind
a flag. This separates "is the build healthy" from "is the feature working", which means a bad
build is caught by telemetry and a bad feature is caught by a flag flip — neither requires an
emergency redeploy.

Stage 5 follows from the same idea in reverse: know how to go back **before** there is a reason to.

## Why rollback is confirmed before rollout

A rollback path that has never been exercised is a hypothesis about your own infrastructure.
Stage 5 requires it rehearsed and timed, and requires the irreversible effects to be listed
separately — because for those, rollback is not the answer. Schema contraction, deleted rows,
sent messages and charged payments need a forward-fix plan, which is exactly why expansion
precedes contraction in [`skills/migration`](../../skills/migration/SKILL.md).

## Scaling

```text
ROUTINE PATCH          1, 2 (abbreviated), 3, 4, 5 (verify retained previous version), 6, 7 (rolling),
                       8, 10
MINOR RELEASE          all stages, progressive rollout with a short dwell
MAJOR RELEASE          all stages, plus a migration guide published ahead of the release, a release
                       candidate consumers can test, and an extended observation window
HOTFIX                 1, 3 (the gates applicable to the risk class, recorded as reduced), 4, 5,
                       7 (accelerated but still progressive), 8, 10 — never skip stage 5
LIBRARY PUBLISH        1, 2, 3, 4, 9 with a clean-environment install verification, 10
```

The hotfix path reduces gate *breadth*, never stage 5. Under pressure is precisely when an
unrehearsed rollback costs the most.

## Failure modes specific to this workflow

```text
SEMVER LIE             A "patch" that removes a field. One occurrence destroys all consumer trust.
GIT-LOG CHANGELOG      Commit messages published as release notes; nobody can tell what to do.
REBUILD PER ENVIRONMENT Staging tested a different artifact than production received.
UNREHEARSED ROLLBACK   Stage 5 skipped because "we've never needed it".
CONFIG WITH CODE       The app boots with missing configuration and fails later as a business bug.
UNWATCHED CANARY       A percentage rollout with no comparison — a slow rolling update.
NO DEPLOY MARKERS      A regression nobody can attribute to a release.
EFFECT BLINDNESS       Code rolled back; the duplicate payments were not.
UNVERIFIED PUBLISH     The registry upload failed or shipped the wrong artifact; users found it.
FLAG DEBT              Forty live flags with no removal dates and no owner.
WEEKEND HERO DEPLOYS    The process is a person who knows the steps, not a pipeline.
```

## References

- [`skills/release-engineering/SKILL.md`](../../skills/release-engineering/SKILL.md) — SemVer, changelog, deprecation and support windows
- [`skills/deployment/SKILL.md`](../../skills/deployment/SKILL.md) — rollout strategies and health semantics
- [`skills/migration/SKILL.md`](../../skills/migration/SKILL.md) — expand-migrate-contract for data changes
- [`agents/qa-engineer/AGENT.md`](../../agents/qa-engineer/AGENT.md) · [`agents/performance-engineer/AGENT.md`](../../agents/performance-engineer/AGENT.md)
- [`skills/dependency-analysis/SKILL.md`](../../skills/dependency-analysis/SKILL.md) · [`skills/security-audit/SKILL.md`](../../skills/security-audit/SKILL.md)
- [`decision-records/`](../../decision-records/) — record the rollout strategy choice for unusual releases
