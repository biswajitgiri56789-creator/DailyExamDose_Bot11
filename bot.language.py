def is_bangla(text):
    return any('\u0980' <= ch <= '\u09FF' for ch in text)