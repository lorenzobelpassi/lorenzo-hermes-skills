# Selva Revenue OS — Product Catalog & Sample Kit Layer (2026-05-06)

Session outcome: Selva Revenue OS was extended so field execution is not generic. A daily people-to-see list should include seasonal product proof points and a short spiel.

## Local package paths

Revenue OS root:
`/Users/lorenzobelpassi/selva-agents/revenue_os/`

New/updated module:
`revenue_os/product_catalog.py`

Generated outputs:
- `exports/sample_kit_may.md`
- `exports/seasonal_products_may.csv`
- `exports/natoora_seasonal_database.json`
- `exports/crm_blueprint.md`
- `exports/crm_blueprint.json`

Verification:
```bash
cd /Users/lorenzobelpassi/selva-agents/revenue_os
python3 run_tests.py
```
Expected: `ALL TESTS PASSED`.

Regenerate May kit:
```bash
python3 -m revenue_os.cli sample-kit \
  --month 5 \
  --lane "Michelin/JB/fine dining" \
  --max-items 6 \
  --out-md exports/sample_kit_may.md \
  --products-csv exports/seasonal_products_may.csv \
  --natoora-json exports/natoora_seasonal_database.json
```

## CRM change

Notion CRM should be seven databases, not five:
1. Accounts
2. Contacts
3. Opportunities
4. Interactions
5. Market Signals
6. Product Catalog
7. Sample Kits

`Product Catalog` fields: Product, Category, Origin, Source Basis, Season Months, Season Phase, Sample Worthy, Sample Priority, Flavor/Talking Point, Best For Lanes, Availability Status, Related Market Signals.

`Sample Kits` fields: Kit Name, Date, Route/Zone, Target Lane, Products, Accounts, Talking Points, Packed?, Outcome Notes.

## May sample kit generated

For Michelin/JB/fine-dining visits in May, first-pass sample kit:
1. Florida Mango — May front edge; aroma/tasting impact.
2. Florida Tomato — still in season; acid/texture/ripeness obvious.
3. Jumbo & Colossal Asparagus — Natoora-style early microseasonal benchmark.
4. Florida Peaches — short-season urgency; verify eating stage before carrying.
5. Baby Artichokes — Natoora-style peak item; tender/nutty chef hook.
6. Wild Morels — high-impact spring mushroom; small amount opens serious chef conversations.

Field rule: bring 3–6 items max, not a truck. Each item needs a reason to taste.

## Grounded seasonality sources captured

FDACS Florida May items include mango, tomato, sweet corn, watermelon, blueberry, cantaloupe, cucumber, eggplant, bell pepper, papaya, peaches, snap bean, squash. Strawberries are generally December–April, so do not lead with Florida strawberries in May unless there is a verified lot.

Natoora public `In Season Today` list on 2026-05-06 included baby artichokes, baby rainbow beets, collard rabe, English peas, fava beans/greens, fiddlehead ferns, goosetongue, green almonds, green asparagus (jumbo/colossal + local), green garlic, kinome leaf, local salad mix, outdoor rhubarb, purple asparagus, radicchio Masera, ramps, red/white spring onions, spruce tips, sugar snap peas, wild morels.

Natoora featured this week: early Jumbo & Colossal Asparagus; peak Baby Artichokes; late Overwintered Parsnips.

## Natoora Miami knowledge captured

Natoora Miami positioning on public wholesale page:
- Direct network of 100+ independent growers from Florida and across the U.S.
- 400+ varieties of fresh produce.
- Miami delivery six days/week, Monday–Saturday.
- Contact: `flavor-mia@natoora.com`, `+1 786-779-2925`.
- Chris Devlin leads Miami.
- Natoora says it has worked with Roberto/Tiny Farm, helping grow it to 7 acres through planning and loans.

Use this as competitive knowledge: Selva should track not only product names but phase (early/peak/late), grower/origin, flavor argument, which accounts care, and what Lorenzo should carry/say.

## Automation rule

Market Intel should update Product Catalog and Market Signals. Revenue OS should attach products/sample kit items to the People To See list. Deal Capture should record product feedback after visits.
