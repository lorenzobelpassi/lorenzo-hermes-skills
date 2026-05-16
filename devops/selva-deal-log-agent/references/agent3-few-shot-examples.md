# Agent 3 Few-Shot Examples

These are the canonical voice examples for the Pipeline Tracker agent. 
The system prompt instructs Claude to pick the right pattern based on 
tier + touch_count + last_touch_type, and adapt specifics — not invent a new style.

---

## Example 1: COLD + First Follow-Up After Drop-Off

**Context:**
- Tier: COLD
- Touch count: 1
- Last touch type: in-person drop-off
- Days since last touch: 1
- Contact: Diego Reyes / Casa Tua (Miami Beach)
- Commodity: Sungold tomatoes from a Veracruz grower
- Last note: Dropped off a pint with the sous chef yesterday afternoon. Diego wasn't in. Left a card.
- Intel: Italian-leaning menu, chef-driven, currently sourcing from Sysco for tomatoes.

**Output:**
- Channel: email
- Subject: tomatoes for casa tua

> Chef Diego —
> 
> Left a pint of Sungolds with your sous yesterday. Veracruz grower we work with direct, picked Tuesday, on a truck Wednesday. Flavor is different from anything in the commodity supply.
> 
> If they hit, I can build a weekly order around what works for the menu. No minimum to start.
> 
> Lorenzo

---

## Example 2: WARM + Post-Tasting, Push for Pricing

**Context:**
- Tier: WARM
- Touch count: 3
- Last touch type: email
- Days since last touch: 7
- Contact: Sarah Liu / Stubborn Seed (South Beach)
- Commodity: Treviso radicchio from a small Veneto grower
- Last note: She tasted the first sample, said the texture was great but wanted to see pricing on a weekly standing order before committing.
- Intel: Tasting menu restaurant, ingredient-forward. Currently buys some heritage stuff from Chef's Garden.

**Output:**
- Channel: email
- Subject: treviso pricing — weekly standing

> Chef —
> 
> Following up on the treviso. On a 4-head weekly standing order I can do $11.50/head delivered, locked for 8 weeks. That's about 12% under the spot price you'd see anywhere else for this variety, and you'd be the only menu in Miami running it.
> 
> Want me to start it for next week's drop?
> 
> Lorenzo

---

## Example 3: HOT + Close the Deal

**Context:**
- Tier: HOT
- Touch count: 5
- Last touch type: tasting
- Days since last touch: 2
- Contact: Marco Salerno / Macchialina (South Beach)
- Commodity: Full Italian heritage program — datterini, puntarelle, agretti
- Last note: Did a tasting Friday. He loved the puntarelle. Said he'd circle back Monday with which items he wants on the standing list.
- Intel: Italian chef, knows the products by name, this is exactly the right account for our positioning.

**Output:**
- Channel: email
- Subject: puntarelle program

> Marco —
> 
> Checking in on Friday's tasting. Puntarelle's only available for another 3 weeks before the season turns, so if it's going on the menu I'd want to lock the standing volume now to make sure you're covered.
> 
> Happy to call this afternoon if it's easier than email.
> 
> Lorenzo

---

## Example 4: WARM + Re-engagement (14+ Days Quiet)

**Context:**
- Tier: WARM
- Touch count: 4
- Last touch type: email
- Days since last touch: 14
- Contact: Eli Brennan / Boia De (Buena Vista)
- Commodity: Heritage tomato program for summer menu
- Last note: Had one good back-and-forth in February. Sent a sample of San Marzanos in March, got 'these look great' back, then nothing.
- Intel: Chef-driven, Italian-leaning, Michelin recommended.

**Output:**
- Channel: email
- Subject: summer menu

> Chef —
> 
> Know you've been heads-down. We're starting to lock in summer tomato programs with restaurants now — first San Marzano harvest is mid-June and supply is tighter than last year.
> 
> If there's a fit for Boia De I'd want to get you on the list before it's full. 10 minutes on the phone to scope it?
> 
> Lorenzo

---

## Example 5: COLD + Instagram DM Channel

**Context:**
- Tier: COLD
- Touch count: 2
- Last touch type: instagram DM
- Days since last touch: 3
- Contact: Jen Park / Itamae Ao (Design District)
- Commodity: Specialty citrus — yuzu, sudachi, kabosu
- Last note: DMed her after she posted a yuzu plate. She read it, didn't reply.
- Intel: Sushi-forward, ingredient obsessive. Active on IG.

**Output:**
- Channel: instagram_dm
- Subject: (none)

> Hey Chef — saw the yuzu plate from last week. We're getting fresh yuzu, sudachi, and kabosu in next Tuesday from a small grower in Wakayama. Direct, not commodity. Want me to drop a sample by the kitchen?

---

## Example 6: SKIP — Move to Nurture

**Context:**
- Tier: WARM
- Touch count: 6
- Last touch type: email
- Days since last touch: 30
- Contact: Patrick Doyle / L'Atelier de Joël Robuchon (Design District)
- Commodity: European herb program
- Last note: Ghosted after 5 touches over 2 months. Hotel restaurant — F&B sign-off is probably stuck somewhere.
- Intel: F&B has final say, chef likes the product but isn't the decision maker.

**Output:**
- Channel: skip
- Subject: (none)

> SKIP — 6th touch with no engagement and decision is stuck above the chef level. Move to quarterly nurture. Suggest Lorenzo flag this account in Notion as 'Nurture Q' and revisit in 90 days with a new seasonal product.

---

## Voice Rules Summary

1. **Direct** — No "I hope this finds you well." No "I wanted to reach out." Lead with the specific thing.
2. **Short** — Email body 3-5 sentences max. DMs 2-3.
3. **No exclamation marks** unless the prior thread had them.
4. **Sign off "Lorenzo"** on its own line. No "Best," / "Cheers," / "Best regards."
5. **Subjects** — lowercase if it's a follow-up to an existing thread, title-case for new ones. Keep under 6 words.
6. **Reference one specific thing** — a product, a market move, a date, a number — not vague enthusiasm.
7. **Never mention "premium" or "high-quality"** — let the specifics do that work.
8. **Never write "Hope you're doing well"** or any version of it.
