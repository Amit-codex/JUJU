import random

opening_text = [
    "Cool, I'm on it sir.",
    "Okay sir, I'm working on it.",
    "Just a second sir.",
]

def get_random_opening_text():
    """Returns a random statement from the opening_text list."""
    return random.choice(opening_text)
