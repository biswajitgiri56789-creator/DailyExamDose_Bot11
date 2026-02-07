import json
import os
from bot.language import detect_language
from bot.formatter import format_post
from bot.post import send_to_telegram

# Load questions
with open("questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

# Load posted history
if os.path.exists("posted.json"):
    with open("posted.json", "r", encoding="utf-8") as f:
        posted = json.load(f)
else:
    posted = []

# Find first unposted question
for q in questions:
    qid = q["id"]
    if qid not in posted:
        message = format_post(q)
        send_to_telegram(message)
        posted.append(qid)
        # Save posted history
        with open("posted.json", "w", encoding="utf-8") as f:
            json.dump(posted, f, ensure_ascii=False, indent=2)
        break
