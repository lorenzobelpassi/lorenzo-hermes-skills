# Selva Intelligence OS — Phase 002 Pricing Matrix Layer

Session learning from extending Selva Intelligence OS / Prototype 001 into a live pricing infrastructure layer.

## When this applies

Use when Lorenzo asks for pricing infrastructure, SKU matrix design, client-facing price lists, or structured-price ingestion inside Selva Intelligence OS.

Frame it as an **operating/pricing layer** of the Company Intelligence OS, not a standalone spreadsheet.

## Naming convention

Use the business-facing term:

```text
Growers Price List
```

Do not call it "supplier/product price list" in user-facing language. Keep backward-compatible code aliases when existing commands/tests still use old names.

Recommended code rename pattern:

```text
parse_supplier_price_list_csv → parse_growers_price_list_csv
--price-list-csv → --growers-price-list-csv
price_list_summary.json → growers_price_list_summary.json
```

Keep old parser/flag/output as aliases where possible to avoid breaking existing Phase 002 runs.

## Google Sheets pricing-matrix shape

Create one central Google Sheet with input, logic, and output tabs:

```text
Instructions
Client Tier Rules
Product Line Defaults
Growers Price List Input
Cosecha Price List Input
SKU Pricing Matrix
Client Tier Assignment
Conference Price List
League 2 Price List
League 1 Price List
Championship Price List
Premier League Price List
```

Inputs:
- Growers Price List: grower/farm, SKU/product, pack size, units per case, case COGS, availability
- Cosecha Price List: Cosecha SKU/product, pack size, units per case, case price, availability
- SKU list: canonical SKU, product name, product line/category, variety/farm/grower where known

Logic:
- Break case/pack pricing down to unit economics.
- Apply COGS margin % and product-line wastage margin % before client-tier margin.
- Product-line wastage should be editable because herbs, berries, stone fruit, mushrooms, citrus, roots, etc. perish differently.

Outputs:
- One client-facing price-list tab per tier.
- Include SKU, product, product line, unit price, case/pack size, case price, and availability.

## Pricing formula

Use gross margin math unless Lorenzo explicitly says the percentages are markups.

```text
Grower Unit COGS = Grower Case COGS / Grower Units Per Case
Cosecha Unit Price = Cosecha Case Price / Cosecha Units Per Case
Base Unit COGS = Grower Unit COGS by default
Adjusted Unit Cost = Base Unit COGS × (1 + COGS Margin % + Wastage Margin %)
Tier Unit Price = Adjusted Unit Cost / (1 - Tier Gross Margin %)
Tier Case Price = Tier Unit Price × Units Per Case
```

## Selva tier defaults

```text
Conference: under $1,500/month → 48% gross margin
League 2: $1,500–$2,200/month → 42% gross margin
League 1: $2,200–$3,000/month → 38% gross margin
Championship: $3,000–$5,000/month → 35% gross margin
Premier League: $5,000+/month → 28% gross margin
```

## Verification checklist

For Sheets:
- Confirm units-per-case columns are formatted as numbers, not currency.
- Confirm sample rows calculate unit COGS, adjusted unit cost, tier unit prices, and case prices.
- Confirm each tier price-list tab populates from `SKU Pricing Matrix`.
- Confirm availability flows through to client-facing output.

For code:
- Run full tests: `python3 run_tests.py`.
- Run CLI with the new flag:

```bash
python3 -m revenue_os.cli intelligence-weekly SOURCE \
  --sales-csv ORDERS.csv \
  --growers-price-list-csv GROWERS.csv \
  --week-start YYYY-MM-DD \
  --week-end YYYY-MM-DD \
  --out-dir exports/intelligence_os/latest
```

- Verify both `growers_price_list_summary.json` and backward-compatible `price_list_summary.json` when compatibility is required.

## User-facing response style

For Lorenzo, summarize this work in plain business language:
- "Done — I built it."
- Link the Google Sheet.
- Explain inputs, formulas, and tier outputs briefly.
- Confirm tests passed.
- Ask for the real Growers Price List, Cosecha Price List, SKU list, pack/case sizes, and wastage assumptions.

Avoid over-explaining implementation details unless asked.