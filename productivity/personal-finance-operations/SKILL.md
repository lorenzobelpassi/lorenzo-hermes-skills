---
name: personal-finance-operations
description: "Manage household cash flow, Tiller/Sheets budget systems, subscription cancellation, payment/dispute trackers, and CPA challenge memos."
version: 1.0.0
author: Nous Research
license: MIT
metadata:
  hermes:
    tags: [finance, budgeting, cash-flow, Tiller, Google Sheets, subscriptions, tax-planning]
    related_skills: [google-workspace]
---

# Personal Finance Operations

Use this skill when the user asks for household budgeting, cash-flow control, Tiller spreadsheet analysis, subscription cuts, bill/payment structure, dispute/cancellation tracking, tax-planning research to pressure-test a CPA, or small-business working-capital/line-of-credit strategy for Lorenzo/Selva/Cosecha.

For detailed grocery lists, meal planning, store-splitting, fridge/freezer photo triage, or Target/Walmart/Aldi/Costco grocery cadence, load `household-grocery-operations` as the class-level skill and use this finance skill only for cash-flow caps and budget tradeoffs.

This skill is **not** a substitute for a licensed financial advisor, CPA, attorney, or bank authorization. It is an operating layer: analyze, structure, flag, draft, track, and prepare decisions for user approval.

## Core operating principles

1. **Be action-oriented and specific.** The user wants concrete moves, not general education. Prefer: “Cancel YouTube TV today; turn off Namecheap auto-renew; freeze nonessential cards.”
2. **Separate cash flow from P&L.** Bank transfers and credit-card payments are cash movement, not operating expenses; show them separately to avoid double-counting.
3. **Stabilize before optimizing.** In a cash crisis, prioritize freezing cards, canceling subscriptions, stopping fees/overdrafts, minimum autopay, and weekly guardrails.
4. **Do not directly execute high-risk financial actions.** Do not make bank payments, initiate disputes, cancel financial products, move money, or change autopay without explicit per-action approval in the relevant portal. Draft instructions/messages and trackers instead.
5. **Tax work is CPA-challenge support.** Research, fact-check, and present legal planning opportunities/questions to the CPA. Do not claim to be the CPA of record or provide final filing advice.

## Business working-capital / LOC strategy

When Lorenzo asks for a business line of credit, produce float, receivables financing, or short-cycle working capital:

1. Ground the need in an actual cash-conversion model or business plan before recommending a product. For Cosecha/Bey Bey, check the Cosecha V3 Pro Model and the reference file below.
2. Size the facility above the modeled core need, not exactly at it. For a $30k base float, a $75k LOC can be justified as cushion for timing variability, late payers, rejected/damaged product, overlapping orders, and growth.
3. Frame the lender story as a payables/receivables bridge tied to confirmed product movement, not as general survival cash or “money for one account.”
4. Compare options by total cost for the expected draw period, not just advertised APR: fixed loan fees on 1–3 month draws can be expensive relative to a 15-day produce cycle.
5. Always flag personal guarantee, UCC/blanket lien, annual fee, origination fee, minimum draw, repayment frequency, early payoff treatment, and whether the product reports to business credit bureaus.
6. Recommend an application order that minimizes hard pulls and underwriting noise. Prefer true bank LOC first if qualification is plausible, then institutional fintech, then expensive emergency lenders only if margin supports it.

## Standard workflow for Tiller/Google Sheets budget work

1. Load `google-workspace` if not already loaded.
2. Access the Tiller spreadsheet through the available OAuth token and Google Sheets/Drive API.
3. Inspect sheet structure first: `Transactions`, `Categories`, `Balances`, `Accounts`, `Monthly Budget`, etc.
4. Pull recent transactions and normalize fields: date, description, category, amount, account, institution, month.
5. Build/refresh operating tabs:
   - `Family Budget OS` — rules, headline findings, guardrails.
   - `Family P and L` — normalized income/outgoings; exclude transfers/CC payment mechanics.
   - `Cash Flow Analysis` — actual deposits, operating expenses, transfers in/out, raw net movement.
   - `Cut Plan` — priority cuts by controllability and monthly improvement.
   - `Subscription Audit` — active recurring charges, cancellation process, status.
   - `Managed Rules` — category map and behavioral rules.
   - `Tax Strategy OS` / `Tax Review Queue` — CPA challenge research and transaction review.
6. Verify the write by reading back key ranges and fixing formatting issues (e.g., month headers being interpreted as currency).

## Emergency budget guardrails

When the user wants to “stem the bleeding,” use austerity caps unless they specify otherwise:

- Restaurants/takeout: **$50/week max**
- Groceries: **$250/week max**
- Cash withdrawals: **$0 except true emergency**
- Nonessential shopping: **$0**
- Entertainment/media: **$0**
- Cigars/tobacco: **$0**
- Nonessential auto spend: **$0**
- Subscriptions: **$150–$250/month**, excluding true essentials like basic internet/security/Tiller
- Zelle/Venmo/wires: **$0 unless pre-approved and categorized**
- Credit-card spend: essentials only; minimum autopay on every card

Allowed without extra discussion: housing, school/childcare, utilities, insurance, groceries within cap, medical/pharmacy, minimum debt payments, gas/urgent safety, Tiller, basic internet/mobile, one home security plan if needed, and one essential work/AI tool max.

## Subscription cancellation pattern

1. Cross-reference suspected subscriptions against the **last 30 days** of transactions before prioritizing.
2. Prioritize active recurring charges over historical ones.
3. Provide each cancellation with:
   - vendor/service
   - last charge date and amount
   - link
   - exact unsubscribe steps
   - email/support message if no portal cancel button
   - keep/cancel recommendation
4. Maintain a tracker with status: `TO CANCEL`, `TRYING TO CANCEL`, `CANCELED`, `VERIFY NEXT MONTH`, `DISPUTE/REVIEW`.
5. Common high-priority categories: Apple/App Store, Namecheap auto-renewals, YouTube TV, Adobe, Care.com, Instantly, Canva, Halo Live, Bubbi, SimpliSafe/Ring duplication, Xfinity/Comcast, MMI/unknown high charges.

## Card freeze/payment structure guidance

For fast spending control, recommend:

1. Keep one operating checking/debit and one primary card active for essentials.
2. Freeze/lock all other cards through issuer apps.
3. Do not close cards by default; freezing is reversible and avoids credit-score disruption.
4. Before freezing, identify essential autopays: mortgage/housing, insurance, utilities, school/childcare, phone/internet, minimum debt payments.
5. Move only essentials to the operating card/account. Let nonessential subscriptions fail or force review.

## CPA challenge / legal tax planning workflow

The user wants a proactive research layer to keep the CPA rigorous. Present material as “questions/opportunities for CPA approval,” not final advice.

Research should be grounded in official sources when possible:

- IRS small business/self-employed hub
- IRS business expense resources and Publications 334, 463, 535, 587, 946, 969
- IRS QBI / Form 8995 guidance
- IRS retirement plans for self-employed people
- IRS business credits / R&D credit resources
- Florida Department of Revenue: sales tax, reemployment tax, corporate tax
- Florida Sunbiz/entity compliance

CPA challenge memos should include:

1. Opportunity/issue in plain English.
2. Why it may apply to the user/business.
3. Official authority/source link.
4. Exact questions the CPA must answer.
5. Documents to gather.
6. Red flags and what not to claim without substantiation.

Common CPA challenge topics:

- entity structure and S-corp timing
- reasonable salary vs distributions
- QBI deduction
- accountable plan/reimbursements
- home office
- mileage/auto method
- business meals/travel documentation
- software/AI subscriptions and mixed-use allocation
- startup/organizational costs
- inventory, COGS, spoilage, samples, promotional product
- Florida sales/use tax and resale certificates
- estimated tax safe harbor
- retirement plan and HSA planning

## Pitfalls

- Do not call credit-card payments “expenses” in P&L; classify separately.
- Do not suggest tax deductions that lack documentation or business purpose.
- Do not bury personal meals/shopping as business expenses.
- Do not recommend spending money solely for a tax deduction.
- Do not automate or execute bank payments/disputes/cancellations without explicit approval and proper portal access.
- Do not recommend a LOC from advertised rate alone; calculate/compare cost over the actual expected draw period and disclose PG/UCC/fee traps.
- If a user asks for personal Gmail drafts but no personal Gmail token exists, state the limitation and provide copy/paste drafts or setup path.

## Reference files

- `references/lorenzo-tiller-finance-os.md` — session-specific details for Lorenzo’s Tiller workbook, created tabs, current guardrails, subscription findings, and CPA-challenge cadence.
- `references/business-working-capital-loc.md` — Selva/Cosecha/Bey Bey produce-float LOC sizing, lender ranking, application order, lender positioning, and May 2026 term notes.
