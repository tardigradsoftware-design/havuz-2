---
name: analyze-existing-project
version: 1.0.0
description: >-
  Understand an unfamiliar codebase or third-party repository from evidence — architecture map,
  conventions, health, license risk, security posture and fitness — before changing or adopting it.
trigger: >-
  Onboarding to an unfamiliar codebase before modifying it; evaluating a library, framework or MCP
  server for adoption; deciding whether to fork, wrap, contribute to or abandon a dependency;
  recording a repository into this knowledge base.
not_for: >-
  A repository already assessed recently and unchanged since (reuse the cached assessment);
  a security question, which needs workflows/security-review; a performance question, which needs
  workflows/performance-review; judging a project on style preference alone.
status: active
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [analysis, onboarding, due-diligence, codebase, repository, workflow]
confidence: high
claim_type: recommendation
evidence_level: practitioner-experience
estimated_duration: 30-90 minutes for an adoption assessment; hours for a full codebase onboarding
stages:
  - id: 1
    name: Establish purpose and constraints
    goal: Fix why the analysis is happening, because the required depth and the report shape both follow from it.
    skill: repository-analysis
    inputs: [the request, integration intent, constraints — license, runtime, security posture, maintenance expectation]
    outputs: [purpose statement, integration mode, constraint list, required depth]
    exit_gate: The purpose is one of adopt, contribute, learn, onboard or record, and the integration mode is stated — dependency, vendored, MCP, fork or reference only.
    on_gate_failure: Ask the requester. An unscoped analysis produces a tour rather than an answer.
  - id: 2
    name: Verify identity and status
    goal: Confirm this is the canonical upstream at the ref that will actually be used, and whether it is alive.
    skill: repository-analysis
    inputs: [slug or URL, lockfile-pinned version or ref]
    outputs: [canonical slug after redirects, owner identity, archived/disabled flag, last push and release dates, star count with observation date, rename or supersession history]
    exit_gate: The canonical upstream is confirmed, the ref under analysis matches what production pins, and archived or maintenance status is stated explicitly.
    max_loops: 2
    on_gate_failure: Follow redirects and check release notes for renames. Analysing a fork and reporting the upstream's reputation is a common and damaging error.
  - id: 3
    name: Read the machine-readable truth
    goal: Take facts from manifests, lockfiles, CI configuration and schemas rather than from prose.
    inputs: [package manifests, lockfiles, CI workflows, Makefile or scripts, config files, schema definitions]
    outputs: [exact dependency set with resolved versions, real build/test/lint commands, enforced CI gates, required configuration and secrets, declared entry points]
    exit_gate: The build, test and run commands are taken from manifests or CI rather than from the README, and every required environment variable and secret is enumerated.
    on_gate_failure: Run the commands. Documentation that cannot be executed is a hypothesis about the project, not a fact about it.
  - id: 4
    name: Map the architecture
    goal: Produce a one-page map of entry point to core flow to outputs, with layering and extension points.
    skill: repository-analysis
    inputs: [source tree, entry points, manifests, tests]
    outputs: [one-page architecture map, layer dependency direction, public versus internal API surface, extension points, external dependencies and data model]
    exit_gate: A reader can trace one request or one command from entry to output using the map alone, and the public API boundary is identified.
    max_loops: 3
    on_gate_failure: Follow one real execution path end to end with the debugger or with logging. A directory listing is not an architecture map.
  - id: 5
    name: Assess health and maintenance
    goal: Determine whether this project will still be maintained when the dependency matters most.
    skill: repository-analysis
    inputs: [commit and release history, contributor list, issue tracker, CI status, SECURITY.md]
    outputs: [health classification — STRONG, WEAK or DEAD/UNSAFE — with the observable evidence and dates for each signal]
    exit_gate: Every health signal cited is observable and dated, and the classification follows the rules in skills/repository-analysis rather than the star count.
    max_loops: 2
    on_gate_failure: Record the health as UNKNOWN with the missing evidence named. An undated health snapshot is noise.
  - id: 6
    name: Read the license
    goal: Establish what may legally be done with this code — the file, not the badge.
    inputs: [LICENSE file, NOTICE, dependency licenses, header comments]
    outputs: [exact license, SPDX identifier, license_risk classification, vendoring and redistribution decision, attribution obligations, copyleft reach]
    exit_gate: The license file has been read; a null license is recorded as no-license-do-not-redistribute with vendoring prohibited; NOASSERTION or custom text is read for field-of-use and trademark restrictions; copyleft compatibility with the distribution model is stated.
    on_gate_failure: Prohibit vendoring and reference only. A high star count combined with no license file is the most common trap in this space.
  - id: 7
    name: Assess quality and security posture
    goal: Determine whether the project's own engineering practices make it safe to depend on.
    skill: security-audit
    inputs: [test suite, CI gates, release discipline, SECURITY.md, advisories, default configuration, install-time scripts]
    outputs: [test and CI assessment, release and SemVer discipline, issue triage quality, advisory history, default-configuration safety, install-time script review, supply-chain posture]
    exit_gate: What CI actually enforces is stated from the workflow files rather than from badges, known advisories at the resolved version are listed, and install-time behaviour is reviewed.
    max_loops: 2
    on_gate_failure: Treat unenforced quality claims as absent. A badge is a claim; a workflow file is evidence.
  - id: 8
    name: Run it
    goal: Execute the quickstart in a clean environment and measure the real onboarding friction.
    inputs: [quickstart instructions, clean environment, the pinned version]
    outputs: [time to first successful run, every friction point encountered, divergence between documentation and reality, examples that do not run]
    exit_gate: The quickstart has been executed on a clean environment at the version that would be adopted, and every divergence between documentation and observed behaviour is recorded.
    max_loops: 2
    on_gate_failure: Record the failure as a finding. A quickstart that does not run is a maintenance signal with direct cost.
  - id: 9
    name: Score fit and removal cost
    goal: Evaluate against this project's constraints rather than in the abstract, including the field everyone skips.
    skill: competitive-analysis
    inputs: [constraints, all findings, candidate alternatives]
    outputs: [weighted fit table, removal cost assessment, coupling measurement, top three risks each with a detection method, exit plan]
    exit_gate: The fit table is weighted against the stated constraints, removal cost is quantified by call sites and files touched, and each of the top three risks has an observable detection method.
    on_gate_failure: Measure coupling by counting import sites. A dependency whose removal cost is unknown is a liability whatever its quality today.
  - id: 10
    name: Report and record
    goal: Produce a verdict with conditions and file it where the next assessment can find it.
    skill: research-synthesis
    agent: skill-curator
    inputs: [all findings]
    outputs: [assessment report with verdict ADOPT/WRAP/EXTEND/AVOID/MONITOR, evidence table with URL or path and date per claim, repository card, index entry]
    exit_gate: A verdict is stated with the conditions attached, every factual claim carries a URL or file path and a date, uncited statements are marked GENERATED, and the assessment is filed with a re-verification date.
    on_gate_failure: Remove or label the uncited claims. An assessment that cannot be traced cannot be trusted or reused.
quality_gates:
  - Purpose and integration mode fixed before analysis begins.
  - Canonical upstream confirmed; the analysed ref matches what production pins.
  - Archived, disabled or maintenance status stated explicitly, never omitted.
  - Build, test and run commands taken from manifests or CI, not from prose.
  - A one-page architecture map traces one real path from entry to output.
  - Every health signal is observable and dated; stars alone are never a quality signal.
  - The license FILE was read; a null license yields no-license-do-not-redistribute and no vendoring.
  - CI enforcement read from workflow files, not from badges.
  - Advisories checked at the resolved version; install-time scripts reviewed.
  - The quickstart was actually executed in a clean environment at the target version.
  - Removal cost quantified; exit plan written.
  - Verdict stated with conditions; every claim cited or marked GENERATED; re-verification date set.
artifacts:
  - purpose and constraint statement
  - identity and status record
  - machine-readable facts — commands, dependencies, configuration
  - one-page architecture map
  - health classification with dated evidence
  - license assessment with license_risk
  - quality and security posture report
  - quickstart execution record with friction log
  - weighted fit table with removal cost and exit plan
  - assessment report with verdict, conditions and evidence table
  - repository card and index entry
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
sources:
  - title: "OpenSSF Scorecard"
    url: https://github.com/ossf/scorecard
    type: github-repository
    organization: Open Source Security Foundation
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
  - title: "GitHub REST API — repositories"
    url: https://docs.github.com/en/rest/repos/repos
    type: official-docs
    organization: GitHub
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
related: [skills/repository-analysis/SKILL.md, skills/competitive-analysis/SKILL.md, workflows/architecture-review/WORKFLOW.md, repositories/]
---

# Workflow: Analyze Existing Project

```text
1 PURPOSE → 2 IDENTITY → 3 MACHINE-READABLE TRUTH → 4 ARCHITECTURE MAP → 5 HEALTH
  → 6 LICENSE → 7 QUALITY+SECURITY → 8 RUN IT → 9 FIT+REMOVAL COST → 10 REPORT
```

## The principle

**The README describes intent; the artefacts describe reality.** This workflow reads manifests,
lockfiles, CI workflows, commit history, the issue tracker and the license file — and then runs
the quickstart — because those are the sources that cannot be aspirational.

Two stages exist purely to catch the errors that make assessments worthless:

```text
STAGE 2 — IDENTITY.  Analysing a fork, a mirror or a renamed repository and reporting the
                     upstream's reputation is a silent, total failure of the assessment.
STAGE 8 — RUN IT.    A quickstart that does not run at the version you would adopt is a
                     maintenance signal with a direct, measurable cost.
```

## Scaling

```text
QUICK ADOPTION CHECK     stages 1, 2, 5, 6, 7 (advisories only), 9 — under 30 minutes
FULL ADOPTION ASSESSMENT all stages
CODEBASE ONBOARDING      stages 1, 3, 4, 7, 8 plus a conventions extract into the project's
                         own AGENTS.md
KB RECORDING             all stages, with stage 10 producing the repository card and index entry
RE-ASSESSMENT            stages 2, 5, 6, 7 and a diff against the previous assessment
```

## Failure modes specific to this workflow

```text
README TRUST          Believing the feature list without running anything.
FORK CONFUSION        Reporting an upstream's reputation for a fork's code.
STALE REF             Assessing main while production pins a two-year-old tag.
STAR RANKING          Letting popularity decide fitness; archived projects with many stars
                      are the trap.
LICENSE BY BADGE      Reading the README badge instead of the LICENSE file, and missing a
                      null license entirely.
DIRECTORY AS MAP      Describing the tree instead of tracing a path.
HEALTH THEATRE        Counting commits without checking whether CI passes or issues are answered.
NO EXIT PLAN          Adopting without knowing what removal would cost.
UNCITED CONFIDENCE    A fluent report with no URLs, paths or dates behind it.
```

## References

- [`skills/repository-analysis/SKILL.md`](../../skills/repository-analysis/SKILL.md) — health signals, license analysis and the report template
- [`skills/competitive-analysis/SKILL.md`](../../skills/competitive-analysis/SKILL.md) · [`skills/dependency-analysis/SKILL.md`](../../skills/dependency-analysis/SKILL.md)
- [`skills/dont-reinvent-the-wheel/SKILL.md`](../../skills/dont-reinvent-the-wheel/SKILL.md)
- [`metadata/repositories.json`](../../metadata/repositories.json) — 414 pre-scored repositories
- [`repositories/`](../../repositories/) — generated cards in 12 categories
- [`scripts/lib/scoring.py`](../../scripts/lib/scoring.py) · [`scripts/update/fetch_github_metadata.py`](../../scripts/update/fetch_github_metadata.py)
