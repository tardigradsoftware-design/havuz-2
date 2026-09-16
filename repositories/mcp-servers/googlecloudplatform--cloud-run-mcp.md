---
id: googlecloudplatform--cloud-run-mcp
title: "GoogleCloudPlatform/cloud-run-mcp"
domain: mcp-servers
summary: >-
  GoogleCloudPlatform/cloud-run-mcp — ACTIVE, tier A,
  631 stars, license Apache-2.0, quality 7.64/10, trust 6.49/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: high
claim_type: fact
evidence_level: verified-github-api
tags: ["gcp", "github-repository", "mcp", "mcp-servers"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 5.0, "maintenance": 10.0, "adoption": 9.56, "documentation": 5.11, "reproducibility": 9.5, "security": 6.0, "recency": 9.97, "evidence": 6.5}
  quality_score: 7.64
  trust_score: 6.49
  tier: A
  maturity: production-ready
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "GoogleCloudPlatform/cloud-run-mcp on GitHub"
    url: https://github.com/GoogleCloudPlatform/cloud-run-mcp
    type: github-repository
    organization: GoogleCloudPlatform
    license: Apache-2.0
    confidence: high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# GoogleCloudPlatform/cloud-run-mcp

🟢 ACTIVE · tier **A** · production-ready · confidence **high**

> MCP server to deploy apps to Cloud Run

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/GoogleCloudPlatform/cloud-run-mcp> |
| Owner | GoogleCloudPlatform (Organization) |
| Official upstream | no |
| Language | JavaScript |
| License | `Apache-2.0` |
| Stars | 631 (checked 2026-09-15) |
| Forks | 121 |
| Open issues | 24 |
| Contributors | 14 |
| Last push | 2026-09-13 (2 days before verification) |
| Latest release | v1.10.0 (2026-03-04) |
| Archived | no |
| Fork | no |
| Homepage | — |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.0 |
| maintenance | 10.0 |
| adoption | 9.56 |
| documentation | 5.11 |
| reproducibility | 9.5 |
| security | 6.0 |
| recency | 9.97 |
| evidence | 6.5 |
| **quality_score** (weighted) | **7.64** |
| **trust_score** | **6.49** |

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
| README size | 13,299 bytes |

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

_No anomalies detected._

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug GoogleCloudPlatform/cloud-run-mcp
python3 scripts/generate-index/generate_repository_cards.py --category mcp-servers
```
