import random

WORDS = ["python", "streamlit", "teacher", "student", "database", "cloud", "security"]

def choose_word():
    random_word = random.choice(WORDS)
    print(random_word)
    return random_word

def check_letter(secret_word, guessed_letters):
    return " ".join([ch if ch in guessed_letters else "_" for ch in secret_word])

def is_word_complete(secret_word, guessed_letters):
    return all(ch in guessed_letters for ch in secret_word)