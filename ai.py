import requests
import json

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": ""
}

data = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "user", "content": "Объясни, что такое токен в LLM"}
    ]
}

response = requests.post(url, headers=headers, json=data)

result = response.json()

print(result["choices"] [0] ["message"] ["content"])