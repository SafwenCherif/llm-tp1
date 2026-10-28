import requests

API_URL = "http://localhost:11434/api/chat"

payload = {
    "model": "qwen3:1.7b",
    "messages": [
        {"role": "user", "content": "Explique le machine learning en deux phrases."}
    ],
    "stream": False,
    "think": False,
}

response = requests.post(API_URL, json=payload, timeout=180)
response.raise_for_status()
data = response.json()

print("Réponse :", data["message"]["content"])
print("Code HTTP :", response.status_code)
