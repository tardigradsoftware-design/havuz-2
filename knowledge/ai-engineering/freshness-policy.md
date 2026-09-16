---
id: freshness-policy
title: "Freshness policy: how long each kind of claim stays trustworthy"
domain: ai-engineering
summary: >-
  The review windows applied to every artifact in this knowledge base, why the window is a property
  of the claim rather than of the source, how staleness is detected and enforced in CI, and what
  happens to content that expires — re-verify, refresh, archive or quarantine, never leave in place.
status: active
confidence: very-high
claim_type: recommendation
evidence_level: cross-checked
tags: [freshness, staleness, maintenance, verification, ttl, curation, policy]
applies_to: [knowledge, skills, sources, repositories, evaluations, patterns]
audience: [both]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-09-15
sections:
  - heading: The principle
    anchor: "#the-principle"
    purpose: overview
  - heading: Review windows
    anchor: "#review-windows"
    purpose: decision
  - heading: What expiry does
    anchor: "#what-expiry-does"
    purpose: implementation
  - heading: Event-driven invalidation
    anchor: "#event-driven-invalidation"
    purpose: implementation
  - heading: Enforcement
    anchor: "#enforcement"
    purpose: validation
  - heading: Worked classifications
    anchor: "#worked-classifications"
    purpose: examples
estimated_tokens: 2283
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related_skills: [evidence-validation, repository-analysis, web-research, research-synthesis]
related:
  - knowledge/ai-engineering/source-scoring.md
  - knowledge/ai-engineering/repository-status.md
  - scripts/update/check_staleness.py
  - workflows/knowledge-base-maintenance/WORKFLOW.md
sources:
  - title: "GitHub REST API — Get a repository"
    url: https://docs.github.com/en/rest/repos/repos#get-a-repository
    type: official-docs
    organization: GitHub
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "pushed_at and archived are the observable signals that invalidate repository-derived claims independently of any schedule."
  - title: "Semantic Versioning 2.0.0"
    url: https://semver.org/
    type: specification
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "A MAJOR bump upstream is an invalidation event for any claim scoped to the previous major."
---

# Freshness Policy

## The principle

**A claim's shelf life is a property of the claim, not of the source.**

A 2017 paper on the computational complexity of an algorithm is as trustworthy today as when it
was published. A 2025 blog post about a framework's default caching behaviour may have been wrong
the week after it was written. Prestige does not confer durability, and recency does not confer
accuracy — the two are independent axes, and conflating them is how knowledge bases rot in one
direction while looking current in the other.

The corollary is that every artifact needs two dates:

```text
verified_at   the date the cited sources were last actually reached and confirmed
expires_at    the date after which the content must be re-verified before it may be relied upon
```

`verified_at` without `expires_at` is a claim with no shelf life, which means it will be trusted
forever. `expires_at` without `verified_at` is a promise with no evidence behind it.

## Review windows

Default windows by claim class. The window starts at `verified_at`.

```text
30 DAYS   pricing, quotas, rate limits, free-tier boundaries, model availability windows,
          anything a vendor can change without notice

90 DAYS   agent frameworks and their APIs · MCP servers and the MCP protocol itself ·
          model capabilities and benchmarks · framework defaults (caching, rendering,
          data fetching) · browser API behaviour · search-engine behaviour and SEO guidance ·
          package-registry security posture · anything in an "emerging consensus" area

6 MONTHS  library and tool APIs with a normal release cadence · component-library behaviour ·
          CI/CD tooling · observability stacks · cloud service features

12 MONTHS stable specifications and protocols (HTTP, OAuth 2.0/OIDC, JSON Schema, WCAG,
          OpenAPI, SemVer) · language semantics · design principles and craft guidance ·
          architectural patterns · scoring models and this policy itself

NO EXPIRY mathematical results · complexity classes · logic · published research findings,
          whose status changes by retraction or replication, not by time
          (a retraction is an event — see below)
```

Two modifiers:

```text
VOLATILITY   If the subject has shipped two or more MAJOR releases in the window, halve the
             window for claims scoped to it. Fast movers move faster than the calendar knows.
LOAD-BEARING If acting on the claim could delete data, move money, change authentication or
             ship to users, halve the window regardless of domain. The cost of being stale
             is what the window is really measuring.
```

## What expiry does

Expiry is not deletion, and it is not a silent loss of trust. It routes the artifact to one of
four outcomes:

```text
RE-VERIFY    Reach the sources again. If they still support the claim, update verified_at and
             set a new expires_at. This is the common case and it is cheap.

REFRESH      The sources changed. Update the content, record what changed and why, update both
             dates. The diff is the valuable part — "the default changed in v15" is worth more
             than the new default alone.

ARCHIVE      The claim is no longer true, and the reason is instructive. Move to archived with
             a superseded_by link. Archived content leaves the active index but stays in the
             repository, because deleting a wrong belief loses the reasoning that prevents it
             being re-adopted.

QUARANTINE   The claim can no longer be graded — the source is gone, paywalled, retracted, or
             was never reachable. Move to experimental/ or the quarantine list, exclude from the
             retrieval index, and record what would make it gradeable again.
```

What must never happen: **leaving expired content in the active index unchanged.** An expired
claim retrieved by an agent carries the confidence its label implies, and the label does not
visibly decay. That is the specific failure mode this policy exists to prevent.

## Event-driven invalidation

Schedules catch gradual decay. Events catch sudden invalidation, and they take precedence over
any window:

```text
REPOSITORY     archived · disabled · renamed · transferred to a new owner · license added,
               changed or removed · a MAJOR release that changes the behaviour a claim describes
               · an ownership or maintainer change · a public security advisory
PAPER          retraction · a published replication failure · a corrected version that changes
               the result · the authors disavowing a widely-cited misreading
SPECIFICATION  a new edition that changes the clause cited · a status change (draft → REC, or
               withdrawal) · an erratum affecting the cited behaviour
VENDOR         a pricing, quota or terms change · a product deprecation or sunset announcement ·
               an acquisition that changes the maintenance outlook
INTERNAL       a correction issue filed against this repository · a conflicting source found ·
               a downstream artifact reporting that acting on the claim failed
```

The response to an event is immediate for the affected records, not at the next scheduled run.
This is why repository metadata is refreshed from the API rather than curated by hand: an archive
flag appears in the same fetch that would otherwise have reported a healthy project.

## Enforcement

The policy is executable, not advisory.

```bash
# report everything past its review window, grouped by urgency
make staleness            # scripts/update/check_staleness.py

# CI fails on expired content in the active index
.github/workflows/kb-ci.yml → job: freshness
```

`check_staleness.py` reports:

```text
overdue      expires_at < today                       → must be actioned this run
due-soon     expires_at within 14 days                → schedule it
undated      active content with no expires_at         → a defect; the window must be set
unverified   content citing sources with no verified_at → a defect; nothing was reached
stale-data   repository records whose stars_checked_at is older than the window
```

CI treats `overdue` in the active index as a failure, and `undated` as a failure regardless of
location. The full maintenance loop that acts on the report is
[`workflows/knowledge-base-maintenance`](../../workflows/knowledge-base-maintenance/WORKFLOW.md).

## Worked classifications

Applying the rules to real content in this repository:

```text
MCP protocol capability semantics      90 days  — the protocol is evolving; a claim about
                                                  transport or capability names goes stale fast
Next.js default caching behaviour      90 days  — scoped to a major version; halved if two
                                                  majors ship inside the window
WCAG 2.2 contrast thresholds           12 months — a W3C Recommendation; changes only by
                                                  a new edition, which is an event
Postgres index types and their uses    12 months — language-level semantics of a stable system
"Lost in the Middle" U-shaped result   no expiry — a published finding; invalidated only by
                                                  retraction or failed replication
A vendor's free-tier request quota     30 days  — changeable without notice, and expensive
                                                  to be wrong about
A GitHub repository's star count       30 days  — not a truth claim but a measured snapshot;
                                                  always carries stars_checked_at
The scoring model in this file's       12 months — but a weight change is a policy change and
  sibling source-scoring.md                      requires an ADR, not a quiet edit
```

## References

- [`knowledge/ai-engineering/source-scoring.md`](source-scoring.md) — the recency component uses these windows
- [`knowledge/ai-engineering/repository-status.md`](repository-status.md) — status classifications that override the score
- [`scripts/update/check_staleness.py`](../../scripts/update/check_staleness.py) — the executable form
- [`scripts/update/fetch_github_metadata.py`](../../scripts/update/fetch_github_metadata.py) — event detection via the API
- [`workflows/knowledge-base-maintenance/WORKFLOW.md`](../../workflows/knowledge-base-maintenance/WORKFLOW.md)
- [`skills/evidence-validation/SKILL.md`](../../skills/evidence-validation/SKILL.md) · [`skills/repository-analysis/SKILL.md`](../../skills/repository-analysis/SKILL.md)
- [`.github/workflows/kb-ci.yml`](../../.github/workflows/kb-ci.yml) — the freshness job
