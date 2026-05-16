# Selva competitor account-map imports

Use this when a PDF is **account intelligence**, not product pricing.

## Trigger phrases
- "customer price category list"
- customer tier list / pricing category list
- competitor client list
- salesperson-owned account list
- account pricing ladder / default level list

## What these files usually are
These PDFs often look like pricing docs but are really **client maps**:
- salesperson / rep owner
- account code
- account name
- open date
- customer class (FOODSERVICE / RETAIL / WHOLESALE)
- pricing tier / default level

They should feed the CRM as:
- **Accounts** → one row per client account
- **Competitor Intel** → one summary record about coverage / segmentation
- **Market Signals** → one signal that a ranked target universe is available

Do **not** route them primarily into Products / Commodities unless the file actually contains SKU-level pricing.

## Proven parsing pattern for the Politis PDF
PyMuPDF extracted the file as one field per line, not one account per line.

Observed 7-line record structure:
1. salesperson
2. code
3. account name
4. open date (`M/D/YYYY`)
5. customer class (`FOODSERVICE|RETAIL|WHOLESALE`)
6. `All Categories Default`
7. `Level 0|1|2`

Ignore recurring header/footer lines such as:
- `Sunday, October 5, 2025`
- `06:54 PM`
- `Politis Steak & Seafood`
- `CUSTOMER PRICE CATEGORY LIST`
- `Page:` / page numbers

Rows beginning with labels like `Employees & Friends` and `House - Foodservice` are valid salesperson labels and must be preserved.

## CRM mapping used successfully
### Accounts
- `Name` = account name
- `Current Supplier` / `Competitor Used` = competitor name (e.g. Politis Steak & Seafood)
- `Tier` from level:
  - Level 0 → `🔥 Strategic`
  - Level 1 → `🟡 Priority`
  - Level 2 → `🔵 Watchlist`
- `Status` = `Researching`
- `Source` = `Market intel`
- `Account Intel` should include salesperson, code, open date, class, and level

### Competitor Intel
Create one summary row with:
- parsed account count
- level distribution
- top salesperson coverage
- explanation that the file is an account map / target universe

### Market Signals
Create one signal that a competitor account segmentation map is available and can be used to prioritize outreach.

## Useful heuristics
- `WHOLESALE` → likely `Distributor` / `B2B wholesale`
- `RETAIL` → likely `Other` or market-type account
- names containing `HOTEL`, `RESORT`, `COUNTRY CLUB`, `YACHT CLUB` → `Hotel / Resort` and often `Luxury hospitality`
- otherwise default restaurant-style accounts to `Restaurant` + `Chef-direct`

## Output preference
For Lorenzo, summarize these imports as:
- total parsed
- total created
- total skipped as existing
- tier breakdown
- a short list of standout accounts worth pursuing next

Keep the explanation direct: "This is a competitor customer map" is the right framing.