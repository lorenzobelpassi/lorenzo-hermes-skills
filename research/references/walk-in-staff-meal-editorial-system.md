# The Walk-In / Staff Meal — Editorial + Visual System

Use when drafting, positioning, or automating Lorenzo's Miami food publication on Substack/social.

## Brand architecture

### Tuesday: The Walk-In
**Tagline:** Cold storage for hot Miami food intel.

Role: weekly intelligence dispatch powered by seasonality, market movement, openings, chef/operator signals, sourcing, product windows, and what is about to matter on menus.

Content should feel like it comes from the market side and back-of-house, not from a PR desk.

### Friday: Staff Meal
**Tagline:** What to order when you know the kitchen.

Role: Miami restaurant recommendation column: what to order, where to sit, what to skip, which openings are real, and what product/seasonality tells reveal kitchen seriousness.

Internal competitive target: a sharper, Miami-native alternative to generic restaurant guides/listicles, including The Infatuation-style review culture. Publicly, do not make the beef obvious. Let readers infer it through specificity, product literacy, and quiet jokes.

## Competitive posture: coded, not obvious

Do not say “anti-Infatuation” in public copy. Do not make it a media beef. The trust move is to let the audience pick up the contrast.

Public enemy: vagueness, lazy listicles, PR-ish opening coverage, hype, dead produce, and restaurants charging a vibe tax.

Tone: funny, precise, slightly sharp, product-literate, chef/operator aware, never bitter. Punch at weak review habits and lazy sourcing, not at small restaurants trying hard.

Good line style:
- “The room is doing a lot. The crudo is doing more.”
- “Go for the salad only if the peaches are still on the menu.”
- “This is a restaurant people will describe as a scene, which is fine. Just don’t let that distract you from the rice.”
- “The tell: the herbs are not decorative.”

Avoid:
- Naming competitors frequently
- “We’re better than X” positioning
- Overt roast-page tone
- Generic “vibes are immaculate” phrasing, except as a subtle target
- Slander or unverifiable claims about restaurants/writers

## Staff Meal format

Use compact sections:

- **The Order** — what to get
- **The Seat** — where/when to sit
- **The Tell** — one detail proving the kitchen is serious: herbs, acid, bread, fish cut, vegetable handling, product timing
- **The Skip** — what not to waste money on
- **The Receipt** — one-line verdict: go now / wait / sit at the bar / order narrow / skip unless nearby

Optional sections:
- **Opening Temperature** — opening read: pitch, risk, product test, first order, verdict
- **Market Tell** — connects Friday recommendation to Tuesday seasonality/product intel
- **Order This, Not That** — direct usefulness without sounding like a listicle

## The Walk-In format

Use compact, hooky blocks:

- **On The Shelf** — product/grower/seasonality worth watching
- **Market Heat** — what is moving in pricing/supply/demand
- **On The Line** — chef/operator/personality/opening signal
- **86’d** — small contrarian take about lazy sourcing/menu habits
- **Where To Sit** — one place/dish worth attention
- **Staff Meal** — closing bite or Friday bridge

## Seasonality + openings engine

Each issue should be grounded in:
1. Current product seasonality and quality windows
2. Miami openings and operator/chef movement
3. Product-market fit: what ingredient makes or breaks a concept
4. One specific order, skip, or buyer action
5. A subtle critique of generic review/list culture through facts, not declarations

## Visual direction

Lorenzo wants a Wynwood Walls / Miami street-art / @renzlovespasta_305-adjacent energy: street textures, flash food, tropical color, restaurant exteriors, stickers, handwritten notes, and imperfect plates.

### Shared visual language
- Wynwood-style graffiti wall texture
- Flash-lit food photography
- Kitchen tickets / handwritten marker arrows / torn stickers
- Tropical Miami color: citrus yellow, tomato red, palm green, aqua, concrete gray
- Stainless steel, tile, concrete, late-night shadows
- No readable text, no logos, no identifiable faces
- Gritty premium, food-zine energy, not sterile magazine flat-lay

### OpenAI image prompt base — The Walk-In

> Flash-lit Miami back-of-house walk-in cooler scene with stainless steel shelves, condensation, crates of seasonal produce, handwritten kitchen labels with unreadable marks, chef towels, torn stickers, subtle Wynwood graffiti texture visible near the open door, tropical color accents, gritty premium editorial food zine aesthetic, cold blue-green light, cinematic shadows, no readable text, no logos, no identifiable faces.

### OpenAI image prompt base — Staff Meal

> Flash-lit Miami restaurant staff meal scene against a Wynwood-style graffiti wall, imperfect plate of pasta or grilled seafood on a stainless prep table, chef towel, kitchen ticket with unreadable marks, sauce stains, torn stickers, tropical colors, punky editorial food zine aesthetic, gritty premium, late-night after-service mood, no readable text, no logos, no identifiable faces.

## Substack/API notes

Substack setup may require manual publication creation first. The unofficial `substackapi.dev` is read-oriented (latest/top/search/single post) and useful for monitoring, but not a reliable publishing backend. Confirm official Substack Developer API capabilities in Lorenzo's account before promising automated draft/publish.

Recommended pipeline before API confirmation:
- Generate Substack-ready markdown
- Generate subject line + preview text
- Generate OpenAI cover/social image prompt
- Generate Instagram caption and Discord/internal preview
- Manual paste/publish until official API access is verified
