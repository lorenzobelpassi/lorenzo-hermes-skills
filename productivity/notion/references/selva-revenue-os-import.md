# Selva Revenue OS Notion import notes

Use this when pushing local Revenue OS / document-assimilation outputs into Notion with the 2025-09-03 API.

## Known live Selva IDs

- Parent page: `Selva Trading Desk CRM`
  - Page ID: `35758362-6119-804d-95ed-de517856e719`
- Revenue OS page created under it:
  - Page ID: `35858362-6119-8136-b8dc-dfc0afd27ec7`
- Source Documents database:
  - Database ID: `ec9a5a2c-2527-420b-989f-024035caa137`
  - Data source ID: `5aa79404-1098-4358-8d8f-5d4919936a5f`
- Integration/workspace observed via `/v1/users/me`:
  - Bot: `Selva Deal Agent - Associated workspace`
  - Workspace: `Chloe’s Space`

## Import sequence that worked

1. Load `NOTION_API_KEY` from `~/.hermes/.env` if it is not already in the environment.
2. Verify workspace with `GET /v1/users/me`.
3. Verify parent page access with `GET /v1/pages/{page_id}`.
4. Search for/reuse an existing `Selva Revenue OS` page; otherwise create it under the parent page.
5. Search for/reuse `Source Documents` data source/database.
6. Ensure the data source schema before creating rows:
   - `PATCH /v1/data_sources/{data_source_id}` with custom properties.
7. Deduplicate imports by stable `Relative Path` by querying the data source first.
8. Create rows with `POST /v1/pages` using `parent: {"database_id": database_id}`.
9. Append a concise status page under `Selva Revenue OS`, not the full raw archive.

## Important API quirk

In Notion API `2025-09-03`, creating a database with many custom properties via `POST /v1/databases` may still yield a data source with only the default title field (`Name`). If row creation then fails with errors like:

`Document Name is not a property that exists. Original Path is not a property that exists...`

Fix:

1. Use the default title property name (`Name`) for page creation.
2. Patch the data source schema directly:

```bash
curl -X PATCH "https://api.notion.com/v1/data_sources/$DATA_SOURCE_ID" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{"properties":{"Original Path":{"rich_text":{}},"Relative Path":{"rich_text":{}},"Category":{"select":{}},"Imported?":{"checkbox":{}}}}'
```

Then use `POST /v1/pages` against the database ID.

## CSV ingestion pitfall

Text extracted from business archives can include NUL bytes (especially when binary-ish or UTF-16-ish content got written into CSV excerpts). Python `csv.DictReader` then fails with:

`_csv.Error: line contains NUL`

Fix before parsing:

```python
csv_text = path.read_text(encoding="utf-8", errors="replace").replace("\x00", "")
rows = list(csv.DictReader(io.StringIO(csv_text)))
```

## UI rule

Do not dump raw archive tables into the daily cockpit. Push documents to `Source Documents` first, then expose only action-ready summaries/pages under the Revenue OS.
