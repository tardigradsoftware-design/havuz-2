# Changelog

Every notable change to this knowledge base. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the repository uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html) at the level of the content corpus: a
**major** version means a schema-breaking or policy-breaking change, a **minor** version means new
content or new capability, and a **patch** version means corrections, re-verification and metadata
refreshes.

Entries are added by the same PR that makes the change. An entry states what changed, why, and — where
a claim changed — what evidence supports the new position. Corrections to previously published claims
are never made silently; they appear here with the old position named.

---

## [2.1.0] — 2026-09-16

A documentation-consistency pass over what the repository *says about itself*. No repository was
re-fetched, no observed value was altered, no score was recomputed, and the scoring model is
untouched. No finding below 2.0.0's high-priority set was addressed: the 24 open Medium and Low
findings remain open and out of scope. **Minor** because it adds a validation capability; it also
corrects one published statistic, named below with its old value.

### Added — `scripts/validate/check_release_claims.py`: the prose is now checked against the data

Every count this repository publishes about itself was, until now, correct only by hand. The README
statistics block is generated, but the sentences around it — in README.md, in REVIEW-REPORT.md and
in this file — restate numbers in prose, and prose is where they go stale.

The new validator recomputes the corpus statistics from source data (`metadata/repositories.json`,
`metadata/tools.json`, `indexes/*.json`, the skill test suites) and cross-checks each prose claim
against the recomputation. It also asserts that the two qualifiers README uses about its test cases
— *"authored specifications, not executed results"* and *"No effectiveness claim is made"* — are
still present, so removing the hedge without removing the number fails validation.

A claim whose pattern stops matching is an **error, not a skip**. The first version of this script
labelled the README claims `"README"` while keying its document map `"README.md"`, so every lookup
missed, every claim was silently skipped, and the script reported success while checking nothing.
That is the failure mode this rule exists to prevent: a consistency checker that passes vacuously
is worse than no checker, because it is trusted. Eleven deliberate mutations were used to confirm
the script now fails on a stale count, a removed qualifier, a renamed table row and an unmarked
historical section.

It is wired into the `validate` job in [`.github/workflows/kb-ci.yml`](.github/workflows/kb-ci.yml)
as the step *Release claims — prose counts vs recomputed corpus statistics*, between the policy
validator and the regression tests. A validator that is not run by CI is advisory, and advisory
checks are how a wrong number stays published for a release.

### Fixed — README reported **50** skill test cases; the corpus holds **1,108**

`scripts/generate-index/update_readme_stats.py` counted `cases.md` **files** where it meant to count
**cases**. Fifty skills each have one `cases.md`, so the statistic reported 50 — the number of files,
not the number of specifications inside them. It now counts `## Case N` headings across those files,
which is 1,108. The old value understated the corpus by a factor of 22.

This was a generator bug, not a data change: no test case was added, removed or edited. The same
figure appears in README's narrative section, which already said 1,108 correctly — the generated
block and the prose disagreed, and the prose was right.

### Changed — REVIEW-REPORT.md now states which of its own sections is current

The report had grown to fifteen sections across four phases, each recording what was true when it
was written. §13 said "do not merge yet"; §14.5 said "merge"; §15.5 said something else again. All
three were correct at the time and a reader could not tell which still applied.

A three-layer reading guide now opens the report: §1–§13 are marked **historical** (the 2.0.0-baseline
review), §14 is marked **historical, Phase 4**, and §15 is marked **current and authoritative**. The
superseded merge recommendations in §13 and §14.5 carry banners saying so and pointing at §15.5,
which is now the sole authoritative merge recommendation.

The historical sections are **labelled, not rewritten**. Their findings, counts and recommendations
are preserved verbatim, because a review report that edits its own past stops being evidence of what
was found and when.

### Changed — README says plainly that the scoring model is not validated

The scoring section documented its weights and thresholds without stating their epistemic status,
which read as endorsement. A new subsection, *"Status of this model: implemented and reproducible,
**not** validated"*, now records that:

- the weights are **documented engineering judgement**, not coefficients fitted or measured against
  any outcome;
- the tier bands (S ≥ 8.0, A ≥ 7.0, B ≥ 5.8, C ≥ 4.3) live **only in code** — `scripts/lib/scoring.py`
  — and [`knowledge/ai-engineering/source-scoring.md`](knowledge/ai-engineering/source-scoring.md) does not restate them, which is an open documentation
  finding rather than something this release resolves;
- revising the model is **planned major-version work** and was out of scope for 2.0.0.

The thresholds themselves are unchanged and were verified to match `scoring.py::tier_for` exactly.

### Changed — the repository category `mcp-servers` no longer reads as a server count

README's generated category table listed `mcp-servers | 35` while its layer table listed
`MCP servers | 26`. Both are right and they measure different things: 35 repositories were filed
under that seed-list **category**, while the registry classifies 26 of its 35 **entries** as servers
on the evidence of each entry's own published text. Printed on one page with nothing said, the pair
invites a reader to reconcile them and conclude one is wrong.

`update_readme_stats.py` now emits a note under the category table saying what the category counts
and where the registry split lives. The note is generated rather than hand-written into README.md so
that regenerating the block cannot drop it, and `check_release_claims.py` fails if the note is
removed or if the split it states drifts from the data.

### Changed — the 1.0.0 section below is marked historical rather than corrected in place

Two figures in `[1.0.0]` no longer describe the corpus: `15 UNVERIFIED` (the tier was renamed and
redefined by H-3 in 2.0.0) and `427 generated cards` (that count included the 12 category READMEs
alongside the cards). They are preserved verbatim under a banner explaining both, because they were
true of 1.0.0 as released and a changelog that rewrites its own history cannot be used to check
anything. `check_release_claims.py` scopes its tier check to the current version section and
requires any older section that restates a superseded label to carry such a banner.

### Added — `tests/test_release_claims.py`: 26 tests, including one against the checker itself

The checker above is now covered by regression tests, and the most important of them tests the
checker rather than the corpus. `test_every_required_claim_pattern_matches` asserts that each
required prose claim still matches something in the file it names. Without it, the defect described
above — claims labelled `"README"` against documents keyed `"README.md"`, so every lookup missed and
every comparison was skipped — would pass unnoticed, because a skipped claim and a verified claim
both exit 0. `test_claim_document_labels_resolve_against_real_files` covers the same bug from the
other direction.

The remaining tests inject each stale figure and assert it is caught: 333 for 1,108 test cases, 35
for 26 servers, 0 for 9 non-server entries, a renamed table row, and each of the four load-bearing
qualifiers removed while its number is left in place. `tier_assertions` is tested directly for the
three cases where a naive `\d+ UNVERIFIED` scan is wrong: a backticked mention naming the old label
in order to record its correction, `0 UNVERIFIED` as a true statement about a corpus with no fetch
failures, and line numbers in a sliced section, which must be reported against the file and not
against the slice.

The suite is now 248 tests (was 222).

### Fixed — `tests/README.md` named a test module that does not exist

Its invariant table listed `test_sanitization.py` for the H-6 regression. No such file exists; the
H-6 module is `test_untrusted_text.py`, and has been since H-6 was fixed. The table is the only
place that explains what each module protects, so a reader following it to the wrong filename finds
nothing and cannot tell whether the module was renamed or never written. Every `tests/` and
`scripts/` path named in `tests/README.md`, `README.md`, `CONTRIBUTING.md` and `AGENTS.md` was then
checked to resolve; this was the only one that did not.

### Verified — no change needed

- README's *"How skills are tested"* section already stated the case count correctly, already
  described the cases as authored specifications rather than executed results, already carried no
  pass-rate statistic, and already recorded the 40-task evaluation suite as specified but not built.
  Left as it was.
- README's tier thresholds match `scripts/lib/scoring.py::tier_for` exactly.
- No document outside REVIEW-REPORT.md and this file claims "35 MCP servers". The one remaining
  occurrence, in `tests/README.md`, quotes the original H-8 finding text and is correct as a
  quotation.

## [2.0.0] — 2026-09-16

The high-priority findings from [`REVIEW-REPORT.md`](REVIEW-REPORT.md), after the critical
ones were fixed in 1.1.0. **Major** because the `tier` vocabulary in
[`schemas/common.defs.json`](schemas/common.defs.json) changes meaning and gains a member:
a consumer that treated `UNVERIFIED` as "no license" will now misread the corpus, so the
old name is recorded here with what it used to mean. No repository was re-fetched, no
observed value was altered, and no score was recomputed — the scoring model is untouched.

### Changed — H-8: nine of the "35 MCP servers" are not servers, and are no longer counted as such

**What was wrong.** The registry was built by filtering `repositories.json` for
`category == "mcp-servers"`, which is a **seed-list** category — an assertion made when the
record was added, not a verified property of the repository. Five of the 35 entries were not
servers, and each entry's own `purpose` field quoted the description that said so, so the
registry contradicted its own label five times over. Consumers are
`skills/dont-reinvent-the-wheel` and `skills/mcp-integration`, which tell an agent to consult
this registry before building or installing a server: an agent handed an SDK or a catalog gets
nothing usable, and the count inflated the registry's apparent coverage.
`modelcontextprotocol/registry` was the sharpest case — a competing registry listed as an entry
in this one.

**Re-checking all 35 against their own observed text found nine, not five.** The four the review
did not list are each classified on a fragment of their own published description:

| Repository | Kind | Its own words |
|---|---|---|
| `modelcontextprotocol/python-sdk` | `sdk` | *"The official Python **SDK** for Model Context Protocol servers and clients"* |
| `modelcontextprotocol/typescript-sdk` | `sdk` | *"The official TypeScript **SDK** …"* |
| `vercel/mcp-handler` | `sdk` | *"Easily **spin up** an MCP Server on Next.js, Nuxt, Svelte, and more"* — it produces servers, it is not one |
| `modelcontextprotocol/inspector` | `tooling` | *"Visual **testing** tool for MCP servers"* |
| `firebase/firebase-tools` | `tooling` | *"The Firebase **Command Line** Tools"* |
| `modelcontextprotocol/registry` | `registry` | *"A community driven **registry** service …"* |
| `punkpeye/awesome-mcp-servers` | `catalog` | *"A **collection of** MCP servers."* |
| `microsoft/mcp` | `catalog` | *"**Catalog** of official Microsoft MCP … server implementations"* |
| `stripe/ai` | `unproven` | *"One-stop shop for building AI-powered products and businesses with Stripe."* — MCP appears only as a bare topic |

**Result: 26 servers of 35 entries.** The other nine remain listed — an SDK and an inspector are
genuinely useful to record, they are just not servers, and hiding them would send the next
reader to rediscover them.

`unproven` is a real answer rather than a placeholder for the timid. `stripe/ai` publishes the
topic `mcp`, which says the repository *relates to* MCP; nothing observed asserts that it *is* a
server, and a bare `mcp` topic is explicitly not accepted as proof. Where the evidence does not
establish the kind, saying so is more useful than defaulting to `server`, because the count is
what a reader uses to decide whether to keep looking.

**Classification uses only text the GitHub API returned**, ordered most specific first — a
repository that calls itself a registry or a catalog is that even though it also contains the
words "MCP server", which every entry in this registry does. Server evidence is accepted in four
shapes: an owner-set `mcp-server`/`mcp-servers` topic, a description asserting an MCP server, a
slug naming the repository as MCP, and — for the nine records that publish no topics at all —
the slug alone.

**Two new fields make every kind auditable:** `registry_kind`
(`server`|`sdk`|`tooling`|`catalog`|`registry`|`unproven`) and `registry_kind_evidence`, which
quotes the deciding fragment. Every entry also states its kind and its consequence in the body a
human or agent actually reads — a non-server entry says *"This is not a server you can connect
to"*, and an `unproven` entry says it is not counted and what to read before adopting it.

**Counts are now derived, not asserted.** `indexes/mcp.md` leads with **26 MCP servers** and
lists the other nine under headings that say what they are and why they are not counted, with the
evidence in a column. The README statistics block shows both numbers —
`MCP servers | 26` and `MCP registry entries (incl. 9 that are not servers) | 35` — because
understating would be as wrong as overstating: the registry does hold 35 entries.

**Enforcement.** `assert_kinds_are_evidenced()` runs in write mode and in `--check`. It
re-derives each classification from the source record, then audits the *stored* claim
independently: a quoted fragment must occur in text the API actually returned for that
repository, a `server` claim may not rest on a bare `mcp` topic, and a `server` claim may not
have empty evidence. As with the category gate, re-derivation and the evidence audit are separate
checks — the first version reported a fabricated quotation only as "does not re-derive" and lost
the specific diagnosis. `--check` now prints the split
(`server:26, sdk:3, tooling:2, catalog:2, registry:1, unproven:1 — 26 of 35 entries counted as
MCP servers`) so it is visible without opening the JSON.

**Regression tests:** `tests/test_registry_kind.py`, 34 cases — each named misclassification
reproduced from its own description, `unproven` as a real answer, real servers still classified
through all four evidence shapes, the nine known non-servers asserted, evidence quotations checked
against the record, README and index counts derived from the classification, non-servers absent
from the server table but present in the index with their reason, each entry stating its kind to a
human reader, and five negative cases proving the gate rejects a kind that does not re-derive, a
fabricated quotation, a bare-topic server claim and an undeclared kind. 105 tests across the suite,
all passing.

### Fixed — H-7: registry categories are assigned by whole token, not by substring

**What was wrong.** `detect_category()` matched signals with `if signal in haystack` against
description + topics + slug, with no word boundaries. Short signals therefore matched inside
ordinary words, and the corpus already showed it: `modelcontextprotocol/python-sdk` and
`modelcontextprotocol/typescript-sdk` were both classified `category: ci-cd` because `'ci'`
occurs inside *"offi**ci**al"* in their own descriptions (*"The official Python SDK for Model
Context Protocol"*). `category` is what a consumer filters the registry on, so `ci-cd` was
confidently wrong for both official SDKs and propagated into `indexes/mcp.md`. The same error
was latent for `'cd'`, `'git'`, `'file'`, `'sql'` and `'docs'` — every signal short enough to
hide in a common word.

**What changed.** Matching is on whole tokens, and the sources are tried in order of how much
they can be trusted to mean what they say:

1. **topics and slug segments** — curated by the owner for discoverability, or chosen as the
   repository's name. Structured: a token is either there or it is not.
2. **the description**, only when nothing structured matched. Free prose is the weakest
   evidence — it is where *"official"* lives — but dropping it entirely would leave nine of the
   35 records that publish no topics unclassified, so it stays as a fallback rather than as a
   peer of the curated fields.
3. **`other`** when nothing matches, which is the honest answer and already a schema member.

**Six classifications changed; 29 did not.**

| Repository | Was | Now | Matched token |
|---|---|---|---|
| `modelcontextprotocol/python-sdk` | `ci-cd` | `other` | none — `'ci'` was inside *"official"* |
| `modelcontextprotocol/typescript-sdk` | `ci-cd` | `other` | none — same |
| `microsoft/mcp` | `ci-cd` | `other` | none — same |
| `stripe/ai` | `ci-cd` | `payments` | `stripe` (slug) |
| `exa-labs/exa-mcp-server` | `browser` | `search` | `exa`, `search` (topics) — `'crawl'` was inside *"crawling"* |
| `tavily-ai/tavily-mcp` | `browser` | `search` | `tavily` (slug) |

`ci-cd` now holds exactly one entry, `czlonkowski/n8n-mcp`, matched on the whole token `n8n`.

**`payments` was dead vocabulary.** It was already a member of the category enum but no signal
could ever select it, so a payments server fell through to whatever short signal happened to
appear in its prose. Signals were added for it. `design` and `knowledge` remain unreachable by
heuristic and are documented in the schema as reachable only by human curation, recorded as
`category_evidence: human-curated` — a category no heuristic can select is not a category the
generator may guess at.

**Two new fields make every classification auditable:** `category_evidence`
(`topics-or-slug` | `description-fallback` | `no-signal-matched` | `human-curated`) and
`category_signals`, the whole tokens that matched. A classification nobody can re-derive is a
classification nobody can check, which is how the `ci-cd` error survived review of the
generator that produced it.

**A hyphen bug the fix exposed, and was nearly caused by.** Tokenising on every
non-alphanumeric run makes hyphenated signals — `web-scraping`, `cloud-run`, `pull-request` —
unmatchable, and `firecrawl/firecrawl-mcp-server` duly dropped from `browser` to `search` under
the first implementation, because it publishes the topic `web-scraping`. Hyphenated forms are
now kept whole *as well as* split, so both are still whole tokens and no substring matching is
reintroduced.

**Enforcement.** `assert_categories_are_whole_tokens()` runs in write mode and in `--check`. It
re-derives each classification from the source record, then audits the *stored* claim
independently: every recorded signal must be a whole token of the field it is claimed from, and
a signal claimed from topics or the slug must not in fact occur only in the description. Those
two checks are deliberately separate — the first version skipped the token audit when
re-derivation disagreed, so a substring-justified category was reported only as "does not
re-derive" and the specific diagnosis was lost. A gate that merely re-ran `detect_category`
would pass against any matcher including the broken one, because it would be comparing the
function with itself; checking the tokens is what makes the substring version fail.

**Regression tests:** `tests/test_mcp_category.py`, 24 cases — the exact `official`/`ci` defect
reproduced from the real records, every short signal embedded in an ordinary word that contains
it (`official`, `social`, `digital`, `profile`, `researcher`, `traceability`…), hyphenated
signals still matchable, `firecrawl` staying a browser server, evidence precedence, `other`
when nothing matches, near-miss tokens (`postgrest`) not matching, every declared category
either reachable or documented as human-curated, and four negative cases proving the gate
rejects a reintroduced substring match, a signal attributed to the wrong field, and a stored
category that does not re-derive. 71 tests across the suite, all passing.

### Changed — H-3: `UNVERIFIED` no longer means "no license"

**What was wrong.** `tier_for()` returned `UNVERIFIED` when no license file was detected.
All **15** records in that tier had `fetch_ok: true` — they were successfully verified
against the GitHub API on 2026-09-15. What was true of them is that **no license was
published**. The label conflated epistemic status with legal status, and the tier spanned
scores 4.02–8.02, so it contained `vercel/mcp-handler` at 8.02 — above the S threshold —
labelled `UNVERIFIED`. An agent reading that label would reasonably re-fetch or discard
metadata that was sound, while the signal that actually mattered (do not redistribute) sat
in a separate field the tier name obscured.

The documentation already had it right: `knowledge/ai-engineering/source-scoring.md`
defined `UNVERIFIED` as *"Could not be verified"* and mapped only *"unresolvable / 404"* to
it. The code disagreed with the documentation.

**The two labels are now strictly separate.**

| Tier | What it says | What it does not say |
|---|---|---|
| `NO-LICENSE` | the metadata **was** verified, and verification found no published license — legally unsafe to redistribute | nothing about reliability; the record is fully trustworthy |
| `UNVERIFIED` | the metadata **could not** be verified — the fetch failed or the repository is unresolvable | nothing about the license; every other field on such a record is also suspect |

Precedence in `tier_for()` is `UNVERIFIED` (fetch failed) → `ARCHIVED` → `NO-LICENSE` →
score band. A failed fetch is tested first because it overrides even `ARCHIVED`: a flag we
could not fetch is a flag we are only repeating from stale data. `ARCHIVED` still outranks
`NO-LICENSE`, because a frozen repository is frozen whether or not it has a license and that
is the more actionable fact. Score bands are unchanged, and a non-SPDX custom license still
caps the tier at `A`.

**Migration.** `NO-LICENSE` was added to the `tier` enum with a description stating the
distinction, and `UNVERIFIED` was kept — it is the correct label for a state the corpus can
be in, and removing it would leave a failed fetch with nowhere honest to go. All 15 records
were retiered `UNVERIFIED → NO-LICENSE` by a new offline mode,
`fetch_github_metadata.py --retier`, which recomputes tier from stored fields without
touching the network. Tier rules change more often than repositories do, and re-fetching to
fix a labelling rule would churn `stars`, `checked_at` and `days_since_push` — data that was
verified and is not wrong. The rest of the distribution is unchanged: 214 S, 127 A, 29 B,
16 C, 3 EXPERIMENTAL, 10 ARCHIVED, **15 NO-LICENSE**, 0 UNVERIFIED. `--retier` is
idempotent and reports `changed: 0` when re-run.

`--retier` re-derives `license_nonstandard` from the stored `license` field, because the
fetcher does not persist the `signals` block that `score_repository()` computes. That
derivation is load-bearing: skipping it silently promotes every custom-licensed repository
from `A` to `S`, since the cap that keeps a `NOASSERTION` project out of the top tier *is*
that flag. The first version of `--retier` did skip it and reported 44 changes where 15 were
correct; it now reports a disagreement between stored signals and the license field as an
error rather than letting one quietly win.

**Enforcement.** `validate_json.py` now checks both directions for every record:
`UNVERIFIED` requires `fetch_ok` not to be true; `NO-LICENSE` requires that no license was
detected and that the fetch succeeded; and no record whose license is absent may sit in a
score band (`S`, `A`, `B`, `C`, `EXPERIMENTAL`), because the license test precedes the bands
in `tier_for()`. The check is deliberately narrow about what counts as "absent": only
`license_risk: no-license-do-not-redistribute` or the literal string `"NONE"`. Reading
`license: null` as absence produced six false errors, because `metadata/tools.json`
collapses `NONE` and `NOASSERTION` into `null` — and those six custom-licensed MCP entries
are correctly in tier `A`.

The registry generator no longer defaults a missing tier to `UNVERIFIED`
(`t.get("tier") or "UNVERIFIED"`), which would have reasserted a fetch failure that never
happened; a record with no tier now stops the build. `update_readme_stats.py` reads the tier
rows from the schema enum instead of a hard-coded list, so the README table cannot print a
label the schema no longer uses — that list is how the table came to show `UNVERIFIED` beside
an empty count.

**Documents updated:** `README.md` (override precedence, plus a table distinguishing the two
labels), `knowledge/ai-engineering/source-scoring.md` (tier table and the hard-override
block, which now names `tier = NO-LICENSE` for `license: null`). The occurrences of
`UNVERIFIED` in `metadata/workflows.json` are prose about quarantining unverifiable
*sources*, which is the word's correct epistemic sense, and were left alone.

**Regression tests:** `tests/test_tier_semantics.py`, 31 cases — the mapping in both
directions, override precedence, score bands unaffected by the rename, the custom-license
cap intact, the committed corpus consistent with its own labels, all four ways the labels can
be confused reported as errors, `license: null` not mistaken for absence, `--retier` offline
and idempotent, and the silent default gone.

### Fixed — H-2: nine registry fields no longer lost between markdown and `tools.json`

**What was wrong.** The chain `repositories.json → knowledge/mcp/registry/*.md →
metadata/tools.json` is one-directional by design, and `extract_registries.py` reads only the
markdown frontmatter. Nine fields that `record_to_tool()` computed were not emitted by
`MD_TMPL`, so they never reached the JSON — and nothing could see it: all nine are optional in
`mcp.schema.json`, so schema validation reported 0 errors, and the drift job passed because
regeneration reproduced the same loss.

The consequential loss was `not_recommended_for`, which for the one archived server
(`browserbase/mcp-server-browserbase`) carried `"adoption in new work — archived"`. That
do-not-adopt signal existed **nowhere** — not in the markdown, not in the JSON — and only the
weaker `production_readiness: deprecated` survived.

**What changed.** All nine round-trip now: `npm_package`, `pypi_package`, `permissions`,
`recommended_for`, `not_recommended_for`, `resources`, `prompts`, `days_since_push` and
`language`. Keys produced by `record_to_tool()` 38, keys present in `tools.json` **29 → 38**,
fields lost **9 → 0**, compared per record rather than on the union so a field emitted for one
repository and dropped for another cannot hide in the aggregate.

The review's list of nine named `uvx` and `npx` rather than `days_since_push` and `language`.
Those two are schema properties the generator never computed at all, so they were absent
rather than lost, and they remain absent: deriving a run command would be exactly the kind of
guess this generator exists to avoid.

**A latent bug surfaced, as the review predicted.** `detect_distribution` derived an npm
package name with `homepage.rsplit("/", 1)[-1]`, which for
`https://www.npmjs.com/package/@playwright/mcp` yields `mcp` — not an installable name. It was
invisible while the field was dropped. `package_from_url()` now takes the path after the
registry's own `/package/` segment, keeps the scope, handles PyPI's `/project/` and legacy
`/pypi/` paths, and returns `None` rather than a truncated guess when the URL is not a package
page. Every npm value in the corpus is checked against the homepage it was derived from, so a
scoped name cannot silently lose its scope again.

Values are emitted through `yaml_scalar()`, which quotes by value rather than by field name:
`@playwright/mcp` must be quoted because `@` is a reserved YAML indicator, and a language named
`null` would otherwise parse as `None`. A test round-trips every emitted shape through a YAML
parser, because a field that does not survive being re-read is lost just as surely as one never
written.

**Enforcement.** Two gates, since one direction alone would miss half the failure: write mode
renders every entry and fails if a computed field is absent from the rendered frontmatter —
checked against *rendered output* rather than `MD_TMPL`'s source, because a conditional prefix
hides a key from a line-start match, which is how the first version of this gate was wrong; and
`--check` additionally compares against the committed `tools.json` in both directions, failing
on any key the schema does not declare. CI already runs `--check`.

**New in this release: a regression test suite.** `tests/` holds dependency-free stdlib
`unittest` modules, because `scripts/requirements.txt` is deliberately minimal and a suite
needing a third-party runner would not be. A test belongs there when it protects an invariant
**no validator can see** — a relationship between two artifacts rather than a property of
either one — and every module includes a negative case that reinjects the original defect and
asserts it is caught, because a gate never seen to fail is not evidence of anything. `make test`
runs them; `audit` and `ci` depend on it; CI has a *Regression tests* step.

---

## [1.1.0] — 2026-09-16

Corrections from the pre-merge review of 1.0.0 ([`REVIEW-REPORT.md`](REVIEW-REPORT.md),
35 findings against commit `32720b8`). This release fixes the three critical findings
and the first high-priority one. No data was invented and no confidence was raised:
every grading change moves a claim **down** to what its evidence supports.

### Fixed — C-1: the skill test corpus was a template

**What was wrong.** 333 cases shared only **4 distinct `FAIL IF` strings** — every
failure condition in the corpus was one of four sentences, identical across
`accessibility-audit`, `rag-pipeline` and `threat-modeling` alike. `THEN` had 45
distinct values, of which 3 covered 87%. Only the `GIVEN` line was skill-specific.
The suite could detect a skill being selected when it should not have been, and
nothing else. `skills/AGENTS.md` rule 3 prohibited this in terms.

**What changed.** `scripts/generate-index/generate_skill_tests.py` now derives all
four clauses from each skill's own body:

| Case kind | Derived from |
|---|---|
| Applies | Purpose, Workflow step titles, Quality Checklist items |
| Declines | each `When NOT to Use` exclusion, with the alternative it names |
| Detects | each `Failure Modes` entry, with its own detection signal and documented response |
| Avoids | each `Anti-Patterns` entry, with the consequence that entry states |

`THEN` and `FAIL IF` quote that material verbatim, so assertions differ per skill by
construction rather than by rewording. Both parsers handle the two `Failure Modes`
shapes in the corpus (14 skills use a `Failure | Detection | Response` table, 36 use
an aligned `NAME  description` block).

**Measured result.** 1,108 cases across 50 skills (17–26 each, up from 333):

| Clause | Before | After |
|---|---|---|
| distinct `GIVEN` | 332 / 333 | 1,092 / 1,108 |
| distinct `THEN` | 45 / 333 (ratio 0.135) | **1,106 / 1,108 (ratio 0.998)** |
| distinct `FAIL IF` | **4 / 333 (ratio 0.012)** | **1,108 / 1,108 (ratio 1.000)** |
| max skills sharing one `FAIL IF` | 50 | **1** |

The two remaining duplicate `THEN` values are two skills that genuinely list the same
anti-pattern ("logging the full request body on an auth endpoint"); the assertion is
shared because the guidance is. `WHEN` stays at 199 distinct values by design — it
names the act of applying a particular skill, so ~4 values per skill is correct.

**The guarantee is enforced, not asserted.** The generator measures its own output and
refuses to write unless `THEN` and `FAIL IF` distinctness are both ≥ 0.95 and no
`FAIL IF` is shared by more than one skill. `--check` runs the same gates for CI.

**Corrected alongside:** `README.md` claimed skills *"are graded by their
`test_pass_rate` in frontmatter"*. No skill has that field and none has been executed
by a harness. The section now states that the cases are **authored specifications, not
executed results**, and that no pass rate exists or should be inferred.

### Fixed — C-2: evidence level now caps confidence, corpus-wide

**What was wrong.** `README.md` stated that `evidence_level: practitioner-experience`
or `model-generated` *"cannot claim `confidence: high`"*. **59 governed documents did
exactly that.** The review counted 28 because it measured `skills/*/SKILL.md` only;
the rule applies to everything with graded frontmatter.

**The single rule adopted**, derived from the `evidenceLevel` descriptions already in
`schemas/common.defs.json` — not invented for this fix:

| `evidence_level` | Maximum `confidence` |
|---|---|
| `verified-github-api`, `verified-official-docs`, `verified-paper`, `verified-benchmark-run` | `very-high` |
| `cross-checked` | `high` |
| `single-source`, `emerging-consensus`, `practitioner-experience` | `medium` |
| `model-generated` | `low` |

Defined once as `CONFIDENCE_CAP` in `scripts/lib/frontmatter.py`, documented in
`README.md`, and enforced as a **hard error** by `validate_frontmatter.py` — so CI now
fails on any future violation rather than warning.

**59 records corrected, all downward:**

| Change | Count | Directories |
|---|---|---|
| `practitioner-experience` + `high` → `medium` | 50 | skills, agents, workflows, knowledge, prompts, decision-records |
| `cross-checked` + `very-high` → `high` | 6 | knowledge |
| `practitioner-experience` + `very-high` → `medium` | 2 | knowledge |
| `emerging-consensus` + `high` → `medium` | 1 | knowledge |

By directory: skills 33, knowledge 10, agents 7, workflows 5, decision-records 2,
prompts 2. `evidence_level` was **never** raised to justify a confidence — that is the
specific failure the rule exists to prevent. Frontmatter warnings fell from 6 to 1 as
a side effect, since five of the six were "confidence high with no sources".

### Fixed — C-3: documentation no longer asserts an evaluation suite that does not exist

**What was wrong.** `README.md` stated *"The repository itself **is benchmarked** in
`evaluations/knowledge-base/` with a 40-task suite run in two arms … comparing success
rate, time, token usage, code quality, bug count, security issues and architecture
quality."* `AGENTS.md` repeated it. `evaluations/` holds **0 content files** and
`evaluations/knowledge-base/` does not exist as a path. `CHANGELOG.md` already said the
suite was "specified but not built", so the repository contradicted itself.

**What changed.** Both documents now state plainly: *"Not measured. No effectiveness
claim is made."* The suite is described as specified-but-not-built, the non-existent
path is gone, and the future plan is separated from present fact. `AGENTS.md` now
distinguishes the three things "tests" could mean here — validators (exist, enforced in
CI), skill test cases (authored, not executed), and the effectiveness suite (not built).

**New check.** `validate_links.py --internal` now asserts that every repository path
named in prose in `README.md`, `AGENTS.md`, `CONTRIBUTING.md`, `SECURITY.md` and
`CHANGELOG.md` actually exists — backticked spans as well as link targets, since prose
paths are rarely links. 101 paths checked. Documented naming conventions
(`research-archive/YYYY/MM/`) are exempt via a placeholder-segment list, and tokens
whose first segment is not a real top-level entry are ignored, which keeps GitHub slugs
and package names out of the check without an allowlist.

**The check immediately found three more false claims**, all now corrected:

- `README.md` listed `scripts/score/score_sources.py` in its automation table. That
  script has never existed; the row is replaced with the five generators that do.
- `CHANGELOG.md` referenced `indexes/sources-papers.md`, which `build_index.py` does
  not produce. Corrected to `metadata/sources-papers.json`, the file that exists.
- `sources/papers/README.md` referenced the same non-existent index (fixed pre-commit).

### Fixed — H-1: the MCP registry no longer guesses authentication

**What was wrong.** `generate_mcp_registry.py` documented that capability fields the
GitHub API cannot report *"are NOT guessed"*, and correctly left five of them empty —
then inferred the sixth:

```python
"authentication": "mixed" if rec.get("official") else None,
```

**28 of 35 records** asserted `authentication: mixed` on the sole evidence that the
owner appears in a hand-maintained organisation list. Authentication is the field an
integrator acts on, and `official` says who owns a repository, not how its server
authenticates. The guarantee was the valuable part of that generator, and one field
quietly voided it.

**What changed.** The inference is removed. `authentication` is now absent from all
35 records and from all 35 markdown entries, which is the honest representation: the
schema's enum has no `unknown` member, and absence plus
`capability_evidence: unverified` says exactly what is known. Entries document how to
fill it in — read the project's own docs, then set `capability_evidence` to
`readme-reviewed` or `verified` and date it.

**The guarantee is now enforced.** `assert_no_guesses()` fails the generator if any
entry with `capability_evidence: unverified` carries a populated capability field
(`transport`, `tools`, `resources`, `prompts`, `permissions`, `authentication`,
`recommended_for`). Verified by negative test: injecting `authentication: "mixed"` or
`tools: ["read_file"]` into a clean corpus is caught and reported with the offending
repository named.

**Verified after the fix:** 35/35 records — `authentication` absent, `transport`,
`tools`, `resources`, `prompts`, `permissions`, `recommended_for` and
`not_recommended_for` all empty, `capability_evidence: unverified` on every entry.

### CI

`generated-drift` now regenerates with both new generators and runs their gates as
named steps — *MCP registry asserts no unobservable capability* and *Skill test cases
are skill-specific* — so each generator's guarantee is checked on every push and pull
request rather than resting on its docstring. `update_readme_stats.py` was added to the
regeneration list, since the statistics block was previously regenerated only by hand.

### Still open from the review

Recorded rather than closed, per this repository's own rule on unstated gaps. The
review's remaining findings are untouched by this release:

- **High:** H-2 nine schema fields lost between the registry markdown and `tools.json`,
  including the archived server's `not_recommended_for` warning; H-3 the `UNVERIFIED`
  tier names the wrong property (all 15 records have `fetch_ok: true`; the real
  condition is "no license detected"); H-4 `SECURITY.md`'s hard exclusions have no
  enforcement path in code; H-5 the license override warns only on source-code files
  in a repository whose vendoring risk is markdown; H-6 GitHub API descriptions are
  rendered into cards as markdown with no sanitisation, an injection surface in a
  corpus built to be read by agents; H-7 MCP `category` assigned by unanchored
  substring match — both official SDKs are labelled `ci-cd` because `'ci'` appears
  inside "offi**ci**al"; H-8 five of the "35 MCP servers" are SDKs, a testing tool, a
  registry and a catalog.
- **Medium/Low:** the scoring model's saturated adoption component (94% of records at
  the ceiling), inconsistent component ceilings (theoretical maximum 9.30, which is why
  51.7% of the corpus reaches tier S), `days_since_push` driving three components, the
  `.cache/gh/` reproducibility claim that is not committed, and 20 further items. These
  are grouped in the report as one major-version scoring revision, to be done before the
  corpus grows.

---

## [1.0.0] — 2026-09-15

> **Historical record — the figures below describe 1.0.0 as released, not the current tree.**
> Two of them have since been superseded and are preserved here verbatim rather than rewritten,
> because a changelog that edits its own past stops being a record. The tier written
> `15 UNVERIFIED` is now `15 NO-LICENSE`: H-3 (in 2.0.0) separated "the fetch failed" from
> "verification found no license", and these records were always the second. The card count
> `427` counted the 12 category READMEs alongside the cards; the current card count is in
> README.md's generated statistics block. For the present state see
> [`REVIEW-REPORT.md` §15](REVIEW-REPORT.md#15-phase-5-post-fix-re-review) and
> `python3 scripts/validate/check_release_claims.py`.

Initial public release. Everything below was authored, verified and validated in a single build pass
against live sources on 2026-09-15.

### Added

**Knowledge layer**

- `knowledge/` — 37 articles across nine domains, each with a graded frontmatter record:
  `claim_type`, `evidence_level`, `confidence`, `verified_at`, `expires_at` and a provenance block.
- Nine domain areas populated: `ai-engineering/`, `agent-engineering/`, `frontend/`, `ui-ux/`,
  `animation/`, `testing/`, `security/`, `research/`, `mcp/`, `database/`, `reasoning/`.
- Freshness windows set per claim class in `knowledge/ai-engineering/freshness-policy.md`:
  30 days for security and pricing, 90 for fast-moving tooling, 180 for framework behaviour,
  365 for architecture and theory, and no expiry for mathematics or specifications.
- The scoring model and its hard overrides in `knowledge/ai-engineering/source-scoring.md`:
  eight weighted components computed only from observable GitHub facts, plus overrides that beat the
  score — archived, abandoned, no license, inactive maintainer, experimental, and security-flagged.

**Repository database**

- `metadata/repositories.json` — 414 repositories fetched live from the GitHub REST API on
  2026-09-15, zero fetch failures, each scored, tiered and merged with curated judgement.
- Tier distribution: 214 S, 127 A, 29 B, 16 C, 3 EXPERIMENTAL, 10 ARCHIVED, 15 UNVERIFIED.
- 427 generated cards under `repositories/`, organised into 12 categories, plus a category README
  for each.
- 417 seed repositories deduplicated to 414 records through alias collapse; 27 confirmed renames
  resolved (among them `facebook/react` → `react/react`, `github/gh` → `cli/cli`,
  `tabby-ml/tabby` → `TabbyML/tabby`, `firebase/genkit` → `genkit-ai/genkit`).
- 10 archived repositories flagged rather than scored: including `protectai/rebuff` and
  `sourcegraph/cody-public-snapshot`.
- Every record carries a `license_risk` field. Repositories returning `license: null` from the API —
  including `anthropics/skills` and `openai/skills` — are marked
  `no-license-do-not-redistribute`, which blocks vendoring regardless of score or popularity.

**Skills**

- `skills/` — 50 skills, each a `SKILL.md` with frontmatter, a body within the 2500-token budget, and
  a `tests/cases.md`.
- 333 test cases across the corpus in GIVEN / WHEN / THEN / FAIL IF form, each derived from the
  skill's own purpose, exclusions, failure modes and anti-patterns rather than from a generic
  template.
- Categories covered: agent design, memory, context engineering, prompt engineering, reasoning,
  evaluation, RAG and retrieval, data pipelines, root-cause analysis, code review, refactoring,
  testing, debugging, performance, security, accessibility, design systems, typography, visual
  hierarchy, animation, CRO, copy, AI-slop detection, repository analysis, research, evidence
  validation, synthesis, MCP design, tool design, and skill curation itself.
- `skills/ai-slop-detection/` with two worked before/after examples: a SaaS analytics dashboard
  scored 8/35 → 30/35 with every contrast pairing measured, and a landing-page rewrite scored
  10/40 → 32/40 with each signature removed individually.

**Agents and workflows**

- `agents/` — 12 agent definitions with scoped permissions, handoff contracts and refusal conditions.
- `workflows/` — 11 staged workflows, each with per-stage exit gates, loop budgets, quality gates and
  named failure modes. Includes `deep-research/` (nine stages, saturation-based stopping condition)
  and `research-before-coding/`.

**Prompts and patterns**

- `prompts/research/deep-research-loop.md` — the single-prompt form of the deep-research workflow,
  with the full prompt text machine-readable in frontmatter.
- `prompts/ui-ux/design-direction-brief.md` — produces a design brief, not a visual implementation.
- `patterns/agents/context-compaction.md` — working-memory compaction with durable state, including
  the silent-loss failure mode that makes compaction dangerous.
- `decision-records/` — an ADR template and a decision-matrix template, both usable as-is.

**Sources**

- `metadata/sources-papers.json` — 9 papers verified against their primary arXiv sources, with title,
  authors, identifier and version date confirmed individually.
- 61 further paper candidates quarantined in `pending-paper-candidates.json` rather than published
  unverified.
- The verification finding that drove the quarantine policy: an aggregator API returned **wrong
  titles for valid arXiv identifiers** on two of the papers checked. Identity is therefore always
  confirmed against the primary source.

**Tooling and governance**

- `schemas/` — 17 JSON Schema files governing every content type, with `additionalProperties: false`
  throughout so that a typo in a field name fails validation rather than being silently ignored.
- `scripts/` — validation (`validate_frontmatter.py`, `validate_json.py`, `validate_links.py`,
  `validate_policy.py`), maintenance (`fetch_github_metadata.py`, `check_staleness.py`, `dedupe.py`),
  generation (`extract_registries.py`, `build_index.py`, `generate_repository_cards.py`,
  `update_readme_stats.py`), scoring (`score_skills.py`, `lib/scoring.py`) and crawling
  (`verify_arxiv_papers.py`, `verify_urls.py`).
- `indexes/` — 13 generated indexes covering 428 entries.
- `.github/workflows/kb-ci.yml` — six CI jobs running the full validation suite on every PR.
- `Makefile` with the same targets, so local and CI runs are identical.
- Five issue templates, plus Dependabot configuration.
- `AGENTS.md` at the root: the operating contract for any agent working in this repository.
- `SECURITY.md` with the exclusion policy, and `CONTRIBUTING.md` with the contribution workflow.
- Dual licensing: `LICENSE` (CC BY-SA 4.0) for content, `LICENSE-CODE` (MIT) for scripts and schemas.

### Ingested text is treated as untrusted input

- **H-6 — untrusted GitHub API text was embedded verbatim into generated markdown.**
  `description`, `homepage`, `topics` and `name` are set by whoever owns the repository, and the
  fetcher recorded them correctly — verbatim, because that is the observed fact. The defect was
  downstream: generators wrote them straight into markdown, so text travelled from an arbitrary
  third party into a file this repository publishes for agents to ingest as trusted guidance.
  Verified in the corpus before the fix, out of 401 descriptions: 5 contained bare URLs that
  GitHub renders as live links (the `postgres/postgres` card linked out to a wiki page nobody
  here had reviewed); `repositories/databases/postgres--postgres.md` rendered `*mirror*` as
  italics, so upstream emphasis silently became this repository's emphasis; and `camel-ai/camel`
  reproduced the vendor claim *"The first and the best multi-agent framework"* as though it were
  content — on a card ranked **#1 under "BEST AGENT FRAMEWORKS"** in `indexes/best-of.md`. None
  of those is malicious, which is exactly why they mattered: the same pipeline that renders a
  harmless `*mirror*` as formatting renders an instruction to whatever agent reads the card next.
  - `scripts/lib/sanitize.py` is the single boundary, on the rule **display, do not interpret**.
    `metadata/repositories.json` keeps the raw string — sanitising the stored record would
    destroy the evidence of what upstream actually said — and sanitisation happens where text
    stops being data and starts being rendering.
  - Markdown-active characters are escaped rather than deleted, so nothing upstream said is
    altered. Escaping is **position-aware**: `!`, `#`, `>` and single `~` are only active in a
    position, so "It's fast\!", ":cherry\_blossom:", "Graphs that teach > graphs that impress"
    and "The #1 library" are left exactly as published. Escaping them everywhere would have put
    visible backslashes into files this repository expects agents to read as plain text. Only
    17 of 401 descriptions change at all.
  - Bare URLs become inline code instead of live links this repository would be asserting. They
    are handled as units, so the address stays readable and copyable rather than being escaped
    to death.
  - `homepage` is a URL field, not prose, so it gets a different treatment: backticking it would
    remove a link readers genuinely want and gains nothing, since a bare URL's destination is
    already visible. What a bare render does *not* protect against is the scheme — so a homepage
    is linked only when it is plainly `http(s)` and free of syntax-breaking characters, with the
    destination as its own label. `javascript:`, `data:`, an embedded pipe and an embedded quote
    are all refused as links.
  - Descriptions are now framed as *"Upstream description, quoted as published and not verified
    here"*. Without the framing a card reads as though this repository asserts the description,
    which is how the vendor superlative came to be presented as content.
  - A description matching an injection pattern is **quarantined, not rendered**: the card says
    so, names the patterns matched, and keeps the raw string in the registry as the observed
    fact. Escaping makes text inert as markdown; it does nothing about a description whose
    *content* is an instruction, which is the more serious case here.
  - `validate_policy.py` check 8 scans `description`, `homepage`, `topics`, `name` and MCP
    `purpose` across `repositories.json`, `tools.json` and `sources.json`, and **fails the build**
    on a match. Zero records match today; that is a property of the current seed list and not of
    the pipeline, which is why the check exists before something is added rather than after.
  - The injection patterns are deliberately conservative. "The system prompt is loaded at
    startup", "you should pin a version", "Runs any tool call you give it" and "Invoke the
    function directly from Python" are ordinary technical prose and are not flagged; a check that
    cries wolf on the corpus it protects gets disabled within a month.
  - `build_index.py` escapes only the two entry kinds whose text originates upstream
    (`repository`, `mcp`). All 11 other kinds are authored here: escaping them would have
    changed 11 workflow summaries that are already correct, for no safety gain.
  - `SECURITY.md` gains an "Ingested text is untrusted input" section. The policy previously did
    not mention ingestion at all.
  - 48 regression tests in `tests/test_untrusted_text.py`, mutation-checked ten ways. Two of the
    mutations initially slipped through — removing the generator's call to `untrusted()` left
    the suite green, because the assertions read the already-generated cards from disk. Tests
    that only read committed output cannot catch the wiring being undone, so the description,
    homepage and framing are now also asserted by rendering through the generator itself.

### License policy reaches the markdown

- **H-5 — the license "hard override" was enforced only as a warning, and only on code files.**
  The override itself was always correct in the data: all 15 no-license records carried
  `license_risk: no-license-do-not-redistribute` and all 57 `NOASSERTION` records carried
  `custom-license-review-before-vendoring`. The enforcement was broken in two opposite
  directions at once. It was **under-inclusive**: it scanned only `.ts/.tsx/.js/.py/.go/.rs`,
  while the realistic vendoring target in this repository is a *markdown article* copying prose
  or a skill from `anthropics/skills` or `openai/skills` — markdown was never looked at. And it
  was **over-inclusive**: it matched the repository *name* alone rather than `owner/name`, so
  every script using the word "skills" was flagged for `openai/skills`. That produced most of
  the warnings in the policy output. A warning that is mostly noise is read once and then
  skipped, which is how a control quietly stops being one.
  - **Matching is now whole-slug**, boundary-anchored. The bare-name match is gone, and the six
    warnings it produced on test files are gone with it.
  - **Markdown is scanned.** Two severities, because they are two different situations: a
    *mention* of a repository whose license carries a consequence is a warning (naming
    `anthropics/skills` in order to say "do not copy this" is legitimate and necessary); a
    mention **attributed to a long code fence** is an error. Attribution means the slug appears
    inside the fence — the way a copied header comment survives — or in the prose immediately
    around it, the way "adapted from X" is actually written.
  - **Proximity alone is not treated as evidence of copying.** The first implementation
    (slug within 40 lines of a 15-line fence) accused seven files on the committed corpus, and
    all seven were innocent: `skills/database-design/SKILL.md` mentions `pgvector/pgvector` in
    one paragraph and carries its own original modelling rules 30 lines away, and
    `knowledge/agent-skills/skill-format.md` names `anthropics/skills` inside the block that
    states its authoring rules — rule 4 of which is *"Never copy external content."* Failing
    the build over the sentence that enforces the policy would remove the incentive to write
    it. Prose fences (```text`, this repository's house style for authored prose) are not
    candidates, and a passage stating the no-copy rule is treated as compliance.
  - **The mention warning is exempted only where naming repositories is the file's job** —
    `scripts/`, `tests/`, `metadata/`, `indexes/`, `repositories/`, `CHANGELOG.md`,
    `REVIEW-REPORT.md`. Warnings fell from 133 to 34 while coverage of prose *widened*. The
    vendoring error applies to every path without exception, so the exemption cannot hide
    copied content: a generator script that pasted 20 lines out of a no-license repository is
    the worst case, not the mildest.
- **The policy now reaches the cards, which it never did.** None of the 72 generated repository
  cards carried the license marker: the consequence lived in `metadata/repositories.json`,
  which is not what a human or an agent reads. This was not in the review's description of H-5
  and was found while enforcing it.
  - `generate_repository_cards.py` emits `license_risk` into the card frontmatter (new optional
    field on the `sourceRef` definition in `schemas/common.defs.json`, enum-constrained) and a
    **banner above the fold** stating the consequence in plain terms — "reference and link
    only" for no-license, "read the upstream LICENSE before vendoring" for `NOASSERTION`. All
    414 cards regenerated; the only change to the 342 cleanly-licensed ones is the added
    frontmatter field.
  - `check_cards_state_license_policy()` fails the build if a risky repository's card is
    missing, or carries the marker in frontmatter but not in readable prose, or vice versa.
    Machine-parseable is not the point of a card.
- **Orphan card found and removed, with a check so it cannot recur.**
  `repositories/developer-tools/firebase--firebase-tools.md` had survived since v1.0.0
  (`7b7b829`) after the repository was reclassified to `mcp-servers`. Two cards for one
  repository, with conflicting `domain` and `tags`, the stale one carrying no license marker and
  a `verified_at` a day behind. Nothing detected it because nothing compared the cards on disk
  to the registry. `check_no_orphan_cards()` now does, as an error.
- 32 regression tests in `tests/test_license_policy.py`, mutation-checked eight ways: removing
  either false-positive exemption, demoting vendoring to a warning, removing either half of the
  card-marker check, reverting to name-only matching, emptying the exemption list, or neutering
  the orphan check each turn the suite red. An earlier draft had a second "relevant paths"
  filter that silently excluded `README.md` to save three warnings; removing it left every
  other test green, which is how the gap was found — the filter is gone and `README.md` is
  covered.

### Security and exclusion decisions

- **H-4 — SECURITY.md's hard exclusions were unenforced.** The policy prose claimed the
  exclusions were mechanical and listed five things `validate_policy.py` did about them. Three
  of the five did not exist: there was no exclusion list anywhere in the codebase, no check
  consulted one, and `fetch_github_metadata.py` would have fetched an excluded repository on
  request. The two documented exclusions held only because nobody had seeded them — a
  contributor adding `asgeirtj/system_prompts_leaks` (~67,100 stars) in good faith would have
  passed every gate that existed, since it fetches fine, scores S-tier on stars, and has a
  license. That is precisely the drift the policy was written to prevent, which is why it
  records exclusions rather than omitting them silently.
  - `metadata/excluded-sources.json` is now the machine-readable form of the decision: two
    exclusion records plus two content patterns, validated by
    `schemas/excluded-source.schema.json`. It is **authored policy data, not a generated
    artifact**, and says so in the file.
  - `scripts/lib/exclusions.py` is the single source of truth both the validator and the
    fetcher read, so they cannot drift apart. Matching is whole-slug (`owner/name`), never the
    bare repository name: `prompts`, `leaks` and `registry` are ordinary words, and an
    exclusion list that implicates unrelated files gets edited around.
  - `validate_policy.py` check 6 fails on: an unusable or empty exclusion list (an
    unenforceable exclusion is the defect, so it is an error rather than a pass over nothing);
    an excluded slug on any ingestion or retrieval path — the seed lists, the registries,
    `indexes/`, or a `sources:` block — where **no wording excuses it**, because a seed entry
    *is* collection; an excluded slug named in prose outside a paragraph that states the
    exclusion; and a governed `.md` whose `sources:` cites one. The policy documents and the
    CHANGELOG may name them, since naming is how a contributor avoids rediscovering a gap.
  - `fetch_github_metadata.py` refuses before requesting, both for seed-list entries and for an
    explicit `--slug` (exit 2 with the reason). Refusing rather than discarding afterwards
    matters: a completed fetch leaves the upstream payload in `.cache/gh/`, so rejecting the
    record post hoc would still have collected the content.
  - 37 regression tests in `tests/test_exclusions.py`, mutation-checked: degrading `slug_in` to
    a substring match, widening the passage check to file scope, making ingestion paths
    unrecognised, or removing the fetch refusal each turn the suite red.
  - The Enforcement section of `excluded-sources.md` was rewritten to describe what the code
    actually does. Two of its five claims were true, three were not.

- **Pre-existing CI break found while validating H-4 (not caused by it).** `validate_links.py`
  failed at `a7dc7ea` and had done since `58dff2e`: README.md said "Every skill has
  `tests/cases.md`", and the prose-path check resolved that against the repository root, where
  no such file exists — the real path is per-skill. Fixed both sides rather than exempting it:
  the README now names `skills/<skill>/tests/cases.md`, and a new check asserts the claim the
  sentence makes, which nothing enforced before. All 50 skill directories are now verified to
  have generated cases, and removing any one of them fails the build.


- Two high-popularity repositories were **excluded from ingestion by policy**, not by score:
  `asgeirtj/system_prompts_leaks` (≈67,100 stars) and `elder-plinius/CL4R1T4S` (≈49,900 stars).
  Both distribute leaked or extracted system prompts. They are recorded as explicit exclusions in
  `SECURITY.md` and in `knowledge/security/llm-security/excluded-sources.md`, and must never be
  vendored, summarised in detail, or treated as evidence.
- The exclusion is recorded rather than the repositories being omitted silently, so that a later
  contributor does not rediscover them and add them in good faith.
- No private, stolen or improperly obtained model internals are present anywhere in this repository.
  All research content derives from public, legally obtainable sources.
- A GitHub personal access token pasted into the build conversation was **not** used, stored or
  written into any file, environment variable or git configuration. All metadata was fetched with the
  sandbox's own credentials. The user was advised to revoke it.

### Verification notes

- Star counts, licenses, archival status and push dates were read from the GitHub REST API on
  2026-09-15 and are accurate as of that date. Approximately 1,900 API responses are cached under
  `.cache/gh/` so that the corpus can be re-audited against the exact data it was built from.
- `EleutherAI/OpenAgentSafety` was checked and **does not exist** on GitHub (404). It is recorded as
  absent rather than listed as unverified.
- The GAIA benchmark was checked and is **not hosted on GitHub**; it lives on Hugging Face. It is
  therefore not in the repository database, which covers GitHub-hosted projects.
- `export.arxiv.org/api/query` was unreachable from the build environment by both HTTP client and
  page fetch, so batch paper verification was not possible. Papers were verified individually against
  `arxiv.org/abs/` pages, which is why only 9 are published as verified and 61 remain quarantined.
- OpenAlex returned incorrect titles for some arXiv DOIs and is **not trusted without cross-check**.
  Where sources disagree, the primary source wins and the conflict is recorded.

### Known gaps at release

Recorded rather than hidden, per the repository's own policy on unstated gaps:

- `patterns/` holds 1 pattern. The taxonomy and the template exist; the corpus does not. Domains with
  empty pattern directories: frontend, backend, database, mcp, security, architecture, animation,
  testing, ui, data.
- `anti-patterns/`, `failure-modes/` and `gotchas/` are scaffolded but empty. Failure modes are
  currently documented inside each skill and workflow rather than as standalone records.
- `evaluations/`, `datasets/` and `models/` are scaffolded but empty. The 40-task evaluation suite
  described in the README is specified but not yet built.
- `prompts/` holds 2 prompts across 9 categories. Seven categories are scaffolded and empty.
- `experimental/` and `research-archive/` are scaffolded but empty.
- 7 validation warnings remain, all of the class "reference file with `confidence: high` and no
  `sources[]`". These are deliberately uncorrected rather than silently downgraded: each needs either
  a citation or a confidence reduction decided by a human, not a script.
- Identity distinctiveness on the dashboard example scores 3/5 by design; removing slop produces a
  competent neutral interface, and a distinctive identity is a separate act of design that was not
  attempted.

### Schema changes made during the build

Recorded because they change what content is expressible, and because two of them were made to fit
structured content rather than to loosen a constraint:

- `agent.schema.json` — added `version`, `estimated_tokens`, `handoff_contract`, `quality_gates`
  (string **or** structured object with `gate`/`checked_by`/`on_failure`), `refusal_conditions`,
  `escalation`, `related_skills`, `related_repositories`, `supersedes`, `superseded_by` and
  `sections`.
- `workflow.schema.json` — added `estimated_tokens`, `estimated_duration`, `claim_type`,
  `evidence_level`, `related_skills`, `related_repositories`, `supersedes`, `superseded_by` and
  `sections`; widened `quality_gates` and `artifacts` to accept structured objects alongside strings.
- `pattern.schema.json` — added `version`, bringing it in line with every other content schema.

Each change was made because the structured form carries information a plain string cannot — who
checks a gate, and what happens when it fails — and each preserves the original string form so that
existing content stays valid.

---

## Versioning policy

| Change | Version bump |
|---|---|
| A field removed or renamed in any schema; a policy reversed | **major** |
| A new schema field, content type, skill, workflow, agent or domain | **minor** |
| Re-verification, metadata refresh, corrected claim, fixed link, typo | **patch** |

Metadata refreshes are expected to be frequent and are always patch-level: re-running
`fetch_github_metadata.py` changes star counts and push dates, which changes scores and tiers, and
none of that is a content decision.

[1.0.0]: https://github.com/tardigradsoftware-design/havuz-2/releases/tag/v1.0.0
