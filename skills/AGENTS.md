# AGENTS.md — `skills/`

Rules for any agent adding, editing or reviewing a skill in this directory. These override nothing in
the root [`AGENTS.md`](../AGENTS.md); they specialise it.

## What a skill is

A skill is a **reusable procedure with stated boundaries** — what it is for, when it must not be used,
what makes it fail, and how you would know. It is not documentation, not a tutorial, and not a prompt.
If the content has no procedure and no boundaries, it belongs in `knowledge/` or `prompts/`.

## Layout

```text
skills/
  <kebab-name>/
    SKILL.md              required — the skill itself
    tests/
      cases.md            required — GIVEN/WHEN/THEN/FAIL IF cases
    references/           optional — material too long for the body
    examples/             optional — worked before/after records
```

The directory name, the `name` frontmatter field and the `id` must agree.

## Hard rules

1. **Frontmatter is validated against `schemas/skill.schema.json` with `additionalProperties: false`.**
   An unknown field fails CI. Required: `name`, `version`, `description`, `category`, `status`,
   `confidence`, `source_type`, `updated`, `tags`.
2. **The body has a token budget of 2500, warning above 3375.** This is a hard constraint, not a
   style preference: a skill that does not fit is a skill an agent will not load in full, and the
   part that gets dropped is usually the boundaries. Move material to `references/` instead of
   raising the budget.
3. **Every skill has `tests/cases.md`.** Cases are derived from the skill's own purpose, exclusions,
   failure modes and anti-patterns — never from a generic template. A case that would pass for any
   skill is not a case. The `tests:` count in frontmatter must match the file.
4. **`category` must be a value from the schema enum.** Do not invent a category to fit a skill;
   either the skill fits an existing category or it does not belong here.
5. **Exclusions are mandatory content.** A skill that does not say when *not* to use it will be
   applied to the wrong problem. `not_for` or an equivalent body section is not optional.
6. **No apostrophes inside single-quoted YAML strings** in generator scripts — this has caused
   repeated `SyntaxError` failures during authoring. Use double quotes or rephrase.

## Prohibited

- Copying an external README, blog post or documentation page into a skill body. Summarise and cite;
  respect the source license. See the root policy on redistribution.
- Citing a repository by star count as evidence of quality. Stars are an adoption signal, not a
  correctness signal, and the scoring model exists precisely because conflating them is wrong.
- Adding a skill for a capability that already exists under a different name. Run
  `scripts/deduplicate/dedupe.py` before adding, and check `indexes/skills.md`.
- Marking `confidence: high` with no `sources[]`. Either cite or downgrade — this is the single most
  common validation warning in the corpus and it is always a real problem, never a false positive.
- Writing a skill whose procedure is "use your judgement". Judgement is what the boundaries encode;
  the procedure must be executable.

## Adding a skill

```bash
# 1. check for an existing skill covering the ground
grep -ril "<topic>" skills/*/SKILL.md
python3 scripts/deduplicate/dedupe.py

# 2. author SKILL.md and tests/cases.md
# 3. validate
python3 scripts/validate/validate_frontmatter.py
python3 scripts/score/score_skills.py

# 4. regenerate indexes and README stats
python3 scripts/generate-index/extract_registries.py
python3 scripts/generate-index/build_index.py
python3 scripts/generate-index/update_readme_stats.py

# 5. validate links, then commit
python3 scripts/validate/validate_links.py --internal
```

`make validate` runs steps 3 and 5 together. Do not commit with errors; warnings need a decision
recorded in the PR description.

## Reviewing a skill

Check in this order, because the later checks are wasted if an earlier one fails:

1. Does it have a procedure an agent could follow without further information?
2. Are the exclusions specific enough to prevent misapplication?
3. Is it inside the token budget, and if not, what was moved to `references/`?
4. Do the test cases fail for the right reasons — would a plausible-but-wrong application of this
   skill be caught?
5. Is every claim graded, and does `confidence` match the evidence actually cited?
6. Does it duplicate an existing skill?

## References

- [`../AGENTS.md`](../AGENTS.md) — the repository-wide operating contract
- [`../CONTRIBUTING.md`](../CONTRIBUTING.md) — the contribution workflow and PR expectations
- [`../schemas/skill.schema.json`](../schemas/skill.schema.json) — the validated shape
- [`skills/skill-curation/SKILL.md`](skill-curation/SKILL.md) — how skills are written, reviewed and retired
- [`../indexes/skills.md`](../indexes/skills.md) — the generated skill index
- [`../scripts/score/score_skills.py`](../scripts/score/score_skills.py) — the content scorer
