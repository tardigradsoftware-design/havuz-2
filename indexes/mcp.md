<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Regenerate: python3 scripts/generate-index/build_index.py
     Generated: 2026-09-21T10:01:03+00:00 -->

# MCP server index

**26 MCP servers**, with their permission surface and risk level. The registry holds 35 entries in total: the other 9 are SDKs, testing tools, a registry service, catalogs and one repository whose own published text does not establish that it is a server. They are listed separately below rather than excluded, and rather than counted as servers. Read `knowledge/security/mcp-security/mcp-threat-model.md` before enabling any of them.

| Server | Category | Provenance | Risk | FS | Network | Exec | Status |
|---|---|---|---|---|---|---|---|
| [mcp-agentdeskai-browser-tools-mcp](../knowledge/mcp/registry/AgentDeskAI__browser-tools-mcp.md) | browser | official | low | — | — | — | STABLE |
| [mcp-browserbase-mcp-server-browserbase](../knowledge/mcp/registry/browserbase__mcp-server-browserbase.md) | browser | official | high | — | — | — | ARCHIVED |
| [mcp-chromedevtools-chrome-devtools-mcp](../knowledge/mcp/registry/ChromeDevTools__chrome-devtools-mcp.md) | browser | community | low | — | — | — | ACTIVE |
| [mcp-firecrawl-firecrawl-mcp-server](../knowledge/mcp/registry/firecrawl__firecrawl-mcp-server.md) | browser | official | medium | — | — | — | ACTIVE |
| [mcp-microsoft-playwright-mcp](../knowledge/mcp/registry/microsoft__playwright-mcp.md) | browser | official | low | — | — | — | ACTIVE |
| [mcp-czlonkowski-n8n-mcp](../knowledge/mcp/registry/czlonkowski__n8n-mcp.md) | ci-cd | community | low | — | — | — | ACTIVE |
| [mcp-awslabs-mcp](../knowledge/mcp/registry/awslabs__mcp.md) | cloud | official | medium | — | — | — | ACTIVE |
| [mcp-cloudflare-mcp-server-cloudflare](../knowledge/mcp/registry/cloudflare__mcp-server-cloudflare.md) | cloud | official | medium | — | — | — | ACTIVE |
| [mcp-googlecloudplatform-cloud-run-mcp](../knowledge/mcp/registry/GoogleCloudPlatform__cloud-run-mcp.md) | cloud | community | low | — | — | — | ACTIVE |
| [mcp-korotovsky-slack-mcp-server](../knowledge/mcp/registry/korotovsky__slack-mcp-server.md) | communication | community | low | — | — | — | STABLE |
| [mcp-makenotion-notion-mcp-server](../knowledge/mcp/registry/makenotion__notion-mcp-server.md) | communication | official | medium | — | — | — | ACTIVE |
| [mcp-sooperset-mcp-atlassian](../knowledge/mcp/registry/sooperset__mcp-atlassian.md) | communication | official | low | — | — | — | ACTIVE |
| [mcp-crystaldba-postgres-mcp](../knowledge/mcp/registry/crystaldba__postgres-mcp.md) | database | official | medium | — | — | — | STABLE |
| [mcp-deusdata-codebase-memory-mcp](../knowledge/mcp/registry/DeusData__codebase-memory-mcp.md) | database | community | low | — | — | — | ACTIVE |
| [mcp-mongodb-js-mongodb-mcp-server](../knowledge/mcp/registry/mongodb-js__mongodb-mcp-server.md) | database | official | medium | — | — | — | ACTIVE |
| [mcp-neondatabase-mcp-server-neon](../knowledge/mcp/registry/neondatabase__mcp-server-neon.md) | database | official | medium | — | — | — | ACTIVE |
| [mcp-redis-mcp-redis](../knowledge/mcp/registry/redis__mcp-redis.md) | database | official | medium | — | — | — | ACTIVE |
| [mcp-supabase-mcp](../knowledge/mcp/registry/supabase__mcp.md) | database | official | medium | — | — | — | ACTIVE |
| [mcp-upstash-context7](../knowledge/mcp/registry/upstash__context7.md) | documentation | official | low | — | — | — | ACTIVE |
| [mcp-mksglu-context-mode](../knowledge/mcp/registry/mksglu__context-mode.md) | filesystem | community | high | — | — | — | ACTIVE |
| [mcp-getsentry-sentry-mcp](../knowledge/mcp/registry/getsentry__sentry-mcp.md) | observability | official | high | — | — | — | ACTIVE |
| [mcp-modelcontextprotocol-servers](../knowledge/mcp/registry/modelcontextprotocol__servers.md) | other | official | high | — | — | — | ACTIVE |
| [mcp-exa-labs-exa-mcp-server](../knowledge/mcp/registry/exa-labs__exa-mcp-server.md) | search | official | medium | — | — | — | STABLE |
| [mcp-oraios-serena](../knowledge/mcp/registry/oraios__serena.md) | search | community | high | — | — | — | ACTIVE |
| [mcp-tavily-ai-tavily-mcp](../knowledge/mcp/registry/tavily-ai__tavily-mcp.md) | search | official | medium | — | — | — | ACTIVE |
| [mcp-github-github-mcp-server](../knowledge/mcp/registry/github__github-mcp-server.md) | vcs | official | low | — | — | — | ACTIVE |

## SDKs — for building a server, not for connecting to one

| Repository | Category | Provenance | Why it is not counted as a server |
|---|---|---|---|
| [mcp-vercel-mcp-handler](../knowledge/mcp/registry/vercel__mcp-handler.md) | cloud | official | description says "spin up" |
| [mcp-modelcontextprotocol-python-sdk](../knowledge/mcp/registry/modelcontextprotocol__python-sdk.md) | other | official | description says "SDK" |
| [mcp-modelcontextprotocol-typescript-sdk](../knowledge/mcp/registry/modelcontextprotocol__typescript-sdk.md) | other | official | description says "SDK" |

## Testing and debugging tools

| Repository | Category | Provenance | Why it is not counted as a server |
|---|---|---|---|
| [mcp-firebase-firebase-tools](../knowledge/mcp/registry/firebase__firebase-tools.md) | cloud | official | description says "Command Line" |
| [mcp-modelcontextprotocol-inspector](../knowledge/mcp/registry/modelcontextprotocol__inspector.md) | other | official | description says "Visual testing" |

## Registry services — a peer of this registry, not an entry in it

| Repository | Category | Provenance | Why it is not counted as a server |
|---|---|---|---|
| [mcp-modelcontextprotocol-registry](../knowledge/mcp/registry/modelcontextprotocol__registry.md) | other | official | description says "registry" |

## Catalogs — curated lists of other servers

| Repository | Category | Provenance | Why it is not counted as a server |
|---|---|---|---|
| [mcp-microsoft-mcp](../knowledge/mcp/registry/microsoft__mcp.md) | other | official | description says "Catalog" |
| [mcp-punkpeye-awesome-mcp-servers](../knowledge/mcp/registry/punkpeye__awesome-mcp-servers.md) | other | official | description says "collection of" |

## Not established as servers — nothing observed says what they are

| Repository | Category | Provenance | Why it is not counted as a server |
|---|---|---|---|
| [mcp-stripe-ai](../knowledge/mcp/registry/stripe__ai.md) | payments | official | the topic "mcp" says the repository relates to MCP; nothing observed asserts that it is a server |
