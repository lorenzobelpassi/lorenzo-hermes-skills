# Discord Setup Diagnostics

## Quick Check Sequence

When Discord appears disconnected or user says "bot isn't working on Discord":

```bash
# 1. Verify bot token and allowed users are set
grep -E "DISCORD_BOT_TOKEN|DISCORD_ALLOWED_USERS" ~/.hermes/.env

# 2. Check gateway is running
hermes gateway status

# 3. Confirm Discord adapter reconciled slash commands (means it's live)
grep -i "discord" ~/.hermes/logs/gateway.log | tail -10
```

A healthy Discord connection looks like:
```
[Discord] Safely reconciled 41 slash command(s): unchanged=0 updated=0 recreated=0 created=41 deleted=0
```

## Common Pitfalls

### Invalid or overwritten DISCORD_BOT_TOKEN
- **Symptom**: Discord fails to connect or reconnect; logs show `401 Unauthorized`, `LoginFailure('Improper token has been passed.')`, or repeated `discord connect timed out after 30s` after token edits.
- **Root cause**: `DISCORD_BOT_TOKEN` was overwritten with a placeholder, client/bot ID, username-like value, or other invalid string.
- **Fix**: Validate the token against Discord before repeatedly restarting:
  ```bash
  python3 - <<'PY'
  from pathlib import Path
  import re, subprocess, json
  text=(Path.home()/'.hermes/.env').read_text(errors='ignore')
  token=re.search(r'^DISCORD_BOT_TOKEN=(.*)$', text, re.M).group(1).strip()
  p=subprocess.run(['curl','-sS','-m','15','-H',f'Authorization: Bot {token}','https://discord.com/api/v10/users/@me'],capture_output=True,text=True)
  data=json.loads(p.stdout)
  print({k:data.get(k) for k in ['id','username','bot','code','message']})
  PY
  ```
  Healthy output includes a bot `id`, `username`, and `bot: True`. If it returns `401: Unauthorized`, restore the token from a known-good backup/snapshot or the Discord Developer Portal, then `hermes gateway restart`.
- **Detailed runbook**: `references/discord-token-recovery.md`.

### DISCORD_ALLOWED_USERS set to bot's own ID (not user's ID)
- **Symptom**: Gateway running, token valid, bot joins server, but never responds
- **Root cause**: `DISCORD_ALLOWED_USERS=<bot_id>` — bot's ID ≠ user's ID
- **Fix**: Get personal Discord user ID:
  1. Discord → Settings → Advanced → enable Developer Mode
  2. Right-click your own username anywhere → Copy User ID
  3. Set `DISCORD_ALLOWED_USERS=<your_user_id>` in `~/.hermes/.env`
  4. `hermes gateway restart`

### Bot appears absent from mcp_send_message targets
- `mcp_send_message` only lists active DM channels (Telegram, etc.)
- Discord not appearing in target list is normal — it's event-driven, not polled
- Use gateway logs to verify it's actually connected (see above)

### Message Content Intent not enabled
- Symptom: bot connects but never sees message content (empty messages)
- Fix: Discord Developer Portal → your app → Bot → Privileged Gateway Intents → enable "Message Content Intent"

## Token Corruption / Recovery

**Symptom**: Bot was working, then stopped. Logs show `LoginFailure: Improper token has been passed` or `401 Unauthorized`. The token in `.env` looks short (< 50 chars), starts with `cbot`, or is clearly a placeholder/client-id rather than a real bot token.

**Root cause**: `DISCORD_BOT_TOKEN` in `~/.hermes/.env` got overwritten — either by a setup wizard run, a migration, or manual edit that pulled in the wrong value.

**Recovery path**:
1. Check state-snapshot backups — Hermes saves pre-update snapshots:
   ```bash
   ls ~/.hermes/state-snapshots/
   cat ~/.hermes/state-snapshots/<latest>/.env | grep DISCORD_BOT_TOKEN
   ```
2. Verify the snapshot token is valid before restoring:
   ```bash
   curl -sS -m 15 -H "Authorization: Bot <token>" https://discord.com/api/v10/users/@me
   # Should return {"id": "...", "username": "...", "bot": true} not {"code": 0, "message": "401: Unauthorized"}
   ```
3. Restore token:
   ```python
   # edit ~/.hermes/.env — replace DISCORD_BOT_TOKEN= line with snapshot value
   ```
4. `hermes gateway restart`

A valid Discord bot token is 72 chars, contains two dots, and starts with the bot's snowflake ID base64-encoded (e.g. `MTUwMTAz...`). Anything shorter or without dots is wrong.

## DISCORD_ALLOWED_USERS Must Be Numeric ID

`DISCORD_ALLOWED_USERS` must be set to the **numeric Discord user ID** (e.g. `1203560828645933086`), NOT a username string like `Lobek85`.

Setting it to a username means the bot runs but silently ignores all messages.

Get your numeric ID: Discord → Settings → Advanced → Developer Mode on → right-click your username anywhere → Copy User ID.

```bash
# correct
DISCORD_ALLOWED_USERS=1203560828645933086

# wrong — bot will ignore all messages
DISCORD_ALLOWED_USERS=Lobek85
```

## Config Locations

| Setting | File |
|---------|------|
| Bot token | `~/.hermes/.env` → `DISCORD_BOT_TOKEN` |
| Allowed users | `~/.hermes/.env` → `DISCORD_ALLOWED_USERS` (comma-separated user IDs) |
| Allowed channels | `~/.hermes/.env` → `DISCORD_ALLOWED_CHANNELS` (empty = all) |
| require_mention | `~/.hermes/config.yaml` → `discord.require_mention: true` |
| auto_thread | `~/.hermes/config.yaml` → `discord.auto_thread: true` |
