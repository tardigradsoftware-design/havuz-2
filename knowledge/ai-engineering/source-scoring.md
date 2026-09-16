---
id: source-scoring
title: "Source scoring: how every repository and claim in this knowledge base is graded"
domain: ai-engineering
summary: >-
  The weighted 0-10 scoring model applied to all 414 repositories in metadata/repositories.json,
  the tier thresholds it produces, and the rule that makes it honest: every component is computed
  from observable GitHub API facts or a cited source, never from reputation, star count alone, or
  an invented number.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [scoring, methodology, source-quality, trust, verification, curation]
applies_to: [repositories, sources, skills, knowledge, evaluations]
audience: [both]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
sections:
  - heading: Why a score at all
    anchor: "#why-a-score-at-all"
    purpose: overview
  - heading: The model
    anchor: "#the-model"
    purpose: decision
  - heading: Component definitions
    anchor: "#component-definitions"
    purpose: implementation
  - heading: Tiers
    anchor: "#tiers"
    purpose: decision
  - heading: Hard overrides
    anchor: "#hard-overrides"
    purpose: pitfalls
  - heading: What the score does not mean
    anchor: "#what-the-score-does-not-mean"
    purpose: pitfalls
  - heading: Curation layer
    anchor: "#curation-layer"
    purpose: implementation
  - heading: Worked examples
    anchor: "#worked-examples"
    purpose: examples
  - heading: Reproducing the score
    anchor: "#reproducing-the-score"
    purpose: validation
estimated_tokens: 3651
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related_skills: [evidence-validation, repository-analysis, competitive-analysis, web-research]
related_repositories: [ossf/scorecard]
related:
  - knowledge/ai-engineering/freshness-policy.md
  - knowledge/ai-engineering/repository-status.md
  - scripts/lib/scoring.py
  - metadata/repositories.json
sources:
  - title: "GitHub REST API — Get a repository"
    url: https://docs.github.com/en/rest/repos/repos#get-a-repository
    type: official-docs
    organization: GitHub
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Defines every field the score is computed from: stargazers_count, pushed_at, archived, disabled, license.spdx_id, open_issues_count, forks_count, default_branch."
  - title: "OpenSSF Scorecard"
    url: https://github.com/ossf/scorecard
    type: github-repository
    organization: Open Source Security Foundation
    license: Apache-2.0
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Prior art for scoring open-source health from observable signals rather than reputation. Its check set informed the maintenance and reproducibility components."
  - title: "Semantic Versioning 2.0.0"
    url: https://semver.org/
    type: specification
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "Release-tag parsing used by the maintenance component."
---

# Source Scoring

## Why a score at all

An agent reading this knowledge base will act on what it finds. A bare list of repositories with
star counts invites the single worst available inference — that attention equals quality — and
produces recommendations of archived projects, license-less code, and abandoned frameworks.

A score does not replace judgement. It makes judgement **reproducible**: two runs on the same
data produce the same number, and every number decomposes into components that can be inspected
and argued with.

Three properties the model is required to have:

```text
OBSERVABLE    Every input is a fact retrieved from an API or a cited document. No component
              is filled in from reputation, familiarity or plausible-sounding knowledge.
DECOMPOSABLE  The total is a weighted sum of named components, each stored alongside it, so a
              low score can be diagnosed rather than merely accepted.
MONOTONIC     More evidence never lowers a score. Absence of evidence lowers it — which is the
              point, because absence of evidence is the actual risk.
```

## The model

Eight weighted components, 0–10 scale, computed in [`scripts/lib/scoring.py`](../../scripts/lib/scoring.py):

| Component | Weight | Question it answers |
|---|---:|---|
| `authority` | 20% | Who is responsible, and are they the minting authority for this claim? |
| `maintenance` | 15% | Is it alive, and will it be alive when the dependency matters? |
| `adoption` | 15% | Is it used, by how many, and does usage corroborate quality? |
| `documentation` | 10% | Can someone actually use it without reading the source? |
| `reproducibility` | 10% | Can the claim be re-derived — code, tests, CI, data, method? |
| `security` | 10% | Is there a disclosure path, and is the supply chain defensible? |
| `recency` | 10% | Is the information current for the version and date in question? |
| `evidence` | 10% | Is the claim corroborated by an independent source? |

```text
trust_score = Σ (component_i × weight_i)      rounded to 2 decimals
```

Weights are a decision, not a discovery. They encode this repository's priorities: **who stands
behind it and whether it is still alive** (35% combined) outweigh **how popular it is** (15%).
A changed weight is a policy change and belongs in an ADR, not in a code edit.

## Component definitions

Each component is computed from named fields. Where a field is missing, the component is scored
from what remains and the record is marked `UNKNOWN` for that dimension — never guessed.

### authority (20%)

```text
10   the specification body, standards org, or original author of the technique
 9   a verified major-vendor org (microsoft, google, vercel, anthropics, openai, github)
 8   a foundation or established org (CNCF, Apache, OpenSSF, Linux Foundation)
 7   a well-known individual maintainer with a history in the domain
 5   an organisation with no domain history, or an unverified account
 3   an anonymous or newly-created account
 1   identity cannot be established
```

Owner identity is read from the repository owner's `type` (`Organization` vs `User`) and the org's
public profile. Verification status is **not** inferred from the name — a name that sounds official
is not evidence.

### maintenance (15%)

Derived from `pushed_at`, `archived`, `disabled`, release tags and contributor count, measured
against the retrieval date (2026-09-15 for the current dataset):

```text
10   pushed < 30 days ago, releases within 90 days, multiple recent contributors
 8   pushed < 90 days ago, releases within 180 days
 6   pushed < 180 days ago, or releases within 12 months
 4   pushed < 12 months ago, no release in 12 months
 2   pushed 12-24 months ago
 0   pushed > 24 months ago, OR archived, OR disabled
```

`archived: true` caps the component at 0 regardless of stars. This is deliberate: an archived
project with 40k stars is a frozen artifact, and treating it as a live dependency is the specific
error this model exists to prevent.

### adoption (15%)

`stargazers_count` and `forks_count`, log-scaled, **always paired with `stars_checked_at`**:

```text
10   ≥ 50,000 stars          8   ≥ 10,000        6   ≥ 2,000
 4   ≥ 500                   2   ≥ 50            0   < 50 or unknown
```

Log scaling is essential. Linear scaling would let a 400k-star tutorial repository outvote a
2k-star specification, and the star count of a curated list measures the curator's marketing, not
the listed projects' quality. Adoption never contributes more than 15%, and it can never lift a
record above its tier ceiling when maintenance or license fails — see [Hard overrides](#hard-overrides).

### documentation (10%)

Presence and quality signals detectable without judgement calls:

```text
+3   README present and > 2,000 characters
+2   a docs/ directory, a documentation site link, or a wiki
+2   CONTRIBUTING.md present
+1   examples/, samples/ or a cookbook directory
+1   CHANGELOG or release notes maintained
+1   issue templates present
capped at 10
```

### reproducibility (10%)

```text
+3   CI configuration present (.github/workflows, .gitlab-ci.yml, Jenkinsfile, …)
+3   a test directory or test configuration
+2   a lockfile or pinned dependency manifest
+2   releases published as tags with artifacts
capped at 10
```

For research artifacts the equivalent question is "could someone re-run this?": code released,
dataset available, method described, hyperparameters stated.

### security (10%)

```text
+4   SECURITY.md with a disclosure path
+3   a license file present and identified (SPDX resolved)
+2   no known open advisory at the default branch
+1   code-owner or branch-protection signals visible
capped at 10
```

`license: null` does not merely score 0 here — it triggers the hard override below.

### recency (10%)

For repositories this is `pushed_at`. For documents and papers it is the publication date judged
against the **claim's** shelf life, not the document's prestige:

```text
10   updated within the domain's freshness window (see freshness-policy.md)
 7   up to 2× the window
 4   up to 4× the window
 1   beyond that, but the claim is version-independent (a specification, a complexity result)
 0   beyond that, and the claim is version-dependent (framework defaults, pricing, model capability)
```

A 2019 paper on algorithmic complexity stays high. A 2024 blog post on framework caching defaults
is already suspect. Recency is a property of the *claim*, never of the *publisher*.

### evidence (10%)

```text
10   primary source reached directly + ≥1 independent corroboration
 8   primary source reached directly, self-consistent, current
 6   official documentation for the exact version, no corroboration
 4   a single credible secondary source
 2   community source only
 0   no source; the statement is model output — must be labelled GENERATED
```

Independence means different **provenance**, not different URLs. Three blogs restating one
changelog are one source and score as one.

## Tiers

| Tier | Score | Meaning for an agent |
|---|---|---|
| `S` | ≥ 9.0 | Adopt or cite without further checking, subject to fit |
| `A` | 7.5 – 8.99 | Prefer; verify the specific claim you depend on |
| `B` | 6.0 – 7.49 | Usable; check status, license and version before depending |
| `C` | 4.0 – 5.99 | Caution; needs a stated reason to choose it over a higher tier |
| `EXPERIMENTAL` | any | Explicitly experimental by its own declaration — never a production dependency |
| `ARCHIVED` | any | Frozen. Fine as a reference or a finished tool; fatal as a security dependency |
| `UNVERIFIED` | any | Could not be verified. Excluded from the retrieval index; never cited |
| `DEPRECATED` | any | Superseded; a successor link must exist |

`EXPERIMENTAL`, `ARCHIVED`, `UNVERIFIED` and `DEPRECATED` are **status tiers, not score tiers**.
They override the numeric band, because a 9.2-scoring archived repository is not an `S` adoption
candidate — it is a frozen artifact with good history.

## Hard overrides

These apply regardless of the computed score, and they are the reason the model is not merely a
weighted average:

```text
license: null                → license_risk = no-license-do-not-redistribute
                               Vendoring and redistribution prohibited. Reference and link only.
                               A high star count does not mitigate this.
archived: true               → tier = ARCHIVED (score retained for history)
disabled: true               → tier = ARCHIVED, flagged as inaccessible
self-declared experimental   → tier = EXPERIMENTAL
unresolvable / 404           → tier = UNVERIFIED, moved out of the active index
no reachable primary source  → confidence ≤ medium, and the record says single-sourced
leaked or prohibited content → REJECTED outright, never scored (see knowledge/security/llm-security/excluded-sources.md)
```

The `license: null` override is the most consequential one in this repository. Two of the highest-
profile agent-skill collections in the seed set return `license: null` from the GitHub API. They
are excellent references and they are **not** redistributable. Any scoring model that expressed
this as "a lower number" would let a sufficiently popular unlicensed project outscore a licensed
one, which is exactly backwards.

## What the score does not mean

```text
✗ It is not a quality judgement about the code. It measures trustworthiness as a dependency
  and as a source of claims — two different things from elegance.
✗ It is not comparable across categories. A specification and a tutorial are both scorable,
  but "which is better" is not a question the score answers.
✗ It is not stable. It is a snapshot with a date. Every star count in this repository carries
  stars_checked_at, and re-running the fetcher changes the numbers.
✗ It is not a substitute for fit. A tier-S library that solves a different problem is worse
  than a tier-B library that solves yours. Fit is scored separately, per decision
  (see skills/competitive-analysis).
✗ It does not measure the maintainers' competence, only the observable traces of their work.
```

## Curation layer

Automated scoring cannot see everything, so a small curated layer sits on top in
[`scripts/update/curation.json`](../../scripts/update/curation.json). It carries fields the API
does not expose:

```text
repo_kind          what the project actually is (framework, skill-collection, mcp-server,
                   benchmark, research-code, documentation, tool, dataset, model)
security_status    a considered judgement about safety to adopt, where the API is silent
curation_note      why a human looked at this one specifically
curated_at         when, so the judgement has a shelf life
```

Curation is merged into `metadata/repositories.json` by the fetcher with provenance recorded, so
a curated field is always distinguishable from an API-derived one. Curated judgements are the
only place where human opinion enters the score, and they are dated and attributed for that reason.

Roughly 31 of 414 records carry curation. That ratio is intentional: curation is expensive and
should be spent where automation is blind, not applied uniformly.

## Worked examples

Three records from the current dataset, showing how the components combine:

```text
A high-scoring live project
  authority 9 (verified major-vendor org)   maintenance 10 (pushed within 30 days, releases)
  adoption 10 (≥50k stars)                  documentation 9   reproducibility 9
  security 8                                recency 10        evidence 8
  → trust_score ≈ 9.2 → tier S

A popular but frozen project
  authority 8   maintenance 0 (archived — caps regardless of history)   adoption 9
  documentation 7   reproducibility 6   security 6   recency 1   evidence 6
  → trust_score ≈ 5.9, but tier = ARCHIVED (status override, not score)
  → correct handling: cite as prior art, never adopt as a dependency

A widely-starred collection with no license file
  authority 7   maintenance 9   adoption 10   documentation 6
  reproducibility 3   security 3 (license null)   recency 9   evidence 5
  → trust_score ≈ 6.6, tier B
  → license_risk = no-license-do-not-redistribute
  → correct handling: link and summarise with attribution; never vendor, copy or redistribute
```

The second and third examples are the reason the override layer exists. In both, a pure weighted
average produces a number that would mislead an agent into the wrong action.

## Reproducing the score

```bash
# refresh observable facts from the GitHub API (authenticated; 5000 requests/hour)
make fetch-repos            # scripts/update/fetch_github_metadata.py

# recompute every score, tier and override from the refreshed records
python3 scripts/update/fetch_github_metadata.py --score-only

# regenerate the human-readable cards from the scored records
make cards                  # scripts/generate-index/generate_repository_cards.py
```

The scoring implementation is deterministic: the same input JSON produces byte-identical output.
CI asserts this, so a score change always corresponds to a data change.

## References

- [`scripts/lib/scoring.py`](../../scripts/lib/scoring.py) — the implementation
- [`knowledge/ai-engineering/freshness-policy.md`](freshness-policy.md) — the recency windows
- [`knowledge/ai-engineering/repository-status.md`](repository-status.md) — status classifications
- [`knowledge/research/source-conflict-case-study.md`](../research/source-conflict-case-study.md) — a real conflict resolved by precedence
- [`skills/evidence-validation/SKILL.md`](../../skills/evidence-validation/SKILL.md) — the per-claim version of this policy
- [`metadata/repositories.json`](../../metadata/repositories.json) — 414 scored records
- GitHub REST API — <https://docs.github.com/en/rest/repos/repos> · OpenSSF Scorecard — <https://github.com/ossf/scorecard>
