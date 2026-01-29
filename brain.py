import random
import re
from memory import remember, recall

def clean_text(text):
    return re.sub(r"[^a-zA-Z ]", "", text.lower())

def get_response(user_input):
    text = clean_text(user_input)

    if "my name is" in text:
        name = text.replace("my name is", "").strip()
        remember("name", name)
        return f"Nice to meet you, {name}."

    if "how are you" in text:
        return "I'm functioning within acceptable parameters. You?"

    if "i am sad" in text or "i feel sad" in text:
        remember("mood", "sad")
        return "That sounds rough. Want to talk about it?"

    if "i am happy" in text:
        remember("mood", "happy")
        return "Good. Happiness is rare. Enjoy it."

    if "who are you" in text:
        return "I'm a simple AI chatbot. Not human. Not magic. Just code."

    if "what is my name" in text:
        name = recall("name")
        if name:
            return f"Your name is {name}."
        return "You never told me your name."

    if "bye" in text:
        return "Goodbye. Try not to break anything."

    return random.choice([
        "Interesting. Tell me more.",
        "I'm still learning. Explain that again.",
        "Humans say strange things sometimes.",
        "I don't fully understand, but I'm listening."
    ])
