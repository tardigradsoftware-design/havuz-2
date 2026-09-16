---
id: testing-flaky-tests
title: "Flaky tests: diagnosis, quarantine and repair"
domain: testing
summary: >-
  The causes of non-deterministic test failure ranked by frequency, the quarantine process that keeps a failing test from destroying suite signal, and the specific repairs for each cause class.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [flaky-tests, testing, determinism, ci, test-isolation, time, concurrency, quarantine]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2027-03-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related: []
sources:
  - title: "Martin Fowler — Eradicating Non-Determinism in Tests"
    url: https://martinfowler.com/articles/nonDeterminism.html
    type: methodology
    organization: martinfowler.com
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "The canonical treatment of non-deterministic tests, including the argument that a flaky suite is worse than a smaller honest one because it destroys the meaning of red."
---
# Flaky Tests

## Why flakiness is the worst test property

A suite that intermittently fails trains the team to re-run instead of investigate. Once "just
re-run it" is the normal response to red, real failures are re-run too, and the suite's signal is
gone — it is now noise with a runtime cost. A smaller suite that is always honest is worth more
than a large one that is usually honest.

```text
The cost of a flaky test is not the occasional failure. It is the erosion of the meaning of failure.
```

## Causes, ranked by how often they are the actual cause

```text
1. TIME AND ORDERING          tests that depend on the current date, on wall-clock timing, on
                              execution order, or on a shared fixture mutated by another test.
                              Sleeps that are "long enough" are the signature.
2. SHARED STATE               a database, a file, an environment variable, a module-level cache, a
                              global registry, a port. Parallel runners expose what sequential runs
                              hid.
3. CONCURRENCY RACES          the code under test is genuinely racy and the test usually wins the
                              race. This is the valuable case: the flake is a real bug report.
4. ASYNC WITHOUT PROPER AWAIT  a test that asserts before the operation completed, and usually gets
                              away with it because the machine was fast.
5. NETWORK AND EXTERNAL SVCS   real HTTP calls, real third-party APIs, DNS, TLS, rate limits.
                              Also the cause of the slowest diagnosis.
6. RESOURCE EXHAUSTION         port already in use, file-handle limits, memory pressure, container
                              startup timeout, CI runner contention.
7. FLOATING POINT AND RANDOM   unseeded RNG; float comparison with ==; locale-dependent number and
                              date formatting; timezone-dependent parsing.
8. TEST-INFRASTRUCTURE BUGS    the mocking framework's call-order assumptions, a fixture teardown
                              that does not complete, a snapshot written by a parallel worker.
```

## Diagnosis

```text
1. REPRODUCE UNDER STRESS      run the single test in a loop, 100-1000 times, and under load:
                                 pytest --count=200 -p no:randomly     (pytest-repeat)
                                 go test -count=100 -race ./pkg/...
                                 npx jest --runInBand --verbose path/to/test
                               Then run it in parallel with the rest of the suite, because
                               isolation and concurrency have different causes.
2. RANDOMISE THE ORDER         a shuffled-order run that fails points at shared state or ordering
                               assumptions rather than at the code.
3. READ THE FAILURE, NOT THE RATE.  A flake that fails 1% of the time with the same stack trace is
                               one bug. A flake that fails with different traces is several.
4. INSTRUMENT                  log timestamps, thread IDs, the values of anything time-derived.
                               For races, run under a race detector — TSan, Go's -race, Java's
                               jcstress.
5. CHECK THE ENVIRONMENT       CI runner image version, CPU count, timezone, locale, available
                               memory. A flake that only occurs in CI is usually cause 6 or 1.
```

## Quarantine

A test that is failing non-deterministically and is not yet diagnosed must be removed from the
blocking path — but visibly, with an owner and a deadline. Silently skipping it is how quarantines
become permanent.

```text
□ Move it to an explicitly named quarantine file or marker (pytest.mark.quarantine, a separate CI
  job that reports but does not block).
□ Record: the failure signature, the reproduction rate, the suspected cause, the owner, the date
  quarantined, and the date it must be repaired or deleted.
□ Run the quarantine job on every build so the failure rate is tracked. A quarantine whose flake
  rate is rising is telling you something.
□ Enforce the deadline in CI: a quarantined test older than N days fails the build as a policy
  error, forcing a repair-or-delete decision.
□ On repair, remove the marker and add the regression test that pins the cause.
□ On deletion, record why in the commit message. A deleted flaky test that was covering something
  real is a silent coverage loss.
```

## Repairs by cause

```text
TIME AND ORDERING     inject the clock; never call the system clock inside the code under test.
                      Use a controllable time source in tests. Remove sleeps entirely — wait on a
                      condition with a timeout, not on a duration.
SHARED STATE          each test owns its fixture. Per-test database schema or transaction rollback,
                      temp directories via the framework's tmp_path, no module-level mutable
                      globals. Where a global is unavoidable, reset it in teardown and assert it was
                      reset.
CONCURRENCY RACES     fix the code. The test is correct and the system is not. Add the regression
                      test that fails deterministically under a race detector.
ASYNC                 await the operation, or poll the condition with a bounded timeout. Never
                      assert on a fixed delay.
NETWORK               stub at the boundary you own. Record-and-replay (VCR-style) for realistic
                      payloads, with the recordings committed and reviewed. Contract tests for the
                      interface. Real network only in a small, clearly labelled, non-blocking suite.
RESOURCES             allocate ports from the OS (bind to 0 and read the assigned port) rather than
                      hardcoding. Retry-with-backoff on container startup. Raise CI resource limits
                      only after confirming the test is not leaking.
FLOATS AND RANDOM     seed the RNG per test and record the seed on failure. Compare floats with a
                      tolerance appropriate to the computation. Set locale and timezone explicitly
                      in the test environment (UTC, C locale) and test the locale-dependent paths
                      separately with the locale set.
```

## Prevention

```text
□ No sleeps in tests, enforced by lint. A sleep is an assertion about machine speed.
□ No wall-clock reads inside code under test; time is an injected dependency.
□ Tests run in random order in CI, always. Ordering assumptions are found before they become flakes.
□ Tests run in parallel in CI, always. Shared state is found before it becomes a flake.
□ No real network in the blocking suite.
□ Every test creates and destroys its own state.
□ New flake detected → quarantined the same day, with an owner. The delay is what makes quarantines
  permanent.
```

## References

- [`knowledge/testing/test-levels.md`](test-levels.md) — where each class of flake belongs
- [`skills/testing-strategy/SKILL.md`](../../skills/testing-strategy/SKILL.md) · [`skills/debugging/SKILL.md`](../../skills/debugging/SKILL.md) · [`skills/root-cause-analysis/SKILL.md`](../../skills/root-cause-analysis/SKILL.md)
- [`failure-modes/`](../../failure-modes/) · [`anti-patterns/testing/`](./) · [`gotchas/`](../../gotchas/)
- [`.github/workflows/kb-ci.yml`](../../.github/workflows/kb-ci.yml) — the quarantine-job pattern applied to this repository
- Fowler, "Eradicating Non-Determinism in Tests" — <https://martinfowler.com/articles/nonDeterminism.html>
