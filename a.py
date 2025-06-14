import requests
import json
import time
import os

SERVER_URL = "http://fi11.bot-hosting.net:20295"  # <-- इसे अपने server IP से बदल देना

def read_comments_from_file(file_path):
    if not os.path.exists(file_path):
        print("❌ File not found.")
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def start_task():
    user_id = input("👤 Enter user_id: ")
    task_id = input("📌 Enter task_id: ")
    post_id = input("🔗 Enter post_id: ")
    resume_post_id = input("🔁 Enter resume_post_id (optional): ")
    cookie = input("🍪 Enter Facebook cookie: ")
    hater_name = input("😈 Enter hater_name prefix (optional): ")
    speed = int(input("⏱️ Delay between comments (in seconds): "))
    comment_file = input("📄 Enter path to comment.txt file: ")

    comments = read_comments_from_file(comment_file)
    if not comments:
        print("⚠️ No comments found. Aborting.")
        return

    payload = {
        "user_id": user_id,
        "task_id": task_id,
        "post_id": post_id,
        "resume_post_id": resume_post_id or None,
        "cookie": cookie,
        "hater_name": hater_name,
        "comments": comments,
        "speed": speed
    }

    try:
        r = requests.post(f"{SERVER_URL}/api/start", json=payload)
        print("✅", r.json())
    except Exception as e:
        print("❌ Error:", e)

def stop_task():
    user_id = input("👤 Enter user_id: ")
    task_id = input("📌 Enter task_id to stop: ")
    try:
        r = requests.post(f"{SERVER_URL}/api/stop", json={
            "user_id": user_id,
            "task_id": task_id
        })
        print("🛑", r.json())
    except Exception as e:
        print("❌ Error:", e)

def stop_all():
    user_id = input("👤 Enter user_id: ")
    try:
        r = requests.post(f"{SERVER_URL}/api/stop-all", json={
            "user_id": user_id
        })
        print("🛑", r.json())
    except Exception as e:
        print("❌ Error:", e)

def show_active():
    user_id = input("👤 Enter user_id: ")
    try:
        r = requests.get(f"{SERVER_URL}/api/active", params={"user_id": user_id})
        print("📊 Active Tasks:", r.json())
    except Exception as e:
        print("❌ Error:", e)

def main():
    while True:
        print("\n📲 Facebook Auto Comment Tool")
        print("1. 🚀 Start Commenting")
        print("2. 🛑 Stop Task")
        print("3. ❌ Stop All Tasks")
        print("4. 📊 Show Active Tasks")
        print("5. 🔚 Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            start_task()
        elif choice == "2":
            stop_task()
        elif choice == "3":
            stop_all()
        elif choice == "4":
            show_active()
        elif choice == "5":
            break
        else:
            print("⚠️ Invalid choice")

if __name__ == "__main__":
    main()
