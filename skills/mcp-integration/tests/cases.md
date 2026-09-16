# Test cases — `mcp-integration`

Derived from this skill's own boundaries: its purpose, its "When NOT to Use" exclusions, its
failure-mode table and its anti-patterns. A case whose content cannot be traced to the skill
body is not included.

Format per [`README.md` → How skills are tested](../../../README.md#how-skills-are-tested):

## Case 1 — Applies to the task it was written for

```text
GIVEN    A task matching the stated purpose: Treat an MCP server as what it is: **third-party executable code with a credential and a capability grant**, speaking a protocol the model can influence. Integrating one is a supply-chain decision plus a security-boundar…
WHEN     the agent selects and executes the `mcp-integration` skill
THEN     the workflow steps are followed in order, each producing its observable result, and the quality checklist is satisfied before the output is delivered
FAIL IF  a step is skipped, the output cannot be checked against the checklist, or the skill is applied without its inputs being present
```

## Case 2 — Declines: When the agent needs one narrow read from one API — a plain function c…

```text
GIVEN    A task that looks like a match but is the excluded case: When the agent needs one narrow read from one API — a plain function call is simpler,
WHEN     the agent considers the `mcp-integration` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 3 — Declines: When a deterministic pipeline can do the job: MCP adds a model in the …

```text
GIVEN    A task that looks like a match but is the excluded case: When a deterministic pipeline can do the job: MCP adds a model in the loop, and with it
WHEN     the agent considers the `mcp-integration` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 4 — Declines: For anything requiring strong guarantees (payments, deletions, deploys…

```text
GIVEN    A task that looks like a match but is the excluded case: For anything requiring strong guarantees (payments, deletions, deploys) without a
WHEN     the agent considers the `mcp-integration` skill
THEN     the skill is not selected; the alternative named in the exclusion is used instead, and the reason is stated
FAIL IF  the skill is applied anyway, or it is declined without naming what should be done instead
```

## Case 5 — Avoids: Enabling a 40-tool server to use 2 of its tools

```text
GIVEN    A situation that invites the anti-pattern: Enabling a 40-tool server to use 2 of its tools
WHEN     the agent applies `mcp-integration`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```

## Case 6 — Avoids: Passing the developer's personal GitHub token to an MCP server

```text
GIVEN    A situation that invites the anti-pattern: Passing the developer's personal GitHub token to an MCP server
WHEN     the agent applies `mcp-integration`
THEN     the anti-pattern is not present in the output, and the reason it fails is reflected in the work
FAIL IF  the anti-pattern appears in the output, or is avoided by accident rather than by the skill guidance
```
