# Contributing

This repository is consumed by machines as well as humans, so contribution rules are
stricter than a typical docs repo. **A contribution that cannot be validated will not
be merged.**

---

## The quality gate

A new resource becomes `curated` only after **all** of these hold:

```text
□ valid source          URL resolves; repository/paper actually exists
□ license verified      SPDX id recorded, or explicitly flagged as missing
□ metadata complete     every required frontmatter field filled
□ quality scored        scored by scripts/score/*, not by hand
□ duplicate checked     scripts/deduplicate/dedupe.py reports no overlap above threshold
□ security checked      no secrets, no private reasoning traces, no unsafe MCP permissions
□ category assigned     one of the enumerated domains
□ confidence stated     very-high | high | medium | low | unverified | conflicting
□ claim_type stated     fact | recommendation | experiment | opinion | hypothesis | unknown
```

Failing any box ⇒ the contribution goes to [`experimental/`](experimental/), not to core.

---

## Submission types

| I want to add… | Use this template | Lands in |
|---|---|---|
| A GitHub repository | `resource-submission.yml` | `scripts/update/seeds.json` → generated card |
| An MCP server | `resource-submission.yml` (kind: mcp) | `knowledge/mcp/registry/*.md` + `metadata/tools.json` |
| A skill | `skill-submission.yml` | `skills/<name>/` with `tests/` |
| A research finding | `research-submission.yml` | `sources/` + `research-archive/YYYY/MM/` |
| A tool / dataset / benchmark | `resource-submission.yml` | `datasets/` or `evaluations/` |
| A correction | `correction.yml` | inline fix + `CHANGELOG.md` |
| A staleness report | `staleness-report.yml` | re-verification run |

---

## Adding a GitHub repository

Do **not** hand-write stars, dates, license or archive status.

```bash
# 1. add the seed
python3 - <<'EOF'
import json
p = "scripts/update/seeds.json"
d = json.load(open(p))
d["seeds"].append({
    "slug": "owner/name",
    "category": "agent-frameworks",     # see schemas/repository.schema.json for the enum
    "tier": "candidate",                # seed|core|reference|candidate|status-check
    "tags": ["agent", "python"],
    # "repo_kind": "research-artifact"  # only if it is a paper artifact / benchmark / catalog
})
json.dump(d, open(p, "w"), indent=2, ensure_ascii=False)
EOF

# 2. verify against the live API
GITHUB_TOKEN=*** python3 scripts/update/fetch_github_metadata.py --slug owner/name

# 3. inspect what the API actually said
python3 -c "import json;r=json.load(open('metadata/fetch-report.json'));print(json.dumps(r,indent=2)[:2000])"

# 4. add curated judgement
$EDITOR scripts/update/curation.json

# 5. regenerate derived artifacts
make cards index validate
```

If the slug 404s, run `scripts/update/resolve_failed_seeds.py`. It searches GitHub and
records candidates — it never silently substitutes one. Pick consciously.

---

## Adding a skill

```text
skills/<name>/
├── SKILL.md          required sections, see AGENTS.md §7
├── references/       deep material (loaded on demand)
├── examples/         real input → output pairs
├── checklists/       short verification lists
└── tests/
    ├── README.md     how to run + how to record results
    └── test-00N.md   GIVEN / WHEN / THEN / FAIL IF
```

Minimum viable skill:

```text
□ ≥3 test cases, each with an objective FAIL IF condition
□ a "When NOT to Use" section with at least two real exclusions
□ at least one cited external source with verified_at
□ declared requires: [] dependencies
□ body ≤ 2,500 tokens
```

A skill with no test cases is filed under `experimental/` with `status: experimental`.

---

## Adding a research finding

```text
1. Cite the primary source (publisher/minting authority), not a summary of a summary.
2. Record verified_at, license, and the verification method you used.
3. Separate FACT from RECOMMENDATION in the body text.
4. If two sources disagree, use the conflict format from
   knowledge/research/source-conflict-case-study.md — do not pick a winner silently.
5. If you cannot reach a primary source, put the item in
   metadata/pending-paper-candidates.json, not in sources/.
```

---

## AI-generated contributions

Allowed and encouraged, but they follow a pipeline:

```text
AI GENERATED → EXPERIMENTAL → HUMAN REVIEW → TEST → EVIDENCE → VALIDATED → CURATED
```

Requirements:

```yaml
provenance:
  content_class: derived        # or original
  generated_by: "<model + date>"
  human_reviewed: false         # must become true before promotion
```

- Mark model-produced assertions `claim_type: opinion` or `hypothesis` unless a source supports them.
- Never present generated text as `confidence: high`.
- Promotion to `curated` requires a human reviewer named in `provenance.reviewed_by`.

---

## Things that will get a PR closed

```text
✗ Copying an entire external README instead of summarising + linking
✗ Vendoring code from a repository with no detected license
✗ Adding leaked, extracted or reverse-engineered system prompts
✗ Adding private chain-of-thought, credentials, tokens, session data or personal data
✗ Hand-editing metadata/*.json or indexes/*.md
✗ Writing stars/dates/archived status by hand
✗ Adding an uncited "best X" list
✗ Promoting experimental content to core without evidence and a named human reviewer
✗ Duplicating guidance that already exists elsewhere instead of linking to it
```

---

## Commit & PR conventions

```text
feat(skills): add ai-slop-detection rewrite phase
fix(metadata): correct status classification for research artifacts
docs(knowledge): document context-compression tradeoffs
chore(ci): add freshness gate threshold
```

Before requesting review:

```bash
make validate && make index && git diff --stat metadata/ indexes/
```

Generated diffs are expected when you re-verify; unexplained ones are not.

---

## Recognition

Contributors are recorded in [`CHANGELOG.md`](CHANGELOG.md) per release and in the
`provenance.reviewed_by` field of the records they validated.
