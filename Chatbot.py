# main.py
def chatbot():
    print("🤖 Chatbot: Hello! I am a simple rule-based chatbot. Type 'bye' to exit.")
    while True:
        # Take user input
        user_input = input("You: ").lower().strip()
        # Rule-based responses
        if "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot: Hello! How can I help you today?")
        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm just code, but I'm doing great! 😃")
        elif "your name" in user_input:
            print("🤖 Chatbot: I'm a Codmetric Rule-Based Chatbot.")
        elif "bye" in user_input:
            print("🤖 Chatbot: Goodbye! Have a nice day 👋")
            break
        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")
# Run chatbot when script starts
if __name__ == "__main__":
    chatbot()
