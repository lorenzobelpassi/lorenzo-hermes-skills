# Notion Deals Database — Schema for Agent 3 (Prospecting)

This is the contract between Agent 1 (deal capture) and Agent 3 (follow-up).
Agent 3 follows up on **outbound prospecting** to Miami restaurants, so the
schema is built around the prospect lifecycle (cold → warm → hot), not deal
negotiation.

## Required properties

| Property name        | Type        | Notes                                                          |
|----------------------|-------------|----------------------------------------------------------------|
| Contact Name         | Title       | Chef name. e.g. "Diego Reyes"                                  |
| Company              | Rich text   | Restaurant name. e.g. "Casa Tua"                               |
| Contact Email        | Email       | Required for Gmail drafts. Optional for DM/text channels.      |
| Neighborhood         | Select      | Miami Beach, Brickell, Design District, Coral Gables, etc.     |
| Tier                 | Select      | 🔥 HOT, 🟡 WARM, 🔵 COLD                                       |
| Status               | Select      | Open, In Progress, Closed, Lost, Nurture                       |
| Touch Count          | Number      | How many touches so far. Increment after each outreach.        |
| Last Touch Type      | Select      | email, instagram_dm, text, in-person, sample-drop, tasting, call |
| Last Contact Date    | Date        | Drives the `days_since_last_touch` calculation                 |
| Next Action Date     | Date        | **THIS DRIVES THE QUERY.** When should the agent remind you?   |
| Commodity            | Rich text   | What you're pitching. e.g. "Sungold tomatoes from Veracruz"    |
| Last Note            | Rich text   | What happened last touch. e.g. "Dropped sample with sous chef" |
| Intel                | Rich text   | Background — chef bio, current suppliers, menu refs, etc.      |

## Optional properties

| Property name        | Type        | Notes                                                          |
|----------------------|-------------|----------------------------------------------------------------|
| Gmail Thread ID      | Rich text   | If set, replies in the existing thread instead of creating new |

## Status semantics

- **Open** — initial outreach, no commitment yet
- **In Progress** — actively being worked, in pipeline
- **Closed** — converted to account, do not include in follow-ups
- **Lost** — dead, do not include in follow-ups
- **Nurture** — moved to quarterly nurture list, do not include in daily follow-ups

The Notion query filters for `Status not in (Closed, Lost, Nurture)`.

## Tier semantics (matches your prospecting-system.md)

- **🔥 HOT** — < 2 weeks to close. Tasting done, asked for pricing, referred. Daily follow-up.
- **🟡 WARM** — 2-6 weeks. Knows Selva, had conversation, follows on social. Weekly touch.
- **🔵 COLD** — Identified target, no relationship yet. 2-3 touches before moving up or to nurture.

## Why these specific fields matter for the prompt

The agent picks an outreach pattern based on:
- `tier` — sets the urgency and template family
- `touch_count` — at 6+ with no engagement, the agent suggests SKIP / move to nurture
- `last_touch_type` — a follow-up to an in-person drop-off reads differently than a follow-up to a cold email
- `days_since_last_touch` — at >14 days the agent shifts to a re-engagement angle (new product, market intel)
- `intel` — gives the agent specifics to reference; without it, the message will be generic

If `intel` is empty, expect generic outputs. The richer this field, the better the drafts.

## Suggested Notion view: "Today"

Filter: `Next Action Date == Today` AND `Status not in (Closed, Lost, Nurture)`
Sort: `Last Contact Date` ascending (most stale on top)
Group by: `Tier`

This is the same query Agent 3 runs.
