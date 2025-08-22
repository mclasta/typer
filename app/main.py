from app.controller import run_typing
import keyboard
import time

def main():
    print("Copie um texto com Ctrl+C, depois clique onde quiser digitar.")
    print("Quando estiver pronto, pressione F9 para começar.")
    keyboard.wait("f9")
    time.sleep(1.5)
    run_typing()

if __name__ == "__main__":
    main()
