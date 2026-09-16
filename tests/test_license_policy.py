#!/usr/bin/env python3
"""H-5 regression: the license hard override reaches the markdown, and fires on vendoring.

The override always worked *in the data*: all 15 no-license records carried
`license_risk: no-license-do-not-redistribute` and all 57 `NOASSERTION` records carried
`custom-license-review-before-vendoring`. What did not work was the enforcement, in two
opposite directions at once.

Under-inclusive: the check scanned only `.ts/.tsx/.js/.py/.go/.rs`, while the realistic
vendoring target in this repository is a **markdown article** copying prose or a skill from
`anthropics/skills` or `openai/skills`. Markdown was never looked at.

Over-inclusive: it matched the repository *name* alone, not `owner/name`, so every script that
used the word "skills" was flagged for `openai/skills`. That produced most of the warnings in
the policy output. A warning that is mostly noise is read once and then skipped, which is how a
control stops being one — the review's point, and the reason both halves had to be fixed rather
than the volume turned down.

Also fixed here, and not reported by the review: none of the 72 generated repository cards
carried the license marker. The policy lived in `metadata/repositories.json`, which is not what
a human or an agent reads. Cards now carry `license_risk` in frontmatter and a banner above the
fold, and a check fails the build if either goes missing.

Run: python3 -m unittest tests.test_license_policy -v
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
    sys.modules[name] = mod            # dataclass processing looks the module up here
    spec.loader.exec_module(mod)
    return mod


vp = load("validate_policy", "scripts/validate/validate_policy.py")

NO_LICENSE = "no-license-do-not-redistribute"
CUSTOM = "custom-license-review-before-vendoring"
SLUG = "anthropics/skills"
OTHER = "openai/skills"


class scratch_root:
    """A temporary ROOT holding a registry and any files a test needs.

    Nothing here touches the committed repository: the checks read `metadata/repositories.json`
    through `vp.ROOT`, so pointing that at a scratch tree is enough to exercise them on
    synthetic records.
    """

    def __init__(self, records=None, files=None):
        self.records = records if records is not None else [
            {"slug": SLUG, "category": "agent-skills", "license": "NONE", "license_risk": NO_LICENSE},
            {"slug": OTHER, "category": "agent-skills", "license": "NONE", "license_risk": NO_LICENSE},
            {"slug": "vercel/ai", "category": "agent-frameworks", "license": "NOASSERTION",
             "license_risk": CUSTOM},
            {"slug": "torvalds/linux", "category": "core", "license": "GPL-2.0", "license_risk": "none"},
        ]
        self.files = files or {}

    def __enter__(self):
        self.root = Path(tempfile.mkdtemp())
        (self.root / "metadata").mkdir()
        (self.root / "metadata" / "repositories.json").write_text(
            json.dumps({"repositories": self.records}))
        for rel, body in self.files.items():
            p = self.root / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(body)
        self._saved = vp.ROOT
        vp.ROOT = self.root
        return self

    def __exit__(self, *exc):
        vp.ROOT = self._saved
        shutil.rmtree(self.root, ignore_errors=True)
        return False

    def paths(self):
        return [self.root / rel for rel in self.files]

    def card(self, slug, body):
        """Add the card the generator would have written for `slug`."""
        rec = next(r for r in self.records if r["slug"] == slug)
        rel = vp.card_path_for(slug, rec["category"])
        self.files[rel] = body
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body)
        return rel


def a_card(slug, risk, frontmatter_marker=True, body_marker=True):
    fm = f"    license_risk: {risk}\n" if frontmatter_marker else ""
    body = (f"> LICENSE RISK — `{risk}`. Do not vendor or redistribute.\n\n"
            if body_marker else "> Nothing about the license here.\n\n")
    return (f"---\ntitle: \"{slug}\"\nsources:\n  - title: \"{slug} on GitHub\"\n"
            f"    url: https://github.com/{slug}\n    type: github-repository\n{fm}---\n\n"
            f"# {slug}\n\n{body}## Facts\n")


def block(lines=20, lang="python"):
    body = "\n".join(f"line {i}" for i in range(lines))
    return f"```{lang}\n{body}\n```\n"


class CardsStateThePolicy(unittest.TestCase):
    """The override has to reach the markdown, not stop at the data file."""

    def test_every_risky_card_in_the_committed_corpus_carries_the_marker(self):
        """The real repository, not a scratch tree: this is the assertion the generator change
        exists to make true. 72 cards were missing it before H-5."""
        errs, _ = vp.check_cards_state_license_policy(vp.load_license_risks())
        self.assertEqual([], errs, "\n".join(errs[:6]))

    def test_the_committed_registry_really_does_have_72_risky_records(self):
        """Guards the guard: if the risk list were empty the card check would pass vacuously."""
        risks = vp.load_license_risks()
        self.assertEqual(15, sum(1 for v in risks.values() if v == NO_LICENSE))
        self.assertEqual(57, sum(1 for v in risks.values() if v == CUSTOM))

    def test_a_card_missing_the_frontmatter_marker_is_an_error(self):
        with scratch_root() as s:
            s.card(SLUG, a_card(SLUG, NO_LICENSE, frontmatter_marker=False))
            errs, _ = vp.check_cards_state_license_policy(vp.load_license_risks())
        self.assertTrue(any("frontmatter does not carry" in e for e in errs), errs)

    def test_a_card_missing_the_readable_banner_is_an_error(self):
        """Machine-parseable is not enough. The point of the card is that someone reads it."""
        with scratch_root() as s:
            s.card(SLUG, a_card(SLUG, NO_LICENSE, body_marker=False))
            errs, _ = vp.check_cards_state_license_policy(vp.load_license_risks())
        self.assertTrue(any("body does not state" in e for e in errs), errs)

    def test_a_missing_card_is_an_error(self):
        with scratch_root() as s:                     # no cards added at all
            errs, _ = vp.check_cards_state_license_policy(vp.load_license_risks())
        self.assertTrue(any("no card exists" in e for e in errs), errs)
        self.assertTrue(len(errs) >= 3, "every risky record should have been reported")

    def test_a_card_for_a_cleanly_licensed_repository_is_not_required_to_carry_one(self):
        with scratch_root() as s:
            risks = vp.load_license_risks()
            self.assertNotIn("torvalds/linux", risks)


class OrphanCardsAreDetected(unittest.TestCase):
    """Found while enforcing H-5: a card survived a reclassification and nothing noticed."""

    def test_the_committed_corpus_has_no_orphan_cards(self):
        """The real repository. `repositories/developer-tools/firebase--firebase-tools.md`
        survived here from v1.0.0 until H-5 found it; nothing compared cards to the registry."""
        self.assertEqual([], vp.check_no_orphan_cards())

    def test_a_card_at_a_path_no_record_maps_to_is_an_error(self):
        with scratch_root() as s:
            s.card(SLUG, a_card(SLUG, NO_LICENSE))
            # the same repository, left behind at its pre-reclassification category
            (s.root / "repositories" / "developer-tools").mkdir(parents=True, exist_ok=True)
            (s.root / "repositories" / "developer-tools" / "anthropics--skills.md").write_text("stale")
            errs = vp.check_no_orphan_cards()
        self.assertTrue(any("orphan" in e for e in errs), errs)
        self.assertTrue(any("developer-tools" in e for e in errs))

    def test_the_category_readme_is_not_mistaken_for_a_card(self):
        with scratch_root() as s:
            s.card(SLUG, a_card(SLUG, NO_LICENSE))
            (s.root / "repositories" / "agent-skills" / "README.md").write_text("# listing\n")
            self.assertEqual([], vp.check_no_orphan_cards())


class VendoringIsAnError(unittest.TestCase):
    """The severity the review asked for: copied content stops the build, a mention does not."""

    def test_a_long_code_block_naming_the_repository_inside_it_is_an_error(self):
        text = f"## Example\n\n{block(20)}\n"
        text = text.replace("line 3", f"line 3  # adapted from {SLUG}")
        with scratch_root(files={"knowledge/agent-skills/x.md": text}) as s:
            errs, _ = vp.check_license_policy(s.paths(), vp.load_license_risks())
        self.assertTrue(any("vendored content" in e for e in errs), errs)
        self.assertIn(SLUG, errs[0])

    def test_a_long_code_block_attributed_in_the_prose_just_above_it_is_an_error(self):
        text = f"## Example\n\nCopied from {SLUG} for illustration:\n\n{block(18)}\n"
        with scratch_root(files={"skills/x/SKILL.md": text}) as s:
            errs, _ = vp.check_license_policy(s.paths(), vp.load_license_risks())
        self.assertTrue(any("vendored content" in e for e in errs), errs)

    def test_a_custom_license_repository_is_held_to_the_same_rule(self):
        text = f"## Example\n\n{block(20)}\n".replace("line 5", "line 5  # from vercel/ai")
        with scratch_root(files={"knowledge/x.md": text}) as s:
            errs, _ = vp.check_license_policy(s.paths(), vp.load_license_risks())
        self.assertTrue(any("vercel/ai" in e and CUSTOM in e for e in errs), errs)

    def test_a_cleanly_licensed_repository_is_not_restricted(self):
        """The check must not become a blanket fear of code blocks next to any repository name."""
        text = f"## Example\n\n{block(25)}\n".replace("line 4", "line 4  # from torvalds/linux")
        with scratch_root(files={"knowledge/x.md": text}) as s:
            errs, warns = vp.check_license_policy(s.paths(), vp.load_license_risks())
        self.assertEqual(([], []), (errs, warns))


class FalseAccusationsAreNotMade(unittest.TestCase):
    """Each of these fired on the committed corpus before the rule was tightened. Every one was
    original work by this repository, and an error that accuses honest prose gets argued with
    once and then ignored."""

    def test_authored_prose_in_a_text_fence_is_not_vendored_content(self):
        """`knowledge/agent-skills/skill-format.md` sets its authoring rules in an aligned
        ```text block, and rule 4 names the no-license collections in order to forbid copying
        them. Reading that as vendoring inverts the finding."""
        prose = ("```text\n"
                 "1. One skill, one procedure.   If the file needs part A and part B it is two skills.\n"
                 "2. Name the negative case.     When NOT to Use is mandatory.\n"
                 "3. Every claim carries provenance.\n"
                 f"4. Never copy external content. Several collections have no license at all\n"
                 f"   ({SLUG}, {OTHER}) — they are reference-only.\n"
                 + "".join(f"{i}. Another authored rule with enough length to matter here.\n"
                           for i in range(5, 20))
                 + "```\n")
        with scratch_root(files={"knowledge/agent-skills/x.md": prose}) as s:
            errs, _ = vp.check_license_policy(s.paths(), vp.load_license_risks())
        self.assertEqual([], errs)

    def test_a_long_prose_fence_naming_the_repository_is_not_accused(self):
        """Pins the prose-fence exclusion on its own. The case above is protected twice over —
        by the fence language *and* by the no-copy wording — so removing either rule left it
        green and the exclusion was untested. Here the wording is absent, so only the fence
        language stands between this passage and a false accusation.

        The limitation is real and deliberate: prose copied into a ```text fence is not caught
        by this check. It is still caught as a mention warning, and copied *code* is caught
        whatever the fence is labeled, because a bare fence stays a candidate.
        """
        text = ("```text\n"
                f"NOTES ON {SLUG}\n"
                + "".join(f"observation {i} about the repository layout and conventions\n"
                          for i in range(1, 22))
                + "```\n")
        with scratch_root(files={"knowledge/x.md": text}) as s:
            errs, warns = vp.check_license_policy(s.paths(), vp.load_license_risks())
        self.assertEqual([], errs)
        self.assertTrue(warns, "the mention is still surfaced, just not as vendoring")

    def test_a_passage_stating_the_no_copy_rule_is_compliance_not_violation(self):
        text = (f"Do not copy from {SLUG}; it has no license. Reference and link only.\n\n"
                f"{block(20)}\n")
        with scratch_root(files={"knowledge/x.md": text}) as s:
            errs, _ = vp.check_license_policy(s.paths(), vp.load_license_risks())
        self.assertEqual([], errs)

    def test_a_code_fence_in_a_passage_stating_the_no_copy_rule_is_not_accused(self):
        """Pins the no-copy exemption on its own: this is a real code fence, so the prose-fence
        rule does not apply, and only the wording protects it. Failing the build over the
        sentence that enforces the policy would remove the incentive to write it."""
        text = (f"Do not copy from {SLUG} — it has no license, so reference and link only.\n\n"
                f"{block(20)}\n".replace("line 2", f"line 2  # from {SLUG}"))
        with scratch_root(files={"knowledge/x.md": text}) as s:
            errs, _ = vp.check_license_policy(s.paths(), vp.load_license_risks())
        self.assertEqual([], errs)

    def test_a_mention_far_from_any_code_block_is_only_a_warning(self):
        text = (f"This article discusses {SLUG} at length.\n\n"
                + "Unrelated prose.\n" * 60
                + f"\n{block(30)}\n")
        with scratch_root(files={"knowledge/x.md": text}) as s:
            errs, warns = vp.check_license_policy(s.paths(), vp.load_license_risks())
        self.assertEqual([], errs)
        self.assertTrue(warns, "the mention should still be surfaced as a warning")

    def test_a_short_code_block_is_not_treated_as_vendored_content(self):
        text = f"Install it:\n\n```bash\npip install {SLUG.split('/')[1]}\n```\n"
        with scratch_root(files={"knowledge/x.md": text}) as s:
            errs, _ = vp.check_license_policy(s.paths(), vp.load_license_risks())
        self.assertEqual([], errs)

    def test_a_card_naming_the_repository_it_describes_is_not_a_violation(self):
        """The card is *about* the repository; requiring it not to name it would be absurd, and
        requiring it to name it is the other check in this module."""
        with scratch_root() as s:
            rel = s.card(SLUG, a_card(SLUG, NO_LICENSE))
            errs, warns = vp.check_license_policy(s.paths(), vp.load_license_risks())
        self.assertEqual(([], []), (errs, warns))
        self.assertTrue(rel)


class MatchingIsWholeSlug(unittest.TestCase):
    """The regression the review named: matching `name` alone flagged every script that used the
    word "skills" as a reference to `openai/skills`."""

    def test_the_bare_repository_name_does_not_match(self):
        for text in ("this repository has many skills",
                     "Skills are authored in markdown",
                     "the skill format is described below",
                     "SKILLS_DIR = './skills'"):
            with scratch_root(files={"knowledge/x.md": text}) as s:
                errs, warns = vp.check_license_policy(s.paths(), vp.load_license_risks())
            self.assertEqual(([], []), (errs, warns), f"fired on {text!r}")

    def test_a_lookalike_owner_does_not_match(self):
        with scratch_root(files={"knowledge/x.md": f"see someone-else/{SLUG.split('/')[1]}\n"}) as s:
            errs, warns = vp.check_license_policy(s.paths(), vp.load_license_risks())
        self.assertEqual(([], []), (errs, warns))

    def test_the_full_slug_does_match(self):
        with scratch_root(files={"knowledge/x.md": f"see {SLUG} for the format\n"}) as s:
            _, warns = vp.check_license_policy(s.paths(), vp.load_license_risks())
        self.assertTrue(warns)

    def test_matching_is_case_insensitive(self):
        with scratch_root(files={"knowledge/x.md": f"see {SLUG.upper()} here\n"}) as s:
            _, warns = vp.check_license_policy(s.paths(), vp.load_license_risks())
        self.assertTrue(warns)


class MentionWarningsAreScopedToWhereCopyingCouldHappen(unittest.TestCase):
    """133 warnings taught nobody anything. The mention warning is emitted only where copied
    content could plausibly live; the vendoring error still applies everywhere."""

    def test_generated_and_machinery_paths_do_not_warn(self):
        # not metadata/repositories.json: in a scratch tree that path *is* the registry
        for rel in ("scripts/generate-index/x.py", "tests/test_x.py",
                    "metadata/index.json", "indexes/mcp.md",
                    "repositories/agent-skills/README.md", "CHANGELOG.md"):
            with scratch_root(files={rel: f"names {SLUG} in passing\n"}) as s:
                _, warns = vp.check_license_policy(s.paths(), vp.load_license_risks())
            self.assertEqual([], warns, f"{rel} should not produce a mention warning")

    def test_knowledge_prose_does_warn(self):
        for rel in ("knowledge/x.md", "skills/x/SKILL.md", "patterns/x.md",
                    "workflows/x/WORKFLOW.md", "agents/x/AGENT.md"):
            with scratch_root(files={rel: f"names {SLUG} in passing\n"}) as s:
                _, warns = vp.check_license_policy(s.paths(), vp.load_license_risks())
            self.assertTrue(warns, f"{rel} is exactly where copied content would land")

    def test_a_root_entry_document_does_warn(self):
        """Pins the exemption list to exactly one rule. An earlier draft had a second filter
        for "paths where copied content could land", which silently excluded README.md — the
        most-read document in the repository — to save three warnings. Removing the filter
        left every other test green, which is how the gap was found."""
        with scratch_root(files={"README.md": f"names {SLUG} in passing\n"}) as s:
            _, warns = vp.check_license_policy(s.paths(), vp.load_license_risks())
        self.assertTrue(warns, "README.md is not exempt from the mention warning")

    def test_vendoring_is_still_an_error_on_a_path_exempt_from_warnings(self):
        """The warning exemption must not become a hole in the error. A generator script that
        pasted 20 lines out of a no-license repository is the worst case, not the mildest."""
        text = f"# helper\n\n{block(22)}\n".replace("line 7", f"line 7  # from {SLUG}")
        with scratch_root(files={"scripts/generate-index/x.py": text}) as s:
            errs, warns = vp.check_license_policy(s.paths(), vp.load_license_risks())
        self.assertEqual([], warns)
        self.assertTrue(any("vendored content" in e for e in errs), errs)


class FenceParsing(unittest.TestCase):

    def test_an_unterminated_fence_is_not_swallowed_to_end_of_file(self):
        """A card ending mid-fence is a different defect. Treating the rest of the document as
        copied code would turn one broken fence into a vendoring accusation."""
        spans = vp.fenced_blocks("```python\na\nb\n")
        self.assertEqual([], spans)

    def test_the_language_is_captured(self):
        self.assertEqual([(0, 2, "yaml")], vp.fenced_blocks("```yaml\na\n```\n"))

    def test_a_bare_fence_is_a_candidate_but_a_text_fence_is_not(self):
        self.assertNotIn("", vp.PROSE_FENCE_LANGS,
                         "an unlabeled fence must stay a candidate: copied content rarely labels itself")
        self.assertIn("text", vp.PROSE_FENCE_LANGS)

    def test_multiple_blocks_are_all_found(self):
        text = "```python\nx\n```\n\nprose\n\n```text\ny\n```\n"
        self.assertEqual([(0, 2, "python"), (6, 8, "text")], vp.fenced_blocks(text))


if __name__ == "__main__":
    unittest.main(verbosity=2)
