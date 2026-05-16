# Lead Processing Patterns

Patterns for cleaning and processing raw lead data (e.g., from Pipedrive exports, scraped data, CSV imports).

## Quality Filtering

Standard thresholds for Miami restaurant prospects:

| Tier | Rating | Reviews | Use Case |
|------|--------|---------|----------|
| All quality | 4.0+ | 100+ | Full pipeline |
| Top tier | 4.5+ | 500+ | Priority outreach |
| Premium | 4.6+ | 1000+ | High-value targets |

## Deduplication

Dedupe by `name + phone` (same restaurant, different email contacts). Consolidate emails and pick the best one:

```python
restaurants = {}
for r in rows:
    key = f"{r['name']}|{r['phone']}"
    if key not in restaurants:
        restaurants[key] = {..., 'emails': set()}
    restaurants[key]['emails'].add(r['email'])

# Pick best email (prefer named contacts over generic)
for r in restaurants.values():
    emails = list(r['emails'])
    best = emails[0]
    for e in emails:
        if not any(x in e.lower() for x in ['info@', 'contact@', 'hello@', 'support@']):
            best = e
            break
    r['email'] = best
```

## Segmentation

Restaurant segmentation for specialty produce targeting:

```python
cat = lead['category'].lower()
if 'sushi' in cat or 'japanese' in cat:
    seg = 'Japanese/Sushi'
elif 'italian' in cat:
    seg = 'Italian'
elif 'steakhouse' in cat or 'steak' in cat:
    seg = 'Steakhouse'
elif 'seafood' in cat:
    seg = 'Seafood'
elif 'mexican' in cat or 'latin' in cat or 'cuban' in cat or 'peruvian' in cat:
    seg = 'Latin/Mexican'
elif 'fine dining' in cat:
    seg = 'Fine Dining'
elif 'bar' in cat or 'lounge' in cat:
    seg = 'Bar/Lounge'
else:
    seg = 'Other'
```

## Miami Cold Outreach Dataset (Feb 2026)

Source: `Miami Cold Outreach - Raw.csv` extracted from Lorenzo's Natoora work email.

| Metric | Value |
|--------|-------|
| Raw rows | 2,037 |
| After dedupe + quality filter | 734 |
| Top tier (4.5+, 500+) | 346 |
| Premium (4.6+, 1000+) | 185 |

Key fields: name, email, phone, city, state, rating, reviews, category/subtypes, website, instagram

Saved to: `/tmp/miami_leads_clean.json`
