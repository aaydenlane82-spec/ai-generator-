import os, requests

def generate_upgrade(prompt):
    key = os.getenv("AI_API_KEY")
    if not key:
        return "Demo: Add AI_API_KEY secret for real AI"
    
    r = requests.post("https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        json={"model": "gpt-4o-mini", "messages": [{"role": "user", "content": prompt}], "max_tokens": 500})
    return r.json()["choices"][0]["message"]["content"]
