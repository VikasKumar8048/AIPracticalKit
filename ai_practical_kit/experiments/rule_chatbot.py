"""Experiment 10: Rule-based chatbot with regular-expression matching."""

import random
import re

RULES = [
    (r"\b(hi|hello|hey)\b", ["Hello! How can I help you?", "Hi! Nice to meet you."]),
    (r"\bhow are you\b", ["I am fine, thank you!", "I am doing great!"]),
    (r"\b(admission|apply|application)\b", ["Please check the college admission portal."]),
    (r"\b(fee|fees|tuition)\b", ["Please check the college fee portal."]),
    (r"\b(library|books?)\b", ["Please check the college library."]),
    (r"\b(hostel|accommodation)\b", ["Please contact the student affairs office."]),
    (r"\b(thanks|thank you)\b", ["You are welcome!", "Happy to help!"]),
    (r"\b(bye|goodbye|exit|quit)\b", ["Goodbye! Have a nice day!"]),
]


def respond(text):
    """Return a rule-based response for a user message."""
    text = text.strip()

    # AND rule: both an admission topic and a fee topic must be present.
    has_admission = re.search(r"\b(admission|apply|application)\b", text, re.I)
    has_fees = re.search(r"\b(fee|fees|tuition)\b", text, re.I)
    if has_admission and has_fees:
        return "Check the admission portal AND the fee portal."

    for pattern, replies in RULES:
        if re.search(pattern, text, re.I):
            return random.choice(replies)

    return "Sorry, I do not understand your question."


def run_cli():
    print("\nEXPERIMENT 10: RULE-BASED CHATBOT")
    print("Ask about greetings, admission, fees, library or hostel.")
    print("Type bye to stop.")
    while True:
        user = input("You: ")
        print("Bot:", respond(user))
        if re.search(r"\b(bye|goodbye|exit|quit)\b", user, re.I):
            break


if __name__ == "__main__":
    run_cli()
