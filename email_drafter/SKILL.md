---
name: email_drafter
description: "Generates professional email drafts for Selva Partners outreach, follow-ups, and client communication."
tags: [email, drafting, outreach, sales, selva-partners]
---

# Email Draft Generator

Generates professional email drafts for Selva Partners — outreach, follow-ups, proposals, and client communication.

## Tone & Style (Lorenzo's confirmed preference)

- **Direct and confident** — no fluff, no wind-up, no throat-clearing
- Short paragraphs, punchy sentences — every word earns its place
- Let the product speak; avoid overselling or adjective stacking
- Understated exclusivity over hard sell — the reader should feel chosen, not pitched
- Less is more. When in doubt: cut it in half, then cut again
- Lorenzo explicitly approved: "I like the direct nature"
- First draft rejected for being too long and flowery. Second draft — 4 short paragraphs, no preamble — approved immediately

## Trigger Words
- "draft email"
- "write email"
- "email template"
- "outreach"
- "send email to"

## Lorenzo's Style — MANDATORY
Direct and confident. Short paragraphs, punchy sentences. Let the product speak — no overselling, no fluff.
Understated exclusivity over hard sell. 3-5 sentences max for body copy.
First draft was too long and formal — user explicitly preferred the second, shorter version.
When in doubt: cut it in half.

## Routing: Outreach vs Newsletter vs Relationship-Risk

This skill is for the writing pass, not the whole operating workflow.

Use it for three cases:
- outreach and follow-up drafts
- relationship-risk drafts for existing accounts
- final subscriber-facing newsletter / market-letter copy once the facts, growers, and product windows are already verified

Do not use this skill alone when the user first asks for market intel, lead qualification, or editorial planning. In those cases:
- use `selva-market-intel` for facts, signals, sources, and internal/public separation
- use `lorenzo-operating-lanes` to identify the lane and source of truth
- then use this skill to write the final draft in the correct tone

## Selva Market Letter / Newsletter Style

For chef/operator newsletters, do not write a generic availability email. Write a short insider editorial (3–4 minute max) for chefs, owners, F&B directors, buyers, and hospitality operators.

Rules:
- Open with an eye-catching headline, not a bland title.
- Every section needs an opinion; do not save all opinion for the end.
- Avoid rigid/bland headings like “Produce,” “Openings,” “Personality,” “Unpopular Opinion.” Use hook headings like “The leaf has to do something,” “More Caribbean menus. More bad mango incoming,” “Watch the connector, not the press release,” “Small heresy.”
- Include one tiny polarizing/controversial section weekly, but punch at lazy sourcing/menus/generic habits, not named restaurants or chefs.
- Include Lorenzo’s personal focus: one product, why he cares, how to cook/use it, the common mistake, and who should care.
- Make it sensory: smell, snap, bitterness, crunch, perfume, plate rhythm, whether it survives dressing/heat/salt/acid.
- Use INBOUND/sourcing-map growers, named varieties, and verified farm/grower names only; keep raw competitor/Natoora archive data internal.

## Selva Market Letter / Newsletter Drafts

When drafting subscriber-facing market letters, keep the same direct style but make the copy feel like a buyer's note, not a generic newsletter:
- Use specific varieties, not broad categories. Example: Cara Cara, Meyer lemon, Oro Blanco, Nagami kumquat, finger lime, Makrut lime leaf — not just “citrus.”
- Include grower/farm names only when verified. If unknown, use `[Farm / grower — verify before send]` in internal drafts and do not send externally.
- Tie every featured product to: variety → farm/grower → current window → kitchen/bar use.
- Keep competitor/Natoora archive data internal; public copy can use generalized seasonality and Selva's own market read, never raw competitor quantities or account names.
- No third-party sends or Chloe sends until Lorenzo explicitly approves copy and recipient list.

## Context Needed
- Recipient name/company (use [Name] if unknown)
- Purpose (intro, follow-up, proposal, etc.)
- Key points to include
- Tone override (if different from default direct style)

## FullFilled Foods Outreach

For FullFilled Foods sales/BD outreach, load `references/fullfilled-foods-outreach.md`. It captures the durable campaign rules: Natoora-style mission flow, family Tuesday Drop positioning, Instagram/TikTok for families, meetings + sampling for companies, white-label wellness, CRM logging, Lorenzo’s Selva sending account, approval-before-send, signature/link validation, and short direct templates.

For Fullfilled Foods revenue-stream CRM building and lead-database structure, load `references/fullfilled-foods-revenue-crm.md`. It covers the five revenue lanes, CRM schema, prioritization, public lead sourcing, community-directory cautions, and CTA by channel.

## Output Format
- Subject line
- Body with greeting and closing
- One clear call to action
- Brief note on placeholders or optional adjustments (keep this short)

## Relationship-Risk Drafts for Existing Clients

Use this when drafting replies to complaints, frustration, repeated delivery problems, quality issues, price confusion, or signs of reduced trust.

**Level 3 Relationship Risk = Soft + Solution-Oriented + Supervised**

Formula:
```text
Acknowledge → Own → Offer Solution → Ask Preference → Track
```

Rules:
- Soft tone first; acknowledge the client's experience before explaining.
- Do not blame suppliers, drivers, policy, or logistics.
- Do not over-explain; keep it practical.
- Include at least one concrete solution or next step that reduces recurrence.
- Ask the client preference when appropriate.
- Mark the draft as requiring supervision/approval before sending.

Example:
> “I’m sorry about that — I understand how frustrating it is when the delivery window isn’t consistent. We’ll look at this on our end, and one option is to move your drop-off earlier going forward so there’s more buffer. Would that work better for you?”

## Selva Market Letter / Newsletter Drafts

When drafting the Selva weekly newsletter, treat it as a branded market note, not cold outreach.

Rules:
- Draft only; do not send or create Gmail sends unless Lorenzo explicitly approves.
- Use subscriber-facing copy with internal notes separated below.
- No raw competitor/Natoora archive quantities or account names in public copy.
- Grower/farm names should come from Lorenzo’s INBOUND Sheet. If the INBOUND Sheet is unavailable, use placeholders and ask for the sheet link/name — do not invent growers.
- Prefer organic/minimal-intervention/regenerative/no-spray/low-input growers from INBOUND.
- Be specific with varieties: write “Cara Cara,” “Meyer lemon,” “Oro Blanco,” “Nagami kumquat,” “finger lime,” etc., not generic “citrus.”
- Include why it matters on the plate/bar: acidity, peel/oil, color, aroma, texture, menu use.

Suggested structure:
1. This Week’s Market Read
2. Product Window
3. Grower/Farm Note
4. Chef Note / Bar Note
5. Miami Watch Items
6. Availability / Samples
7. Quiet CTA

## Selva Distribution / Procurement Messaging

When drafting Selva/Cosecha distribution strategy copy, onboarding messages, case studies, or LinkedIn posts for chefs/operators/F&B/procurement decision makers, load `references/selva-distribution-messaging.md`. It captures the stable Selva-set sourcing rhythm, demand aggregation flywheel, budget-matching tradeoffs, local-first sourcing ladder, trust language, and LinkedIn/case-study patterns. Key correction: do **not** position cadence as custom per chef; Selva sets the rhythm and chefs adhere to it.

## Selva Market Letter / Branded Newsletter Drafts

Use this when Lorenzo asks for a subscriber-facing weekly market letter. This is **not outreach** unless he explicitly approves a send.

Rules:
- Draft as if a chef/operator subscriber is reading it, but label it clearly as a draft when responding in chat.
- Do not send, create Gmail drafts, or add recipients automatically.
- Do not expose raw competitor data, archive quantities, or Natoora account names.
- Use INBOUND/vendor-facing product list growers where possible; do not invent farms.
- Preferred style: named varieties + grower/place + practical chef/bar use. Example: “Meyer lemon — Regenerative Farm, Exeter, CA”, not “citrus.”
- Avoid generic hype: no “premium”, “high-quality”, “best-in-class.”
- CTA should be quiet: “Reply and I’ll send what’s actually available.”

## Closing
Always sign off:
  Best regards,
  Lorenzo
  Selva Partners

## Sending Infrastructure (confirmed working May 2026)

Two Gmail accounts authorized and tested via Gmail API:
- `lorenzo.belpassi@selva-partners.com` → token: ~/.hermes/selva_outreach_token.pickle
- `chloe.sanchez@selva-partners.com` → token: ~/.hermes/chloe_outreach_token.pickle

Both use: ~/.hermes/selva_outreach_credentials.json (project: selva-outreach, Desktop app)
To send programmatically — see selva-deal-log-agent skill for Gmail API send pattern.

9 approved outreach sequences (Alapattah wholesale, cruise lines, hotels/resorts) are in:
  selva-deal-log-agent skill → references/outreach-prospects.md

## Approved Example

Subject: The Heirloom Tomato You've Been Missing

Dear [Name],

Most tomatoes are an afterthought. This one isn't.

I've sourced a small allocation of dry-farmed heirloom tomatoes — harvested to order, delivered within 48 hours. The flavour is what tomatoes tasted like before yield and shelf life became the priority.

Interested? I can have a selection with you this week.

Best regards,
Lorenzo
Selva Partners
