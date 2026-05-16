# Selva Partners Gmail Account Reference

## Token Files (~/.hermes/)

| Account | Token File | Scopes |
|---------|-----------|--------|
| lorenzo.belpassi@selva-partners.com | selva_outreach_token.pickle | send, readonly, modify, settings.basic |
| chloe.sanchez@selva-partners.com | chloe_outreach_token.pickle | send, readonly, modify — MISSING settings.basic |
| chloe.lorenzob1987@gmail.com | gmail_token.pickle | (Gmail API not enabled for its project) |

Credentials JSON for both selva-partners.com accounts: ~/.hermes/selva_outreach_credentials.json

## Re-auth Chloe with settings.basic scope

```python
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/gmail.settings.basic',
]

flow = InstalledAppFlow.from_client_secrets_file(
    '/Users/lorenzobelpassi/.hermes/selva_outreach_credentials.json',
    scopes=SCOPES,
    redirect_uri='http://localhost:1'
)
auth_url, _ = flow.authorization_url(prompt='consent', access_type='offline')
print(auth_url)
```

Open URL in browser as chloe.sanchez@selva-partners.com. Browser will fail on localhost:1 — expected.
Paste back full redirect URL, then exchange the code to save new token to chloe_outreach_token.pickle.

## Email Signature Status

- Lorenzo: full branded HTML signature set (20,457 chars), verified working
- Chloe: NO signature set yet — pending re-auth with settings.basic scope

## Signature Field Substitutions (Lorenzo -> Chloe)

| Field | Lorenzo | Chloe |
|-------|---------|-------|
| Name | Lorenzo Belpassi | Chloe Sanchez |
| Title | Founder &amp; Managing Partner | Executive Assistant |
| Email href | mailto:lorenzo@selva-partners.com | mailto:chloe.sanchez@selva-partners.com |
| Email text | lorenzo@selva-partners.com | chloe.sanchez@selva-partners.com |
| Phone | (646) 286-4344 | (646) 286-4344 (temp — swap when Twilio number arrives) |

Logo, styling, website URL all stay identical.

## Org Logo

- Location: admin.google.com/ac/accountsettings > Personalization > Logo
- Required size: 320x132px PNG or GIF, max 30KB
- Current logo appears smushed — needs to be resized to correct aspect ratio
- Admin login: lorenzo.belpassi@selva-partners.com / Lollo2159!!@@
