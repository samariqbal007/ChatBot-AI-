import random

# Predefined mood-based responses
responses = {
    "sad": [
        "I'm sorry you're feeling down. Want to talk about it?",
        "You matter. Even if it doesn't feel like it right now.",
        "Tough times never last, but tough people do 💪"
    ],
    "anxious": [
        "Try taking a deep breath. Inhale... exhale...",
        "You're doing better than you think.",
        "Anxiety is real, but you're not alone. I'm here with you."
    ],
    "happy": [
        "That's wonderful! Tell me more about what's making you happy!",
        "Love to hear that! Keep smiling 😊",
        "Yay! Let’s celebrate the little wins 🎉"
    ],
    "angry": [
        "It’s okay to feel angry sometimes. Want to share what happened?",
        "Let’s talk it out calmly. I'm listening.",
        "You're strong for not bottling things up."
    ],
    "default": [
        "I'm here for you. Tell me more.",
        "I may be just a bot, but I care about how you feel.",
        "Want a motivational quote?"
    ]
}

def get_response(user_input):
    user_input = user_input.lower()

    # Keyword-based mood detection
    if "sad" in user_input or "depressed" in user_input or "down" in user_input:
        return random.choice(responses["sad"])
    elif "anxious" in user_input or "nervous" in user_input or "worried" in user_input:
        return random.choice(responses["anxious"])
    elif "happy" in user_input or "excited" in user_input or "joy" in user_input:
        return random.choice(responses["happy"])
    elif "angry" in user_input or "mad" in user_input or "frustrated" in user_input:
        return random.choice(responses["angry"])
    else:
        return random.choice(responses["default"])
