# The Walk-In Substack automation + competitor scout

Session context: Lorenzo designated a Discord thread as the operating room for The Walk-In Substack: automated draft creation, two weekly publishing days, and future post ideation. He then asked to automate based on questions and requested influential Miami food-industry people on Substack.

## Operating frame

- The Walk-In is a public Substack / media publication, not Selva/Cosecha company intelligence.
- Public brand hierarchy: `RLP 305` logo/avatar, `@renzlovespasta_305` personality/byline, `The Walk-In` publication, `Staff Meal` column.
- Voice: sensual, Miami, pasta/wine, late-night, industry-adjacent, reader-first.
- Default automation posture: draft-only; deliver to the Discord thread; do not publish automatically without explicit approval.
- Useful internal market/seasonal sources may inspire posts, but public copy must not expose internal competitor/Natoora data or sound like a company market letter.

## Existing scheduled automations found

A cronjob list showed existing Walk-In jobs:

- `The Walk-In Tuesday draft` — `0 8 * * 2`, origin delivery, enabled tools: web/terminal/file.
- `Staff Meal Friday draft` — `0 8 * * 5`, origin delivery, enabled tools: web/terminal/file.
- `The Walk-In Shared Daily Lead Bank` — `15 7 * * *`, local delivery, enabled tools: web/file/terminal.
- `Staff Meal review database reminder` — `0 17 * * 0`, origin delivery, asks Lorenzo for 1–3 restaurants he personally tried/wants logged.

When asked to automate, first inspect existing cronjobs and update them rather than creating duplicates.

## Automation intake questions that worked

Ask Lorenzo concise multiple-choice questions:

1. Keep Tuesday + Friday, or change days?
2. What time should drafts arrive?
3. Tuesday format: essay / scene report / personal food diary / market-ingredient / mix.
4. Friday Staff Meal format: restaurant notes / 3 things to eat / rant-opinion / personal recap / mix.
5. Draft length: 500–700 / 800–1,200 / 1,500+ words.
6. Voice: polished editorial / loose personality / darker late-night / chef-operator insider / mix.
7. Sources: only this thread / public Miami food research / meal notes / safe rewritten market intelligence / all.
8. Output format: Discord only / Google Doc / Substack-ready markdown / email style / all useful.
9. Hard no-go topics, restaurants, people, personal details.
10. Should the agent ask weekly before drafting, or draft first and let Lorenzo edit?

## Miami food Substack scout list

Search method: Substack search pages for queries like `miami food`, `Miami restaurant`, `Miami chef food`, `Miami food writer`, `Miami culinary`. Google/Bing/DDG were blocked by bot challenges, but Substack search was usable.

Good names/publications to scout or benchmark:

1. Alan Philips — `What's Good Miami` / `@alanphilips`: Miami lifestyle/culture, events/community cadence, Friday Lunch Club energy.
2. Adriana Paschen — `@miamifoodstylist`: Miami food-styling/visual world; useful for visual language and possible collaborator angle.
3. Kiera Andrews — `No Menu Needed`: surfaced with “Miami Food Diary”; close to personal taste-led food writing.
4. The Leftovers Miami: surfaced with “The 21 Best Restaurants in Miami”; direct local restaurant/listicle benchmark.
5. Anne Manning — `Trusted Tables`: surfaced with “Miami's best food isn't in Miami”; opinionated restaurant recommendation lane.
6. Uma Chalik — `Rare Medium`: restaurant essay/list writing with destination-dining polish.
7. David Mann — `Restaurant 101`: restaurant operator/marketing angle; useful for industry-insider angle.
8. Chef Ray — `Solo Supper Club`: chef/recipe creator with high Substack food engagement; useful recipe-personality benchmark.
9. Ronny Lvovski: recipe/food creator with strong engagement in Substack food notes; useful for high-performing recipe hooks.
10. Hannah — `Hannah’s Substack`: Miami lifestyle audience overlap, less food-specific.

Strategic read: Miami food Substack appears thin. The open lane is Miami food + late-night sensuality + pasta/wine + restaurant-world intimacy + personal taste diary. Avoid flattening The Walk-In into generic lifestyle/listicle/recipe content.
