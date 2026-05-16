# Substack as Free Distribution for a Custom Static Publication

Session date: 2026-05-09

## Situation

User wanted a full custom publication but then clarified they did not want to pay for hosting/CMS/email at launch and asked which platform self-promotes. The resulting pattern is: build/keep the custom Astro site as brand system and future front door, but launch on Substack for free distribution and discovery.

## Key finding

Substack cannot ingest or host a custom Astro/Next static site/theme. You cannot upload the custom CSS/layout/routes as the Substack publication.

What transfers well:

- Publication name and URL
- Tagline and positioning
- About page copy
- Launch manifesto
- Section architecture
- Recurring issue templates
- Post voice and editorial rubrics
- Cover art prompts/assets
- Social/Notes drafts

What does not transfer:

- Custom Astro routes/layouts
- Custom CSS/typography
- Custom archive/subscribe pages
- Full visual system beyond Substack settings
- Automated publishing via the official Substack API

## Recommended workflow

1. Treat the static site as the brand/design/content source of truth.
2. Export Substack-portable materials into a launch kit:
   - publication settings
   - About page
   - launch/welcome post
   - recurring issue templates
   - Notes/social snippets
   - image prompts/header assets
3. Launch on Substack for free email/discovery.
4. Keep the static site in reserve as a future front door once traffic exists.
5. Do not claim direct Substack automation unless authenticated in browser or using a proven unofficial workflow; official Substack API is profile lookup only, not draft/publish CMS automation.

## Concrete file pattern

Inside the project root, create:

```text
substack-launch-kit.md
SUBSTACK_SETUP_CHECKLIST.md
substack-drafts/
  welcome-to-the-publication.md
  first-issue-template.md
  recurring-column-template.md
substack-assets/
  publication-wordmark.png
  publication-wordmark.svg
```

## Guardrails

- If not authenticated, prepare assets and exact checklist instead of pretending setup is complete.
- Do not publish without user approval.
- Prefer free/self-promoting launch surfaces when the user explicitly does not want to pay.
