
def chatbot():
    print("=" * 35)
    print("       BASIC PYTHON CHATBOT")
    print("=" * 35)
    print("Hello! I am your chatbot.")
    print("You can say: hello, how are you, or bye.")

    while True:
        user_input = input("\nYou: ").lower().strip()

        if user_input == "hello":
            print("Bot: Hi!")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
