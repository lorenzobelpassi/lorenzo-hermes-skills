# Pipeline Tracker Agent (Agent 3) Setup

Deployed to Modal as `selva-agent-3-pipeline`. Daily 4:50am ET cron.

## Location
- **Code:** `~/selva-agents/pipeline1/`
- **Modal app:** `selva-agent-3-pipeline`
- **Cron:** `50 4 * * *` (4:50am ET daily)

## Files
| File | Purpose |
|------|---------|
| `main.py` | Modal app entry, cron definition |
| `notion_query.py` | Queries Notion deals DB via httpx (NOT notion-client v3 — API changed) |
| `prompts.py` | System prompt + deal-to-prompt logic |
| `few_shot.py` | 6 example follow-ups defining Lorenzo's voice |
| `drafts.py` | Claude Sonnet 4.6 draft generation |
| `gmail_drafts.py` | Creates Gmail drafts with deep links |
| `hermes.py` | HMAC-signed webhook to Hermes |

## Modal Secrets
Two secrets required:

**selva-agent-3:**
- ANTHROPIC_API_KEY
- NOTION_API_KEY
- NOTION_DEALS_DB_ID
- HERMES_WEBHOOK_URL (ngrok URL + `/webhooks/selva-agent`)
- HERMES_WEBHOOK_SECRET (from `~/.hermes/webhook_subscriptions.json`, NOT config.yaml)
- OPERATOR_NAME

**selva-gmail-token:**
- GMAIL_TOKEN_JSON (JSON blob from `selva_gmail_token.pickle`)

## Notion Database Schema
Lorenzo's "Selva Deals" DB uses these Status options (not the default):
- Initial Contact, Quoted, Negotiating, Closed, Dead

Required fields added:
- Contact Email (email)
- Neighborhood (select)
- Tier (select: 🔥 HOT, 🟡 WARM, 🔵 COLD)
- Touch Count (number)
- Last Touch Type (select)
- Last Contact Date (date)
- Last Note (rich_text)
- Intel (rich_text)
- Gmail Thread ID (rich_text)

Title field is `Deal ID`, not `Contact Name`.

## Critical: Webhook HMAC

Hermes webhooks require HMAC-SHA256 in `X-Webhook-Signature` header:

```python
import hashlib, hmac, json
payload_str = json.dumps(payload)
sig = hmac.new(secret.encode(), payload_str.encode(), hashlib.sha256).hexdigest()
headers = {"X-Webhook-Signature": sig, "Content-Type": "application/json"}
```

The secret is **per-subscription** (in `~/.hermes/webhook_subscriptions.json`), NOT the global config.yaml secret.

## Critical: notion-client v3 Breaking Change

notion-client v3.0.0 removed `notion.databases.query()`. Solution: use httpx directly:

```python
import httpx
resp = httpx.post(
    f"https://api.notion.com/v1/databases/{db_id}/query",
    headers={"Authorization": f"Bearer {api_key}", "Notion-Version": "2022-06-28"},
    json={"filter": {...}}
)
```

## ngrok Tunnel

Local Hermes webhook exposed via ngrok. URL changes on restart.

```bash
# Start tunnel
ngrok http 8644

# Get current URL
curl -s http://127.0.0.1:4040/api/tunnels | jq '.tunnels[0].public_url'
```

After restart, update Modal secret with new URL:
```bash
modal secret create selva-agent-3 ... HERMES_WEBHOOK_URL="https://NEW-URL.ngrok-free.dev/webhooks/selva-agent" --force
```

## Deploy & Test

```bash
cd ~/selva-agents/pipeline1
modal deploy main.py
modal run main.py::manual_run  # test immediately
```
