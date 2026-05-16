# Natoora Email Extraction (March 2026)

Extracted 100 emails from `lorenzo.belpassi@gmail.com` containing Natoora correspondence.
These represent Natoora's Miami customer base — potential Selva targets.

## Token Used
- `~/.hermes/personal_gmail_token.pickle`
- OAuth via `~/.hermes/gmail_credentials.json` (selva-495405 project, External user type)

## Extraction Command
```python
import pickle, warnings, json, base64, re
warnings.filterwarnings('ignore')
from googleapiclient.discovery import build

with open('/Users/lorenzobelpassi/.hermes/personal_gmail_token.pickle', 'rb') as f:
    creds = pickle.load(f)

service = build('gmail', 'v1', credentials=creds)
results = service.users().messages().list(userId='me', q='from:natoora', maxResults=100).execute()
# ... extract body, headers, clean HTML
```

## Natoora Key Contacts (for reference)
| Name | Role | Email | Phone |
|------|------|-------|-------|
| Nicolas Brunk | Regional Sales Lead | nicolas.brunk@natoora.com | 786.676.5092 |
| Chris Devlin | Sales | chris.devlin@natoora.com | — |
| Kayla | Customer Service (Flavor MIA) | flavor-mia@natoora.com | 786.779.2925 |
| Rodrigo Chacon | Operations Manager | rodrigo.chacon@natoora.com | 786.483.4132 |

## Natoora Operations Intel
- Delivery: Mon-Sat, next-day cutoff 11:59 PM
- Minimum: $100 (under $100 = $20 fee)
- Avg basket: ~$223
- Avg daily sales: ~$7,100
- Total orders/day: ~32
- Uses NatooraPro app

## Confirmed Pricing
- Romaine Hearts (FL): $49/12x3 case
- Razor Clams in Olive Oil: $16.95 ea
- Valentine Pomelos: $6.49/lb
- Virgin Olive Oil: $8.90/L
- EVOO Arbequinha: $14.50/L

## Leads Pushed to Notion (11 records)
1. COTE Miami — Design District, Korean steakhouse
2. Mandolin Aegean Bistro — Buena Vista, high-volume
3. Van Leeuwen Ice Cream — National brand, NEW 3/16
4. MBC Miami — Prospect, awaiting forms
5. MegaYacht Provisions — Yacht provisioner, PICKUP
6. Mother Wolf Miami — Evan Funke restaurant
7. The Concours Club — Luxury car club F&B
8. Bistro 8 — Daniela Soto-Innes connection
9. Ezio's — Active account
10. Karyu — Japanese, specialty items
11. Mae's Room — Berry orders
