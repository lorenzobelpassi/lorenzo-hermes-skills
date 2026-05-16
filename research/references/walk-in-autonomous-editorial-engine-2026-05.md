# The Walk-In Autonomous Editorial Engine — May 2026

Session learning for future Selva/The Walk-In work.

## Current architecture

The Walk-In / Staff Meal should not run as isolated newsletter jobs that repeat the same research as Selva agents. Use a shared-intelligence pattern:

1. Existing upstream agents gather operational intelligence:
   - Selva Restaurant Intel Scraper
   - Selva Market Briefs
   - Selva Brokerage Daily Intel
2. A daily Shared Lead Bank dedupes and routes the intelligence into buckets:
   - Publication angles for The Walk-In
   - Staff Meal leads
   - Selva/Cosecha sales signals
   - Product + seasonality signals
   - Duplicate/already-covered items
   - Source notes + verification queue
3. Tuesday and Friday editorial jobs consume the shared bank first, then do fresh web research only for verification or high-value gaps.

## Cron jobs created

- Shared Daily Lead Bank: `01bbe0f0b464`, daily 7:15am ET, local delivery, consumes context from existing Selva intel jobs.
- The Walk-In Tuesday draft: `37a836d9eddb`, Tuesday 8am ET, origin delivery, now uses the Shared Daily Lead Bank via `context_from`.
- Staff Meal Friday draft: `c9958c5d8839`, Friday 8am ET, origin delivery, now uses the Shared Daily Lead Bank via `context_from`.
- Staff Meal review database reminder: `20ec9a170af6`, Sunday 5pm ET, origin delivery.

## Review database

A private first-person review database was started at:

`/Users/lorenzobelpassi/thewalkin305/review-database/`

Files:
- `README.md` — purpose/fields/guardrails.
- `interview-template.md` — questions for restaurant visits.
- `workflow.md` — conversion from interview to Staff Meal sections.
- `reviews.json` — structured review records.

Use this database to capture Lorenzo's actual restaurant experiences and generate credible Staff Meal content. First-person notes beat generic web summaries. Mark unverified facts and whether Lorenzo personally tried each dish.

## First captured review

Ariete/Arriette Coconut Grove visit, beginning of May 2026:
- Private wine-room/tasting-menu setting with friends, wife, and group owners.
- Best dish named: Cuban-style ceviche; liked oysters and braised beef.
- Core Staff Meal angle: a kitchen pursuing a Miami food identity with real gumption, without leaning on easy tropical/fruit seasonality.
- Verify spelling `Ariete` vs `Arriette`, chef name, exact dish names, exact wine/sweet-wine reference, and public availability of wine room/private seating before publishing.

## Substack setup caveat

Substack login links/codes authenticate the browser or app where they are opened. If Lorenzo clicks the login email in the iPhone app or his local browser, the remote Browserbase session remains signed out. Do not repeatedly ask for the email if already known; use `lorenzo.belpassi@selva-partners.com` for The Walk-In Substack unless corrected.

Best options:
1. Ask Lorenzo to copy the temporary Substack sign-in link itself and paste it into chat so the remote browser can open it; or
2. Walk him click-by-click in his authenticated local/iPhone session and provide prepared copy to paste.

Avoid posting live verification codes into group chats/Discord threads. They are temporary but still account-login credentials.

## Operating principle

The Walk-In should become a public editorial layer on top of Selva intelligence, not another independent research silo. Public editorial angles and internal Selva/Cosecha sales signals must remain separated, with no automated outreach or publishing without Lorenzo approval.
