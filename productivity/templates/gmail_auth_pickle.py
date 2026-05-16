"""
Pickle-based Google OAuth flow.
Saves token to ~/.hermes/gmail_token.pickle.
Run locally in user's terminal (opens browser).
Re-run after adding new scopes (delete old token first).
"""
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
