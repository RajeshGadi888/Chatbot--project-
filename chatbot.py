print("Hi! I am your chatbot. Type 'bye' to exit.")

while True:
    user = input("You: ")

    if user.lower() == "hello":
        print("Bot: Hi! How are you?")
    elif user.lower() == "how are you":
        print("Bot: I am fine 😊")
    elif user.lower() == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand 😅")