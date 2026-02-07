# bot.py
import json
import os
import random
from datetime import datetime

from bot_language import detect_language
from bot_formatter import format_post
from bot_post import send_to_telegram


SUBJECTS_FILE = "subjects.json"
QUESTIONS_FILE = "questions.json"
POSTED_FILE = "posted.json"


def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def pick_new_question(subjects, questions, posted):
    available = []

    for cls, cls_data in subjects.items():
        for subject in cls_data["subjects"]:
            key = f"{cls}::{subject}"
            qlist = questions.get(key, [])
            for q in qlist:
                uid = f"{key}::{q}"
                if uid not in posted:
                    available.append((cls, subject, q, uid))

    if not available:
        return None

    return random.choice(available)


def main():
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")

    if not BOT_TOKEN or not CHAT_ID:
        raise Exception("BOT_TOKEN or CHAT_ID missing")

    subjects = load_json(SUBJECTS_FILE, {})
    questions = load_json(QUESTIONS_FILE, {})
    posted = load_json(POSTED_FILE, [])

    picked = pick_new_question(subjects, questions, posted)

    if not picked:
        print("No new questions left")
        return

    cls, subject, question, uid = picked

    language = detect_language(subject)
    message = format_post(
        cls=cls,
        subject=subject,
        question=question,
        language=language,
        time=datetime.now().strftime("%d %B %Y | %I:%M %p")
    )

    send_to_telegram(BOT_TOKEN, CHAT_ID, message)

    posted.append(uid)
    save_json(POSTED_FILE, posted)

    print("Posted successfully:", uid)


if __name__ == "__main__":
    main()