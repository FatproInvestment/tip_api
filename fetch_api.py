import requests
import json

API_URL = "https://meme-backend.degate.com/api/metrics/tokens"

response = requests.get(API_URL)
data = response.json()

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
