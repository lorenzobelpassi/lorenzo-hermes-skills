# Autonomous Editorial Cron Pattern

Use this when the user wants Hermes to act like a recurring editorial/research desk rather than waiting for one-off prompts.

## Pattern

Create scheduled Hermes cron jobs that generate **approval-ready drafts**, not automatic publications.

Good candidates:
- Weekly newsletter drafts.
- Restaurant/market intelligence briefs.
- Social post ideas.
- Lead-gathering research sweeps.
- Source/verification checklists.

## Recommended workflow

1. Define the publication/brand voice and recurring sections.
2. Create one cron job per recurring issue/column rather than one vague omnibus job.
3. Deliver to `origin` or the user's active messaging channel so the draft appears where they already work.
4. Enable only the toolsets required for the job, usually `web`, `terminal`, and `file` for editorial research/drafting.
5. In the prompt, explicitly state:
   - Do **not** publish automatically.
   - Produce a ready-to-edit draft.
   - Include source notes and uncertainty labels.
   - Do not invent named facts, people, venues, dates, menu items, prices, or sourcing details.
   - Human approval is required before sending/posting.
6. Save an operating doc in the project folder with job IDs, schedules, approval boundaries, and management commands.
7. Verify with `hermes cron list` that jobs are enabled and scheduled.

## Example commands

```bash
hermes cron create '0 8 * * 2'
# Then provide a prompt such as:
# "Every Tuesday, create a ready-to-edit issue draft. Do NOT publish anywhere. Deliver title options, subject lines, draft sections, and source notes."
```

When using the cron tool/API directly, set:
- `schedule`: cron expression such as `0 8 * * 2`
- `repeat`: forever/default
- `deliver`: `origin`, `discord`, `telegram`, or a specific gateway target
- `enabled_toolsets`: e.g. `["web", "terminal", "file"]`

## Editorial guardrails

Automatic drafting is useful; automatic publishing is usually risky unless there is a reliable first-party publishing API and the user has explicitly approved the workflow.

Keep humans in the loop for:
- Restaurant criticism.
- Claims about specific businesses/people.
- Pricing, sourcing, opening dates, or other facts that may change.
- Any externally published content under the user's brand.

## Example session outcome

For a Miami food publication, two jobs were created:
- Tuesday 8 AM ET: main market/product/openings issue draft.
- Friday 8 AM ET: restaurant recommendation column draft.

Both delivered to the originating Discord thread and included title options, subject lines, a Substack Note, markdown draft, and verification checklist. Nothing auto-published.