---
name: selva-brokerage-intel
description: "Daily brokerage/wholesale produce and dried goods opportunity briefing for Selva Partners"
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [selva, brokerage, wholesale, produce, dried-goods, allapattah, market-intel]
---

# Selva Brokerage / Wholesale Daily Intel

Generate a daily brokerage briefing for Selva Partners' wholesale/cash-flow business. This is separate from the direct-to-chefs margin business.

## Business Context

Selva has two lanes:
1. **Direct to restaurants/chefs** — relationship-driven, high-margin, specialty/minimal-intervention produce.
2. **Brokerage / wholesale** — cash-flow and volume-driven, selling to Allapattah Terminal, distributors, large purchasers, restaurant groups, and wholesale buyers.

The brokerage lane should identify volume opportunities, price spreads, supply gaps, and dried/pantry lines Selva can own.

A key internal source is Natoora weekly inbound PO documents. These are supplier-side purchase orders showing where Natoora bought product from, not customer POs. Use them to build supplier maps and identify lines Selva can recreate, broker, or replace. See `references/natoora-weekly-inbounds.md` for the Week 6 extraction pattern and `references/supplier-sourcing-map.md` for the full supplier-map workflow, public enrichment approach, and known pitfalls around Google Sheet share emails / malformed PDFs.

## Notion Databases

- **Brokerage / Wholesale Pipeline**
  - Database ID: `35858362-6119-8113-8ffc-c4ca32b554b1`
  - URL: https://www.notion.so/35858362611981138ffcc4ca32b554b1

- **Dried Goods Opportunity Map**
  - Database ID: `35858362-6119-81f9-ad0a-ceffa79a0b98`
  - URL: https://www.notion.so/35858362611981f9ad0aceffa79a0b98

## Daily Briefing Structure

### 1. Wholesale Cash-Flow Watch

Track daily/near-daily market movement for high-volume lines:
- Onion, yellow sweet
- Lettuce, Little Gem / romaine / heads
- Tomatoes: heirloom, beefsteak, specialty
- Sweet corn
- Persian cucumbers / seedless cucumbers
- Zucchini
- Potatoes: Yukon Gold / Idaho
- Bell peppers
- Citrus: lemons, limes, Cara Cara, blood orange, grapefruit
- Mango / local mango
- Banana

For each key line, report:
- Supply condition: tight / balanced / long
- Price direction: up / flat / down
- Weather/logistics driver
- Miami/Florida relevance
- Brokerage action: buy / quote / wait / avoid

### 2. Terminal / Wholesale Buyer Angle

Focus on Allapattah Terminal and wholesale buyers:
- What would move today?
- Which lines have volume and urgency?
- Which lines are too commoditized / margin-light?
- Which have a spread between specialty demand and wholesale availability?

### 3. Dried Goods / Pantry Ownership Scan

Priority seed lines from Natoora 2025 Miami data:
- Dried Butter Beans — 299 lb, 39 active weeks — priority Own
- Dried Giganti Beans — 134 lb, 32 active weeks — priority Own
- Dried Sorana Beans — 136 lb, 23 active weeks — Test
- Cantabric anchovies 1kg — 158 units, 45 active weeks — Own/Test
- Premium vinegars, especially apple cider / Minus 8 category — 203 units, 48 active weeks — Test
- Olive oil, especially Senia / Spanish single-varietal formats — 160 units, 36 active weeks — Test
- Tahini — 92 units, 35 active weeks — Watch/Test
- Carnaroli rice — 51 units, 20 active weeks — Test
- Conservas / tuna — Watch
- Dried figs and dried fruits — Watch seasonally

For each opportunity, assess:
- Demand signal
- Existing supplier fragmentation
- Shelf-life advantage
- Import/domestic route
- Margin potential
- Ownership difficulty
- Recommended next action

### 4. Arbitrage / Margin Opportunities

Identify:
- Weather-driven gaps
- Market-to-market price spread opportunities
- Items where specialty buyers pay a premium but wholesale supply is available
- Dried/pantry lines where Selva can consolidate supplier relationships

### 5. Action List

End with 3-7 concrete actions:
- Buyers to call
- Product lines to quote
- Suppliers to research
- Notion items to update
- Lines to avoid today

## Data Sources to Search Daily

Use the source stack in `references/miami-produce-pricing-sources.md` before falling back to generic market news. For supplier/source-map requests, use `references/supplier-sourcing-map.md` and build a CSV + Markdown package rather than only a chat summary.

Primary public pricing sources:
- USDA MyMarketNews / MARS Miami Terminal Fruit report ID `2310`: https://mymarketnews.ams.usda.gov/viewReport/2310
- USDA MyMarketNews / MARS Miami Terminal Vegetable report ID `2311`: https://mymarketnews.ams.usda.gov/viewReport/2311
- USDA MARS API pattern when an API key is available: `https://marsapi.ams.usda.gov/services/v1.2/reports/{report_id}`
- Restaurant Depot / Jetro Miami regional flyer as a cash-and-carry comp: https://www.restaurantdepot.com/jetro/view-regional-flyers

Context/secondary sources:
- USDA Miami/Orlando shipping-point reports only when the publication date is current; legacy `mh_fv111`, `mh_fv121`, and `or_fv120` feeds may be stale or migrated.
- FreshPoint, Cheney Brothers, Mr Greens, Jack Scalisi, South Florida Produce, Manso, Tocumen, Coosemans Interproduce: use public pages for availability/context unless pricing is visible or supplied via authorized login/export/email sheet.
- Florida grower/shipper pages such as Mack Farms and Week 6 inbound suppliers for seasonality/supply pressure.
- The Packer, Fresh Plaza, Produce News.
- EIA diesel / freight indicators.
- NOAA/NWS weather for Florida, California, Mexico, Peru, Chile.
- Port/logistics news for Miami and imports.
- Import/export and specialty pantry supplier information for dried goods.

## Output Style

- Short, actionable, trader-like.
- Use bullets, not long essays.
- Prioritize specific calls: **Buy / Quote / Watch / Avoid**.
- Include numbers where reliably available; do not invent prices.
- If no fresh data is found, say so and reason from last known signal.
- Include source freshness/confidence: current / partial / stale.
- Never treat Restaurant Depot/Jetro flyers as full wholesale market pricing; label them as cash-and-carry comps.
- Do not present login-gated distributor portals as live price sources unless actual authorized data was accessed.
- Total length: 700-1000 words.
