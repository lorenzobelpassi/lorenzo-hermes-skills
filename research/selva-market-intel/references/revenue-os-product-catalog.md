# Revenue OS Product Catalog and Sample Kit Integration

Use this when Market Intel needs to become field execution for Selva Partners.

## Principle

A market brief is not enough. Each actionable product signal should become one or more of:
- Product Catalog row
- Market Signal row
- Sample Kit item
- People-to-see product angle
- Gmail draft / call reason / visit reason

If it does not create a person to see/call, a product to carry, a draft to send, a quote/sample to prepare, or a risk decision, it is only informational.

## Local Revenue OS paths

Root:
`/Users/lorenzobelpassi/selva-agents/revenue_os/`

Product module:
`revenue_os/product_catalog.py`

Commands:
```bash
cd /Users/lorenzobelpassi/selva-agents/revenue_os
python3 run_tests.py
python3 -m revenue_os.cli sample-kit --month 5 --lane "Michelin/JB/fine dining" --max-items 6 --out-md exports/sample_kit_may.md --products-csv exports/seasonal_products_may.csv --natoora-json exports/natoora_seasonal_database.json
```

Generated files:
- `exports/sample_kit_may.md`
- `exports/seasonal_products_may.csv`
- `exports/natoora_seasonal_database.json`

## Data shape for Product Catalog

Fields: Product, Category, Origin, Source Basis, Season Months, Season Phase, Sample Worthy, Sample Priority, Flavor/Talking Point, Best For Lanes, Availability Status, Related Market Signals.

Must capture:
- season phase: early / peak / late / verify
- origin/grower if known
- why it tastes good now
- who cares: Michelin/JB, Natoora takeover, hotels, cruise, Alapattah wholesale
- whether Lorenzo should physically carry it

## May sample kit generated 2026-05-06

1. Florida Mango — May front edge; strong aroma and immediate tasting impact.
2. Florida Tomato — still in Florida season; acid/texture/ripeness are obvious.
3. Jumbo & Colossal Asparagus — Natoora-featured early benchmark.
4. Florida Peaches — short-season urgency; verify eating stage.
5. Baby Artichokes — Natoora-featured peak item; tender/nutty chef hook.
6. Wild Morels — high-impact spring mushroom.

## Natoora public knowledge captured

Natoora public `In Season Today` list included: baby artichokes, baby rainbow beets, collard rabe, English peas, fava beans/greens, fiddlehead ferns, goosetongue, green almonds, green asparagus (jumbo/colossal + local), green garlic, kinome leaf, local salad mix, outdoor rhubarb, purple asparagus, radicchio Masera, ramps, red/white spring onions, spruce tips, sugar snap peas, wild morels.

Natoora featured this week: early Jumbo & Colossal Asparagus; peak Baby Artichokes; late Overwintered Parsnips.

Natoora Miami wholesale page positioned Miami around: 100+ independent growers, 400+ varieties, delivery Monday–Saturday, `flavor-mia@natoora.com`, `+1 786-779-2925`, Chris Devlin leading Miami, Tiny Farm/Roberto relationship.

## Market Intel output rule

When a product is in season/tight/peaking/late or has price movement, output should include:
- commodity/product
- phase or market condition
- urgency
- account lanes/accounts that care
- recommended action
- sample/availability recommendation

Example:
`Florida Mango | early May | high chef hook | Michelin/JB + hotels | carry 2 ripe samples + ask pastry/bar/chef contact.`
