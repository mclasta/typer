import re
import unicodedata

def sanitize_text(text: str) -> str:
    text = text.replace('\t', ' ')
    text = re.sub(r'[ \t]+\n', '\n', text)
    text = re.sub(r'\n[ \t]+', '\n', text)
    text = re.sub(r' {2,}', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def normalize_chars(text: str) -> str:
    replacements = {
        '“': '"', '”': '"', '‘': "'", '’': "'",
        '–': '-', '—': '-', '−': '-',
        '…': '...',
        '\u00A0': ' ',  # espaço não separável
    }
    for src, tgt in replacements.items():
        text = text.replace(src, tgt)
    return unicodedata.normalize("NFKC", text)
