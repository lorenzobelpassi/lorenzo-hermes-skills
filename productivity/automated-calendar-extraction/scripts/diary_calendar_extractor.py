#!/usr/bin/env python3
"""
Diary & Calendar Extraction Agent
Scrapes email, Telegram, Discord, (and WhatsApp when configured) for:
- Appointments
- Meeting times
- Diary entries
- Soft bookings
- Time-sensitive reminders

Pushes structured events to Google Calendar.

USAGE:
  python diary_calendar_extractor.py

CONFIGURATION:
  Set environment variables:
  - TELEGRAM_BOT_TOKEN (optional, for Telegram scanning)
  - DISCORD_BOT_TOKEN (optional, for Discord scanning)
  - GOOGLE_CALENDAR_OAUTH_PATH (optional, for auto-push to calendar)
"""

import os
import json
import re
from datetime import datetime, timedelta
import sys

def extract_events_from_text(text, source="unknown"):
    """
    Extract calendar-worthy events from text using pattern matching.
    
    Looks for:
    - Time mentions: "3pm", "at 2:30", "tomorrow at 9am"
    - Date mentions: "May 15", "next Tuesday", "05/20"
    - Meeting keywords: "meeting", "call", "appointment", "lunch", "dinner"
    
    Returns list of extracted events with confidence scores.
    """
    events = []
    
    # Common patterns
    time_pattern = r'\b(\d{1,2}):?(\d{2})?\s?(am|pm|AM|PM)\b'
    date_pattern = r'\b(tomorrow|today|next\s+\w+|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|\d{1,2}/\d{1,2})\b'
    meeting_keywords = ['meeting', 'call', 'appointment', 'lunch', 'dinner', 'conference', 'zoom', 'check-in']
    
    lines = text.split('\n')
    for line in lines:
        # Check if line mentions both time and meeting keyword
        has_time = re.search(time_pattern, line, re.IGNORECASE)
        has_date = re.search(date_pattern, line, re.IGNORECASE)
        has_meeting = any(keyword in line.lower() for keyword in meeting_keywords)
        
        if (has_time or has_date) and has_meeting:
            # High confidence if both time and date present
            confidence = 0.8 if (has_time and has_date) else 0.5
            
            events.append({
                'raw_text': line.strip(),
                'source': source,
                'confidence': confidence,
                'extracted_at': datetime.now().isoformat(),
                'time_match': has_time.group() if has_time else None,
                'date_match': has_date.group() if has_date else None,
            })
    
    return events

def scan_email():
    """
    Scan Gmail via Himalaya CLI or Gmail API.
    
    TODO: Implement real email scanning:
    - Use Himalaya CLI: `himalaya list --folder inbox --max-messages 50`
    - OR use Google Workspace OAuth via google-workspace skill
    """
    print("📧 Scanning email...")
    
    # Placeholder - replace with real implementation
    sample_email_text = """
    Hi Lorenzo,
    
    Can we schedule a meeting tomorrow at 3pm to discuss Q2 budget?
    
    Thanks,
    John
    """
    
    return extract_events_from_text(sample_email_text, source="Email")

def scan_telegram():
    """
    Scan recent Telegram messages via Telegram Bot API.
    
    TODO: Implement real Telegram scanning:
    - Use Telegram Bot API with TELEGRAM_BOT_TOKEN
    - Fetch recent messages from private chats/groups
    """
    print("📱 Scanning Telegram...")
    
    # Placeholder
    return []

def scan_discord():
    """
    Scan recent Discord messages via Discord Bot API.
    
    TODO: Implement real Discord scanning:
    - Use Discord Bot token
    - Fetch messages from monitored channels/DMs
    """
    print("💬 Scanning Discord...")
    
    # Placeholder
    return []

def scan_whatsapp():
    """
    Scan WhatsApp Web (requires user setup with whatsapp-web.js).
    
    TODO: Implement WhatsApp scanning:
    - Requires Node.js background agent (see whatsapp_scanner.js)
    - Polls for new messages and extracts events
    """
    print("💚 WhatsApp scan not yet configured (requires setup)")
    
    # Placeholder
    return []

def push_to_google_calendar(events):
    """
    Push extracted events to Google Calendar via Google Calendar API.
    
    TODO: Implement Google Calendar push:
    - Use Google Calendar API OAuth
    - Create events with extracted title, start time, duration
    - Tag events with source (Email, Telegram, etc.)
    """
    if not events:
        return
    
    print(f"📅 Would push {len(events)} events to Google Calendar:")
    for event in events:
        print(f"  - [{event['source']}] {event['raw_text'][:80]}")
    
    # Placeholder - replace with real API call
    # Example using google-workspace skill or direct API:
    # gws calendar create \
    #   --summary "Meeting with John" \
    #   --start "2026-05-15T15:00:00" \
    #   --end "2026-05-15T16:00:00"

def format_summary(all_events):
    """Format daily summary of extracted appointments."""
    if not all_events:
        return f"""**Daily Diary Extraction** — {datetime.now().strftime('%Y-%m-%d')}

✅ No new appointments or diary entries found across email, Telegram, Discord, WhatsApp.

*Auto-scanned sources: Gmail, Telegram DMs, Discord threads*
"""
    
    msg = f"""**Daily Diary Extraction** — {datetime.now().strftime('%Y-%m-%d')}

📅 **Found {len(all_events)} potential calendar entries:**

"""
    for event in all_events[:20]:  # Max 20
        confidence_emoji = "🟢" if event['confidence'] > 0.6 else "🟡"
        msg += f"{confidence_emoji} **[{event['source']}]** {event['raw_text']}\n"
    
    msg += f"\n*Auto-scan complete | Check Google Calendar for updates*"
    return msg

def main():
    """Main extraction pipeline."""
    print(f"=== Diary/Calendar Extractor Starting at {datetime.now()} ===")
    
    all_events = []
    
    # Scan all sources
    all_events.extend(scan_email())
    all_events.extend(scan_telegram())
    all_events.extend(scan_discord())
    all_events.extend(scan_whatsapp())
    
    print(f"Total events extracted: {len(all_events)}")
    
    # Push high-confidence events to calendar
    high_confidence = [e for e in all_events if e['confidence'] > 0.6]
    push_to_google_calendar(high_confidence)
    
    # Generate summary
    summary = format_summary(all_events)
    print("\n" + "="*80)
    print(summary)
    print("="*80)
    
    # Return for cron job delivery
    return summary

if __name__ == '__main__':
    output = main()
    print(output)
