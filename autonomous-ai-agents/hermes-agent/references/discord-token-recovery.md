# Discord Token Recovery / Reconnect Runbook

Use this when Hermes Gateway is running but Discord will not connect, messages stop being processed, or logs show token/auth failures.

## Symptoms

Look for any of these in `~/.hermes/logs/gateway.log` or `~/.hermes/logs/gateway.error.log`:

- `discord.errors.LoginFailure: Improper token has been passed.`
- `401 Unauthorized` from `discord/http.py` or Discord REST
- `✗ discord error: discord connect timed out after 30s` after a failed token change
- repeated `Reconnect discord ... timed out`

## Fast Diagnosis

```bash
# Gateway process status
hermes gateway status

# Recent Discord lines
grep -i "discord\|loginfailure\|unauthorized\|reconnect" ~/.hermes/logs/gateway.log ~/.hermes/logs/gateway.error.log | tail -80

# Show Discord env shape without leaking token
python3 - <<'PY'
from pathlib import Path
import re
text=(Path.home()/'.hermes/.env').read_text(errors='ignore')
for k in ['DISCORD_BOT_TOKEN','DISCORD_ALLOWED_USERS','DISCORD_ALLOWED_CHANNELS']:
    m=re.search(rf'^{k}=(.*)$', text, re.M)
    if m:
        v=m.group(1).strip()
        shown=(v[:6]+'...'+v[-4:]) if 'TOKEN' in k and len(v)>12 else v
        print(k, 'len=', len(v), 'value=', shown)
PY
```

A real Discord bot token commonly has two dots and should validate against Discord's API. A placeholder/client-id-like value (for example a bare bot/client ID or a `cbot...` string) will fail.

## Validate the Token Directly

This checks the token without printing it:

```bash
python3 - <<'PY'
from pathlib import Path
import re, subprocess, json
text=(Path.home()/'.hermes/.env').read_text(errors='ignore')
token=re.search(r'^DISCORD_BOT_TOKEN=(.*)$', text, re.M).group(1).strip()
p=subprocess.run([
  'curl','-sS','-m','15','-H',f'Authorization: Bot {token}',
  'https://discord.com/api/v10/users/@me'
], capture_output=True, text=True)
print('curl_exit', p.returncode)
data=json.loads(p.stdout)
print({k:data.get(k) for k in ['id','username','bot','code','message']})
PY
```

Healthy result includes the bot ID, username, and `bot: True`, e.g.:

```text
{'id': '1501030574746501210', 'username': 'bot...', 'bot': True, 'code': None, 'message': None}
```

Unhealthy result usually includes:

```text
{'code': 0, 'message': '401: Unauthorized'}
```

## Recovery Pattern

1. Find a previous valid token in backups/snapshots without printing the full value:

```bash
python3 - <<'PY'
from pathlib import Path
import re
for p in Path.home().joinpath('.hermes').rglob('*'):
    if p.is_file() and p.stat().st_size < 2_000_000:
        try: s=p.read_text(errors='ignore')
        except Exception: continue
        if 'DISCORD_BOT_TOKEN' in s:
            m=re.search(r'^DISCORD_BOT_TOKEN=(.*)$', s, re.M)
            if m:
                v=m.group(1).strip()
                print(p, 'len=', len(v), 'dots=', v.count('.'), 'prefix=', v[:6], 'suffix=', v[-4:])
PY
```

2. Back up `~/.hermes/.env` before editing.
3. Restore the valid `DISCORD_BOT_TOKEN` from a known-good snapshot or re-copy it from the Discord Developer Portal.
4. Set `DISCORD_ALLOWED_USERS` to the numeric personal Discord user ID, not the username and not the bot/client ID.
5. Restart the gateway:

```bash
hermes gateway restart
```

6. Verify:

```bash
grep -i "discord" ~/.hermes/logs/gateway.log | tail -30
```

Healthy reconnect lines:

```text
[Discord] Connected as bot...#....
✓ discord connected
Gateway running with 3 platform(s)
Channel directory built: ... target(s)
```

## Pitfalls

- `DISCORD_ALLOWED_USERS=Lobek85` is not as reliable as the numeric Discord user ID. Use the numeric ID.
- The Discord client/application ID is not the bot token. If the token looks like an ID or placeholder, validate before restarting repeatedly.
- A gateway restart cannot fix an invalid token; validate `/users/@me` first.
- Do not paste or print the full token into chat/logs. Show length, dot count, prefix/suffix only.
