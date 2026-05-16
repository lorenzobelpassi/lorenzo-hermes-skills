# Selva Market Letter — INBOUND Grower Workflow (May 2026)

Use this when drafting Selva's branded weekly market letter/newsletter from market intel, Natoora archive seasonality, and product availability.

## Hard guardrails

- Newsletter is **internal-only until Lorenzo approves**: no third-party sends, no Chloe sends, no automated outreach, no Gmail drafts unless explicitly requested in the current session.
- Pipeline rows derived from restaurant/intel scrapes should stay `Needs Review` / `Nurture` unless Lorenzo approves contact.
- Do not expose raw competitor data externally: no “Natoora sales show…”, no archive quantities, no competitor account names.
- Public-facing copy can use generalized seasonality, product education, market reads, and Selva positioning.

## Source-of-truth for growers

Lorenzo corrected the sourcing standard: for newsletter grower/product stories, use growers/products that appear on the **INBOUND / vendor-facing product list**, not random farms found online.

Primary local source found in this session:

```text
/Users/lorenzobelpassi/Library/Mobile Documents/com~apple~CloudDocs/SELVA PARTNERS/Cosecha/Natoora downloads/NATOORA - VENDOR FACING PRODUCT LIST.xlsx
```

Sheets:
- `VENDOR`
- `PRODUCT LIST`
- `EXPORT`
- `Lists`

Extracted CSVs:

```text
~/.hermes/selva_leads/inbound_extracted/PRODUCT_LIST.csv
~/.hermes/selva_leads/inbound_extracted/EXPORT.csv
~/.hermes/selva_leads/inbound_extracted/inbound_citrus_grower_matrix.csv
```

If iCloud files error with `OSError(11, 'Resource deadlock avoided')`, force local download first:

```bash
brctl download "/Users/lorenzobelpassi/Library/Mobile Documents/com~apple~CloudDocs/SELVA PARTNERS/Cosecha/Natoora downloads/NATOORA - VENDOR FACING PRODUCT LIST.xlsx"
```

## Newsletter product eligibility

Feature products only when they are:
1. INBOUND-list backed, and
2. organic / regenerative / biodynamic / no-spray / minimal-intervention **or** explicitly approved by Lorenzo, and
3. farm/grower/growing-standard language is verified for external copy.

Live INBOUND items can be used internally, but if the row lacks a farm/grower/standard, do **not** make a grower claim externally.

## Citrus examples from extracted INBOUND list

Strong external candidates because grower/standard is present:

| Item | Grower/standard text | Live? | Notes |
|---|---|---:|---|
| Meyer lemons | Regenerative Farm, Exeter, CA | 1 | Strong weekly-letter candidate |
| Makrut lime leaf | Regenerative Farm, Exeter, CA | 1 | Chef/bar aroma item |
| Ruby Red grapefruit | Organic Citrus Farm, San Diego, CA | 1 | Verified organic row |
| Lemongrass | Roberto's Regenerative Farm, Homestead, FL | 1 | Local Miami/Redland angle |

Internal-only until grower verified:

| Item | Live? | Issue |
|---|---:|---|
| Cara Cara oranges | 1 | grower not listed in row |
| Oro Blanco grapefruit | 1 | grower not listed in row |
| Daisy tangerines | 1 | grower not listed in row |
| Sweet Meiwa kumquats | 1 | grower not listed in row |
| Limequats | 1 | grower not listed in row |
| Heirloom navel oranges | 1 | grower not listed in row |
| Seville sour oranges | 1 | grower not listed in row |

## Drafting style Lorenzo liked

Subscriber-facing copy should be tight, specific, and useful:
- named varieties, not generic categories (“Meyer lemon”, not “citrus”)
- farm/grower + place when verified
- practical chef/bar uses
- no hype words: avoid “premium”, “best-in-class”, “high-quality”
- quiet CTA: “Reply and I’ll send what’s actually available.”

## Weekly workflow

1. Read seasonal calendar for what is historically active/peaking.
2. Cross-reference INBOUND/vendor product list for live products and grower standards.
3. Draft internal newsletter with explicit `Internal Notes` section.
4. Mark any product with missing grower/standard as internal-only or “verify before external use.”
5. Lorenzo reviews voice, grower accuracy, and send list.
6. Only after approval: create/send branded newsletter.
