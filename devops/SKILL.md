---
name: selva-deal-log-agent
description: "Selva Partners Deal Log Agent: Plaud audio → Google Drive → Whisper → Hermes extract → Notion row."
tags: [selva-partners, deal-log, audio, whisper, notion, google-drive, service-account]
---

# Selva Deal Log Agent

Automated pipeline that picks up Plaud voice recordings from Google Drive, transcribes via OpenAI Whisper, extracts deal fields via Hermes 4 70B on OpenRouter, and writes structured rows into a Notion database.

## Agent file
~/.hermes/selva_deal_log_agent.py

## Authentication: OAuth token (NOT service account)

The agent uses Lorenzo's OAuth token at `~/.hermes/gmail_token.pickle` (Drive scope already included).
Service account key creation is blocked by org policy (`iam.disableServiceAccountKeyCreation`) on the chloe-lorenzob1987-org Workspace org — do NOT attempt service account key approach again.

The `drive_service()` function loads the pickle token and auto-refreshes it. No `GOOGLE_SERVICE_ACCOUNT_JSON` needed.

If the token expires and can't refresh, re-run: `python3 ~/.hermes/gmail_auth.py`

## Required env vars (all in ~/.hermes/.env)

| Var | Value | Notes |
|-----|-------|-------|
| OPENAI_API_KEY | sk-proj-... | Whisper transcription |
| OPENROUTER_API_KEY | sk-or-... | Hermes 4 70B extraction |
| NOTION_API_KEY | ntn_... | Notion integration secret |
| NOTION_DATABASE_ID | ... | Set after running setup |
| GDRIVE_FOLDER_ID | 1VUFBOa... | "Selva Recordings" folder |

## Setup checklist (one-time)

1. [ ] Enable Google Drive API in the SAME project as the service account.
       Use the API Library URL: https://console.cloud.google.com/apis/library/drive.googleapis.com?project=PROJECT_ID
       If you see "Request access" instead of "Enable", you're in the wrong project or wrong Google account — switch accounts in the top-right profile menu.
       Confirmed working project for Lorenzo: selva-495405 (Drive API enabled there May 2026)
2. [ ] Share "Selva Recordings" Drive folder with the service account email as Editor:
       selva-deal-agent@selva-deal-agent.iam.gserviceaccount.com
3. [ ] Get Notion parent page ID (32-char string at end of page URL)
4. [ ] Share that Notion page with the Notion integration (ntn_... key) — Settings → Connections
5. [ ] Run: python3 ~/.hermes/selva_deal_log_agent.py setup <NOTION_PARENT_PAGE_ID>
6. [ ] Copy printed NOTION_DATABASE_ID into ~/.hermes/.env

## Current setup state (as of May 2026)

- [x] OAuth token at ~/.hermes/gmail_token.pickle (Drive scope included)
- [x] Drive API enabled in selva-495405
- [x] Drive folder "Selva Recordings" ID: 1VUFBOa301HmQfEODd6EkBneDZxEoB_Ka
- [x] OPENAI_API_KEY, OPENROUTER_API_KEY, NOTION_API_KEY, GDRIVE_FOLDER_ID set in ~/.hermes/.env
- [x] Notion integration "Selva Deal Agent" created in "Chloe's Space" (ntn_2367909916165...)
- [x] Notion parent page: 357583626119804d95edde517856e719 (shared with integration)
- [x] NOTION_DATABASE_ID: 35758362-6119-816d-a0ab-e3b6bb3d7ff2 (set in ~/.hermes/.env)
- [x] Full pipeline tested — Drive connected, folder accessible, agent runs clean

## Webhook endpoints

Two webhook endpoints registered on the Hermes gateway (port 8644):

| Name | URL | Secret | Purpose |
|------|-----|--------|---------|
| selva-agent | http://localhost:8644/webhooks/selva-agent | NQ_VZHHwJ94T20RXVX8V8yjJ3PoJzRAO8DeA007WWuM | General purpose Selva agent |
| deal-log | http://localhost:8644/webhooks/deal-log | I1cGKmvlxOrM_p8kvoV9rmebetVzVVS6dQ0t9wWaI_g | Trigger deal log on demand |

HMAC header: `X-Webhook-Signature` (plain hex SHA-256, no prefix — NOT `sha256=hex`)

## Hermes Python client

Reusable client at `~/.hermes/selva_hermes_client.py`:

```python
from selva_hermes_client import HermesClient, ask_hermes

# Simple one-liner
ask_hermes("Draft a follow-up email to Juan about the lime shipment")

# With context
client = HermesClient()
client.send("Log this deal", context="Persian limes, 3 containers, $8.50 FOB")

# Trigger deal log agent on demand
deal_client = HermesClient(
    url="http://localhost:8644/webhooks/deal-log",
    secret="I1cGKmvlxOrM_p8kvoV9rmebetVzVVS6dQ0t9wWaI_g"
)
deal_client.send("process now")
```

Health check: `curl http://localhost:8644/health` → `{"status": "ok", "platform": "webhook"}`

A ready-to-copy client template is at `templates/selva_hermes_client.py` in this skill.

## Run commands

```bash
# One-shot (process all new files)
python3 ~/.hermes/selva_deal_log_agent.py run

# Continuous loop (every 6 hours)
python3 ~/.hermes/selva_deal_log_agent.py loop

# Dry-run a single Drive file (no Notion write)
python3 ~/.hermes/selva_deal_log_agent.py test <DRIVE_FILE_ID>
```

## Notion database schema

Deal ID (title), Date, Contact Name, Company, Location, Role (select), Commodity,
Grade, Pack Size, Quantity, Price Supplier ($), Price Buyer ($), Status (select),
Next Action, Next Action Date, Notes, Needs Review (checkbox), Review Reason, Source, Source File

Status options: Initial Contact, Quoted, Negotiating, Closed, Dead
Role options: Grower, Buyer, Freight, Other

## Pitfalls

- **`gmail_token.pickle` missing after Hermes update/reset** — The deal log agent hardcodes `~/.hermes/gmail_token.pickle` as its Drive auth token path. After a Hermes state reset or fresh setup, this file won't exist even though `selva_outreach_token.pickle` (which has the Drive scope) does. Fix: `ln -sf ~/.hermes/selva_outreach_token.pickle ~/.hermes/gmail_token.pickle`. Verify with `python3 ~/.hermes/selva_deal_log_agent.py run` — should output `No new audio files.` if auth is working.
- **Gmail label with emoji not found** — Gmail API returns labels without emoji rendering issues, but if a user says "🥑 Natoora" and you only see "Natoora-Archive", the label may be in a different account, recently created (needs token refresh), or the data is in Pipedrive directly (not Gmail). Ask which account before digging further.
- **Notion 404 on setup** — almost always means the page isn't shared with the integration yet. Go to the page → ... → Connections → Add the integration. Must be done on EVERY page in the path (parent pages too).
- **Notion page ID extraction** — copy from URL but strip query params. `?v=...`, `?source=copy_link`, `&pvs=...`, `&wfv` are NOT part of the ID. The ID is the 32-char hex string only.
- **Notion URL is a database, not a page** — if the URL contains `?v=` it's a database view. Go up one level in the sidebar to the parent page and use that URL instead.
- **Google Workspace org policy blocks service account keys.** Lorenzo's org (`chloe-lorenzob1987-org`) enforces `iam.disableServiceAccountKeyCreation`. Do NOT attempt service account key creation — use the OAuth pickle token at `~/.hermes/gmail_token.pickle` instead (Drive scope already included).
- **Service account ≠ OAuth client.** If user pastes `{"web": {...}}` credentials, that's for user login flows — flag it and redirect. For Lorenzo specifically, skip service accounts entirely due to org policy.
- **"Request access" on Drive API enable page** means wrong project or wrong Google account. Use API Library URL: https://console.cloud.google.com/apis/library/drive.googleapis.com?project=PROJECT_ID. Switch to chloe.lorenzob1987@gmail.com if needed.
- **GOOGLE_SERVICE_ACCOUNT_JSON in .env** must be single-line JSON. Use `json.dumps(json.load(f))` to serialize.
- **Notion parent page** must be shared with the integration before running setup.
- State file at `~/.selva_agent_state.json` tracks processed file IDs to avoid re-processing.
- **Discord mcp_send_message(action="list") returns STALE cached channel/thread names.** The tool does NOT reflect renames Lorenzo makes in Discord. To get current thread names and content, use the Bot API directly:
  ```bash
  TOKEN="YOUR_DISCORD_BOT_TOKEN_HERE"
  curl -s -H "Authorization: Bot $TOKEN" "https://discord.com/api/v10/channels/THREAD_ID" | python3 -c "import json,sys; c=json.load(sys.stdin); print(c.get('name','?'))"
  # Read messages:
  curl -s -H "Authorization: Bot $TOKEN" "https://discord.com/api/v10/channels/THREAD_ID/messages?limit=50"
  ```
  Server ID: 1501049826350071889. Bot token in ~/.hermes/.env as DISCORD_BOT_TOKEN.
- **Webhook HMAC header is `X-Webhook-Signature`** (plain hex SHA-256). NOT `X-Hermes-Signature`, NOT `sha256=hex`. Using the wrong header name returns 401 Unauthorized. Confirmed by reading `gateway/platforms/webhook.py` `_validate_signature` method.
- **Webhook server on port 8644** must be enabled in config.yaml under `platforms.webhook.enabled: true`. Restart gateway after adding. Verify with `curl http://localhost:8644/health`.

## Selva Partners Email Accounts (CONFIRMED WORKING May 2026)

Two outreach accounts fully authorized and tested:

| Account | Token | Purpose |
|---------|-------|---------|
| lorenzo.belpassi@selva-partners.com | ~/.hermes/selva_outreach_token.pickle | Primary outreach |
| chloe.sanchez@selva-partners.com | ~/.hermes/chloe_outreach_token.pickle | Chloe's outreach |

Both use credentials: `~/.hermes/selva_outreach_credentials.json` (project: selva-outreach)
Auth scripts: `~/.hermes/selva_outreach_auth.py` and `~/.hermes/chloe_outreach_auth.py`

`chloe.sanchez@selva-partners.com` is a Google Workspace user created under the selva-partners.com org. Previously `chloe.lorenzob1987@gmail.com` — now has a proper work identity.

Send test to confirm working:

```bash
python3 -c "
import pickle, base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
creds = pickle.load(open('/Users/lorenzobelpassi/.hermes/selva_outreach_token.pickle','rb'))
svc = build('gmail','v1',credentials=creds)
msg = MIMEText('test')
msg['to'] = 'lorenzo.belpassi@gmail.com'
msg['subject'] = 'test'
raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
print(svc.users().messages().send(userId='me',body={'raw':raw}).execute())
"
```
If 403 `accessNotConfigured`: enable Gmail API at https://console.cloud.google.com/apis/library/gmail.googleapis.com?project=selva-outreach

## Selva Revenue Operating System

The three agents should be treated as workers inside one revenue operating loop, not as separate “cool agents.” The goal is to produce selling actions: who Lorenzo needs to see/call, what he should say, what product angle to lead with, and what next action gets logged.

Reference for the implemented local package, commands, lead scoring, people-to-see logic, and field spiel:
- `references/selva-revenue-os.md`
- `references/selva-notion-cockpit-and-doc-ingestion-2026-05-06.md` — palatable Notion daily cockpit, Source Documents database, local Natoora archive ingestion, and UI limits for the six-month plan

Local package:
```text
/Users/lorenzobelpassi/selva-agents/revenue_os
```

Key outputs:
```text
exports/daily_command.txt
exports/people_to_see.md
exports/people_to_see.csv
exports/scored_miami_leads.csv
exports/selva_daily_cockpit.md
exports/natoora_docs/natoora_document_manifest.json
exports/natoora_docs/source_documents_import.csv
```

Important caveat: scored leads are not automatically approved for outbound. Use the list to decide who to see/research; verify contact names/emails before production email sends.

Daily UI rule: keep Notion palatable. The front page is a cockpit, not a warehouse: show Today, People To See, Product/Sample Angle, Drafts To Approve, Capture, and End of Day. Hide raw databases/source documents behind linked views and agent workflows.

## Selva Revenue OS — Product Catalog & Sample Kits

As of May 6 2026, Selva Revenue OS includes a seasonal product/sample-kit layer in addition to lead scoring, people-to-see lists, and daily command output.

Local root: `/Users/lorenzobelpassi/selva-agents/revenue_os/`

Key generated files:
- `exports/scored_miami_leads.csv` — scored lead import
- `exports/people_to_see.md` — route-ready field list
- `exports/sample_kit_may.md` — seasonal products to carry
- `exports/seasonal_products_may.csv` — Product Catalog import source
- `exports/natoora_seasonal_database.json` — Natoora public seasonality + Miami positioning knowledge

CRM should include eight databases: Accounts, Contacts, Opportunities, Interactions, Market Signals, Product Catalog, Sample Kits, Source Documents. See `references/revenue-os-sample-kit-2026-05-06.md` for the product/sample layer and `references/selva-notion-cockpit-and-doc-ingestion-2026-05-06.md` for the palatable Notion cockpit and Natoora document ingestion pattern.

Field rule: no A/A+ chef visit should be generic. Attach a product angle and 3–6 seasonal proof-point items or an availability sheet.

## Selva Partners Agent System — Discord Threads

Lorenzo is building a 3-agent system for Selva Partners operations. Each agent has its own Discord thread in #general (server: 1501049826350071889). Thread names and IDs:

| Thread Name | Thread ID | Purpose | Status |
|-------------|-----------|---------|--------|
| Lead/Deal Capture Agent | 1501254005693747324 | Unstructured signals (emails, calls, messages) → structured CRM records → Notion | Existing Plaud→Notion pipeline covers this |
| Market Intel Agent | 1501077317764649041 | Pre-market briefing / decision support (USDA, freight, weather, FX) | DEPLOYED May 5 2026 — see selva-market-intel skill |
| Pipeline Tracker & Follow-Up Agent | 1501062192248918148 | Deal pipeline tracking, follow-up scheduling, RevOps automation | Code at ~/Downloads/Pipeline1 — see Agent 3 section below |

Note: Lorenzo renamed the threads May 5 2026. mcp_send_message(action="list") shows STALE names. Always verify via Bot API.

### Revenue Operating System Framing (IMPORTANT — confirmed May 2026)

When Lorenzo asks about the six-month Selva plan, infrastructure, lead research, market intelligence, or CRM/pipeline discipline, do not frame the answer as “agents that run.” Frame it as a Selva revenue operating system:

1. Market Intelligence finds opportunities.
2. Lead Research turns opportunities into named accounts + people.
3. CRM stores every target, conversation, quote, sample, and next step.
4. Pipeline Tracker forces daily follow-up.
5. Deal Log captures calls/voice/emails and keeps the CRM alive.
6. Weekly review measures progress against the May–Oct 2026 $157K net target.

The agents are workers; Notion/CRM is the operating system. See `references/selva-revenue-operating-system.md` for the recommended account-based CRM schema, lead scoring model, daily command brief, and weekly cadence.

## Agent Architecture (IMPORTANT — confirmed May 2026)

**These are 3 standalone agents. NO automatic data passing between them.**

```
Market Intel Agent ──────────────────────────────────────────────┐
  • Trigger: Cron (Mon/Thu 8am)                                  │
  • Output: Research briefs → Telegram + Discord                 │
  • Does NOT auto-feed leads to Pipeline Tracker                 │
                                                                 │
Lead/Deal Capture Agent ─────────────────────────────────────────┤
  • Trigger: On-demand (user sends emails/calls/notes)           │──► NOTION (shared DB)
  • Output: Structured CRM rows → Notion                         │
  • Handles: Meetings, calls, industry news, ongoing signals     │
                                                                 │
Pipeline Tracker & Follow-Up Agent ──────────────────────────────┤
  • Trigger: Daily cron + on-demand                              │
  • Input: Reads from Notion (deals where Next Action = today)   │
  • Output: Follow-up drafts → user approval → send              │
```

**The connection is Notion** — it's the shared database:
- Lead/Deal Capture WRITES to Notion
- Pipeline Tracker READS from Notion
- Market Intel is pure research/awareness — user manually decides what becomes a lead
- **Notion is the shared database** — agents don't pass data directly, they read/write Notion

```
Market Intel (discovery/briefs) → YOU decide what to pursue
                                      ↓
Lead/Deal Capture (emails, calls, news) → structures → Notion
                                                          ↓
Pipeline Tracker ← reads Notion (Next Action = today) → drafts follow-ups
```

**To feed the pipeline with data:**
1. Bulk import (CSV/Pipedrive export) → load directly into Notion
2. Use Lead/Deal Capture Agent — send emails/notes there, it structures and writes to Notion
3. Manual entry in Notion

## Gmail Attachment Extraction

To pull CSV/data attachments from Gmail (e.g., lead lists forwarded from work email):

```python
import pickle, base64
from googleapiclient.discovery import build

creds = pickle.load(open('~/.hermes/gmail_token.pickle', 'rb'))
service = build('gmail', 'v1', credentials=creds)

# Search for emails
results = service.users().messages().list(userId='me', q='from:domain.com subject:prospects').execute()
msg_id = results['messages'][0]['id']
full = service.users().messages().get(userId='me', id=msg_id, format='full').execute()

# Extract attachment
def find_attachment(payload):
    if 'parts' in payload:
        for part in payload['parts']:
            if part.get('filename') and part['filename'].endswith('.csv'):
                att_id = part['body'].get('attachmentId')
                if att_id:
                    att = service.users().messages().attachments().get(
                        userId='me', messageId=msg_id, id=att_id).execute()
                    return part['filename'], base64.urlsafe_b64decode(att['data'])
            result = find_attachment(part)
            if result: return result
    return None

filename, data = find_attachment(full['payload'])
with open(f'/tmp/{filename}', 'wb') as f:
    f.write(data)
```

**Pitfall:** Gmail labels with emoji (like `🥑-natoora`) may not appear via labels.list() API. Use `q='from:domain.com'` or `q='subject:keyword'` as reliable fallbacks.

## Lead Processing

See `references/lead-processing-patterns.md` for:

See `references/revenue-os-build-2026-05-06.md` for the new Selva Revenue OS package at `/Users/lorenzobelpassi/selva-agents/revenue_os/`: lead scoring, CSV cleanup, CRM blueprint, command-center generation, tests, generated outputs, and the rule to enrich/verify leads before outreach.

See `references/natoora-email-extraction.md` for:
- Natoora competitor intel from Gmail extraction (March 2026)
- Contacts, pricing, operations data
- 11 leads pushed to Notion Selva Deals database
- Quality filtering thresholds (rating/reviews)
- Deduplication by name+phone
- Restaurant segmentation logic
- Miami Cold Outreach dataset stats (734 cleaned leads from Feb 2026)

## Market Intel Agent — Deployment Notes (May 2026)

**STATUS: FULLY DEPLOYED May 5, 2026.** See `selva-market-intel` skill for full details.

Production codebase: `/Users/lorenzobelpassi/Downloads/selva_market_intel/` (modified from original at `~/Downloads/marketintel/`).

Architecture: Modal cron (daily ~4:55am ET) → concurrent fetchers (USDA, weather, freight, FX) → Claude Opus writes brief → deliver to Discord + Telegram.

**Keys confirmed:**
- ANTHROPIC_API_KEY: from ~/.hermes/.env (ANTHROPIC_TOKEN)
- OPENWEATHER_API_KEY: YOUR_OPENWEATHER_API_KEY_HERE
- TELEGRAM_BOT_TOKEN: from ~/.hermes/.env
- DISCORD_BOT_TOKEN: from ~/.hermes/.env
- Discord delivery channel: thread 1501077317764649041 (Market Intel Agent)

**DAT freight scraping:** Lorenzo has no DAT account and won't pay for one. Replace dat.py fetcher with open web scraping (DAT public pages, FreightWaves free content, Google search for lane rates). Agent degrades gracefully if freight fetch fails — brief still ships.

**Email delivery:** Skip SMTP entirely. Lorenzo has no Gmail app password. Options:
1. Deliver via Discord thread + Telegram only (preferred for now)
2. If email needed later: use Gmail API via chloe.sanchez@selva-partners.com OAuth token (~/.hermes/chloe_outreach_token.pickle) — has gmail.send scope, no SMTP needed.

**Modal secret to create:**
```bash
/Users/lorenzobelpassi/Library/Python/3.9/bin/modal secret create selva-market-intel \
  ANTHROPIC_API_KEY=sk-ant-oat01-... \
  OPENWEATHER_API_KEY=YOUR_OPENWEATHER_API_KEY_HERE \
  TELEGRAM_BOT_TOKEN=8711845322:AAHk6RWiUi3YqdNtYZjlOuC8TN5J-eX6lWI \
  DISCORD_BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN_HERE \
  DISCORD_CHANNEL_ID=1501077317764649041
```

**Telegram chat ID:** Not yet confirmed — Lorenzo needs to send a message to the bot so we can grab it from getUpdates.

When Lorenzo asks "where were we on outreach agents" or "the agents" or "the agent system":
- Check these Discord threads FIRST — session search often misses in-progress Discord work
- Use the Bot API directly (see pitfall below) — do NOT rely on mcp_send_message(action="list") for thread names, it returns cached/stale data
- The Lead/Deal Capture Agent extends the existing Plaud→Notion pipeline to handle ALL inbound signals, not just voice recordings

## Agent 3: Pipeline Tracker & Follow-Up Agent

Codebase: `/Users/lorenzobelpassi/Downloads/Pipeline1/`

**What it does:**
- Daily cron at 4:50am ET via Modal
- Queries Notion for deals where Next Action Date = today
- Generates follow-up drafts with Claude Sonnet 4.6 (channel-aware: email, IG DM, text, or skip)
- Creates Gmail drafts for email follow-ups (with deep links)
- Sends morning summary via Hermes webhook (Telegram + Discord + Email)

**Files:**
| File | Purpose |
|------|---------|
| main.py | Modal app — cron entry point + manual_run |
| notion_query.py | Pulls deals from Notion where Next Action Date = today |
| prompts.py | System prompt + deal-to-prompt logic |
| few_shot.py | 6 example follow-ups defining Lorenzo's voice |
| drafts.py | Calls Claude to generate drafts |
| gmail_drafts.py | Creates Gmail drafts with deep links |
| hermes.py | Formats & sends morning summary |
| notion_schema.md | Required Notion database schema |
| setup.md | Full setup walkthrough |

**Notion Database Schema (required properties):** See `references/agent3-notion-schema.md` for full schema.

**Modal Secrets to create:**
```bash
modal secret create selva-agent-3 \
    ANTHROPIC_API_KEY=sk-ant-... \
    NOTION_API_KEY=secret_... \
    NOTION_DEALS_DB_ID=abc123... \
    HERMES_WEBHOOK_URL=http://localhost:8644/webhooks/selva-agent \
    OPERATOR_NAME=Lorenzo

# Gmail token is its own secret (JSON blob)
modal secret create selva-gmail-token \
    GMAIL_TOKEN_JSON='<paste entire JSON blob>'
```

**Gmail OAuth setup:**
1. Use existing project selva-outreach (same as other Selva agents)
2. Enable Gmail API if not already
3. Run get_gmail_token.py script from setup.md
4. Scope needed: `https://www.googleapis.com/auth/gmail.compose`
5. Paste resulting JSON into Modal secret

**Deploy:**
```bash
cd ~/Downloads/Pipeline1
modal deploy main.py
# Creates selva-agent-3-pipeline app with daily cron
```

**Test commands:**
```bash
# Local dry-run (no external calls except Claude)
export ANTHROPIC_API_KEY=sk-ant-...
python test_local.py

# Modal dry-run (real Notion + Gmail + Hermes)
modal run main.py::manual_run
```

**Voice/Tone:** Defined in few_shot.py with 6 canonical examples (see `references/agent3-few-shot-examples.md`):
- Direct, no "I hope this finds you well"
- Short (3-5 sentences for email, 2-3 for DM)
- No exclamation marks
- Sign off "Lorenzo" alone
- Reference one specific thing (product, date, number)
- Never say "premium" or "high-quality"

**Pattern Selection (from prompts.py):**
- COLD + touch 1-2: short re-touch, low-friction ask
- COLD + touch 3+: usually SKIP unless new info
- WARM + had tasting: reference item, push next step
- WARM + 14+ days quiet: re-engagement angle
- HOT: push for decision with real reason
- Any tier + touch 6+ + no engagement: SKIP → nurture

## Outreach Research

Prospect lists for organic Mexican citrus outreach (researched May 2026):
- `references/outreach-prospects.md` — top picks across Alapattah market, national wholesale, cruise lines, hotels/resorts

## Gmail Attachment Extraction for Lead Data

When Lorenzo mentions Natoora leads, Pipedrive data, or client lists in Gmail:

1. Search: `from:natoora.com has:attachment` or `from:lorenzo.belpassi@natoora.com`
2. Download attachments via Gmail API (base64 decode from `attachmentId`)
3. Key files from Feb 2026 export (saved to `/tmp/natoora_clients/`):
   - `Miami Cold Outreach - Raw.csv` — 2,037 scraped restaurant prospects
   - Client pricing sheets: MILA, Makoto, Fisher Island, Maple & Ash, Papi Steak, Gekko, Mr. C, Centner Academy, Fiola/Daniels

**Existing Natoora accounts (warm leads):** MILA, Makoto, Fisher Island Club, Maple & Ash, Fiola Miami, Centner Academy, Papi Steak, Gekko, Tin Tin/Tinta y Cafe, Mr. C Miami

**Filtering for high-end independents:**
- Minimum: 4.6+ rating, 1000+ reviews
- Exclude chains (El Toro Loco, Havana 1957, Bulla, STK, etc.)
- Target: Fine dining, seafood, steakhouses, Japanese/sushi
- Result: ~166 premium independents from the cold outreach CSV

See `references/natoora-data-extraction.md` for full workflow.

## Workflow (user-facing)

1. Record on Plaud (any tag/folder)
2. In Plaud app: Export → Save to Google Drive → "Selva Recordings" folder
3. Agent picks up once per day (cron job: every 24h, job_id: 8aafb5c48129), transcribes, extracts, logs to Notion, moves to Processed/
4. Rows flagged "Needs Review" = missing contact name, company, or commodity
