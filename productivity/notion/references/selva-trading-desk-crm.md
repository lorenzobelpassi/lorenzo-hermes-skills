# Selva Trading Desk CRM Notion Build Notes

Session-derived operating model for converting a flat deal log into an account-based CRM/trading desk.

## Page / workspace

- Workspace/account: Chloe Notion (`chloe.lorenzob1987@gmail.com`)
- Parent page: `357583626119804d95edde517856e719`
- Page title after build: `Selva Trading Desk CRM`
- Table ID map saved locally at: `~/.hermes/selva_trading_desk_crm_ids.json`
- Legacy `Selva Deals` remains useful as ingestion/deal-log history, not the operating CRM.

## Operating tables

Create tables at the class level, not one table per import:

1. Accounts — source of truth for targets/customers/suppliers/competitors.
2. Contacts — people, roles, decision authority, relationship strength.
3. Opportunities — tradable setups: buyer + product + trigger + margin thesis + next action.
4. Interactions — emails/calls/texts/tastings and extracted commitments/signals.
5. Products / Commodities — SKU/spec/pack/season/supplier and Selva edge.
6. Quotes — buyer price, supplier price, competitor price, quantity, status.
7. Tasks / Next Actions — daily desk actions with owner, priority, status.
8. Market Signals — shortages, price moves, menu changes, account openings, supplier issues.
9. Competitor Intel — Natoora and other competitor pricing, availability gaps, ops details, account wins/losses.

## Notion API 2025-09-03 quirks hit during build

1. `POST /v1/data_sources` cannot create new databases; use `POST /v1/databases`.
2. `POST /v1/databases` may create a database shell with one underlying data source and only default `Name` property.
3. Retrieve database with `GET /v1/databases/{database_id}` and read `data_sources[0].id`.
4. Patch schema with `PATCH /v1/data_sources/{data_source_id}`.
5. Insert rows with `POST /v1/pages` using `parent: {"data_source_id": "..."}`.
6. Map logical title fields (`Account`, `Contact`, `Opportunity`, `Quote`, etc.) into the actual default `Name` title property.

## User-facing output preference

When reporting CRM imports back to Lorenzo, avoid dense all-column tables. Use grouped, legible sections:

- group by tier / priority (`🔥 HOT`, `🟡 WARM`, `🔵 COLD`)
- show only Company, Contact, Commodity / Angle in the first view
- put detailed notes in Notion, not in the Discord summary

## Seeded Natoora import pattern

From Natoora emails, seed records across multiple tables rather than only one Deal row:

- Account: COTE, Mandolin, Van Leeuwen, MegaYacht, MBC, Mother Wolf, Bistro 8, Concours, Ezios, Karyu, Mae's Room
- Contact: signatures and thread participants
- Opportunity: product/buyer/trading thesis
- Quote: competitor pricing comps (e.g. romaine, pomelos, olive oil)
- Market Signal: operational/pricing/availability signal
- Competitor Intel: actionable weakness/opening + Selva response
- Task: concrete next action with owner and priority
