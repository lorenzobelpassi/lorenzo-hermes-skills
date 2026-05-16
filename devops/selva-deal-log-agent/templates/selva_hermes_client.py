"""
Selva Hermes Client
-------------------
Reusable Python interface to talk to the local Hermes agent via webhook.
Copy to project directory and import as needed.

HMAC header: X-Webhook-Signature (plain hex SHA-256)
"""

import hashlib
import hmac
import json
import time
import requests

WEBHOOK_URL    = "http://localhost:8644/webhooks/selva-agent"
WEBHOOK_SECRET = "NQ_VZHHwJ94T20RXVX8V8yjJ3PoJzRAO8DeA007WWuM"


class HermesClient:
    def __init__(self, url: str = WEBHOOK_URL, secret: str = WEBHOOK_SECRET):
        self.url    = url
        self.secret = secret

    def send(self, message: str, context: str = "", timeout: int = 30) -> dict:
        payload = json.dumps({
            "message": message,
            "context": context,
            "timestamp": time.time(),
        })
        signature = hmac.new(self.secret.encode(), payload.encode(), hashlib.sha256).hexdigest()
        try:
            r = requests.post(
                self.url,
                data=payload,
                headers={
                    "Content-Type": "application/json",
                    "X-Webhook-Signature": signature,  # NOT X-Hermes-Signature
                },
                timeout=timeout,
            )
            r.raise_for_status()
            return {"status": "ok", "response": r.text}
        except requests.exceptions.ConnectionError:
            return {"status": "error", "response": "Hermes gateway not running. Start: hermes gateway run"}
        except requests.exceptions.Timeout:
            return {"status": "error", "response": f"Timed out after {timeout}s"}
        except requests.exceptions.HTTPError as e:
            return {"status": "error", "response": str(e)}

    def health(self) -> bool:
        try:
            r = requests.get(self.url.rsplit("/webhooks", 1)[0] + "/health", timeout=5)
            return r.status_code == 200
        except Exception:
            return False


def ask_hermes(message: str, context: str = "") -> str:
    """One-liner helper."""
    return HermesClient().send(message, context)["response"]
