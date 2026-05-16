# Selva static site cutover notes (May 2026)

Concrete reference for updating an exported/static hospitality website when source code and branded-domain access are incomplete.

## Environment and hosting findings

- Working artifact: `/Users/lorenzobelpassi/Downloads/selva-website-v10`.
- Live primary domain `selvapartners.co` was behind Cloudflare but headers showed Vercel (`x-vercel-cache`, `x-vercel-id`).
- Authenticated Vercel account could deploy a new project, but did not own the existing `selvapartners.co` domain/project.
- New preview project: `selva-partners-advisory`; public preview alias: `https://selva-partners-advisory.vercel.app/`.
- Adding `selvapartners.co` failed with Vercel `403 Not authorized`, meaning branded-domain cutover required the owning Vercel account/team or Cloudflare DNS/domain access.
- `selva-partners.com` and `www.selva-partners.com` could be added to the new Vercel project, but Cloudflare DNS still needed updating.

## Static export repair path

1. Back up the export before edits.
2. Patch visible content across HTML/TXT/JS, not just `index.html`.
3. Browser-verify after hydration. The Next static export initially reintroduced old copy from chunks.
4. Avoid risky JS chunk renames unless all references are updated. Renaming/cache-busting caused chunk/RSC failures and blank pages.
5. If source is unavailable and chunk/RSC rendering remains brittle, rewrite visible routes as vanilla static HTML/CSS. This made Vercel preview reliable.

## Route/content changes

- Recruitment was repositioned as small/optional network support, not a core offering.
- Public nav/page changed from Talent to Advisory.
- New page: `/advisory/`.
- Old page: `/talent/` retained as redirect/fallback to `/advisory/`.
- Sitemap/canonical/internal links updated to `/advisory/`.
- Verification searched for old phrases like `Executive search`, `Talent / Executive Search`, and old CTA/form labels.

## Visual/design lessons

- User preferred older Selva style: cream background, forest green, muted gold, Playfair/serif headings, Montserrat-like sans, spacious split hero, white cards, rounded dark green footer.
- Do not replace a liked brand system with a dark generic redesign just because imagery is being changed. Make content and imagery evolve inside the existing brand system.
- Final interim image direction that worked best:
  - Homepage: kitchen operations / culinary team hero.
  - Homepage supporting chips: produce/sourcing + fine dining outcome.
  - Advisory: procurement/systems image.
  - Procurement: produce/sourcing image.
  - Culinary: fine dining image.
  - Intelligence: restaurant operating environment image.
  - Contact: hospitality table/conversation image.
- Reasoning: pure fine dining was too generic; pure produce read grocery/market. Layered kitchen operations plus produce and dining better expressed Selva’s advisory/procurement/culinary/intelligence mix.
- If a lower/supporting image feels off, replace it with an editorial operating-principles panel instead of forcing another stock image. In this session, replacing the lower image with “How Selva Works” rows made the homepage cleaner.

## Copy/positioning lessons

- Remove “Talent” completely from the updated preview when the user says it is not the offering. This includes meta descriptions, legacy services/team pages, JS chunks, TXT mirrors, and phrases like “talent movement,” not only nav labels.
- Zero-to-one / chef-first language is useful as internal positioning, but the user preferred the older, more restrained public copy. Do not over-index on explicit “zero-to-one” copy on the homepage unless asked again.
- Preferred public posture: selective and inquiry-led. Say enough for qualified customers to understand Selva’s areas (Advisory, Culinary, Procurement, Intelligence), then invite them to reach out rather than over-explaining deliverables.
- Chef-first angle still matters, but keep it subtle: Selva supports the operating infrastructure around craft so chefs/operators can focus on execution. Use it as nuance, not a heavy repeated slogan.
- CTA pattern that worked after correction: a single hero “Start a Conversation,” concise service cards, and a closing “Private Inquiries” section: “Have a hospitality decision worth discussing? Share the context. If there is a fit, we will route the conversation carefully.”
- Avoid “Talent” everywhere; “leadership movement” is acceptable only for intelligence context if needed, but omit it when the user wants no hint of recruiting.

## Tool/verification notes

- If `image_generate` fails because `FAL_KEY` is missing, stop retrying it and pivot to existing assets, stock sourcing, or Midjourney prompts.
- Python `urllib` with a browser User-Agent was a good fallback when `curl` timed out or Cloudflare/WAF blocked basic requests.
- Always stop local `python3 -m http.server` processes after verification.

## Communication pattern

Be precise about what is live:

- “Updated preview is live at Vercel alias.”
- “Primary branded domain still serves old site until Vercel ownership/DNS is fixed.”

Do not tell the user the actual branded domain is updated until browser verification confirms it.
