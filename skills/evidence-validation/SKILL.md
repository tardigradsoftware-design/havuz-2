---
name: evidence-validation
version: 1.0.0
description: >-
  Grade a source before acting on it. Turns "I found this" into "this is trustworthy for this
  specific claim, at this confidence, as of this date" — and rejects what cannot be graded.
category: research
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [verification, evidence, confidence, anti-hallucination, source-quality, methodology]
applies_to: [any]
priority: 92
requires: []
conflicts_with: []
estimated_tokens: 2281
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: The twelve checks
    anchor: "#the-twelve-checks"
    purpose: implementation
  - heading: Confidence ladder
    anchor: "#confidence-ladder"
    purpose: decision
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "Open Web Application Security Project — source and verification guidance"
    url: https://owasp.org/www-project-top-ten/
    type: standard
    organization: OWASP
    confidence: high
    claim_type: recommendation
    verified_at: 2026-09-15
  - title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
    url: https://arxiv.org/abs/2305.10601
    type: research-paper
    published: 2023-05-17
    license: CC BY 4.0
    confidence: very-high
    claim_type: fact
    verified_at: 2026-09-15
    note: "Self-evaluation of intermediate states is what makes deliberate search work; the same principle applies to grading evidence."
related_skills: [web-research, research-before-code, fact-checker, repository-analysis]
related_repositories: [ossf/scorecard, aquasecurity/trivy]
tests: 17
---

# Evidence Validation

## Purpose

Assign every claim a **confidence level backed by a checkable procedure**, and refuse to
promote ungradeable material into the knowledge base.

Validation is not "does this look right". It is: *what would have to be true for this
source to be wrong, and did I check for that?*

## When to Use

```text
□ Before recording any external claim in knowledge/, sources/ or a decision record
□ Before recommending a library, service, model or pattern to a user
□ Before acting on a number (benchmark, price, quota, star count, performance figure)
□ Whenever two sources disagree
□ Before promoting experimental/ content to core
```

## When NOT to Use

```text
✗ Statements about this repository's own contents — read the file
✗ Pure preferences ("I like this layout") — label them opinion and move on
✗ Re-validating something already validated today with an unchanged source:
  reuse the existing verified_at instead of burning budget
```

## Inputs

```text
claim          the exact statement to be validated, scoped to a version and a date
source(s)      URL(s), publisher, page date, author
usage          what will be done if the claim is accepted (this sets the required confidence)
```

**Required confidence by usage:**

```text
delete/migrate data, change auth, spend money   → very-high
choose a dependency for a new project           → high
write guidance others will follow               → high
mention as context                              → medium
form a hypothesis to test                       → low is acceptable if labelled
```

## The twelve checks

Run in order; stop early only if a check produces a hard rejection.

```text
 1 EXISTS          Does the URL resolve? Does the repository/paper/package actually exist?
                   (Resolve it. Do not trust a remembered URL.)
 2 IDENTITY        Is this the canonical upstream, or a fork/mirror/aggregator?
                   Check owner, org verification, and whether the README claims to be official.
 3 STATUS          Archived? Disabled? Last push date? Releases? Contributor count?
                   Use metadata/repositories.json if the subject is a GitHub project.
 4 LICENSE         Is there one? Which? Can we vendor, redistribute, or only reference?
                   NONE  → reference only.  NOASSERTION → read the text before vendoring.
 5 MAINTAINER      Who is responsible? One person, a team, a foundation, a vendor?
                   Is there a SECURITY.md and a disclosure path?
 6 DATING          What is the date ON the page, not the date you found it?
                   Does the content apply to the version you are using?
 7 SCOPE           Does the source actually claim what you are about to say it claims?
                   Read the surrounding paragraph. Most mis-citations are scope errors.
 8 METHOD          For numbers: how was it measured? Sample size, hardware, baseline,
                   prompt format, repetitions, who paid for it?
 9 INDEPENDENCE    Is there a second source with different provenance?
                   Three blogs quoting one changelog = one source.
10 SELF-CONSISTENCY Does the record agree with itself? (Title vs authors vs year vs
                   citation count vs claimed results.) Internal contradiction is a red flag.
11 INCENTIVE        Does the publisher benefit from you believing this?
                   Vendor benchmarks, sponsored comparisons, affiliate links.
12 REPRODUCIBILITY Could you re-derive the claim yourself? Is there code, a dataset,
                   a runnable example, or an API you can query?
```

## Confidence ladder

```text
VERY HIGH    primary source reached directly + ≥1 independent corroboration +
             self-consistent + within its freshness window + no incentive conflict
HIGH         primary or official source reached directly, self-consistent, current;
             corroboration absent but the source is the minting authority
MEDIUM       single credible secondary source, or a primary source you could not
             reach directly, or a primary source slightly past its freshness window
LOW          community source only, or a credible source well past its window,
             or a claim that depends on unstated assumptions
UNVERIFIED   no source; the statement came from the model. Must be labelled GENERATED.
CONFLICTING  ≥2 credible sources disagree. Record both. Do not average them.
```

Rules:

```text
1. Confidence attaches to a (claim, source, date) triple — not to a source in general.
   A very-high source can support a low-confidence claim if it is out of scope.
2. UNVERIFIED content may never be presented as fact. Prefix it: GENERATED / UNVERIFIED.
3. CONFLICTING is a valid final state. Publishing a resolved-looking answer from
   conflicting evidence is a defect.
4. A number without a measurement method is LOW at best, whatever the source's prestige.
5. Recency is claim-dependent: a 2019 paper on algorithmic complexity stays VERY HIGH;
   a 2024 blog on framework defaults is already suspect.
```

## Outputs

```markdown
### Validated claim
> <the exact claim, scoped to version and date>

- Source: <url> (<type>, <publisher>, page dated <date>)
- Checks passed: <list of the 12 that applied>
- Checks failed / not applicable: <list>
- Independent corroboration: <url or "none — single-sourced">
- Incentive note: <who benefits if you believe this>
- Confidence: <level>
- Required for intended use: <level>
- Verdict: ACCEPT | ACCEPT-WITH-CAVEAT | DOWNGRADE | REJECT | QUARANTINE
- Re-verify by: <date>
```

`QUARANTINE` means: interesting, not gradeable, goes to `experimental/` or
`metadata/pending-paper-candidates.json`. Quarantined material is excluded from the
retrieval index and must never be cited.

## Failure Modes

```text
PRESTIGE TRANSFER    "It's from Stanford, so the specific number is right."
                     Prestige grades the publisher, not the measurement.
DATE CONFUSION       Using the crawl date as the publication date.
SCOPE CREEP          Source says "in our benchmark on task X"; you record "in general".
VERSION DRIFT        Source describes v4; you apply it to v6.
SINGLE-SOURCE STACK  Building a plan on one medium-confidence claim without flagging it.
CONFIDENCE INFLATION Labelling a model-generated statement `high` because it sounds right.
CHECKLIST THEATRE    Filling the form without actually resolving the URL.
OVER-VALIDATION      Re-verifying a stable specification every day and burning the budget.
```

## Quality Checklist

```text
□ Claim written exactly, with version and date scope
□ Required confidence determined by the intended use before grading
□ All 12 applicable checks run and recorded
□ URL actually resolved (not recalled)
□ License recorded; vendoring decision made explicitly
□ Independent corroboration found, or its absence stated
□ Incentive noted
□ Confidence assigned from the ladder, not from a feeling
□ Verdict recorded; QUARANTINE used rather than publishing ungradeable material
□ Re-verification date set from the freshness policy
```

## Anti-Patterns

```text
✗ Accepting a claim because it matches what you already believed
✗ Recording a number with no measurement method
✗ Citing an aggregator when the primary source is reachable
✗ Letting a conflict disappear by choosing the more convenient side
✗ Marking model output as `fact`
✗ Validating the source but not the claim's scope
```

## References

- [`knowledge/ai-engineering/source-scoring.md`](../../knowledge/ai-engineering/source-scoring.md)
- [`knowledge/ai-engineering/freshness-policy.md`](../../knowledge/ai-engineering/freshness-policy.md)
- [`knowledge/research/source-conflict-case-study.md`](../../knowledge/research/source-conflict-case-study.md)
- [`agents/fact-checker/AGENT.md`](../../agents/fact-checker/AGENT.md)
- [`scripts/lib/scoring.py`](../../scripts/lib/scoring.py) — the executable version of this policy
- Tree of Thoughts, arXiv:2305.10601 (verified 2026-09-15)

## Related Skills

`web-research` · `research-before-code` · `repository-analysis` · `research-synthesis`

## Evaluation Criteria

```text
1. Calibration: claims labelled high should be right substantially more often than claims
   labelled medium. Measured in evaluations/knowledge-base/ task runs.
2. Rejection rate: fabricated or unresolvable citations must be caught before publication.
   Target: 100% of nonexistent URLs rejected.
3. Conflict surfacing: disagreements in the source set are recorded, never averaged away.
4. Cost: validation must not dominate the task budget — measured as sources opened per
   load-bearing claim (target ≤ 4).
```

Test cases in [`tests/`](tests/).
