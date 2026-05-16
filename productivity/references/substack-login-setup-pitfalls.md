# Substack Login and Setup Pitfalls

Session learning: Substack setup via remote browser was repeatedly blocked by account authentication. The user's local iPhone/app/browser login did not authenticate the remote Browserbase/automation session.

## Key pitfalls

- Opening a Substack sign-in link on the user's iPhone signs in the iPhone app/browser only; it does not authenticate the remote browser session.
- Substack may email either a magic link or a “verification code” message, but the sign-in page may still only expose a link flow with no code input in the remote browser.
- Do not keep asking for the email if the user already gave it; Lorenzo's Substack/work email is `lorenzo.belpassi@selva-partners.com`.
- Avoid pasting live login codes into a Discord/server thread. Treat them as account credentials.
- If remote browser auth keeps failing, switch quickly to guided manual setup in the user's local Substack app/mobile browser.

## Best fallback workflow

1. Prepare paste-ready settings/copy/assets locally.
2. Tell the user to use Substack mobile web, not only the iPhone app, for full publication settings if the app hides controls.
3. Provide exact values for:
   - publication name
   - byline
   - tagline
   - About copy
   - website editor colors/assets/nav
   - launch post
4. Keep custom Astro code as a design source-of-truth, but translate it to Substack editor settings.

## Current The Walk-In auth/setup details

- Publication URL: `thewalkin305.substack.com`
- Account email: `lorenzo.belpassi@selva-partners.com`
- Public byline should not remain `Skwphmh`.
- Preferred byline after pivot: `renzlovespasta_305` or fallback `Lorenzo from The Walk-In`.
