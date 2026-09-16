---
id: ai-engineering-repository-status
title: "Repository status: the classifications that override a score"
domain: ai-engineering
summary: >-
  The status vocabulary applied to repository records — active, maintenance, archived, experimental,
  deprecated, unverified, snapshot — how each is detected from observable GitHub facts, and the
  action an agent must take for each.
status: active
confidence: very-high
claim_type: recommendation
evidence_level: verified-github-api
tags: [status, lifecycle, archived, maintenance, curation, github-api]
applies_to: [repositories, sources, skills, knowledge]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
sections:
  - heading: Why status overrides score
    anchor: "#why-status-overrides-score"
    purpose: overview
  - heading: The vocabulary
    anchor: "#the-vocabulary"
    purpose: decision
  - heading: Detection
    anchor: "#detection"
    purpose: implementation
  - heading: Actions by status
    anchor: "#actions-by-status"
    purpose: decision
estimated_tokens: 1127
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related_skills: [repository-analysis, dependency-analysis, evidence-validation]
related:
  - knowledge/ai-engineering/source-scoring.md
  - knowledge/ai-engineering/freshness-policy.md
  - metadata/repositories.json
sources:
  - title: "GitHub REST API — Get a repository"
    url: https://docs.github.com/en/rest/repos/repos#get-a-repository
    type: official-docs
    organization: GitHub
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "archived, disabled, pushed_at and license.spdx_id are the fields status is derived from."
---

# Repository Status

## Why status overrides score

A numeric score is a weighted average, and averages hide the one fact that should dominate. A
repository with 9.2-scoring authority, adoption and documentation that is `archived: true` is not
a strong adoption candidate — it is a frozen artifact with good history.

Status is therefore a **layer above** the score, not a component of it. The score is retained for
history and comparability; the status decides the action.

## The vocabulary

| Status | Meaning | Detection |
|---|---|---|
| `active` | Under normal development; recent pushes and releases | `pushed_at` < 90 days, releases present, not archived |
| `maintenance` | Bug fixes only; no feature work expected | `pushed_at` < 180 days but releases sparse, or self-declared |
| `archived` | Read-only by the owner. Development has stopped | `archived: true`, or `disabled: true` |
| `experimental` | Self-declared unstable; API may change without notice | README/name/topics declare it, or no 1.0 release after long history |
| `deprecated` | Superseded; a successor exists | owner statement, or a redirect to a renamed successor with a note |
| `snapshot` | A frozen public copy of something that became closed | name contains `-snapshot`/`-archive`, or `archived` with a rename |
| `unverified` | Could not be resolved or reached | 404, unreachable, or no reachable primary source |
| `rejected` | Excluded by policy, not by quality | leaked or improperly obtained material — see excluded-sources.md |

`rejected` and `unverified` never enter the active retrieval index. `snapshot` and `archived` do,
but with the action constraint below attached to the card.

## Detection

Status is computed, not asserted, wherever the API supports it:

```text
archived: true          → archived       (hard fact; caps maintenance component at 0)
disabled: true          → archived       (inaccessible; flagged)
pushed_at age           → active / maintenance thresholds per the table
rename to *-snapshot    → snapshot       (combined with archived)
license: null           → not a status, but sets license_risk and blocks redistribution
404 / unreachable       → unverified     (moved out of the active index)
self-declaration        → experimental   (README, name, topics; recorded with the quote)
curation.json           → any of the above, with curated_at and a curation_note explaining why
```

Automated detection covers most records. `scripts/update/curation.json` covers the cases where the
API is silent — roughly 31 of 414 — and every curated status carries a date and a note.

## Actions by status

```text
active         adopt, depend on, cite, recommend. Verify the specific claim you depend on.
maintenance    depend with a migration plan. Check the last release before pinning.
archived       cite as prior art, study the design, use as a finished tool where it is complete
               and offline. NEVER adopt as a security dependency or as a live dependency in new
               work. An unmaintained security tool supplies confidence without coverage.
experimental   do not use in production. Fine for a prototype or a benchmark, with the instability
               stated in whatever you produce.
deprecated     do not adopt. Link the successor. If already depended on, schedule migration.
snapshot       read-only reference. Do not file issues, do not expect fixes, do not depend.
unverified     do not cite. If the claim matters, find another source or mark it UNVERIFIED.
rejected       do not reference except as an example of the excluded category.
```

The `archived` rule is the one agents most often get wrong, because archived projects are usually
archived *after* becoming popular. Popularity is a record of the past; the archive flag is a
statement about the future.

## References

- [`knowledge/ai-engineering/source-scoring.md`](source-scoring.md) — hard overrides and tiers
- [`knowledge/ai-engineering/freshness-policy.md`](freshness-policy.md) — the windows behind the thresholds
- [`knowledge/ai-engineering/verification-findings.md`](verification-findings.md) — archived projects found on 2026-09-15
- [`metadata/repositories.json`](../../metadata/repositories.json) · [`scripts/update/curation.json`](../../scripts/update/curation.json)
