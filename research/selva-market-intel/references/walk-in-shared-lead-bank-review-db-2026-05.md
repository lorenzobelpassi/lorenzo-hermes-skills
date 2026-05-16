# The Walk-In Shared Lead Bank + Staff Meal Review Database (May 2026)

Session learning: The Walk-In should not operate as a separate blogger-like workflow. It should reuse existing Selva/Market/Restaurant/Brokerage intelligence and Lorenzo's first-person dining notes so the agents do not duplicate searches or produce generic food content.

## Shared intelligence architecture

A daily shared lead bank was added to dedupe and route intelligence across Selva/Cosecha and The Walk-In/Staff Meal.

- Job name: `The Walk-In Shared Daily Lead Bank`
- Job ID: `01bbe0f0b464`
- Schedule: daily 7:15 AM ET
- Delivery: local/internal
- Purpose: absorb recent outputs from Selva Restaurant Intel, Selva Brokerage Daily Intel, and Selva Market Briefs, then produce one reusable bank for downstream editorial and sales jobs.

Downstream jobs updated to consume the shared lead bank first:

- `The Walk-In Tuesday draft` — job ID `37a836d9eddb`
- `Staff Meal Friday draft` — job ID `c9958c5d8839`

## Operating rule

Before doing fresh web research for The Walk-In or Staff Meal, check/reuse the shared lead bank and explicitly dedupe against already-covered items. Fresh search is for verification or important gaps, not broad repeat discovery.

## Shared lead bank output buckets

- Executive Routing — top items Lorenzo should care about.
- Publication Angles for The Walk-In — angle, why it matters, confidence, source/verification, suggested section.
- Staff Meal Leads — restaurant/dish/room leads, verification needed, possible Staff Meal section.
- Selva/Cosecha Sales Signals — account/product angle, urgency, suggested action, CRM-ready fields, public-safe vs internal-only.
- Product + Seasonality Signals — verified products/varieties/origins separated from hypotheses.
- Duplicate/Already-Covered Items — items not to research again without new info.
- Source Notes + Verification Queue — links and human verification tasks.

## Public/private separation

The same signal can be useful in two different ways:

- Public editorial: Miami food identity, seasonality, openings, room reads, dishes, what to order/skip.
- Internal sales: account/product angles, buyer/opportunity signals, sample/quote/follow-up actions.

Never leak internal sales context or raw competitive data into public newsletter copy. Mark ambiguous items as `public-safe`, `internal-only`, or `verify_before_publish`.

## Staff Meal first-person review database

Created local source-of-truth at:

`/Users/lorenzobelpassi/thewalkin305/review-database/`

Files:

- `README.md` — schema, guardrails, purpose.
- `interview-template.md` — interview questions for Lorenzo after restaurant visits.
- `workflow.md` — converts interview notes into Staff Meal sections.
- `reviews.json` — structured database.

Weekly reminder job:

- Job name: `Staff Meal review database reminder`
- Job ID: `20ec9a170af6`
- Schedule: Sundays 5:00 PM ET

## Interview workflow

When Lorenzo says he visited a restaurant, immediately capture the raw memory, ask targeted follow-ups, and store a structured source note. Core fields:

- restaurant name + neighborhood
- visit date/period
- who he went with
- seat/room
- dishes ordered
- best dish
- skip/underperformer
- product/kitchen tell
- wine/drink/service/room read
- whether he would return
- public-safe / needs verification

Convert into Staff Meal sections:

- The Order
- The Seat
- The Tell
- The Skip
- The Receipt

## Example first entry: Ariete/Arriette

Lorenzo described a beginning-of-May private tasting-menu visit in Coconut Grove, likely Ariete (verify spelling). Key angle: a kitchen pursuing a Miami identity with conviction, not relying on easy tropical/fruit seasonality. Strong lead for Staff Meal, but verify exact restaurant spelling, chef name, dish names, wine references, and whether the private wine-room seating is public/bookable.

## Substack login pitfall

When setting up The Walk-In on Substack, do not repeatedly ask Lorenzo for the login email if it is already known. Use `lorenzo.belpassi@selva-partners.com` for Substack magic-link login unless he corrects it. If the remote browser is unauthenticated, trigger the magic link, then wait for Lorenzo to click it and say `done`. Do not publish without explicit approval.
