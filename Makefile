# havuz-2 — AI Engineering Intelligence Repository
# Everything here is safe to run repeatedly. `make refresh` needs GITHUB_TOKEN.

PY      ?= python3
TOKEN   ?= $(GITHUB_TOKEN)

.DEFAULT_GOAL := help

.PHONY: help install validate validate-frontmatter validate-json validate-links validate-policy \
        dedupe stale refresh refresh-github refresh-papers score index cards stats registries \
        urls audit clean ci

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-22s\033[0m %s\n", $$1, $$2}'

install: ## Install tooling dependencies
	$(PY) -m pip install -r scripts/requirements.txt

# ---------------------------------------------------------------- validation

validate: validate-frontmatter validate-json validate-policy validate-links ## Run every validator (what CI runs)

validate-frontmatter: ## YAML frontmatter + JSON Schema conformance
	$(PY) scripts/validate/validate_frontmatter.py

validate-json: ## metadata/*.json against schemas/
	$(PY) scripts/validate/validate_json.py

validate-links: ## Internal links + anchors (add EXTERNAL=1 for network checks)
ifeq ($(EXTERNAL),1)
	$(PY) scripts/validate/validate_links.py --internal --external
else
	$(PY) scripts/validate/validate_links.py --internal
endif

validate-policy: ## Secrets, collection ethics, license policy, hallucination firewall
	$(PY) scripts/validate/validate_policy.py

dedupe: ## Near-duplicate detection across the knowledge base
	$(PY) scripts/deduplicate/dedupe.py --report

stale: ## Freshness report: what has expired and must be re-verified
	$(PY) scripts/update/check_staleness.py --json metadata/staleness.json

# ---------------------------------------------------------------- refresh

refresh: refresh-github refresh-papers ## Re-verify GitHub + arXiv sources (needs network)

refresh-github: ## Re-verify every repository against the GitHub API
	GITHUB_TOKEN=$(TOKEN) $(PY) scripts/update/fetch_github_metadata.py --workers 8

resolve-seeds: ## Resolve seed slugs that 404 (renamed / moved)
	GITHUB_TOKEN=$(TOKEN) $(PY) scripts/update/resolve_failed_seeds.py

refresh-papers: ## Verify research papers against arXiv
	$(PY) scripts/crawl/verify_arxiv_papers.py

urls: ## Reachability check for every external URL
	$(PY) scripts/crawl/verify_urls.py --report metadata/url-report.json

# ---------------------------------------------------------------- generation

score: ## Re-score authored content (skills, knowledge, patterns, agents)
	$(PY) scripts/score/score_skills.py

registries: ## Extract metadata/*.json from authored frontmatter
	$(PY) scripts/generate-index/extract_registries.py

cards: ## Generate repository cards from metadata/repositories.json
	$(PY) scripts/generate-index/generate_repository_cards.py

index: ## Build metadata/index.json + indexes/*.md
	$(PY) scripts/generate-index/build_index.py

stats: ## Refresh the README statistics block
	$(PY) scripts/generate-index/update_readme_stats.py

rebuild: score registries cards index stats ## Regenerate every derived artifact in order

audit: validate dedupe stale ## Full audit: validation + duplicates + staleness

ci: validate ## CI entrypoint (links checked separately with retries)

clean: ## Remove caches and generated reports (never removes authored content)
	rm -rf .cache metadata/staleness.json metadata/url-report.json metadata/duplicates.json
	find . -name '__pycache__' -type d -prune -exec rm -rf {} +
