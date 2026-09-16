---
name: repository-analysis
version: 1.0.0
description: >-
  Assess an unfamiliar codebase or third-party repository: architecture, conventions, health,
  maintenance status, license risk, security posture and fitness for adoption — from evidence, not
  from the README's claims.
category: research
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [codebase, onboarding, evaluation, maintenance, license, due-diligence, architecture]
applies_to: [any]
priority: 87
requires: [evidence-validation, web-research]
conflicts_with: []
estimated_tokens: 2910
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Workflow
    anchor: "#workflow"
    purpose: implementation
  - heading: Health signals
    anchor: "#health-signals"
    purpose: decision
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "OpenSSF Scorecard"
    url: https://github.com/ossf/scorecard
    type: github-repository
    organization: Open Source Security Foundation
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Automated, observable health/security checks for open-source projects."
  - title: "GitHub REST API — repositories"
    url: https://docs.github.com/en/rest/repos/repos
    type: official-docs
    organization: GitHub
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
related_skills: [evidence-validation, dependency-analysis, dont-reinvent-the-wheel, code-review, security-audit]
related_repositories: [ossf/scorecard, oraios/serena, upstash/context7]
tests: 6
---

# Repository Analysis

## Purpose

Answer two questions with evidence: **how does this codebase actually work**, and **is it
safe and sensible to depend on it**.

The README describes intent. This skill reads the artefacts that describe reality: the
lockfile, the CI config, the commit history, the test suite, the issue tracker, the license
file, and the code itself.

## When to Use

```text
□ Onboarding to an unfamiliar codebase before changing it
□ Evaluating a library/framework/MCP server for adoption
□ Deciding whether to fork, wrap, contribute to, or abandon a dependency
□ Assessing whether a project is still maintained
□ Due diligence before recommending a project to someone else
□ Recording a repository into this knowledge base (feeds repositories/*/*.md)
```

## When NOT to Use

```text
✗ A repository you already know well and that has not changed — reuse the cached assessment
✗ Judging a project solely to satisfy a style preference
✗ As a substitute for security-audit when security is the actual question
```

## Inputs

```text
repository       slug or URL; the exact commit/tag/ref under analysis
purpose          why you are analysing it (adopt? contribute? learn? onboard?)
integration      how you would consume it (dependency, vendored, MCP, fork, reference)
constraints      license, language/runtime, security posture, maintenance expectations
```

## Workflow

```text
IDENTIFY → MAP → HEALTH → LICENSE → QUALITY → SECURITY → FIT → REPORT
```

### 1. IDENTIFY — is this the real thing?
```text
□ Canonical upstream, or a fork/mirror/renamed repo? Follow redirects; record the final slug.
□ Owner identity: verified org, foundation, vendor, or an individual?
□ Archived, disabled, or in maintenance mode? (`archived`, `disabled`, `pushed_at`)
□ Renamed or superseded? Check the README's first lines and the release notes.
□ Star/fork counts and the date they were observed — stars without a date are noise.
```
Prefer [`metadata/repositories.json`](../../metadata/repositories.json): it already holds
`status`, `tier`, `license_risk`, `trust_score`, `stars` and `stars_checked_at` for 414
projects, refreshed from the GitHub API.

### 2. MAP — how is it organised?
```text
□ Entry points: package manifests, main/bin, exported public API surface
□ Layering: which directories depend on which; is there an obvious core vs periphery?
□ Build & run: the exact commands (from Makefile/package.json/CI — not from the README prose)
□ Configuration: env vars, config files, defaults, required secrets
□ Extension points: plugin systems, hooks, documented interfaces
□ Boundaries: what is public API vs internal; does the project enforce that?
□ Data model and external dependencies (services, databases, networks)
```
Produce a one-page map: entry point → core flow → outputs. If you cannot draw it, you do
not yet understand it.

### 3. HEALTH — see [Health signals](#health-signals).

### 4. LICENSE
```text
□ Which license, exactly? Read the file; do not trust the badge.
□ GitHub reports `license: null` → NO LICENSE → reference only, never vendor or redistribute.
   Record license_risk: no-license-do-not-redistribute.
□ `NOASSERTION` or a custom file → read it; check for trademark, field-of-use and
  commercial-use restrictions.
□ Copyleft (GPL/AGPL) → check compatibility with your distribution model; AGPL covers
  network use.
□ Dependency licenses: are any incompatible with yours? (This recurses.)
□ NOTICE/attribution obligations: what must ship with your product?
□ Patents: is there an explicit grant (Apache-2.0) or none (MIT is silent)?
□ Trademark: some projects restrict use of the name in forks.
```

### 5. QUALITY
```text
□ Tests: do they exist, what do they cover, do they run in CI, are they fast enough to matter?
□ CI: what is actually enforced (lint, type-check, test, build, security scan)?
□ Release discipline: SemVer? Changelog maintained? Breaking changes documented?
□ Issue triage: are issues answered, labelled, closed with reasons?
□ Contribution path: CONTRIBUTING.md, review turnaround, first-time-contributor merges
□ Code style consistency; presence of linters/formatters config
□ Documentation-to-code ratio for the parts you will use
□ Try it: install and run the quickstart on a clean machine. Time it. Note every friction point.
```

### 6. SECURITY
```text
□ SECURITY.md and a disclosure path
□ Known advisories (dependabot/GHSA/OpenSSF Scorecard results)
□ Secret leakage in history
□ Default configuration safety (does it work securely out of the box, or must you harden it?)
□ Supply-chain posture: signed releases, pinned builds, install-time scripts
□ If it is an MCP server or agent tool: what capabilities does it request? (see mcp-integration)
```

### 7. FIT
Score against *your* constraints, not in the abstract:

```text
| criterion            | weight | score | evidence |
| solves the problem   |        |       |          |
| maintenance outlook  |        |       |          |
| license compatibility|        |       |          |
| integration cost     |        |       |          |
| removal cost         |        |       |          |
| performance footprint|        |       |          |
| team familiarity     |        |       |          |
```

**Removal cost is the field everyone skips.** A dependency you cannot remove is a
liability regardless of its quality today.

### 8. REPORT
Produce a structured assessment:

```markdown
## <owner/repo>@<ref> — assessed <date>
Purpose: <adopt | learn | contribute>
Verdict: ADOPT | WRAP | EXTEND | AVOID | MONITOR
Identity:   canonical? owner? archived?
Health:     stars <n> (checked <date>) · last push <date> · releases <n>/yr ·
            contributors <n> · open/closed issue ratio · CI status
License:    <SPDX> · risk: <none | attribution | copyleft | no-license-do-not-redistribute>
Quality:    tests · CI gates · release discipline · docs
Security:   SECURITY.md · advisories · default hardening · scorecard
Architecture: the one-page map
Fit:        the weighted table
Risks:      top 3, each with a detection method
Conditions: what must be true to adopt (version pin, wrapper, monitoring, exit plan)
Exit plan:  how we would remove it, and what it would cost
Evidence:   every claim with a URL or file path and a date
```

Every claim gets a citation. If a claim cannot be cited, mark it `GENERATED`.

## Health signals

Observable, and each one falsifiable:

```text
STRONG
  releases within the last 6 months · commits from ≥3 distinct contributors in 90 days ·
  CI green on the default branch · issues answered within days · SECURITY.md present ·
  changelog maintained · dependency updates merged · tags follow SemVer ·
  documentation versioned per release

WEAK
  no release in 12 months · single maintainer, no bus factor plan · CI absent or
  permanently red · issue count rising with no responses · README promises features
  absent from the code · examples do not run

DEAD / UNSAFE
  archived or disabled · `pushed_at` > 24 months · license absent · known unpatched
  advisory with no fix · repo renamed to a "-snapshot" or "-archive" suffix ·
  install-time scripts fetching remote code
```

Interpretation rules:

```text
1. Stars measure attention, not quality. Never rank by stars alone.
2. Recency of PUSH matters more than recency of RELEASE for maintenance, and release
   cadence matters more than commit count for stability.
3. A single-maintainer project with excellent tests can beat a foundation project with none.
4. Archived is not "bad" — it is "frozen". Frozen is fine for a finished tool and fatal
   for a security dependency.
5. High star count + `license: null` is the most common trap in this space. Both facts
   must appear in the report.
```

## Failure Modes

```text
README TRUST           Believing the feature list without running the quickstart.
STAR RANKING           Equating popularity with fitness.
FORK CONFUSION         Analysing a fork and reporting the upstream's reputation.
STALE SNAPSHOT         Assessing `main` while your lockfile pins a two-year-old tag.
LICENSE ASSUMPTION     Reading the badge instead of the file; missing `license: null`.
HEALTH THEATRE         Counting commits without checking whether CI passes or issues get answers.
NO EXIT PLAN           Adopting without knowing the removal cost.
SURFACE MAP            Describing the directory tree instead of the control flow.
```

## Quality Checklist

```text
□ Canonical identity confirmed; final slug and ref recorded
□ Archived/maintenance status checked explicitly
□ One-page architecture map drawn (entry → core flow → outputs)
□ Build/run commands taken from manifests or CI, not from prose
□ License file read; license_risk recorded; vendoring decision made
□ Test and CI enforcement inspected (what gates actually run)
□ Release cadence, contributor count and issue responsiveness measured with dates
□ Security posture checked: SECURITY.md, advisories, defaults, scorecard
□ Quickstart executed on a clean environment; friction noted
□ Weighted fit table completed, including removal cost
□ Top 3 risks each have a detection method
□ Exit plan written
□ Verdict is one of ADOPT | WRAP | EXTEND | AVOID | MONITOR with stated conditions
□ Every claim cited or marked GENERATED
```

## Anti-Patterns

```text
✗ "40k stars, must be good"
✗ Recommending an archived project without saying it is archived
✗ Vendoring a repository that has no license file
✗ Reading the directory listing and calling it an architecture review
✗ Assessing `main` when production pins `v1.4.2`
✗ Ignoring install-time scripts in a dependency
✗ Reporting a health snapshot without the observation date
```

## References

- [`metadata/repositories.json`](../../metadata/repositories.json) — 414 scored repositories
- [`repositories/`](../../repositories/) — per-repository cards in 12 categories
- [`scripts/lib/scoring.py`](../../scripts/lib/scoring.py) — the executable scoring model
- [`scripts/update/fetch_github_metadata.py`](../../scripts/update/fetch_github_metadata.py)
- [`dependency-analysis`](../dependency-analysis/SKILL.md) · [`dont-reinvent-the-wheel`](../dont-reinvent-the-wheel/SKILL.md)
- [`security-audit`](../security-audit/SKILL.md) · [`code-review`](../code-review/SKILL.md)
- OpenSSF Scorecard — <https://github.com/ossf/scorecard> · GitHub REST API — <https://docs.github.com/en/rest/repos/repos>

## Related Skills

`evidence-validation` · `web-research` · `dependency-analysis` · `dont-reinvent-the-wheel` ·
`security-audit` · `research-before-code`

## Evaluation Criteria

```text
1. Identity accuracy: 100% of assessments point at the canonical upstream at the analysed ref.
2. Claim citation rate: 100% of factual claims carry a URL/path + date.
3. Verdict reproducibility: a second analyst given the same repo reaches the same verdict
   (target ≥ 0.8 agreement).
4. License correctness: no assessment mis-states a license; every `license: null` flagged.
5. Predictive value: ADOPT verdicts do not turn into emergency removals within 12 months.
```

Test cases in [`tests/`](tests/).
