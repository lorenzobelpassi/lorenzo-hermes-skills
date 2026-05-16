# Notion API Client v3 Breaking Change

## Problem

`notion-client>=3.0.0` changed the API surface. Code using `notion.databases.query(**query)` fails with:

```
AttributeError: 'DatabasesEndpoint' object has no attribute 'query'
```

## Solution

**Option 1: Use httpx directly (recommended)**

Avoids library version churn entirely:

```python
import os
import httpx

NOTION_API_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

def _headers() -> dict:
    return {
        "Authorization": f"Bearer {os.environ['NOTION_API_KEY']}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }

def query_database(db_id: str, filter_payload: dict) -> list[dict]:
    results = []
    cursor = None
    with httpx.Client(timeout=30.0) as http:
        while True:
            payload = {**filter_payload}
            if cursor:
                payload["start_cursor"] = cursor
            resp = http.post(
                f"{NOTION_API_URL}/databases/{db_id}/query",
                headers=_headers(),
                json=payload,
            )
            resp.raise_for_status()
            data = resp.json()
            results.extend(data.get("results", []))
            if not data.get("has_more"):
                break
            cursor = data.get("next_cursor")
    return results
```

**Option 2: Pin to notion-client<3.0.0**

```
pip install "notion-client>=2.2.1,<3.0.0"
```

## Filter Validation Errors

Notion API returns 400 with helpful messages for invalid filters:

```json
{
  "object": "error",
  "status": 400,
  "code": "validation_error", 
  "message": "select option \"Lost\" not found for property \"Status\". Available options: \"Initial Contact\", \"Quoted\", \"Negotiating\", \"Closed\", \"Dead\"."
}
```

**Always test filters against the actual database schema** — property names and select options are case-sensitive and must match exactly.

## Pipeline1 Implementation

The Pipeline1 agent (`~/selva-agents/pipeline1/notion_query.py`) uses the httpx approach. If deploying to Modal, no `notion-client` dependency needed — just `httpx>=0.27.0`.
