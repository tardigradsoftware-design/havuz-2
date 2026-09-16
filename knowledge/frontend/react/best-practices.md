---
id: frontend-react-best-practices
title: "React in practice: rendering, state and the causes of slow interfaces"
domain: frontend
summary: >-
  The rendering model that makes React performance and correctness predictable — what triggers a render, where state belongs, when memoisation actually pays, the key mistakes that carry state to the wrong item, and the checklist for diagnosing a slow interface.
status: active
confidence: high
claim_type: recommendation
evidence_level: cross-checked
tags: [react, rendering, state-management, hooks, performance, memoisation, keys, frontend]
applies_to: [any]
version: 1.0.0
updated: 2026-09-15
verified_at: 2026-09-15
expires_at: 2026-12-15
provenance:
  content_class: original
  generated_by: null
  human_reviewed: true
related: [knowledge/frontend/rendering-strategies.md, knowledge/performance/frontend-budgets.md]
sources:
  - title: "React documentation — Thinking in React"
    url: https://react.dev/learn/thinking-in-react
    type: official-docs
    organization: React
    claim_type: fact
    confidence: very-high
    verified_at: 2026-09-15
    note: "The state-lifting and derivation guidance this document operationalises, from the current react.dev documentation."
---
# React in Practice

## The rendering model

Almost every React performance and correctness problem is a misunderstanding of these four rules.

```text
1. A render is triggered by a STATE UPDATE in that component or an ancestor — not by a prop changing
   in isolation, and not by a mutation. Mutating state schedules nothing and leaves the UI
   inconsistent with the data.

2. RENDERING IS NOT COMMITTING. React calls the component function, computes the new tree, diffs it,
   then commits DOM changes. The function may run more than once per commit — twice in development
   under StrictMode, and whenever a concurrent render is interrupted and restarted. The component
   function must therefore be PURE: same props and state in, same element tree out, no side effects.

3. CHILDREN PASSED AS ELEMENTS ARE NOT RE-RENDERED when the parent re-renders. Children created
   inline in the parent's JSX are. This makes composition-over-configuration a performance pattern as
   well as a design one.

4. STATE IS BOUND TO POSITION IN THE TREE. Moving a component, or changing its key, destroys and
   recreates its state. This is a feature, and the cause of the most common "my form reset itself" bug.
```

## Where state belongs

```text
DERIVE, DO NOT STORE.      Anything computable from existing state or props is not state: a filtered
                           list, a total, a formatted date, a boolean from two other values. Compute
                           it during render. Storing it creates a second source of truth that must be
                           synchronised — and the synchronisation is where the bug lives.
LIFT ONLY AS FAR AS NEEDED. State shared by two siblings goes to their nearest common parent, not to
                           a global store. Lifting higher re-renders a larger subtree and couples
                           components that should not know about each other.
SERVER STATE ≠ UI STATE.   Data from an API is not application state; it is a cache of someone else's
                           truth, with fetching, staleness, revalidation, mutation and error
                           handling. A data layer handles that. useState + useEffect does not, and
                           hand-rolling it produces races on unmount and on rapid re-fetch.
CO-LOCATE WITH THE OWNER.  State one component reads belongs in that component, even if it is
                           conceptually "app state". Reach for a global store when three or more
                           distant components genuinely need the same writable value.
URL IS STATE.              Filters, pagination, sort order, selected tab and search query belong in
                           the URL: shareable, restorable on refresh, correct under the back button.
                           The most commonly omitted piece of state design, and the one users notice.
```

## Effects

```text
An effect synchronises with something OUTSIDE React: a subscription, a timer, a third-party library, a
DOM API React does not manage, an analytics event.

NOT for:
✗ fetching data the data layer or router could fetch
✗ computing derived state
✗ responding to a user action — that belongs in the event handler, where the intent is explicit
✗ synchronising two pieces of state — that is a modelling problem and the effect is the symptom

Every effect needs a cleanup, or an explicit reason it does not. The classic bugs: a subscription never
removed, a fetch resolving after unmount, a timer outliving the component.

The dependency array is a CORRECTNESS CLAIM, not a lint formality. A missing dependency means the effect
closes over a stale value. The fix is almost never to disable the rule — it is to move the logic into the
event handler, or to include the dependency and accept the re-run.
```

## When memoisation pays

Memoisation is a trade: memory and comparison cost now, avoided render work later. It pays only when the
avoided work is expensive AND the inputs are stable.

```text
WORTH IT WHEN
  ✓ the computation is measurably expensive (a large list transform, a heavy parse) — measure first
  ✓ the memoised value goes to a component wrapped in React.memo, so a stable reference prevents a render
  ✓ the value is a dependency of an effect whose re-run is costly
  ✓ the value enters a context, where every change re-renders every consumer

NOT WORTH IT WHEN
  ✗ the render it prevents is cheap — comparing dependencies costs more than re-rendering a component
    that outputs a few DOM nodes
  ✗ the dependencies are objects or arrays created during render — the memo never hits and you paid for
    the comparison and the allocation
  ✗ it is applied preemptively across a codebase. The most common React performance anti-pattern:
    hundreds of memo calls, no measured benefit, harder to read.

React Compiler changes this calculus by memoising automatically where it can prove safety. Where it is
enabled, hand-written useMemo/useCallback is mostly unnecessary — check before adding either.

React.memo on a component pays when it renders often with unchanged props and its render is non-trivial.
It is defeated by inline object, array and function props — which is the only legitimate reason to reach
for useCallback.
```

## Keys

A key is an identity across renders, not an index into a list.

```text
✓ A stable domain ID.
✗ The array index, when the list can be reordered, filtered, inserted into or deleted from. React
  matches by position and carries the wrong state to the wrong item: a field showing another row's
  value, an animation on the wrong row, an input keeping the previous row's text. Invisible in the
  demo; appears the first time someone sorts a table.
✗ A key generated per render (Math.random(), Date.now(), an inline object). Destroys and recreates the
  subtree every render: state lost, inputs unfocused, remount cost on every update.

Deliberately CHANGING a key is the correct way to force a subtree reset — a documented technique, not
a hack.
```

## Lists and large data

```text
□ Virtualise any list that can exceed roughly 100 rows, or whose row height is non-trivial. The DOM
  node count is the constraint, not the array length.
□ Window the DATA, not just the rendering, when the array itself is large — 50,000 items in memory is a
  GC problem before it is a DOM problem.
□ Never fetch "everything" because pagination is awkward. That is a load-time and memory cost paid by
  every user for one developer's convenience.
□ Stable sort order. A list whose order changes between renders for equal elements thrashes
  reconciliation. Sort on a total order: value, then ID.
```

## The slow-interface checklist

```text
1. Render count higher than expected?   React DevTools Profiler → "record why each component rendered".
                                        Answers the question directly instead of by inference.
2. One render expensive?                The Profiler's ranked view. Usually a large list, heavy work
                                        during render, or a context change re-rendering a big subtree.
3. State too high in the tree?          Every keystroke in an input whose state lives at the page root
                                        re-renders the page.
4. Context value a new object each render?  Every consumer re-renders on every provider render. Split
                                        the context or memoise the value.
5. A fetch cascade?                     fetch → state → effect → fetch → state. Move fetching into the
                                        data layer or the router.
6. Main thread blocked by something that is not React?  A third-party long task, a synchronous layout
                                        read, a large JSON parse. The browser Performance panel shows
                                        it; React's profiler does not.
7. The bundle rather than the render?   An INP regression is often parse and compile time, not
                                        component time — see frontend-budgets.md.
```

## References

- [`../rendering-strategies.md`](../rendering-strategies.md) — where the HTML comes from
- [`../../performance/frontend-budgets.md`](../../performance/frontend-budgets.md) — INP, bundle size, long tasks
- [`../../accessibility/wcag-practical-checklist.md`](../../accessibility/wcag-practical-checklist.md) — focus management on route change, live regions
- [`skills/frontend-design/SKILL.md`](../../../skills/frontend-design/SKILL.md) · [`skills/code-review/SKILL.md`](../../../skills/code-review/SKILL.md) · [`skills/performance-optimization/SKILL.md`](../../../skills/performance-optimization/SKILL.md)
- [`patterns/frontend/`](../) · [`anti-patterns/frontend/`](../) · [`gotchas/`](../../../gotchas/)
- react.dev — <https://react.dev/learn> · Thinking in React — <https://react.dev/learn/thinking-in-react> · React Compiler — <https://react.dev/learn/react-compiler>
