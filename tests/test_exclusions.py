#!/usr/bin/env python3
"""H-4 regression: SECURITY.md's hard exclusions are enforced by code, not by nobody having added them.

`SECURITY.md` declares a list of things this repository will never collect, and
`knowledge/security/llm-security/excluded-sources.md` names two high-popularity repositories as
excluded under it — `asgeirtj/system_prompts_leaks` (~67,100 stars) and `elder-plinius/CL4R1T4S`
(~49,900 stars). The prose said "the policy is mechanical, not aspirational" and listed five
things `validate_policy.py` supposedly did about it. Three of the five did not exist: there was
no exclusion list anywhere in the codebase, no check consulted one, and
`fetch_github_metadata.py` would have fetched either repository on request.

The exclusions held only because nobody had seeded them. That is exactly the failure mode the
policy documents anticipate — the reason an exclusion is *recorded* rather than silently omitted
is so a later contributor does not rediscover a popular repository and add it in good faith. Such
a contribution would have passed every gate that existed: it fetches fine, it scores S-tier on
stars, and it has a license.

Run: python3 -m unittest tests.test_exclusions -v
"""
from __future__ import annotations

import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    # Registered before execution: frontmatter.py builds dataclasses, and dataclass
    # processing looks the defining module up in sys.modules. Without this the import
    # fails with "'NoneType' object has no attribute '__dict__'" rather than loading.
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


excl = load("exclusions_lib", "scripts/lib/exclusions.py")
vp = load("validate_policy", "scripts/validate/validate_policy.py")
fetcher = load("fetch_github_metadata", "scripts/update/fetch_github_metadata.py")
fm = load("frontmatter_lib", "scripts/lib/frontmatter.py")

POLICY = ROOT / "metadata" / "excluded-sources.json"
SCHEMA = ROOT / "schemas" / "excluded-source.schema.json"
PROSE = ROOT / "knowledge" / "security" / "llm-security" / "excluded-sources.md"

# The two repositories the prose names. Hard-coded on purpose: these tests exist to catch the
# data drifting away from the documented decision, so they must not read the decision from the
# file whose correctness is in question.
DOCUMENTED = ("asgeirtj/system_prompts_leaks", "elder-plinius/CL4R1T4S")


def committed():
    """The exclusion list as committed."""
    return excl.load_exclusions()


def made(records=None, patterns=None, load_error=None):
    """A synthetic exclusion list, so a test never has to edit the committed policy."""
    return excl.Exclusions(
        {"exclusions": records if records is not None else [],
         "content_patterns": patterns or []},
        load_error=load_error)


def a_record(slug="acme/leaked", **over):
    rec = {"slug": slug, "kind": "github-repository",
           "category": "leaked-system-prompts", "reason": "distributes extracted system prompts",
           "decision": "never ingest, never summarise, never redistribute",
           "decided_on": "2026-09-15", "observed_stars": 1000,
           "prohibits": ["ingestion"], "permitted_mentions": ["this policy document"],
           "documented_in": "knowledge/security/llm-security/excluded-sources.md"}
    rec.update(over)
    return rec


class PolicyDataIsUsable(unittest.TestCase):
    """Failure 1 in check_exclusions: an unusable list means every exclusion is unenforced."""

    def test_the_committed_list_loads_without_error(self):
        e = committed()
        self.assertIsNone(e.load_error)
        self.assertFalse(e.is_empty())

    def test_the_committed_list_is_schema_valid(self):
        """Resolved through the same store validate_json.py uses, because the schema $refs
        common.defs.json and a bare validate() cannot follow it."""
        if not hasattr(fm, "jsonschema"):
            self.skipTest("jsonschema not installed")
        schema = fm.load_schema("excluded-source.schema.json")
        store = {}
        for f in (ROOT / "schemas").glob("*.json"):
            s = json.loads(f.read_text())
            if "$id" in s:
                store[s["$id"]] = s
            store[f.name] = s
        resolver = fm.RefResolver(base_uri=f"file://{ROOT/'schemas'}/", referrer=schema, store=store)
        validator = fm.jsonschema.Draft202012Validator(schema, resolver=resolver)
        records = json.loads(POLICY.read_text())["exclusions"]
        self.assertTrue(records)
        for rec in records:
            errs = list(validator.iter_errors(rec))
            self.assertEqual([], [e.message for e in errs], f"{rec.get('slug')} is schema-invalid")

    def test_the_data_names_exactly_what_the_prose_decided(self):
        """The prose is the decision; the data is its enforcement. Drift in either direction
        leaves an exclusion documented but unenforced, or enforced but undocumented."""
        self.assertEqual(sorted(DOCUMENTED), sorted(committed().slugs))
        prose = PROSE.read_text()
        for slug in committed().slugs:
            self.assertIn(slug, prose, f"{slug} is enforced but not documented in the policy prose")

    def test_a_missing_policy_file_is_an_error_not_a_silent_pass(self):
        e = excl.Exclusions.load(ROOT / "metadata" / "does-not-exist.json")
        self.assertTrue(e.load_error)
        errs, _ = vp.check_exclusions([], e)
        self.assertTrue(any("exclusion policy" in x for x in errs))

    def test_a_malformed_policy_file_is_an_error(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            bad = tmp / "excluded-sources.json"
            bad.write_text("{ not json")
            errs, _ = vp.check_exclusions([], excl.Exclusions.load(bad))
            self.assertTrue(any("not valid JSON" in x for x in errs))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_an_empty_list_is_an_error_because_security_md_declares_exclusions(self):
        """Satisfying a hard exclusion by declaring nothing is the same as not enforcing it."""
        errs, _ = vp.check_exclusions([], made([]))
        self.assertTrue(any("declares no exclusions" in x for x in errs))

    def test_a_bad_content_pattern_is_reported(self):
        e = made(patterns=[{"id": "broken", "pattern": "([unclosed"}])
        self.assertTrue(e.load_error and "bad pattern" in e.load_error)


class MatchingIsWholeSlug(unittest.TestCase):
    """An exclusion that implicates unrelated text gets ignored, so matching has to be narrow."""

    def setUp(self):
        self.e = committed()

    def test_the_exact_slug_is_found(self):
        for slug in DOCUMENTED:
            self.assertEqual([slug], self.e.slug_in(f"see {slug} for details"))

    def test_matching_is_case_insensitive_on_owner_and_name(self):
        self.assertEqual(["asgeirtj/system_prompts_leaks"],
                         self.e.slug_in("AsgeirTJ/System_Prompts_Leaks"))

    def test_a_repository_whose_name_merely_ends_with_an_excluded_name_is_not_implicated(self):
        """The regression the review asked for. `registry` and `prompts` are ordinary words;
        a substring test would implicate every file that uses them."""
        for near in ("someone-else/system_prompts_leaks",
                     "asgeirtj/system_prompts_leaks_v2",
                     "myorg/CL4R1T4S",
                     "prefix-elder-plinius/CL4R1T4S"):
            self.assertEqual([], self.e.slug_in(near), f"{near} was falsely implicated")

    def test_ordinary_prose_about_the_topic_is_not_a_hit(self):
        """The policy forbids the collections, not discussing the subject. A validator that
        flagged honest security prose would be edited around within a week."""
        for prose in ("leaked system prompts are a real risk",
                      "system prompts are not collected here",
                      "extracted prompts of commercial assistants",
                      "we refuse to redistribute system prompt collections"):
            self.assertEqual([], self.e.slug_in(prose))
            self.assertEqual([], self.e.pattern_hits(prose))

    def test_the_collection_identifiers_themselves_are_matched_as_content(self):
        """Identifiers are matched separately from slugs, because a mirror may rename the
        owner while keeping the collection's own name."""
        for text in ("asgeirtj/system_prompts_leaks", "the system_prompts_leaks archive",
                     "CL4R1T4S"):
            self.assertTrue(self.e.pattern_hits(text), f"identifier missed in {text!r}")


class PassageWordingIsParagraphScoped(unittest.TestCase):
    """Naming an excluded source is legitimate — invisibility is not. But the wording has to be
    in the passage that names it, not somewhere else in the file."""

    def setUp(self):
        self.e = committed()
        self.slug = DOCUMENTED[0]

    def test_a_passage_that_states_the_exclusion_is_accepted(self):
        text = (f"Note on {self.slug}: this repository is excluded from ingestion by policy and "
                f"must never be vendored or cited as evidence.\n")
        self.assertTrue(self.e.passage_states_exclusion(text, self.slug))

    def test_a_passage_that_recommends_it_is_rejected(self):
        text = f"For prompt examples, see {self.slug} — it has 67,000 stars and is well maintained.\n"
        self.assertFalse(self.e.passage_states_exclusion(text, self.slug))

    def test_exclusion_wording_elsewhere_in_the_file_does_not_excuse_a_recommending_passage(self):
        """Paragraph scope is the whole point. File scope would let a document carry the word
        'excluded' in one section and recommend the source in another."""
        text = ("## Exclusions\n\nLeaked prompt collections are excluded from ingestion here.\n\n"
                "## Recommended reading\n\n"
                f"Start with {self.slug}, which is comprehensive and frequently updated.\n")
        other = text.split("## Recommended reading")[0]
        self.assertTrue(self.e.passage_states_exclusion(other, "Leaked prompt collections"),
                        "test premise: the first paragraph really does state an exclusion")
        self.assertNotIn(self.slug, other, "test premise: the slug is only in the second paragraph")
        self.assertFalse(self.e.passage_states_exclusion(text, self.slug))

    def test_wording_inside_a_code_span_does_not_count(self):
        """The statement has to be prose. `excluded` as a filename or a field name is not a
        claim about policy."""
        text = f"Use {self.slug} and set `excluded: false` in the config.\n"
        self.assertFalse(self.e.passage_states_exclusion(text, self.slug))


class IngestionPathsGetNoWordingExcuse(unittest.TestCase):
    """A seed entry or a registry record *is* collection, whatever the prose around it says."""

    def setUp(self):
        self.e = made([a_record("acme/leaked-prompts")])
        self.slug = "acme/leaked-prompts"
        # Wording that would excuse the slug in prose. On an ingestion path it must not.
        self.excusing = (f"{self.slug} is excluded from ingestion by policy and must never be "
                         f"collected.\n")

    def test_the_ingestion_paths_are_the_seed_lists_and_the_registries(self):
        for rel in ("scripts/update/seeds.json", "metadata/repositories.json",
                    "metadata/tools.json", "metadata/index.json", "indexes/mcp.md",
                    "repositories/acme/thing.md", "sources/papers.md"):
            self.assertTrue(self.e.is_ingestion_path(rel), f"{rel} should be an ingestion path")
        for rel in ("README.md", "CHANGELOG.md", "knowledge/security/supply-chain.md",
                    "scripts/lib/exclusions.py"):
            self.assertFalse(self.e.is_ingestion_path(rel), f"{rel} is prose, not ingestion")

    def test_an_excluded_slug_in_a_seed_list_is_an_error_even_with_excusing_wording(self):
        with self._file("scripts/update/seeds.json", self.excusing) as f:
            errs, _ = vp.check_exclusions([f], self.e)
        self.assertTrue(any("ingestion or retrieval path" in x for x in errs), errs)

    def test_an_excluded_slug_in_prose_with_wording_is_accepted(self):
        with self._file("knowledge/security/supply-chain.md", self.excusing) as f:
            errs, warns = vp.check_exclusions([f], self.e)
        self.assertEqual([], errs)
        self.assertEqual([], warns)

    def test_an_excluded_slug_in_prose_without_wording_is_an_error(self):
        with self._file("knowledge/security/supply-chain.md",
                        f"For prompt corpora, {self.slug} is the largest available.\n") as f:
            errs, _ = vp.check_exclusions([f], self.e)
        self.assertTrue(any("does not state the exclusion" in x for x in errs), errs)

    def test_the_policy_document_itself_may_name_the_exclusions(self):
        """The allowlist is two files long and cannot grow into exempting the corpus."""
        for rel in excl.POLICY_FILES:
            self.assertTrue(self.e.is_policy_file(rel))
        with self._file("metadata/excluded-sources.json", self.slug) as f:
            errs, _ = vp.check_exclusions([f], self.e)
        self.assertEqual([], errs)

    def test_a_clean_file_produces_no_findings(self):
        with self._file("metadata/repositories.json", '{"repositories": []}\n') as f:
            errs, warns = vp.check_exclusions([f], self.e)
        self.assertEqual(([], []), (errs, warns))

    def test_a_content_pattern_on_an_ingestion_path_is_an_error(self):
        with self._file("scripts/update/seeds.json",
                        json.dumps({"seeds": [{"slug": "x/system_prompts_leaks"}]})) as f:
            errs, _ = vp.check_exclusions([f], committed())
        self.assertTrue(errs)

    def _file(self, rel: str, body: str):
        """Create `rel` under a scratch ROOT so no committed file is ever touched."""
        class _Ctx:
            def __enter__(inner):
                inner.tmp = Path(tempfile.mkdtemp())
                inner.root = inner.tmp
                p = inner.root / rel
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(body)
                inner._saved = vp.ROOT
                vp.ROOT = inner.root
                return p

            def __exit__(inner, *exc):
                vp.ROOT = inner._saved
                shutil.rmtree(inner.tmp, ignore_errors=True)
                return False
        return _Ctx()


class CitationsAreRejected(unittest.TestCase):
    """Failure 3: a `sources:` entry is an attribution of authority, which the policy prohibits."""

    def setUp(self):
        self.e = made([a_record(DOCUMENTED[0])])

    def _md(self, tmp: Path, sources_block: str) -> Path:
        p = tmp / "knowledge" / "x" / "SKILL.md"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("---\ntitle: T\n" + sources_block + "---\n\nBody.\n")
        return p

    def test_a_sources_entry_citing_an_excluded_repository_is_rejected(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            saved, vp.ROOT = vp.ROOT, tmp
            try:
                self._md(tmp, 'sources:\n  - repository: %s\n    title: Leaked\n' % DOCUMENTED[0])
                errs = vp.check_excluded_citations(self.e)
            finally:
                vp.ROOT = saved
            self.assertTrue(any("cites the excluded source" in x for x in errs), errs)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_a_url_pointing_at_an_excluded_repository_is_rejected(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            saved, vp.ROOT = vp.ROOT, tmp
            try:
                self._md(tmp, 'sources:\n  - url: https://github.com/%s\n    title: T\n'
                         % DOCUMENTED[0])
                errs = vp.check_excluded_citations(self.e)
            finally:
                vp.ROOT = saved
            self.assertTrue(errs)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_an_unrelated_source_is_accepted(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            saved, vp.ROOT = vp.ROOT, tmp
            try:
                self._md(tmp, 'sources:\n  - repository: torvalds/linux\n    title: Linux\n')
                errs = vp.check_excluded_citations(self.e)
            finally:
                vp.ROOT = saved
            self.assertEqual([], errs)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_an_empty_exclusion_list_cannot_reject_anything(self):
        """Guards the guard: if the list fails to load, citation checking must not silently
        pass. check_exclusions reports the empty list as its own error, tested above."""
        self.assertEqual([], vp.check_excluded_citations(made([])))


class FetchingIsRefused(unittest.TestCase):
    """Collection happens at fetch time. Filtering the record afterwards still leaves the
    upstream payload in `.cache/gh/`, so the boundary belongs before the request."""

    def setUp(self):
        self.e = committed()

    def test_fetch_refusal_names_the_decision_and_the_document(self):
        for slug in DOCUMENTED:
            r = self.e.fetch_refusal(slug)
            self.assertTrue(r, f"{slug} was not refused")
            self.assertIn(slug, r)
            self.assertIn("excluded-sources.md", r)

    def test_refusal_is_case_insensitive_and_tolerates_padding(self):
        self.assertTrue(self.e.fetch_refusal("  ASGEIRTJ/system_prompts_LEAKS "))

    def test_an_unrelated_slug_is_not_refused(self):
        for slug in ("torvalds/linux", "google/adk-python", "modelcontextprotocol/servers"):
            self.assertIsNone(self.e.fetch_refusal(slug))

    def test_a_lookalike_slug_is_not_refused(self):
        self.assertIsNone(self.e.fetch_refusal("someone-else/system_prompts_leaks"))

    def test_fetch_one_refuses_without_making_a_request(self):
        """`http_json` is the only network entry point in the fetcher. Replacing it with a
        sentinel that fails the test proves the refusal is decided before any request is
        issued — a refusal applied after fetching would still have collected the payload."""
        def no_network(*a, **k):
            self.fail("an excluded slug reached the network")
        saved, fetcher.http_json = fetcher.http_json, no_network
        try:
            for slug in DOCUMENTED:
                rec = fetcher.fetch_one({"slug": slug, "category": "mcp-servers"},
                                        tok=None, use_cache=False, excluded=self.e)
                self.assertFalse(rec["fetch_ok"])
                self.assertEqual("EXCLUDED_BY_COLLECTION_POLICY", rec.get("refused"))
                self.assertTrue(rec.get("refusal_reason"))
        finally:
            fetcher.http_json = saved

    def test_fetch_one_passes_a_permitted_slug_through_to_the_fetch(self):
        """The refusal must not have become a blanket failure — that would be indistinguishable
        from working, and would break every legitimate fetch. The sentinel records that the
        permitted slug did reach the network layer."""
        reached = []

        def sentinel(url, *a, **k):
            reached.append(url)
            raise RuntimeError("stop here; reaching the request is all this test needs")

        saved, fetcher.http_json = fetcher.http_json, sentinel
        try:
            # fetch_one does not wrap the request, so the sentinel propagates. Reaching it at
            # all is the assertion: a permitted slug gets as far as the network layer.
            with self.assertRaises(RuntimeError):
                fetcher.fetch_one({"slug": "torvalds/linux", "category": "core"},
                                  tok="fake", use_cache=False, excluded=self.e)
        finally:
            fetcher.http_json = saved
        self.assertTrue(reached, "a permitted slug never reached the fetch layer")

    def test_the_fetcher_consults_the_committed_policy_at_import(self):
        """Both the argument pre-check and the fetch loop must read the same list, or they can
        disagree about what is excluded."""
        self.assertIsNone(fetcher._EXCLUSIONS.load_error)
        self.assertEqual(sorted(DOCUMENTED), sorted(fetcher._EXCLUSIONS.slugs))


class TheCommittedCorpusIsClean(unittest.TestCase):
    """The checks above prove the controls fire. This proves the repository satisfies them."""

    def test_no_tracked_file_violates_the_exclusions(self):
        e = committed()
        errs, warns = vp.check_exclusions(vp.tracked_files(), e)
        self.assertEqual([], errs, "\n".join(errs[:5]))

    def test_no_artifact_cites_an_excluded_source(self):
        self.assertEqual([], vp.check_excluded_citations(committed()))

    def test_the_exclusions_are_absent_from_the_seed_list_and_the_registries(self):
        """The state the policy was relying on before H-4 — now asserted rather than assumed."""
        for rel, key in (("scripts/update/seeds.json", "seeds"),
                         ("metadata/repositories.json", "repositories"),
                         ("metadata/tools.json", "tools")):
            data = json.loads((ROOT / rel).read_text())
            blob = json.dumps(data).lower()
            for slug in DOCUMENTED:
                self.assertNotIn(slug.lower(), blob, f"{slug} appears in {rel}")
            self.assertTrue(data.get(key), f"{rel} is unexpectedly empty")


if __name__ == "__main__":
    unittest.main(verbosity=2)
