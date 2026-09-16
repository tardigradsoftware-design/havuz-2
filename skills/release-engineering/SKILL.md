---
name: release-engineering
version: 1.0.0
description: >-
  Manage versions, changelogs, release trains, deprecations and support windows so consumers can
  upgrade predictably — including SemVer discipline and the breaking-change contract.
category: devops
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [release, versioning, semver, changelog, deprecation, support-window, dx]
applies_to: [any]
priority: 77
requires: [deployment, documentation]
conflicts_with: []
estimated_tokens: 3027
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Versioning contract
    anchor: "#versioning-contract"
    purpose: decision
  - heading: Workflow
    anchor: "#workflow"
    purpose: implementation
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
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
  - title: "Conventional Commits"
    url: https://www.conventionalcommits.org/en/v1.0.0/
    type: specification
    confidence: high
    claim_type: recommendation
    verified_at: 2026-09-15
related_skills: [deployment, documentation, migration, dependency-analysis, project-planning]
related_repositories: [semantic-release/semantic-release, conventional-changelog/standard-version, release-drafter/release-drafter]
tests: 20
---

# Release Engineering

## Purpose

Make upgrading **predictable for the consumer**. A version number is a promise about what
changed and what will not break; a changelog is the evidence; a deprecation policy is how you
keep the promise while still moving.

Consumers do not need your release to be exciting. They need to know whether it is safe to
install today.

## When to Use

```text
□ Publishing anything versioned: a library, an API, a CLI, an application, a spec
□ Preparing a major release with breaking changes
□ Deprecating a feature, an endpoint, a field or a platform
□ Deciding a support window or an end-of-life date
□ When consumers are surprised by a release (which means the contract failed)
```

## When NOT to Use

```text
✗ An internal, single-consumer service with no version contract — coordinate directly instead
✗ Continuous deployment of a SaaS frontend where there is no consumer-installable artifact
  (but the API and data contracts still need versioning)
```

## Versioning contract

**SemVer 2.0.0** (`MAJOR.MINOR.PATCH`) — <https://semver.org/>:

```text
MAJOR    incompatible change to the PUBLIC surface
MINOR    new functionality, backwards compatible
PATCH    backwards-compatible bug fixes
PRE-RELEASE   1.2.0-alpha.1 < 1.2.0-beta.2 < 1.2.0-rc.1 < 1.2.0
BUILD METADATA 1.2.0+20130313144700 — ignored for precedence; never relied upon

0.y.z    initial development: anything may change at any time; no stability promise.
         Do not use 0.x to avoid committing to a contract you are already publishing.
```

### What counts as breaking (the part everyone gets wrong)

```text
BREAKING
  removing or renaming a public endpoint, field, function, parameter, type, event, config key
  changing a type, a unit, a default that alters behaviour, or a required-ness (optional → required)
  narrowing accepted input; widening returned output where consumers switch exhaustively
  adding an enum value when consumers are expected to handle all values
  changing semantics of an existing field or status code
  changing error shapes, authentication, or rate limits in a way that breaks clients
  dropping support for a runtime, platform or dependency version
  making a previously-synchronous operation asynchronous, or vice versa

NOT BREAKING
  adding an optional field, endpoint, parameter with a default, or event
  widening accepted input; improving performance; fixing a documented-behaviour bug
  internal refactoring with no observable change
  deprecating (warning) without removing
  adding a new enum value IF and ONLY IF unknown-value tolerance is documented and tested
```

Rules:

```text
1. Define the PUBLIC surface explicitly, in writing. Everything else is internal and may change
   in a patch. An undocumented surface will be depended upon anyway — so document it.
2. Bug fixes that change observable behaviour someone depended on are breaking. The fix is still
   correct; the version bump acknowledges reality.
3. One source of truth for the version. Derive it from commits (Conventional Commits) or set it
   deliberately — but never have two places disagreeing.
4. Pre-releases are for consumers to test, not for you to skip testing.
```

## Changelog

Written for the person upgrading, in **Keep a Changelog** form
(<https://keepachangelog.com/en/1.1.0/>):

```markdown
## [2.3.0] - 2026-09-15
### Added        new capabilities, with the use case, not just the name
### Changed      changes in existing behaviour — state the old and the new
### Deprecated   present but scheduled for removal, with the removal version and date
### Removed      deleted features, with the replacement and the migration path
### Fixed        bug fixes, with the symptom users would have recognised
### Security     vulnerabilities fixed, with an advisory link and the affected version range
```

Rules:

```text
□ Every entry answers "do I need to do anything?" — if yes, say exactly what
□ Breaking changes get a MIGRATION section with before/after code, not a description
□ Group by change class, never by author, ticket or commit message
□ Never "various fixes", "improvements", "updates" — that is a git log, not a changelog
□ Link the issue, PR, advisory and docs for every entry
□ Unreleased section accumulates during development; cut at release
□ Generate the skeleton from commits; write the human parts by hand. Fully automated
  changelogs are usually unreadable, and fully manual ones are usually incomplete.
```

## Deprecation and support

```text
ANNOUNCE      in the changelog, in the docs, and at the point of use:
              a runtime warning (once per process, not per call), a linter rule or codemod,
              and the `Deprecation` / `Sunset` response headers for HTTP APIs
WINDOW        a stated period before removal. Rough practice: minor features one minor cycle;
              widely-used public APIs at least one major cycle or a fixed number of months;
              security-relevant interfaces longer, with a migration path
ESCALATE      warning → louder warning (or error behind a flag) → removal in the next MAJOR
REMOVE        only in a major release; removal is listed in the changelog with the replacement
CODMOD        provide an automated migration wherever the change is mechanical
SUPPORT WINDOW publish which versions are supported, for how long, and with what:
              security fixes only vs full maintenance vs unsupported. Include the dates.
EOL           announce end-of-life in advance with the final supported date; keep the artifacts
              downloadable after EOL; state clearly that no fixes will follow
SECURITY BACKPORTS  fix supported versions; document which versions received the patch,
              so consumers can tell whether they are exposed
```

## Workflow

```text
COLLECT → CLASSIFY → BUMP → DOCUMENT → BUILD → ANNOUNCE → PUBLISH → SUPPORT → REVIEW
```

```text
1 COLLECT     Changes since the last release, from commits/PRs, with their user-visible effect.
2 CLASSIFY    Each change as breaking / feature / fix / deprecation / security, against the
              public-surface definition. Disagreement here is resolved before release, not after.
3 BUMP        Derive the version. If any change is breaking, it is a MAJOR — no exceptions,
              and no "we'll call it minor because nobody will notice".
4 DOCUMENT    Changelog entries with migration notes for every breaking change and every removal.
              Update versioned docs; state which docs apply to which version.
5 BUILD       Reproducible artifact, pinned dependencies, signed where possible, with SBOM.
              Build once; promote the same artifact (see deployment).
6 ANNOUNCE    Before a major release: a migration guide published ahead of the release, ideally
              with a release candidate consumers can test. Surprises are the failure mode.
7 PUBLISH     Tag immutably; publish to the registry; verify the published artifact installs and
              works from a clean environment (never assume the publish step succeeded).
8 SUPPORT     Monitor adoption and issue reports for the release; be reachable for the first days;
              track the support window and the deprecation timers.
9 REVIEW      Per release: what broke for consumers, what the changelog failed to convey, how long
              the process took, what was manual that could be automated.
```

## Failure Modes

```text
SEMVER LIE            A "patch" release removes a field. One occurrence destroys all trust.
UNDEFINED SURFACE     Everything is public because nothing was declared internal.
GIT-LOG CHANGELOG     Commit messages published as a changelog; no migration guidance.
SILENT BREAKING CHANGE A behaviour change with no changelog entry because "it was a bug fix".
ENUM TRAP             A new enum value in a minor release breaking exhaustive switches.
NO DEPRECATION PATH   Features removed with no warning, no window and no codemod.
DEPRECATION SPAM      A warning per call, per request, filling logs and teaching people to ignore it.
UNSUPPORTED BY ACCIDENT Nobody knows which versions get security fixes.
UNVERIFIED PUBLISH     The registry upload failed or published the wrong artifact; discovered by users.
MAJOR WITHOUT A GUIDE  Breaking changes announced only in the release itself.
VERSION IN TWO PLACES package.json and a constant disagree.
PRE-RELEASE AS PRODUCTION  `-beta` shipped to everyone because the stable release was late.
```

## Quality Checklist

```text
□ Public surface defined in writing; everything else explicitly internal
□ Every change classified against the breaking-change list before the version is chosen
□ SemVer applied honestly; breaking changes are MAJOR without exception
□ Changelog grouped by change class, answering "do I need to act?"
□ Migration notes with before/after code for every breaking change and removal
□ Deprecations announced in changelog, docs, runtime (once per process) and HTTP headers
□ Deprecation window stated with the removal version and date; codemod provided where mechanical
□ Support window and EOL dates published, including which versions get security fixes
□ Reproducible, pinned, signed artifact with SBOM; built once and promoted
□ Published artifact verified by installing from a clean environment
□ Tag immutable; version has one source of truth
□ Major releases preceded by a published migration guide and a release candidate
□ Security fixes documented with the affected and patched version ranges
□ Post-release review: consumer breakage, changelog clarity, process time, automation gaps
```

## Anti-Patterns

```text
✗ Bumping MINOR for a change you know will break someone
✗ A changelog entry reading "misc improvements and bug fixes"
✗ Removing a deprecated field without ever having warned about it
✗ Publishing the docs for `main` as though they applied to the released version
✗ A deprecation warning printed on every request
✗ "We don't support old versions" with no published window
✗ Skipping the clean-install verification because the CI build passed
✗ Two files declaring different versions of the same package
```

## References

- SemVer 2.0.0 — <https://semver.org/> · Keep a Changelog — <https://keepachangelog.com/en/1.1.0/>
- Conventional Commits — <https://www.conventionalcommits.org/en/v1.0.0/>
- [`deployment`](../deployment/SKILL.md) · [`documentation`](../documentation/SKILL.md) · [`migration`](../migration/SKILL.md)
- [`dependency-analysis`](../dependency-analysis/SKILL.md) — consuming the same contract as a consumer
- [`api-design`](../api-design/SKILL.md) — versioning and compatibility at the contract level
- [`workflows/release-checklist/`](../../workflows/release-checklist/)

## Related Skills

`deployment` · `documentation` · `migration` · `api-design` · `dependency-analysis` ·
`project-planning`

## Evaluation Criteria

```text
1. Contract accuracy: 0 releases whose version understates the change class.
2. Consumer surprise rate: breaking changes reported by consumers that were not documented (target 0).
3. Migration success: fraction of consumers upgrading within one minor cycle of a major release.
4. Changelog usefulness: a consumer can decide whether to act from the entry alone.
5. Deprecation hygiene: 0 removals without a completed announce → window → escalate cycle.
6. Release cadence and lead time: regular, predictable, and fast from merge to publish.
7. Publish reliability: 0 releases requiring re-publish due to a bad artifact.
```

Test cases in [`tests/`](tests/).
