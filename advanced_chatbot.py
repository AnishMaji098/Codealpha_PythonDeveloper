import ast
import operator
import random
from datetime import datetime


# Safe arithmetic operations supported by the calculator.
_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def safe_calculate(expression):
    """Evaluate basic arithmetic without using eval()."""
    def evaluate(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in _OPERATORS:
            left = evaluate(node.left)
            right = evaluate(node.right)

            # Avoid excessively large exponentiation.
            if isinstance(node.op, ast.Pow) and abs(right) > 8:
                raise ValueError("Exponent is too large.")

            return _OPERATORS[type(node.op)](left, right)

        if isinstance(node, ast.UnaryOp) and type(node.op) in _OPERATORS:
            return _OPERATORS[type(node.op)](evaluate(node.operand))

        raise ValueError("Only basic arithmetic is allowed.")

    tree = ast.parse(expression, mode="eval")
    return evaluate(tree.body)


class AdvancedChatbot:
    def __init__(self):
        self.user_name = None
        self.history = []
        self.running = True

        self.jokes = [
            "Why did the computer go to the doctor? It had a virus!",
            "Why was the math book sad? It had too many problems.",
            "What do computers like to eat? Microchips!"
        ]

        self.responses = {
            "greeting": (
                ["Hello! Great to meet you.", "Hi there! How can I help?",
                 "Hey! It's nice to chat with you."]
            ),
            "thanks": ["You're welcome!", "Happy to help!", "Anytime!"],
            "goodbye": ["Goodbye! Have a wonderful day.", "See you later!"],
            "feeling": ["I'm doing great, thanks for asking!",
                        "I'm fine and ready to chat with you!"],
            "creator": ["I was created as a Python rule-based chatbot project."]
        }

    def remember(self, user_message, bot_reply):
        self.history.append(("You", user_message))
        self.history.append(("ChatBot", bot_reply))

    def respond(self, user_message):
        message = user_message.strip()
        normalized = message.lower()

        if not message:
            return "Please type a message so we can chat."

        # Exit commands
        if normalized in {"bye", "goodbye", "exit", "quit"}:
            self.running = False
            return random.choice(self.responses["goodbye"])

        # Help
        if normalized in {"help", "what can you do", "commands"}:
            return (
                "Here are some things you can try:\n"
                "- Say hello or ask how I am.\n"
                "- Type 'my name is Alex' so I can remember your name.\n"
                "- Ask 'what is my name?'.\n"
                "- Ask for the date or time.\n"
                "- Type 'calculate 12 * (5 + 2)' for arithmetic.\n"
                "- Type 'tell me a joke'.\n"
                "- Type 'history' to review this chat.\n"
                "- Type 'bye' to exit."
            )

        # Personalization: remember the user's name.
        if normalized.startswith("my name is "):
            name = message[11:].strip()
            if name:
                self.user_name = name.title()
                return f"Nice to meet you, {self.user_name}! I'll remember your name during this session."
            return "Please tell me your name after 'my name is'."

        if normalized in {"what is my name", "what's my name", "do you know my name"}:
            if self.user_name:
                return f"Your name is {self.user_name}."
            return "You haven't told me your name yet. Try: my name is Alex."

        # Date and time
        if normalized in {"time", "what time is it", "tell me the time"}:
            return "The current time is " + datetime.now().strftime("%I:%M:%S %p") + "."

        if normalized in {"date", "what is the date", "what's the date", "today's date"}:
            return "Today's date is " + datetime.now().strftime("%d %B %Y") + "."

        # Safe calculator
        if normalized.startswith("calculate "):
            expression = message[len("calculate "):].strip()
            try:
                result = safe_calculate(expression)
                return f"The answer is {result}."
            except (SyntaxError, ValueError, TypeError, ZeroDivisionError, OverflowError):
                return "I couldn't calculate that. Try a basic expression, such as: calculate 10 + 5 * 2."

        # Joke
        if normalized in {"tell me a joke", "joke", "make me laugh"}:
            return random.choice(self.jokes)

        # Conversation history
        if normalized == "history":
            if not self.history:
                return "There are no previous messages in this session."
            recent = self.history[-10:]
            return "Recent conversation:\n" + "\n".join(
                f"{speaker}: {text}" for speaker, text in recent
            )

        # Rule-based intent matching
        if normalized in {"hello", "hi", "hey", "good morning", "good afternoon", "good evening"}:
            reply = random.choice(self.responses["greeting"])
            if self.user_name:
                reply = reply.rstrip("!") + f", {self.user_name}!"
            return reply

        if "how are you" in normalized:
            return random.choice(self.responses["feeling"])

        if normalized in {"thank you", "thanks", "thx"}:
            return random.choice(self.responses["thanks"])

        if "who created you" in normalized or "who made you" in normalized:
            return self.responses["creator"][0]

        if "your name" in normalized:
            return "I'm Advanced ChatBot, a Python rule-based assistant."

        if "weather" in normalized:
            return "I can't check live weather, but you can ask me about the date, time, or basic calculations."

        return (
            "I'm not sure I understood that. Type 'help' to see what I can do, "
            "or try asking in a different way."
        )

    def save_history(self, filename="chat_history.txt"):
        with open(filename, "w", encoding="utf-8") as file:
            file.write("ADVANCED CHATBOT - CONVERSATION HISTORY\n")
            file.write("=" * 45 + "\n")
            for speaker, message in self.history:
                file.write(f"{speaker}: {message}\n")
        return filename

    def run(self):
        print("=" * 52)
        print("             ADVANCED PYTHON CHATBOT")
        print("=" * 52)
        print("Hello! I'm your rule-based assistant.")
        print("Type 'help' to see features or 'bye' to exit.\n")

        while self.running:
            user_message = input("You: ")
            bot_reply = self.respond(user_message)
            print(f"ChatBot: {bot_reply}\n")
            self.remember(user_message, bot_reply)

        # Save transcript when the conversation ends.
        filename = self.save_history()
        print(f"Conversation saved to '{filename}'.")
        print("Thanks for chatting. Goodbye!")


def main():
    chatbot = AdvancedChatbot()
    chatbot.run()


if __name__ == "__main__":
    main()
