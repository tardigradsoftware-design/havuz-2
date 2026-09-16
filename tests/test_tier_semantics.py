#!/usr/bin/env python3
"""H-3 regression: a tier label must mean what its name says.

`UNVERIFIED` is an epistemic claim — the record could not be checked against its source.
`NO-LICENSE` is a legal one — the record was checked and no license was published. The
scoring model used to return `UNVERIFIED` for the license case, so all 15 records in that
tier carried `fetch_ok: true` while being labelled as though their metadata were
untrustworthy, and the tier spanned scores 4.02–8.02 — it contained `vercel/mcp-handler`
at 8.02, above the S threshold, labelled UNVERIFIED.

The documentation had it right all along: `knowledge/ai-engineering/source-scoring.md`
defined UNVERIFIED as "could not be verified" and mapped only "unresolvable / 404" to it.
The code disagreed with the documentation, which is the shape these tests now lock down.

Run: python3 -m unittest tests.test_tier_semantics -v
"""
from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from lib.scoring import tier_for  # noqa: E402


def load(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


vj = load("vj", "scripts/validate/validate_json.py")

REPOS = ROOT / "metadata" / "repositories.json"
SCHEMA = ROOT / "schemas" / "common.defs.json"

# Tiers the score alone decides, so a missing license must override them. Taken from the
# validator rather than restated here, so the two cannot drift apart.
SCORE_BANDS = vj.SCORE_BAND_TIERS
STATUS_TIERS = ("ARCHIVED", "NO-LICENSE", "UNVERIFIED", "DEPRECATED")


class TestTierForSeparatesTheTwoMeanings(unittest.TestCase):
    """The mapping itself: one label per fact, and neither standing in for the other."""

    def test_no_license_is_its_own_tier(self):
        self.assertEqual("NO-LICENSE", tier_for(9.5, license_ok=False))

    def test_failed_fetch_is_unverified(self):
        self.assertEqual("UNVERIFIED", tier_for(9.5, fetch_ok=False))

    def test_unverified_is_never_returned_for_a_license_problem(self):
        """The original defect, stated as an invariant rather than as a value."""
        self.assertNotEqual("UNVERIFIED", tier_for(9.5, license_ok=False))
        self.assertNotEqual("UNVERIFIED", tier_for(2.0, license_ok=False))

    def test_no_license_is_never_returned_for_a_fetch_problem(self):
        self.assertNotEqual("NO-LICENSE", tier_for(9.5, fetch_ok=False))

    def test_fetch_failure_outranks_every_other_override(self):
        """If the metadata could not be fetched, the other flags are stale repetitions of
        old data, not observations — so nothing else may claim to describe the record."""
        for kwargs in ({"archived": True}, {"license_ok": False},
                       {"archived": True, "license_ok": False},
                       {"archived": True, "license_ok": False, "nonstandard": True}):
            with self.subTest(**kwargs):
                self.assertEqual("UNVERIFIED", tier_for(9.5, fetch_ok=False, **kwargs))

    def test_archived_still_outranks_a_missing_license(self):
        """Precedence below UNVERIFIED is unchanged: an archived repository is frozen
        whether or not it has a license, and that is the more actionable fact."""
        self.assertEqual("ARCHIVED", tier_for(9.5, archived=True, license_ok=False))

    def test_no_license_outranks_the_score_band(self):
        """The case the old label obscured: 8.02 is above the S threshold, and the record
        still must not be presented as an adoption candidate."""
        for score in (4.02, 6.0, 8.0, 8.02, 9.3):
            with self.subTest(score=score):
                self.assertEqual("NO-LICENSE", tier_for(score, license_ok=False))

    def test_score_bands_are_unaffected_by_the_rename(self):
        """The rename must not move a single correctly-tiered record."""
        self.assertEqual("S", tier_for(9.5))
        self.assertEqual("S", tier_for(8.0))
        self.assertEqual("A", tier_for(7.0))
        self.assertEqual("B", tier_for(5.8))
        self.assertEqual("C", tier_for(4.3))
        self.assertEqual("EXPERIMENTAL", tier_for(4.29))

    def test_custom_license_still_caps_at_a(self):
        """NOASSERTION is a license, just not an SPDX-recognised one. Capping at A is the
        existing rule and the rename must not disturb it — this is the distinction a
        naive `license is null` check gets wrong."""
        self.assertEqual("A", tier_for(9.5, nonstandard=True))
        self.assertNotEqual("NO-LICENSE", tier_for(9.5, nonstandard=True))


class TestSchemaDeclaresBothTiers(unittest.TestCase):
    def test_both_labels_are_in_the_tier_enum(self):
        enum = json.loads(SCHEMA.read_text())["$defs"]["tier"]["enum"]
        self.assertIn("NO-LICENSE", enum)
        self.assertIn("UNVERIFIED", enum,
                      "UNVERIFIED must stay in the vocabulary: it is the correct label for "
                      "a record whose fetch failed, which is a state the corpus can be in")

    def test_the_enum_documents_the_difference(self):
        """A future contributor should not have to rediscover this from a bug report."""
        desc = json.loads(SCHEMA.read_text())["$defs"]["tier"].get("description", "")
        self.assertIn("NO-LICENSE", desc)
        self.assertIn("UNVERIFIED", desc)
        self.assertRegex(desc.lower(), r"could not be verified|could not verify")

    def test_readme_states_the_override_precedence(self):
        text = (ROOT / "README.md").read_text()
        self.assertIn("NO-LICENSE", text)
        self.assertRegex(text, r"`UNVERIFIED` if the GitHub fetch failed")

    def test_scoring_documentation_agrees_with_the_code(self):
        """The mismatch that made this defect possible was between prose and code."""
        doc = (ROOT / "knowledge" / "ai-engineering" / "source-scoring.md").read_text()
        self.assertIn("`NO-LICENSE`", doc)
        self.assertRegex(doc, r"unresolvable / 404\s+→ tier = UNVERIFIED")
        self.assertRegex(doc, r"license: null\s+→[^\n]*\n\s+tier = NO-LICENSE")


class TestCommittedCorpusHonoursTheLabels(unittest.TestCase):
    def setUp(self):
        self.recs = json.loads(REPOS.read_text())["repositories"]

    def test_no_record_is_unverified_while_its_fetch_succeeded(self):
        bad = [r["slug"] for r in self.recs
               if r.get("tier") == "UNVERIFIED" and r.get("fetch_ok") is True]
        self.assertEqual([], bad)

    def test_every_unlicensed_record_is_in_the_no_license_tier(self):
        bad = [r["slug"] for r in self.recs
               if r.get("license_risk") == "no-license-do-not-redistribute"
               and r.get("tier") != "NO-LICENSE"]
        self.assertEqual([], bad, "an unlicensed record sits in a tier that invites adoption")

    def test_no_license_tier_contains_only_unlicensed_records(self):
        bad = [r["slug"] for r in self.recs
               if r.get("tier") == "NO-LICENSE"
               and r.get("license_risk") != "no-license-do-not-redistribute"]
        self.assertEqual([], bad, "a licensed record is marked legally unsafe to redistribute")

    def test_no_score_band_contains_an_unlicensed_record(self):
        bad = [(r["slug"], r["tier"]) for r in self.recs
               if r.get("tier") in SCORE_BANDS
               and r.get("license_risk") == "no-license-do-not-redistribute"]
        self.assertEqual([], bad)

    def test_custom_licensed_records_are_not_accused_of_having_no_license(self):
        """NOASSERTION records belong in a score band, capped at A. They must not be swept
        into NO-LICENSE by a check that cannot tell the two apart."""
        custom = [r for r in self.recs if r.get("license") == "NOASSERTION"]
        self.assertTrue(custom, "corpus has no NOASSERTION record; test has lost its subject")
        self.assertEqual([], [r["slug"] for r in custom if r.get("tier") == "NO-LICENSE"])
        self.assertEqual([], [r["slug"] for r in custom if r.get("tier") == "S"],
                         "a custom license must cap the tier at A")

    def test_validator_reports_the_committed_corpus_clean(self):
        errs = []
        for i, r in enumerate(self.recs):
            errs += vj.tier_semantics_errors(r, "metadata/repositories.json", i, "slug")
        self.assertEqual([], errs)

    def test_generated_registries_are_clean_too(self):
        """The tier is copied into tools.json and index.json; a stale copy there would
        keep asserting the old meaning after the source was fixed."""
        for rel, listkey in (("metadata/tools.json", "tools"),):
            recs = json.loads((ROOT / rel).read_text())[listkey]
            errs = []
            for i, r in enumerate(recs):
                errs += vj.tier_semantics_errors(r, rel, i, "id")
            self.assertEqual([], errs, f"{rel} carries a tier its own facts contradict")


class TestValidatorCatchesTheDefect(unittest.TestCase):
    """Negative cases: each way the two labels can be confused must be an error."""

    def check(self, rec):
        return vj.tier_semantics_errors(rec, "t.json", 0, "slug")

    def test_original_defect_unverified_with_a_successful_fetch(self):
        errs = self.check({"tier": "UNVERIFIED", "fetch_ok": True, "license": "NONE",
                           "license_risk": "no-license-do-not-redistribute"})
        self.assertEqual(1, len(errs))
        self.assertIn("fetch_ok is true", errs[0])

    def test_unlicensed_record_promoted_into_a_score_band(self):
        for tier in SCORE_BANDS:
            with self.subTest(tier=tier):
                errs = self.check({"tier": tier, "fetch_ok": True, "license": "NONE",
                                   "license_risk": "no-license-do-not-redistribute"})
                self.assertTrue(errs)
                self.assertIn("expected NO-LICENSE", errs[0])

    def test_no_license_claimed_for_a_licensed_record(self):
        errs = self.check({"tier": "NO-LICENSE", "fetch_ok": True, "license": "MIT",
                           "license_risk": "none"})
        self.assertTrue(errs)
        self.assertIn("'MIT'", errs[0])

    def test_no_license_claimed_without_a_successful_fetch(self):
        errs = self.check({"tier": "NO-LICENSE", "fetch_ok": False})
        self.assertTrue(errs)
        self.assertIn("cannot claim to have verified", errs[0])

    def test_correct_records_are_left_alone(self):
        for rec in ({"tier": "NO-LICENSE", "fetch_ok": True, "license": "NONE",
                     "license_risk": "no-license-do-not-redistribute"},
                    {"tier": "UNVERIFIED", "fetch_ok": False},
                    {"tier": "S", "fetch_ok": True, "license": "MIT", "license_risk": "none"},
                    {"tier": "ARCHIVED", "fetch_ok": True, "license": "Apache-2.0"},
                    {"tier": "A", "fetch_ok": True, "license": "NOASSERTION",
                     "license_risk": "custom-license-review-before-vendoring"}):
            with self.subTest(tier=rec["tier"], license=rec.get("license")):
                self.assertEqual([], self.check(rec))

    def test_a_null_license_alone_is_not_treated_as_absence(self):
        """`license: null` is ambiguous: tools.json collapses NONE and NOASSERTION into it.
        Reading null as "no license" produced six false errors on correctly-tiered entries
        while this test's subject was being written."""
        self.assertEqual([], self.check({"tier": "A", "license": None,
                                         "license_risk": "custom-license-review-before-vendoring"}))
        self.assertEqual([], self.check({"tier": "A", "license": None, "license_risk": "none"}))

    def test_a_record_with_no_license_fields_at_all_is_not_accused(self):
        self.assertEqual([], self.check({"tier": "S"}))


class TestRetierIsOfflineAndMinimal(unittest.TestCase):
    """The migration path: changing a tier rule must not require re-fetching, and must not
    churn records the rule change does not affect."""

    def test_retier_mode_exists_and_needs_no_network(self):
        src = (ROOT / "scripts" / "update" / "fetch_github_metadata.py").read_text()
        self.assertIn("--retier", src)
        body = src[src.index("def retier("):src.index("\ndef main() -> int:")]
        self.assertNotIn("http_json", body, "retier must not call the API")
        self.assertIn("tier_for", body)

    def test_retier_derives_the_custom_license_cap_from_stored_data(self):
        """The fetcher does not persist the `signals` block, so `license_nonstandard` has
        to be re-derived from `license`. Skipping it silently promotes every NOASSERTION
        repository from A to S — the first version of --retier did exactly that, and
        reported 44 changes where 15 were correct."""
        body = (ROOT / "scripts" / "update" / "fetch_github_metadata.py").read_text()
        body = body[body.index("def retier("):body.index("\ndef main() -> int:")]
        self.assertIn("noassertion", body.lower())
        self.assertIn("nonstandard=nonstandard", body)

    def test_retier_is_idempotent_on_the_committed_corpus(self):
        """Re-running it must change nothing, or the registry would drift on every build."""
        import subprocess
        r = subprocess.run([sys.executable, "scripts/update/fetch_github_metadata.py",
                            "--retier", "--dry"], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(0, r.returncode, r.stderr)
        self.assertIn("changed: 0", r.stdout)

    def test_a_missing_tier_has_no_silent_default(self):
        """The registry generator used to fall back to `or "UNVERIFIED"`, which would
        reassert a fetch failure that never happened."""
        src = (ROOT / "scripts" / "generate-index" / "generate_mcp_registry.py").read_text()
        self.assertNotIn('or "UNVERIFIED"', src)


if __name__ == "__main__":
    unittest.main(verbosity=2)
