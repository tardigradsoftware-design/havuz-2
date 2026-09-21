---
id: hesreallyhim--awesome-claude-code
title: "hesreallyhim/awesome-claude-code"
domain: agent-skills
summary: >-
  hesreallyhim/awesome-claude-code — ACTIVE, tier A,
  54,374 stars, license NOASSERTION, quality 8.21/10, trust 7.95/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent", "agent-skills", "catalog", "discovery", "github-repository", "skills"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 7.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 7.0, "reproducibility": 7.6, "security": 6.5, "recency": 10.0, "evidence": 6.0}
  quality_score: 8.21
  trust_score: 7.95
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: true
sources:
  - title: "hesreallyhim/awesome-claude-code on GitHub"
    url: https://github.com/hesreallyhim/awesome-claude-code
    type: github-repository
    organization: hesreallyhim
    license: NOASSERTION
    license_risk: custom-license-review-before-vendoring
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# hesreallyhim/awesome-claude-code

🟢 ACTIVE · tier **A** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC. A delectable showcase of top tier skills, ambidextrous agents, scintillating status lines, top notch developer tooling, and also we have plugins

> ⚠️ **LICENSE RISK — `custom-license-review-before-vendoring`.** GitHub could not classify
> this license (`NOASSERTION`) on 2026-09-21, so its terms are unknown to this repository. Read the
> upstream `LICENSE` yourself **before** vendoring, copying or redistributing anything from it —
> a custom license may permit, restrict or require attribution in ways a standard SPDX id would
> have made obvious.

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/hesreallyhim/awesome-claude-code> |
| Owner | hesreallyhim (User) |
| Official upstream | yes |
| Language | Python |
| License | `NOASSERTION` |
| Stars | 54,374 (checked 2026-09-21) |
| Forks | 4,741 |
| Open issues | 1,098 |
| Contributors | 14 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `catalog` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 7.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 7.0 |
| reproducibility | 7.6 |
| security | 6.5 |
| recency | 10.0 |
| evidence | 6.0 |
| **quality_score** (weighted) | **8.21** |
| **trust_score** | **7.95** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | yes |
| ci | yes |
| examples | no |
| security md | yes |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 194,635 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(on 2026-09-21) and must be
re-checked against your own constraints._

**Recommended for**

- Broad discovery of Claude Code resources, tools and community skills

**Not recommended for**

- Automatic ingestion - the list is large and not individually vetted
- Vendoring content: non-SPDX license

**Strengths**

- Very large resource surface (~195 KB README verified)
- Has SECURITY.md and CI, unusual for a catalogue
- 14 contributors, pushed on verification date

**Weaknesses**

- License is non-SPDX (NOASSERTION) - read it before reusing
- Single-maintainer concentration (14 contributors for 54k stars)

**Related projects**

- VoltAgent/awesome-agent-skills
- anthropics/claude-code
- ComposioHQ/awesome-claude-skills

## Verification notes

Non-SPDX/custom license (NOASSERTION). Read the license text before vendoring; referencing is fine. Verified 2026-09-15: ACTIVE, 54k stars, NOASSERTION license. Use as a discovery layer only; re-verify each resource.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug hesreallyhim/awesome-claude-code
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
