def format_post(q):
    text = f"*Class:* {q['class']}\n"
    text += f"*Subject:* {q['subject']}\n"
    text += f"*Chapter:* {q['chapter']}\n"
    text += f"*Question:* {q['question']}\n"
    return text
