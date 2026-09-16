---
name: dependency-analysis
version: 1.0.0
description: >-
  Analyse a dependency graph for risk, health, licensing, duplication and upgrade cost — and decide
  what to pin, replace, wrap or remove before it decides for you.
category: coding
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [dependencies, supply-chain, licensing, upgrades, security, maintenance]
applies_to: [any]
priority: 83
requires: [repository-analysis, evidence-validation]
conflicts_with: []
estimated_tokens: 2736
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Analysis dimensions
    anchor: "#analysis-dimensions"
    purpose: implementation
  - heading: Workflow
    anchor: "#workflow"
    purpose: implementation
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
  - title: "Trivy"
    url: https://github.com/aquasecurity/trivy
    type: github-repository
    organization: Aqua Security
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
related_skills: [repository-analysis, dont-reinvent-the-wheel, security-audit, migration, release-engineering]
related_repositories: [ossf/scorecard, aquasecurity/trivy, dependabot/dependabot-core, renovatebot/renovate, semgrep/semgrep]
tests: 5
---

# Dependency Analysis

## Purpose

Know exactly what your project depends on, what each dependency costs you, and what happens
when one of them changes, is compromised, or dies. Most projects have never enumerated their
transitive graph — and that graph is where the license conflict, the abandoned package and
the CVE actually live.

## When to Use

```text
□ Before adding any dependency (see dont-reinvent-the-wheel for the adopt/build decision)
□ Periodically on any maintained project (recommended: monthly scan, quarterly deep review)
□ Before a release that changes the dependency set
□ After any advisory, ownership change or license change upstream
□ When the build is slow, the bundle is large, or two packages do the same thing
□ During due diligence, acquisition review or compliance work
```

## When NOT to Use

```text
✗ A throwaway script with a couple of well-known dependencies
✗ As a reason to remove all dependencies — zero-dependency is not automatically safer,
  it just moves the code into your repo where nobody audits it
```

## Analysis dimensions

```text
1 INVENTORY        Full graph, direct and transitive, including build-time, dev-time and
                   install-time dependencies. Lockfile is the source of truth, not the manifest.
                   Record: name, resolved version, range declared, registry, integrity hash.

2 HEALTH           Per dependency: last release, release cadence, last commit, contributor
                   count, open/closed issue trend, CI status, archived flag.
                   Archived or >24 months without a push = a decision point, not a footnote.
                   Use metadata/repositories.json where the dependency is a GitHub project.

3 SECURITY         Known advisories (GHSA/OSV/NVD) at the resolved version — not the range.
                   Reachability: is the vulnerable code path actually reachable from your app?
                   (Unreachable is lower risk, but still recorded and scheduled.)
                   Install-time scripts: pre/post-install running arbitrary code is the
                   highest-risk event in the whole graph.
                   Typosquatting: verify the name character-by-character against the canonical
                   package, and the publisher identity against the project's own site.
                   Provenance: signed releases/build attestation where available.

4 LICENSE          Every dependency's license, including transitives. Classify:
                   permissive (MIT, BSD, Apache-2.0, ISC) · weak copyleft (MPL, LGPL, EPL) ·
                   strong copyleft (GPL, AGPL) · proprietary/custom · NONE.
                   NO LICENSE = do not vendor, do not redistribute; reference only, and record
                   license_risk: no-license-do-not-redistribute.
                   NOASSERTION or custom text = read it; check field-of-use, trademark and
                   commercial restrictions.
                   AGPL is a network-use trigger — it can reach a SaaS product.
                   Record attribution/NOTICE obligations that must ship with your product.

5 DUPLICATION      Multiple packages solving the same problem (two date libs, two HTTP clients,
                   three assertion libs). Each duplicate is a cost multiplier and a consistency bug.

6 WEIGHT           Install size, unpacked size, bundle contribution, runtime memory, cold-start
                   impact, native build requirements. Measured, not estimated.

7 COUPLING         How much of your code touches each dependency's API surface. A dependency
                   used in 200 files has a different removal cost than one used in 2.
                   This determines whether to WRAP it (see dont-reinvent-the-wheel).

8 REMOVAL COST     What it would take to delete this dependency tomorrow: files touched,
                   behaviour to reimplement, tests to rewrite, migration risk. The field
                   everyone skips, and the one that decides whether a dependency is a liability.

9 MAINTAINER RISK  Bus factor: single-maintainer packages carrying critical function.
                   Ownership changes: a sold or transferred package is a new supply-chain risk.
```

## Workflow

```text
INVENTORY → SCAN → CLASSIFY → RANK → DECIDE → AUTOMATE → MONITOR
```

```text
1 INVENTORY   Generate the full resolved graph from the lockfile. Diff it against the previous
              snapshot — the diff is the reviewable unit, not the whole list.
2 SCAN        Run automated scanners (Trivy, OSV-Scanner, `npm audit`/`pip audit`/`cargo audit`,
              Scorecard, license checkers) in CI. Treat output as leads, never as conclusions.
3 CLASSIFY    Every finding gets: reachable? exploitability? severity? license class? health class?
              Discard noise explicitly and record why — an untriaged scanner report trains
              everyone to ignore it.
4 RANK        By (severity × reachability × exposure) for security; by
              (criticality × abandonment risk) for maintenance; by license incompatibility for legal.
5 DECIDE      Per ranked item, one of:
                UPGRADE      to a fixed/healthy version (check the changelog for breaking changes)
                REPLACE      with a maintained alternative (record why the original failed)
                WRAP         isolate behind an internal interface to cut coupling and removal cost
                PIN          exact version + integrity hash; forbid mutable refs in production
                ACCEPT RISK  written acceptance: who, until when, what compensating control
                REMOVE       the best outcome where the dependency is not actually needed
6 AUTOMATE    Renovate/Dependabot with grouped, scheduled, tested updates; required CI green;
              auto-merge only for dev/tooling deps with a strong test suite; humans review
              anything in the runtime path or with a major-version bump.
7 MONITOR     A live watchlist: critical single-maintainer packages, packages with past ownership
              changes, packages with install scripts, packages with no license.
              Re-run the deep review quarterly; alert on new advisories within a day.
```

## Failure Modes

```text
MANIFEST-ONLY REVIEW   Analysing declared deps and missing the 400 transitive ones.
RANGE TRUST            "We declare ^1.2.0" — the resolved version is what ships. Read the lockfile.
SCANNER AS VERDICT     Merging whatever the scanner says, or ignoring it entirely.
UNREACHABLE COMPLACENCY Dismissing a critical CVE as unreachable without proving the code path.
INSTALL SCRIPT BLINDNESS Ignoring pre/post-install hooks — the classic supply-chain entry point.
TYPOSQUAT              A package one character from the real one.
LICENSE BY BADGE       Trusting a README badge instead of the license file; missing `null`.
AGPL SURPRISE          Discovering a network-copyleft transitive after launch.
DUPLICATE STACK        Three date libraries, two fetch clients, four test runners.
ABANDONED CRITICAL     A single-maintainer package holding up authentication, unnoticed.
FOREVER-PINNED         Pinning so tightly that security updates cannot land.
NO REMOVAL PLAN        Adopting without knowing the exit cost.
```

## Quality Checklist

```text
□ Full resolved graph enumerated from the lockfile, including build/dev/install-time deps
□ Diff against the previous snapshot reviewed on every change
□ Automated scanning in CI: advisories, license, install scripts, provenance
□ Every finding triaged: reachability, exploitability, severity — noise discarded with a reason
□ License class recorded per dependency, including transitives; NO LICENSE flagged as
  no-license-do-not-redistribute; AGPL/copyleft compatibility checked against distribution model
□ Attribution/NOTICE obligations listed
□ Duplicates identified and consolidated
□ Weight measured (install size, bundle contribution, cold start), not estimated
□ Coupling measured (files/call sites touching each API); removal cost stated for critical deps
□ Health assessed: release cadence, contributors, archived status, with observation dates
□ Single-maintainer critical packages on a named watchlist
□ Every runtime dependency pinned to an exact version with an integrity hash
□ Update automation configured with grouping, CI gating and a human-review rule for majors
□ Accepted risks recorded with owner, expiry and compensating control
□ Deep review scheduled quarterly; advisory alerts within one day
```

## Anti-Patterns

```text
✗ `npm audit` output pasted into a ticket with no triage
✗ Depending on a git branch or a mutable tag in production
✗ Adding a 3 MB dependency for one 10-line function
✗ Shipping a product with an AGPL transitive and no legal review
✗ Vendoring a package that has no license file
✗ Three date libraries in one bundle
✗ Ignoring a package's ownership change because "it's probably fine"
✗ Auto-merging major-version bumps of a runtime dependency
```

## References

- [`repository-analysis`](../repository-analysis/SKILL.md) · [`dont-reinvent-the-wheel`](../dont-reinvent-the-wheel/SKILL.md)
- [`security-audit`](../security-audit/SKILL.md) — supply-chain section
- [`migration`](../migration/SKILL.md) · [`release-engineering`](../release-engineering/SKILL.md)
- [`metadata/repositories.json`](../../metadata/repositories.json) · [`indexes/repositories.md`](../../indexes/repositories.md)
- [`scripts/update/check_staleness.py`](../../scripts/update/check_staleness.py)
- OpenSSF Scorecard — <https://github.com/ossf/scorecard> · Trivy — <https://github.com/aquasecurity/trivy>
- OSV — <https://osv.dev/>

## Related Skills

`repository-analysis` · `dont-reinvent-the-wheel` · `security-audit` · `migration` ·
`release-engineering` · `evidence-validation`

## Evaluation Criteria

```text
1. Inventory completeness: 100% of resolved dependencies enumerated, including transitives.
2. Triage quality: 100% of findings classified with reachability; 0 untriaged criticals.
3. Time-to-remediate: median days from advisory publication to a merged fix, by severity.
4. License accuracy: 0 mis-stated licenses; every `license: null` dependency flagged.
5. Drift: duplicate-package count and abandoned-critical count decrease over time.
6. Removal readiness: every critical dependency has a documented exit plan and measured cost.
```

Test cases in [`tests/`](tests/).
