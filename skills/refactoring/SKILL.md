---
name: refactoring
version: 1.0.0
description: >-
  Change the structure of working code without changing its behaviour — in small verified steps,
  with a safety net, one refactor per commit, and no smuggling of feature work.
category: coding
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
source_type: original
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
tags: [refactoring, code-quality, maintainability, testing, incremental-change]
applies_to: [any]
priority: 79
requires: [testing]
conflicts_with: []
estimated_tokens: 2755
sections:
  - heading: Purpose
    anchor: "#purpose"
    purpose: overview
  - heading: Preconditions
    anchor: "#preconditions"
    purpose: implementation
  - heading: Catalogue
    anchor: "#catalogue"
    purpose: implementation
  - heading: Quality Checklist
    anchor: "#quality-checklist"
    purpose: checklist
provenance: { content_class: original, generated_by: null, human_reviewed: true }
sources:
  - title: "Refactoring — improving the design of existing code (Martin Fowler)"
    url: https://refactoring.com/
    type: methodology
    organization: Martin Fowler / Thoughtworks
    confidence: high
    claim_type: recommendation
    verified_at: 2026-09-15
    note: "Not fetched in this run; canonical catalogue of named refactors. Verify before citing specific recipe steps."
related_skills: [testing, code-review, debugging, migration, documentation]
related_repositories: [semgrep/semgrep, errorprone/errorprone]
tests: 6
---

# Refactoring

## Purpose

Improve the internal structure of code while its **observable behaviour is provably
unchanged**. The discipline is what makes it safe: small steps, verification after each,
and no behavioural change mixed in.

Refactoring is not "cleaning up". Cleaning up without a safety net and without verification
is rewriting, and rewriting is where regressions live.

## When to Use

```text
□ Before adding a feature to code whose current shape makes the feature expensive
□ After a bug fix, to remove the structural cause (the fix makes it right; the refactor makes
  it stay right)
□ When the same confusion has cost a second engineer time
□ When a module's change frequency is high and its test coverage is adequate
□ As the second commit of a two-commit change: behaviour first, structure second (or reverse)
```

## When NOT to Use

```text
✗ Without tests and without the budget to write characterisation tests first
✗ On code about to be deleted
✗ As a way to avoid a difficult feature (refactoring as procrastination)
✗ On code you do not understand yet — understand first; refactoring an unfamiliar system
  destroys the accumulated intent you cannot see
✗ Bundled with a feature in one commit: the reviewer cannot tell which change caused a regression
```

## Preconditions

Do not start until all four hold.

```text
1 SAFETY NET    Tests exist that cover the behaviour you are about to restructure.
                If they do not: write CHARACTERISATION TESTS that capture today's behaviour,
                including the parts you suspect are wrong. They say "this is what it does",
                which is the only safe baseline for "this is what it should do".
2 SMALL STEPS   Each step is minutes, not hours, and is verified before the next begins.
                A refactor you cannot verify incrementally is a rewrite.
3 SEPARATION    Behaviour changes and structure changes are in different commits.
                Two hats; never both at once.
4 REVERSIBILITY Everything committed, on a branch, with a clean working tree before starting.
                `git commit` is the undo button; use it after every green step.
```

## Catalogue

The common refactors, with the smell each addresses. Use the standard names — a shared
vocabulary makes reviews fast ("this is Extract Method" beats a paragraph).

```text
EXTRACT METHOD / FUNCTION     a code fragment that can be named → name it
INLINE                        an indirection whose body is as clear as its name → remove it
EXTRACT VARIABLE / CONSTANT   a complex expression read more than once, or a magic value
RENAME                        the name does not say what the thing is (the highest-value,
                              lowest-risk refactor; do it constantly)
REPLACE MAGIC LITERAL         an unexplained number or string → a named constant
EXTRACT CLASS / MODULE        one type doing two jobs (fields/methods that change together
                              belong together; those that do not, do not)
MOVE METHOD / FIELD           behaviour lives somewhere other than the data it uses most
SLIDE STATEMENTS              related statements scattered → adjacent
REPLACE CONDITIONAL WITH POLYMORPHISM   a switch on type repeated in several places
DECOMPOSE CONDITIONAL         a complex condition → named predicate functions
CONSOLIDATE CONDITIONAL       several conditions with the same result → one
REPLACE NESTED WITH GUARD CLAUSES       deep nesting → early returns for the exceptional cases
INTRODUCE PARAMETER OBJECT    several parameters that always travel together → one type
REMOVE PARAMETER / ADD PARAMETER        the signature does not match the actual needs
CHANGE FUNCTION DECLARATION   a name or signature that misleads callers
ENCAPSULATE FIELD / COLLECTION          mutable internals exposed → accessors and invariants
REPLACE TYPE CODE WITH SUBCLASSES/ENUM  primitives standing in for a closed set
INTRODUCE SPECIAL CASE / NULL OBJECT    null checks scattered everywhere → one representation
REPLACE CONSTRUCTOR WITH FACTORY        construction logic that does not belong in a constructor
SPLIT LOOP / REPLACE LOOP WITH PIPELINE one loop doing three things → three passes (or the reverse,
                                        when the passes are the cost)
PULL UP / PUSH DOWN           inheritance hierarchies with misplaced members
REPLACE INHERITANCE WITH DELEGATION     a subclass that does not honour the parent's contract
                                        (the Liskov violation refactor)
```

Structural and architectural moves (larger, need a plan and often a migration):

```text
INTRODUCE AN ANTI-CORRUPTION LAYER   isolate a third-party or legacy API behind your own interface
SEPARATE READ FROM WRITE (CQRS-lite) divergent read and write models forced into one shape
EXTRACT SERVICE / MODULE BOUNDARY    a seam where a future split becomes possible
STRANGLER FIG                        route around legacy behaviour incrementally until it is unused
INTRODUCE A SEAM                     make a hard-to-test dependency injectable
```

## Workflow

```text
UNDERSTAND → NET → PLAN → STEP → VERIFY → COMMIT → REPEAT → REVIEW → CLEAN UP
```

```text
1 UNDERSTAND    Read until you can state the current behaviour and the intent behind it.
                Ask "why is it like this?" before "why is it not like I would write it?".
                Check git blame and prior ADRs — the oddity may be load-bearing.
2 NET           Confirm or build the safety net. Measure coverage of the paths you will touch.
                Record the baseline: test results, and for performance-sensitive code, the
                current numbers (a refactor that changes performance is not behaviour-preserving
                in the sense that matters).
3 PLAN          Choose the target structure and the ordered list of named refactors that get
                you there. Each step must leave the system working. If a step cannot, you need
                an intermediate step (expand → migrate → contract; see migration).
4 STEP          Apply ONE refactor. Use IDE/automated tooling wherever it exists — automated
                refactors are correct by construction in a way that manual edits are not.
5 VERIFY        Run the tests. Green → commit. Red → revert the step, do not debug forward.
                Debugging forward inside a refactor is how behaviour changes sneak in.
6 COMMIT        One refactor per commit, named with the refactor: "Extract method: validateOrder".
                A reviewer can then verify the diff matches the named transformation.
7 REPEAT        Until the target structure is reached.
8 REVIEW        The reviewer checks: is the behaviour provably unchanged? Are the tests
                unweakened? Is the new structure actually better for the next change, or just
                different?
9 CLEAN UP      Delete the scaffolding: temporary shims, dual-write paths, feature flags that
                are now always on, dead code left behind by the moves.
```

## Failure Modes

```text
NO SAFETY NET           Restructuring uncovered code and hoping.
BIG-BANG REFACTOR       A 3,000-line commit that cannot be reviewed or bisected.
BEHAVIOUR SMUGGLING     A "pure refactor" that quietly fixes a bug — now nobody knows what changed.
DEBUGGING FORWARD       A red test after a step, answered by editing the test or pushing on.
REWRITE AS REFACTOR     "Cleaning up" that discards accumulated intent and edge-case handling.
TASTE-ONLY CHURN        Restructuring to a personal preference with no maintainability argument.
PROCRASTINATION         Endless refactoring to avoid shipping a feature.
ABANDONED MID-FLIGHT    Half-migrated structure left in place — worse than either endpoint.
UNMEASURED PERFORMANCE  A structure that is cleaner and 4× slower on the hot path.
TOOLING AVOIDANCE       Hand-editing what an automated refactor would do correctly.
```

## Quality Checklist

```text
□ Current behaviour and intent understood before changing structure
□ Safety net in place; characterisation tests written where coverage was missing
□ Baseline recorded: test results and, where relevant, performance numbers
□ Target structure and the ordered list of named refactors written down
□ Each step is one named refactor, verified green before committing
□ One refactor per commit, named after the transformation
□ No behaviour change mixed in; bugs found during refactoring filed separately and fixed after
□ Automated/IDE tooling used wherever available
□ Red steps reverted, never debugged forward
□ Tests unweakened: no assertion removed or loosened to pass
□ Performance on hot paths measured before and after
□ Scaffolding, shims, dual-writes and flags cleaned up at the end
□ Review confirms the new structure helps the next change, not just this one
```

## Anti-Patterns

```text
✗ "I refactored it" as a description of a 3,000-line diff with no tests
✗ Renaming a method and changing its behaviour in the same commit
✗ Deleting the `if` that looked redundant and was handling a production edge case
✗ Loosening an assertion so the refactor could pass
✗ A half-finished strangler migration left running for a year
✗ Restructuring a module you have read once
✗ Refactoring generated or vendored code
```

## References

- Refactoring catalogue — <https://refactoring.com/>
- [`testing`](../testing/SKILL.md) — the safety net · [`code-review`](../code-review/SKILL.md)
- [`migration`](../migration/SKILL.md) — expand/migrate/contract for structural changes
- [`debugging`](../debugging/SKILL.md) · [`patterns/architecture/`](../../patterns/architecture/)
- [`anti-patterns/`](../../anti-patterns/) — what the refactors are aimed at
- [`knowledge/coding/`](../../knowledge/coding/)

## Related Skills

`testing` · `code-review` · `migration` · `debugging` · `documentation` · `performance-audit`

## Evaluation Criteria

```text
1. Behaviour preservation: 0 functional regressions attributable to a refactor commit.
2. Step size: median diff per refactor commit small enough to verify by reading.
3. Safety-net coverage: 100% of touched paths covered by tests before restructuring.
4. Bisectability: any regression can be attributed to one named refactor commit.
5. Maintainability gain: measured by change cost, defect rate or review time on the module
   in the following quarter — not by subjective tidiness.
6. Completion: 0 refactors abandoned half-applied.
```

Test cases in [`tests/`](tests/).
