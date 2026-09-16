# Test cases — `motion-design`

Every clause below is derived from this skill's own body text. Nothing here is a
generic control that would read the same for a different skill:

| Case kind | Derived from | What it asserts |
|---|---|---|
| Applies | Purpose, Workflow step titles, Quality Checklist items | the named checklist conditions hold and the named steps ran |
| Declines | each `When NOT to Use` exclusion | the exclusion is honoured and the alternative it names is used |
| Detects | each `Failure Modes` entry, with its own detection signal and response | the failure is caught by that signal and answered by that response |
| Avoids | each `Anti-Patterns` entry, with the consequence it states | the anti-pattern is absent for the reason this skill gives |

Quoted text is the skill's own wording. A case whose quoted material could be
lifted from another skill is a defect and should be reported, not relaxed.

Regenerate: `python3 scripts/generate-index/generate_skill_tests.py`
Measure distinctness: `python3 scripts/generate-index/generate_skill_tests.py --report`

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):


## Case 1 — Applies to the task it was written for

```text
GIVEN    A task inside this skill's stated purpose: Make change **legible**. Motion exists to answer three questions a static frame cannot: where did this come from, what just happened, and what is related to what.
WHEN     the agent executes `motion-design` end to end on that task
THEN     and before delivery these specific conditions hold: "Duration, easing and property tokens defined in the design system; components use only tokens"; "Motions are interruptible, skippable, reversible and semantically consistent"; "Each motion documented with purpose, trigger, tokens and reduced-motion behaviour"
FAIL IF  "Duration, easing and property tokens defined in the design system; components use only tokens" is false, or "Each motion documented with purpose, trigger, tokens and reduced-motion behaviour" is false, or "Motions are interruptible, skippable, reversible and semantically consistent" is false
```

## Case 2 — Declines: To make a page "feel alive" — that is the slop signal (M1/M3 in…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: To make a page "feel alive" — that is the slop signal (M1/M3 in ai-slop-detection)
WHEN     the agent considers `motion-design` for that task
THEN     the skill is not selected, because this task is the excluded case "To make a page "feel alive" — that is the slop signal (M1/M3 in ai-slop-detection)", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "To make a page "feel alive" — that is the slop signal (M1/M3 in ai-slop-detection)"; or `motion-design` is declined without naming that exclusion
```

## Case 3 — Declines: On data that updates continuously (dashboards, logs,

```text
GIVEN    A task that looks like a match but is this skill's excluded case: On data that updates continuously (dashboards, logs, tickers) — motion obscures the value
WHEN     the agent considers `motion-design` for that task
THEN     the skill is not selected, because this task is the excluded case "On data that updates continuously (dashboards, logs, tickers) — motion obscures the value", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "On data that updates continuously (dashboards, logs, tickers) — motion obscures the value"; or `motion-design` is declined without naming that exclusion
```

## Case 4 — Declines: Entrance animations on content the user came to read

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Entrance animations on content the user came to read
WHEN     the agent considers `motion-design` for that task
THEN     the skill is not selected, because this task is the excluded case "Entrance animations on content the user came to read", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Entrance animations on content the user came to read"; or `motion-design` is declined without naming that exclusion
```

## Case 5 — Declines: Anything that delays an interaction's result

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Anything that delays an interaction's result
WHEN     the agent considers `motion-design` for that task
THEN     the skill is not selected, because this task is the excluded case "Anything that delays an interaction's result", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Anything that delays an interaction's result"; or `motion-design` is declined without naming that exclusion
```

## Case 6 — Declines: Where the user has asked for reduced motion — provide the non-motion…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: Where the user has asked for reduced motion — provide the non-motion equivalent
WHEN     the agent considers `motion-design` for that task
THEN     the skill is not selected, because this task is the excluded case "Where the user has asked for reduced motion — provide the non-motion equivalent", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "Where the user has asked for reduced motion — provide the non-motion equivalent"; or `motion-design` is declined without naming that exclusion
```

## Case 7 — Detects: DECORATIVE MOTION

```text
GIVEN    A run of this skill in which the known failure mode is present: DECORATIVE MOTION
WHEN     the agent executes `motion-design` and reaches the point where this failure occurs
THEN     "DECORATIVE MOTION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Animation with no cause — the strongest AI-slop signal (M1, M3). UNIFORM 300ms EASE Every transition identical; no hierarchy, no intent (M2)."
FAIL IF  "DECORATIVE MOTION" appears in the work and is reported as complete — specifically "Animation with no cause — the strongest AI-slop signal (M1, M3). UNIFORM 300ms EASE Every transition identical; no hierarchy, no intent (M2)."
```

## Case 8 — Detects: LINEAR UI MOTION

```text
GIVEN    A run of this skill in which the known failure mode is present: LINEAR UI MOTION
WHEN     the agent executes `motion-design` and reaches the point where this failure occurs
THEN     "LINEAR UI MOTION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Mechanical, unfinished feel."
FAIL IF  "LINEAR UI MOTION" appears in the work and is reported as complete — specifically "Mechanical, unfinished feel."
```

## Case 9 — Detects: LAYOUT-PROPERTY ANIMATION

```text
GIVEN    A run of this skill in which the known failure mode is present: LAYOUT-PROPERTY ANIMATION
WHEN     the agent executes `motion-design` and reaches the point where this failure occurs
THEN     "LAYOUT-PROPERTY ANIMATION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Animating height/top/box-shadow; dropped frames under load."
FAIL IF  "LAYOUT-PROPERTY ANIMATION" appears in the work and is reported as complete — specifically "Animating height/top/box-shadow; dropped frames under load."
```

## Case 10 — Detects: NON-INTERRUPTIBLE

```text
GIVEN    A run of this skill in which the known failure mode is present: NON-INTERRUPTIBLE
WHEN     the agent executes `motion-design` and reaches the point where this failure occurs
THEN     "NON-INTERRUPTIBLE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Queued animations that ignore the user's second click."
FAIL IF  "NON-INTERRUPTIBLE" appears in the work and is reported as complete — specifically "Queued animations that ignore the user's second click."
```

## Case 11 — Detects: BLOCKING ENTRANCE

```text
GIVEN    A run of this skill in which the known failure mode is present: BLOCKING ENTRANCE
WHEN     the agent executes `motion-design` and reaches the point where this failure occurs
THEN     "BLOCKING ENTRANCE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Content unavailable until the animation completes."
FAIL IF  "BLOCKING ENTRANCE" appears in the work and is reported as complete — specifically "Content unavailable until the animation completes."
```

## Case 12 — Detects: MISSING REDUCED PATH

```text
GIVEN    A run of this skill in which the known failure mode is present: MISSING REDUCED PATH
WHEN     the agent executes `motion-design` and reaches the point where this failure occurs
THEN     "MISSING REDUCED PATH" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Motion runs regardless of user preference — an accessibility failure. INCONSISTENT SEMANTICS Two different animations for the same kind of change."
FAIL IF  "MISSING REDUCED PATH" appears in the work and is reported as complete — specifically "Motion runs regardless of user preference — an accessibility failure. INCONSISTENT SEMANTICS Two different animations for the same kind of change."
```

## Case 13 — Detects: FLASHING / AUTOPLAY

```text
GIVEN    A run of this skill in which the known failure mode is present: FLASHING / AUTOPLAY
WHEN     the agent executes `motion-design` and reaches the point where this failure occurs
THEN     "FLASHING / AUTOPLAY" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Seizure risk and no pause control."
FAIL IF  "FLASHING / AUTOPLAY" appears in the work and is reported as complete — specifically "Seizure risk and no pause control."
```

## Case 14 — Detects: DATA-CHART ANIMATION

```text
GIVEN    A run of this skill in which the known failure mode is present: DATA-CHART ANIMATION
WHEN     the agent executes `motion-design` and reaches the point where this failure occurs
THEN     "DATA-CHART ANIMATION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Re-animating the whole chart on every update, hiding the actual change."
FAIL IF  "DATA-CHART ANIMATION" appears in the work and is reported as complete — specifically "Re-animating the whole chart on every update, hiding the actual change."
```

## Case 15 — Detects: MOTION AS MASK

```text
GIVEN    A run of this skill in which the known failure mode is present: MOTION AS MASK
WHEN     the agent executes `motion-design` and reaches the point where this failure occurs
THEN     "MOTION AS MASK" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Animating to distract from a slow operation instead of fixing the slowness."
FAIL IF  "MOTION AS MASK" appears in the work and is reported as complete — specifically "Animating to distract from a slow operation instead of fixing the slowness."
```

## Case 16 — Avoids: Entrance animations on every card, staggered, on page load, for no reason

```text
GIVEN    A situation that invites the anti-pattern "Entrance animations on every card, staggered, on page load, for no reason"
WHEN     the agent applies `motion-design` in that situation
THEN     "Entrance animations on every card, staggered, on page load, for no reason" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Entrance animations on every card, staggered, on page load, for no reason" appears in the output; or it is absent by accident, with nothing in `motion-design` having ruled it out
```

## Case 17 — Avoids: A logo that animates on load

```text
GIVEN    A situation that invites the anti-pattern "A logo that animates on load"
WHEN     the agent applies `motion-design` in that situation
THEN     "A logo that animates on load" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A logo that animates on load" appears in the output; or it is absent by accident, with nothing in `motion-design` having ruled it out
```

## Case 18 — Avoids: Floating blurred orbs drifting in the background

```text
GIVEN    A situation that invites the anti-pattern "Floating blurred orbs drifting in the background"
WHEN     the agent applies `motion-design` in that situation
THEN     "Floating blurred orbs drifting in the background" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Floating blurred orbs drifting in the background" appears in the output; or it is absent by accident, with nothing in `motion-design` having ruled it out
```

## Case 19 — Avoids: `transition: all 300ms ease` applied globally

```text
GIVEN    A situation that invites the anti-pattern "`transition: all 300ms ease` applied globally"
WHEN     the agent applies `motion-design` in that situation
THEN     "`transition: all 300ms ease` applied globally" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`transition: all 300ms ease` applied globally" appears in the output; or it is absent by accident, with nothing in `motion-design` having ruled it out
```

## Case 20 — Avoids: Animating `height: auto` with a JS-driven maxHeight hack and jank

```text
GIVEN    A situation that invites the anti-pattern "Animating `height: auto` with a JS-driven maxHeight hack and jank"
WHEN     the agent applies `motion-design` in that situation
THEN     "Animating `height: auto` with a JS-driven maxHeight hack and jank" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Animating `height: auto` with a JS-driven maxHeight hack and jank" appears in the output; or it is absent by accident, with nothing in `motion-design` having ruled it out
```

## Case 21 — Avoids: A spinner that delays content the server already returned

```text
GIVEN    A situation that invites the anti-pattern "A spinner that delays content the server already returned"
WHEN     the agent applies `motion-design` in that situation
THEN     "A spinner that delays content the server already returned" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A spinner that delays content the server already returned" appears in the output; or it is absent by accident, with nothing in `motion-design` having ruled it out
```

## Case 22 — Avoids: Ignoring `prefers-reduced-motion` because "it looks worse"

```text
GIVEN    A situation that invites the anti-pattern "Ignoring `prefers-reduced-motion` because "it looks worse"
WHEN     the agent applies `motion-design` in that situation
THEN     "Ignoring `prefers-reduced-motion` because "it looks worse" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Ignoring `prefers-reduced-motion` because "it looks worse" appears in the output; or it is absent by accident, with nothing in `motion-design` having ruled it out
```

## Case 23 — Avoids: A chart that re-animates every bar when one value changes

```text
GIVEN    A situation that invites the anti-pattern "A chart that re-animates every bar when one value changes"
WHEN     the agent applies `motion-design` in that situation
THEN     "A chart that re-animates every bar when one value changes" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A chart that re-animates every bar when one value changes" appears in the output; or it is absent by accident, with nothing in `motion-design` having ruled it out
```
