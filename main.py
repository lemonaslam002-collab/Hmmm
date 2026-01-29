from brain import get_response

print("AI: Hello. I'm online. Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("AI:", response)

    if "bye" in user_input.lower():
        break
