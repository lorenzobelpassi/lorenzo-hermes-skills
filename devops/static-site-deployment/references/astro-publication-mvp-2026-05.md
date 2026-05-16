# Astro publication MVP notes — 2026-05

Use this reference when building a custom static editorial/publication site with Astro 6+, Markdown content collections, section pages, archive pages, and RSS.

## Proven stack

- Framework: Astro static output
- Content: Markdown files under `src/content/posts/`
- Feed: `@astrojs/rss`
- Typical routes:
  - `/`
  - `/archive/`
  - `/about/`
  - `/subscribe/`
  - section pages such as `/walk-in/`, `/staff-meal/`
  - dynamic posts at `/posts/[slug]/`
  - `/rss.xml`

## Astro 6 content collection config

Astro 6 removed legacy `src/content/config.ts` content collections. Use `src/content.config.ts` plus a loader.

```ts
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/posts' }),
  schema: z.object({
    title: z.string(),
    dek: z.string(),
    pubDate: z.coerce.date(),
    section: z.enum(['The Walk-In', 'Staff Meal']),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
  }),
});

export const collections = { posts };
```

## Error: legacy content config

Symptom:

```text
[LegacyContentConfigError] Found legacy content config file in "src/content/config.ts". Please move this file to "src/content.config.ts" and ensure each collection has a loader defined.
```

Fix:

1. Create `src/content.config.ts` using `glob` from `astro/loaders`.
2. Remove `src/content/config.ts`.
3. Re-run `npm run build`.

## Error: Missing parameter: slug

Symptom during static build:

```text
Missing parameter: slug
```

Cause: content entries from the Astro 6 loader may not expose `post.slug` the way older examples do.

Fix dynamic route `getStaticPaths()` and all links/RSS URLs to derive slugs from `post.id`:

```ts
return posts.map((post) => ({
  params: { slug: post.id.replace(/\.md$/, '') },
  props: { post },
}));
```

Link pattern:

```astro
<a href={`/posts/${post.id.replace(/\.md$/, '')}/`}>{post.data.title}</a>
```

RSS pattern:

```ts
link: `/posts/${post.id.replace(/\.md$/, '')}/`,
```

## Verification checklist

- `npm run build` succeeds and emits `dist/`.
- Generated routes include homepage, archive, section pages, post pages, and `/rss.xml`.
- Run `npm run dev -- --host 127.0.0.1` and browser-check at least:
  - homepage
  - one section page
  - one dynamic post
  - `/rss.xml`
- Check browser console for JS errors.
- Kill the local dev server after verification.

## Communication pattern

When reporting a completed MVP, include:

- Local project path
- Stack
- Routes created
- Build status (`npm run build` passed)
- Local verification summary
- Exact commands to run locally
- Clear caveats: email backend, CMS, deployment, domain, and mobile QA if not completed
