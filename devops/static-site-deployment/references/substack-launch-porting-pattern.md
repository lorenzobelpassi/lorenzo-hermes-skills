# Substack Launch Porting Pattern

Session-specific reference for moving a custom-coded publication concept into Substack when the user wants a free, self-promoting platform instead of paying for hosting/CMS/email.

## When this applies

- User has a custom static publication MVP (Astro/Next/static HTML) but does not want to pay for hosting, CMS, or email infrastructure.
- User asks if the coded site can be “put on Substack.”
- User wants free built-in promotion/discovery more than full design control.

## Core answer

Substack cannot import/upload a custom site theme, Astro build, routes, CSS, or CMS. What transfers is the publication system:

- Brand name and tagline
- About page copy
- Launch manifesto
- Post/issue drafts
- Section architecture
- Recurring column formats
- Notes/social drafts
- Header/logo/cover art assets
- Editorial voice and prompts

Position Substack as the **free distribution engine** and the custom coded site as the **future premium front door/archive/source of truth**.

## Workflow

1. Audit the coded publication content:
   - `src/pages/index.*` for hero, tagline, section copy.
   - `src/pages/about.*` for About/manifesto.
   - `src/content/posts/*.md` or equivalent for issue templates.
   - `src/pages/subscribe.*` for intended Substack URL.
2. Create a launch kit in the project root:
   - `substack-launch-kit.md`
   - `SUBSTACK_SETUP_CHECKLIST.md`
   - `substack-drafts/<launch-post>.md`
   - `substack-drafts/<issue-template>.md`
   - `substack-assets/<wordmark/header>.png`
3. Attempt browser setup only if authenticated. If Substack asks for sign-in/magic link, stop before credentials friction and produce exact manual steps.
4. Check the public Substack page for visible identity mistakes. In this session, the page showed `By Skwphmh`, which became a high-priority manual fix.
5. If image generation credentials are missing, do not retry the same unavailable generator. Create a simple local wordmark/header asset with SVG/Pillow or provide prompts.
6. Verify files exist and report exact paths.

## Suggested file contents

`substack-launch-kit.md` should include:

- Publication settings: name, URL, sender name, tagline, categories, cadence.
- About page copy.
- Launch welcome post.
- First Tuesday issue template.
- First Friday/column issue template.
- Substack Notes drafts.
- Instagram bio.
- Cover art prompts.

`SUBSTACK_SETUP_CHECKLIST.md` should be short and actionable:

- Fix publication/author identity.
- Paste About page.
- Publish/schedule launch post.
- Save issue templates as drafts.
- Upload header/wordmark.
- Turn on free discovery settings: public archive, recommendations, Notes, SEO, comments.
- Keep paid/pledge off until the free audience exists.

## User preference learned

For Lorenzo/The Walk-In, prioritize free launch and native discovery over custom design. Recommend Substack first, preserve the coded Astro site for later once audience demand exists.
