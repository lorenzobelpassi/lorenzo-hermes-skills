# Selva Google Sheets Pricing Engine Pattern

Use this reference when building or repairing Google Sheets pricing workbooks for Selva/Cosecha, especially Growers Price List → SKU matrix → tiered client price lists.

## Context

A working sheet was built at:

`https://docs.google.com/spreadsheets/d/1_0RHrFWa9XNdQS2jUQwHilSfXdANr1coUtk2py4oymg/edit`

Current business terminology:
- Use **Growers Price List**, not supplier product price list.
- Use **Cosecha Price List** for current/internal sell-side reference.
- Client tiers: Conference, League 2, League 1, Championship, Premier League.

Tier gross margin defaults:
- Conference: 48%
- League 2: 42%
- League 1: 38%
- Championship: 35%
- Premier League: 28%

Core formula:

```text
Adjusted Unit Cost = Base Unit COGS × (1 + COGS Margin % + Wastage Margin %)
Client Unit Price = Adjusted Unit Cost ÷ (1 - Tier Gross Margin %)
```

## Preferred workflow

1. Load the sourcing/grower CSV or Growers Price List input.
2. Build normalized product rows with stable SKUs, product name, product line, grower, case size, units per case, case COGS, availability, notes.
3. If actual grower cost or units/case are missing, mark availability/status as `Needs Quote` and leave price inputs blank. Do **not** invent costs.
4. Feed rows into `Growers Price List Input`.
5. Use the `SKU Pricing Matrix` to calculate adjusted unit cost and tier prices.
6. Use separate tier price-list tabs for client-facing outputs.
7. Verify formulas with `valueRenderOption='FORMULA'`, then verify displayed values with normal render.

## Google Sheets API pattern

When the standard `gws` setup files are missing but Lorenzo's Selva OAuth pickle exists, use direct Google API client with the Selva token:

```python
import pickle, warnings
warnings.filterwarnings('ignore')
from googleapiclient.discovery import build

SPREADSHEET_ID = '...'
with open('/Users/lorenzobelpassi/.hermes/selva_outreach_token.pickle', 'rb') as f:
    creds = pickle.load(f)
svc = build('sheets', 'v4', credentials=creds)

values = svc.spreadsheets().values().get(
    spreadsheetId=SPREADSHEET_ID,
    range="'SKU Pricing Matrix'!A1:AC8",
).execute().get('values', [])
```

Security rule: never expose OAuth token contents or credential JSON; refer to secrets as `[REDACTED]` if needed.

## Formula pitfall: blank × blank becomes `$0.00`

In tier output tabs, this formula shows `$0.00` when unit price and units are blank:

```text
IFERROR(UnitPriceRange * UnitsRange, "")
```

Because blank multiplication returns zero, not an error. Use an explicit blank guard:

```text
IF(UnitPriceRange="","",IFERROR(UnitPriceRange*UnitsRange,""))
```

Example tier output formula pattern:

```text
=FILTER({
  'SKU Pricing Matrix'!A2:A,
  'SKU Pricing Matrix'!B2:B,
  'SKU Pricing Matrix'!D2:D,
  'SKU Pricing Matrix'!S2:S,
  'SKU Pricing Matrix'!F2:F,
  IF('SKU Pricing Matrix'!S2:S="","",IFERROR('SKU Pricing Matrix'!S2:S*'SKU Pricing Matrix'!G2:G,"")),
  'SKU Pricing Matrix'!AB2:AB
}, 'SKU Pricing Matrix'!A2:A<>"")
```

Swap the tier price column for other tiers:
- Conference: `S`
- League 2: `U`
- League 1: `W`
- Championship: `Y`
- Premier League: `AA`

## Product classification pitfall

When inferring product lines from product names, check pepper terms before stone-fruit terms. Products like `Peppers, Cherry Hot - Florida` contain `Cherry` but must classify as `Peppers`, not `Stone Fruit`.

Pepper override terms used successfully:
- `pepper`
- `shishito`
- `serrano`
- `jimmy nardello`
- `long hot`

## Business-facing update style

When reporting completion to Lorenzo, keep it concise and operational:
- Say what was built.
- Give counts if useful (e.g. candidate rows and source entries).
- Say what now flows automatically.
- State the remaining data blocker plainly: case size, units per case, grower case COGS, availability.
- Avoid long implementation detail unless asked.