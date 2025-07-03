import time
import random
import re
from pynput.keyboard import Controller, Key

kb = Controller()

def human_type(text: str, base_speed=0.03, burst_factor=0.5, typo_chance=0.05):
    tokens = tokenize(text)
    for token in tokens:
        if token.isspace():
            kb.type(token)
            delay_typing(token, base_speed, burst_factor)
            continue

        intended = token
        typed = ""
        for i, char in enumerate(token):
            if should_make_typo(char, typo_chance):
                wrong_char = get_typo(char)
                kb.type(wrong_char)
                typed += wrong_char
                delay_typing(char, base_speed, burst_factor)
                # Termina digitação com erro e corrige
                remaining = token[i+1:]
                time.sleep(random.uniform(0.3, 0.6))  # Simula pausa ao perceber erro
                backspace_n(len(typed))
                kb.type(token)
                delay_typing(char, base_speed, burst_factor)
                break
            else:
                kb.type(char)
                typed += char
                delay_typing(char, base_speed, burst_factor)
        else:
            # Se não houve erro, só pausa mais longo após token
            time.sleep(random.uniform(0.04, 0.1))

def tokenize(text: str):
    # Mantém palavras, espaços, quebras de linha e pontuações como tokens
    return re.findall(r'\s+|\w+|[^\w\s]', text, re.UNICODE)

def should_make_typo(char: str, chance: float) -> bool:
    return char.isalpha() and random.random() < chance

def get_typo(char: str) -> str:
    if not char.isalpha():
        return char
    offset = random.choice([-1, 1])
    if char.islower():
        return chr((ord(char) - ord('a') + offset) % 26 + ord('a'))
    else:
        return chr((ord(char) - ord('A') + offset) % 26 + ord('A'))

def backspace_n(n: int):
    for _ in range(n):
        kb.press(Key.backspace)
        kb.release(Key.backspace)
        time.sleep(random.uniform(0.01, 0.03))

def delay_typing(char: str, base_speed: float, burst_factor: float):
    if char == "\n":
        time.sleep(base_speed + random.uniform(0.15, 0.4))
    elif char.isspace():
        time.sleep(base_speed + random.uniform(0.04, 0.08))
    elif char in ".!?":
        time.sleep(base_speed + random.uniform(0.2, 0.5))
    else:
        factor = random.uniform(0.2, 0.5) if random.random() < burst_factor else random.uniform(0.8, 1.5)
        time.sleep(base_speed * factor)
