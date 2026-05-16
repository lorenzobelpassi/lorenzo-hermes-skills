# The Walk-In / Staff Meal — Substack + Editorial Notes

Session-derived operating notes for building Lorenzo's Miami food publication on Substack.

## Brand architecture

- Parent publication: **The Walk-In**
- Tagline: **Cold storage for hot Miami food intel.**
- Tuesday issue: seasonality, openings, product/market intel, chef/operator signals.
- Friday column: **Staff Meal**
- Staff Meal tagline: **What to order when you know the kitchen.**

## Positioning

Staff Meal should compete with Miami restaurant-guide/listicle culture without naming competitors too directly. The reader should infer the critique.

Avoid overt lines like:
- "anti-Infatuation"
- "better than Infatuation"
- constant direct competitor callouts

Use subtle positioning instead:
- more seasonal
- more product-literate
- more specific about what to order/skip
- less impressed by room design than what is on the plate
- chef/operator insider voice

Public stance: **Miami restaurant intel for people who can taste the difference.**

## Voice rules

- Be sharp, funny, and specific, not bitter.
- Punch at vague review culture, not at individual writers.
- Prefer implication over explanation; trust the readership to pick up the critique.
- Tie restaurant judgment to seasonality, sourcing, product quality, and execution.
- Use recurring coded tells: herbs, acidity, fish cutting, vegetables, bread, market products.

Example tone:
> The room is doing a lot. The crudo is doing more.

> Go for the salad only if the peaches are still on the menu. Otherwise, sit at the bar and order the shrimp.

## Staff Meal recurring sections

- **The Order** — what to get.
- **The Skip** — what not to waste money on.
- **The Seat** — where/when to sit.
- **The Tell** — the one detail proving whether the kitchen is serious.
- **Opening Temperature** — new opening read without PR fluff.
- **Market Tells** — seasonal/product tie-in from The Walk-In.
- **The Receipt** — concise final verdict.

## Visual direction

Lorenzo wants a Wynwood Walls / Miami street-art visual system, inspired by the feel of @renzlovespasta_305: restaurant discovery, tropical Miami, food close-ups, storefronts, personal/candid rather than polished stock.

### The Walk-In visuals
Cold, back-of-house, product-intel:
- walk-in cooler
- stainless shelves
- condensation
- produce crates
- handwritten chef labels
- cool blue-green light
- tropical color accents
- street-art texture as editorial overlay

### Staff Meal visuals
Warmer, late-night, guide/recommendation:
- flash-lit dish
- Wynwood graffiti wall texture
- torn sticker textures
- kitchen tickets with unreadable marks
- chef towel
- stainless prep table
- sauce stains
- tropical colors
- gritty premium food-zine aesthetic
- no readable text/logos/identifiable faces

Reusable Staff Meal prompt:
> Flash-lit Miami restaurant dish photographed against a Wynwood street-art wall, torn sticker textures, chef towel, handwritten kitchen ticket with unreadable marks, tropical color accents, gritty premium editorial food zine aesthetic, imperfect plating, warm late-night shadows, high contrast, no readable text, no logos, no identifiable faces.

## Substack API findings

Official Substack Developer API doc checked May 2026. It is **not a publishing/CMS API**.

Official endpoint documented:
```bash
GET https://substack.com/profile/search/linkedin/{linkedin-handle}
```

It returns public profile data for verified Substack creators who linked LinkedIn accounts, including handle/profile URL, leaderboard status, bestseller tier, rough free subscribers, and follower count.

Access path:
1. Create/login to Substack.
2. Review Developer API Terms of Use.
3. Submit agreement via Substack's linked Google Form.
4. Wait 7–10 business days.
5. Enable Developer API under https://www.substack.com/settings and create token.

Implication: launch workflow should use Substack UI manually for publishing while Hermes generates Substack-ready issue packages (markdown, subject, preview, image prompt, social captions). If Substack later exposes draft/publish endpoints, automate then.
