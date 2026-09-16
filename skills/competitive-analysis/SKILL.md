---
name: competitive-analysis
version: 1.0.0
description: >-
  Compare products, libraries or approaches on evidence — feature matrices with sources, real
  tradeoffs, positioning gaps and a defensible recommendation rather than a verdict.
category: research
status: active
confidence: high
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [competitive-analysis, comparison, research, positioning, decision, evaluation]
applies_to: [any]
priority: 78
requires: [web-research, evidence-validation]
conflicts_with: []
estimated_tokens: 2540
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Workflow
    anchor: "#workflow"
    purpose: implementation
  - heading: Comparison discipline
    anchor: "#comparison-discipline"
    purpose: decision
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "OpenSSF Scorecard"
    url: https://github.com/ossf/scorecard
    type: github-repository
    license: Apache-2.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
related_skills: [web-research, evidence-validation, repository-analysis, dont-reinvent-the-wheel, visual-design-research]
related_repositories: [ossf/scorecard, lmarena/arena-hard-auto]
tests: 6
---

# Competitive Analysis

## Purpose

Produce a comparison that survives contact with a sceptical reader: every cell sourced,
every tradeoff named, every "winner" qualified by the constraint that makes it win.

The output is never "X is best". It is **"for these constraints, X; for those, Y; here is
what would change the answer."**

## When to Use

```text
□ Choosing between libraries, frameworks, services or vendors
□ Positioning a product against competitors (feeds visual-design-research and strategy)
□ Evaluating whether to build, adopt or wait
□ Preparing a recommendation someone else must approve
□ Re-checking a decision made a year ago against a changed landscape
```

## When NOT to Use

```text
✗ A question with one acceptable answer already decided — that is a migration plan
✗ Comparing things that are not substitutes (a library vs a hosted service vs a pattern)
  unless you explicitly frame the comparison at the capability level
✗ When the deciding constraint is unknown: establish it first, or the matrix is decoration
```

## Inputs

```text
capability        the job to be done, stated as a behaviour — not as a product category
options           3–6 candidates, including "do nothing" and "build it"
constraints       the hard limits: budget, license, stack, compliance, team skills, deadline,
                  scale, egress, exit requirements
weights           which criteria decide, and by how much (agreed BEFORE scoring)
audience          who consumes the analysis and what they will do with it
```

## Workflow

```text
FRAME → ENUMERATE → GATHER → NORMALISE → MATRIX → TRADEOFFS → POSITION → RECOMMEND → RE-VALIDATE
```

```text
1 FRAME        Write the decision question with its constraints and the weights. Agree them
               with the decision-maker before gathering data — after seeing the data, weights
               drift toward the preferred answer.
2 ENUMERATE    Find candidates from ≥3 independent discovery paths (category search, the
               ecosystem's own comparison pages, practitioner recommendations, this KB's
               indexes/, the package registry sorted by relevance not downloads). Include the
               non-obvious ones: the boring incumbent, the platform-native option, "build it".
3 GATHER       Per candidate, from primary sources in this order: official docs for the
               version in question · the repository (README, CHANGELOG, issues, releases) ·
               the vendor's pricing and limits pages · independent benchmarks with a published
               method · practitioner reports. Record URL + date for every fact.
4 NORMALISE    Make cells comparable: same units, same version class, same test conditions,
               same pricing period, same date. An unnormalised matrix compares marketing to
               measurement.
5 MATRIX       One row per criterion, one column per candidate. Every cell is either a sourced
               fact, "not applicable", or "unknown" — never blank and never guessed.
6 TRADEOFFS    For each candidate: what you gain, what you lose, what you cannot do at all.
               Name the failure mode of each, not only its strengths.
7 POSITION     Place candidates on the two axes that actually decide this choice. Identify the
               gaps — and ask why each gap is empty before recommending anyone fill it.
8 RECOMMEND    Conditional recommendation: "choose X if <constraints>; choose Y if <other
               constraints>; the answer changes if <trigger>." Include the runner-up, the
               switching cost, and the re-validation date.
9 RE-VALIDATE  Landscapes move. Re-check the matrix on a schedule and after any upstream
               release, license change, acquisition or abandonment.
```

## Comparison discipline

### Criteria that are usually decisive
```text
FIT              does it actually solve the stated capability, or 80% of it?
MATURITY         release history, SemVer discipline, breaking-change frequency
MAINTENANCE      cadence, contributor count, issue responsiveness, archived status, bus factor
LICENSE          usable for your distribution model? copyleft reach? `license: null`?
SECURITY         SECURITY.md, advisory history, patch turnaround, default hardening,
                 provenance/sigstore, install-time scripts
OPERATIONAL COST infra, hosting, monitoring, on-call, upgrade effort
INTEGRATION COST time to first working integration, measured by running the quickstart
REMOVAL COST     coupling, data portability, contract stability, exit plan
PERFORMANCE      on YOUR workload shape, not the vendor's benchmark
ECOSYSTEM        plugins, community answers, hiring pool, docs quality
TRAJECTORY       improving or declining? funded how? what happens if it dies?
LOCK-IN          proprietary formats, data egress fees, non-standard APIs
```

### Rules for cells
```text
1. Every factual cell cites a source and a date. Uncited cells are marked GENERATED.
2. Vendor claims are labelled as vendor claims. A vendor benchmark is evidence of what the
   vendor measured, not of what you will experience.
3. Numbers require a method: workload, hardware, dataset, version, repetitions, who paid.
   A number without a method is at best LOW confidence (see evidence-validation).
4. "Unknown" is a valid and common cell. Do not fill it with an inference.
5. Version-scope every behavioural claim: "as of v3.2, checked 2026-09-15".
6. Recency matters asymmetrically: pricing and limits go stale in weeks; architecture and
   license terms go stale in years.
7. Do not average conflicting sources. Record the conflict and its likely cause.
8. Weight criteria before scoring. Scoring first and weighting second is motivated reasoning.
```

### Anti-bias checks
```text
□ Did you use the same depth of research on the candidate you dislike as on the one you like?
□ Did you run every quickstart, or only the favourite's?
□ Are you comparing the incumbent's reality with the challenger's marketing?
□ Did a sponsor, employer or prior investment influence the ranking? Say so explicitly.
□ Would the recommendation change if the weights shifted by 10%? If yes, say it is sensitive.
```

## Failure Modes

```text
MARKETING MATRIX        Cells filled from vendor homepages.
UNNORMALISED UNITS      Comparing $/month to $/request to "free tier".
STALE PRICING           Limits and prices from a year ago.
MISSING CANDIDATES      Only the three loudest options; the boring incumbent never evaluated.
NO "DO NOTHING" ROW     Building or deferring is never considered.
WEIGHTS AFTER SCORING   Criteria weighted to justify a preference already formed.
VENDOR BENCHMARK TRUST  Reproducing a sponsored comparison as fact.
STAR AS QUALITY         Ranking repositories by stars, ignoring status and license.
REMOVAL COST OMITTED    The decisive criterion for anything you will depend on for years.
PERPETUAL ANALYSIS      Never recommending because one more option might exist.
UNQUALIFIED VERDICT     "X is the best" with no constraint set attached.
```

## Quality Checklist

```text
□ Decision question, constraints and weights agreed before data gathering
□ 3–6 candidates from ≥3 discovery paths, including "build" and "do nothing"
□ Every factual cell sourced with URL + date; vendor claims labelled as such
□ Numbers carry their measurement method; unmeasured numbers are marked LOW confidence
□ Cells normalised to the same units, version class and date
□ "Unknown" used rather than guessed; no blank cells
□ Tradeoffs and failure modes stated per candidate, not only strengths
□ Positioning on the two decisive axes; gaps interrogated before being recommended
□ Conditional recommendation with the runner-up, switching cost and re-validation date
□ Anti-bias checks run and recorded
□ Sensitivity noted where a 10% weight change alters the answer
□ Re-validation date set; landscape changes tracked
```

## Anti-Patterns

```text
✗ A feature matrix with ✓/✗ and no sources
✗ Quoting a vendor's "3× faster" with no workload definition
✗ Comparing a self-hosted library with a managed service on price alone
✗ Ranking GitHub repositories by stars
✗ "X is the industry standard" with no evidence of who decided
✗ Omitting removal cost from a five-year dependency decision
✗ Presenting a recommendation with no stated conditions
```

## References

- [`web-research`](../web-research/SKILL.md) · [`evidence-validation`](../evidence-validation/SKILL.md)
- [`repository-analysis`](../repository-analysis/SKILL.md) · [`dont-reinvent-the-wheel`](../dont-reinvent-the-wheel/SKILL.md)
- [`decision-records/`](../../decision-records/) — matrix and ADR templates
- [`indexes/best-of.md`](../../indexes/best-of.md) · [`indexes/frameworks.md`](../../indexes/frameworks.md)
- [`knowledge/research/source-conflict-case-study.md`](../../knowledge/research/source-conflict-case-study.md)
- OpenSSF Scorecard — <https://github.com/ossf/scorecard>

## Related Skills

`web-research` · `evidence-validation` · `repository-analysis` · `dont-reinvent-the-wheel` ·
`visual-design-research` · `project-planning`

## Evaluation Criteria

```text
1. Source coverage: 100% of factual cells carry a URL and date.
2. Candidate completeness: a domain expert names no obvious missing candidate.
3. Normalisation: 0 cells comparing incomparable units or dates.
4. Bias resistance: a reviewer cannot identify a systematically under-researched candidate.
5. Decision usefulness: the decision-maker can act without further questions.
6. Durability: the recommendation is not invalidated within its re-validation window by
   information that was available at the time.
```

Test cases in [`tests/`](tests/).
