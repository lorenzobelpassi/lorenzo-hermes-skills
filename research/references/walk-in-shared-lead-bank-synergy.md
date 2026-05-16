# The Walk-In Shared Daily Lead Bank / Cross-Agent Synergy

Session date: 2026-05-09

## Why this exists

Lorenzo identified that Selva/The Walk-In jobs were at risk of duplicating effort: multiple agents independently researching the same Miami openings, restaurant signals, product movement, and market data. The correction was to make the system behave like a shared intelligence desk rather than isolated bloggers/briefing agents.

## Pattern

Create one daily routing/deduplication job that consumes recent outputs from upstream intelligence jobs, then inject that shared lead bank into downstream editorial/sales jobs.

### Daily shared lead bank

- Job name: `The Walk-In Shared Daily Lead Bank`
- Job ID: `01bbe0f0b464`
- Schedule: daily at 7:15 AM ET
- Delivery: local/internal
- Input context from existing jobs:
  - Selva Restaurant Intel Scraper
  - Selva Brokerage Daily Intel
  - Selva Market Briefs
- Purpose: dedupe signals, split public-safe editorial angles from internal sales/outreach signals, and produce one reusable intelligence bank.

### Downstream consumers

- `The Walk-In Tuesday draft` now consumes the Shared Daily Lead Bank first.
- `Staff Meal Friday draft` now consumes the Shared Daily Lead Bank first.
- Fresh web searches should be limited to verification or important gaps, not broad repeated discovery.

## Output shape for shared bank

Use this structure:

```md
# Shared Daily Lead Bank — YYYY-MM-DD

## Executive Routing
- Top 5 items Lorenzo should care about today.

## Publication Angles for The Walk-In
For each item: angle, why it matters, confidence, source/verification, suggested section (On The Shelf / Market Heat / On The Line / 86’d / Where To Sit / Staff Meal).

## Staff Meal Leads
For each item: restaurant/dish/room lead if available, what to verify, possible sections (The Order / The Seat / The Tell / The Skip / The Receipt).

## Selva/Cosecha Sales Signals
For each item: account/product angle, urgency, suggested action, CRM-ready fields, and whether it is public-safe or internal-only.

## Product + Seasonality Signals
Named products/varieties/origins only when verified. Separate verified from hypotheses.

## Duplicate/Already-Covered Items
List items that should not be researched again unless new info appears.

## Source Notes + Verification Queue
Links or clear source references. Include what a human should verify before publishing/sending.
```

## Rules

- Use injected/shared context before doing new web research.
- Deduplicate aggressively; merge repeated mentions into one signal with source notes.
- Keep public editorial material separate from internal Selva/Cosecha sales/outreach material.
- Do not publish or send outreach automatically.
- Label uncertain items as `verify_before_publish` or `verify_before_outreach`.
- Track when a lead has been consumed by The Walk-In, Staff Meal, or Selva sales workflows to avoid repeats.

## Future upgrade

Move from ephemeral cron context to a persistent signal database with fields such as:

- `signal_id`
- `title`
- `entity` / `restaurant` / `product`
- `source_urls`
- `confidence`
- `public_safe`
- `internal_only`
- `status`: `new`, `verified`, `used_in_walk_in`, `used_in_staff_meal`, `converted_to_selva_signal`, `needs_human_verification`, `dead`
- `last_seen_at`
- `consumed_by_jobs`
