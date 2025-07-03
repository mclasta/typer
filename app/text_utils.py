import pyperclip
from app.cleaner import sanitize_text, normalize_chars

def get_clipboard_text() -> str:
    raw = pyperclip.paste()
    if not raw:
        return ""
    cleaned = sanitize_text(normalize_chars(raw))
    return cleaned
