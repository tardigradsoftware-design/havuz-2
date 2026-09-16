---
id: cursor--cursor
title: "cursor/cursor"
domain: agent-skills
summary: >-
  cursor/cursor — MAINTENANCE, tier UNVERIFIED,
  33,244 stars, license NONE, quality 5.71/10, trust 3.26/10.
  Verified against the GitHub API on 2026-09-15.
status: active
confidence: low
claim_type: fact
evidence_level: verified-github-api
tags: ["agent-skills", "coding-agent", "github-repository", "issue-tracker"]
version: 1.0.0
updated: 2026-09-16
verified_at: 2026-09-15
expires_at: 2026-10-30
scoring:
  components: {"authority": 5.5, "maintenance": 5.5, "adoption": 10.0, "documentation": 4.05, "reproducibility": 2.5, "security": 4.0, "recency": 8.27, "evidence": 4.0}
  quality_score: 5.71
  trust_score: 3.26
  tier: UNVERIFIED
  maturity: maintenance-mode
  scored_by: scripts/lib/scoring.py
  scored_at: 2026-09-15
provenance:
  content_class: reference
  generated_by: scripts/generate-index/generate_repository_cards.py
  human_reviewed: false
sources:
  - title: "cursor/cursor on GitHub"
    url: https://github.com/cursor/cursor
    type: github-repository
    organization: cursor
    license: NONE
    confidence: low
    claim_type: fact
    verified_at: 2026-09-15
---

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Source of truth: metadata/repositories.json (GitHub API, 2026-09-15)
     Curated judgement: scripts/update/curation.json
     Regenerate: python3 scripts/generate-index/generate_repository_cards.py -->

# cursor/cursor

🟡 MAINTENANCE · tier **UNVERIFIED** · maintenance-mode · confidence **low**

> _No description published._

## Facts (verified 2026-09-15 via the GitHub API)

| Field | Value |
|---|---|
| URL | <https://github.com/cursor/cursor> |
| Owner | cursor (Organization) |
| Official upstream | no |
| Language | — |
| License | `NONE` |
| Stars | 33,244 (checked 2026-09-15) |
| Forks | 2,287 |
| Open issues | 3 |
| Contributors | 31 |
| Last push | 2026-05-12 (126 days before verification) |
| Latest release | — (no release) |
| Archived | no |
| Fork | no |
| Homepage | https://cursor.com |
| SECURITY.md | yes → `policy-published` |
| Repository kind | `software` |

## Scores

| Component | 0–10 |
|---|---|
| authority | 5.5 |
| maintenance | 5.5 |
| adoption | 10.0 |
| documentation | 4.05 |
| reproducibility | 2.5 |
| security | 4.0 |
| recency | 8.27 |
| evidence | 4.0 |
| **quality_score** (weighted) | **5.71** |
| **trust_score** | **3.26** |

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
| examples | no |
| security md | yes |
| changelog | no |
| contributing | no |
| root entries | yes |
| README size | 622 bytes |

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

Repository moved: `getcursor/cursor` -> `cursor/cursor`. Update any hard-coded URLs; the old path 404s once GitHub drops the redirect. No push in 126 days (>120d). Treat as maintenance mode: usable, but check for a recommended successor before adopting. NO LICENSE FILE DETECTED by GitHub. Copyright defaults to all-rights-reserved: do not vendor, copy or redistribute code from this repository. Reference and link only.

## How to re-verify

```bash
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug cursor/cursor
python3 scripts/generate-index/generate_repository_cards.py --category agent-skills
```
