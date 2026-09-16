---
name: knowledge-base-maintenance
version: 1.0.0
description: >-
  Keep this repository trustworthy over time — validate, refresh sources, re-score, deduplicate,
  resolve conflicts, demote what no longer holds, regenerate every index, and record the run.
trigger: >-
  On a schedule (weekly validation, monthly source refresh, quarterly deep review); on new
  contribution; on a CI failure in any validation job; on an upstream event that invalidates content
  (release, rename, archive, license change, advisory, retraction); or on a user-reported correction.
not_for: >-
  Authoring new knowledge from scratch, which begins with workflows/research-before-coding;
  one-off typo fixes; content whose subject is private, leaked or prohibited — that is rejected, not
  maintained; deciding policy, which is a human decision recorded in an ADR.
status: active
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2026-12-15
tags: [maintenance, curation, validation, freshness, scoring, indexes, workflow, meta]
confidence: high
claim_type: recommendation
evidence_level: cross-checked
estimated_duration: 15-30 minutes for a scheduled run; hours for a quarterly deep review
stages:
  - id: 1
    name: Validate the current state
    goal: Establish a green baseline before changing anything, so new failures are attributable to this run.
    skill: evidence-validation
    agent: skill-curator
    inputs: [repository contents, schemas/, metadata/]
    outputs: [validation report from validate_frontmatter.py, validate_json.py, validate_links.py, validate_policy.py, dedupe.py, check_staleness.py]
    exit_gate: All validators report zero errors, or every pre-existing error is listed with its cause and a decision to fix it in this run.
    max_loops: 2
    on_gate_failure: Fix the validator failures before proceeding. Maintaining content on top of a red baseline produces changes nobody can attribute.
  - id: 2
    name: Refresh repository-derived records
    goal: Re-fetch observable facts from the source of truth so repository metadata reflects today rather than the last run.
    skill: repository-analysis
    inputs: [scripts/update/seeds.json, scripts/update/curation.json, GitHub API]
    outputs: [updated metadata/repositories.json with stars, stars_checked_at, pushed_at, status, license, license_risk, archived flag, tier and trust_score; resolution log for renames and failures]
    exit_gate: Every seed resolves to a canonical repository or is recorded as failed with a reason; renamed and archived repositories are detected; every star count carries its observation date; and null licenses are flagged no-license-do-not-redistribute.
    max_loops: 2
    on_gate_failure: Quarantine the unresolvable seed rather than retaining a stale record. A repository record that cannot be resolved is a claim with no evidence.
  - id: 3
    name: Verify external sources
    goal: Re-check the reachability and continued accuracy of cited non-repository sources.
    skill: evidence-validation
    agent: fact-checker
    inputs: [sources blocks across all artifacts, metadata/sources-papers.json, indexes/sources-papers.md]
    outputs: [per-source reachability result, consecutive-failure history, corrected citations, newly quarantined sources]
    exit_gate: Every cited URL in active content was fetched; sources that fail consecutively are marked for review rather than silently retained; and papers remain verified against their primary source rather than a secondary aggregator.
    max_loops: 2
    on_gate_failure: Downgrade the dependent claims and set claim_type or confidence accordingly. A dead source supporting a live fact is a defect.
  - id: 4
    name: Scan for staleness
    goal: Find content past its review date or invalidated by an upstream event.
    skill: evidence-validation
    inputs: [expires_at and verified_at across all frontmatter, external_changes list, freshness policy]
    outputs: [staleness report — artifact, domain, days past review, required action]
    exit_gate: Every artifact past expires_at has an assigned action — re-verify, refresh, archive or quarantine — and fast-moving domains are on their 90-day cycle rather than a longer one.
    max_loops: 2
    on_gate_failure: Quarantine the expired artifact out of the active index. Expired content retrieved with fresh-looking confidence is worse than absent content.
  - id: 5
    name: Admit new submissions
    goal: Apply the admission standard to anything submitted since the last run.
    skill: evidence-validation
    agent: skill-curator
    inputs: [new or changed artifacts, their frontmatter and sources, issue-template submissions]
    outputs: [per-artifact verdict — ADMIT, REVISE with the specific fix, QUARANTINE to experimental/, or REJECT with the reason]
    exit_gate: Every admitted artifact has resolvable sources actually fetched in this run, a claim_type supported by its evidence, a confidence the evidence justifies, an expires_at per the freshness policy, declared provenance, and a clean policy check.
    max_loops: 3
    on_gate_failure: Quarantine rather than admit. An ungradeable artifact never enters the retrieval index, because a retrieved claim is acted upon with the confidence its label implies.
  - id: 6
    name: Deduplicate and resolve conflicts
    goal: Prevent the same knowledge existing twice and the same question being answered two ways.
    skill: research-synthesis
    inputs: [dedupe.py output, overlapping claim reports, conflict reports]
    outputs: [merged records with supersede links, conflict entries in the prescribed format, claim_type adjustments]
    exit_gate: No two active artifacts make the same load-bearing claim with different content; every conflict is recorded with both sources, the likely cause, the side relied upon and what would settle it — never averaged and never silently resolved.
    max_loops: 2
    on_gate_failure: Escalate load-bearing unresolvable conflicts. A hidden contradiction in a knowledge base is worse than a visible one.
  - id: 7
    name: Re-score
    goal: Recompute quality scores from observable properties so tiers reflect current evidence rather than past judgement.
    skill: evidence-validation
    inputs: [all authored content, refreshed repository metadata, verified source data]
    outputs: [updated scores written back to frontmatter and metadata/scores.json, tier assignments, tier-change report]
    exit_gate: Scores are computed by scripts/score/score_skills.py from the seven components rather than assigned by judgement, and every tier change is explained by an observable change in its inputs.
    on_gate_failure: Investigate the unexplained tier change. A score that moved without a cause indicates either a scoring defect or a content change that was not recorded.
  - id: 8
    name: Demote and archive
    goal: Remove what no longer holds without losing the reason it was once believed.
    skill: documentation
    inputs: [staleness report, conflict resolutions, tier changes, deprecation notices]
    outputs: [deprecated or archived artifacts with successor links, removal from the active index, retained files]
    exit_gate: Every demotion records the reason and links a successor where one exists; nothing is deleted outright, because deleting a wrong decision loses the reasoning that prevents it recurring.
    on_gate_failure: Mark quarantined rather than deleting. An artifact that cannot be graded today may be gradeable with evidence that arrives later.
  - id: 9
    name: Regenerate all derived artifacts
    goal: Rebuild every generated file from its records so no index can drift from its source.
    inputs: [metadata/repositories.json, all frontmatter, registries]
    outputs: [regenerated indexes/ via extract_registries.py and build_index.py, repository cards via generate_repository_cards.py, README statistics via update_readme_stats.py]
    exit_gate: The generated-drift CI check is clean — regeneration produces byte-identical output to what is committed, proving no index was hand-edited.
    max_loops: 2
    on_gate_failure: Revert the hand edit and fix the underlying record instead. A hand-edited generated index is silently wrong from the moment its source changes.
  - id: 10
    name: Final validation and record
    goal: Confirm the repository is green after maintenance and record what changed.
    skill: documentation
    agent: skill-curator
    inputs: [all changes from this run]
    outputs: [clean validation suite, CHANGELOG.md entry listing admitted, revised, quarantined, rejected, refreshed, deprecated, re-scored and regenerated items with reasons, commit]
    exit_gate: All validators pass with zero errors, the changelog entry accounts for every change made in this run, and the run is committed with its date and trigger.
    max_loops: 2
    on_gate_failure: Fix before committing. Never commit maintenance that leaves the repository red.
quality_gates:
  - Validation suite green before changes begin and after they end.
  - Every repository record resolved to a canonical upstream, with dated star counts.
  - Null licenses flagged no-license-do-not-redistribute; archived and renamed repositories detected.
  - 100% of cited URLs in active content fetched during the run.
  - Papers verified against their primary source, never a secondary aggregator alone.
  - Every artifact past expires_at actioned; none left in the active index.
  - Admitted content has verified sources, supported claim_type, justified confidence and declared provenance.
  - No duplicate load-bearing claims; every conflict recorded in the prescribed format, never averaged.
  - Scores computed by script from observable properties, never assigned by judgement.
  - Demotions retain the file and record the reason with a successor link.
  - Generated artifacts byte-identical on regeneration; no hand-edited index.
  - CHANGELOG entry accounts for every change in the run.
  - No leaked, proprietary or prohibited material admitted at any stage.
artifacts:
  - validation reports before and after
  - refreshed metadata/repositories.json with resolution log
  - source verification results and failure history
  - staleness report with assigned actions
  - admission decisions per submission
  - merge and conflict records
  - updated scores and tier-change report
  - demotion and archive records
  - regenerated indexes, cards and README statistics
  - CHANGELOG.md entry and commit
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
sources:
  - title: "GitHub REST API — repositories"
    url: https://docs.github.com/en/rest/repos/repos
    type: official-docs
    organization: GitHub
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
  - title: "OpenSSF Scorecard"
    url: https://github.com/ossf/scorecard
    type: github-repository
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
related: [agents/skill-curator/AGENT.md, agents/fact-checker/AGENT.md, CONTRIBUTING.md, scripts/validate/]
---

# Workflow: Knowledge Base Maintenance

```text
1 VALIDATE → 2 REFRESH REPOS → 3 VERIFY SOURCES → 4 STALENESS → 5 ADMIT
  → 6 DEDUPE+CONFLICTS → 7 RE-SCORE → 8 DEMOTE → 9 REGENERATE → 10 VALIDATE+RECORD
```

## The invariant this workflow protects

**Nothing in the retrieval index may be untraceable, undated or ungraded.** An agent that reads
this repository will act on what it finds with the confidence the label implies — so a stale,
unsourced or contradictory entry is not a documentation defect, it is a defect in whatever the
reading agent goes on to build.

## Why validation runs twice

Stage 1 establishes a green baseline so that any failure at stage 10 is attributable to this run
rather than to pre-existing damage. Stage 10 proves the maintenance did not break the repository.
Committing red is prohibited — a knowledge base whose validators fail teaches its readers to
ignore its validators.

## Why indexes are never hand-edited

Stage 9 regenerates every derived file from its records, and CI asserts the result is
byte-identical to what is committed. A hand-edited index is correct at the moment it is edited and
silently wrong from the first change to its source. Fix the record; regenerate the index.

## Cadence

```text
EVERY RUN (weekly or on trigger)     stages 1, 4, 5, 6, 9, 10
MONTHLY                              add stages 2, 3 — repository and source refresh
QUARTERLY (deep review)              all stages, plus a spot audit of high-tier content and a
                                     review of the scoring rubric and freshness policy themselves
ON EVENT                             stages 2, 3, 4, 6, 8, 9, 10 — a rename, archive, license
                                     change, advisory or retraction invalidates specific records
```

## Failure modes specific to this workflow

```text
ADMISSION BY FORMAT      Content admitted because its frontmatter parses, not because its claims
                         were verified. Stage 5 requires URLs fetched in this run.
INDEX DRIFT              A hand-edited generated index. Stage 9 plus the CI drift check.
STALENESS NEGLECT        Expired content left in the index, retrieved with fresh-looking confidence.
SILENT DELETION          Removing content with no reason recorded, so the mistake is re-made.
SCORE INFLATION          Tiers drifting upward because scoring is applied leniently. Scores are
                         script-computed for exactly this reason.
CONFLICT ERASURE         Averaging two disagreeing sources into a single confident statement.
PARTIAL RUN              Skipping stage 10 and committing without final validation.
PROHIBITED MATERIAL      Admitting leaked prompts or private model internals because they are
                         publicly reachable. Prohibited by policy regardless of reachability.
```

## References

- [`agents/skill-curator/AGENT.md`](../../agents/skill-curator/AGENT.md) · [`agents/fact-checker/AGENT.md`](../../agents/fact-checker/AGENT.md)
- [`CONTRIBUTING.md`](../../CONTRIBUTING.md) · [`SECURITY.md`](../../SECURITY.md) · [`AGENTS.md`](../../AGENTS.md)
- [`scripts/validate/`](../../scripts/validate/) · [`scripts/update/`](../../scripts/update/)
- [`scripts/score/score_skills.py`](../../scripts/score/score_skills.py) · [`scripts/generate-index/`](../../scripts/generate-index/)
- [`scripts/deduplicate/dedupe.py`](../../scripts/deduplicate/dedupe.py)
- [`knowledge/ai-engineering/freshness-policy.md`](../../knowledge/ai-engineering/freshness-policy.md)
- [`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md)
- [`.github/workflows/kb-ci.yml`](../../.github/workflows/kb-ci.yml) · [`Makefile`](../../Makefile)
