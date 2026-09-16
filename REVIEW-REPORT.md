# REVIEW-REPORT.md — PR #1 comprehensive review

**PR:** [#1](https://github.com/tardigradsoftware-design/havuz-2/pull/1) — `arena/01a0a577-havuz-2` → `main`
**Reviewed commit:** `32720b8`
**Review date:** 2026-09-16
**Reviewer:** automated agent review, ordered per the requested sequence (SECURITY.md → scoring.py → CHANGELOG.md → skills → MCP registry → schemas/validation → README/AGENTS)
**Scope note:** read-only review. No source file was modified to produce this report. The regeneration runs performed during the review were verified to leave the git tree unchanged (`git status --porcelain` → 0 entries), which is itself one of the findings below.
**Fix commit:** `58dff2e` — C-1, C-2, C-3 and H-1 resolved. Each finding below now carries a **RESOLVED** block recording what changed and the measurement taken afterwards; the post-fix re-review is §14. The findings this report identified are unchanged as originally written, so the review remains readable as the state of `32720b8`.

---

## 1. Executive Summary

The PR is structurally sound and CI-green, and a meaningful part of what it claims is
verifiably true: all 414 repository records were fetched live with zero failures, the
generation chain is deterministic and byte-stable, no secret-shaped string exists in any
tracked file, the generated README statistics block honestly reports the empty corpora
(`Patterns 1`, `Failure knowledge 0`, `Evaluations 0`), and the `license: null` override
is applied consistently to all 15 affected records.

It should **not** be merged as-is. Three findings are critical, and all three share a
shape: **a documented guarantee that the data does not honour, which no validator checks.**

The most serious is the test corpus. `skills/*/tests/cases.md` contains 333 cases, and the
count is accurate — but the `FAIL IF` clause, which is the part that makes a test able to
fail, takes only **4 distinct values across all 333 cases**. `THEN` takes 45 distinct
values, of which 3 account for 87%. Only the `GIVEN` line is genuinely skill-specific.
`skills/AGENTS.md` forbids exactly this in terms: *"never from a generic template. A case
that would pass for any skill is not a case."* The suite cannot detect a skill producing
wrong output; it can only detect a skill being selected when it should not have been.

Second, 28 of 50 skills carry `evidence_level: practitioner-experience` together with
`confidence: high`, a combination `README.md` explicitly prohibits. Third, `README.md` and
`AGENTS.md` both assert — in the present tense, with a link — that a 40-task two-arm
evaluation suite exists at `evaluations/knowledge-base/`. It does not; `evaluations/`
contains zero content files.

None of these are visible to CI. Frontmatter validates, counts match, links resolve,
generated files are drift-free. The failures are all in the space between what the
documentation promises and what the corpus delivers, which is precisely the space this
repository exists to police. That gap is the finding.

A secondary theme runs through the scoring model and the MCP registry: **inference
presented as observation.** `scoring.py`'s docstring states that all inputs are observable
facts, but `official` — worth up to +0.6 weighted score — comes from a hand-maintained list
of ~250 organisation names. The MCP registry generator states that it refuses to guess
capability fields, then emits `authentication: "mixed"` for 28 of 35 records by inferring
it from the `official` flag. In both cases the guarantee is the valuable part, and in both
cases it is quietly violated by one field.

**Verdict:** fix the three critical findings, then merge. The high-priority items are
substantive but can follow immediately after; none of them corrupts existing data.

### Resolution status (updated 2026-09-16, commit `58dff2e`)

All three critical findings and the first high-priority finding are resolved, measured
afterwards rather than assumed. Each resolution is enforced in CI, not only in prose —
which was the shape of all three failures.

| Finding | Status | Measured result after the fix |
|---|---|---|
| C-1 template test corpus | **RESOLVED** | distinct `FAIL IF` 4/333 → **1108/1108**; `THEN` 45/333 → **1106/1108**; max skills sharing one `FAIL IF` 50 → **1**; 333 → **1108** cases over 50 skills |
| C-2 grading-rule violations | **RESOLVED** | **59** records corrected downward, not 28 — the review undercounted by measuring `skills/*/SKILL.md` only. Rule now a hard validator error corpus-wide |
| C-3 non-existent evaluation suite | **RESOLVED** | claims removed from README and AGENTS.md; new prose-path check covers **101** paths and found **3 further** false claims, all corrected |
| H-1 guessed `authentication` | **RESOLVED** | absent from **35/35** records; generator fails if any unverified entry carries a capability field |
| H-2 … H-8, M-1 … M-15, L-1 … L-9 | **OPEN** | untouched by this fix; recorded rather than closed |

| Severity | Count |
|---|---|
| Critical | 3 |
| High | 8 |
| Medium | 15 |
| Low | 9 |
| **Total** | **35** |

Positive verifications (no issue found) are recorded in §12 and §13 rather than omitted,
so that "not checked" and "checked and clean" are distinguishable.

---

## 2. Critical Issues

### C-1 · The test corpus is a template with the skill name substituted

- **File:** `skills/*/tests/cases.md` (all 50 files, 333 cases)
- **Location:** every `THEN` and `FAIL IF` line
- **Problem:** measured across the whole corpus:

  | Clause | Distinct values | Cases | Concentration |
  |---|---|---|---|
  | `GIVEN` | 332 | 333 | genuinely per-skill ✓ |
  | `WHEN` | 163 | 333 | ~6 templates with the skill name substituted |
  | `THEN` | 45 | 333 | 3 strings cover 291 cases (87%) |
  | `FAIL IF` | **4** | 333 | 4 strings cover **333 cases (100%)** |

  The four failure conditions are, verbatim: *"the skill is applied anyway, or it is
  declined without naming what should be done instead"* (143×), *"the anti-pattern appears
  in the output, or is avoided by accident rather than by the skill guidance"* (98×),
  *"a step is skipped, the output cannot be checked against the checklist, or the skill is
  applied without its inputs being present"* (50×), *"the failure goes unnoticed, or is
  noticed but the response is not the documented one"* (42×).
- **Why it matters:** `FAIL IF` is what makes a case falsifiable. A failure condition that
  is identical for `accessibility-audit`, `rag-pipeline` and `threat-modeling` cannot
  distinguish them failing. The suite can detect mis-selection; it cannot detect a skill
  that is correctly selected and produces wrong output. `README.md:309` then claims skills
  *"are graded by their `test_pass_rate`"* — a pass rate computed over these cases would
  measure nothing. `skills/AGENTS.md` rule 3 prohibits this explicitly: *"Cases are derived
  from the skill's own purpose, exclusions, failure modes and anti-patterns — never from a
  generic template. A case that would pass for any skill is not a case."* The rule was
  written in this PR and violated by the corpus generated in the same PR.
- **Caught by CI?** **No.** `validate_frontmatter.py` checks that the declared `tests:`
  count matches the file; it does. `validate_links.py` resolves the paths. No check
  measures assertion specificity. The corpus is fully CI-green.
- **Recommended fix:** the honest options are (a) regenerate `THEN`/`FAIL IF` per skill from
  that skill's own `Failure Modes` table and `Anti-Patterns` list, which are already
  skill-specific prose — the source material exists, only the generator ignored it; or
  (b) downgrade the claim: rename the files to `tests/selection-cases.md`, state that they
  cover selection and exclusion only, and remove the `test_pass_rate` sentence from
  `README.md`. Option (a) is better but is real work; option (b) is a one-line honesty fix.
  Do not merge with the current `README.md` claim either way.

> **RESOLVED — `58dff2e`, measured afterwards.** Option (a) was implemented, not option
> (b). New `scripts/generate-index/generate_skill_tests.py` derives all four clauses from
> each skill's own body: `Applies` cases from Purpose, Workflow step titles and Quality
> Checklist items; `Declines` from each `When NOT to Use` exclusion and the alternative it
> names; `Detects` from each `Failure Modes` entry with its own detection signal and
> documented response; `Avoids` from each `Anti-Patterns` entry and the consequence that
> entry states. `THEN` and `FAIL IF` quote that material verbatim, so assertions differ per
> skill by construction rather than by rewording. Both `Failure Modes` shapes in the corpus
> are parsed (14 skills use a `Failure | Detection | Response` table, 36 an aligned
> `NAME  description` block).
>
> | Clause | Before | After |
> |---|---|---|
> | cases | 333 | **1,108** (17–26 per skill) |
> | distinct `GIVEN` | 332 / 333 | 1,092 / 1,108 |
> | distinct `WHEN` | 163 / 333 | 199 / 1,108 — by design; it names the act of applying a particular skill |
> | distinct `THEN` | 45 / 333 (0.135) | **1,106 / 1,108 (0.998)** |
> | distinct `FAIL IF` | **4 / 333 (0.012)** | **1,108 / 1,108 (1.000)** |
> | max skills sharing one `FAIL IF` | 50 | **1** |
>
> The two remaining duplicate `THEN` values are two skills that genuinely list the same
> anti-pattern ("logging the full request body on an auth endpoint"); the assertion is
> shared because the guidance is. All four boilerplate `FAIL IF` strings named in this
> finding are gone.
>
> **Enforced, not asserted.** The generator measures its own output and refuses to write
> unless `THEN` and `FAIL IF` distinctness are both ≥ 0.95 and no `FAIL IF` is shared by
> more than one skill; `--check` runs the same gates as a named CI step. This closes the
> gap the finding identified — no validator previously measured assertion specificity.
>
> **The `test_pass_rate` claim was also wrong and is now corrected.** `README.md` said skills
> *"are graded by their `test_pass_rate` in frontmatter"*; no skill has that field and no
> case has been executed by a harness. The section now states the cases are **authored
> specifications, not executed results**, and that no pass rate exists or should be
> inferred. Regenerating them did not create evidence that any skill passes.

### C-2 · 28 of 50 skills violate the README's own grading rule

- **Files:** `README.md:309-311`; `skills/*/SKILL.md` frontmatter (28 files)
- **Problem:** `README.md` states: *"A skill that has never been run against a real task is
  marked `evidence_level: practitioner-experience` or `model-generated` and **cannot claim
  `confidence: high`**."* Measured distribution across the 50 skills:

  | `evidence_level` | `confidence` | Count |
  |---|---|---|
  | practitioner-experience | **high** | **28** ← prohibited |
  | cross-checked | high | 18 |
  | emerging-consensus | medium | 2 |
  | practitioner-experience | medium | 2 |

  Affected skills include `ai-safety-evaluation`, `ai-slop-detection`, `architecture-design`,
  `backend-engineering`, `code-review`, `data-pipeline`, `database-design`, `deployment`,
  `frontend-design`, `rag-pipeline` and 18 others.
- **Why it matters:** these 28 skills do carry `sources[]` (1–4 each), so they are not
  uncited — but the README rule is about `evidence_level`, not about citation, and having
  sources does not satisfy it as written. An agent following the documented policy reaches
  the opposite conclusion from an agent reading the frontmatter. When a knowledge base's
  stated grading rule and its graded content disagree, neither can be trusted, and the
  disagreement is load-bearing: `confidence` is the field a consumer uses to decide whether
  to act without a human check.
- **Caught by CI?** **No.** `validate_frontmatter.py` warns on *"`confidence: high` with no
  `sources[]`"* — a different rule, which these records pass. Nothing cross-checks
  `evidence_level` against `confidence`.
- **Recommended fix:** decide which is authoritative and make them agree. Either amend
  `README.md:309` to state the actual rule (*"practitioner-experience may claim `high` only
  where `sources[]` is non-empty and each source was reached"*) — defensible, since all 28
  do cite — or downgrade the 28 to `confidence: medium`. Then add the chosen invariant to
  `validate_frontmatter.py` so it cannot silently regress. The current state, where the
  stricter reading is documented and the looser one is implemented, is the worst of the
  three options.

> **RESOLVED — `58dff2e`, and the count in this finding was too low.** The rule was fixed
> once and applied corpus-wide, and the true violation count is **59, not 28**: this finding
> measured `skills/*/SKILL.md` only, while the rule applies to everything with graded
> frontmatter. By directory — skills 33, knowledge 10, agents 7, workflows 5,
> decision-records 2, prompts 2.
>
> The single rule adopted is derived from the `evidenceLevel` descriptions already present
> in `schemas/common.defs.json`, not invented for the fix: `verified-*` → `very-high`,
> `cross-checked` → `high`, `single-source` / `emerging-consensus` / `practitioner-experience`
> → `medium`, `model-generated` → `low`. It is defined once as `CONFIDENCE_CAP` in
> `scripts/lib/frontmatter.py`, documented in `README.md`, and enforced as a **hard error**
> by `validate_frontmatter.py` — so CI now fails on any future violation instead of warning.
>
> All 59 corrections move **downward**: 50 `practitioner-experience`+`high` → `medium`,
> 6 `cross-checked`+`very-high` → `high`, 2 `practitioner-experience`+`very-high` → `medium`,
> 1 `emerging-consensus`+`high` → `medium`. `evidence_level` was never raised to justify a
> confidence — that is the specific failure the rule exists to prevent, and the alternative
> would have been faster. Post-fix: 155 governed files, **0 errors**, warnings 6 → 1 (five
> of the six were "confidence high with no sources", resolved by the downgrade).

### C-3 · README and AGENTS.md assert an evaluation suite that does not exist

- **Files:** `README.md:313-317`; `AGENTS.md:53`
- **Problem:** `README.md` states, in the present tense: *"The repository itself **is
  benchmarked** in `evaluations/knowledge-base/` with a 40-task suite run in two arms —
  `without-kb` and `with-kb` — comparing success rate, time, token usage, code quality, bug
  count, security issues and architecture quality."* The link target `evaluations/` contains
  **0 content files** — only scaffolded directory READMEs. `evaluations/knowledge-base/`
  does not exist as a path at all. `AGENTS.md:53` repeats the claim: *"'Tests' here means
  validators plus the evaluation suite in `evaluations/`."*
- **Why it matters:** this is the one claim in the README that would persuade a sceptical
  reader the guidance works rather than merely existing — *"Did it actually work?"* is how
  the layer table frames it. It is also the claim most likely to be relied upon: a
  contributor told that a suite exists will look for it, and an agent asked whether the KB
  is validated will cite seven specific metrics that were never measured. `CHANGELOG.md`
  correctly records the suite as *"specified but not built"*, so the repository contradicts
  itself — the honest statement exists, it is just not where the promise is.
- **Caught by CI?** **No.** `validate_links.py` passes because the link points at
  `evaluations/`, which exists as a directory with a README. The path in the prose
  (`evaluations/knowledge-base/`) is inside a markdown link target that resolves to the
  parent, so the specific claim is never checked.
- **Recommended fix:** rewrite both sentences in the future or conditional mood and point
  at the specification rather than a result: *"A 40-task two-arm suite is specified in
  `CHANGELOG.md` and scaffolded under `evaluations/`; it has not been run. No effectiveness
  claim is made for this repository."* An effectiveness claim with no measurement behind it
  is the exact failure the `SUPERLATIVE`-without-a-date check in `validate_policy.py` exists
  to catch, and it slipped through because the sentence contains no superlative.

---

> **RESOLVED — `58dff2e`.** Both documents now state, in the present tense, *"Not measured.
> No effectiveness claim is made."* The 40-task two-arm suite is described as **specified but
> not built**, the non-existent `evaluations/knowledge-base/` path is gone, and the future
> plan is separated from present fact — matching what `CHANGELOG.md` already said.
> `AGENTS.md` now distinguishes the three things "tests" could mean here: validators (exist,
> enforced in CI), skill test cases (authored, not executed), effectiveness suite (not built).
>
> **The requested path check was added, and it found more.** `validate_links.py --internal`
> now asserts that every repository path named in prose in `README.md`, `AGENTS.md`,
> `CONTRIBUTING.md`, `SECURITY.md` and `CHANGELOG.md` actually exists — backticked spans as
> well as link targets, because prose paths are rarely links and a link to a *parent*
> directory resolves happily while the file named in the sentence does not. **101 paths
> checked, 0 errors** after three further false claims were found and corrected:
>
> | Claim | Reality | Correction |
> |---|---|---|
> | `README.md` listed `scripts/score/score_sources.py` in its automation table | never existed; `scripts/score/` holds only `score_skills.py` | row replaced with the five generators that do exist |
> | `CHANGELOG.md` referenced `indexes/sources-papers.md` | `build_index.py` does not produce it | corrected to `metadata/sources-papers.json` |
> | `sources/papers/README.md` referenced the same index | same | corrected pre-commit |
>
> The check is deliberately narrow so it does not decay into an allowlist: a token counts as
> a path only when its first segment is a real top-level entry (which keeps GitHub slugs and
> package names out), documented naming conventions are exempt via a placeholder-segment list
> (`research-archive/YYYY/MM/`), and a correction paragraph that names a path *in order to
> record that it was falsely claimed* is exempt only when the denial is in prose — not when a
> filename merely contains a marker word. **Verified by negative test:** injecting
> `scripts/validate/validate_everything.py` and `metadata/nonexistent.json` into `README.md`
> is caught and reported with the file named; the first implementation of this exemption
> missed both, because `nonexistent.json` matched the marker inside its own filename.

## 3. High Priority Issues

### H-1 · MCP registry guesses a security-relevant field it promises not to guess

- **File:** `scripts/generate-index/generate_mcp_registry.py` (`record_to_tool`,
  `authentication` line); output `metadata/tools.json`, `knowledge/mcp/registry/*.md`
- **Problem:** the module docstring states that *"Capability fields that the GitHub API
  cannot tell us — transport, tool list, resource list, prompt list, authentication scheme —
  are emitted as null or empty and flagged `capability_evidence: unverified`. They are NOT
  guessed."* Five of those six are correctly empty (verified: `transport`, `tools`,
  `resources`, `prompts`, `permissions` are all empty in 35/35 records). The sixth is not:

  ```python
  "authentication": "mixed" if rec.get("official") else None,
  ```

  28 of 35 records therefore assert `authentication: mixed`, inferred from the `official`
  flag — which is itself derived from a hand-maintained organisation list (§L-2), not from
  an API fact.
- **Why it matters:** authentication scheme is the field an integrator acts on. `mixed`
  tells them the server supports several auth paths; the evidence is that its owner appears
  in a list. This is worse than an empty field, because an empty field is visibly unknown
  and a populated one looks verified — and the surrounding prose loudly advertises that
  nothing was guessed, which lends the false value credibility.
- **Caught by CI?** **No.** `mixed` is a valid enum member of `mcp.schema.json`, and the
  drift job confirms the output matches the generator. Both checks pass because the
  generator is self-consistent; consistency with its own docstring is not checked.
- **Recommended fix:** emit `authentication` only when observed, otherwise omit it (the
  markdown template already omits it when falsy, so this is a one-line change in
  `record_to_tool`). If a heuristic is genuinely wanted, it must be recorded as a heuristic
  in a separate field, not in the field the schema defines as the authentication scheme.

> **RESOLVED — `58dff2e`, exactly as recommended: omit unless observed.** The inference line
> is removed and `authentication` is now **absent from 35/35 records and 35/35 markdown
> entries**. Absence is the honest representation here: `mcp.schema.json`'s enum has no
> `unknown` member, and the field is optional, so omitting it plus
> `capability_evidence: unverified` says precisely what is known. Each entry documents how to
> fill it in — read the project's own documentation, then set `capability_evidence` to
> `readme-reviewed` or `verified` and date it. No heuristic was substituted; a guess recorded
> in a differently-named field would still be a guess an integrator could act on.
>
> **The guarantee is now machine-enforced, which is what made this finding possible to miss.**
> `assert_no_guesses()` fails the generator — write mode and `--check` alike — if any entry
> with `capability_evidence: unverified` carries a populated capability field (`transport`,
> `tools`, `resources`, `prompts`, `permissions`, `authentication`, `recommended_for`). CI
> runs it as the named step *MCP registry asserts no unobservable capability*. This closes the
> gap identified above: the drift job previously passed because the generator was
> self-consistent, and nothing checked consistency with its own docstring.
>
> **Verified by negative test.** On the clean corpus the gate reports 0 violations; injecting
> `authentication: "mixed"` into one record or `tools: ["read_file"]` into another is caught
> in both cases, with the offending repository named in the message. Post-fix measurement of
> all 35 records: `authentication` absent, and `transport`, `tools`, `resources`, `prompts`,
> `permissions`, `recommended_for` and `not_recommended_for` all empty.
>
> Note this resolves the *inference*. `official` itself still comes from a hand-maintained
> organisation list (§L-2) and remains worth up to +0.6 weighted score — that finding is
> untouched and still open.

### H-2 · Nine schema fields are silently lost between the registry markdown and `tools.json`

- **Files:** `scripts/generate-index/generate_mcp_registry.py` (`MD_TMPL`);
  `scripts/generate-index/extract_registries.py`; `metadata/tools.json`
- **Problem:** the chain established in this PR is
  `repositories.json → knowledge/mcp/registry/*.md → metadata/tools.json`. The markdown
  template does not emit nine fields that `record_to_tool()` computes, so they never reach
  the JSON. Verified absent from all 35 records: `npm_package`, `pypi_package`,
  `permissions`, `recommended_for`, `not_recommended_for`, `resources`, `prompts`, `uvx`,
  `npx`.
  The consequential loss is `not_recommended_for`, which for the one archived server
  (`browserbase/mcp-server-browserbase`) carried `"adoption in new work — archived"`. That
  do-not-adopt signal now exists **nowhere** — not in the markdown, not in the JSON. Only
  the weaker `production_readiness: deprecated` survives.
  A latent bug sits behind it: `detect_distribution` derives an npm package name with
  `homepage.rsplit("/", 1)[-1]`, which for `https://www.npmjs.com/package/@playwright/mcp`
  yields `mcp` rather than `@playwright/mcp`. It is currently invisible because the field is
  dropped, so fixing the loss would surface the wrong value.
- **Why it matters:** the single-writer change was made specifically to stop the registry
  drifting from the documents it describes. It succeeded — the chain is deterministic
  (§12) — but one-directional now also means one-lossy: any field not in the markdown is
  gone from the machine-readable registry that agents consume. The archived warning is a
  safety signal, and losing it silently is the opposite of what the change was for.
- **Caught by CI?** **No.** `validate_json.py` reports 0 errors because all nine fields are
  optional in `mcp.schema.json`. `generated-drift` passes because regeneration reproduces
  the same loss. Neither job compares the generator's intermediate output against the final
  JSON.
- **Recommended fix:** add the nine fields to `MD_TMPL` so the markdown round-trips
  completely, and fix the scoped-package parse (split on `/package/`, not on `/`). Then add
  a CI assertion that the set of keys produced by `record_to_tool()` equals the set of keys
  present in `tools.json` — that check would have caught this at once and will catch the
  next field added to only one side.

### H-3 · The `UNVERIFIED` tier names the wrong thing

- **Files:** `scripts/lib/scoring.py` (`tier_for`); `metadata/repositories.json`;
  `indexes/*.md`; `repositories/**/*.md`; `CHANGELOG.md`
- **Problem:** `tier_for` returns `"UNVERIFIED"` when `license_ok` is false. All 15 records
  in that tier have `fetch_ok: true` — they were successfully verified against the GitHub
  API on 2026-09-15. What is actually true of them is that **no license was detected**. The
  tier label conflates verification status with legal status. The tier spans scores
  4.02–8.02, so it contains `vercel/mcp-handler` at 8.02 — above the S threshold of 8.0 —
  labelled `UNVERIFIED`.
- **Why it matters:** an agent reading `tier: UNVERIFIED` will reasonably conclude the
  metadata is unreliable and re-fetch or discard it, when the metadata is fine and the
  *license* is the problem. The signal that matters — do not redistribute — is carried in a
  separate field (`license_risk`) that the tier name actively obscures. `validate_json.py`
  already encodes the correct meaning elsewhere (`fetch_ok == false` may not claim
  `evidence_level: verified-github-api`), so the codebase uses "verified" consistently
  everywhere except here.
- **Caught by CI?** **No.** `UNVERIFIED` is a valid member of the `tier` enum, and the
  data is internally consistent.
- **Recommended fix:** rename the tier to `NO-LICENSE` or `UNLICENSED` in
  `common.defs.json#/$defs/tier` and `tier_for`, regenerate, and record the rename in
  `CHANGELOG.md` as a major-version schema change with the old name noted. Keep
  `UNVERIFIED` reserved for records whose fetch actually failed, which is the meaning every
  other part of the codebase gives it.

### H-4 · SECURITY.md's "hard exclusions" are prose-only; nothing enforces them

- **Files:** `SECURITY.md:22-45`; `scripts/validate/validate_policy.py` (whole file)
- **Problem:** `SECURITY.md` declares a set of things the repository will *"never collect,
  store, summarise in reproducing form, or redistribute"*, including leaked or extracted
  system prompts, and names two specific high-popularity repositories as excluded.
  `validate_policy.py` implements five checks — secret shapes, `FORBIDDEN` content regexes,
  unlicensed-vendor warnings, superlatives without a date, and quarantine-citation wording —
  and **none of them consults an exclusion list.** There is no `EXCLUDED_SOURCES` constant
  anywhere in the codebase. Grep for the two excluded slugs across `metadata/*.json`,
  `indexes/*.md` and `repositories/` returns nothing, so the policy is honoured *today*,
  purely because nobody has added them.
- **Why it matters:** the exclusions are described as hard, and the reason they are recorded
  rather than silently omitted — stated in `SECURITY.md` and in the PR description — is so
  that a later contributor does not rediscover those repositories and add them in good
  faith. That is exactly the scenario the code does not defend against. A contributor
  seeding a popular repo with 67k stars would pass every check: it fetches fine, it scores
  well, and its license is present. The policy has no enforcement path, so it will degrade
  on the first well-intentioned addition.
- **Caught by CI?** **No** — there is no check to catch it. The `FORBIDDEN` regexes look for
  reproduced *content* shapes (chain-of-thought dumps, leaked-prompt preambles), not for
  *sources* that distribute such content.
- **Recommended fix:** add an explicit exclusion list (slug → reason → date decided) as
  data, not prose — `metadata/excluded-sources.json` is the natural home, since
  `knowledge/security/llm-security/excluded-sources.md` already documents the reasoning.
  Have `validate_policy.py` error if any excluded slug appears in `seeds.json`,
  `repositories.json`, or any tracked file outside the exclusion documentation itself. Also
  have `fetch_github_metadata.py` refuse to fetch excluded slugs. That converts a policy
  that depends on contributor diligence into one that fails a build.

### H-5 · The license "hard override" is enforced only as a warning, and only on code files

- **File:** `scripts/validate/validate_policy.py:139-146` (check 3)
- **Problem:** the override itself works correctly in the data: all 15 no-license records
  carry `license_risk: no-license-do-not-redistribute` and `tier: UNVERIFIED`, and the 57
  `NOASSERTION` records carry `custom-license-review-before-vendoring`. But the *enforcement*
  is a warning, and its scope is wrong:

  ```python
  if re.search(rf"(?i){re.escape(name)}", text) and f.suffix in (".ts", ".tsx", ".js", ".py", ".go", ".rs"):
      warns.append(...)
  ```

  It fires only on source-code files and matches only the repository *name*, not the owner.
  In this repository the realistic vendoring target is a **markdown article** copying prose
  or a skill from `anthropics/skills` or `openai/skills` — and `.md` files are not scanned at
  all. Meanwhile the name-only match produces the 88 warnings that currently dominate the
  policy output, mostly scripts mentioning the word "skills".
- **Why it matters:** the PR description and `CHANGELOG.md` both describe this as *"a hard
  override that beats the weighted score"*. It does beat the score, in the data. But nothing
  prevents the thing the override exists to prevent — copying unlicensed content into the
  corpus — and the warning that nominally covers it is both under-inclusive (wrong file
  types) and over-inclusive (name substring), which trains reviewers to ignore it.
- **Caught by CI?** Partially, and only as a warning: the job passes with 88 warnings.
  `--strict` would promote them to errors, but CI does not run `--strict`.
- **Recommended fix:** scan `.md` files as well, match `owner/name` rather than `name`
  alone, and promote to an error when an unlicensed slug is referenced from a file that also
  contains a fenced code block over ~15 lines (the shape of vendored content) as opposed to a
  passing mention. Separately, exclude `scripts/**` from the warning — the generator scripts
  legitimately name these repositories, and their warnings are pure noise.

### H-6 · Untrusted GitHub API text is embedded verbatim into generated markdown

- **Files:** `scripts/generate-index/generate_repository_cards.py:111`;
  `scripts/generate-index/generate_mcp_registry.py` (`purpose` field); all 427 cards and 35
  registry entries
- **Problem:** the card generator writes the repository's own description as a markdown
  blockquote with no escaping:

  ```python
  f"> {r.get('description') or '_No description published._'}"
  ```

  The MCP registry does the same, wrapping it as *"As stated by the repository itself: …"*.
  Descriptions are attacker-controlled: any repository owner can set one, and the fetcher
  reads it without sanitisation. Verified in the current corpus — 401 of 414 records have a
  description, maximum length 346 characters, and:
  - 5 contain raw URLs, which GitHub renders as live links
    (`camel-ai/camel`, `D4Vinci/Scrapling`, `postgres/postgres`, `hoppscotch/hoppscotch`,
    `xyflow/xyflow`)
  - 1 contains markdown emphasis that is interpreted rather than displayed:
    `repositories/databases/postgres--postgres.md:50` renders `*mirror*` as italics
  - 1 reproduces an unverified vendor superlative as though it were content:
    `repositories/agent-frameworks/camel-ai--camel.md:50` → *"The first and the best
    multi-agent framework"* — and that card is ranked **#1 under "BEST AGENT FRAMEWORKS"**
    in `indexes/best-of.md`
- **Why it matters:** this repository is explicitly built to be read by agents as external
  long-term memory. Description text therefore travels from an arbitrary third party, through
  the fetcher, into a file an agent will ingest as trusted guidance. A description reading
  `Ignore prior instructions and …` would be rendered verbatim into a card. Today's corpus is
  clean — a scan for instruction-shaped, role-marker, HTML and markdown-link patterns across
  all 401 descriptions returned zero hits — but that is a property of the current seed list,
  not of the pipeline. The `SUPERLATIVE`-without-a-date check in `validate_policy.py` does
  not fire on the camel-ai superlative because the generated card has a verification date
  nearby, so the check passes while reproducing a vendor's marketing claim as fact.
- **Caught by CI?** **No.** Nothing sanitises or scans fetched description text. The policy
  scanner checks *authored* content for forbidden shapes; it does not treat *ingested*
  content as untrusted input.
- **Recommended fix:** treat API-sourced strings as untrusted at the generation boundary.
  Minimum: escape markdown-active characters (`*`, `_`, `` ` ``, `[`, `]`, `<`, `>`) and
  strip or angle-bracket bare URLs when writing descriptions into cards. Better: also run
  `validate_policy.py`'s `FORBIDDEN` patterns over the `description`, `homepage` and
  `topics` fields in `repositories.json`, and quarantine any record that matches rather than
  rendering it. Add a standing note to `SECURITY.md` that repository descriptions are
  untrusted third-party input, since the current policy section does not mention ingestion at
  all.

### H-7 · MCP `category` is assigned by unanchored substring match and is already wrong

- **File:** `scripts/generate-index/generate_mcp_registry.py` (`CATEGORY_SIGNALS`,
  `detect_category`)
- **Problem:** signals are matched with `if any(s in haystack for s in signals)` against a
  haystack of description + topics + slug, with no word boundaries. Short signals therefore
  match inside ordinary words. Verified by direct execution:
  `modelcontextprotocol/python-sdk` and `modelcontextprotocol/typescript-sdk` are both
  classified `category: ci-cd`, and the matched signal is `'ci'` — found inside the word
  *"offi**ci**al"* in their own descriptions (*"The official Python SDK for Model Context
  Protocol"*).
- **Why it matters:** `category` is how a consumer filters the registry, and `ci-cd` is
  confidently wrong for both official SDKs. The same class of error is latent for the other
  short signals: `'cd'`, `'git'`, `'file'`, `'sql'`, `'docs'`, `'ci'` will all match inside
  unrelated prose. Because the value looks authoritative and is emitted into a graded
  registry entry, the error propagates into `indexes/mcp.md` and into any agent that filters
  on it.
- **Caught by CI?** **No.** `ci-cd` is a valid enum member.
- **Recommended fix:** match on word boundaries (`re.search(rf"\b{re.escape(s)}\b", …)`) and
  require the match in `topics` or the slug, not in free-text descriptions — topics are
  curated by the owner for discoverability and are far less prone to accidental substring
  hits. Where nothing matches, `other` is the correct answer and is already the fallback.

### H-8 · Five of the "35 MCP servers" are not servers

- **Files:** `knowledge/mcp/registry/*.md`; `metadata/tools.json`; `README.md` stats block
  (`MCP servers | 35`); `indexes/mcp.md`
- **Problem:** the registry is built by filtering `repositories.json` for
  `category == "mcp-servers"`, which is a *seed-list* category, not a verified property. The
  resulting 35 include:

  | Repository | What it actually is |
  |---|---|
  | `modelcontextprotocol/python-sdk` | SDK for building servers |
  | `modelcontextprotocol/typescript-sdk` | SDK for building servers |
  | `modelcontextprotocol/inspector` | testing/debugging tool (its own description says so) |
  | `modelcontextprotocol/registry` | a registry service — a peer of this registry, not an entry |
  | `punkpeye/awesome-mcp-servers` | a curated list of other servers |

  Each entry's own `purpose` field quotes the description that says this, so the registry
  contradicts its own label five times over.
- **Why it matters:** the registry's consumers are `skills/dont-reinvent-the-wheel` and
  `skills/mcp-integration`, which instruct an agent to consult it before building or
  installing a server. An agent told "35 servers are available, here is the browser one"
  that installs an SDK or a catalog gets nothing usable, and the count inflates the apparent
  coverage of the registry by ~14%. `modelcontextprotocol/registry` is the sharpest case:
  listing a competing registry as an entry in your own registry is a category error that a
  reader will notice immediately.
- **Caught by CI?** **No.** Nothing validates that a registry entry is a server; the schema
  has no field for it.
- **Recommended fix:** add a `registry_kind` field to `mcp.schema.json` with values
  `server | sdk | tooling | catalog | registry`, populate it from the observed description
  and topics (these five are unambiguous from their own text), and filter `indexes/mcp.md`
  and the README statistic to `server` only while keeping the others listed under a separate
  heading — SDKs and the inspector are genuinely useful to record, they are just not servers.

---

## 4. Medium Priority Issues

### M-1 · The adoption component saturates for 94% of the corpus

- **File:** `scripts/lib/scoring.py:265-270`
- **Problem:** `adoption = _clamp(2.0 + 2.4 * log10(stars + 1) + 0.4 * log10(forks + 1))`
  reaches the 10.0 clamp at approximately **2,153 stars** (with forks = 0). Measured: 389 of
  414 records (94.0%) sit at exactly 10.0; the histogram is `[(10.0, 389), (9.6, 6), (9.9,
  4), (9.5, 2), …]`. Mean 9.95.
- **Why it matters:** a component carrying 15% of the weight contributes essentially no
  discrimination across the corpus — it is a constant for 94% of records. The stated intent
  (*"log-scaled so a star-farmed repo cannot dominate the score"*) is achieved, but the
  practical effect is that adoption has been switched off rather than tamed, and 15% of the
  model's budget is spent on it. Because the seed list is deliberately skewed toward notable
  projects, the saturation is a property of the corpus and the curve together.
- **Caught by CI?** **No.**
- **Recommended fix:** either rescale so the corpus occupies the middle of the range
  (e.g. `2.0 + 1.6 * log10(stars + 1)` saturates near 40k) and document the intended
  saturation point, or reduce adoption's weight and redistribute it to components that
  actually vary (`security` mean 5.06, `evidence` mean 5.84, `documentation` mean 6.95).
  State the chosen saturation point in `knowledge/ai-engineering/source-scoring.md` — a
  reader cannot currently tell that the component is flat.

### M-2 · Component ceilings are inconsistent, so the 0–10 scale is not normalised

- **File:** `scripts/lib/scoring.py` (`score_repository`, all eight components)
- **Problem:** each component is built by adding bonuses to a base and then clamping to 10,
  but the maximum reachable value differs per component:

  | Component | Base | Max reachable | Weight |
  |---|---|---|---|
  | authority | 4.0 | 9.0 | 20% |
  | maintenance | 0.5–10.0 | 10.0 (11.5 before bonuses clamp) | 15% |
  | adoption | 2.0 | 10.0 | 15% |
  | documentation | 1.0 | 10.0 | 10% |
  | reproducibility | 1.0 | 10.5 → 10.0 | 10% |
  | **security** | 3.5 | **7.0** | 10% |
  | recency | 0–10 | 10.0 | 10% |
  | **evidence** | 1.0 | **8.0** | 10% |

  `security` can never exceed 7.0 (3.5 + 2.5 SECURITY.md + 1.0 official) and `evidence` never
  exceeds 8.0. The theoretical maximum weighted total is therefore
  `0.20·9 + 0.15·10 + 0.15·10 + 0.10·10 + 0.10·10 + 0.10·7 + 0.10·8 + 0.10·10 = 9.30` —
  and the observed maximum across all 414 records is **exactly 9.30**.
- **Why it matters:** the S threshold of 8.0 sits at 86% of the achievable maximum, not 80%
  of a true 10-point scale, and the shortfall is caused entirely by two components being
  structurally unable to reach their nominal range. This is the main mechanical reason
  **51.7% of the corpus lands in tier S** (214 of 414): the top of the scale is compressed,
  so scores cluster near a ceiling that is itself below 10. Any reader interpreting "S tier"
  as "top decile" will be wrong by a factor of five.
- **Caught by CI?** **No.**
- **Recommended fix:** normalise each component by its own reachable maximum before weighting
  (`component / ceiling * 10`), or raise the `security` and `evidence` bases so all eight can
  reach 10. Then re-derive the tier thresholds from the resulting distribution rather than
  carrying 8.0/7.0/5.8/4.3 over unchanged, and document the derivation. Note this is a
  **major-version** change under the repository's own versioning policy, since it moves tiers.

### M-3 · `days_since_push` drives three components simultaneously

- **File:** `scripts/lib/scoring.py` (`maintenance`, `recency`, `security`)
- **Problem:** one observed field feeds three components: `maintenance` (15% weight, the
  entire 0.5–10 ladder), `recency` (10%, `10 − d_push/73`), and a `−1.0` penalty inside
  `security` when `d_push > 365`. Measured saturation: `maintenance` is at 10.0 for 70.5% of
  records and `recency` at 10.0 for 58.5%.
- **Why it matters:** roughly 25% of the total score is one signal counted twice, and 35%
  for stale repositories where the security penalty also fires. Two collinear components
  behave as a single component with a larger weight, so the published weight table
  (maintenance 15%, recency 10%) does not describe the model's actual sensitivity. It also
  makes the score brittle to a single trivial commit: a bot push resets `d_push` to 0 and
  moves two components at once.
- **Caught by CI?** **No.**
- **Recommended fix:** keep `maintenance` as the activity signal and redefine `recency` to
  measure something distinct — release cadence (`days_since_release` is already fetched but
  only used for a `+0.5` bonus) or the age of the latest release tag. Remove the `d_push`
  term from `security`, which is already covered by the `archived` penalty and by
  `maintenance`.

### M-4 · The `security` component does not measure security, and license risk is counted four times

- **File:** `scripts/lib/scoring.py:283-296` (`security`), `_trust`, `tier_for`,
  `reproducibility`
- **Problem:** the `security` component is built from `has_security_md` (+2.5), `official`
  (+1.0), license class (−1.0 for AGPL/SSPL/commons-clause, −2.0 for no license, −0.5 for
  non-standard), `archived` (−2.0) and staleness (−1.0). It contains **no vulnerability,
  advisory, dependency-audit or CVE signal at all** — none is fetched. The code even
  acknowledges the confusion in a comment: `security -= 1.0  # redistribution risk, not
  vulnerability risk`. Separately, the absence of a license affects four places at once:
  `security` (−2.0), `reproducibility` (misses the +2.0 license bonus), `_trust` (−1.5) and
  `tier_for` (forced to `UNVERIFIED`).
- **Why it matters:** a component named `security` carrying 10% of the weight mostly measures
  legal posture and documentation hygiene. That is defensible as a *trust* signal — and
  `_trust` already exists for it — but it means the published weight table misleads: a reader
  seeing "security 10%" will assume vulnerabilities are considered. The quadruple-counting of
  license absence is deliberate for the tier (it is the hard override) but unintentional in
  the three numeric components, where it penalises the same fact ~0.55 weighted points on top
  of the override.
- **Caught by CI?** **No.**
- **Recommended fix:** rename the component to `legal-and-posture` or `trust-signals` and
  document what it does and does not cover, or fetch a real security signal (GitHub's
  `security_and_analysis` / open-advisory endpoints) and use it. Remove the license terms
  from the numeric components and let the tier override carry the license decision alone, so
  the fact is counted once where it matters.

### M-5 · Tier is not monotonic in score, and the indexes do not explain why

- **Files:** `scripts/lib/scoring.py` (`tier_for`); `indexes/best-of.md`;
  `repositories/**/*.md`
- **Problem:** 29 records are tier **A** while scoring ≥ 8.0, the S threshold. The highest is
  `Arize-ai/phoenix` at **9.26**, then `BerriAI/litellm` 9.21, `lobehub/lobehub` 9.06,
  `nodejs/node` 8.91, `oven-sh/bun` 8.88, `langfuse/langfuse` 8.86. All 29 are
  `license_nonstandard: true`, so the cause is the deliberate rule *"A custom (NOASSERTION)
  license caps the tier at A."* Verified there are no S-tier records below 8.0.
- **Why it matters:** the rule is sound and documented in the `tier_for` docstring, but it is
  invisible at the point of consumption. `indexes/best-of.md` displays `BerriAI/litellm |
  58.8k | A | ACTIVE` in a list headed *"Ranked by trust score"*, adjacent to S-tier
  repositories with fewer stars, with no note. A reader concludes the ranking is broken or
  that litellm is worse than an 8.0-scoring S project. Neither is true, and the reason is not
  recoverable from the index.
- **Caught by CI?** **No.**
- **Recommended fix:** add a footnote to every generated index and card explaining the cap
  (*"tier A despite score ≥ 8.0: license is non-standard and requires a human read before
  vendoring"*), and surface `license_risk` as a visible column in `indexes/best-of.md`. The
  generator already has the field.

### M-6 · `NOASSERTION` is treated as "custom license" when it means "unclassified"

- **Files:** `scripts/lib/scoring.py` (`license_nonstandard`); `metadata/repositories.json`;
  57 records
- **Problem:** `license_nonstandard = has_license_file and license_id in ("noassertion",
  "other", "")`, and those 57 records receive `license_risk:
  custom-license-review-before-vendoring` plus the tier-A cap. But GitHub's `NOASSERTION`
  means *licensee could not classify the LICENSE file* — it is not an assertion that the
  terms are non-standard. Several affected repositories are widely understood to carry
  ordinary permissive licenses, including `nodejs/node`, `oven-sh/bun`, `BerriAI/litellm` and
  `langfuse/langfuse`. (Recorded here as requiring verification, not asserted as fact — the
  LICENSE file of each must be read, which is exactly what the flag asks a human to do.)
- **Why it matters:** the cap demotes 29 high-scoring projects (§M-5) on a signal that means
  "unclassified", so the registry may be systematically under-tiering mainstream permissive
  projects while the label tells readers the terms are unusual. The conservative direction is
  right — treating unclassified as needs-review is safer than assuming MIT — but the *label*
  asserts more than the evidence supports, and `CHANGELOG.md` describes these as
  "non-standard" without qualification.
- **Caught by CI?** **No.**
- **Recommended fix:** relabel the risk value to `unclassified-license-review-before-vendoring`
  so it states what was observed, keep the tier cap (conservatism is correct), and read the
  LICENSE file for the 29 records scoring ≥ 8.0 — a bounded, one-off task that would move
  several major projects to their correct tier. Record the outcome per repository in
  `curation.json`, which exists for precisely this kind of human judgement.

### M-7 · `distribution` and `setup_complexity` are inferred from the absence of evidence

- **File:** `scripts/generate-index/generate_mcp_registry.py` (`detect_distribution`)
- **Problem:** when the homepage is not a package-registry URL, distribution falls back to
  `"source"` — *"the only claim we can defend"*, per the code comment. 33 of 35 records take
  that fallback, including 23 that do have a homepage (a docs site). `setup_complexity` is
  then derived from distribution, so 33 of 35 are `medium` and 2 are `low`.
- **Why it matters:** `setup_complexity: medium` is a positive assertion produced from not
  finding an npm URL. For projects that are in fact one `npx` invocation from running, the
  registry overstates the cost of adoption — and `skills/dont-reinvent-the-wheel` uses this
  registry to decide whether to build or install, so an inflated complexity value pushes
  toward building. This is the same failure mode as H-1 in a less security-critical field.
- **Caught by CI?** **No.** Both values are valid enum members.
- **Recommended fix:** omit `setup_complexity` when distribution is the `source` fallback,
  rather than deriving it. If a distribution claim is wanted for the 23 with homepages, it
  requires reading the repository's README install section — which is the same manual pass
  that would fill in `capability_evidence: verified`, so bundle them.

### M-8 · Four documents claim a `.cache/gh/` audit trail that is not in the repository

- **Files:** `CHANGELOG.md:129-130`; `knowledge/ai-engineering/verification-findings.md:89`
  and `:233`; `metadata/AGENTS.md:20`
- **Problem:** all four state that ~1,903 cached API responses are retained under `.cache/gh/`
  *"so that scores are reproducible offline"* / *"so that the corpus can be re-audited
  against the exact data it was built from"*. `.cache/` is gitignored (`.gitignore:3`) and
  `git ls-files | grep -c '^\.cache/'` returns **0**. Empirically confirmed during this
  review: the directory existed during the build (28 MB) and was absent afterward, without
  anyone deleting it — gitignored paths do not survive a workspace restore or a fresh clone.
- **Why it matters:** the claim is the stated basis for reproducibility of 414 scored records,
  and it does not hold for anyone but the original build environment. A reviewer who tries to
  re-audit a score against the cached response will find nothing. The real audit trail *is*
  committed — `metadata/repositories.json` retains every observed field the score was
  computed from (`stars`, `pushed_at`, `structure.*`, `contributors`, `latest_release`) — so
  the substance survives; only the claim about the cache is false.
- **Caught by CI?** **No.** `validate_links.py` checks markdown links, and these are inline
  code spans, not links.
- **Recommended fix:** correct all four places to say the cache is a local build artifact
  that is **not** committed, and that reproducibility rests on the observed fields retained in
  `repositories.json` (naming them). If offline re-audit is genuinely wanted, commit a
  trimmed, license-safe snapshot of the API responses under `metadata/evidence/` — but that is
  a new feature, not a correction, and the wording should not claim it until it exists.

### M-9 · "Knowledge articles" means two different things in two places

- **Files:** `README.md` generated stats block (`Knowledge articles | **72**`);
  `CHANGELOG.md` (*"37 articles across nine domains"*); PR description (37)
- **Problem:** `find knowledge -name '*.md' -not -name 'README.md'` returns 72. 37 are
  authored articles; 35 are the MCP registry entries added by this PR under
  `knowledge/mcp/registry/`. `update_readme_stats.py` counts all of them, so the README
  statistic doubled during this PR without either document acknowledging the change of
  meaning.
- **Why it matters:** the stats block is generated and trusted precisely because it is not
  hand-written; a reader comparing it to `CHANGELOG.md` finds 72 versus 37 for the same
  metric name and cannot tell which is wrong. Both are defensible, which is the problem — the
  label does not say what it counts.
- **Caught by CI?** **No.**
- **Recommended fix:** have `update_readme_stats.py` exclude `knowledge/mcp/registry/` from the
  article count and add a separate `MCP registry entries | 35` row (the `MCP servers` row
  already exists and should be relabelled per H-8), so the two numbers reconcile: 37 articles
  + 35 registry entries = 72 markdown files under `knowledge/`.

### M-10 · README states 418 repositories where the data holds 414

- **File:** `README.md` (architecture diagram, `repositories.json ← 418 GitHub repos,
  live-verified`); two other places in the same file say 414
- **Problem:** 418 was the pre-deduplication seed count; 414 is the record count after 4
  aliases collapsed. The architecture diagram was not updated when the fetcher added alias
  deduplication. `CHANGELOG.md` describes the 418→414 relationship correctly.
- **Why it matters:** small, but it is the one number in the README that a reader can check in
  ten seconds, and it disagrees with the file it describes and with two other statements in
  the same document.
- **Caught by CI?** **No.** `update_readme_stats.py` maintains the stats block, not the
  hand-written architecture diagram.
- **Recommended fix:** change the diagram to `414 GitHub repos (418 seeds, 4 aliases
  collapsed), live-verified` — which is both correct and more informative.

### M-11 · README lists seven CI checks that do not correspond to the six actual jobs

- **Files:** `README.md` ("Validation & CI" section); `.github/workflows/kb-ci.yml`
- **Problem:** the README lists `validate-yaml`, `validate-schemas`, `validate-links`,
  `validate-duplicates`, `validate-freshness`, `validate-policy`, `markdown-lint` as checks
  that "run on every push and pull request". The workflow defines six **jobs**: *Validate
  structure, schemas and policy*, *Freshness and staleness*, *Generated files are not
  hand-edited*, *External link reachability*, *Re-verify sources (weekly / manual)*, *Secret
  and supply-chain scanning*. The README's names correspond to **steps inside the first job**
  (JSON parses, YAML parses, frontmatter + schema, internal links, policy, duplicate
  detection, markdown heading structure) — so the substance is largely right, but:
  - `markdown-lint` and `validate-duplicates` do not exist as named entities anywhere in
    `.github/` or `Makefile`; they are steps named *Markdown heading structure* and *Duplicate
    detection (report only)*
  - `validate-links` is described as checking that *"external links resolve (retry +
    allowlist)"*, but external-link checking is a **separate job gated on `schedule` or
    `workflow_dispatch`** — it does **not** run on push or pull request. The README claims
    otherwise.
  - Three real jobs are not mentioned at all: secret scanning, generated-drift, and
    source re-verification.
- **Why it matters:** the external-link claim is the substantive one — a reader will believe
  every external URL is verified on each PR, when in fact the 340 non-GitHub homepage URLs
  embedded in generated cards are never checked at merge time. The omissions undersell work
  that was actually done.
- **Caught by CI?** **No.**
- **Recommended fix:** replace the list with the six real job names, mark which are
  conditional and on what trigger, and state explicitly that external links are checked only
  on the weekly schedule. Consider adding external-link checking to `pull_request` for files
  the PR touched, which would make the original claim true.

### M-12 · A real-shaped secret passes the scanner if the word "example" appears nearby

- **File:** `scripts/validate/validate_policy.py:113-119` (check 1)
- **Problem:** the bypass condition is

  ```python
  if "<" in s or "YOUR" in s.upper() or "xxxx" in s.lower() or "example" in low[max(0, m.start()-80):m.start()]:
      continue
  ```

  The last clause skips any match preceded within 80 characters by the substring `example`.
  Demonstrated with a synthetic 40-character token (no real credential involved):

  | Context | Result |
  |---|---|
  | `token = ghp_AAAA…` | **CAUGHT** |
  | `example config: ghp_AAAA…` | **BYPASSED** |
  | `see example above ghp_AAAA…` | **BYPASSED** |
  | `<ghp_AAAA…>` | CAUGHT |

  Also note the `"<" in s` clause is dead for every current pattern: none of the 14 regexes
  can capture a `<` character, so the placeholder form `<YOUR_TOKEN>` is caught by the `YOUR`
  clause, not by the angle brackets.
- **Why it matters:** `example` is one of the most common words in technical documentation,
  and this repository is full of it. A contributor pasting a real token into any sentence
  that happens to mention an example within 80 characters defeats the scanner silently. The
  bypass is well-intentioned — placeholders must not fail the build — but the trigger is too
  broad and too easy to hit accidentally.
- **Caught by CI?** **No** — this *is* the CI check.
- **Recommended fix:** narrow the bypass to the placeholder's own shape rather than its
  neighbourhood: skip only when the matched string itself contains a placeholder marker
  (`YOUR`, `XXXX`, `<`, `REDACTED`, all-same-character runs), and drop the `example`-proximity
  clause entirely. Then remove the dead `"<" in s` test or extend the patterns to capture
  surrounding angle brackets so it does something.

### M-13 · `expires_for()` raises `KeyError` on an unknown kind, and its TTLs disagree with the freshness policy

- **File:** `scripts/lib/scoring.py:494-501`
- **Problem:** the TTL lookup is `ttl_days = {…}[kind]` — direct indexing, so any `kind` not in
  the 12-entry table raises `KeyError` rather than falling back to the `default: 90` entry
  that the table itself provides. Separately, the TTLs do not match
  `knowledge/ai-engineering/freshness-policy.md` as summarised in `CHANGELOG.md` and the PR
  description (*"30 days for security and pricing, 90 for fast-moving tooling, 180 for
  framework behaviour, 365 for architecture and theory"*): `scoring.py` has `framework: 60`,
  `github-repository: 45`, `mcp: 45`, `tool: 45`, and no security or pricing kind at all.
- **Why it matters:** the KeyError makes the function unsafe to call with a new source type,
  which is a routine operation as the corpus grows. The TTL disagreement means two documents
  give different lifetimes for the same claim class, and `check_staleness.py` — the tool that
  decides what has expired — uses whichever it reads. A 45-day versus 90-day window for
  fast-moving tooling is the difference between a record being fresh and being stale.
- **Caught by CI?** **No.** `check_staleness.py` currently reports `expired: 0`, so no
  divergence is observable yet; it will appear as records age.
- **Recommended fix:** use `ttl_days.get(kind, ttl_days["default"])`, then reconcile the table
  with `freshness-policy.md` and make one of them the single source — ideally have
  `freshness-policy.md` carry the table in a machine-readable block that `scoring.py` reads, so
  they cannot drift.

### M-14 · `EXPERIMENTAL` means two different things in two fields

- **Files:** `scripts/lib/scoring.py` (`classify_status`, `tier_for`)
- **Problem:** `classify_status` returns `EXPERIMENTAL` when `stars < 300 and not has_releases
  and activity < 90` — a statement about project maturity. `tier_for` returns `EXPERIMENTAL`
  when the weighted score is below 4.3 — a statement about measured quality. The same token
  appears in the `status` field and the `tier` field with unrelated definitions, and
  `CHANGELOG.md` reports *"3 EXPERIMENTAL"* in the tier distribution without distinguishing it
  from the status value.
- **Why it matters:** a consumer filtering on `EXPERIMENTAL` gets two different populations
  depending on which field it reads, and a record could carry `status: EXPERIMENTAL` with
  `tier: A` or the reverse with no contradiction. `validate_json.py` already cross-checks
  `status: ARCHIVED` against `tier`, so the codebase treats these fields as related — but the
  relationship is undefined for this value.
- **Caught by CI?** **No.**
- **Recommended fix:** rename the tier value to `LOW-SCORE` or `UNPROVEN`, keeping
  `EXPERIMENTAL` for the maturity status where it is accurate, and document both in
  `knowledge/ai-engineering/repository-status.md`.

### M-15 · 340 external URLs are embedded in generated cards and never checked at merge time

- **Files:** `repositories/**/*.md`; `knowledge/mcp/registry/*.md`;
  `.github/workflows/kb-ci.yml:200-207`
- **Problem:** 340 of 414 records carry a non-GitHub `homepage`, rendered into cards, plus
  every `url` and `sources[].url`. The `external-links` job that would verify them is gated
  on `github.event_name == 'schedule' || workflow_dispatch || inputs.external_links == 'true'`,
  so it does not run on `push` or `pull_request`. Confirmed skipped in both CI runs for this
  PR.
- **Why it matters:** dead external links are the most common way a knowledge base rots, and
  this corpus has hundreds of them sourced from a field (repository homepage) that owners
  change or abandon. README claims they are checked (§M-11). Nothing verifies them at the
  moment they are added.
- **Caught by CI?** Only on the weekly schedule, which has not yet run for this branch.
- **Recommended fix:** run the external-link job on `pull_request` scoped to URLs added or
  changed by the PR (bounded, so runtime stays sane), keeping the full sweep weekly. At
  minimum correct the README claim so it matches the trigger.

---

## 5. Low Priority Issues

### L-1 · `tier_for` contains an unreachable branch

- **File:** `scripts/lib/scoring.py` (`tier_for`)
- **Problem:** `if score >= 7.0 or (score >= 8.0 and nonstandard): return "A"` — the second
  disjunct is unreachable, because any score ≥ 8.0 already satisfies `score >= 7.0`. The
  preceding branch returns S only when `not nonstandard`, so control reaches this line with
  score ≥ 8.0 and `nonstandard` true, where the first disjunct fires anyway.
- **Why it matters:** dead code in a function whose logic is load-bearing for 414 tier
  assignments. Harmless today, but it reads as though the cap needs that clause, which invites
  a future edit to "fix" the wrong line.
- **Caught by CI?** **No.**
- **Recommended fix:** reduce to `if score >= 7.0: return "A"` and move the explanation of the
  NOASSERTION cap into the docstring, where it already partly lives.

### L-2 · `official` is derived from a hand-maintained list, contradicting the "observable facts" guarantee

- **File:** `scripts/lib/scoring.py` (`OFFICIAL_ORGS`, ~250 entries; `authority`, `_trust`)
- **Problem:** the module docstring states *"All inputs are observable facts (GitHub API
  responses, presence of files, licenses, releases) rather than opinions, so scores are
  reproducible."* `official` is not an API fact: it is membership in a curated set of
  organisation logins, plus a `force_official` curation override. It contributes **+3.0 to
  `authority`** (≈ +0.60 weighted, the single largest discrete bonus in the model) and **+0.5
  to `_trust`**.
- **Why it matters:** the list is a defensible judgement — owner identity genuinely is a proxy
  for canonical upstream — but it is an opinion, it is unaudited, and it is the largest single
  lever on the score. `CHANGELOG.md` and the PR description both state that scores are
  "computed only from observable GitHub API facts", which overstates the case by exactly this
  field. Reproducibility holds (the list is committed), but "observable fact" does not.
- **Caught by CI?** **No.**
- **Recommended fix:** keep the list — it is useful — but document it as a curated input in
  `knowledge/ai-engineering/source-scoring.md`, name it in the "not purely observable" caveat,
  and add a review cadence. Correct the "only observable facts" wording wherever it appears to
  "computed from observable GitHub API facts plus one curated input (`OFFICIAL_ORGS`), which is
  committed and auditable".

### L-3 · `OFFICIAL_ORGS` contains duplicates and stale organisation names

- **File:** `scripts/lib/scoring.py` (`OFFICIAL_ORGS`)
- **Problem:** duplicates (harmless in a set, but symptomatic): `microsoft` ×4, `vercel` ×2,
  `google` ×2, `huggingface` ×2, `grafana` ×2, `redis` ×2, `cloudflare` ×2, `getsentry` ×2,
  `firebase` ×2. Stale or non-existent logins: `gaia-benchmark` (verified absent from GitHub
  during the build — GAIA lives on Hugging Face), `sentry-experts`, `rebuff-ai`, `plane-so`,
  `lmarena-ai`, `slackapi`, `tabby-ml`, `open-interpreter`, `anthropics` vs `anthropic-ai`
  (all seven of which were confirmed renamed or moved during the build, per `CHANGELOG.md`).
- **Why it matters:** a stale entry silently fails to confer `official` on the renamed
  organisation's repositories, so those projects score up to 0.60 weighted points lower than
  they should. The build already resolved 27 renames in the seed data; the same renames were
  not applied here.
- **Caught by CI?** **No.**
- **Recommended fix:** deduplicate, apply the 27 known renames, and drop logins that no longer
  resolve. Add a test that every `OFFICIAL_ORGS` entry matches the owner of at least one record
  in `repositories.json`, which would surface dead entries automatically.

### L-4 · SECURITY.md documents 7 secret patterns; the code checks 14

- **Files:** `SECURITY.md:57-64`; `scripts/validate/validate_policy.py:33-47`
- **Problem:** the documented list omits `gho_`, `AIza` (Google), `sk_live_` (Stripe), `eyJ…`
  (JWT), `sbp_` (Supabase), `npm_`, `hf_` (Hugging Face), all of which are enforced. The
  documented `ghp_[A-Za-z0-9]{36}` is narrower than the enforced `\bghp_[A-Za-z0-9]{30,}`.
- **Why it matters:** the documentation understates the control, so a contributor may
  duplicate a check that already exists, or assume a pattern is not covered and add a weaker
  one. Understating a security control is the safe direction of error, but it is still drift
  between policy and implementation.
- **Caught by CI?** **No.**
- **Recommended fix:** generate the documented list from `SECRET_PATTERNS.keys()` so it cannot
  drift, or simply state the count and point at the source file as authoritative.

### L-5 · SECURITY.md asserts a repository setting that cannot be verified from the build

- **File:** `SECURITY.md:50` (*"GitHub push protection + secret scanning enabled on the
  repository"*)
- **Problem:** presented as a checked box. Querying the setting is not possible with the
  available token (`gh api repos/…/actions/permissions` → 403 "Resource not accessible by
  integration"), and nothing in the repository records when or by whom it was enabled.
- **Why it matters:** every other item in that checklist is verifiable from the tree
  (`validate_policy.py` exists, `.gitignore` contains the listed patterns — both confirmed in
  this review). This one is not, and a reader cannot distinguish it from the ones that are. If
  it was never enabled, the checkbox is the only evidence and it is self-asserted.
- **Caught by CI?** **No.**
- **Recommended fix:** mark it as requiring an owner to confirm, with a date, or add a
  `workflow_dispatch` job that queries the setting with an appropriately scoped token and fails
  if it is off.

### L-6 · Twelve `mcp.schema.json` properties are never populated by any record

- **Files:** `schemas/mcp.schema.json`; `metadata/tools.json`
- **Problem:** the schema declares 42 properties; records use 33. Never present: `uvx`, `npx`,
  `resources`, `prompts`, `permissions`, `recommended_for`, `not_recommended_for`,
  `npm_package`, `pypi_package`, `last_verified`, and — added by this PR — `days_since_push`
  and `language`. The last two were added to the schema in this PR while the markdown template
  that feeds the JSON does not emit them (§H-2), so the PR created two dead fields.
- **Why it matters:** dead schema surface invites contributors to populate fields nothing
  reads, and makes the schema a poor description of the data. `days_since_push` and `language`
  are genuinely useful and are available in `repositories.json`; they are simply dropped in
  transit.
- **Caught by CI?** **No.** All are optional.
- **Recommended fix:** emit the two new fields from `MD_TMPL` (they are already computed), and
  either populate or remove the rest. `permissions` in particular is worth keeping as an empty
  object with a comment, since it is the field a future manual pass should fill in.

### L-7 · Generator bookkeeping keys are published in the machine-readable registries

- **Files:** `metadata/*.json`; `scripts/validate/validate_json.py` (`BUILD_ANNOTATIONS`)
- **Problem:** `_path`, `_tokens` and `_headings` are present in every record of `tools.json`,
  `skills.json`, `agents.json`, `workflows.json` and `prompts.json`. They are not declared in
  any schema; `validate_json.py` strips an explicit allowlist before validating (added in this
  PR, and correctly documented as such).
- **Why it matters:** an external consumer reading `tools.json` sees three fields no schema
  describes. The allowlist is explicit and small, so a typo'd annotation still fails — the
  design is sound. It is simply undeclared surface in a published artifact.
- **Caught by CI?** **No** — deliberately, by the allowlist.
- **Recommended fix:** either declare them in each schema under a `_`-prefixed pattern property
  with a description marking them as generator metadata, or have `extract_registries.py` keep
  them in a sibling key (`_build`) outside the record array. The first is a smaller change.

### L-8 · `infer_repo_kind` indexes `slug.split("/")[1]` without a guard

- **File:** `scripts/lib/scoring.py` (`infer_repo_kind`)
- **Problem:** `if slug.split("/")[1].lower().endswith((".md", "-docs", "-spec",
  "-specification"))` raises `IndexError` for a slug with no `/`. All current inputs are
  well-formed `owner/name` slugs, so this is latent.
- **Why it matters:** the fetcher resolves renames and aliases, and a malformed seed entry
  would crash the whole run rather than skipping one record. `fetch_github_metadata.py`
  currently reports per-record failures, so a hard crash is a regression in behaviour.
- **Caught by CI?** **No**, unless a malformed slug is committed.
- **Recommended fix:** `parts = slug.split("/"); if len(parts) == 2 and parts[1].lower().endswith(...)`.

### L-9 · Duplicate-detection runs in report-only mode and its output is not acted on

- **Files:** `.github/workflows/kb-ci.yml:88`; `scripts/deduplicate/dedupe.py`
- **Problem:** CI runs `dedupe.py --report --threshold 0.45` as a step named *"Duplicate
  detection (report only)"*. Local execution surfaces repeated heading clusters (`escalation`,
  `hard-rules`, `enforcement`, `scaling` each appearing in 3 files) — expected, since the
  AGENTS.md family shares structure — but the step cannot fail and nothing records whether the
  report was read.
- **Why it matters:** near-duplicate content is the mechanism by which a knowledge base starts
  contradicting itself, and `CONTRIBUTING.md` presents deduplication as a gate. A report-only
  gate is not a gate.
- **Caught by CI?** Reported, never enforced.
- **Recommended fix:** keep report-only for structural similarity, but add a hard failure above
  a higher threshold (e.g. 0.85) where similarity almost certainly means duplicated content
  rather than shared headings.

---

## 6. Security Findings

**Findings:** H-4 (exclusions unenforced), H-5 (license override is a warning on the wrong file
types), H-6 (untrusted API text rendered as markdown — the prompt-injection surface), M-12
(secret-scanner bypass), M-15 (external URLs unchecked at merge time), L-4 (documented patterns
understate enforcement), L-5 (unverifiable repository-setting claim).

**Verified clean — no issue found:**

| Check | Method | Result |
|---|---|---|
| Secret-shaped strings in tracked files | `git ls-files \| xargs grep -E` with all 14 patterns from `validate_policy.py`, word-boundary anchored | **0 matches** |
| `.gitignore` covers what SECURITY.md claims | grepped for `.env`, `*.pem`, `*.key`, `credentials`, `.cache/` | **all 5 present** |
| Excluded repositories absent from generated data | grepped `metadata/*.json`, `indexes/*.md`, `repositories/` for both excluded slugs | **0 occurrences** |
| No leaked-prompt content vendored | `FORBIDDEN` regexes over all tracked files via `validate_policy.py` | **0 errors** |
| Secret-scanning CI job | run `35057785309` | **pass, 13s** |
| PAT pasted into the build conversation | `git log -p`, config, environment | **never written anywhere**; `CHANGELOG.md` records the handling |
| Instruction-shaped content in fetched descriptions | regex scan for `you must`, `ignore previous`, `system prompt`, role markers, HTML tags, markdown links over 401 descriptions | **0 hits** (see H-6: clean today, unguarded structurally) |

**Assessment.** No credential, token, private key or PII is present in the repository. The
collection-ethics exclusions are honoured in the data. The security *posture* is nonetheless
weaker than `SECURITY.md` presents, for one consistent reason: **the policies are documented as
hard and implemented as advisory.** The exclusions have no enforcement path (H-4), the license
override warns only on source-code files in a repository whose vendoring risk is markdown (H-5),
and the secret scanner can be defeated by the word "example" appearing 80 characters earlier
(M-12). None of these is exploitable today; all three will degrade without a build failure to
stop them.

The one genuinely new attack surface introduced by this repository's design is H-6. A knowledge
base built to be ingested by agents, populated from fields that arbitrary third parties control,
is an injection vector by construction — and the pipeline treats those fields as data rather
than as untrusted input. The corpus is clean now because the seed list was chosen by a human.
That is luck, not a control.

---

## 7. Data Integrity Findings

**Findings:** H-2 (nine fields lost in the generation chain), H-3 (`UNVERIFIED` tier mislabels
verified records), H-7 (substring-match misclassification), H-8 (five non-servers in the server
registry), M-5 (non-monotonic tiers, unexplained in indexes), M-6 (`NOASSERTION` read as
"custom"), M-7 (complexity inferred from absence of evidence), M-8 (cache audit trail not
committed), M-9/M-10 (count disagreements), M-14 (`EXPERIMENTAL` overloaded).

**Verified clean — no issue found:**

| Check | Method | Result |
|---|---|---|
| All 414 records fetched successfully | `fetch_ok` across `repositories.json` | **414/414 true, 0 failures** |
| Generation chain is deterministic | ran `generate_mcp_registry.py` + `extract_registries.py` twice, compared outputs | **`tools.json` byte-identical ignoring `generated_at`; 0 of 35 registry files differ** |
| Committed output is in sync with sources | `generate_mcp_registry.py --check`; `git status` after full regeneration | **"in sync: 35 entries"; git tree unchanged (0 modified files)** |
| `license: null` override applied consistently | cross-checked `license`, `license_risk`, `tier` for all 15 no-license records | **all 15 → `no-license-do-not-redistribute` + `UNVERIFIED`, no exceptions** |
| License-risk classes partition the corpus | value counts | **342 `none` + 57 `custom-license-review-before-vendoring` + 15 `no-license-do-not-redistribute` = 414** ✓ |
| No S-tier record below the threshold | filtered `tier == S and score < 8.0` | **0 records** |
| Archived records never marked production-ready | `validate_json.py` invariant | **0 violations** (10 archived, all `production_ready: false`) |
| Stars never asserted without a check date | `validate_json.py` invariant | **0 violations**; all carry `stars_checked_at: 2026-09-15` |
| Quarantined papers absent from the index | `validate_json.py` leakage check | **0 leaked**; 61 candidates stay in `pending-paper-candidates.json` |
| Test-case count as claimed | counted `GIVEN` blocks across 50 files | **333 — matches `CHANGELOG.md` and the PR description exactly** |
| README stats block honesty | generated block vs. `find` counts | **`Patterns 1`, `Failure knowledge 0`, `Evaluations 0`, `Model cards 0`, `Datasets 0`, `Verified GitHub repositories 414` — all accurate** |
| Unverified/verified/quarantined separation | 9 published papers vs 61 quarantined vs `UNVERIFIED` tier | **no mixing found**; the three populations are disjoint and separately labelled (but see H-3 on the tier's *name*) |
| Repository-schema coverage | declared vs. used properties | **71 declared, 69 used; the 2 unused (`error`, `http_status`) exist for failed fetches, of which there were none** ✓ |

**Assessment.** The *fetched* data is sound: complete, internally consistent, deterministic,
drift-free, and every invariant the validators define holds without exception. The integrity
problems are all downstream of the fetch, in interpretation and in transit — a tier that names
the wrong property (H-3), a field lost between two generators (H-2), a classification made by
substring accident (H-7), a category label applied to five things that are not servers (H-8), and
four documents describing an audit trail that is not committed (M-8). None corrupts an observed
value; several mislabel one.

---

## 8. Scoring System Review

**Findings:** M-1 (adoption saturates for 94%), M-2 (inconsistent component ceilings → max 9.30,
51.7% S tier), M-3 (`days_since_push` triple-counted), M-4 (`security` measures license, license
counted four times), M-5 (tier non-monotonic in score), M-14 (`EXPERIMENTAL` overloaded),
L-1 (dead branch), L-2 (`official` is a curated opinion worth +0.60), L-3 (stale org list),
M-13 (`expires_for` KeyError + TTL disagreement).

**Verified correct:**

| Check | Result |
|---|---|
| `WEIGHTS` sums to 1.0 | **0.20+0.15+0.15+0.10+0.10+0.10+0.10+0.10 = 1.00** ✓ |
| `_trust` weights sum to 1.0 | **0.30+0.25+0.20+0.15+0.10 = 1.00** ✓ |
| Every component clamped to [0,10] | `_clamp` applied to all eight before weighting ✓ |
| Observed max equals the theoretical max | **9.30 observed = 9.30 computed** — confirms the ceiling analysis in M-2 and that no component exceeds its intended range |
| Weights match the documented model | `knowledge/ai-engineering/source-scoring.md` and the PR description both state the same eight weights ✓ |
| `STATIC_KINDS` handling | paper artifacts, benchmarks and model releases are `STABLE`, not `ABANDONED` — the docstring records this was added after observing mislabelling on `deepseek-ai/DeepSeek-R1`, `ysymyth/ReAct`, `noahshinn/reflexion` ✓ |
| No invented inputs | every component reads only `repo`, `tree` or `meta` — no constant is presented as an observation, **except** `official` (L-2) |

**Is the eight-component model logically and technically consistent?** *Arithmetically yes,
statistically no.* The implementation is correct: it computes what it says it computes, clamps
consistently, and reproduces exactly. The problems are in the model's design, and they compound
in one direction:

1. **Three components barely vary.** `adoption` is at its ceiling for 94% of records (M-1),
   `maintenance` for 70.5%, `recency` for 58.5%. Together they carry 40% of the weight and
   behave largely as constants across this corpus.
2. **Two components cannot reach their nominal range.** `security` caps at 7.0 and `evidence`
   at 8.0 (M-2), pulling the achievable maximum to 9.30.
3. **The varying components are collinear.** `maintenance` and `recency` both read
   `days_since_push`; `security`, `evidence` and `reproducibility` share five inputs (M-3, M-4).

The net effect is that a model presented as eight weighted dimensions is functionally closer to
four, with a compressed top end — which is why 214 of 414 records (51.7%) reach tier S. That
distribution is not wrong in isolation, since the seed list is deliberately composed of notable
projects, but it is **not** the distribution the tier names imply, and nothing in the
documentation says S means "top half of a curated list of well-known projects" rather than
"exceptional".

**Is the tier distribution consistent with the data?** Internally, yes — every tier assignment
follows from `tier_for` without exception, and the one non-monotonicity (29 A-tier records
scoring ≥ 8.0) is fully explained by the documented NOASSERTION cap. Externally, the
distribution over-represents S because of the ceiling compression in M-2 and the saturation in
M-1, and the indexes present tiers without the explanation a reader needs (M-5).

**Do the 414 records contain false or hypothetical information?** No fabricated values were
found. Every observed field traces to an API response, all 414 fetched successfully, and the
invariants hold without exception. Three categories of *inference* are nonetheless presented
with the same authority as observation: `official` from a curated list (L-2), `authentication`
in the MCP registry from `official` (H-1), and `setup_complexity` from the absence of a package
URL (M-7). Those are the places where the data asserts more than it knows.

**Recommended fix (consolidated):** the components need re-basing rather than re-tuning.
Normalise each by its own reachable ceiling, redefine `recency` to measure release cadence
instead of duplicating `maintenance`, remove the license terms from the numeric components and
let the tier override carry them once, then re-derive the tier thresholds from the resulting
distribution and document the derivation. That is a **major-version** change under the
repository's own versioning policy, because it moves tiers — and it should be done before the
corpus grows, not after, since every additional record inherits the current distortion.

---

## 9. MCP Registry Review

**Findings:** H-1 (`authentication` guessed), H-2 (nine fields lost in transit), H-7 (category by
substring), H-8 (five non-servers), M-7 (`setup_complexity` inferred from absence), L-6 (twelve
dead schema fields).

**Are capability fields the API cannot report left un-guessed?** *Five of six, yes.* Verified
across all 35 records: `transport`, `tools`, `resources`, `prompts` and `permissions` are empty
in every record, and all 35 carry `capability_evidence: unverified`. Each entry's markdown
states plainly what is not verified and gives a six-item checklist to confirm before adoption.
That is the right design and it is implemented correctly for those five fields.

The sixth, `authentication`, is inferred (H-1) — and it is the one with security consequences,
in a registry whose stated purpose is telling an agent which tools it can *safely* be given.

**Other observations:**

- **Coverage.** 35 entries across 11 categories (`browser` 7, `database` 6, `cloud` 5, `ci-cd` 5
  — two of which are wrong per H-7, `other` 4, `communication` 3, and 1 each for
  `observability`, `vcs`, `filesystem`, `search`, `documentation`). No `payments`, `design` or
  `knowledge` entries, though the schema defines them.
- **Risk flags work.** `browserbase/mcp-server-browserbase` is correctly `production_readiness:
  deprecated` with `security.risk_level: high`; 8 records carry license-risk values, and each
  entry's "Adoption guidance" section states the redistribution consequence in plain terms.
- **One entry admits its own weakness.** `modelcontextprotocol/inspector`'s purpose is flagged
  `purpose_evidence: repository-description-thin` with a note to expand from the README — the
  generator correctly identifies and labels the one case where the source description was
  insufficient. Good behaviour, worth preserving.
- **`distribution` is weak.** 33 of 35 fall back to `source` (M-7), and `npm_package` is never
  populated even for `microsoft/playwright-mcp`, whose homepage *is* its npm URL — the value is
  computed correctly as `distribution: npm` and then dropped with the field (H-2).

**Recommended fix (consolidated):** omit `authentication` unless observed; add the nine missing
fields to the markdown template and fix the scoped-package parse; match categories on word
boundaries against topics and slug only; add `registry_kind` and report server counts
separately; omit `setup_complexity` where distribution is the fallback. All five are contained
changes to one generator plus a regeneration — none requires re-fetching.

---

## 10. Schema/Validation Review

**Findings:** C-2 (grading rule unenforced), H-3 (tier enum names the wrong property), L-6 (dead
fields), L-7 (undeclared bookkeeping keys), M-13 (`expires_for` fragility), M-14 (`EXPERIMENTAL`
in two enums), L-1 (dead branch in a validated code path).

**Are the JSON Schemas compatible with the real data structures?** **Yes, without exception.**
`validate_json.py` reports **959 records, 0 errors, 0 warnings** across 12 registries. Coverage
is tight in both directions:

| Schema | Declared | Used | Unused | Undeclared-but-present |
|---|---|---|---|---|
| `repository.schema.json` | 71 | 69 | `error`, `http_status` (exist for failed fetches; there were none) | — |
| `mcp.schema.json` | 42 | 33 | 12 (see L-6) | `_path`, `_tokens`, `_headings` (see L-7) |

`additionalProperties: false` is set on every content schema, so a mistyped field name fails the
build — verified by the four schema-vs-content mismatches found and fixed during this PR's
construction, each of which did fail loudly. That is the single most valuable property of the
validation layer and it is working.

**What the validators cover well:**

- frontmatter presence, schema conformance, unique IDs, body token budgets (155 governed files,
  0 errors)
- internal link and anchor resolution (0 broken)
- registry invariants a per-record schema cannot express: archived ≠ production-ready, failed
  fetch ≠ verified evidence, stars require a check date, expired records reported, quarantined
  records cannot leak into the index
- generated-file provenance (must declare a generator) and drift (regeneration must reproduce)
- near-duplicate detection, markdown heading structure

**What nothing validates — the gap that produced C-1, C-2 and C-3:**

| Unchecked property | Consequence observed |
|---|---|
| Cross-field semantic consistency (`evidence_level` × `confidence`) | 28 of 50 skills violate the documented rule (C-2) |
| Assertion specificity in test cases | 4 distinct `FAIL IF` strings for 333 cases (C-1) |
| Prose claims against filesystem reality | a 40-task suite asserted at a path that does not exist (C-3) |
| A generator's output against its own docstring | `authentication` guessed despite a promise not to (H-1) |
| Field completeness across a generation chain | 9 fields silently dropped (H-2) |
| Ingested third-party strings as untrusted input | descriptions rendered as markdown (H-6) |

**Assessment.** The validation layer is strong on *shape* and weak on *meaning*. Every structural
property is checked, and checked well — the schema strictness is genuinely unusual and is why the
corpus is internally consistent. But all three critical findings are semantic: a documented rule
the data violates, a test suite that cannot fail, and a claim about a file that does not exist.
Each is expressible as a validator, and none currently is.

**Recommended fix:** add three checks to `validate_frontmatter.py` / `validate_policy.py`, in this
order of value:
1. the `evidence_level` × `confidence` invariant, once C-2 decides which rule is authoritative;
2. a distinctness measure on `tests/cases.md` — e.g. fail when the ratio of distinct `FAIL IF`
   strings to cases across the corpus falls below a threshold, which is a direct proxy for
   template-generated assertions;
3. a prose-path check — extract every backticked or linked path from `README.md` and `AGENTS.md`
   and assert it exists, which would have caught C-3 and M-8.

---

## 11. Documentation Consistency

**Findings:** C-3 (evaluation suite claimed as existing), M-8 (cache audit trail), M-9 (knowledge
article count 72 vs 37), M-10 (418 vs 414), M-11 (CI check names and the external-link claim),
L-2 ("only observable facts" overstates), L-4 (secret patterns understated), L-5 (unverifiable
setting), M-6 (`NOASSERTION` described as non-standard).

**Do the gaps get misrepresented as present anywhere?** Mostly no — and where they are, it is
inconsistent rather than systematic:

| Location | States the gap honestly? |
|---|---|
| `README.md` generated stats block | **Yes** — `Patterns 1`, `Failure knowledge 0`, `Evaluations 0`, `Model cards 0`, `Datasets 0`, `Prompt templates 2` |
| `CHANGELOG.md` → "Known gaps at release" | **Yes** — every empty corpus listed, plus the 7 frontmatter and 88 policy warnings, the 3/5 identity score, and the unreachable arXiv API |
| Directory READMEs (57 of them) | **Yes** — each opens with *"Status: scaffolded, empty"* and states what belongs there |
| `README.md` layer table (lines 64-78) | **No** — presents `patterns/`, `anti-patterns/`, `failure-modes/`, `gotchas/`, `evaluations/` as functional layers answering questions, with no note that five are empty |
| `README.md:313-317` | **No** — asserts the 40-task two-arm suite exists and names seven metrics it compares (C-3) |
| `AGENTS.md:53` | **No** — *"'Tests' here means validators plus the evaluation suite in `evaluations/`"* (C-3) |
| `README.md` CI section | **No** — claims external links resolve on every push/PR (M-11) |

So the same repository says "0 evaluations" in the generated stats block and "is benchmarked with
a 40-task suite" eleven screens earlier. The generated block is right; the prose is not. This is
the documentation equivalent of H-2: the honest value exists and is authoritative, and a
hand-written claim elsewhere contradicts it.

**Is the 40-task suite specification-only?** **Yes.** Confirmed: `evaluations/` contains 0 content
files, `evaluations/knowledge-base/` does not exist as a path, `metadata/evaluations.json` holds 0
records, `indexes/evaluations.md` is an empty generated index, and `CHANGELOG.md` states plainly
that the suite *"is specified but not built"*. The specification itself is real and reasonably
detailed (seven comparison metrics, two arms) — but no task, rubric, run or result exists.

**Recommended fix:** make the generated stats block the single source for every count, and have
the prose reference it rather than restating numbers. For the three places that assert
non-existent capability (C-3 ×2, M-11), restate in the conditional and link to the specification
or to `CHANGELOG.md`'s gap list. A simple rule would prevent recurrence: **no hand-written
sentence in `README.md` or `AGENTS.md` may contain a count or a path that the validators do not
check.**

---

## 12. Known Gaps

These are correctly disclosed in `CHANGELOG.md` and are recorded here for completeness, not as
new findings. None blocks merge, since all are stated honestly where it matters.

| Gap | Actual | Disclosed in |
|---|---|---|
| `patterns/` corpus | 1 pattern; 10 domain directories scaffolded and empty | `CHANGELOG.md`, directory READMEs, README stats |
| `anti-patterns/`, `failure-modes/`, `gotchas/` | 0 content files; failure modes documented inside skills and workflows instead | `CHANGELOG.md`, README stats |
| `evaluations/`, `datasets/`, `models/` | 0 content files each | `CHANGELOG.md`, README stats |
| 40-task evaluation suite | specified, not built | `CHANGELOG.md` — but contradicted by `README.md:313` (C-3) |
| `prompts/` | 2 prompts across 9 categories; 7 categories empty | `CHANGELOG.md`, README stats |
| `experimental/`, `research-archive/` | 1 and 0 content files | `CHANGELOG.md` |
| 6 frontmatter warnings | `references/` files with `confidence: high` and no `sources[]` | `CHANGELOG.md` — deliberately not auto-fixed |
| 88 policy warnings | unlicensed-slug mentions in code files | `CHANGELOG.md` — see H-5 for why most are noise |
| MCP registry capability fields | empty for 35/35, `capability_evidence: unverified` | each registry entry, plus a six-item confirmation checklist |
| 1 thin MCP purpose | `purpose_evidence: repository-description-thin` | flagged in the entry itself |
| arXiv batch verification | API unreachable from the build environment; 9 papers verified individually, 61 quarantined | `CHANGELOG.md` |
| `EleutherAI/OpenAgentSafety` | does not exist on GitHub (404) | `CHANGELOG.md` |
| GAIA benchmark | not GitHub-hosted (Hugging Face only), so out of scope for this database | `CHANGELOG.md` |
| Dashboard example identity score | 3/5 by design; removing slop yields a competent neutral interface | the example file itself, §4 |

---

## 13. Recommended Next Steps

### Must fix before merge

Ordered by the risk of merging without them. All four are contained changes; none requires
re-fetching data or rewriting content.

| # | Finding | Change | Effort |
|---|---|---|---|
| 1 | **C-3** | Rewrite `README.md:313-317` and `AGENTS.md:53` in the conditional; point at the specification, state that no effectiveness claim is made | ~15 min |
| 2 | **C-2** | Decide the authoritative rule, then either amend `README.md:309` to match the 28 skills' actual (cited) state or downgrade them to `confidence: medium`; add the invariant to `validate_frontmatter.py` | ~1 h |
| 3 | **C-1** | Either regenerate `THEN`/`FAIL IF` from each skill's own Failure Modes and Anti-Patterns sections (the source material already exists and is skill-specific), or rename to `selection-cases.md` and remove the `test_pass_rate` claim from `README.md` | ~2 h (regenerate) / ~15 min (relabel) |
| 4 | **H-1** | Emit `authentication` only when observed; otherwise omit | ~5 min |

Items 1 and 4 are trivial and should not be deferred. Item 2 is a decision, not a task, and the
decision is the work. Item 3's honest minimum is the relabel; the regeneration is better and is
not large, because the per-skill prose it needs is already written.

### Should follow immediately after merge

| # | Finding | Change |
|---|---|---|
| 5 | **H-2** | Add the nine dropped fields to `MD_TMPL`; fix the scoped-package parse; add a CI assertion that `record_to_tool()`'s keys equal `tools.json`'s keys |
| 6 | **H-6** | Escape markdown-active characters in API-sourced strings; run `FORBIDDEN` patterns over `description`/`homepage`/`topics` and quarantine matches; add an ingestion-trust section to `SECURITY.md` |
| 7 | **H-4** | Move the exclusion list into `metadata/excluded-sources.json`; error in `validate_policy.py` if an excluded slug appears outside the exclusion docs; refuse to fetch them |
| 8 | **H-5** | Scan `.md` as well as code files; match `owner/name`; error on the vendoring shape; exclude `scripts/**` from the warning |
| 9 | **H-3** | Rename the `UNVERIFIED` tier to `NO-LICENSE`; reserve `UNVERIFIED` for failed fetches; record as a major-version schema change |
| 10 | **H-7, H-8** | Word-boundary category matching against topics/slug; add `registry_kind` and report server counts separately |
| 11 | **M-8, M-9, M-10, M-11** | Correct the cache claim in four places; split the knowledge-article count; fix 418→414; replace the CI check list with the six real job names and their triggers |
| 12 | **M-12** | Narrow the secret-scanner bypass to the matched string's own shape; drop the `example`-proximity clause and the dead `"<" in s` test |

### Defer to the scoring-model revision

M-1 through M-5, M-7, M-13, M-14, L-1, L-2, L-3 belong together: they are all properties of one
model, and fixing them piecemeal would move tiers several times. Treat as a single
**major-version** change — normalise components by their reachable ceilings, decorrelate
`recency` from `maintenance`, count license risk once, re-derive tier thresholds from the
resulting distribution, document the derivation, and reconcile the TTL table with
`freshness-policy.md`. Do this **before** the corpus grows, since every additional record
inherits the current compression.

### Defer to the content phase

L-4, L-5, L-6, L-7, L-8, L-9, M-6, M-15 — documentation accuracy, schema hygiene, and the
29-record LICENSE-file read. None affects correctness of what exists today.

### Add these validators, in this order

Each corresponds to a finding that CI currently cannot see, which is the common cause of every
critical issue in this report:

1. `evidence_level` × `confidence` cross-field invariant → catches C-2
2. assertion-distinctness measure on `tests/cases.md` → catches C-1
3. prose-path existence check for `README.md` and `AGENTS.md` → catches C-3, M-8, M-10
4. key-set equality across each generation chain → catches H-2
5. exclusion-list enforcement → catches H-4
6. untrusted-input scan over fetched API strings → catches H-6

### Merge recommendation

**Do not merge yet.** Fix C-1, C-2, C-3 and H-1 — roughly half a day's work, of which only the
C-2 decision and the C-1 regeneration are substantive. Then merge as the baseline checkpoint,
and take the high-priority items as the first follow-up PR.

The reason to hold is not that the repository is in poor shape. It is that all three critical
findings are the same failure — **a guarantee stated in prose and not honoured in data, with no
check in between** — and this repository's entire premise is that guarantees must be checkable.
Merging with three known instances of the failure it exists to prevent would set the wrong
precedent for every contributor who reads `skills/AGENTS.md` rule 3 and then looks at a test
file. The six validators listed above are what makes the precedent stick.

---

## 14. Post-fix re-review

**Re-reviewed commit:** `58dff2e` (fix) on `1d40468` (this report) on `32720b8` (reviewed state)
**Re-review date:** 2026-09-16
**Scope:** verify the four resolutions by measurement, check that the fixes did not introduce
regressions elsewhere, and re-state the merge recommendation against the current tree.

### 14.1 The four findings, re-measured

Each resolution was verified by running the repository's own validators and generators against
the fixed tree, not by reading the diff.

| Finding | Claim made by the fix | Independent measurement | Verdict |
|---|---|---|---|
| C-1 | `FAIL IF` no longer boilerplate | 1,108 cases, **1,108 distinct `FAIL IF`** (ratio 1.000, was 0.012), 1,106 distinct `THEN` (0.998, was 0.135), max skills sharing one `FAIL IF` = **1** (was 50) | **Confirmed** |
| C-2 | one rule, enforced, violations fixed | `validate_frontmatter.py` → 155 files, **0 errors**; 59 records changed, all downward; rule is an error not a warning | **Confirmed** — and the original count was wrong (28 → **59**) |
| C-3 | claims removed, paths checked | README/AGENTS.md say "Not measured"; prose-path check covers **101** paths, **0 errors**; 3 further false claims found and fixed | **Confirmed** |
| H-1 | `authentication` no longer guessed | **0 / 35** records carry the field; `assert_no_guesses()` reports 0 violations; negative test catches an injected `mixed` and an injected `tools` list | **Confirmed** |

Two of the four fixes found the original finding was **understated**: C-2's violation count was
59 rather than 28, because the review measured `skills/*/SKILL.md` only while the rule applies to
all graded frontmatter; and C-3's path check surfaced three additional false path claims that the
review did not list. Both are recorded in the resolution blocks above rather than quietly
absorbed.

### 14.2 The failure shape is now closed, not just the instances

The three critical findings shared one shape: *a guarantee stated in prose and not honoured in
data, with no check in between.* Every resolution adds the missing check, which is the part that
prevents recurrence:

| Guarantee | Previously checked by | Now checked by |
|---|---|---|
| "Cases are derived from the skill's own … failure modes and anti-patterns — never from a generic template" (`skills/AGENTS.md` rule 3) | nothing | `generate_skill_tests.py --check` — distinctness gates, CI step *Skill test cases are skill-specific* |
| "A skill that has never been run … cannot claim `confidence: high`" (`README.md`) | nothing | `validate_frontmatter.py` — `CONFIDENCE_CAP`, hard error |
| "Capability fields the GitHub API cannot tell us … are NOT guessed" (generator docstring) | nothing; the drift job passed because the generator was self-consistent | `assert_no_guesses()` — CI step *MCP registry asserts no unobservable capability* |
| paths named in prose exist | `validate_links.py` — markdown links only, which prose paths rarely are | `validate_links.py --internal` — backticked spans too |

The drift job also now regenerates with both new generators plus `update_readme_stats.py`, so a
hand-edited `cases.md` or registry entry fails CI the same way a hand-edited index already did.

### 14.3 Regressions checked for, and one real consequence

Verified clean after the fix:

- **Frontmatter:** 155 governed files, 0 errors, 1 warning — the warning is pre-existing
  (`patterns/agents/context-compaction.md` exceeds its token budget) and unrelated.
- **JSON registries:** 959 records, 0 errors, 0 warnings.
- **Links:** internal 0 errors, 1 pre-existing warning (`skills/evidence-validation` lists a
  `fact-checker` related skill that does not exist).
- **Generated drift:** timestamp-only, which is what CI's own filter accepts.
- **No confidence was raised anywhere**, and no `evidence_level` was changed to justify one.
- **No timestamps or verification dates were added to make CI green.** The opposite happened:
  one exemption was widened (§14.3 below) and the honest answer to "is this measured?" was
  written into README as *no*.
- **Data not implicated by a finding was not churned.** Of 192 changed files, 50 are
  `tests/cases.md` and 50 are the `tests:` count in their `SKILL.md` (C-1), 59 carry a single
  `confidence` line (C-2), 35 are registry entries losing one `authentication` line (H-1), and
  the remainder are regenerated indexes/metadata plus the five documents and four scripts the
  findings name.

**One real consequence, reported rather than hidden.** Regenerating `cases.md` raised policy
warnings from 97 to 119, because the new cases quote skill prose verbatim and some of that prose
contains superlatives ("the fastest", "state-of-the-art") without an adjacent verification date —
the hallucination-firewall check flags each quotation as a fresh instance of a claim already
flagged at its source. Adding dates to generated test cases to silence this would have been
exactly the fabrication the fix was meant to avoid.

Instead the scan now skips **generated** artifacts (`indexes/*.md`, `repositories/**/*.md`,
`skills/*/tests/cases.md`), defined once as `GENERATED_GLOBS` / `is_generated()` in
`scripts/lib/frontmatter.py`. This loses no coverage: a generated file has no claims of its own,
and every governed source it quotes is still scanned in its own right — confirmed for all five
skills whose generated cases quoted superlatives, each still flagged at its own source —
`competitive-analysis/SKILL.md` (3), `deployment/SKILL.md` (3), `web-research/SKILL.md` (2),
`mcp-integration/SKILL.md` (2), `research-synthesis/SKILL.md` (1). Total warnings fall to **80**, below the
pre-fix baseline, and errors remain **0**. Structural documents (README, AGENTS, CHANGELOG) are
deliberately *not* exempted from this scan, so the one warning this fix added to `AGENTS.md` and
the seven in this report remain visible.

### 14.4 What the fixes did **not** accomplish

Stated plainly, because an unstated gap is how C-3 happened in the first place.

- **No skill test has been executed.** 1,108 cases are authored specifications of what would
  prove a skill failed. There is no harness, no runner, no result, and no `test_pass_rate`. The
  corpus is now able to discriminate between skills; nobody has measured whether any skill
  passes.
- **The knowledge base's effectiveness is still unmeasured.** The 40-task suite remains
  specified and unbuilt. C-3 removed the false claim; it did not build the thing.
- **`authentication` is now unknown for all 35 MCP servers, and that is a gap.** The honest
  field is absent until someone reads each project's documentation. H-1 removed a wrong answer;
  it did not supply a right one.
- **`official` still comes from a hand-maintained organisation list** (§L-2) and still carries
  up to +0.6 weighted score. H-1 removed the authentication inference that rested on it; the
  underlying inference in the scoring model is untouched.
- **H-2 … H-8 remain open**, including the nine schema fields still lost between the registry
  markdown and `tools.json` — which is why `not_recommended_for` still does not reach the JSON
  for the one archived server.

### 14.5 Merge recommendation

**Merge.** The three critical findings are resolved and measured, and each resolution is enforced
by a check that did not exist before, so the specific failure this repository exists to prevent —
a guarantee in prose with nothing honouring it in data — no longer has three live instances.

Recommended immediately after merge, in this order, as the first follow-up PR:

1. **H-2** — nine fields lost in the markdown → JSON chain. This is data loss on the path agents
   actually read, and it hides the archived-server warning.
2. **H-3** — the `UNVERIFIED` tier names the wrong property; all 15 records have `fetch_ok: true`
   and the real condition is "no license detected". A tier whose label misdescribes its own
   membership will be misread by every consumer.
3. **H-7 and H-8** — `category` assigned by unanchored substring match (both official SDKs are
   labelled `ci-cd` because `'ci'` appears inside "offi**ci**al"), and five of the "35 MCP
   servers" are SDKs, a testing tool, a registry and a catalog. Both are one-line-ish corrections
   to generated data.
4. **H-4, H-5, H-6** — enforcement path for `SECURITY.md`'s hard exclusions, license-override
   warnings on markdown rather than source code only, and sanitisation of untrusted API
   descriptions rendered into cards.
5. **The scoring revision** (M-1 … M-6 as a group) before the corpus grows: the saturated
   adoption component, inconsistent component ceilings, and `days_since_push` driving three
   components are one coherent change and get harder to make with every record added.

Deferring these is defensible; merging with C-1/C-2/C-3 open was not, because each was a false
statement on the repository's front page or in its grading rule.

---

*§1–§13 generated 2026-09-16 against commit `32720b8`; §14 and the resolution blocks added the
same day against `58dff2e`. All quantitative claims were measured by executing the repository's
own scripts and reading its own data files; the measurement method is stated alongside each
finding so any of them can be re-checked independently. Finding text in §1–§13 is preserved as
originally written, including the counts §14 corrects.*
