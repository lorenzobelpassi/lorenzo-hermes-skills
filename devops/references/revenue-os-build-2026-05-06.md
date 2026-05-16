# Selva Revenue OS Build — 2026-05-06

Session outcome: built the first local Selva Revenue Operating System package to turn the existing agents into one account-based revenue loop.

## Code location

`/Users/lorenzobelpassi/selva-agents/revenue_os/`

Key files:
- `revenue_os/scoring.py` — lead/account scoring engine.
- `revenue_os/importer.py` — raw CSV → CRM-ready leads.
- `revenue_os/notion_schema.py` — target CRM blueprint.
- `revenue_os/command_center.py` — daily command-center text.
- `revenue_os/cli.py` — local CLI.
- `tests/test_revenue_os.py` — behavior tests.
- `run_tests.py` — no-pytest test runner because system Python lacked pytest.

## Generated outputs

- `exports/scored_miami_leads.csv`
- `exports/scored_miami_leads.json`
- `exports/crm_blueprint.md`
- `exports/crm_blueprint.json`
- `exports/daily_command.txt`
- `BUILD_NOTES.md`

Input lead file used:
- `/tmp/natoora_clients/Miami Cold Outreach - Raw.csv`

Result:
- 425 cleaned/scored leads at minimum score 55.

## Scoring model

100-point model:
- 30 buyer quality
- 20 product fit
- 15 geography
- 15 buying power
- 10 timing trigger
- 10 contactability

Tiers:
- A+ 85–100: Lorenzo touches personally.
- A 70–84: Chloe enriches, Lorenzo sends/calls.
- B 55–69: batch outreach or nurture.
- D below 55: ignore unless a specific trigger appears.

Lead lanes:
- Natoora takeover
- Michelin/JB/fine dining
- Luxury hotels/resorts
- Cruise/provisioning
- Alapattah/wholesale
- New openings
- Chef-direct

## CRM blueprint

Target CRM databases:
1. Accounts
2. Contacts
3. Opportunities
4. Interactions
5. Market Signals

Principle: Notion should be the source of truth. Market Intel creates signals; Lead Research creates qualified accounts; Pipeline Tracker creates daily follow-up drafts; Deal Log keeps interactions alive.

## Daily command center

The command center combines:
- Top 10 selling actions
- Follow-ups due today
- Stale pipeline
- Market signals to convert
- Visible pipeline vs $157K target
- Gap to target

Example command:

```bash
cd /Users/lorenzobelpassi/selva-agents/revenue_os
python3 -m revenue_os.cli command \
  --leads-json exports/scored_miami_leads.json \
  --opportunities-json exports/opportunities.json \
  --signals-json exports/market_signals.json \
  --out exports/daily_command.txt
```

## Useful commands

Run tests:

```bash
cd /Users/lorenzobelpassi/selva-agents/revenue_os
python3 run_tests.py
```

Regenerate CRM schema docs:

```bash
python3 -m revenue_os.cli schema --out-dir exports
```

Rescore the Miami CSV:

```bash
python3 -m revenue_os.cli score-csv "/tmp/natoora_clients/Miami Cold Outreach - Raw.csv" \
  --out exports/scored_miami_leads.csv \
  --min-score 55
```

## Critical caveat

Do not send outreach directly from `scored_miami_leads.csv`. It is a first-pass machine ranking and requires enrichment/verification:
- Verify whether email belongs to the actual restaurant/buyer.
- Identify chef/buyer/owner.
- Remove remaining chains/off-strategy accounts.
- Add product-specific opening angle.
- Assign owner and next action date.

## Recommended next step

Before importing into Notion, confirm whether to create a fresh CRM or migrate the existing Selva Deals database. Then:
1. Create the five CRM databases.
2. Import only top 100 A/A+ leads first.
3. Enrich contacts for top 25.
4. Convert top 10 into Opportunities with Next Action Dates.
5. Point Pipeline Tracker at Opportunities.
6. Feed Market Intel signals into Market Signals.
7. Generate one Daily Command every morning.
