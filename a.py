import requests
import json

# 🔧 API server ka URL
SERVER_URL = "fi11.bot-hosting.net:20295/api/start"  # <-- yaha apna IP daalo

# 📥 User se inputs lo
username = input("👤 Enter your username: ")
cookie = input("🍪 Enter your Facebook cookie: ")
post_id = input("📝 Enter target Post ID: ")
resume_post_id = input("🔄 Enter resume Post ID (press Enter to skip): ")
speed = int(input("⏱️ Delay between comments (in seconds): "))

# 🔁 Comment list
print("💬 Enter comments (enter 'END' to finish):")
comments = []
while True:
    c = input("> ")
    if c.upper() == 'END':
        break
    comments.append(c)

# 🧠 Task ID create kar do
import uuid
task_id = f"{username}_{str(uuid.uuid4())[:8]}"

# 📨 Request payload
payload = {
    "task_id": task_id,
    "post_id": post_id,
    "resume_post_id": resume_post_id if resume_post_id else None,
    "comments": comments,
    "speed": speed,
    "cookie": cookie,
    "username": username
}

# 🔥 POST request bhejo
try:
    response = requests.post(SERVER_URL, json=payload)
    print("✅ Server Response:", response.json())
except Exception as e:
    print("❌ Failed to connect to server:", str(e))
