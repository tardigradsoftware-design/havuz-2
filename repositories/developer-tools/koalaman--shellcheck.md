---
id: koalaman--shellcheck
title: "koalaman/shellcheck"
domain: developer-tools
summary: >-
  koalaman/shellcheck — ACTIVE, tier S,
  40,058 stars, license GPL-3.0, quality 8.27/10, trust 8.24/10.
  Verified against the GitHub API on 2026-09-21.
status: active
confidence: very-high
claim_type: fact
evidence_level: verified-github-api
tags: ["developer-tools", "github-repository", "linting", "shell"]
version: 1.0.0
updated: 2026-09-21
verified_at: 2026-09-21
expires_at: 2026-11-05
scoring:
  components: {"authority": 8.0, "maintenance": 10.0, "adoption": 10.0, "documentation": 6.76, "reproducibility": 7.95, "security": 4.5, "recency": 10.0, "evidence": 7.5}
  quality_score: 8.27
  trust_score: 8.24
  tier: S
  maturity: production-grade
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-21
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "koalaman/shellcheck on GitHub"
    url: https://github.com/koalaman/shellcheck
    type: github-repository
    organization: koalaman
    license: GPL-3.0
    license_risk: none
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-21
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-21)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# koalaman/shellcheck

🟢 ACTIVE · tier **S** · production-grade · confidence **very-high**

> _Upstream description, quoted as published and not verified here:_
>
> ShellCheck, a static analysis tool for shell scripts

## Facts (verified 2026-09-21 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/koalaman/shellcheck> |
| Owner | koalaman (User) |
| Official upstream | yes |
| Language | Haskell |
| License | `GPL-3.0` |
| Stars | 40,058 (checked 2026-09-21) |
| Forks | 1,946 |
| Open issues | 1,134 |
| Contributors | 166 |
| Last push | 2026-09-21 (0 days before verification) |
| Latest release | v0.11.0 (2025-08-04) |
| Archived | no |
| Fork | no |
| Homepage | [https://www.shellcheck.net](https://www.shellcheck.net) |
| SECURITY.md | no → `no-policy` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 8.0 |
| maintenance | 10.0 |
| adoption | 10.0 |
| documentation | 6.76 |
| reproducibility | 7.95 |
| security | 4.5 |
| recency | 10.0 |
| evidence | 7.5 |
| **quality_score** (weighted) | **8.27** |
| **trust_score** | **8.24** |

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
| security md | no |
| changelog | yes |
| contributing | no |
| root entries | yes |
| README size | 21,160 bytes |

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
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug koalaman/shellcheck
python3 scripts/generate-index/generate_repository_cards.py --category developer-tools
```
