---
id: anthropics--claude-code
title: "anthropics/claude-code"
domain: agent-skills
summary: >-
  anthropics/claude-code — ACTIVE, tier NO-LICENSE,
  150,327 stars, license NONE, quality 7.77/10, trust 6.34/10.
  Verified against the GitHub API on 2026-10-12.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-skills", "anthropic", "coding-agent", "github-repository"]
version: 1.0.0
updated: 2026-10-12
verified_at: 2026-10-12
expires_at: 2026-11-26
scoring:
  components: {"authority": 8.5, "maintenance": 10.0, "adoption": 10.0, "documentation": 5.24, "reproducibility": 4.5, "security": 5.0, "recency": 10.0, "evidence": 6.0}
  quality_score: 7.77
  trust_score: 6.34
  tier: NO-LICENSE
  maturity: early
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-10-12
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "anthropics/claude-code on GitHub"
    url: https://github.com/anthropics/claude-code
    type: github-repository
    organization: anthropics
    license: NONE
    license_risk: no-license-do-not-redistribute
    confidence: high
    claim_type: fact
    verified_at: 2026-10-12
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-10-12)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# anthropics/claude-code

🟢 ACTIVE · tier **NO-LICENSE** · early · confidence **high**

> _Upstream description, quoted as published and not verified here:_
>
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

> ⚠️ **LICENSE RISK — `no-license-do-not-redistribute`.** GitHub detected **no license file**
> on 2026-10-12. Default copyright applies, so all rights are reserved: **reference and link only**.
> Do not vendor, copy, quote at length, or redistribute any file from this repository, however
> useful it looks. A high star count does not create a license.

## Facts (verified 2026-10-12 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/anthropics/claude-code> |
| Owner | anthropics (Organization) |
| Official upstream | yes |
| Language | TypeScript |
| License | `NONE` |
| Stars | 150,327 (checked 2026-10-12) |
| Forks | 26,298 |
| Open issues | 14,657 |
| Contributors | 57 |
| Last push | 2026-10-11 (0 days before verification) |
| Latest release | v2.1.296 (2026-10-09) |
| Archived | no |
| Fork | no |
| Homepage | [https://code.claude.com/docs/en/overview](https://code.claude.com/docs/en/overview) |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.5 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 5.24 |
| reproducibility | 4.5 |
| security | 5.0 |
| recency | 10.0 |
| evidence | 6.0 |
| **quality_score** (weighted) | **7.77** |
| **trust_score** | **6.34** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | no |
| tests | no |
| ci | yes |
| examples | yes |
| security md | yes |
| changelog | yes |
| contributing | no |
| root entries | yes |
| README size | 2,873 bytes |

## Curated judgement

_The following is **RECOMMENDATION**, not fact. It was written by a human/agent reviewer
(not yet curated) and must be
re-checked against your own constraints._

**Recommended for**

- _not curated yet_

**Not recommended for**

- _not curated yet_

**Strengths**

- _not curated yet_

**Weaknesses**

- _not curated yet_

**Related projects**

- _not curated yet_

## Verification notes

NO LICENSE FILE DETECTED by GitHub. Copyright defaults to all-rights-reserved: do not vendor, copy or redistribute code from this repository. Reference and link only.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug anthropics/claude-code
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
