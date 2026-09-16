---
id: hashicorp--terraform
title: "hashicorp/terraform"
domain: developer-tools
summary: >-
  hashicorp/terraform — ACTIVE, tier A,
  49,659 stars, license NOASSERTION, quality 8.04/10, trust 7.87/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["developer-tools", "github-repository", "iac"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 9.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.83, "reproducibility": 6.6, "security": 4.0, "recency": 10.0, "evidence": 5.0}
  quality_score: 8.04
  trust_score: 7.87
  tier: A
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "hashicorp/terraform on GitHub"
    url: https://github.com/hashicorp/terraform
    type: github-repository
    organization: hashicorp
    license: NOASSERTION
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# hashicorp/terraform

🟢 ACTIVE · tier **A** · production-grade · confidence **very-high**

> Terraform enables you to safely and predictably create, change, and improve infrastructure. It is a source-available tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned.

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/hashicorp/terraform> |
| Owner | hashicorp (Organization) |
| Official upstream | yes |
| Language | Go |
| License | `NOASSERTION` |
| Stars | 49,659 (checked 2026-09-15) |
| Forks | 10,615 |
| Open issues | 1,922 |
| Contributors | 351 |
| Last push | 2026-09-15 (0 days before verification) |
| Latest release | v1.16.2 (2026-09-09) |
| Archived | no |
| Fork | no |
| Homepage | http://developer.hashicorp.com/terraform |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 9.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.83 |
| reproducibility | 6.6 |
| security | 4.0 |
| recency | 10.0 |
| evidence | 5.0 |
| **quality_score** (weighted) | **8.04** |
| **trust_score** | **7.87** |

Weights: authority 20%, maintenance 15%, adoption 15%, documentation / reproducibility /
security / recency / evidence 10% each. See
[`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md).

## Repository structure signals

| Signal | Present |
|---|---|
| readme | yes |
| docs | yes |
| tests | no |
| ci | yes |
| examples | no |
| security md | no |
| changelog | yes |
| contributing | no |
| root entries | yes |
| README size | 3,935 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug hashicorp/terraform
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
