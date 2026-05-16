# Selva Partners Google Account Map

## Active Token Files (updated May 2026)

| Token path | GCP Project | Scopes | Valid? | Account |
|---|---|---|---|---|
| ~/.hermes/selva_outreach_token.pickle | selva-outreach (333270...) | gmail.send, gmail.readonly, gmail.modify, gmail.settings.basic, calendar, drive, documents, spreadsheets, contacts | VALID (re-authed May 2026) | lorenzo.belpassi@selva-partners.com |
| ~/.hermes/chloe_outreach_token.pickle | selva-outreach (333270...) | gmail.send, gmail.readonly, gmail.modify, gmail.settings.basic | VALID | chloe.sanchez@selva-partners.com |

## Retired / Abandoned Tokens (cosecha-491019 project — do not use)

| Token path | Status |
|---|---|
| ~/.hermes/gmail_token.pickle | ABANDONED — old cosecha-491019 project |
| ~/.hermes/personal_gmail_token.pickle | ABANDONED — chloe.lorenzob1987@gmail.com retired |
| ~/.hermes/selva_gmail_token.pickle | ABANDONED — old cosecha-491019 project |

These files can be deleted. The cosecha-491019 GCP project itself can be shut down.

## OAuth Apps / Credential Files

| File | GCP Project | Notes |
|---|---|---|
| ~/.hermes/selva_outreach_credentials.json | selva-outreach | ACTIVE — use this for all new auth flows |
| ~/.hermes/gmail_credentials.json | cosecha-491019 | RETIRED — do not use |

## Account Consolidation (completed May 2026)

- `chloe.lorenzob1987@gmail.com` has been retired — all activity moved to `chloe.sanchez@selva-partners.com`
- Single GCP project: `selva-outreach` under `selva-partners.com` Workspace org
- Two accounts: Lorenzo (work) + Chloe (work)
- No service account keys (org policy blocks them — use OAuth pickle tokens)

## Re-auth Pattern: Minimal Disruption

When re-authing, keep the same token filenames. Only the token content changes — no agent scripts, cron jobs, or code references need updating.

Lorenzo's full scope list for re-auth:
```
https://www.googleapis.com/auth/gmail.send
https://www.googleapis.com/auth/gmail.readonly
https://www.googleapis.com/auth/gmail.modify
https://www.googleapis.com/auth/gmail.settings.basic
https://www.googleapis.com/auth/calendar
https://www.googleapis.com/auth/drive
https://www.googleapis.com/auth/documents
https://www.googleapis.com/auth/spreadsheets
https://www.googleapis.com/auth/contacts
```

Auth URL generation (no PKCE — avoids "Missing code verifier" errors):
```python
import json, urllib.parse, os
with open(os.path.expanduser('~/.hermes/selva_outreach_credentials.json')) as f:
    cfg = json.load(f).get('installed') or json.load(f).get('web') or {}
params = {
    'response_type': 'code',
    'client_id': cfg['client_id'],
    'redirect_uri': 'http://localhost:1',
    'scope': ' '.join(SCOPES),
    'access_type': 'offline',
    'prompt': 'consent',
}
url = 'https://accounts.google.com/o/oauth2/auth?' + urllib.parse.urlencode(params)
```

Exchange with curl (codes expire in ~60s):
```bash
curl -s -X POST https://oauth2.googleapis.com/token \
  -d "code=CODE" \
  -d "client_id=CLIENT_ID" \
  -d "client_secret=CLIENT_SECRET" \
  -d "redirect_uri=http://localhost:1" \
  -d "grant_type=authorization_code"
```

Then build Credentials object and pickle:
```python
import pickle
from google.oauth2.credentials import Credentials
creds = Credentials(
    token=token_response['access_token'],
    refresh_token=token_response['refresh_token'],
    token_uri='https://oauth2.googleapis.com/token',
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    scopes=SCOPES,
)
with open(os.path.expanduser('~/.hermes/selva_outreach_token.pickle'), 'wb') as f:
    pickle.dump(creds, f)
```

## Diagnostic: Inspecting Pickle Tokens

```python
python3 << 'EOF'
import pickle, os, warnings
warnings.filterwarnings('ignore')

tokens = {
    'Lorenzo': '~/.hermes/selva_outreach_token.pickle',
    'Chloe':   '~/.hermes/chloe_outreach_token.pickle',
}
for name, path in tokens.items():
    with open(os.path.expanduser(path), 'rb') as f:
        creds = pickle.load(f)
    print(f'=== {name} ===')
    print(f'  valid:   {creds.valid}')
    print(f'  expired: {creds.expired}')
    print(f'  scopes:  {sorted(creds.scopes)}')
    print()
EOF
```

## Signature State (as of May 2026)

- **Lorenzo**: Full branded HTML signature with embedded base64 logo, ~20K chars. Name: Lorenzo Belpassi, Title: Founder & Managing Partner, Phone: (646) 286-4344.
- **Chloe**: Mirror of Lorenzo's — Name: Chloe Sanchez, Title: Executive Assistant, same phone (temporary until Twilio number assigned).

Fields to swap Lorenzo → Chloe:
- `>Lorenzo Belpassi<` → `>Chloe Sanchez<`
- `>Founder &amp; Managing Partner<` → `>Executive Assistant<`
- `mailto:lorenzo@selva-partners.com` → `mailto:chloe.sanchez@selva-partners.com`
- `>lorenzo@selva-partners.com<` → `>chloe.sanchez@selva-partners.com<`

## Org Logo

- Correct format: 320x132px PNG, under 30KB
- Prepared file: ~/Desktop/selva_logo_320x132.png
- Upload at: admin.google.com → Account settings → Personalization → Logo

## Scope Requirements Per Task

| Task | Required scope |
|---|---|
| Send email | gmail.send |
| Read email | gmail.readonly |
| Modify labels | gmail.modify |
| Read/write Gmail signature | gmail.settings.basic |
| Calendar | calendar |
| Drive | drive |
| Docs | documents |
| Sheets | spreadsheets |
| Contacts | contacts |
