# AGENTS.md — `metadata/`

Rules for any agent touching the machine-readable registries in this directory. This data is
**generated**, and the distinction matters: hand-editing it is how a knowledge base starts lying
about itself.

## Contents

| File | Records | Producer |
|---|---|---|
| `repositories.json` | 414 repositories, scored and tiered | `scripts/update/fetch_github_metadata.py` |
| `sources-papers.json` | 9 verified papers | `scripts/crawl/verify_arxiv_papers.py` |
| `pending-paper-candidates.json` | 61 quarantined candidates | same |
| `curation.json` | Curated human judgement for ~25 repositories | **hand-edited — the one exception** |

## Hard rules

1. **Never hand-edit `repositories.json`.** It is regenerated from live GitHub API data merged with
   `curation.json`. A hand edit is overwritten on the next run and, worse, silently diverges from the
   cached evidence in `.cache/gh/`.
2. **Judgement goes in `curation.json`, not in the output.** If a repository's score is wrong because
   the observable facts do not capture something — a project that is excellent but young, or popular
   but abandoned in all but name — record the reasoning in `curation.json` and let the fetcher merge
   it. That keeps the reasoning auditable and the data reproducible.
3. **Scores come from observable GitHub API facts only.** Authority 20%, maintenance 15%, adoption
   15%, documentation 10%, reproducibility 10%, security 10%, recency 10%, evidence 10%. Never
   invent a data point to make a score look right. A missing fact lowers confidence in the score; it
   does not get estimated.
4. **`license: null` means legally unsafe, not low-scoring.** Any repository the API returns without a
   license is marked `license_risk: no-license-do-not-redistribute`. This is a hard override that
   beats the weighted score regardless of how good the project is. `anthropics/skills` and
   `openai/skills` are both in this state as of 2026-09-15.
5. **Archived and maintenance-mode projects are flagged, never merely scored down.** 10 records are
   currently `ARCHIVED`. An archived project can still be the right answer for a frozen dependency;
   hiding that behind a low tier would be a disservice.
6. **Papers are verified individually against the primary source.** An aggregator API was observed
   returning **wrong titles for valid arXiv identifiers**, which is why 61 candidates sit quarantined
   rather than published. Do not promote a candidate without reaching `arxiv.org/abs/<id>` directly
   and confirming title, authors and version date.
7. **Renames are resolved, not duplicated.** 27 confirmed renames exist in the corpus. The fetcher
   follows them; 417 seeds collapsed to 414 records through alias dedup. If you add a seed that turns
   out to be an alias, the record count drops and that is correct behaviour.

## Regenerating

```bash
python3 scripts/update/fetch_github_metadata.py    # live API -> repositories.json (+ curation merge)
python3 scripts/validate/validate_json.py          # 849 records across all registries
python3 scripts/update/check_staleness.py          # what has aged past its window
python3 scripts/deduplicate/dedupe.py              # alias and duplicate detection
python3 scripts/generate-index/extract_registries.py
python3 scripts/generate-index/build_index.py
python3 scripts/generate-index/generate_repository_cards.py
python3 scripts/generate-index/update_readme_stats.py
```

The last four are what turn this directory into `indexes/` and `repositories/`. Running the fetcher
without them leaves the human-readable corpus inconsistent with the machine-readable one.

## Credentials

`fetch_github_metadata.py` uses the environment's own GitHub credentials. **Never** write a token into
a file, a script, a config, an environment file or a commit message in this repository. During the
1.0.0 build a personal access token was pasted into the conversation; it was not used, not stored and
not written anywhere, and the user was advised to revoke it. That is the expected handling.

Rate limit: 5,000 authenticated core requests per hour confirmed. A full refresh of 414 repositories
fits comfortably; approximately 1,900 responses are cached under `.cache/gh/` so the corpus can be
re-audited against the exact data it was built from.

## Staleness

Metadata ages. `check_staleness.py` reports what has passed its window. A refresh is always a **patch**
release: star counts and push dates change, scores and tiers move, and none of that is a content
decision. Record the refresh in [`../CHANGELOG.md`](../CHANGELOG.md) with the date and the tier
movement if any repository changed tier.

## References

- [`../AGENTS.md`](../AGENTS.md) — the repository-wide operating contract
- [`../SECURITY.md`](../SECURITY.md) — the exclusion policy and credential handling
- [`../scripts/lib/scoring.py`](../scripts/lib/scoring.py) — the weighted model and its hard overrides
- [`../knowledge/ai-engineering/source-scoring.md`](../knowledge/ai-engineering/source-scoring.md) — why the model is shaped this way
- [`../knowledge/ai-engineering/freshness-policy.md`](../knowledge/ai-engineering/freshness-policy.md) — the windows `check_staleness.py` enforces
- [`../knowledge/security/llm-security/excluded-sources.md`](../knowledge/security/llm-security/excluded-sources.md) — what is excluded and why
- [`../indexes/repositories.md`](../indexes/repositories.md) — the generated index over this data
