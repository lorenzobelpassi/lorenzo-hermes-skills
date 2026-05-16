---
name: selva-market-intel
description: "Selva Partners Market Intel Agent: daily produce market brief via Modal cron → email + Telegram + Discord"
version: 2.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [produce, commodities, market-research, USDA, logistics, organic, modal, cron, discord, telegram, gmail]
---

# Selva Market Intel Agent

Daily 5am ET brief covering limes, oranges, tomatoes, avocados — Mexico→Miami supply chain. Delivers to:

## New Data Modules (Planned — May 2026)

| Module | Source | Status |
|--------|--------|--------|
| `miami_pricing.py` | USDA ESMIS API → PDF download → pdfplumber parse | Planned |
| `fl_final_mile.py` | GoShip scrape + hardcoded baselines w/ diesel adjustment | Planned |
| `cruise_intel.py` | Carnival schedule scrape + SAM.gov RFQ monitor | Planned |
| `lead_gen.py` | Eater Miami, DBPR filings, Michelin/JB | Planned |

**USDA ESMIS API (Miami Terminal Pricing):**
- Base URL: `https://esmis.nal.usda.gov/`
- API docs: `https://esmis.nal.usda.gov/api-documentation`
- Miami reports: MH_FV020 (vegetables), MH_FV010 (fruits), MH_FV056 (tropical — avocados, mangoes, limes)
- Format: Daily PDFs with price ranges — needs pdfplumber parsing
- No auth required

**FL Final Mile Freight (Free Sources):**
- GoShip — cleanest free quote calculator, has API
- FreightQuote (C.H. Robinson) — instant quotes
- R+L Carriers — has reefer/temperature-controlled
- Fallback: hardcoded baselines + diesel index adjustment

**Cruise/Port Intel:**
- PortMiami perishables: 3,000+ reefer plugs
- Carnival: `carnival.com/cruise-search` (API-friendly)
- SAM.gov for provisioning RFQs
- USITC DataWeb for reefer import volumes

## Commodity Coverage (Organic/Minimal Intervention Focus)

**Top 10 Vegetables:** Tomatoes, peppers, lettuce, onions, potatoes, cucumbers, squash, broccoli, carrots, celery

**Top 10 Fruits:** Avocados, strawberries, blueberries, lemons, limes, oranges, grapes, apples, mangoes, bananas

**Top 10 Specialty:** Microgreens, edible flowers, heirloom tomatoes, baby vegetables, exotic mushrooms, ramps/wild foraged, dragon fruit, passion fruit, finger limes, fresh truffles

## Delivery Channels
- Email: lorenzo.belpassi@selva-partners.com (sent from chloe.sanchez@selva-partners.com via Gmail API)
- Telegram: chat ID 7336078952
- Discord: Market Intel Agent thread, ID 1501077317764649041

## Deployed Codebase

Production code at `/Users/lorenzobelpassi/Downloads/selva_market_intel/` (NOT `marketintel/` — that's the original unmodified source).

Key files:
- `modal_app.py` — Modal cron entry, deploy with modal CLI
- `pipeline.py` — concurrent fetchers + failure isolation, delivers to email + Telegram + Discord
- `config.py` — commodities, thresholds, terminals, Secrets dataclass
- `brief.py` — Claude API call (falls back to deterministic template on rate limit/error)
- `__init__.py` — prompts: SYSTEM_PROMPT, build_facts_block, build_user_prompt
- `usda.py` — USDA MARS API fetcher
- `freight.py` — FREE public web scraper (replaces DAT — Lorenzo has no DAT account, will not pay)
- `weather.py` — OpenWeatherMap One Call 3.0
- `currency.py` — exchangerate.host (free, no key)
- `email.py` — Gmail API via OAuth (chloe_outreach_token.pickle, NOT SMTP)
- `telegram.py` — Telegram bot API
- `discord_delivery.py` — Discord bot API, posts to thread 1501077317764649041

## Import Convention (Critical)

All imports must be ABSOLUTE (`from selva_market_intel.config import ...`), NOT relative (`from ..config import ...`). Modal's `add_local_python_source` mounts the package at root level — relative imports break with "attempted relative import beyond top-level package". Fix with:

```python
import re
fixed = re.sub(r'from \.\.([\w.]+) import', r'from selva_market_intel.\1 import', raw)
fixed = re.sub(r'from \.([\w]+) import', r'from selva_market_intel.\1 import', fixed)
```

## Gmail API — No SMTP

Lorenzo uses OAuth tokens, not SMTP app passwords. Email delivery uses `google-api-python-client` + Chloe Sanchez's OAuth token. Token path: `~/.hermes/chloe_outreach_token.pickle`. Scope needed: `gmail.send`.

In Modal (cloud), the token is stored as base64 in the Modal secret as `GMAIL_TOKEN_B64`. Load it:

```python
import base64, os, pickle
b64 = os.environ.get("GMAIL_TOKEN_B64", "")
creds = pickle.loads(base64.b64decode(b64.encode()))
```

To re-encode the token for the secret:
```python
import base64, pickle
with open('/Users/lorenzobelpassi/.hermes/chloe_outreach_token.pickle', 'rb') as f:
    raw = f.read()
encoded = base64.b64encode(raw).decode()
```

`modal.Mount` does NOT exist in modal v1.2.6. Use the base64 env var approach instead.

## Modal Secret

```bash
/Users/lorenzobelpassi/Library/Python/3.9/bin/modal secret create selva-market-intel --force \
  ANTHROPIC_API_KEY="sk-ant-oat01-..." \
  OPENWEATHER_API_KEY="YOUR_OPENWEATHER_API_KEY_HERE" \
  EMAIL_TO="lorenzo.belpassi@selva-partners.com" \
  TELEGRAM_BOT_TOKEN="8711845322:AAHk6RWiUi3YqdNtYZjlOuC8TN5J-eX6lWI" \
  TELEGRAM_CHAT_ID="7336078952" \
  DISCORD_BOT_TOKEN="YOUR_DISCORD_BOT_TOKEN_HERE" \
  GMAIL_TOKEN_B64="<base64 encoded chloe_outreach_token.pickle>"
```

Secret already created and deployed as of May 5, 2026.

## Deploy & Test

```bash
# Deploy
cd /Users/lorenzobelpassi/Downloads
/Users/lorenzobelpassi/Library/Python/3.9/bin/modal deploy selva_market_intel/modal_app.py

# Test (fires immediately, delivers to all 3 channels)
/Users/lorenzobelpassi/Library/Python/3.9/bin/modal run selva_market_intel/modal_app.py::run_now
```

## Schedule Options

**Option A: Hermes Cron (Current)**
Twice weekly briefings via Hermes cron jobs (simpler, no Modal needed):
- Monday 8:00 AM ET → Telegram + Discord
- Thursday 8:00 AM ET → Telegram + Discord

Cron job IDs:
- `8faba05c5d47` — Monday Telegram
- `c54641692f43` — Thursday Telegram  
- `96dadb116a49` — Monday Discord
- `5ff1124445c3` — Thursday Discord

**Option B: Modal Cron (Original)**
`modal.Cron("0 9 * * 1-5")` — 09:00 UTC weekdays = 5:00am EDT.

## Freight Fetcher — Free Sources Only

DAT replaced with `freight.py` which:
1. Scrapes FreightWaves public reefer tag page for direction signals
2. Falls back to Truckstop.com market updates
3. Uses hardcoded baseline $/mile rates from 2024-2025 public benchmarks when scraping fails

Baseline rates ($/mile): McAllen→Miami $2.45, Laredo→Miami $2.50, Pharr→Miami $2.45, Nogales→LA $2.20.

## Known Issues / Pitfalls

- **USDA MARS API returns 403 from Modal cloud IPs** — USDA blocks cloud datacenter ranges. Brief degrades gracefully (ships with no price data). Fix: add a residential proxy, or switch to scraping USDA's public HTML report pages.
- **Claude rate limit on test runs** — 429 on first run is normal if API key is on a low-RPM tier. Brief falls back to deterministic template. Not a production issue at 5am daily cadence.
- **modal.Mount does not exist in v1.2.6** — use base64 env var for token files instead.
- **Model name** — brief.py uses `claude-opus-4-7`. Verify this matches Anthropic account access; update in `brief.py` if needed.
- **GMAIL_TOKEN_B64 expiry** — OAuth tokens expire. When the token expires in Modal, update the secret with a freshly re-encoded pickle. Run locally first to refresh: `python3 -c "import pickle; ..."` then re-encode.

## Discord Channels (Selva Partners server ID: 1501049826350071889)

Three agent threads in #general:
- `1501254005693747324` — Lead/Deal Capture Agent
- `1501077317764649041` — Market Intel Agent (this agent posts here)
- `1501062192248918148` — Pipeline Tracker & Follow-Up Agent

Bot token: `YOUR_DISCORD_BOT_TOKEN_HERE`

## Lead Generation Module (NEW — May 2026)

Market Intel Agent now doubles as lead gen. Scrape and qualify restaurant leads daily.

**Restaurant Intel Cron:** `fa7aa1e484df` — runs daily at 6:00am ET and delivers to Discord Market Intel thread. It watches restaurant openings, chef moves, investor/operator signals, real estate, farmers/growers, and DBPR/license signals.

**Qualification Framework (Natoora-style targets):**
- A-Tier: Michelin starred, James Beard winner/nom, farm-to-table/organic focus, high-density zone
- B-Tier: High foot traffic zone, upscale concept, chef-driven, good reviews
- C-Tier: Right location but unproven, or right concept but off-map

**Miami Heat Map Zones (Priority):**
Brickell, Downtown/Arts District, Coconut Grove, Coral Gables, Miami Beach (SoBe + Mid-Beach), Design District, Wynwood, Edgewater/Midtown, Aventura

**Lead Sources:**
- Eater Miami (openings, chef news)
- Miami New Times Food
- South Florida Business Journal
- Florida DBPR (new restaurant license filings)
- Michelin Guide Miami
- James Beard Foundation
- Instagram #miamichef #miamirestaurants

**Output:** Daily qualified lead list with: name, chef/buyer contact, zone, qualification tier, source link, suggested product angle, and Pipeline Tracker import fields.

**Newsletter / outreach guardrail:** Restaurant Intel and Market Intel are internal intelligence by default. Do not send third-party outreach or create Chloe/Gmail sends from scraped leads unless Lorenzo explicitly approves. Pipeline rows from new intel should default to Needs Review / Nurture until approved.

**Files:**
- Hit list: `~/.hermes/selva_leads/natoora_hit_list.md`
- Daily intel JSON/briefs: `~/.hermes/selva_leads/daily_intel/`
- Investor watchlist: `~/.hermes/selva_leads/investor_watchlist.md`
- Chloe sequences: `~/.hermes/selva_leads/chloe_outreach_sequences.md`
- First-wave Chloe drafts: `~/.hermes/selva_leads/chloe_first_wave_drafts_2026-05-05.md`
- Pipeline import CSVs/results: `~/.hermes/selva_leads/pipeline_imports/`

## Natoora Competitive Intel

Primary competitor. Miami ops run by Chris Devlin.
- Email: flavor-mia@natoora.com
- Phone: +1 786-779-2925
- Warehouse: Allapattah
- Deliveries: 6 days/week (Mon-Sat)
- Key farm partner: Tiny Farm (Roberto) — 7 acres

**Confirmed Natoora Miami accounts (priority takeover targets):**
Palma, Mandolin Aegean Bistro, ViceVersa, Kul Goods, Sili Miami, Gramps Getaway, Façade Bakery

## Cross-Agent Signal Deduplication / Shared Lead Bank

When adding editorial, market-intel, restaurant-intel, or brokerage jobs, avoid isolated agents repeatedly searching the same sources. Use a shared lead-bank pattern: one daily router/deduper consumes recent outputs from existing Selva Market Intel, Restaurant Intel, and Brokerage Intel jobs, separates public-safe editorial angles from internal sales/outreach signals, and feeds downstream Walk-In / Staff Meal / sales jobs via cron context. See `references/walk-in-shared-lead-bank-synergy.md`.

Rule of thumb: downstream jobs should use shared context first and only perform fresh web searches for verification or important gaps.

## Revenue OS Signal Conversion

Market Intel must not stop at an informational brief. Each high-value item should become a CRM-ready `Market Signal` that can feed the Selva Revenue OS daily command and people-to-see list.

Reference: see `selva-deal-log-agent` → `references/selva-revenue-os.md` for the local Revenue OS package at `/Users/lorenzobelpassi/selva-agents/revenue_os`, lead scoring, people-to-see generation, and field spiel.

Each signal should include:
- commodity
- implication
- urgency
- suggested accounts
- recommended action
- converted_to_lead/action_taken flags once pushed to CRM

Rule of thumb: if a market-intel output does not create a person to see/call, a draft to send, a sample/quote to prepare, a stale opportunity to rescue, or a nurture/dead decision, it is informational rather than operational.

## Investment Opportunities Section

Each briefing must include actionable trading signals:

Required sections:

**Price Board** — Key products such as limes, avocados, tomatoes, mangoes, berries, citrus, herbs, tropical fruit, and specialty items. Include Miami terminal pricing when available, trend vs prior week, availability/quality notes, and spread/margin implications.

**Weather / Supply Risk** — Mexico growing regions, Florida weather, California if relevant, Caribbean disruptions, hurricane/flood/heat alerts, and cold-chain/logistics implications.

**Freight / Logistics** — Mexico→Miami, Texas border lanes, Florida final mile, diesel, PortMiami/reefer activity, and any bottlenecks.

**Demand Signals** — Restaurant openings, Michelin/chef activity, cruise provisioning windows, hotel/resort seasonal demand, Miami events, and menu trends.

**Volatility Plays** — Lines with significant price swings worth positioning on; weather-driven supply gaps creating opportunities.

**Margin Opportunities** — Underpriced organic/specialty lines with strong high-end restaurant demand; arbitrage between markets.

**Emerging Trends** — New varietals gaining traction; sourcing regions to watch; categories with growing demand.

**Buy/Avoid Signals** — Clear recommendations based on the week's data.

**Account-Specific Actions** — Convert signals into sales moves: named accounts, product angle, recommended channel, and urgency. Example: “Persian limes: watch/buy. Miami price range widening and cocktail/bar demand strong. Target ViceVersa, Mandolin, Palma, and high-end hotel bars. Action: send availability note today.”

## Shared Lead Bank / Cross-Agent Synergy

When The Walk-In, Staff Meal, Selva Restaurant Intel, Brokerage Intel, and Market Intel are all active, avoid duplicate research. Use a shared lead-bank pattern:

1. Run one daily dedupe/router job before editorial jobs.
2. Inject recent outputs from restaurant intel, brokerage intel, and market briefs as context.
3. Produce buckets for:
   - publication angles
   - Staff Meal leads
   - Selva/Cosecha sales signals
   - product/seasonality signals
   - duplicate/already-covered items
   - verification queue
4. Downstream Tuesday/Friday publication drafts must consume the lead bank first and only do fresh web research to verify/fill high-value gaps.
5. Keep public editorial material separated from internal sales/outreach material.

Current May 2026 job IDs:
- Shared Daily Lead Bank: `01bbe0f0b464`
- The Walk-In Tuesday draft: `37a836d9eddb`
- Staff Meal Friday draft: `c9958c5d8839`

## Three-Agent System (Selva Partners)

1. **Lead/Deal Capture Agent** — unstructured signals (email, call notes, voice) → structured Notion records. Uses existing Selva Deal Log Agent pipeline.
2. **Market Intel Agent** — THIS agent. Twice-weekly brief, Hermes cron (or Modal cron).
3. **Pipeline Tracker & Follow-Up Agent** — deal stage tracking + follow-up reminders. Code at `/Users/lorenzobelpassi/Downloads/Pipeline1/`. See `references/pipeline-agent-setup.md` for full setup notes.

## Revenue OS Integration

As of May 6 2026, local package `/Users/lorenzobelpassi/selva-agents/revenue_os/` converts Market Intel output into a single revenue operating loop. Market Intel should produce `Market Signals`, not just a prose brief. Signals should be shaped so they can feed the Daily Command Center:
- commodity
- urgency
- implication
- suggested accounts
- action
- source

The command-center module is `revenue_os/command_center.py`; it combines market signals, scored leads, follow-ups due, stale pipeline, and progress vs the $157K target into one morning operating message. See `selva-deal-log-agent` reference `references/revenue-os-build-2026-05-06.md` for build details.

Market Intel also feeds the Product Catalog and Sample Kit layer. Product/seasonality outputs should capture phase (early/peak/late), origin/grower, flavor argument, sample-worthiness, and target account lanes. See `references/revenue-os-product-catalog.md` for the May 2026 sample-kit workflow and Natoora public seasonality knowledge.

**Natoora 2025 seasonal sales calendar:** Generated from the 869-product sales archive into:
- Google Sheet: `https://docs.google.com/spreadsheets/d/1buZGrV73CD3KIyxr7y3-hKEIOR3Vvlzze9V3In_fUq8/edit`
- CSV: `/Users/lorenzobelpassi/selva-agents/revenue_os/exports/seasonal_calendar/natoora_2025_seasonal_calendar.csv`
- Monthly peaks CSV: `/Users/lorenzobelpassi/selva-agents/revenue_os/exports/seasonal_calendar/natoora_2025_monthly_product_peaks.csv`
- Summary: `/Users/lorenzobelpassi/selva-agents/revenue_os/exports/seasonal_calendar/natoora_2025_seasonal_calendar_summary.md`
Use this to chart product sales across the year, plan leafy greens/fruits windows, and build availability sheets/sample kits.

**Selva Market Letter / newsletter guardrails:** Lorenzo wants a branded weekly market letter similar in utility to Natoora's weekly, but with strict pre-launch guardrails: internal draft only, no third-party sends, no raw competitor data, and no automated Chloe outreach until approved. Grower/product stories must come from the INBOUND/vendor-facing product list where possible, not random web-found growers. See `references/selva-market-letter-inbound-grower-workflow.md` for the INBOUND source file, extracted citrus grower matrix, eligible grower rules, and drafting workflow.

**INBOUND Sheet grower rule:** Public newsletter/product features should use growers from Lorenzo’s INBOUND Sheet as the grower source of truth. Do not invent or web-source random growers for the newsletter. Within INBOUND growers, prefer organic/minimal-intervention/regenerative/no-spray/low-input farms. If the INBOUND Sheet is not accessible, ask for the exact sheet link/name before naming growers.

## Routing: Brief vs CRM Action vs Editorial Draft

Use this skill primarily for the intelligence layer.

Choose the output path explicitly:
- Market brief: short actionable read on supply, pricing, freight, demand, volatility, and buy/avoid signals.
- CRM / revenue action: convert high-value items into `Market Signals`, named account actions, people-to-see, samples, quotes, or follow-up tasks.
- Editorial support: provide public-safe angles, product windows, restaurant/opening notes, and verification notes for The Walk-In / Staff Meal or Selva market-letter drafts.

Routing rules:
- If the user wants operating action from intel, end with named accounts, urgency, and the next move.
- If the user wants publication copy, separate public-safe material from internal-only competitor, pricing, and account intelligence.
- If the user wants subscriber-facing writing, use this skill for the facts/signals layer and hand off the actual copy generation to the dedicated editorial workflow skill or `email_drafter` only for the final writing pass.
- Do not let a market-intel output stop at "interesting"; it must become a decision, a task, a signal, or a draft input.

## Weekly Market Letter Guardrails

Lorenzo wants Market Intel to support a branded weekly newsletter before any third-party outreach. Treat newsletter copy as internal draft material until explicitly approved. Use variety-specific product notes and verified farm/grower names; never invent farms or expose raw competitor/Natoora archive quantities. Keep Restaurant Intel leads in `Needs Review`/`Nurture` until Lorenzo approves a send/list. See `references/weekly-market-letter-guardrails.md` for the full workflow and template rules.

See also: `references/deployment-log-2026-05-05.md` for full session deployment notes.

See also: `references/miami-data-sources.md` for Miami-specific data source research (USDA ESMIS, freight, cruise/port, lead gen).

See also: `references/selva-market-letter-editorial-strategy.md` for the short, provocative, sensory editorial strategy for Selva's weekly chef/operator newsletter: hooky headings, INBOUND/sourcing-map grower guardrails, opinion in every section, and Lorenzo's personal product/cooking focus.

See also: `references/walk-in-staff-meal-substack-2026-05-08.md` for The Walk-In / Staff Meal Substack launch system: Tuesday/Friday brand architecture, subtle competitive positioning against generic Miami restaurant guides, Wynwood street-art/OpenAI image prompts, and the official Substack Developer API limitation that it is profile lookup only—not publishing/CMS automation.

See also: `references/walk-in-staff-meal-editorial-system.md` for Lorenzo's Substack/social brand system: Tuesday **The Walk-In** market/seasonality/openings intel, Friday **Staff Meal** Miami restaurant recommendations, subtle Infatuation/listicle competition posture, Wynwood street-art image prompts, and Substack/API caveats.

See also: `references/walk-in-shared-lead-bank-synergy.md` for the May 2026 cross-agent deduplication pattern: a Shared Daily Lead Bank that consumes Selva Restaurant/Market/Brokerage intel and feeds The Walk-In/Staff Meal drafts so agents reuse research instead of duplicating searches.

See also: `references/selva-market-letter-guardrails.md` for the internal-only weekly newsletter workflow, no-send guardrails, INBOUND Sheet grower source-of-truth rule, and subscriber-facing format.

See also: `references/notion-api-v3-breaking-change.md` for Notion client v3 migration notes (use httpx directly instead of notion-client library).

See also: `references/walk-in-review-database-and-shared-lead-bank-2026-05.md` for the May 2026 shared lead-bank pattern and Staff Meal review database: daily deduped intelligence router, downstream cron `context_from` usage, and Lorenzo first-person restaurant interview workflow.

See also: `references/walk-in-staff-meal-substack-notes.md` for the May 2026 Substack/publication setup: The Walk-In Tuesday + Staff Meal Friday, subtle competitor-to-Miami-listicle positioning, Wynwood/street-art visual prompts, and the finding that Substack's official Developer API is profile-lookup only (not draft/publish automation).

See also: `references/walk-in-autonomous-editorial-engine-2026-05.md` for the Shared Daily Lead Bank, Tuesday/Friday editorial cron jobs, Staff Meal first-person review database, and Substack remote-login caveat (iPhone/local login does not authenticate Browserbase).

See also: `references/walk-in-autonomous-editorial-engine-2026-05.md` for the daily Shared Lead Bank, Tuesday/Friday context-linked draft jobs, Staff Meal review database/interview workflow, and first-person restaurant-note guardrails.

See also: `references/walk-in-shared-lead-bank-review-db-2026-05.md` for the shared lead-bank architecture that dedupes Selva Restaurant/Market/Brokerage intel before The Walk-In/Staff Meal drafts, plus the Staff Meal first-person review database/interview workflow and Substack login pitfall.
