import json, random, os, requests
from bot.formatter import format_post

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send_message(text):
    requests.post(BASE_URL, data={
        "chat_id": CHAT_ID,
        "text": text
    })

with open("questions.json", encoding="utf-8") as f:
    questions = json.load(f)

with open("posted.json", encoding="utf-8") as f:
    posted = json.load(f)

for cls in questions:
    for subject in questions[cls]:
        q = random.choice(questions[cls][subject])
        if q not in posted:
            msg = format_post(cls, subject, q)
            send_message(msg)
            posted.append(q)
            break
    break

with open("posted.json", "w", encoding="utf-8") as f:
    json.dump(posted, f, ensure_ascii=False)