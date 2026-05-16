# The Walk-In / Staff Meal Substack + Editorial System (2026-05-08)

## Brand architecture

- Parent publication: **The Walk-In**
- Tagline: **Cold storage for hot Miami food intel.**
- Tuesday issue: **The Walk-In** — seasonality, openings, market/product signals, chef/operator intel.
- Friday column: **Staff Meal**
- Staff Meal tagline: **What to order when you know the kitchen.**

## Positioning

The project should compete with Miami restaurant guides/listicles by being more seasonal, specific, product-literate, and chef/operator-aware. Do **not** make the competitive target too obvious publicly; readers should infer the critique.

Internal positioning:
- Staff Meal is a sharper Miami restaurant guide for readers who can tell when coverage is generic or press-release-driven.
- The enemy is vagueness, listicle logic, room/design worship, and lazy restaurant hype — not a public media beef.

Public voice:
- Specific, funny, insider, precise.
- Let the critique sit in the details; avoid naming competitors casually.
- Good line style: “The room is doing a lot. The crudo is doing more.”
- Avoid sounding bitter or like a roast page.
- Punch at bad review culture, not small operators trying hard.

## Staff Meal recurring sections

Use subtle edge:
- **The Order** — what to get.
- **The Skip** — what not to waste money on.
- **The Seat** — where/when to sit.
- **The Tell** — one product/technique/detail proving whether the kitchen is serious.
- **Opening Temperature** — read of new openings without PR tone.
- **Market Tells** — seasonal/product tie-in from The Walk-In.
- **The Receipt** — concise verdict.

Example structure:

```md
## Staff Meal: [Restaurant]

**The order:** grilled snapper, citrus salad, martini at the bar.  
**The seat:** early, before the room starts performing.  
**The tell:** the herbs are not decorative. Someone is tasting as they plate.  
**The skip:** the “for the table” appetizer that looks better than it eats.  
**The receipt:** go now, but order narrow.
```

## Visual direction

User wants a **Wynwood Walls / Miami street-art / RENZLOVESPASTA_305** vibe, not clean magazine stock photography.

Visual language:
- flash-lit food
- Wynwood graffiti/street-art textures
- handwritten kitchen tickets, stickers, marker tags
- tropical color, concrete, tile, stainless steel
- late-night Miami, back-alley restaurant exterior, punky chef energy
- no readable text/logos; no identifiable faces

OpenAI image prompt base:

```text
Flash-lit Miami restaurant dish photographed against a Wynwood street-art wall, torn sticker textures, chef towel, handwritten kitchen ticket with unreadable marks, tropical color accents, gritty premium editorial food zine aesthetic, imperfect plating, warm late-night shadows, high contrast, no readable text, no logos, no identifiable faces.
```

Staff Meal prompt:

```text
Flash-lit Miami restaurant staff meal scene against a Wynwood-style graffiti wall, imperfect plate of pasta or grilled seafood, chef towel, kitchen ticket, sauce stains, tropical colors, street-art textures, punky editorial food zine aesthetic, gritty premium, late-night after-service mood, no readable text, no logos, no identifiable faces.
```

The Walk-In remains colder/market-side; Staff Meal is warmer, street-art, after-service, recommendation-oriented.

## Substack API finding

Official Substack Developer API docs (support article `45099095296916-Substack-Developer-API`, updated 2026-04-21) show the API is **not a CMS/publishing API**.

Current official endpoint described:

```bash
GET https://substack.com/profile/search/linkedin/{linkedin-handle}
```

Purpose: retrieve public profile data for verified Substack creators linked to LinkedIn handles. Response may include Substack handle, profile URL, leaderboard status, bestseller tier, rough free subscriber count, and follower count.

Limitations:
- No post creation/draft endpoint documented.
- No publish endpoint documented.
- No image upload endpoint documented.
- No subscriber/analytics management documented.

Access path:
1. Create/login to Substack.
2. Agree to API Terms of Use.
3. Submit access form.
4. Wait 7–10 business days.
5. If approved, enable Developer API in account settings and create token.

Launch implication: treat Substack as a manual CMS for now. Generate Substack-ready markdown, subject line, preview text, OpenAI cover image/prompt, and social captions; user pastes/publishes manually unless Substack later exposes publish/draft API.

## Substack setup copy

Publication name: **The Walk-In**

Tagline: **Cold storage for hot Miami food intel.**

About/description:

```text
The Walk-In tracks what’s moving through Miami food before it hits the menu — seasonal product, restaurant openings, chef/operator signals, and the dishes worth paying attention to.
```

Friday column:

```text
Staff Meal
What to order when you know the kitchen.
```
