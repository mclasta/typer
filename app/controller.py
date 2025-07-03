from app.text_utils import get_clipboard_text
from app.typer import human_type

def run_typing():
    text = get_clipboard_text()
    if not text:
        print("⚠️ Área de transferência vazia.")
        return
    print("✍️ Digitando...")
    human_type(text)
    print("\n✅ Finalizado!")
