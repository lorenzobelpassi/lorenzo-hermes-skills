# Pickle-Based OAuth Alternative

When the standard `setup.py` flow is unavailable or the user already has a
`credentials.json` from Google Cloud Console (Desktop app type), you can use
the Python `google-auth-oauthlib` library directly to authorize and produce a
`gmail_token.pickle` file.

## When to use this
- User pastes raw credentials JSON in chat (Desktop app type)
- `setup.py --auth-url` / PKCE flow is unavailable
- Quick one-off setup where the user can run a local script themselves

## Files produced
- `~/.hermes/gmail_credentials.json` — save the pasted credentials JSON here
- `~/.hermes/gmail_token.pickle` — produced after browser auth

## Auth script (~/.hermes/gmail_auth.py)

```python
import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = [
    # Gmail
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.modify',
    # Calendar
    'https://www.googleapis.com/auth/calendar',
    # Drive
    'https://www.googleapis.com/auth/drive',
    # Docs
    'https://www.googleapis.com/auth/documents',
    # Sheets
    'https://www.googleapis.com/auth/spreadsheets',
    # Slides
    'https://www.googleapis.com/auth/presentations',
    # Contacts
    'https://www.googleapis.com/auth/contacts',
]

creds = None
token_path = os.path.expanduser('~/.hermes/gmail_token.pickle')
creds_path = os.path.expanduser('~/.hermes/gmail_credentials.json')

if os.path.exists(token_path):
    with open(token_path, 'rb') as token:
        creds = pickle.load(token)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
        creds = flow.run_local_server(port=0)
    with open(token_path, 'wb') as token:
        pickle.dump(creds, token)

print("Authentication successful! Token saved to ~/.hermes/gmail_token.pickle")
```

## Steps
1. Save credentials JSON to `~/.hermes/gmail_credentials.json`
2. Write the auth script to `~/.hermes/gmail_auth.py`
3. Tell user to run: `python3 ~/.hermes/gmail_auth.py`
4. Script opens browser — user signs in and approves
5. Token saved automatically on success

## Re-authorizing with new scopes
Delete the old token first, then re-run:
```bash
rm ~/.hermes/gmail_token.pickle
python3 ~/.hermes/gmail_auth.py
```

## Install dependencies
```bash
pip3 install google-auth google-auth-oauthlib google-api-python-client
```
Note: on macOS the script may install to ~/Library/Python/3.9/bin/ which
is not on PATH. Use `pip3` not `pip` on stock macOS.

## Pitfalls
- Script times out if the user doesn't complete the browser flow within ~60s.
  Run it in the user's own terminal, not via hermes terminal tool.
- `pip` may not exist on macOS — always use `pip3`.
- Python 3.9 (stock macOS) shows FutureWarning from google-auth — harmless.
