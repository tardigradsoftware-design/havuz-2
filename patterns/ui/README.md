# ui

> **Status: scaffolded, empty.** The directory exists because the taxonomy requires it and because
> links elsewhere in this repository point here. No content has been authored yet.

## What belongs here

UI patterns: interface structures that solve a recurring interaction problem, with the forces that make them work.

## Before you add anything

Read the operating contract in [`AGENTS.md`](../../AGENTS.md) and the contribution workflow in
[`CONTRIBUTING.md`](../../CONTRIBUTING.md). In short:

- Every document carries graded frontmatter validated against a schema in
  [`schemas/`](../../schemas/) with `additionalProperties: false`. An unknown field fails CI.
- Every claim carries `claim_type`, `evidence_level` and `confidence`, and `confidence: high`
  requires `sources[]`. Either cite or downgrade — there is no third option.
- Nothing is copied from an external README, blog post or documentation page. Summarise, cite, and
  respect the source license. Repositories the GitHub API returns without a license are marked
  `no-license-do-not-redistribute` and must not be vendored.
- Star count is an adoption signal, never a quality signal. Archived and maintenance-mode projects
  are flagged as such rather than quietly scored down.
- Leaked, extracted or improperly obtained model internals are refused regardless of popularity.
  See [`SECURITY.md`](../../SECURITY.md).

## Start here

- [`knowledge/ui-ux/visual-hierarchy.md`](../../knowledge/ui-ux/visual-hierarchy.md)
- [`CHANGELOG.md`](../../CHANGELOG.md) — record what you add, and why
- [`indexes/`](../../indexes/) — the generated indexes; regenerate them after adding content

```bash
python3 scripts/validate/validate_frontmatter.py
python3 scripts/validate/validate_links.py --internal
python3 scripts/generate-index/extract_registries.py
python3 scripts/generate-index/build_index.py
```

`make validate` runs the full suite. Do not commit with errors.
