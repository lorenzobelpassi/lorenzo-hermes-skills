# Fallback Providers — Practical Notes

## Key Pitfalls

- `hermes fallback add` and `hermes model` are **interactive TUI pickers** with no CLI flags.
  For scripted/automated setup, edit `~/.hermes/config.yaml` directly.

- `hermes fallback add` opens an interactive picker that cannot be invoked non-interactively.
  Direct YAML edit is the only reliable non-interactive path.

- **Provider name must be `copilot`, not `githubcopilot`**: The string `githubcopilot` is not a
  recognized provider. It silently fails with "unknown provider 'githubcopilot'" in
  `gateway.error.log` and the fallback is skipped entirely. Use `copilot` everywhere
  (fallback_providers, delegation.provider).

- **`claude-haiku-3-5` is not a valid model name**: The correct versioned name is
  `claude-haiku-3-5-20241022`. Anthropic returns HTTP 404 for the unversioned alias, exhausting
  all 3 retry attempts before moving to the next fallback.

- **Delegation provider must also be `copilot`**: `delegation.provider` in config.yaml has the
  same issue — set it to `copilot`, not `githubcopilot`.

- **OpenRouter 401 "User not found"**: If the OpenRouter key returns 401, validate it at
  `https://openrouter.ai/api/v1/auth/key` with `Authorization: Bearer <key>`. A 401 means the
  key is invalid/revoked — generate a new one at openrouter.ai/keys. Note: `curl` exit code 43
  on macOS is a proxy/SSL interception issue; use Python's `urllib.request` to test the key
  instead.

## Verifying All Fallbacks Are Healthy

After setting up the chain, check gateway.error.log for any of these patterns:
- `unknown provider 'githubcopilot'` → rename to `copilot`
- `HTTP 404: model: claude-haiku-3-5` → use `claude-haiku-3-5-20241022`
- `HTTP 401: User not found` → OpenRouter key invalid, regenerate
- `Personal Access Tokens are not supported` → Copilot token is wrong type (see Copilot section)

## Setting Up OpenRouter as a Fallback

1. Set the API key in config (not just as an env var):
   ```bash
   hermes config set openrouter.api_key "sk-or-v1-..."
   ```

2. Edit `~/.hermes/config.yaml` to add the fallback entry:
   ```yaml
   fallback_providers:
     - provider: openrouter
       model: google/gemini-2.0-flash-exp
   ```

3. Verify with:
   ```bash
   hermes fallback list
   ```

## OpenRouter Model Name Format

OpenRouter models use `vendor/model-name` slash format regardless of which underlying provider serves them.
The `provider` field in config is always `openrouter`.

Examples:
- `google/gemini-2.0-flash-exp`
- `anthropic/claude-sonnet-4-5`
- `meta-llama/llama-3.1-70b-instruct`
- `openai/gpt-4o`

## Multiple Fallbacks

The chain is tried in order. You can stack multiple entries:
```yaml
fallback_providers:
  - provider: openrouter
    model: google/gemini-2.0-flash-exp
  - provider: anthropic
    model: claude-haiku-3-5
```

Docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/fallback-providers
