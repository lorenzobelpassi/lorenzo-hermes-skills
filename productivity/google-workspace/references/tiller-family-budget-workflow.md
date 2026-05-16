# Tiller family budget / cash-flow workflow

Use this when the user asks to analyze a Tiller Google Sheet and build a managed household budget, cash-flow analysis, or P&L inside the workbook.

## Core workflow

1. **Confirm access and locate workbook**
   - Use Drive search for `name contains 'Tiller'` and/or the provided sheet URL.
   - Read workbook metadata first; Tiller usually has tabs like `Transactions`, `Categories`, `Balances`, `Accounts`, `Monthly Budget`, `Yearly Budget`.

2. **Inspect structure before writing**
   - Read headers and samples from:
     - `Transactions!A1:S20`
     - `Categories!A1:P80`
     - `Balances!A1:Y30`
     - `Accounts!A1:Q30`
   - Identify date, description, category, amount, account, institution columns.

3. **Normalize personal-finance P&L**
   - For P&L, **exclude bank transfers and credit-card payment mechanics** to avoid double-counting. Examples: `Online Transfer`, `Payment Thank You`, `American Express ACH Pmt`, `Citi Card Online Payment`, `Capital One Mobile Pmt`, `Discover E-payment`, etc.
   - Show those separately in a **Cash Flow Analysis** tab because they matter for liquidity.
   - Build description-based classification rules for uncategorized transactions, but label uncertain items as review-needed rather than pretending they are known.

4. **Recommended tabs to create**
   - `Family Budget OS` — operating rules, headline findings, links to other tabs.
   - `Family P and L` — normalized income/outgoings by month, Jan-Apr or trailing average, target budget, variance, notes.
   - `Cash Flow Analysis` — income deposits, operating expenses, transfer/CC-payment outflows, transfer inflows, net raw cash movement, balance snapshot.
   - `Cut Plan` — prioritized cut opportunities with current avg/month, target/month, monthly improvement, action, reason.
   - `Managed Rules` — pattern → budget category → group → management rule.

5. **Cut-plan logic**
   Prioritize categories that are both material and controllable:
   - Zelle/Venmo/wires needing review (must tag payee/purpose)
   - ATM/cash withdrawals
   - debt interest, overdraft, late/service fees
   - restaurants/dining
   - shopping/general merchandise
   - subscriptions/software
   - phone/internet plans
   - nonessential auto spend

6. **Formatting pitfalls**
   - Month headers such as `2026-01` can be interpreted by Google Sheets as dates/serial numbers and displayed as currency if a currency format is applied. Prefix month labels with an apostrophe (`'2026-01`) or apply text format to the header row before/after writing.
   - Apply currency formatting only to data rows, not header rows.
   - Freeze row 2 and auto-resize columns for readability.

7. **Privacy / safety**
   - Treat finance data as sensitive. Do not expose full transaction dumps unless requested.
   - Do not change source Tiller tabs unless explicitly asked; create separate analysis tabs instead.
   - In the final response, summarize material findings and link to the new tabs, but avoid listing excessive personal transaction detail.

## Useful implementation pattern

Use Python with `googleapiclient` and the existing OAuth pickle token:

```python
import pickle, warnings
warnings.filterwarnings('ignore')
from googleapiclient.discovery import build

with open('/path/to/token.pickle', 'rb') as f:
    creds = pickle.load(f)
sheets = build('sheets', 'v4', credentials=creds)

meta = sheets.spreadsheets().get(
    spreadsheetId=SHEET_ID,
    fields='properties/title,sheets(properties(title,sheetId,gridProperties(rowCount,columnCount)))'
).execute()
```

When creating analysis tabs, use `spreadsheets().batchUpdate()` for adding sheets and formatting, and `values().batchUpdate(valueInputOption='USER_ENTERED')` for values.
