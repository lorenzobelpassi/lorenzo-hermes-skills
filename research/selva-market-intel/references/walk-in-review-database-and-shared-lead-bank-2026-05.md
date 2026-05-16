# The Walk-In Shared Lead Bank + Review Database (May 2026)

## Why this exists

Lorenzo identified two operating problems:

1. The Walk-In / Staff Meal needs first-person taste, not only web research.
2. Multiple agents were at risk of repeating the same Miami openings/product/restaurant searches.

The solution is a shared intelligence layer plus a first-person review database.

## Shared Daily Lead Bank

Created Hermes cron job:

- Name: `The Walk-In Shared Daily Lead Bank`
- Job ID: `01bbe0f0b464`
- Schedule: daily at 7:15 AM ET
- Delivery: `local`
- Toolsets: `web`, `file`, `terminal`
- Context sources when created: Selva Restaurant Intel, Selva Brokerage Daily Intel, Selva Market Brief jobs.

Purpose:

- Deduplicate existing Market Intel, Restaurant Intel, brokerage intel, and current web checks.
- Split leads into publication angles, Staff Meal leads, Selva/Cosecha sales signals, product/seasonality signals, duplicate/already-covered items, and verification queue.
- Keep public editorial material separate from internal sales/outreach material.
- Avoid fresh web research unless needed to verify or fill high-value gaps.

Downstream jobs updated to consume this lead bank via `context_from=["01bbe0f0b464"]`:

- `37a836d9eddb` — The Walk-In Tuesday draft
- `c9958c5d8839` — Staff Meal Friday draft

Prompt principle for downstream jobs:

> Use the Shared Daily Lead Bank first. Do not repeat broad searches already covered by the lead bank unless verifying a specific high-value fact. Deduplicate leads. Advance covered items into angles rather than researching them again.

## Review database

Created local review database folder:

`/Users/lorenzobelpassi/thewalkin305/review-database/`

Files:

- `README.md` — purpose, core fields, guardrails.
- `interview-template.md` — structured interview questions.
- `workflow.md` — review-to-content workflow and status labels.
- `reviews.json` — structured database starter.

Weekly interview reminder cron:

- Name: `Staff Meal review database reminder`
- Job ID: `20ec9a170af6`
- Schedule: Sundays at 5:00 PM ET
- Purpose: ask Lorenzo for 1–3 restaurants he personally visited and interview him into structured Staff Meal source notes.

## First captured review

Lorenzo described a private tasting-menu visit to “Arriette” in Coconut Grove in early May with friends, his wife, and owners of the group. Important: verify exact restaurant spelling before public use; likely `Ariete`.

Saved notes:

- JSON entry ID: `arriette-coconut-grove-2026-05-private-tasting`
- Markdown note: `/Users/lorenzobelpassi/thewalkin305/review-database/arriette-coconut-grove-2026-05.md`

Extracted Staff Meal angle:

- The real tell was not simply the tasting menu; it was the kitchen’s care/devotion in pursuing a Miami identity with gumption, without leaning on easy tropical/fruit-seasonality cues.
- Best named dish so far: Cuban-style ceviche.
- Also liked: oysters and braised beef.
- Strong wine/pairing read: impressed by wine selection, California reds, tequila, sake, and a French sweet wine/Sauternes-style pairing (verify exact reference).
- Return intent: yes, specifically to try the à la carte menu.

Follow-up questions still needed:

1. Confirm spelling: Ariete vs Arriette.
2. Exact ceviche details and what made it Cuban-style.
3. Which dishes had more complexity.
4. Oyster preparation.
5. Braised beef details.
6. Whether anything underperformed.
7. Whether wine room/private seating is publicly bookable.
8. Strongest pairing.
9. What he wants to order à la carte next.
10. Verdict framing: worth going / worth going if ordering right / important but not casual.

## Operating guardrails

- First-person Lorenzo experience beats web research for Staff Meal.
- Mark anything not personally tried as `not_personally_tried` or `lead_only`.
- Public copy should be sharp but not defamatory or reckless.
- Avoid direct Infatuation callouts; make the critique legible through specificity.
- Do not publish or send outreach automatically.
- Internal sales/account angles and public editorial angles must remain separated until Lorenzo approves.
