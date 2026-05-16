# Free Publication Launch / Substack Bridge Pattern

Use this when a user has or wants a custom-coded publication site but does **not** want to pay for hosting/CMS/email at launch and asks which platform self-promotes.

## Core recommendation

Substack is often the best free distribution engine for early-stage editorial projects because it provides:
- Email delivery.
- Subscriber management.
- Public archive and SEO-indexable posts.
- Recommendations/discovery surfaces.
- Notes/social feed.
- No up-front hosting/CMS/email cost.

Tradeoff: Substack controls the layout and does not allow uploading a custom Astro/Next theme as the publication UI.

## What can be ported from a custom site into Substack

Portable:
- Publication name, tagline, about copy.
- Brand voice and positioning.
- Section architecture and recurring column names.
- Post templates and issue structures.
- Launch manifesto/welcome post.
- Notes/social post drafts.
- Header/logo/wordmark assets if the platform allows uploads.

Not portable:
- Custom routes like `/staff-meal/` or `/walk-in/`.
- Custom CSS, typography system, archive layout, and homepage design.
- Custom subscribe flow.
- Framework behavior/components.

## Practical workflow

1. Keep the custom static site as the brand/design source of truth and future premium front door.
2. Create a `substack-launch-kit.md` with:
   - Publication settings.
   - About page copy.
   - Launch post.
   - First issue templates.
   - Notes drafts.
   - Instagram/bio copy.
   - Cover art prompts/assets.
3. Create separate draft files under `substack-drafts/` so the user can paste them directly.
4. Create `SUBSTACK_SETUP_CHECKLIST.md` with exact dashboard steps.
5. If browser automation is not authenticated, stop at the sign-in/magic-link blocker and report exactly what remains manual.
6. Do not promise automatic Substack publishing: the official Substack Developer API is not a post publishing API.

## Authentication/publishing caveat

Substack magic links and private dashboard routes often block remote/browser automation unless the user completes login in the same browser session. Treat dashboard setup as possible only after authenticated access is verified. If unauthenticated, package copy/assets locally and give the user exact paste targets.

## Example file layout

```text
publication-project/
  substack-launch-kit.md
  SUBSTACK_SETUP_CHECKLIST.md
  substack-drafts/
    welcome-post.md
    first-issue-template.md
    recurring-column-template.md
  substack-assets/
    wordmark.png
    wordmark.svg
```
