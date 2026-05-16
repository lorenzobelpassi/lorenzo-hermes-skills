# Selva Supplier Sourcing Map Workflow

Use this when Lorenzo asks to build or refresh a supplier sourcing map from Natoora/restaurant-produce archives, inbound POs, Google Sheet share emails, or public supplier research.

## Goal

Create an actionable Selva sourcing list that connects:

- Supplier / grower name
- Region and route type: local Florida, Miami importer, West Coast air/ground, NYC cross-dock, market/blended
- Product focus and example SKUs/quantities
- Source evidence: weekly inbound PO, dry-goods list, sales archive, public website, email/shared sheet reference
- Public website/contact note where reliably available
- Confidence: High / Medium / Low
- Selva lane: Brokerage/wholesale, Direct-to-chefs premium story, Dried goods/pantry ownership, Benchmark/route intelligence
- Opportunity rating: Own/Test, Quote/Watch, Benchmark/Verify, Avoid/Needs verification

## Source priority

1. **Natoora weekly inbound PO docs** — supplier-side purchases; best source for who Natoora bought from.
2. **Exported Google Sheets / Excel / PDFs** — EPL/F&V, NYC lists, stock availability, dry goods.
3. **Natoora 2025 sales archive** — demand/velocity signal, not margin unless prices/costs are present.
4. **Public supplier websites/directories** — enrichment only; do not invent contact info.
5. **Customer POs/email purchase orders** — useful for buyer demand, not supplier sourcing.

## Proven extraction steps

1. Search local files first:
   - `*WEEKLY INBOUNDS*`, `*PO*`, `*EPL*`, `*F&V*`, `*NYC*`, `*Dry Goods*`, `*Product Data*`, `*.xlsx`, `*.pdf`.
2. Search Natoora mbox backups for Google Drive/Sheets share emails:
   - Subjects like `F&V Report_NYC_EPL`, `MIAMI - EPL/YR - (Full F&V Range)`, `Stock Availability / Forecasting - Miami`.
   - Important: share emails usually do **not** contain the spreadsheet as an attachment. Treat them as evidence that a sheet exists, not as extracted data.
3. Parse PDFs with PyMuPDF when possible.
4. For malformed/iCloud-placeholder PDFs, do not pretend extraction succeeded. Mark as unreadable and ask/export another copy if needed.
5. Merge parsed line items with public enrichment.
6. Package both a working CSV and a readable Markdown summary.

## Known Week 6 fresh supplier targets

From `WEEKLY INBOUNDS/Week 6 PO.pdf`:

- Natoora US Inc. NYC — route/benchmark hub, not grower.
- C&B Farms — Florida local supplier; verify exact identity.
- Exotic Growers — Homestead/Miami-Dade tropical/exotic fruit; verify contact.
- Naturama Foods — Miami herbs/distribution; verify contact/domain.
- Coosemans Miami / Interproduce — specialty produce distributor; strong public site.
- Tiny Farm — Homestead regenerative local farm; strong direct-to-chef story.
- Ray’s Heritage — Belle Glade/Palm Beach County grower/packer; strong Florida volume source.
- Ark Foods — specialty vegetable grower/brand; strong public site.
- County Line Harvest / County Line Air — California organic/specialty greens; verify `Air` route label.
- Sunny Cal — likely California citrus/fruit; low confidence until verified.
- Miami Agro Import — South Florida importer/distributor; strong public site.
- Kai-Kai Farm — Indiantown/Martin County farm; strong local premium story.
- Lindcove Ranch — California citrus; medium-low confidence without owned site.
- Natoora US Inc LA Market — West Coast route/benchmark hub, not grower.
- Jaem Produce — Miami wholesale vendor; verify exact contact.
- Tropical Fresh Citrus — citrus supplier; low confidence until exact identity verified.
- Galpin Farms — Central Valley fruit; medium confidence via public partner/social evidence.
- Valdivia Farms — California tomatoes/specialty produce; medium confidence via public social evidence.
- Dunagan Family Farms — Homestead farm; verify product/commercial role.
- Pine Island Farms — ambiguous; low confidence until exact vendor verified.
- Paradise Farms — Homestead certified organic/sustainable farm; strong public site.

## Pantry / dried-goods sourcing signals

High-priority ownership candidates from NYC dry-goods docs + Natoora 2025 demand signals:

- Dried Butter Beans
- Dried Giganti Beans
- Dried Sorana Beans
- Cantabrian anchovies / conservas
- Seed + Mill tahini
- Minus 8 vinegar / premium vinegar category
- Premium olive oil, e.g. Senia category
- Carnaroli rice

Treat these as **demand/opportunity signals** until direct supplier/importer identities and landed costs are verified.

## Output package pattern

Create:

- `selva_supplier_sourcing_map_finished.csv` — spreadsheet/list view.
- `selva_supplier_sourcing_map_finished.md` — readable summary with priority targets.
- `source_notes.md` — source evidence and limitations.
- Optional extracted text files from PDFs.
- Zip the folder and send it to Lorenzo.

## Pitfalls

- Do not confuse customer purchase orders from hotels/restaurants with supplier-side weekly inbounds.
- Do not expose raw Natoora archive data externally; use it internally for source mapping and Selva strategy.
- Do not present weak directory hits as verified supplier contacts; mark confidence and verification need.
- If Google Sheet share emails are found without attachments, say so clearly and use local/exported copies only if available.
- If a PDF exists but PyMuPDF fails with `FileDataError` / `no objects found`, mark it malformed/unreadable rather than extracting from it.
