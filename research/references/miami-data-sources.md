# Miami Market Data Sources
*Researched May 5, 2026*

## Miami Terminal Pricing

### USDA ESMIS (Primary — Free, No Auth)
- **Base URL:** `https://esmis.nal.usda.gov/`
- **API Docs:** `https://esmis.nal.usda.gov/api-documentation`

| Report | ID | Pub ID | Frequency | Commodities |
|--------|-----|--------|-----------|-------------|
| Wholesale Vegetable - Miami | MH_FV020 | 2157 | Daily | Tomatoes, peppers, lettuce, cucumbers, squash |
| Wholesale Fruit - Miami | MH_FV010 | 2297 | Daily | Oranges, strawberries, lemons |
| Wholesale Onion & Potato - Miami | MH_FV030 | 1970 | Daily | Onions |
| Wholesale Tropical F&V - Miami | MH_FV056 | 892 | Daily | Avocados, mangoes, limes |

**API Endpoints:**
- `GET /api/v1/publication/search?query=Miami%20terminal`
- `GET /api/v1/publication/findById/{publicationId}`
- `GET /api/v1/release/findAll`

**Format:** PDFs with structured data — use pdfplumber for parsing.

**Known Issue:** USDA MARS API returns 403 from Modal cloud IPs. Use ESMIS instead, or add residential proxy.

### Sources That Don't Work
- ProduceMarketGuide.com — directory only, no pricing
- The Packer — bot detection, paywall
- AMS.USDA.gov — blocks automated access
- MyMarketNews.AMS.USDA.gov — SSL errors

---

## FL Final Mile Freight

### Free Rate Quote Sources

| Source | URL | Notes |
|--------|-----|-------|
| **GoShip** | goship.com | Free LTL & FTL quotes, API available |
| **FreightQuote** | freightquote.com/book/ | C.H. Robinson, no signup for quotes |
| **R+L Carriers** | rlcarriers.com | Has Temperature-Controlled (reefer) |
| **Saia LTL** | saia.com/rates | LTL, Expedited, Spot rates |
| **uShip** | uship.com/freight/ | Marketplace, see multiple bids |
| **RXO** | rxo.com | Spot quotes for FTL |

### Sources That Don't Work (Paid/Blocked)
- DAT/SONAR — paid only
- Truckstop.com — paid subscription
- TruckerPath — CloudFront block
- USDA Fruit & Vegetable Truck Rate Report — blocked

### Hardcoded Baseline Rates ($/mile, 2024-2025)
- McAllen → Miami: $2.45
- Laredo → Miami: $2.50
- Pharr → Miami: $2.45
- Nogales → LA: $2.20

---

## Cruise/Port Intel

### PortMiami
- **Perishables Page:** miamidade.gov/portmiami — 3,000+ reefer plugs, USDA hours
- **Stats:** 1.1M TEUs cargo, 8.5M cruise passengers annually

### Cruise Line Schedules
- **Carnival:** carnival.com/cruise-search — API-friendly, filter by Miami homeport
- **Royal Caribbean:** royalcaribbean.com/cruises
- **Norwegian:** ncl.com

### Trade Data
- **USITC DataWeb:** dataweb.usitc.gov — free import/export by HTS code
- **USA Trade Online:** usatrade.census.gov — Census Bureau data

### Provisioning RFQs
- **SAM.gov:** Federal contracts — filter "food services" + Florida
- **Miami-Dade County:** miamidade.gov/global/strategic-procurement

---

## Lead Gen Sources

### Restaurant Openings
- Eater Miami
- Miami New Times Food
- South Florida Business Journal
- Palm Beach Post Food

### Accolades
- Michelin Guide: guide.michelin.com/us/en/florida/miami/restaurants
- James Beard Foundation

### License Filings
- Florida DBPR — new restaurant licenses

### Social
- Instagram: #miamichef #miamirestaurants #natoora
