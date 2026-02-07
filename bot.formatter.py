from datetime import datetime
from bot.language import is_bangla

def format_post(class_name, subject, question):
    now = datetime.now().strftime("%d %b %Y | %I:%M %p")

    if is_bangla(subject):
        return f"""📚 Daily Exam Dose | Important Suggestion

🎓 {class_name}
📘 বিষয়: {subject}

❓ {question}

📝 সাজেশন: খুবই গুরুত্বপূর্ণ
🕒 {now}
"""
    else:
        return f"""📚 Daily Exam Dose | Important Suggestion

🎓 {class_name}
📘 Subject: {subject}

❓ {question}

📝 Suggestion: Very Important
🕒 {now}
"""