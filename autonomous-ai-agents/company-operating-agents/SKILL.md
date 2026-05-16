---
name: company-operating-agents
description: "Design company-managing agents: source of truth, intake, operating loops, authority levels, relationship risk, and daily operating briefs."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [agents, operations, business-os, strategy, selva]
    related_skills: [notion, google-workspace, email_drafter, selva-deal-log-agent]
---

# Company Operating Agents

## When to Use

Use this skill when the user asks to design, launch, explain, or operationalize an agent that manages a business across sales, buying, operations, logistics, client relationships, product/inventory, or learning loops.

This is for **company operating systems**, not single-purpose chatbots.

## Core Principle

Do not frame the agent as a job-title replacement. Frame it as a process manager of cause and effect:

```text
What happened?
→ Why does it matter?
→ What should happen next?
→ Can the agent handle it?
→ Does it need supervision?
→ What did we learn?
```

Plain thesis:

> The agent watches the business, decides what matters, helps act on it, and learns from what keeps happening.

Value definition:

```text
Value = Business Impact / Agent Attention
```

Plain version:

> Value is the business impact created when an agent notices what matters and helps the company respond correctly.

## Preferred Style for This User

- Keep language simple, direct, and operational.
- Avoid abstract consulting language unless immediately translated into plain English.
- Prefer concrete business examples over theory.
- Use Selva examples when relevant: buyer follow-up, supplier pricing, delivery delays, produce quality, walk-in fridge layout, perishability, logistics, relationship risk.
- Emphasize practical next actions, not analysis alone.

## Architecture Pattern

Build a complete operating agent with these layers:

```text
Business Brain / Source of Truth
↓
Intake Layer
↓
Operating Loops
↓
Decision Rules / Authority Levels
↓
Relationship Risk System
↓
Daily Operating Brief
↓
Learning Loop
```

### 1. Business Brain / Source of Truth

Define where the company lives. For Selva, the default is Notion.

Common entities:
- Accounts / Buyers
- Contacts
- Products
- Suppliers
- Prices
- Quotes
- Orders
- Inventory
- Deliveries
- Issues
- Follow-ups
- Relationship Risk
- Lessons Learned
- Daily Operating Briefs

### 2. Intake Layer

Identify what the agent watches:
- email
- WhatsApp/text/manual notes
- call transcripts / Plaud notes
- supplier lists
- price sheets
- order notes
- delivery notes
- inventory/fridge notes
- client complaints or tone changes

### 3. Operating Loops

Design around connected loops, not departments:

1. Buyer / Sales Loop
2. Product / Market Loop
3. Buying / Supplier Loop
4. Order / Operations Loop
5. Inventory / Fridge Loop
6. Logistics / Delivery Loop
7. Learning / Process Improvement Loop

For each loop, define:
- what the agent watches
- why it matters
- what the agent can do
- what needs supervision
- what should be learned

### 4. Authority Levels

Classify actions clearly:

**Level A — Agent Can Do Alone**
- log notes
- update CRM/source of truth
- create follow-up
- compare supplier prices
- draft quote
- summarize account
- flag reorder opportunity
- create inventory reminder

**Level B — Agent Can Draft, Needs Approval**
- frustrated-client response
- complaint response
- important buyer follow-up
- sensitive pricing change
- credit/discount suggestion
- supplier switch recommendation
- relationship-sensitive delivery change

**Level C — Agent Must Stop and Escalate**
- client threatens to leave
- trust/reputation risk
- legal/payment dispute
- major account upset
- serious quality failure
- large credit decision
- strategic partnership or irreversible decision

### 5. Relationship Risk System

Use these levels:

- Level 1 — Normal: routine; agent can handle.
- Level 2 — Small Friction: minor confusion/delay; agent may draft/send if routine.
- Level 3 — Relationship Risk: frustration, repeated issue, disappointment, confusion, reduced trust. Agent drafts only; requires supervision.
- Level 4 — Trust Problem: client questions reliability or expresses real dissatisfaction. Agent prepares full context and recommends a call.
- Level 5 — Major Decision / Strategic Risk: money, legal, reputation, strategic account, or long-term relationship impact. Agent stops and briefs.

Level 3 rule:

```text
Soft + Solution-Oriented + Supervised
```

Formula:

```text
Acknowledge → Own → Offer Solution → Ask Preference → Track
```

Permanent instruction:

> If an issue reaches Level 3 Relationship Risk, the agent must include at least one practical solution or next step in the draft response. The solution should reduce the chance of the same issue happening again.

### 6. Daily Operating Brief

The main daily output should be one clear brief, not scattered dashboards.

Use exactly these sections:

```text
1. What Happened
2. Why It Matters
3. What the Agent Can Do
4. What Needs Supervision
5. What We Learned
```

This format should connect sales, buying, operations, logistics, and relationships in one view.

## Physical Operations / Cause-and-Effect Examples

Agents must understand physical processes when they affect business outcomes. Example for produce distribution:

```text
bad fridge layout → slower picking → lower freshness → late packing → unhappy buyer → relationship risk
```

Fridge/intake logic should consider:
- perishability
- temperature sensitivity
- ethylene sensitivity
- FIFO
- picking speed
- product quality
- spoilage risk
- customer-facing risk

## Sales / BD-First Variant

When the company-agent is for a retained sales/BD engagement, make the first operating system a revenue cockpit, not a general operations dashboard. Optimize around:

- highest-probability buyers
- recurring revenue potential
- next outreach/follow-up
- proposal/sample/meeting conversion
- commission or upside economics
- hours used vs retained monthly scope

For food businesses, include **direct-to-consumer** as a first-class loop when relevant, alongside B2B and partnerships:

```text
B2B sales
+ BD partnerships
+ direct-to-consumer campaigns
```

The weekly brief should answer: who to contact, what to say, why now, estimated revenue, upside/commission, and what needs approval.

See `references/fullfilled-foods-sales-bd-notes.md` for a concrete FullFilled Foods example.

## Build Sequence

Do not overbuild. Build in phases:

1. Business Brain
2. Capture Agent
3. Daily Operating Brief
4. Buyer Follow-Up / Sales Loop
5. Buying + Product Intelligence
6. Operations + Inventory
7. Logistics + Relationship Risk
8. Learning Loop

First launch loop should usually include:

```text
Buyer requests
+ supplier/product availability
+ order/delivery issues
+ relationship risk
+ daily action brief
```

## Prototype 001 / Operating Intelligence Build Pattern

When the user wants to build the first version of a company intelligence OS, prove the operating loop with local files before over-automating APIs:

```text
messy input → parsed signals → bad-data / confidence notes → daily brief → weekly management report → relationship risk → efficiency recommendations
```

For Phase 002 pricing infrastructure, treat pricing as a live operating layer, not a spreadsheet side quest. Use **Growers Price List** as the business-facing term; keep old supplier/price-list code flags as compatibility aliases only. Build a central SKU pricing matrix that ingests Growers + Cosecha price lists, normalizes case/pack prices to unit economics, applies COGS and wastage margins, then generates client-facing tier price lists.

Default Selva tier margins: Conference 48%, League 2 42%, League 1 38%, Championship 35%, Premier League 28%. Treat these as gross margins unless Lorenzo explicitly says markup. See `references/selva-pricing-matrix-phase-002.md` for the sheet tabs, formulas, CLI rename pattern, and verification checklist.

A good first implementation should produce Markdown for management consumption and JSON/CSV for later Notion/CRM import. Include tests for every layer and a full CLI run.

For Selva Intelligence OS specifically, keep these permanent requirements:

- Product name: **Selva Intelligence OS**.
- Prototype name: **Prototype 001**.
- Category: **Company Intelligence OS** / **Operating Intelligence Infrastructure**.
- Weekly/monthly reports follow Natoora-style management reporting: numbers + commentary + cause/effect + operational issue + next action.
- Bad, incomplete, duplicated, or conflicting data is part of the product, not an afterthought.
- Efficiency layer always asks: **“Can this be more efficient and better?”**
- Relationship-sensitive Level 3+ issues are draft-only and require Lorenzo approval.

See `references/selva-intelligence-os-prototype-001-build.md` for the concrete first-build pattern, output files, CLI shape, report sections, and pitfalls discovered while implementing Prototype 001.

## Pitfalls

- Do not build “one giant chatbot.” Build an operating system with structured data, loops, authority levels, and daily outputs.
- Do not organize only by job roles such as sales/ops/finance/logistics; show how actions affect each other.
- Do not stop at apology in relationship-risk moments; offer a practical solution.
- Do not let the agent send Level 3+ relationship-risk responses unsupervised.
- Do not describe dashboards without actions; every brief should say what should happen next.
- Do not let PDF/text parsing pretend to be exact structured data. Treat it as directional intelligence until order/sales exports, price lists, product files, and notes are connected.
- Do not turn every sales-commentary sentence into an efficiency recommendation. Deduplicate and only recommend process changes when there is operational friction, lost sales, margin leakage, shortages, logistics delay, service issue, or relationship risk.

## References

- `references/cosecha-business-plan-framing.md` — Cosecha-specific business-plan framing: Selva Partners hierarchy, Zero-to-One posture, sourcing/distribution value system, and plan spine.
- `references/cosecha-v3-source-of-truth.md` — current-doc source order for Cosecha v3, confirmed workbook metrics, and Deborah-facing translation rules.
- `references/selva-prototype-001.md` — session-specific blueprint for Selva Operating Agent as Prototype 001.
- `references/fullfilled-sales-bd-os.md` — FullFilled Foods Sales/BD operating system: 20-hour monthly plan, Tuesday Drop offer, white-label wellness, luxury hospitality targets, CRM IDs, and email/signature rules.
- `references/fullfilled-sales-bd-os.md` — FullFilled Foods sales/BD operating system: 20-hour monthly sales wing, Tuesday Drop DTC offer, white-label wellness, company sampling, CRM/mass outreach workflow, and Natoora-network synergy guardrails.
- `references/selva-intelligence-os-prototype-001-build.md` — concrete build notes for Selva Intelligence OS Prototype 001: CLI shape, output files, Natoora-style reporting sections, relationship-risk rules, efficiency layer pitfalls, and next-phase data requirements.
- `references/selva-pricing-matrix-phase-002.md` — Phase 002 pricing matrix layer: Growers Price List terminology, Google Sheets tab structure, unit/case pricing formulas, tier margins, CLI rename pattern, and verification checklist.
- `references/fullfilled-foods-sales-bd.md` — session-specific blueprint for applying the operating-agent pattern to FullFilled Foods sales, BD, DTC, white-label wellness menus, family Tuesday Drops, and company sampling.
- `references/fullfilled-foods-sales-bd-notes.md` — FullFilled Foods sales/BD operating notes: retainer/commission context, DTC + luxury fulfillment channels, Natoora-network synergy, starter targets, and outreach angles.
