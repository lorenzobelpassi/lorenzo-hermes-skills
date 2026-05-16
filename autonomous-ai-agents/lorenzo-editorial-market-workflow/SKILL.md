---
name: lorenzo-editorial-market-workflow
description: "Use when turning market intel, restaurant intel, and product signals into public-safe editorial drafts or revenue actions for Lorenzo across The Walk-In, Staff Meal, and Selva market-letter workflows."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [editorial, market-intel, selva, walk-in, staff-meal, newsletter, revenue-os, lead-bank]
    related_skills: [lorenzo-operating-lanes, selva-market-intel, email_drafter, company-operating-agents]
---

# Lorenzo Editorial + Market-to-Action Workflow

## Overview

This skill is for the seam between research, editorial, and business action.

Use it when a request is not just "write this" and not just "research this," but instead needs a workflow like this:

market signal -> sort into public-safe vs internal-only -> choose output lane -> produce either a draft, a CRM action, or both.

It is especially useful for Lorenzo because the same source material often feeds two different systems:
- public/editorial output: The Walk-In, Staff Meal, Selva market-letter drafts
- internal/business output: Market Signals, named-account actions, outreach ideas, pipeline moves

The core job is separation and routing.

## When to Use

Use this skill when Lorenzo asks for any of the following:
- turn market intel into a newsletter, column, or draft post
- turn restaurant/opening intel into either editorial angles or sales actions
- decide what belongs in The Walk-In vs Staff Meal vs Selva market letter
- convert research into account-specific actions for Selva/Cosecha
- use a shared lead bank to avoid duplicate research across agents
- create a public-safe draft from sensitive internal intelligence

Do not use this skill for:
- generic cold email writing with no research workflow attached
- pure market brief generation with no editorial or action-routing layer
- unrelated creative writing tasks

## Core Decision Tree

For each item, classify it before writing anything:

### A. Public-safe editorial angle
Use when the signal is useful to readers without exposing proprietary sales logic.

Examples:
- product window and why it matters on the plate or bar
- restaurant opening or menu shift with cultural relevance
- chef movement or neighborhood change with broader meaning
- seasonality note, sourcing philosophy, or small contrarian opinion

### B. Internal-only business signal
Use when the signal creates commercial advantage or exposes sensitive details.

Examples:
- named target account with takeover angle
- competitor account intelligence
- raw pricing edge or margin opportunity
- outreach sequence or lead qualification logic
- account-specific watchlists and recommendations

### C. Split output
Many items should become both:
- a softened, public-safe editorial angle
- a separate internal action note with named accounts, urgency, and next move

If in doubt, split it.

## Output Routing Rules

### The Walk-In
Use for Tuesday-style market/seasonality/openings intelligence.

Default characteristics:
- reader-first
- sharp point of view
- Miami food-world intelligence
- not generic listicle tone
- strong headline and section hooks
- public-safe only

Good inputs:
- product windows
- market signals with cultural or menu relevance
- notable openings / chef moves / neighborhood shifts
- subtle contrarian observations

### Staff Meal
Use for Friday-style restaurant recommendation / review / scene energy.

Default characteristics:
- first-person or close-to-experience where possible
- hospitality-aware
- less trade-data heavy
- more scene, feeling, room, dish, rhythm, service, use-case

Good inputs:
- restaurant leads that feel worth visiting
- review notes
- neighborhood shifts
- restaurant openings with actual point of view

### Selva Market Letter
Use for chef/operator subscriber-facing market notes.

Default characteristics:
- internal draft unless approved
- product-specific
- farm/grower/variety verified
- practical kitchen/bar use
- quiet CTA
- no raw competitor data

Good inputs:
- variety-specific product windows
- grower-backed sourcing notes
- quality/availability shifts
- menu-use guidance

### Selva/Cosecha Revenue Action
Use when the signal should move the business directly.

Default characteristics:
- named account or segment
- urgency
- action recommendation
- sample / quote / outreach / nurture / rescue move
- CRM-ready structure where possible

Good inputs:
- volatility or margin opportunities
- openings that map to target accounts
- competitor displacement opportunities
- product window that fits named buyers

## Shared Lead-Bank Workflow

When multiple agents exist, use this sequence:

1. start with shared context first
2. dedupe repeated items
3. classify each surviving item as:
   - publication angle
   - Staff Meal lead
   - Selva/Cosecha sales signal
   - product/seasonality note
   - verification queue
   - duplicate / already used
4. only then produce the final draft or action brief

Rule:
Fresh search is for verification or clear gaps, not for redoing yesterday's work.

## Writing Rules by Stage

### Stage 1: Signal capture
Write in bullets.
Do not force prose too early.

Fields to capture:
- signal
- source
- confidence
- why it matters
- public-safe? yes/no
- editorial lane
- business lane
- next action

### Stage 2: Separation
Make two buckets:
- public-safe material
- internal-only material

Never let raw competitor/account intelligence leak into public output.

### Stage 3: Final pass
Only now decide the final form:
- editorial draft
- market-letter draft
- CRM note
- outreach suggestion
- combined package with separate sections

## Market-to-Action Conversion Pattern

When the user asks for something like "what do we do with this?", end with a short operating block:

- What happened
- Why it matters
- Who to target
- What to send / say / sample
- What needs Lorenzo approval

If there is no named action, keep working.

## Guardrails

- Draft-first by default.
- Separate editorial and internal business layers clearly.
- Do not invent growers, farms, named accounts, or sourcing claims.
- For public-facing copy, strip out raw competitor data, private pricing edges, and account-sensitive intelligence.
- For Selva market letters, use verified farms/growers and product windows only.
- For The Walk-In and Staff Meal, preserve voice and point of view; do not flatten into generic newsletter prose.
- When a signal can create revenue action, note the action even if the user asked for an editorial draft.

## Common Pitfalls

1. Writing too early.
Classify first. Draft second.

2. Mixing public and internal intelligence.
Keep them in visibly separate sections.

3. Letting market intel remain abstract.
Every strong signal should become either a draft input or an operating action.

4. Using generic Miami food writing.
The Walk-In and Staff Meal need taste, friction, and specificity.

5. Treating Selva market letters like sales emails.
They should read like informed buyer notes, not pitches.

## Verification Checklist

- [ ] I classified the item before drafting
- [ ] I separated public-safe from internal-only material
- [ ] I chose the right lane: Walk-In, Staff Meal, Selva market letter, or revenue action
- [ ] Any public-facing copy removes sensitive competitor/account intelligence
- [ ] Any business-facing output ends with a concrete next move
- [ ] Anything needing approval is clearly marked
