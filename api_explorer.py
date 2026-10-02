import json
import urllib.request

API_URL = "https://dummyjson.com/quotes/random"
WEBHOOK_URL = "https://webhook.site/d7208d5b-9f54-4d98-9c56-2d7c3a3ad691"
HEADERS = {"User-Agent": "api-explorer/1.0", "Content-Type": "application/json"}

# Part 1: API call
req = urllib.request.Request(API_URL, headers=HEADERS)
response = urllib.request.urlopen(req)
data = json.loads(response.read().decode("utf-8"))
print(data)

# Part 2: Response ko file mein save karo
with open("quote.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
print("Saved to quote.json")

# Part 3: Webhook bhejo
body = json.dumps(data).encode("utf-8")
req = urllib.request.Request(WEBHOOK_URL, data=body, headers=HEADERS, method="POST")
resp = urllib.request.urlopen(req)
print("Webhook sent, status:", resp.status)