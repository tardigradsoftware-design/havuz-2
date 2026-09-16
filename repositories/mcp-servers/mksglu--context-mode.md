---
id: mksglu--context-mode
title: "mksglu/context-mode"
domain: mcp-servers
summary: >-
  mksglu/context-mode — ACTIVE, tier A,
  23,009 stars, license NOASSERTION, quality 7.81/10, trust 7.1/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["context", "github-repository", "mcp", "mcp-servers", "tokens"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 5.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 9.5, "reproducibility": 8.1, "security": 3.0, "recency": 10.0, "evidence": 7.5}
  quality_score: 7.81
  trust_score: 7.1
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "mksglu/context-mode on GitHub"
    url: https://github.com/mksglu/context-mode
    type: github-repository
    organization: mksglu
    license: NOASSERTION
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# mksglu/context-mode

🟢 ACTIVE · tier **A** · production-grade · confidence **high**

> Context window optimization for AI coding agents. Sandboxes tool output (98% reduction), persists session memory, and   enforces routing across 17 platforms via MCP + hooks.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/mksglu/context-mode> |
| Owner | mksglu (User) |
| Official upstream | no |
| Language | TypeScript |
| License | `NOASSERTION` |
| Stars | 23,009 (checked 2026-09-15) |
| Forks | 1,661 |
| Open issues | 246 |
| Contributors | 110 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v1.0.169 (2026-06-29) |
| Archived | no |
| Fork | no |
| Homepage | https://context-mode.com |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 9.5 |
| reproducibility | 8.1 |
| security | 3.0 |
| recency | 10.0 |
| evidence | 7.5 |
| **quality_score** (weighted) | **7.81** |
| **trust_score** | **7.1** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | yes |
| tests | yes |
| ci | yes |
| examples | no |
| security md | no |
| changelog | no |
| contributing | yes |
| root entries | yes |
| README size | 94,871 bytes |

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

Non-SPDX/custom license (NOASSERTION). Read the license text before vendoring; referencing is fine.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug mksglu/context-mode
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
