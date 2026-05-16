# Selva Notion Cockpit + Natoora Document Ingestion (2026-05-06)

## Why this matters

Lorenzo wants the Notion interface to stay palatable for daily use while still building against the six-month Selva business plan. The backend may contain many databases and raw documents, but the daily UI should feel like an execution cockpit.

Core daily question:

> What do I do today? Who do I see? What am I selling? What happens next?

## Six-month plan anchors

Plan window: 2026-05-01 through 2026-10-31
Total: 184 days
Target: $157,000 net
As of 2026-05-06: 6 days elapsed, 178 remaining, 3.3% through
Monthly pace: about $26.2K net/month
Before actual booked net is loaded, simple remaining-day pressure is roughly target gap / days remaining.

## Daily Notion front page

Name: `Selva Daily Cockpit`

Visible sections only:

1. Today
   - Max 5 items
   - Due/overdue opportunities and top money-moving actions.
2. People To See
   - Max 10 items
   - Route-ready A/A+ accounts only; hide research backlog.
3. Product/Sample Angle
   - Max 3-6 products
   - Today’s sample kit/product angle, not the full Product Catalog.
4. Drafts To Approve
   - Max 5 items
   - Ready-to-send Gmail drafts only; no blind raw-lead outreach.
5. Capture
   - Fast voice-note/field-note capture; do not make Lorenzo manage raw databases.
6. End of Day
   - Wins/losses/moved opportunities, product feedback, next action/date.

Rule: every visible row must imply an action.

## Backend databases

CRM/OS databases now include eight databases:

1. Accounts
2. Contacts
3. Opportunities
4. Interactions
5. Market Signals
6. Product Catalog
7. Sample Kits
8. Source Documents

Daily front page should not display all eight. Hide backend databases behind filtered linked views, rollups, templates, and agent workflows.

## Source Documents database

Needed because Lorenzo has a large local Natoora archive. Do not dump all docs into daily pages.

Suggested fields:
- Document Name
- Original Path
- Category
- File Type
- Revenue Use
- Route To Database
- Text Excerpt
- Imported?
- Linked Account
- Linked Product
- Linked Opportunity

## Natoora local document ingestion

Source folder used:

```text
/Users/lorenzobelpassi/Library/Mobile Documents/com~apple~CloudDocs/NATOORA
```

Revenue OS local package:

```text
/Users/lorenzobelpassi/selva-agents/revenue_os
```

New module:

```text
revenue_os/document_ingestion.py
```

CLI:

```bash
cd /Users/lorenzobelpassi/selva-agents/revenue_os
python3 -m revenue_os.cli ingest-natoora-docs "/Users/lorenzobelpassi/Library/Mobile Documents/com~apple~CloudDocs/NATOORA" --out-dir exports/natoora_docs --max-text-chars 1500
```

Generated outputs:

```text
exports/natoora_docs/natoora_document_manifest.json
exports/natoora_docs/natoora_document_index.md
exports/natoora_docs/source_documents_import.csv
```

Observed archive inventory:
- 217 total files
- 130 PDFs
- 30 XLSX
- 7 CSV
- 7 DOCX
- 2 PPTX
- 18 images
- 3 archives, including a large email backup zip inventoried only

Categories observed:
- price_list: 71
- reference: 42
- sales_performance: 41
- image: 18
- invoice: 18
- onboarding: 9
- brand_education: 6
- target_accounts: 5
- hotel_strategy: 4
- archive: 3

Routing logic:
- price lists / availability / order guides -> Product Catalog
- invoices / credit notes -> Interactions
- hotel strategy / amenity docs -> Accounts
- client lists / leads / prospect docs -> Accounts
- weekly/monthly reports / performance sheets -> Opportunities
- brand/education/seasonal docs -> Product Catalog
- archives/images -> Source Documents first

Extraction notes:
- PyMuPDF worked for many text PDFs.
- openpyxl was available for XLSX.
- python-docx and python-pptx were not installed, so office ZIP XML extraction was implemented as a lightweight fallback.
- Pages/Numbers files were inventoried only; deeper extraction requires Apple conversion/export.
- Images were inventoried, not OCR’d.
- Large email ZIP was inventoried, not unpacked.

## Palatable dashboard spec

New module:

```text
revenue_os/notion_dashboard.py
```

CLI:

```bash
cd /Users/lorenzobelpassi/selva-agents/revenue_os
python3 -m revenue_os.cli cockpit-spec --out-md exports/selva_daily_cockpit.md --out-json exports/selva_daily_cockpit.json
```

Generated outputs:

```text
exports/selva_daily_cockpit.md
exports/selva_daily_cockpit.json
```

Design rules:
- Do not show all databases on the daily front page.
- Every visible row must imply an action.
- Hide raw source documents behind rollups/links.
- Limit sections to 5-10 visible items.
- Use capture templates/buttons; Lorenzo should not manually manage databases.
- Agents are backend workers; Notion cockpit is the operator UI.

## Testing

Use custom runner because pytest was not installed in system Python:

```bash
cd /Users/lorenzobelpassi/selva-agents/revenue_os
python3 run_tests.py
```

Session ended with 15/15 custom tests passing after adding document ingestion and cockpit tests.
