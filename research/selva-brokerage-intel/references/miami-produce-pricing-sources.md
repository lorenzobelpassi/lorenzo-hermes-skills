# Miami Produce Pricing Source Stack

Use this when generating Selva brokerage/wholesale daily intel or building pricing automation. Goal: avoid trading off stale USDA legacy text files and clearly label public vs login-gated sources.

## Source priority

### 1. USDA MyMarketNews / MARS Miami Terminal Market

- Fruit report: https://mymarketnews.ams.usda.gov/viewReport/2310
- Vegetable report: https://mymarketnews.ams.usda.gov/viewReport/2311
- API pattern: `https://marsapi.ams.usda.gov/services/v1.2/reports/{report_id}`
- Report IDs: fruit `2310`, vegetables `2311`
- Pricing type: Miami terminal market wholesale price ranges by commodity, package, origin, size/grade.
- Access: public report pages; structured API may require a free USDA MARS API key.
- Automation value: highest reliable public baseline if current.

### 2. USDA shipping-point reports — only if current

- Miami fruit legacy TXT/PDF examples: `mh_fv111.txt` / `mh_fv111.pdf`
- Miami vegetables legacy TXT/PDF examples: `mh_fv121.txt` / `mh_fv121.pdf`
- Orlando/Central Florida veg context: `or_fv120.txt` / `or_fv120.pdf`
- Treat these as directional only unless the publication date is current. Some legacy text feeds may be stale or migrated.

### 3. Restaurant Depot / Jetro Miami flyer

- Regional flyer page: https://www.restaurantdepot.com/jetro/view-regional-flyers
- Observed Miami flyer pattern: `Jetro_Miami_*.pdf`
- Pricing type: advertised cash-and-carry specials, not a full daily wholesale book.
- Update frequency: roughly flyer-cycle/biweekly.
- Automation value: useful street comp and buyer psychology signal; parse PDF when available.

### 4. Account-gated distributors and portals

Use public pages for catalog/availability/context only unless Lorenzo provides legitimate account access/export/email sheets.

- FreshPoint South Florida / myFreshPoint
- Cheney Brothers / Cheney Central
- Restaurant Depot full ordering portal
- Mr Greens Produce
- Jack Scalisi Wholesale Fruit & Produce
- South Florida Produce
- Manso Products
- Tocumen Produce USA
- Coosemans Interproduce Miami

Pricing here is typically daily/order-cycle and high value, but not public. Do not claim exact prices from these sources unless actually visible or extracted from an authorized sheet/export.

### 5. Grower / shipper context

Use Florida and specialty grower pages for seasonality, product focus, and supply pressure rather than daily price.

Examples from Week 6 inbound/supplier-map work:

- Mack Farms — Florida potatoes, watermelon, onions, crop/season context.
- C&B Farms — Florida vegetables/herbs context.
- Ray’s Heritage — Florida vegetables.
- Ark Foods — specialty peppers/tomatoes.
- Kai-Kai Farm, Tiny Farm, Paradise Farms — local/specialty farm context.
- County Line, Galpin, Lindcove, Sunny Cal, Valdivia — air/California specialty/citrus context.

## Briefing rules

- Include a “Market confidence” note: current / partial / stale.
- Do not invent live prices. If a source is stale, inaccessible, or login-gated, say so.
- Separate true market-price signals from availability/seasonality signals.
- Restaurant Depot/Jetro is a cash-and-carry comp, not the terminal market.
- Internal Natoora/Selva documents are proprietary context for supplier/product focus; they are not live market price unless the document is current and explicitly priced.

## Suggested daily output sections

1. Market confidence and source freshness.
2. Miami price signals: fruit, vegetables, specialty.
3. Cash-and-carry comps from Restaurant Depot/Jetro when current.
4. Buy / Quote / Watch / Avoid.
5. Supplier/grower opportunities: who to call and why.
6. Brokerage moves for today: 3-5 concrete actions.
7. Dried/pantry gap alerts when relevant.
8. Source links used.
