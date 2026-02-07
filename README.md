# 📚 Daily Exam Dose Bot

This is an automated Telegram bot that posts **important exam questions**
for:

- Class 11
- Class 12
- College 1st Year
- College 2nd Year
- College 3rd Year

### ✨ Features
- Auto-post every 1 hour using GitHub Actions
- Bengali subjects → Bengali post
- English subjects → English post
- Never repeats the same question
- Runs 100% FREE on GitHub

---

## 🔧 Setup

1. Create a Telegram bot using @BotFather
2. Add bot as **Admin** to your channel
3. Copy:
   - BOT_TOKEN
   - CHAT_ID

4. Go to GitHub Repo → Settings → Secrets → Actions  
   Add:
   - `BOT_TOKEN`
   - `CHAT_ID`

---

## ⏰ Auto Posting
Uses GitHub Actions cron:
- Runs every **1 hour**
- No server required
- Works year after year

---

## 📂 Important Files
- `bot.py` → main runner
- `subjects.json` → all classes & subjects
- `questions.json` → question bank
- `posted.json` → prevents duplicates

---

Made for students ❤️  
Free education for everyone.