#!/usr/bin/env python3
"""Regression: the release-claims checker must actually check the claims it lists.

`scripts/validate/check_release_claims.py` exists because every count this repository publishes
about itself was correct only by hand. The README statistics block is generated, but the sentences
around it — in README.md, REVIEW-REPORT.md and CHANGELOG.md — restate numbers in prose, and prose
is where they go stale. Phase 6 found README reporting **50** skill test cases where the corpus
holds **1,108**: `update_readme_stats.py` counted `cases.md` files instead of `## Case N` headings.
The generated block and the prose disagreed, and the prose was right.

The important failure mode here is not a wrong number. It is a checker that looks green while
asserting nothing. The first version of this script labelled its README claims `"README"` while
keying its document map `"README.md"`, so every lookup missed, every claim was silently skipped,
and it reported success. A consistency checker that passes vacuously is worse than no checker,
because it is trusted. `test_every_required_claim_pattern_matches` is the guard against that
specific bug, and it is the reason the other tests can be believed.

Run: python3 -m unittest tests.test_release_claims -v
"""
from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts" / "validate" / "check_release_claims.py"


def load_checker():
    spec = importlib.util.spec_from_file_location("check_release_claims", CHECKER)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["check_release_claims"] = mod
    spec.loader.exec_module(mod)
    return mod


crc = load_checker()


def run_checker() -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(CHECKER), "--quiet"],
                          capture_output=True, text=True, cwd=str(ROOT))


class TestCheckerIsSound(unittest.TestCase):
    """The checker must fail on the committed corpus only if the corpus is wrong."""

    def test_passes_on_the_committed_corpus(self):
        r = run_checker()
        self.assertEqual(r.returncode, 0,
                         f"the committed tree fails its own release-claims check:\n{r.stdout}\n{r.stderr}")

    def test_stats_recompute_to_the_published_figures(self):
        """Guard the recomputation itself: if this is wrong, every comparison downstream is noise."""
        s = crc.corpus_stats()
        self.assertEqual(s["skill_test_cases"], 1108)
        self.assertEqual(s["skills"], 50)
        self.assertEqual(s["mcp_entries"], 35)
        self.assertEqual(s["mcp_servers"], 26)
        self.assertEqual(s["mcp_entries"] - s["mcp_servers"], 9)
        self.assertEqual(s["repositories"], 414)
        self.assertEqual(s["repository_cards"], 414)
        self.assertEqual(s["evaluation_records"], 0)
        self.assertEqual(s["tiers"].get("UNVERIFIED", 0), 0,
                         "this corpus has no fetch failures, so no record may be tier UNVERIFIED")

    def test_test_case_count_comes_from_headings_not_files(self):
        """The original bug: counting `cases.md` files (50) instead of the cases inside them (1108)."""
        files = sorted((ROOT / "skills").glob("*/tests/cases.md"))
        self.assertEqual(len(files), 50)
        headings = 0
        for f in files:
            headings += len(re.findall(r"(?m)^## Case \d+", f.read_text(encoding="utf-8")))
        self.assertEqual(headings, crc.corpus_stats()["skill_test_cases"],
                         "the checker and a direct heading count disagree — one of them is wrong")
        self.assertNotEqual(headings, len(files),
                            "if these are equal the statistic has collapsed back to counting files")


class TestNoVacuousPass(unittest.TestCase):
    """A required claim that stops matching must fail, never be skipped."""

    def test_every_required_claim_pattern_matches(self):
        """The `"README"` vs `"README.md"` regression.

        If a pattern stops matching — because a table row was renamed, a sentence reworded — the
        check has to fail. Skipping it means the checker silently narrows what it verifies until
        it verifies nothing, while still exiting 0.
        """
        s = crc.corpus_stats()
        unmatched = []
        for doc, pattern, _expected, required in crc.prose_claims(s):
            if not required:
                continue
            p = ROOT / doc
            self.assertTrue(p.exists(), f"{doc} is listed as a required claim source but is absent")
            if not re.search(pattern, p.read_text(encoding="utf-8", errors="replace")):
                unmatched.append(f"{doc}: /{pattern}/")
        self.assertEqual(unmatched, [],
                         "these required claims no longer match anything, so they are not being "
                         "checked at all:\n  " + "\n  ".join(unmatched))

    def test_claim_document_labels_resolve_against_real_files(self):
        """Every document a claim names must be a file that exists — the label-mismatch bug."""
        for doc, _pattern, _expected, _required in crc.prose_claims(crc.corpus_stats()):
            self.assertTrue((ROOT / doc).exists(),
                            f"claim names {doc!r} but no such file exists; a label that does not "
                            f"resolve makes every claim against it a silent no-op")

    def test_renaming_a_readme_row_fails_the_check(self):
        """Renaming a row changes no number, but it stops the claim being verified."""
        readme = ROOT / "README.md"
        original = readme.read_text(encoding="utf-8")
        mutated = original.replace("| Skill test cases | **1108** |", "| Skill cases | **1108** |", 1)
        self.assertNotEqual(mutated, original, "the mutation did not apply; the row was renamed")
        try:
            readme.write_text(mutated, encoding="utf-8")
            self.assertNotEqual(run_checker().returncode, 0,
                                "renaming a claimed table row must fail the check, not pass it")
        finally:
            readme.write_text(original, encoding="utf-8")


class TestStaleNumbersAreCaught(unittest.TestCase):
    """Each published figure is mutated to a stale value and must be detected."""

    def _assert_caught(self, find: str, replace: str, desc: str) -> None:
        readme = ROOT / "README.md"
        original = readme.read_text(encoding="utf-8")
        self.assertIn(find, original, f"mutation target for {desc} is absent from README.md")
        try:
            readme.write_text(original.replace(find, replace, 1), encoding="utf-8")
            r = run_checker()
            self.assertNotEqual(r.returncode, 0, f"{desc}: stale value was not detected")
        finally:
            readme.write_text(original, encoding="utf-8")

    def test_stale_test_case_count(self):
        self._assert_caught("| Skill test cases | **1108** |", "| Skill test cases | **333** |",
                            "333 was the pre-Phase-5 case count")

    def test_stale_server_count(self):
        self._assert_caught("| MCP servers | **26** |", "| MCP servers | **35** |",
                            "35 is the entry count, not the server count (H-8)")

    def test_stale_registry_split(self):
        self._assert_caught("(incl. 9 that are not servers) | **35**",
                            "(incl. 0 that are not servers) | **35**",
                            "the nine non-server entries are the substance of H-8")

    def test_stale_knowledge_count(self):
        self._assert_caught("| Knowledge articles | **72** |", "| Knowledge articles | **37** |",
                            "knowledge article count")

    def test_stale_narrative_case_count(self):
        self._assert_caught("**1,108 cases across 50", "**333 cases across 50",
                            "the narrative restates the count outside the generated block")


class TestQualifiersAreLoadBearing(unittest.TestCase):
    """The hedges are the point; removing a hedge while keeping the number must fail."""

    def _assert_caught(self, find: str, replace: str, desc: str) -> None:
        readme = ROOT / "README.md"
        original = readme.read_text(encoding="utf-8")
        self.assertIn(find, original, f"qualifier for {desc} is absent from README.md")
        try:
            readme.write_text(original.replace(find, replace, 1), encoding="utf-8")
            self.assertNotEqual(run_checker().returncode, 0, f"{desc}: qualifier removal undetected")
        finally:
            readme.write_text(original, encoding="utf-8")

    def test_not_executed_results_qualifier_is_required(self):
        self._assert_caught("**These cases are authored specifications, not executed results.**",
                            "**These cases are authored specifications.**",
                            "the cases are specifications; calling them results implies they ran")

    def test_no_effectiveness_claim_is_required(self):
        self._assert_caught("**Not measured. No effectiveness claim is made.**", "**Not measured.**",
                            "without this, 1,108 cases read as evidence the skills work")

    def test_evaluations_claim_is_required(self):
        self._assert_caught(
            "`evaluations/` holds seven scaffolded\ndomain READMEs and **zero evaluation records**",
            "`evaluations/` has no content",
            "the scoring section's 'not validated' argument rests on there being no outcome data")

    def test_category_note_is_required(self):
        """`mcp-servers` = 35 repositories and 26 servers are different axes; the note says so."""
        self._assert_caught("`mcp-servers` above is a **repository-corpus category**",
                            "The mcp-servers category",
                            "without the note, README shows 35 and 26 for 'MCP servers' unexplained")


class TestTierAssertions(unittest.TestCase):
    """`tier_assertions` decides what counts as asserting the superseded `UNVERIFIED` label."""

    def test_backticked_mentions_are_naming_not_asserting(self):
        """A changelog must be able to record the correction, which requires naming the old label."""
        text = "The tier written `15 UNVERIFIED` is now `15 NO-LICENSE`."
        self.assertEqual(crc.tier_assertions(text), [],
                         "a backticked mention documents the fix; flagging it makes the fix "
                         "unrecordable")

    def test_prose_assertion_is_caught(self):
        text = "- Tier distribution: 214 S, 127 A, 15 UNVERIFIED.\n"
        self.assertEqual(crc.tier_assertions(text), [(1, 15)])

    def test_zero_is_a_true_statement_not_a_stale_label(self):
        """There are no fetch failures here, so reporting zero unverified records is correct."""
        self.assertEqual(crc.tier_assertions("16 C, 3 EXPERIMENTAL, **15 NO-LICENSE**, 0 UNVERIFIED."), [])

    def test_masking_preserves_line_numbers(self):
        """Code spans are blanked, not deleted, so reported lines stay accurate."""
        text = "line one `99 UNVERIFIED`\nline two\nline three 7 UNVERIFIED\n"
        self.assertEqual(crc.tier_assertions(text), [(3, 7)])

    def test_line_offset_makes_sliced_numbers_file_accurate(self):
        """The CHANGELOG is sliced to its current section; a slice-relative line number misleads."""
        text = "preamble\npreamble\npreamble\n## [2.1.0]\n\nbody 5 UNVERIFIED\n"
        heads = [m.start() for m in re.finditer(r"(?m)^## \[", text)]
        offset = text[:heads[0]].count("\n")
        self.assertEqual(crc.tier_assertions(text[heads[0]:], offset), [(6, 5)],
                         "the reported line must be the line in the file, not in the slice")


class TestHistoricalSectionsAreLabelled(unittest.TestCase):
    """History is preserved verbatim and labelled — never silently rewritten."""

    def test_released_sections_that_restate_a_superseded_label_carry_a_banner(self):
        text = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        heads = [m.start() for m in re.finditer(r"(?m)^## \[", text)]
        self.assertGreaterEqual(len(heads), 3, "expected at least 2.1.0, 2.0.0 and 1.0.0 sections")
        for i, start in enumerate(heads[1:], start=1):
            end = heads[i + 1] if i + 1 < len(heads) else len(text)
            section = text[start:end]
            title = section.splitlines()[0]
            if crc.tier_assertions(section):
                self.assertIn("historical", section.lower(),
                              f"{title} restates a superseded tier label without saying it is a "
                              f"historical record; a reader could take it for the current state")

    def test_the_1_0_0_figures_were_preserved_not_rewritten(self):
        """The correction is a banner, not an edit: 1.0.0 really did ship that label."""
        text = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        self.assertIn("15 UNVERIFIED", text,
                      "the 1.0.0 record must keep the label it shipped with")
        self.assertIn("Historical record", text)

    def test_removing_the_banner_fails_the_check(self):
        changelog = ROOT / "CHANGELOG.md"
        original = changelog.read_text(encoding="utf-8")
        mutated = original.replace("> **Historical record — the figures below", "> The figures below", 1)
        self.assertNotEqual(mutated, original, "the banner text was not found to remove")
        try:
            changelog.write_text(mutated, encoding="utf-8")
            self.assertNotEqual(run_checker().returncode, 0,
                                "deleting the historical banner must fail the check")
        finally:
            changelog.write_text(original, encoding="utf-8")


class TestAuthoritativeLayerIsSingle(unittest.TestCase):
    """REVIEW-REPORT.md grew four phases of recommendations; exactly one may be current."""

    def setUp(self):
        self.text = (ROOT / "REVIEW-REPORT.md").read_text(encoding="utf-8")

    def test_exactly_one_section_is_marked_current_and_authoritative(self):
        n = self.text.count("CURRENT AND AUTHORITATIVE")
        self.assertEqual(n, 1, f"found {n} sections claiming to be current and authoritative")

    def test_superseded_merge_recommendations_point_at_the_live_one(self):
        """Three phases each ended in a merge recommendation; only §15.5 may stand."""
        self.assertGreaterEqual(self.text.count("SUPERSEDED"), 2,
                                "§13's 'do not merge yet' and §14.5's 'merge' must both be marked")
        # Every SUPERSEDED banner has to say what replaces it, or a reader is told to stop
        # without being told where to go. The banners are multi-line blockquotes and the pointer
        # sits on a continuation line, so a banner is the run of `>` lines, not a single line.
        lines = self.text.splitlines()
        banners = []
        for i, ln in enumerate(lines):
            if "SUPERSEDED" not in ln or not ln.lstrip().startswith(">"):
                continue
            block = [ln]
            j = i + 1
            while j < len(lines) and lines[j].lstrip().startswith(">"):
                block.append(lines[j]); j += 1
            banners.append((i + 1, "\n".join(block)))
        self.assertGreaterEqual(len(banners), 2, "expected superseded banners on §13 and §14.5")
        dangling = [(n, b) for n, b in banners if "15.5" not in b and "§15" not in b]
        self.assertEqual(dangling, [],
                         "these SUPERSEDED banners do not point at the authoritative section:\n"
                         + "".join(f"  line {n}: {b.strip()[:150]}\n" for n, b in dangling))
        self.assertIn("§15.5", self.text)

    def test_a_reading_guide_precedes_the_numbered_sections(self):
        """The guide must come first; searched against `## 1.` because the guide is itself a `## `."""
        guide = self.text.find("How to read this report")
        first_numbered = self.text.find("\n## 1. ")
        self.assertNotEqual(guide, -1, "the three-layer reading guide is missing")
        self.assertNotEqual(first_numbered, -1, "no numbered section found to compare against")
        self.assertLess(guide, first_numbered,
                        "the reading guide must come before §1, or a linear reader hits the "
                        "historical layers before being told they are historical")


if __name__ == "__main__":
    unittest.main(verbosity=2)
