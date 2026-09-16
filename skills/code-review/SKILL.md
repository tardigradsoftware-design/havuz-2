---
name: code-review
version: 1.0.0
description: >-
  Review changes for correctness, security, maintainability and design — with feedback that is
  specific, graded, actionable and reviewable by a third party.
category: coding
status: active
confidence: high
claim_type: recommendation
evidence_level: practitioner-experience
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [code-review, quality, feedback, maintainability, security, process]
applies_to: [any]
priority: 85
requires: []
conflicts_with: []
estimated_tokens: 2739
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Review order
    anchor: "#review-order"
    purpose: implementation
  - heading: Feedback format
    anchor: "#feedback-format"
    purpose: implementation
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "Google Engineering Practices — Code Review"
    url: https://google.github.io/eng-practices/review/
    type: official-docs
    organization: Google
    license: CC BY 4.0
    confidence: high
    claim_type: recommendation
    verified_at: 2026-09-15
    note: "Not fetched in this run; verify current guidance before quoting specifics."
related_skills: [testing, debugging, security-audit, refactoring, documentation]
related_repositories: [reviewdog/reviewdog, danger/danger, semgrep/semgrep]
tests: 6
---

# Code Review

## Purpose

Improve the change **and** the codebase's long-term health, while transferring understanding
to a second person. Review is not gatekeeping and not style enforcement — machines enforce
style. A reviewer's unique value is the things a linter cannot see: an incorrect assumption,
a missing failure path, a design that will cost six months from now.

## When to Use

```text
□ Every change entering a shared branch, including agent-authored code
□ Before merging anything touching auth, money, data deletion or infrastructure
□ As a self-review pass before requesting a human reviewer
□ Reviewing a dependency bump, a config change or a CI/workflow change (these are code)
```

## When NOT to Use

```text
✗ To relitigate an agreed architectural decision — that is an ADR conversation
✗ To enforce formatting, naming style or import order — automate it
✗ On a diff so large it cannot be reviewed properly: ask for it to be split first
  (rough guide: >400 changed lines of non-generated code loses review quality fast)
```

## Inputs

```text
the diff          including generated/vendored code marked as such
the intent        what the change is for, and the acceptance criteria
the context       linked issue, prior discussion, the ADR it implements
the blast radius  what could break: callers, data, deployments, users
test evidence     what was run, what passed, coverage of the new paths
```

**No stated intent, no review.** Reviewing a diff without knowing what it is supposed to do
means reviewing whether the code looks like code.

## Review order

Review in this order; most reviewers invert it and spend their attention on formatting.

```text
1  INTENT          Does the change do what it claims? Is the claim the right thing to do?
                   Is this the smallest change that achieves it? Should it be split?
2  CORRECTNESS     Does it work? Trace the main path, then every branch, then the boundaries:
                   empty, one, many, max, null, unicode, negative, concurrent, retried,
                   out-of-order, permission-denied, partial failure, timeout.
3  SECURITY        Input validation · authorisation per operation (IDOR) · injection ·
                   secrets · logging of sensitive data · new attack surface · new dependency ·
                   agent/tool capability grants. Escalate to security-audit when in doubt.
4  DATA            Schema changes reversible? Migrations safe under load? Constraints added
                   where invariants exist? Backfill batched? Anything irreversible flagged?
5  FAILURE PATHS   What happens when the network, database, queue or third party fails?
                   Timeouts, retries (bounded, jittered, idempotent), circuit breaking,
                   degradation. Silent catch blocks are defects.
6  TESTS           Do the tests prove the new behaviour, or just execute it? Boundaries and
                   error paths covered? Assertions with an oracle? Any test weakened to pass?
                   Regression test for any bug fixed?
7  DESIGN          Is the abstraction at the right level? Does it follow existing patterns,
                   or introduce a second way of doing the same thing? Coupling, cohesion,
                   naming, direction of dependencies. Will this be understandable in a year?
8  OPERATIONS      Observability added where behaviour changed? Logs correlated and redacted?
                   Metrics and alerts for new failure modes? Feature-flagged where risky?
                   Rollback possible without a redeploy?
9  PERFORMANCE     Complexity of the hot path · query count (N+1) · allocations in loops ·
                   unbounded collections · payload sizes · cache behaviour · render counts.
10 READABILITY     Names that say what things are · functions doing one thing · comments
                   explaining WHY, never WHAT · dead code removed · docs updated with the change.
```

Agent-authored code gets the same review plus two extras:

```text
□ Fabrication check: do the referenced APIs, packages, functions, config keys and file paths
  actually exist? Resolve them. Model-generated code invents plausible identifiers.
□ Consistency check: does it follow this repository's conventions (AGENTS.md), or a generic
  convention from its training distribution?
```

## Feedback format

Every comment is specific, graded and actionable. Vague feedback is unactionable and teaches
nothing.

```text
BLOCKER     incorrect, insecure, data-losing, or breaks a caller. Must change before merge.
MAJOR       a design or reliability problem that will cost later. Change before merge,
            or record an accepted risk with an owner and a date.
MINOR       worth fixing, does not block.
NIT         style/preference; explicitly optional; the author decides.
QUESTION    the reviewer does not understand — the answer may be a comment, not a change.
PRAISE      something done well, said specifically. (Rare in reviews, high value.)
```

Format per comment:

```text
[SEVERITY] file:line — what is wrong — why it matters — what to do instead
```

```text
✗ "This looks risky."
✓ "[BLOCKER] src/orders/service.ts:112 — the uniqueness check and the insert are not
   atomic, so two concurrent requests can both create the same order. Add a UNIQUE
   constraint on (customer_id, idempotency_key) and handle the violation."
```

Rules for the reviewer:

```text
1. Comment on the code, not the author.
2. State the reason. "Because our style guide" is weaker than "because this silently drops
   the error the caller depends on".
3. Offer the alternative. A problem without a suggested direction stalls the change.
4. Distinguish requirement from preference, explicitly. NIT means the author decides.
5. Do not drive-by-rewrite someone's design in a comment; request a conversation.
6. Approve only what you actually reviewed. "LGTM" on 2000 lines is a false statement.
7. If you cannot review it properly, say so and ask for a split — do not rubber-stamp.
```

Rules for the author:

```text
1. Make the change reviewable: small, self-contained, with a stated intent and a walkthrough
   of the non-obvious parts.
2. Answer every comment; resolve only with agreement, not unilaterally.
3. Pushback is welcome when it is reasoned. "The reviewer said so" is not a design principle,
   and neither is "it works on my machine".
4. Never weaken a test to make CI pass without saying so in the PR description.
```

## Failure Modes

```text
RUBBER STAMP          Approval without reading. Common with large diffs and with agent output.
STYLE REVIEW          Fifty comments on formatting, zero on correctness.
LATE BLOCKING         Raising an architectural objection after implementation is complete —
                      that belongs in design review, before code.
DIFF-ONLY REVIEW      Reading changed lines without the surrounding code, so context errors
                      are invisible. Open the file.
NITPICK FLOOD         Twenty NITs burying one BLOCKER; the author fixes the easy ones.
UNGRADED FEEDBACK     The author cannot tell what must change from what is taste.
TEST-FREE APPROVAL    Merging new behaviour with no test, because the diff looked clean.
SILENT TEST WEAKENING An assertion removed to make a failing test pass, unremarked.
GENERATED-CODE TRUST  Skimming vendor/generated diffs, which is where the CVE lives.
REVIEW-BY-CI          Assuming green checks mean the change is right.
```

## Quality Checklist

```text
□ Intent and acceptance criteria stated before review began
□ Diff is small enough to review properly, or was split
□ Correctness traced on the main path, all branches and all boundaries
□ Security reviewed: input, authorisation, injection, secrets, new surface, new dependencies
□ Data changes reversible; migrations safe under load; constraints present
□ Failure paths reviewed: timeout, retry, partial failure, degradation — no silent catches
□ Tests prove the behaviour; boundaries and error paths covered; none weakened silently
□ Design consistent with existing patterns; no second way of doing the same thing
□ Observability, alerting and rollback considered
□ Performance reviewed on the hot path: complexity, query count, allocations, bounds
□ For agent-authored code: fabricated identifiers resolved; repo conventions followed
□ Every comment graded (BLOCKER/MAJOR/MINOR/NIT/QUESTION), specific, with a reason and a fix
□ Requirement vs preference clearly separated
□ All comments answered; resolutions agreed, not unilateral
□ Approval covers only what was actually read
```

## Anti-Patterns

```text
✗ "LGTM" with no comments on a 1500-line diff
✗ `try { … } catch (e) {}` approved because it "handles errors"
✗ A comment that says "consider refactoring" with no direction and no severity
✗ Reviewing only the files you already know
✗ Approving a migration you have not checked for locks
✗ Merging a change that deletes an assertion, unremarked
✗ Formatting comments in a codebase with a formatter configured
✗ Trusting a generated lockfile diff without looking at what changed
```

## References

- [`testing`](../testing/SKILL.md) · [`security-audit`](../security-audit/SKILL.md)
- [`refactoring`](../refactoring/SKILL.md) · [`debugging`](../debugging/SKILL.md)
- [`workflows/architecture-review/`](../../workflows/architecture-review/) · [`workflows/security-review/`](../../workflows/security-review/)
- [`anti-patterns/ai-generated-code/`](../../anti-patterns/ai-generated-code/)
- [`agents/code-reviewer` / `security-reviewer`](../../agents/)
- Google Engineering Practices — <https://google.github.io/eng-practices/review/>

## Related Skills

`testing` · `security-audit` · `debugging` · `refactoring` · `documentation` · `dependency-analysis`

## Evaluation Criteria

```text
1. Escape rate: defects merged past review and found in production (target → 0 for BLOCKER class).
2. Attention allocation: fraction of comments about correctness/security/data vs style (target ≥ 0.7).
3. Specificity: 100% of comments graded, located and actionable without a follow-up question.
4. Cycle time: median time from review request to first substantive response (< 1 business day).
5. Seeded-defect recall: on a benchmark diff with planted defects, fraction found (target ≥ 0.8).
6. False-positive rate: comments the author successfully rebuts as invalid (target < 0.2).
```

Test cases in [`tests/`](tests/).
