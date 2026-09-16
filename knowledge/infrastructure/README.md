# infrastructure

> **Status: scaffolded, empty.** The taxonomy requires this domain and skills link here, but no
> article has been authored yet. A link to an empty directory is an honest gap; a fabricated article
> to fill it would not be.

## What belongs here

Infrastructure: compute, networking and storage decisions for systems that host models or serve agent traffic.

## Rules for the first article

- Graded frontmatter validated against [`schemas/knowledge.schema.json`](../../schemas/knowledge.schema.json)
  with `additionalProperties: false`. Required: `id`, `title`, `domain`, `summary`, `status`,
  `confidence`, `claim_type`, `evidence_level`, `tags`, `applies_to`, `version`, `updated`,
  `verified_at`, `expires_at`, `provenance`, `related`, `sources[]`.
- `confidence: high` requires `sources[]`. Either cite or downgrade — the validator warns on exactly
  this and the warning is never a false positive.
- `domain` must be a value from the schema enum, not a free string.
- Freshness windows come from
  [`knowledge/ai-engineering/freshness-policy.md`](../ai-engineering/freshness-policy.md):
  30 days for security and pricing, 90 for fast-moving tooling, 180 for framework behaviour,
  365 for architecture and theory, and no expiry for mathematics or specifications.
- Nothing copied from an external README, blog or documentation page. Summarise, cite, respect the
  license. Star count is adoption, never quality.
- Conflicting sources are recorded with the precedence rule applied, not silently resolved.

## Start here

- [`skills/deployment/SKILL.md`](../../skills/deployment/SKILL.md)
- [`AGENTS.md`](../../AGENTS.md) — the operating contract
- [`CONTRIBUTING.md`](../../CONTRIBUTING.md) — the contribution workflow
- [`CHANGELOG.md`](../../CHANGELOG.md) — record what you add, and why

```bash
python3 scripts/validate/validate_frontmatter.py
python3 scripts/generate-index/extract_registries.py && python3 scripts/generate-index/build_index.py
```
