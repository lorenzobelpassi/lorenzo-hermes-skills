# Selva Revenue Operating System

Session learning from May 6, 2026: Lorenzo does not just need separate agents; he needs one revenue operating loop that outputs who to see, what to say, what to sell, and what happens next.

## Core concept

The Selva agents should converge into a daily execution system:

Market Intel Agent → market signals
Lead Research / Revenue OS → scored accounts + contacts
Lead/Deal Capture Agent → interactions + CRM updates
Pipeline Tracker Agent → follow-ups + drafts
Daily Command → Lorenzo's action list
People To See → route-ready field sales list

The success metric is not “agent ran.” It is: did the system produce selling actions?

Every output should become one of:
- a person to see
- a person to call
- a draft to approve/send
- a sample/quote to prepare
- a stale opportunity to rescue
- a nurture/dead decision

## Local Revenue OS package

Built locally at:

```text
/Users/lorenzobelpassi/selva-agents/revenue_os
```

Important files:

```text
revenue_os/scoring.py              # 0-100 lead fit scoring
revenue_os/importer.py             # raw CSV → CRM-ready scored leads
revenue_os/notion_schema.py        # Accounts/Contacts/Opportunities/Interactions/Market Signals blueprint
revenue_os/command_center.py       # Daily Command text generator
revenue_os/visit_list.py           # People To See route/call sheet generator
run_tests.py                       # stdlib no-pytest runner
AUTOMATION_PLAYBOOK.md             # operating cadence + agent roles
PEOPLE_TO_SEE_PLAN.md              # implementation plan for Notion/import/wiring
```

Generated outputs:

```text
exports/scored_miami_leads.csv
exports/scored_miami_leads.json
exports/crm_blueprint.md
exports/crm_blueprint.json
exports/daily_command.txt
exports/people_to_see.md
exports/people_to_see.csv
```

## Lead scoring model

100-point model:
- 30 buyer quality
- 20 product fit
- 15 geography
- 15 buying power
- 10 timing trigger
- 10 contactability

Tiers:
- A+ 85-100: Lorenzo touches personally
- A 70-84: Chloe enriches; Lorenzo sends/calls
- B 55-69: batch outreach/nurture
- D <55: ignore unless specific trigger

Lead lanes:
- Natoora takeover
- Michelin/JB/fine dining
- Luxury hotels/resorts
- Cruise/provisioning
- Alapattah/wholesale
- New openings
- Chef-direct

## People To See logic

A lead becomes field-sales-ready when:
- fit score >= 70
- A or A+ tier
- routeable geography/address or contact path exists
- there is a product-specific opening angle

Priority order:
1. A+ accounts with active market signal
2. Natoora takeover targets
3. Michelin/JB/fine dining in dense zones
4. Warm/stale opportunities with due next action
5. Luxury hotels/resorts
6. Alapattah/wholesale tactical visits

Route buckets:
Miami Beach, Design District, Wynwood, Edgewater/Midtown, Brickell, Coconut Grove, Coral Gables, Aventura, Allapattah.

## Field spiel pattern

Keep it short, direct, and product-specific. Do not say “premium.”

Base:

```text
I’m Lorenzo with Selva Partners. I wanted to introduce myself because [ACCOUNT] looks like the kind of account we should be serving. Right now I’m focused on [PRODUCT ANGLE]. I work with chefs who care about what actually shows up in the box. If I bring you a tight list this week, who is the right person to show it to?
```

Natoora takeover variant:

```text
I’m Lorenzo with Selva Partners. I wanted to introduce myself because [ACCOUNT] looks like the kind of account we should be serving. Right now I’m focused on [PRODUCT ANGLE]. I know the kind of produce standard you are used to. I am building a tighter Miami source with better responsiveness. If I bring you a tight list this week, who is the right person to show it to?
```

## Commands

```bash
cd /Users/lorenzobelpassi/selva-agents/revenue_os
python3 run_tests.py
python3 -m revenue_os.cli score-csv "/tmp/natoora_clients/Miami Cold Outreach - Raw.csv" --out exports/scored_miami_leads.csv --min-score 55
python3 -m revenue_os.cli command --leads-json exports/scored_miami_leads.json --opportunities-json exports/opportunities.json --signals-json exports/market_signals.json --out exports/daily_command.txt
python3 -m revenue_os.cli visit-list --leads-json exports/scored_miami_leads.json --signals-json exports/market_signals.json --max-visits 15 --min-score 70 --out-md exports/people_to_see.md --out-csv exports/people_to_see.csv
```

## Caveat

The scored CSV is not approved for blind outbound. Some raw lead emails are bad or unrelated (e.g. ADP-style emails). Use the scored list to decide who to see/research; verify contact names and emails before sending production outreach.

## Next build sequence

1. Create five Notion CRM databases: Accounts, Contacts, Opportunities, Interactions, Market Signals.
2. Import top 100 A/A+ leads only.
3. Enrich top 25 contacts.
4. Convert top 10 into Opportunities with next action dates.
5. Point Pipeline Tracker at Opportunities.
6. Feed Market Intel signals into Market Signals.
7. Deliver Daily Command + People To See every morning.
