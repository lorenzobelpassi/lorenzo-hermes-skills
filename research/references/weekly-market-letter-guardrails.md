# Selva Weekly Market Letter — Guardrails and Format

Session origin: Lorenzo wants the Market Intel / lead-gen system to support a branded weekly newsletter before any third-party outreach. The newsletter should feel like Natoora-style market education, but be Selva-owned and safe.

## Hard guardrails

- **Internal intelligence first.** Restaurant intel, Natoora archive data, seasonal sales calendars, scraped lead data, and competitor account mapping are internal inputs only.
- **No third-party sends by default.** Do not email/DM/text prospects or create live sending workflows unless Lorenzo explicitly approves in the current session.
- **No automated Chloe sending.** Chloe may draft only. Every external send requires Lorenzo approval of both copy and recipients.
- **No raw competitor data externally.** Public-facing copy must not mention competitor sales quantities, raw archive signals, or “Natoora sold X.” Use generalized seasonality and Selva’s own availability/market read.
- **No unverified farm names.** Farm/grower names may be used only when verified from supplier/grower-side source for that week. Otherwise use placeholders in internal drafts.
- **Pipeline safety.** Restaurant Intel leads should stay `Needs Review` / `Nurture` until Lorenzo approves outreach. Newsletter material can warm the market before direct selling.

## Public newsletter content allowed

- Seasonal product features
- Miami market notes: weather, freight, FX, pricing, quality separation
- Variety-specific produce education
- Chef/bar use cases
- Farm/grower stories once verified
- Availability highlights and sample-worthy items
- Quiet CTA: reply for availability/sample list

Avoid:
- “Premium,” “high-quality,” hype language
- Direct named comparison to Natoora unless Lorenzo explicitly approves
- Scraped private contact data
- Unverified claims or invented grower relationships

## Preferred weekly structure

Working title: **Selva Market Letter**

1. This Week’s Market Read
2. Product Window / What’s Coming In
3. Grower / Farm Note (verified only)
4. Chef Note — how to use it on menu/bar
5. Miami Watch Items
6. Availability / Samples
7. Quiet CTA

## Copy style

- Direct, short, useful; reads like a buyer/trader’s note.
- Specific varieties beat broad categories. Do not write “citrus” when the useful detail is Cara Cara, Meyer lemon, Oro Blanco, Nagami kumquat, finger lime, Makrut lime leaf, yuzu, Seville orange, Sorrento lemon, etc.
- Tie each item to: **variety → farm/grower → current window → kitchen/bar use**.
- If farm/grower is unknown, keep the farm line as `[Farm / grower — verify before send]` and mark the draft internal.

## Citrus example pattern

```text
### Cara Cara Orange
Grower: [Farm / grower — verify before send]
Window: Active now
Use: salads, crudo, seafood, desserts, cocktails

Cara Cara gives color without being loud. Lower acid than standard navel, with a deeper berry-like note. Good for composed plates where blood orange is too aggressive.
```

## Approval workflow

1. Draft internal edition.
2. Fill verified farm/grower names and actual availability.
3. Mark anything source-sensitive as internal notes only.
4. Lorenzo reviews copy and recipient list.
5. Only after explicit approval, create/send newsletter.

## Local artifacts from setup

- Guardrails: `~/.hermes/selva_leads/NEWSLETTER_GUARDRAILS.md`
- Template: `~/.hermes/selva_leads/selva_market_letter_template.md`
- Seasonal sheet: `https://docs.google.com/spreadsheets/d/1buZGrV73CD3KIyxr7y3-hKEIOR3Vvlzze9V3In_fUq8/edit`
