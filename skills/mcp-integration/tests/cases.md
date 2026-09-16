# Test cases — `mcp-integration`

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
GIVEN    A task inside this skill's stated purpose: Treat an MCP server as what it is: **third-party executable code with a credential and a capability grant**, speaking a protocol the model can influence.
WHEN     the agent executes `mcp-integration` end to end on that task
THEN     and before delivery these specific conditions hold: "Capability written as one sentence with an explicit boundary"; "Sandbox with resource limits and no ambient credentials"; "Named human owner; re-vetting scheduled (90 days for fast-moving servers)"
FAIL IF  "Capability written as one sentence with an explicit boundary" is false, or "Named human owner; re-vetting scheduled (90 days for fast-moving servers)" is false, or "Sandbox with resource limits and no ambient credentials" is false
```

## Case 2 — Declines: When the agent needs one narrow read from one API — a plain function call is…

```text
GIVEN    A task that looks like a match but is this skill's excluded case: When the agent needs one narrow read from one API — a plain function call is simpler, cheaper and easier to secure than a protocol server
WHEN     the agent considers `mcp-integration` for that task
THEN     the skill is not selected, because this task is the excluded case "When the agent needs one narrow read from one API — a plain function call is simpler, cheaper and easier to secure than a protocol server", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "When the agent needs one narrow read from one API — a plain function call is simpler, cheaper and easier to secure than a protocol server"; or `mcp-integration` is declined without naming that exclusion
```

## Case 3 — Declines: When a deterministic pipeline can do the job: MCP adds a model in the loop,

```text
GIVEN    A task that looks like a match but is this skill's excluded case: When a deterministic pipeline can do the job: MCP adds a model in the loop, and with it nondeterminism and injection surface
WHEN     the agent considers `mcp-integration` for that task
THEN     the skill is not selected, because this task is the excluded case "When a deterministic pipeline can do the job: MCP adds a model in the loop, and with it nondeterminism and injection surface", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "When a deterministic pipeline can do the job: MCP adds a model in the loop, and with it nondeterminism and injection surface"; or `mcp-integration` is declined without naming that exclusion
```

## Case 4 — Declines: For anything requiring strong guarantees (payments, deletions,

```text
GIVEN    A task that looks like a match but is this skill's excluded case: For anything requiring strong guarantees (payments, deletions, deploys) without a human-confirmation gate
WHEN     the agent considers `mcp-integration` for that task
THEN     the skill is not selected, because this task is the excluded case "For anything requiring strong guarantees (payments, deletions, deploys) without a human-confirmation gate", and the reason given is that exclusion rather than a generic decline
FAIL IF  the skill is run on a task where "For anything requiring strong guarantees (payments, deletions, deploys) without a human-confirmation gate"; or `mcp-integration` is declined without naming that exclusion
```

## Case 5 — Detects: CAPABILITY CREEP

```text
GIVEN    A run of this skill in which the known failure mode is present: CAPABILITY CREEP
WHEN     the agent executes `mcp-integration` and reaches the point where this failure occurs
THEN     "CAPABILITY CREEP" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Enabling a server "for search" and inheriting shell execution."
FAIL IF  "CAPABILITY CREEP" appears in the work and is reported as complete — specifically "Enabling a server "for search" and inheriting shell execution."
```

## Case 6 — Detects: AMBIENT CREDENTIALS

```text
GIVEN    A run of this skill in which the known failure mode is present: AMBIENT CREDENTIALS
WHEN     the agent executes `mcp-integration` and reaches the point where this failure occurs
THEN     "AMBIENT CREDENTIALS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "The agent runs with the developer's full token."
FAIL IF  "AMBIENT CREDENTIALS" appears in the work and is reported as complete — specifically "The agent runs with the developer's full token."
```

## Case 7 — Detects: UNPINNED RUNTIME

```text
GIVEN    A run of this skill in which the known failure mode is present: UNPINNED RUNTIME
WHEN     the agent executes `mcp-integration` and reaches the point where this failure occurs
THEN     "UNPINNED RUNTIME" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "`npx some-mcp@latest` fetching unreviewed code on every start."
FAIL IF  "UNPINNED RUNTIME" appears in the work and is reported as complete — specifically "`npx some-mcp@latest` fetching unreviewed code on every start."
```

## Case 8 — Detects: TOOL-OUTPUT-AS-INSTRUCTION

```text
GIVEN    A run of this skill in which the known failure mode is present: TOOL-OUTPUT-AS-INSTRUCTION
WHEN     the agent executes `mcp-integration` and reaches the point where this failure occurs
THEN     "TOOL-OUTPUT-AS-INSTRUCTION" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A web page's text becomes a command the agent obeys."
FAIL IF  "TOOL-OUTPUT-AS-INSTRUCTION" appears in the work and is reported as complete — specifically "A web page's text becomes a command the agent obeys."
```

## Case 9 — Detects: NO CONFIRMATION GATE

```text
GIVEN    A run of this skill in which the known failure mode is present: NO CONFIRMATION GATE
WHEN     the agent executes `mcp-integration` and reaches the point where this failure occurs
THEN     "NO CONFIRMATION GATE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Tier 2/3 actions executed on untrusted triggers."
FAIL IF  "NO CONFIRMATION GATE" appears in the work and is reported as complete — specifically "Tier 2/3 actions executed on untrusted triggers."
```

## Case 10 — Detects: BROAD FILESYSTEM ROOT

```text
GIVEN    A run of this skill in which the known failure mode is present: BROAD FILESYSTEM ROOT
WHEN     the agent executes `mcp-integration` and reaches the point where this failure occurs
THEN     "BROAD FILESYSTEM ROOT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A tool rooted at `/` or the home directory."
FAIL IF  "BROAD FILESYSTEM ROOT" appears in the work and is reported as complete — specifically "A tool rooted at `/` or the home directory."
```

## Case 11 — Detects: METADATA ENDPOINT

```text
GIVEN    A run of this skill in which the known failure mode is present: METADATA ENDPOINT
WHEN     the agent executes `mcp-integration` and reaches the point where this failure occurs
THEN     "METADATA ENDPOINT" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "SSRF to 169.254.169.254 through a fetch tool → cloud credentials."
FAIL IF  "METADATA ENDPOINT" appears in the work and is reported as complete — specifically "SSRF to 169.254.169.254 through a fetch tool → cloud credentials."
```

## Case 12 — Detects: CONTEXT FLOOD

```text
GIVEN    A run of this skill in which the known failure mode is present: CONTEXT FLOOD
WHEN     the agent executes `mcp-integration` and reaches the point where this failure occurs
THEN     "CONTEXT FLOOD" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A tool returning 40k tokens of JSON per call, evicting the task."
FAIL IF  "CONTEXT FLOOD" appears in the work and is reported as complete — specifically "A tool returning 40k tokens of JSON per call, evicting the task."
```

## Case 13 — Detects: SILENT PARTIAL FAILURE

```text
GIVEN    A run of this skill in which the known failure mode is present: SILENT PARTIAL FAILURE
WHEN     the agent executes `mcp-integration` and reaches the point where this failure occurs
THEN     "SILENT PARTIAL FAILURE" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "A tool errors; the agent proceeds as if it succeeded."
FAIL IF  "SILENT PARTIAL FAILURE" appears in the work and is reported as complete — specifically "A tool errors; the agent proceeds as if it succeeded."
```

## Case 14 — Detects: STAR RANKING

```text
GIVEN    A run of this skill in which the known failure mode is present: STAR RANKING
WHEN     the agent executes `mcp-integration` and reaches the point where this failure occurs
THEN     "STAR RANKING" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Choosing an MCP by popularity rather than by scope and maintenance."
FAIL IF  "STAR RANKING" appears in the work and is reported as complete — specifically "Choosing an MCP by popularity rather than by scope and maintenance."
```

## Case 15 — Detects: VENDOR LOCK BLINDNESS

```text
GIVEN    A run of this skill in which the known failure mode is present: VENDOR LOCK BLINDNESS
WHEN     the agent executes `mcp-integration` and reaches the point where this failure occurs
THEN     "VENDOR LOCK BLINDNESS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "No removal plan for a server that becomes unmaintained."
FAIL IF  "VENDOR LOCK BLINDNESS" appears in the work and is reported as complete — specifically "No removal plan for a server that becomes unmaintained."
```

## Case 16 — Detects: UNLOGGED ACTIONS

```text
GIVEN    A run of this skill in which the known failure mode is present: UNLOGGED ACTIONS
WHEN     the agent executes `mcp-integration` and reaches the point where this failure occurs
THEN     "UNLOGGED ACTIONS" is recognised as a failure of this skill rather than accepted as a result, because the skill states what it looks like: "Side effects with no attribution — unauditable and unreproducible."
FAIL IF  "UNLOGGED ACTIONS" appears in the work and is reported as complete — specifically "Side effects with no attribution — unauditable and unreproducible."
```

## Case 17 — Avoids: Enabling a 40-tool server to use 2 of its tools

```text
GIVEN    A situation that invites the anti-pattern "Enabling a 40-tool server to use 2 of its tools"
WHEN     the agent applies `mcp-integration` in that situation
THEN     "Enabling a 40-tool server to use 2 of its tools" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Enabling a 40-tool server to use 2 of its tools" appears in the output; or it is absent by accident, with nothing in `mcp-integration` having ruled it out
```

## Case 18 — Avoids: Passing the developer's personal GitHub token to an MCP server

```text
GIVEN    A situation that invites the anti-pattern "Passing the developer's personal GitHub token to an MCP server"
WHEN     the agent applies `mcp-integration` in that situation
THEN     "Passing the developer's personal GitHub token to an MCP server" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Passing the developer's personal GitHub token to an MCP server" appears in the output; or it is absent by accident, with nothing in `mcp-integration` having ruled it out
```

## Case 19 — Avoids: `npx @someone/mcp@latest` in a startup script

```text
GIVEN    A situation that invites the anti-pattern "`npx @someone/mcp@latest` in a startup script"
WHEN     the agent applies `mcp-integration` in that situation
THEN     "`npx @someone/mcp@latest` in a startup script" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "`npx @someone/mcp@latest` in a startup script" appears in the output; or it is absent by accident, with nothing in `mcp-integration` having ruled it out
```

## Case 20 — Avoids: Letting a fetched web page decide which tool to call next without a gate

```text
GIVEN    A situation that invites the anti-pattern "Letting a fetched web page decide which tool to call next without a gate"
WHEN     the agent applies `mcp-integration` in that situation
THEN     "Letting a fetched web page decide which tool to call next without a gate" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Letting a fetched web page decide which tool to call next without a gate" appears in the output; or it is absent by accident, with nothing in `mcp-integration` having ruled it out
```

## Case 21 — Avoids: A filesystem tool rooted at the user's home directory

```text
GIVEN    A situation that invites the anti-pattern "A filesystem tool rooted at the user's home directory"
WHEN     the agent applies `mcp-integration` in that situation
THEN     "A filesystem tool rooted at the user's home directory" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "A filesystem tool rooted at the user's home directory" appears in the output; or it is absent by accident, with nothing in `mcp-integration` having ruled it out
```

## Case 22 — Avoids: Ignoring a tool error and continuing the plan

```text
GIVEN    A situation that invites the anti-pattern "Ignoring a tool error and continuing the plan"
WHEN     the agent applies `mcp-integration` in that situation
THEN     "Ignoring a tool error and continuing the plan" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Ignoring a tool error and continuing the plan" appears in the output; or it is absent by accident, with nothing in `mcp-integration` having ruled it out
```

## Case 23 — Avoids: Pasting raw tool JSON into the context without truncation

```text
GIVEN    A situation that invites the anti-pattern "Pasting raw tool JSON into the context without truncation"
WHEN     the agent applies `mcp-integration` in that situation
THEN     "Pasting raw tool JSON into the context without truncation" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Pasting raw tool JSON into the context without truncation" appears in the output; or it is absent by accident, with nothing in `mcp-integration` having ruled it out
```

## Case 24 — Avoids: Adopting an MCP server because it has 5k stars and no license file

```text
GIVEN    A situation that invites the anti-pattern "Adopting an MCP server because it has 5k stars and no license file"
WHEN     the agent applies `mcp-integration` in that situation
THEN     "Adopting an MCP server because it has 5k stars and no license file" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "Adopting an MCP server because it has 5k stars and no license file" appears in the output; or it is absent by accident, with nothing in `mcp-integration` having ruled it out
```

## Case 25 — Avoids: No log of which agent called which tool with which arguments

```text
GIVEN    A situation that invites the anti-pattern "No log of which agent called which tool with which arguments"
WHEN     the agent applies `mcp-integration` in that situation
THEN     "No log of which agent called which tool with which arguments" is absent from the output, and the work shows the alternative this skill prescribes was chosen deliberately
FAIL IF  "No log of which agent called which tool with which arguments" appears in the output; or it is absent by accident, with nothing in `mcp-integration` having ruled it out
```
