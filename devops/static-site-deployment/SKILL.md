---
name: static-site-deployment
description: "Use when publishing, repairing, or cutting over static websites from exported artifacts or source folders, especially Vercel/Cloudflare-backed sites where domain ownership, hydrated JS chunks, DNS, redirects, and live verification matter."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [static-site, vercel, cloudflare, deployment, dns, nextjs-export, website]
    related_skills: [cloudflare-domain-management, github-repo-management, requesting-code-review]
---

# Static Site Deployment

## Overview

Use this skill for end-to-end static website work: finding the deployable artifact, making copy/content edits, replacing assets, deploying to Vercel or another static host, connecting branded domains, and verifying the live site. It is especially useful when the original source code is missing and the only available artifact is a static export.

The key rule: **separate artifact deployment from branded-domain cutover.** A new Vercel deployment can be live and correct while the real domain is still serving an old project. Always verify both.

## When to Use

- User asks to make a website live, publish changes, deploy a static folder, or update a branded domain.
- A site is behind Cloudflare but response headers indicate Vercel or another origin.
- You have a static export (`index.html`, `_next/`, `robots.txt`, `sitemap.xml`) rather than source components.
- User asks for route changes, content changes, or image swaps on an exported site.
- A deployment works on a temporary URL but not the production/branded domain.

Don't use this skill as the primary guide for dynamic app debugging, database-backed apps, or CI/CD pipeline design unless the final artifact is a static site.

## Deployment Workflow

1. **Inventory the hosting stack before promising a cutover.**
   ```bash
   curl -sS -I https://example.com | sed -n '1,40p'
   dig +short example.com
   dig +short www.example.com
   command -v vercel || true
   vercel whoami || true
   vercel project ls || true
   vercel domains ls || true
   ```
   If headers include `x-vercel-cache` or `x-vercel-id`, treat Vercel as the deployment owner even when `server: cloudflare` appears.

2. **Back up the artifact before editing.**
   ```bash
   cd /path/to/site
   zip -qr ../site-backup-before-edits.zip .
   ```

3. **Make edits in the real files served by the browser.**
   Static exports may include multiple representations of the same route: `index.html`, RSC/text mirrors, JS chunks, manifests, and fallback pages. Search broadly before patching.
   ```bash
   grep -RIn "Old phrase\|/old-route/\|old-image.jpg" . --include='*.html' --include='*.txt' --include='*.js' --include='*.xml'
   ```

4. **Run a local server and verify with a browser, not only grep.**
   ```bash
   python3 -m http.server 8765
   ```
   Navigate to the local URL and check visible text, routes, console errors, and form behavior.

5. **Deploy the artifact.**
   ```bash
   cd /path/to/site
   vercel deploy --prod --yes
   ```
   If the project is not linked, Vercel may create `.vercel/`. Do not expose internal IDs or tokens from that folder.

6. **Verify the deployment URL and the branded domain separately.**
   Use browser automation for Cloudflare-protected domains and Python/urllib when `curl` is flaky.
   ```python
   from urllib.request import Request, urlopen
   req = Request('https://deployment.example.vercel.app/', headers={'User-Agent':'Mozilla/5.0'})
   with urlopen(req, timeout=20) as r:
       html = r.read().decode('utf-8', 'ignore')
       print(r.status, html.count('Expected phrase'), html.count('Old phrase'))
   ```

## Vercel + Cloudflare Domain Cutover

A successful Vercel deployment does not mean the user's branded domain is connected.

- `vercel domains add example.com` returning `403 Not authorized` means the domain belongs to another Vercel account/project. You need the owning Vercel account/team, a transfer/removal from the old project, or DNS/API access that can repoint to the new project.
- If Vercel lets you add the domain but says it is not configured, Cloudflare DNS still needs to be updated to the current Vercel-recommended records. Verify current Vercel guidance before editing DNS.
- For simple redirects on Cloudflare, load `cloudflare-domain-management`. Redirect targets must include the scheme, e.g. `https://target.com`, not `www.target.com`.

Communication rule: say exactly which surface is live:

- `Updated version is live on the Vercel deployment URL: ...`
- `The branded domain still serves the old site until Vercel ownership/DNS is connected.`

## Static Next Export Pitfalls

Next.js static exports can hydrate from `_next/static/chunks/app/**` and RSC/text mirrors. Editing only `index.html` can appear correct in `curl` while the browser reverts to old content after hydration.

Checklist for hand-edited Next static exports:

- Search and patch `*.html`, `*.txt`, `*.js`, and relevant manifests.
- Verify browser-visible content after hydration.
- Scan for missing JS references after renaming/cache-busting chunks.
- If patched chunks produce blank pages, chunk load errors, or RSC fetch failures and the source is unavailable, replace key route `index.html` files with vanilla static HTML/CSS as an emergency publish path.
- Preserve route structure, metadata, image paths, `robots.txt`, and `sitemap.xml`.

Missing JS reference scanner:

```python
from pathlib import Path
import re
root = Path('/path/to/site')
missing = []
for p in list(root.rglob('*.html')) + list(root.rglob('*.txt')) + list(root.rglob('*.js')):
    s = p.read_text(errors='ignore')
    for m in re.findall(r'/_next/static/[^"\']+\.js', s):
        if not (root / m.lstrip('/')).exists():
            missing.append((str(p.relative_to(root)), m))
print(missing)
```

## Route Rename Pattern

When changing a public route such as `/talent/` to `/advisory/`:

1. Create the new directory and copy/rewrite the page: `advisory/index.html`.
2. Replace internal links, sitemap entries, canonicals, and metadata from `/old/` to `/new/`.
3. Keep the old route as a redirect/fallback to avoid breaking existing URLs:
   ```html
   <meta http-equiv="refresh" content="0; url=/advisory/">
   <script>location.replace('/advisory/');</script>
   ```
4. Verify both URLs: `/new/` must render the page, `/old/` must land on `/new/` or clearly link there.
5. Deploy and re-check the hosted URL before touching branded DNS.

## Content Repositioning / Copy Cleanup Pattern

When the user asks to remove or de-emphasize a visible service/category, scan for semantic leftovers, not only exact nav labels. For example, after changing a hospitality site from “Talent” to “Advisory,” also search/remove body/meta terms like “talent movement,” “executive talent placement,” route links in legacy `services/` or `team/` pages, JS layout chunks, `404` pages, and TXT/RSC mirrors.

Recommended scan after every repositioning deploy:

```python
from urllib.request import Request, urlopen
import re
base = 'https://preview.example.vercel.app'
for path in ['/', '/about/', '/advisory/', '/old-route/', '/services/', '/team/', '/sitemap.xml']:
    req = Request(base + path, headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(req, timeout=20) as r:
        html = r.read().decode('utf-8', 'ignore')
        print(path, 'old term hits', len(re.findall('old term', html, re.I)))
```

For positioning changes, preserve the liked visual system unless the user explicitly asks for a redesign. Make content sharper by changing headlines, cards, and operating-principle panels before changing layout.

If the user wants the site to drive inquiries rather than explain everything, keep the homepage selective: concise hero positioning, one primary contact CTA, short service cards, and a closing private-inquiry CTA. Do not over-correct into long methodology copy just because strategic positioning was discussed; public pages can hint at the operating thesis and leave the rest for the conversation.

## Image Replacement Pattern

1. Inventory image assets and references:
   ```python
   from pathlib import Path
   import re, os
   root = Path('/path/to/site')
   for p in root.rglob('*.html'):
       s = p.read_text(errors='ignore')
       refs = re.findall(r"(?:src|href)=['\"]([^'\"]+\.(?:jpg|jpeg|png|webp|svg|ico))['\"]|url\(['\"]?([^'\")]+\.(?:jpg|jpeg|png|webp|svg|ico))['\"]?\)", s, re.I)
       for a,b in refs:
           print(p.relative_to(root), a or b)
   ```
2. If the user delegates creative direction, do a first pass instead of asking them to choose every image: create a contact sheet, use browser/vision review to pick the strongest assets, update references, deploy to a preview URL, and include a screenshot for approval.
3. Ask for or locate replacement files. Preserve filenames for the lowest-risk swap, or update all references if renaming.
4. If using AI image generation, first verify the required env/API key is present. If image generation fails due missing credentials, switch to licensed/sourceable stock assets or provide Midjourney prompts rather than retrying the same failed tool.
5. Optimize large images before deploy when possible.
6. Verify visual fit in-browser on every page that uses the image; text/count checks alone do not catch generic or off-brand imagery.

## Astro Static Publication Pattern

For custom editorial/publication sites, Astro is a good default when the user needs fast static output, Markdown/MDX issue pages, archives, section pages, and RSS without a heavy app.

If the user later decides they do **not** want to pay for hosting/CMS/email and asks for a platform that self-promotes, do not try to force the custom site onto Substack as code. Substack can act as the free distribution engine, but only the brand/copy/templates/assets port over; custom Astro routes/CSS/layouts do not. Package a `substack-launch-kit.md`, `substack-drafts/`, `substack-assets/`, and a paste-by-hand setup checklist. See `references/substack-free-distribution-for-static-publications.md`.

Recommended scaffold flow:

1. Create the site and install RSS support:
   ```bash
   npm create astro@latest my-publication -- --template minimal --typescript strict --install
   cd my-publication
   npm install @astrojs/rss
   ```
2. On Astro 6+, use `src/content.config.ts` with an explicit loader; do **not** create legacy `src/content/config.ts`:
   ```ts
   import { defineCollection, z } from 'astro:content';
   import { glob } from 'astro/loaders';

   const posts = defineCollection({
     loader: glob({ pattern: '**/*.md', base: './src/content/posts' }),
     schema: z.object({
       title: z.string(),
       dek: z.string(),
       pubDate: z.coerce.date(),
       section: z.string(),
       tags: z.array(z.string()).default([]),
       draft: z.boolean().default(false),
     }),
   });

   export const collections = { posts };
   ```
3. For dynamic post routes on Astro 6 content entries, derive URL slugs from `post.id` unless the schema explicitly defines a slug field:
   ```ts
   return posts.map((post) => ({
     params: { slug: post.id.replace(/\.md$/, '') },
     props: { post },
   }));
   ```
   Use the same `post.id.replace(/\.md$/, '')` pattern in archive cards and RSS links.
4. Verify both build and browser render:
   ```bash
   npm run build
   npm run dev -- --host 127.0.0.1
   ```
   Check homepage, section pages, at least one post page, RSS, and console errors. Stop the dev server before finishing.

See `references/astro-publication-mvp-2026-05.md` for a concrete Astro 6 publication scaffold and the migration errors/fixes encountered.

## Substack Fallback / Free Distribution Pattern

When a user pivots from a custom coded publication to a free self-promoting platform, Substack is often the best distribution-first option. Do not imply the custom static site can be uploaded as-is: Substack cannot import Astro/Next routes, CSS, custom layouts, or themes. Instead, port the **publication system**: brand settings, About copy, launch post, issue templates, recurring sections, Notes drafts, and header/cover assets. If the browser session is not authenticated, create local launch-kit/checklist files with exact paste-in steps and stop before credentials friction. See `references/substack-free-distribution-for-static-publications.md`.

## Substack Website Editor Translation Pattern

Substack has a website/publication editor, but it is not a full custom-code surface. Do not promise that Astro/React/HTML/CSS can be pasted into Substack as a theme. When moving a custom-coded editorial site into Substack:

1. Translate the custom site into editor settings:
   - publication name / byline
   - tagline / About copy
   - logo/header asset
   - theme choice
   - accent/background colors if available
   - nav labels and sections/categories
   - launch post copy
2. Preserve the coded site as a design/source-of-truth archive or future front door.
3. If the user says Substack has a website editor, acknowledge it and provide a settings sheet. Do not overcorrect with “Substack can’t do code” only; the useful answer is “yes, use the editor, but translate code into settings.”
4. Treat Substack as the free distribution layer; custom Astro remains the upgrade path if full design control or API publishing becomes necessary.

## Forms

Static form markup often looks functional but does nothing. Inspect the final deployed HTML/JS before claiming form support.

- Confirm `form action`, `method`, input `name` attributes, and third-party endpoint.
- If using Formspree or similar, test with a harmless submission only if the user approves sending a test inquiry.
- If no backend exists, use `mailto:` or replace the form with clear contact CTAs rather than a fake submit button.

## Common Pitfalls

1. **Confusing Cloudflare edge with the host.** Cloudflare headers only prove the domain is proxied; check origin hints and deployment provider.
2. **Saying “live” before the branded domain changes.** A Vercel preview/production URL is not the same as `example.com`.
3. **Editing static HTML only on a hydrated export.** Browser content may come from JS/RSC chunks.
4. **Breaking old routes during renames.** Keep redirects/fallbacks for public URLs.
5. **Repeating flaky verification commands.** If `curl` times out and a tool blocks retries, switch to browser navigation or Python `urllib` with a normal User-Agent.
6. **Exposing secrets.** Redact OAuth device codes, API tokens, dashboard passwords, `.vercel` internals, and long opaque IDs in summaries.
7. **Repeating unavailable generation tools.** If `image_generate` fails with missing provider credentials (for example `FAL_KEY environment variable not set`), stop retrying that tool in the same turn. Use existing assets, source licensed stock imagery, or prepare prompts for the user's external generator.

## Verification Checklist

- [ ] Backed up the original artifact.
- [ ] Local browser verification completed for all edited routes.
- [ ] Hosted deployment URL shows expected copy/images/routes.
- [ ] Old phrases/routes are absent where required.
- [ ] Branded domain separately verified, or blocker stated clearly.
- [ ] DNS/domain ownership status checked if branded domain is still old.
- [ ] Forms inspected and tested only with appropriate approval.
- [ ] Long-running local test servers stopped after use.

## References

- `references/selva-static-site-cutover-2026-05.md` — concrete session notes for a Vercel/Cloudflare static export recovery, `/talent/` → `/advisory/` rename, image inventory, and domain-access blocker.
