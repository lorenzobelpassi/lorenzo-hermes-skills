---
name: automated-calendar-extraction
description: |
  Extract appointments, meetings, and diary entries from email, messaging platforms
  (Telegram, Discord, WhatsApp), and push structured events to Google Calendar.
  Use when user wants automated calendar management, appointment scraping, or
  zero-effort agenda creation.
  Trigger: "extract calendar", "scan appointments", "diary extraction", "auto-calendar"
allowed-tools: terminal, web, file, execute_code
version: 1.0.0
author: Hermes Agent
license: MIT
---

# Automated Calendar & Diary Extraction

## Overview

Automatically scan email, messaging platforms (Telegram, Discord, WhatsApp), and other text sources for calendar-worthy events—meetings, appointments, soft bookings, time-sensitive reminders—and push them to Google Calendar.

**Key Features:**
- Pattern-based event extraction (time, date, meeting keywords)
- Multi-source scanning (Gmail, Telegram, Discord, WhatsApp)
- Confidence scoring (high-confidence events auto-added, low-confidence flagged for review)
- Daily summary delivery via Telegram/Discord
- Google Calendar integration for seamless sync

---

## Prerequisites

### Required
```bash
pip install requests python-dateutil
```

### Optional (for WhatsApp Web)
```bash
npm install whatsapp-web.js
```

### API Access
- **Gmail:** Google Workspace OAuth or Himalaya CLI
- **Telegram:** Telegram Bot API token
- **Discord:** Discord Bot token
- **WhatsApp:** WhatsApp Web.js (requires local QR code scan once)
- **Google Calendar:** Google Calendar API OAuth

---

## Instructions

### Step 1: Configure Sources

**Enable email scanning (Gmail):**
```bash
# Using Himalaya CLI (if installed)
himalaya list --folder inbox --max-messages 50

# OR via Google Workspace skill/OAuth
# See google-workspace skill for setup
```

**Enable Telegram scanning:**
- Requires Telegram Bot API token
- Set as environment variable: `TELEGRAM_BOT_TOKEN`

**Enable Discord scanning:**
- Requires Discord Bot token
- Set as environment variable: `DISCORD_BOT_TOKEN`

**Enable WhatsApp scanning (optional):**
- Requires Node.js background agent (see `scripts/whatsapp_scanner.js`)
- Run once to authenticate via QR code
- Scans WhatsApp Web messages for calendar entries

### Step 2: Run Manual Extraction

```bash
python scripts/diary_calendar_extractor.py
```

**Output:**
```
=== Diary/Calendar Extractor Starting at 2026-05-14 07:00 ===
📧 Scanning email...
📱 Scanning Telegram...
💬 Scanning Discord...
💚 Scanning WhatsApp...
Total events extracted: 12

🟢 [Email] "Meeting with John tomorrow at 3pm to discuss Q2 budget"
🟢 [Telegram] "Lunch at Zuma Friday 1:30pm"
🟡 [Discord] "Call later today?"
...
```

### Step 3: Deploy as Daily Cron

```bash
hermes cronjob create \
  --name "Daily Diary & Calendar Extraction" \
  --schedule "0 7 * * *" \
  --script "scripts/diary_calendar_extractor.py" \
  --deliver "telegram" \
  --no-agent
```

---

## Event Extraction Logic

### Pattern Matching
Extracts events when text contains:
- **Time mention:** `3pm`, `at 2:30`, `09:00`, `tomorrow at 9am`
- **Date mention:** `tomorrow`, `next Tuesday`, `May 15`, `05/20`
- **Meeting keywords:** `meeting`, `call`, `appointment`, `lunch`, `dinner`, `conference`, `zoom`

### Confidence Scoring
- **High (≥0.7):** Time + date + meeting keyword → auto-add to calendar
- **Medium (0.4–0.6):** Only time or date + meeting keyword → flag for review
- **Low (<0.4):** Vague mention → ignore or log

### Example Matches
✅ `"Meeting with Sarah tomorrow at 3pm"` → High confidence  
✅ `"Lunch next Tuesday 1:30pm"` → High confidence  
🟡 `"Call later today"` → Medium confidence (no specific time)  
❌ `"We should meet soon"` → Low confidence (no time/date)

---

## Output

### Daily Summary (Telegram/Discord)
```
**Daily Diary Extraction** — 2026-05-14

📅 **Found 8 potential calendar entries:**

🟢 **[Email]** Meeting with John tomorrow at 3pm to discuss Q2 budget
🟢 **[Telegram]** Lunch at Zuma Friday 1:30pm
🟡 **[Discord]** Call later today?
🟢 **[WhatsApp]** Dentist appointment May 20 at 10am
...

*Auto-scan complete | Check Google Calendar for updates*
```

### Google Calendar Integration
High-confidence events (score ≥ 0.7) are automatically pushed to Google Calendar as:
- **Title:** Extracted meeting subject
- **Start time:** Parsed from text
- **Duration:** Default 1 hour (or extracted if specified)
- **Source:** Tagged with origin (Email, Telegram, etc.)

---

## Pitfalls

### Pattern Matching Limitations
- **Ambiguous dates:** "Next week" without day-of-week → requires current date context
- **Timezones:** Assumes user's local timezone unless explicitly stated
- **Relative time:** "In 2 hours" → requires current timestamp for conversion
- **Multi-event messages:** Single message with multiple meetings → may extract only first

### API Rate Limits
- **Gmail:** 250 quota units/user/second (reading messages = 5 units each)
- **Telegram:** 30 messages/second per bot
- **Discord:** 50 requests/second per bot

### False Positives
- **Past events:** "We had lunch yesterday at 1pm" → may incorrectly extract as future event
- **Hypotheticals:** "What if we meet at 3pm?" → may extract as real event

**Mitigation:**
- Filter out past dates/times
- Require imperative/declarative phrasing (not questions)
- Manual review for medium-confidence events

---

## Example Workflows

### Workflow 1: Daily Auto-Scan (Recommended)
1. Cron runs at 7 AM daily
2. Scans last 24 hours of email, messages
3. Extracts high-confidence events → auto-add to Google Calendar
4. Sends summary to Telegram with medium-confidence events flagged
5. User manually confirms/adds flagged events

### Workflow 2: Pre-Meeting Reminder Scrape
1. Run on-demand before weekly planning
2. Scans last 7 days of all sources
3. Generates full week agenda
4. Pushes to Notion database or Google Calendar

### Workflow 3: WhatsApp-Only Family Calendar
1. Dedicated WhatsApp group for family scheduling
2. Scanner monitors group only
3. Auto-adds all events with time/date to shared family Google Calendar

---

## Resources

- **Google Calendar API:** [https://developers.google.com/calendar/api/guides/overview](https://developers.google.com/calendar/api/guides/overview)
- **Telegram Bot API:** [https://core.telegram.org/bots/api](https://core.telegram.org/bots/api)
- **Discord.py:** [https://discordpy.readthedocs.io](https://discordpy.readthedocs.io)
- **WhatsApp Web.js:** [https://github.com/pedroslopez/whatsapp-web.js](https://github.com/pedroslopez/whatsapp-web.js)
- **python-dateutil:** [https://dateutil.readthedocs.io](https://dateutil.readthedocs.io)

See `scripts/diary_calendar_extractor.py` for working implementation.
See `scripts/whatsapp_scanner.js` for WhatsApp Web.js setup (Node.js).
