# Selva Intelligence OS — Prototype 001 Build Notes

Session learning from building the first working local Selva Intelligence OS prototype inside `/Users/lorenzobelpassi/selva-agents/revenue_os`.

## Product framing

Use the name **Selva Intelligence OS** for the infrastructure/product and **Prototype 001** for the first working proof.

Frame it as:

> Operating intelligence infrastructure that turns messy business information into daily actions, weekly management reporting, relationship-risk flags, and continuous process improvement.

Avoid framing it as a chatbot. The important loop is:

```text
messy input → source signals → bad-data checks → daily brief → weekly management report → risk flags → efficiency recommendations → supervised actions
```

## Reporting model

Model weekly/monthly management reporting after Natoora-style reports:

```text
1. What happened
2. Why it happened
3. What changed vs last week/month
4. Which customers/products/suppliers caused it
5. What issues created lost sales or margin leakage
6. What the agent recommends next
7. What needs management approval
```

Reports should include numbers plus management commentary, cause/effect, operational issue, and next action.

## First prototype architecture

When proving a company intelligence OS, build local structured outputs before deep Notion/API automation:

1. Add parser/intake for weekly PDF or text reports.
2. Convert extracted text into operating signals.
3. Classify relationship risk.
4. Generate efficiency/process recommendations.
5. Produce a daily operating brief.
6. Produce a weekly management report.
7. Write JSON/CSV/Markdown outputs that can later be imported into Notion.
8. Add tests for each layer and one full run.

Working CLI shape used:

```bash
cd /Users/lorenzobelpassi/selva-agents/revenue_os
python3 -m revenue_os.cli intelligence-weekly /path/to/Weekly_Report.pdf --out-dir exports/intelligence_os/latest
```

Outputs used:

```text
parsed_report.json
relationship_risks.json
efficiency_recommendations.json
daily_operating_brief.md
weekly_management_report.md
source_documents.csv
```

## Relationship risk rule

Level 3+ relationship risk must remain supervised:

```text
Agent drafts only. Lorenzo approves before anything is sent.
Tone: soft, solution-oriented, supervised.
Response rule: Acknowledge → Own → Offer Solution → Ask Preference → Track
```

In Prototype 001, competitor pricing, spend decline, food-cost pressure, and 0%/low-margin pressure should trigger Level 3 relationship risk rather than being treated as normal sales movement.

## Efficiency layer rule

Keep the improvement loop permanent:

> Can this be more efficient and better?

Convert signals into process recommendations when they indicate:

- logistics delays
- shortages / not availables
- forecasting failures
- repeated service problems
- margin leakage / lost sales
- competitor pressure or relationship risk

Pitfall: do not convert every normal sales-performance sentence into a generic recommendation. Deduplicate recommendations and skip normal sales commentary unless it mentions lost sales, margin, food cost, competitor, shortage, or similar operational friction.

## Good daily brief format

Use the existing company-operating-agents daily format exactly:

```text
1. What Happened
2. Why It Matters
3. What the Agent Can Do
4. What Needs Supervision
5. What We Learned
```

The brief should be concise and action-oriented. It should not read like raw PDF extraction.

## Good weekly management report sections

A useful first Natoora-style weekly report can use:

```text
1. Executive Summary
2. Sales Performance
3. Customer Numbers
4. New / Reactivated / Dormant Accounts
5. Product Performance
6. Fulfilment / Not Availables
7. Supplier / Buying Notes
8. Logistics / Delivery Issues
9. Service Performance
10. Margin / Lost Sales
11. Relationship Risk
12. Efficiency Improvements
13. Next Week Priorities
```

## Prototype caveat

PDF/text parsing is directional. It can extract useful signals and commentary, but exact account/product/order intelligence needs structured operating data:

1. order/sales export
2. Growers Price List / product price list
3. messy notes or voice transcript

The next phase should move from directional report parsing to exact metrics: sales vs budget, order frequency, average basket, active/new/dormant customers, product trends, supplier performance, and margin/lost sales by customer/product.

## Phase 002 structured-data layer

After Prototype 001 proves PDF/report intelligence, add structured sales/order and **Growers Price List** CSV ingestion before deeper Notion automation. "Growers Price List" is the user-facing term; older `supplier`/`price-list` names may remain as compatibility aliases only.

Working CLI shape used:

```bash
cd /Users/lorenzobelpassi/selva-agents/revenue_os
python3 -m revenue_os.cli intelligence-weekly /path/to/Weekly_Report.pdf \
  --sales-csv /path/to/orders.csv \
  --growers-price-list-csv /path/to/growers_price_list.csv \
  --week-start 2025-09-08 \
  --week-end 2025-09-14 \
  --out-dir exports/intelligence_os/latest
```

Sales/order parser should accept common columns like:

```text
Order Date, Customer, Product, Quantity, Unit Price, Unit Cost, Revenue, Budget, Order ID
```

Growers Price List parser should accept common columns like:

```text
Grower/Farm, Product, Pack Size, Available, Unit Cost, Suggested Price, Previous Cost
```

Phase 002 outputs add:

```text
sales_summary.json
growers_price_list_summary.json
price_list_summary.json  # backward-compatible alias when needed
```

Structured data should feed the management report with exact metrics:

- sales vs budget and percentage to budget
- number of orders
- active customers
- order frequency by customer
- average basket
- top products by sales/quantity/margin
- dormant account movement
- unavailable products by grower/supplier
- grower cost increases
- margin-pressure products

Important: dormant account movement from one export is not automatically a relationship-risk escalation. Treat it as account movement unless there is frustration, repeated issue, competitor pressure, spend decline context, or management-defined risk threshold.

## Verification pattern

For this class of prototype, verify:

```bash
python3 run_tests.py
python3 -m revenue_os.cli intelligence-weekly /path/to/report.pdf --out-dir exports/intelligence_os/latest
python3 -m revenue_os.cli intelligence-weekly /path/to/report.pdf --sales-csv /path/to/orders.csv --growers-price-list-csv /path/to/growers_price_list.csv --week-start YYYY-MM-DD --week-end YYYY-MM-DD --out-dir exports/intelligence_os/latest_structured
```

Then inspect:

- `daily_operating_brief.md` for actionable five-section brief.
- `weekly_management_report.md` for exact structured metrics plus management commentary and next actions.
- `relationship_risks.json` for Level 3+ supervision flags.
- `efficiency_recommendations.json` for concise, non-duplicative process improvements.
- `sales_summary.json` for sales/order metrics when a sales CSV is provided.
- `growers_price_list_summary.json` for grower/product metrics when a Growers Price List is provided.
- `price_list_summary.json` only as a backward-compatible alias when present.
