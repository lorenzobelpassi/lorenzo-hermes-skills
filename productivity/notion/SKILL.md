---
name: notion
description: "Notion API via curl: pages, databases, blocks, search."
version: 1.0.0
author: community
license: MIT
metadata:
  hermes:
    tags: [Notion, Productivity, Notes, Database, API]
    homepage: https://developers.notion.com
prerequisites:
  env_vars: [NOTION_API_KEY]
---

# Notion API

Use the Notion API via curl to create, read, update pages, databases (data sources), and blocks. No extra tools needed — just curl and a Notion API key.

## References

- `references/block-types.md` — Notion block payload examples.
- `references/selva-trading-desk-crm.md` — Selva-specific account-based CRM/trading desk schema, Notion 2025 data-source quirks, and reporting format preferences from the Natoora import build.
- `references/selva-competitor-account-map-import.md` — Treat competitor customer tier/category PDFs as account intelligence, not product pricing; includes the proven 7-line parsing pattern from the Politis import.

## Prerequisites

1. Create an integration at https://notion.so/my-integrations
2. Copy the API key (starts with `ntn_` or `secret_`)
3. Store it in `~/.hermes/.env`:
   ```
   NOTION_API_KEY=ntn_your_key_here
   ```
4. **Important:** Share target pages/databases with your integration in Notion (click "..." → "Connect to" → your integration name)

## API Basics

All requests use this pattern:

```bash
curl -s -X GET "https://api.notion.com/v1/..." \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json"
```

The `Notion-Version` header is required. This skill uses `2025-09-03` (latest). In this version, databases are called "data sources" in the API.

## Common Operations

### Search

```bash
curl -s -X POST "https://api.notion.com/v1/search" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{"query": "page title"}'
```

### Get Page

```bash
curl -s "https://api.notion.com/v1/pages/{page_id}" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03"
```

### Get Page Content (blocks)

```bash
curl -s "https://api.notion.com/v1/blocks/{page_id}/children" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03"
```

### Create Page in a Database

```bash
curl -s -X POST "https://api.notion.com/v1/pages" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{
    "parent": {"database_id": "xxx"},
    "properties": {
      "Name": {"title": [{"text": {"content": "New Item"}}]},
      "Status": {"select": {"name": "Todo"}}
    }
  }'
```

### Query a Database

```bash
curl -s -X POST "https://api.notion.com/v1/data_sources/{data_source_id}/query" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{
    "filter": {"property": "Status", "select": {"equals": "Active"}},
    "sorts": [{"property": "Date", "direction": "descending"}]
  }'
```

### Create a Database

In API version `2025-09-03`, **create databases via `/v1/databases`**, not `/v1/data_sources`. The API returns a database with one default data source.

```bash
curl -s -X POST "https://api.notion.com/v1/databases" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{
    "parent": {"type": "page_id", "page_id": "xxx"},
    "title": [{"text": {"content": "My Database"}}],
    "properties": {
      "Name": {"title": {}},
      "Status": {"select": {"options": [{"name": "Todo"}, {"name": "Done"}]}},
      "Date": {"date": {}}
    }
  }'
```

If you mistakenly call `POST /v1/data_sources`, Notion returns: `Creating new databases with data sources is not supported... Use the Create Database API instead.`

### Update Page Properties

```bash
curl -s -X PATCH "https://api.notion.com/v1/pages/{page_id}" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{"properties": {"Status": {"select": {"name": "Done"}}}}'
```

### Add Content to a Page

```bash
curl -s -X PATCH "https://api.notion.com/v1/blocks/{page_id}/children" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{
    "children": [
      {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"text": {"content": "Hello from Hermes!"}}]}}
    ]
  }'
```

## Property Types

Common property formats for database items:

- **Title:** `{"title": [{"text": {"content": "..."}}]}`
- **Rich text:** `{"rich_text": [{"text": {"content": "..."}}]}`
- **Select:** `{"select": {"name": "Option"}}`
- **Multi-select:** `{"multi_select": [{"name": "A"}, {"name": "B"}]}`
- **Date:** `{"date": {"start": "2026-01-15", "end": "2026-01-16"}}`
- **Checkbox:** `{"checkbox": true}`
- **Number:** `{"number": 42}`
- **URL:** `{"url": "https://..."}`
- **Email:** `{"email": "user@example.com"}`
- **Relation:** `{"relation": [{"id": "page_id"}]}`

## Key Differences in API Version 2025-09-03

- **Databases → Data Sources:** Use `/data_sources/` endpoints for queries and retrieval.
- **Two IDs:** Each database has both a `database_id` and a `data_source_id`.
  - Use `data_source_id` when querying (`POST /v1/data_sources/{id}/query`).
  - When search returns a `data_source`, `id` is the `data_source_id`; `parent.database_id` is the enclosing database ID.
- **Creating pages:** For new 2025-style databases created via `POST /v1/databases`, pages may need `parent: {"data_source_id": "..."}` rather than `parent: {"database_id": "..."}`. If page creation says properties do not exist even though the table exists, retrieve the database (`GET /v1/databases/{database_id}`), take `data_sources[0].id`, and create pages under that data source.
- **Creating database schemas:** `POST /v1/databases` may create a database shell whose underlying data source initially has only a default `Name` title property. If inserts fail with `X is not a property that exists`, patch the data source schema first with `PATCH /v1/data_sources/{data_source_id}` and then insert pages under the data source.
- **Default title field:** In 2025-created data sources the default title property is often `Name` even if the table is called `Accounts`, `Contacts`, etc. Map the logical entity title (`Account`, `Contact`, `Opportunity`) into the actual `Name` title property when inserting rows.

**Selva Deals Database (Lorenzo):**
- Data Source ID: `35758362-6119-81b3-911d-000b5b3d8258`
- Database ID (for creating pages): `35758362-6119-816d-a0ab-e3b6bb3d7ff2`
- Workspace: Chloe's Space (`chloe.lorenzob1987@gmail.com`)
- Integration: "Selva Deal Agent - Associated workspace"

## Revenue archive / Source Documents imports

When importing a local business archive into Notion, create a backend Source Documents database first and keep the daily cockpit/page small. Import raw files as Source Documents, then promote useful rows into Accounts, Product Catalog, Opportunities, or Interactions. For the Selva/Natoora live-import pattern, see `references/selva-revenue-os-import.md`.

**API 2025-09-03 schema pitfall:** creating a database via `/v1/databases` can leave the returned data source exposing only the default `Name` title field. If page creation fails with `X is not a property that exists`, retrieve/patch the data source schema with `PATCH /v1/data_sources/{data_source_id}` before creating rows. When creating pages, use the actual title field name (`Name`) unless you explicitly created another title property. Deduplicate archive imports by a stable `Relative Path` property.

## Selva Revenue OS / archive imports

For Lorenzo's Selva Revenue OS, see `references/selva-revenue-os-import.md` for the working Source Documents import flow, live page/database IDs, data-source schema patch workaround, dedupe-by-relative-path pattern, and the NUL-byte CSV pitfall.

## Pitfalls

- **Data source custom properties may be missing after database creation** — with Notion API `2025-09-03`, `POST /v1/databases` can leave the returned data source with only the default `Name` title field. If `POST /v1/pages` fails with many `... is not a property that exists` validation errors, `PATCH /v1/data_sources/{data_source_id}` to add/update properties, use `Name` for the title property, then retry row creation.
- **Page ID extraction from URL** — strip ALL query params before using. Common traps:
  - `?v=ffb58362...` — this is a database VIEW ID, not the page ID
  - `?source=copy_link`, `&pvs=12`, `&wfv` — URL decorators, discard them
  - The ID is ONLY the 32-char hex string before the first `?`
  - If the URL contains `?v=`, you're looking at a database view — go up one level in the sidebar to find the parent page URL
  - A URL like `notion.so/88c583626119823d8274818d2128edd4?v=...` — the page ID is `88c583626119823d8274818d2128edd4`, but that ID may itself be a database, not a page (returns 400 with "is a database, not a page" — use the parent page instead)
- **404 on page even after sharing** — the integration and the target page must be in the SAME Notion workspace. If you created the integration in "Chloe's Space" but the page lives in a team workspace (or vice versa), the API returns 404 regardless of sharing. Verify with `GET /v1/users/me` — the response shows `bot.workspace_name`. If it doesn't match the workspace containing the page, create a new integration in the correct workspace.
- **Can't find integration at notion.so/profile/integrations** — integrations are workspace-scoped. If the user has multiple Notion accounts/workspaces, the integration may be in a different one. Check notion.so/my-integrations while logged into each account. When in doubt, just create a fresh integration in the target workspace — it takes 2 minutes.
- **"Add connections" vs "Connect to"** — Notion UI wording varies by version. Look for "..." menu → Connections → Add connections, or Settings → Integrations. The user must confirm the pop-up warning before the integration gains access.

## Revenue OS / daily cockpit design

When building Notion for a revenue operating system, keep the daily user interface palatable: a small action cockpit, not a wall of databases. Backend databases can be rich, but the front page should show only filtered action views such as Today, People To See, Product/Sample Angle, Drafts To Approve, Capture, End of Day, and a compact plan scoreboard. See `references/revenue-cockpit-design.md`.

## Selva account-based CRM / trading desk pattern

For Selva, a flat deals table is not enough. Default to an **account-based operating CRM** with these tables:
- Accounts
- Contacts
- Opportunities
- Interactions
- Products / Commodities
- Quotes
- Tasks / Next Actions
- Market Signals
- Competitor Intel

The current/user-approved framing is:
- **Accounts** = source of truth for who buys / who competes / who matters
- **Opportunities** = tradable setups, not generic pipeline rows
- **Market Signals** = shortages, menu changes, price moves, account openings, supplier issues
- **Competitor Intel** = attack points: pricing tiers, service gaps, account penetration, availability gaps

### Selva-specific import rule
When a document or email import is really an account/competitor map, ingest into the operating CRM — not just a legacy deals log.

### Reporting format preference
For Lorenzo, do not report CRM imports back as one dense table. Prefer grouped, legible summaries:
- group by priority / tier (`🔥 Now`, `🟡 Soon`, `🔵 Later` or `🔥 HOT`, `🟡 WARM`, `🔵 COLD`)
- first view should show only company + contact/angle
- detailed notes belong in Notion, not in the chat summary

## Notes

- Page/database IDs are UUIDs (with or without dashes)
- Rate limit: ~3 requests/second average
- The API cannot set database view filters — that's UI-only
- Use `is_inline: true` when creating data sources to embed them in pages
- Add `-s` flag to curl to suppress progress bars (cleaner output for Hermes)
- Pipe output through `jq` for readable JSON: `... | jq '.results[0].properties'`
