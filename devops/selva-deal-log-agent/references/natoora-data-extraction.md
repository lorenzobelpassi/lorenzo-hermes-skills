# Natoora Data Extraction Reference

## Gmail Search Queries

```
from:natoora.com has:attachment
from:lorenzo.belpassi@natoora.com
```

## Attachment Download (Python)

```python
import pickle
import base64
from googleapiclient.discovery import build

creds = pickle.load(open('/Users/lorenzobelpassi/.hermes/gmail_token.pickle', 'rb'))
service = build('gmail', 'v1', credentials=creds)

# Find messages with attachments
results = service.users().messages().list(userId='me', q='from:natoora.com has:attachment', maxResults=20).execute()

for msg in results.get('messages', []):
    full = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
    
    def download_attachments(payload, msg_id):
        if 'parts' in payload:
            for part in payload['parts']:
                filename = part.get('filename')
                if filename and (filename.endswith('.csv') or filename.endswith('.xlsx')):
                    att_id = part['body'].get('attachmentId')
                    if att_id:
                        att = service.users().messages().attachments().get(
                            userId='me', messageId=msg_id, id=att_id
                        ).execute()
                        data = base64.urlsafe_b64decode(att['data'])
                        with open(f'/tmp/{filename}', 'wb') as f:
                            f.write(data)
                download_attachments(part, msg_id)
    
    download_attachments(full['payload'], msg['id'])
```

## Key Data Files (Feb 2026 Export)

| File | Contents |
|------|----------|
| Miami Cold Outreach - Raw.csv | 2,037 scraped restaurant prospects (name, email, phone, rating, reviews, category) |
| PRODUCE BID SHEET JUNE 11_ MILA.xlsx | MILA order guide |
| Makoto Produce List.xlsx | Makoto order guide |
| price-list_FisherIsland_WHOLESALE.xlsx | Fisher Island pricing |
| MAPLE & ASH BUYING GUIDE X NATOORA UPDATED.xlsx | Maple & Ash buying guide |
| Papi Steak & Gekko Produce Catalog Q3 2025.csv | Papi Steak + Gekko catalog |
| Centner Academy Order Guide.csv | Centner Academy orders |
| MrC.csv | Mr. C Miami orders |
| Daniels.xlsx | Fiola Miami master perpetual |

## Filtering Cold Outreach for High-End

```python
import csv
import json

with open('/tmp/Miami Cold Outreach - Raw.csv', 'r') as f:
    rows = list(csv.DictReader(f))

# Known chains to exclude
chains = [
    'el toro loco', 'havana 1957', 'bulla gastrobar', 'la carreta', 
    'stk', 'nobu', 'zuma', 'komodo', 'carbone', 'capital grille',
    'ruth chris', 'morton', 'pf chang', 'benihana', 'bubba gump',
    'rusty pelican', 'cheesecake factory', 'seasons 52'
]

# Dedupe by name+phone, filter quality
restaurants = {}
for r in rows:
    name = r.get('name', '').strip()
    phone = r.get('phone', '').strip()
    key = f"{name}|{phone}"
    email = r.get('email', '').strip()
    
    if not email:
        continue
    
    try:
        rating = float(r.get('rating', 0) or 0)
        reviews = int(r.get('reviews', 0) or 0)
    except:
        continue
    
    # Quality threshold
    if rating < 4.0 or reviews < 100:
        continue
    
    # Exclude chains
    if any(chain in name.lower() for chain in chains):
        continue
    
    if key not in restaurants:
        restaurants[key] = {
            'name': name,
            'email': email,
            'phone': phone,
            'city': r.get('city', ''),
            'rating': rating,
            'reviews': reviews,
            'category': r.get('subtypes', ''),
        }

# Premium filter: 4.6+, 1000+ reviews
premium = [r for r in restaurants.values() if r['rating'] >= 4.6 and r['reviews'] >= 1000]
# Result: ~166 high-end independents
```

## Existing Warm Accounts

These accounts had active pricing sheets — warm leads for Selva:

1. **MILA** — Asian fusion, Miami Beach
2. **Makoto** — Japanese, Bal Harbour
3. **Fisher Island Club** — Private club/resort (ultra high-end)
4. **Maple & Ash** — Steakhouse
5. **Fiola Miami** — Italian fine dining
6. **Centner Academy** — Private school (institutional)
7. **Papi Steak** — Celebrity steakhouse, Miami Beach
8. **Gekko** — Japanese steakhouse, Miami Beach
9. **Tin Tin / Tinta y Cafe** — Cafe
10. **Mr. C Miami** — Luxury hotel, Coconut Grove

## Bulk Email Body Extraction (for CRM Ingestion)

When user wants to extract leads/deals from email threads (not just attachments), pull full message bodies and extract structured records.

### Search & Pull Pattern

```python
import pickle, warnings, json, base64, re
warnings.filterwarnings('ignore')
from googleapiclient.discovery import build

with open('/Users/lorenzobelpassi/.hermes/personal_gmail_token.pickle', 'rb') as f:
    creds = pickle.load(f)
service = build('gmail', 'v1', credentials=creds)

# Search for emails from a domain
results = service.users().messages().list(userId='me', q='from:natoora', maxResults=100).execute()
messages = results.get('messages', [])

emails = []
for msg in messages:
    m = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
    headers = {h['name']: h['value'] for h in m.get('payload', {}).get('headers', [])}
    
    # Extract body (handles multipart)
    def get_body(part):
        if part.get('body', {}).get('data'):
            return base64.urlsafe_b64decode(part['body']['data']).decode('utf-8', errors='ignore')
        if part.get('parts'):
            for p in part['parts']:
                result = get_body(p)
                if result:
                    return result
        return ""
    
    body = get_body(m.get('payload', {}))
    body = re.sub(r'<[^>]+>', ' ', body)  # Strip HTML
    body = re.sub(r'\s+', ' ', body).strip()[:3000]  # Collapse whitespace, truncate
    
    emails.append({
        'id': msg['id'],
        'date': headers.get('Date', ''),
        'from': headers.get('From', ''),
        'to': headers.get('To', ''),
        'subject': headers.get('Subject', ''),
        'body': body
    })

print(json.dumps(emails, indent=2))
```

### Token Notes

| Account | Token Path | Scope |
|---------|------------|-------|
| lorenzo.belpassi@gmail.com (personal) | ~/.hermes/personal_gmail_token.pickle | gmail.readonly, gmail.send, gmail.modify |
| lorenzo.belpassi@selva-partners.com | ~/.hermes/selva_outreach_token.pickle | full gmail + settings |
| chloe.sanchez@selva-partners.com | ~/.hermes/chloe_outreach_token.pickle | gmail.send, gmail.readonly, gmail.modify |

**Personal Gmail auth uses Chloe project credentials** (`~/.hermes/gmail_credentials.json` from project selva-495405) because:
- Selva Outreach project (`selva-outreach`) is internal to selva-partners.com org
- Personal Gmail (lorenzo.belpassi@gmail.com) can't auth against an internal org project
- Chloe project allows external accounts

Auth script: `~/.hermes/personal_gmail_auth.py`

### Fields to Extract (CRM Structure)

For each unique company/contact discovered in emails:

| Field | Source |
|-------|--------|
| Company | Email signature, "via Orders" pattern, or explicit mention |
| Contact Name | From header, signature block |
| Email | From header |
| Phone | Signature block |
| Address | Signature block |
| Role | Signature (Executive Chef, Director of Supply Chain, etc.) |
| Products | Order items mentioned in body |
| Order Frequency | Count of emails, daily/weekly pattern |
| Intel | Pricing discussions, menu development, account status |

### Pattern: "via Orders" Emails

Natoora CC's `orders-mia@natoora.com` on customer orders. These appear as:
```
From: "'Alejandro Rico' via Orders Mia" <orders-mia@natoora.com>
```

Extract the actual customer name from the single quotes. The real contact email is in the body (signature block) or prior thread messages.

### Discovered Accounts (from March 2026 emails)

**Active Natoora Miami Customers:**
- COTE Miami (Alberto Vargas, Purchasing)
- Mandolin Aegean Bistro (Robert Errichetti, Exec Chef + Alejandro Rico, Sous Chef)
- Van Leeuwen Ice Cream (Marisa Austin, Director Supply Chain) — NEW March 2026
- Mother Wolf Miami (Joselyn Spiewak)
- MBC Miami (Emmanuel Mendia + Angie Hossain) — prospect, pending account forms
- MegaYacht Provisions (Reinaldo Malave) — NEW March 2026, yacht provisioner, pickup model
- The Concours Club
- Bistro 8 x Daniela Soto-Innes
- Ezio's (George Musho)
- Karyu (Japanese)
- Mae's Room (Emma Anderson)

**Natoora Key Contacts:**
- Nicolas Brunk — Regional Sales Lead, 786.676.5092
- Chris Devlin — Sales
- Kayla — Customer Service (Flavor MIA), 786.779.2925
- Rodrigo Chacon — Operations Manager, 786.483.4132

**Natoora Operations Intel:**
- Delivery: Mon-Sat, next-day cutoff 11:59 PM
- Minimum: $100 (under $100 = $20 fee)
- Avg basket: ~$223
- Uses NatooraPro app for ordering

## Selva Target Criteria

Lorenzo's guidance: "We are not supplying chains, we are only hitting the top end of the market"

Target segments:
- Fine dining (any cuisine)
- High-end seafood
- Premium steakhouses
- Japanese/sushi (omakase level)
- Luxury hotels and private clubs
- Cruise lines (Carnival, Royal Caribbean, Norwegian — Miami HQ)

NOT targeting:
- Chains (even upscale ones like STK, Capital Grille)
- Mid-tier casual dining
- Fast casual
