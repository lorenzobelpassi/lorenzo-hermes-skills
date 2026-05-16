# Lorenzo's Hermes Agent Skills

Curated collection of production-ready Hermes Agent skills for:
- **GitHub workflows** — auth, PRs, code review, issues, repo management
- **Software development** — systematic debugging, TDD, planning, subagent-driven dev
- **Selva/Cosecha operations** — market intel, brokerage signals, deal logging, outreach
- **Productivity** — Google Workspace, Notion, Obsidian, calendar automation
- **Content & editorial** — brand naming, humanizer, social media (X/Twitter)
- **DevOps** — static site deployment, webhooks, Kanban workflows

## Installation

```bash
# Install the skill hub CLI if you haven't already
hermes skills hub install

# Add this tap
hermes skills hub tap add lorenzobelpassi/lorenzo-hermes-skills

# Install specific skills
hermes skills hub install github-pr-workflow
hermes skills hub install systematic-debugging
hermes skills hub install lorenzo-operating-lanes

# Or install all from a category
hermes skills hub install --category github
hermes skills hub install --category software-development
```

## Skill Categories

### GitHub (5 skills)
- `github-auth` — Authentication setup: HTTPS tokens, SSH keys, gh CLI login
- `github-pr-workflow` — PR lifecycle: branch, commit, open, CI, merge
- `github-code-review` — Review PRs: diffs, inline comments, formal reviews
- `github-issues` — Create, triage, label, assign issues
- `github-repo-management` — Clone/create/fork repos, releases, secrets, workflows

### Software Development (7 skills)
- `systematic-debugging` — 4-phase root cause debugging: understand before fixing
- `writing-plans` — Implementation plans: bite-sized tasks, paths, code
- `test-driven-development` — TDD: enforce RED-GREEN-REFACTOR
- `requesting-code-review` — Pre-commit review: security scan, quality gates
- `subagent-driven-development` — Execute plans via delegate_task subagents
- `spike` — Throwaway experiments to validate ideas before building
- `plan` — Plan mode: write markdown plans without execution

### Selva/Cosecha Operations (5 skills)
- `lorenzo-operating-lanes` — Cross-workflow defaults: tools, guardrails, outputs
- `lorenzo-editorial-market-workflow` — Market intel → editorial drafts & revenue actions
- `selva-market-intel` — Daily produce market briefing via Modal cron
- `selva-brokerage-intel` — Brokerage/wholesale opportunity briefing
- `selva-deal-log-agent` — Plaud audio → transcription → Notion
- `email_drafter` — Professional email drafts for outreach and follow-ups

### Productivity (5 skills)
- `google-workspace` — Gmail, Calendar, Drive, Docs, Sheets via gws CLI
- `notion` — Notion API: pages, databases, blocks, search
- `automated-calendar-extraction` — Extract appointments from email/messaging → Calendar
- `personal-finance-operations` — Cash flow, Tiller/Sheets budgets, subscriptions
- `airtable` — Airtable REST API: records CRUD, filters, upserts

### Note-Taking (1 skill)
- `obsidian` — Read, search, create, edit notes in Obsidian vault

### Content & Editorial (3 skills)
- `editorial-brand-naming` — Develop names, taglines, section architecture
- `humanizer` — Strip AI-isms and add real voice
- `xurl` — X/Twitter via xurl CLI: post, search, DM, media

### DevOps (3 skills)
- `static-site-deployment` — Publish/repair static sites (Vercel/Cloudflare)
- `webhook-subscriptions` — Event-driven agent runs
- `kanban-worker` — Hermes Kanban worker pitfalls and lifecycle

### Autonomous AI Agents (2 skills)
- `hermes-agent` — Configure, extend, contribute to Hermes Agent
- `company-operating-agents` — Design company-managing agents: source of truth, intake, operating loops

## Contributing

These skills are maintained for my personal workflow but shared publicly. If you find a bug or have improvements:

1. Open an issue describing the problem
2. Submit a PR with the fix
3. I'll review and merge if it aligns with the skill's purpose

## License

MIT — Use freely, attribution appreciated.

## Author

Lorenzo Belpassi  
[Selva Partners](https://selva-partners.com)
