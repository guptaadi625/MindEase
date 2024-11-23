from groq import Groq
import json
from voice import record_voice

# def process_voice_input():
#     """Get voice input, convert it to text, and use it as chatbot input."""
#     user_input = record_voice()  # Record and recognize voice
#     if user_input:  # Check if voice was successfully converted to text
#         return user_input
#     else:
#         return "I couldn't understand that. Please try again."


def load_config():
    """Load the chat configuration from chat.json."""
    with open("chat.json", "r") as f:
        config = json.load(f)
    return config

def update_chat_json(messages):
    """Update the messages in chat.json."""
    with open("chat.json", "r") as f:
        data = json.load(f)
    data["messages"] = messages
    with open("chat.json", "w") as f:
        json.dump(data, f, indent=4)

def get_response_from_api(messages, model, temperature, max_tokens, top_p, stream, stop):
    """Make an API call to Groq to get the chatbot's response."""
    client = Groq(
        api_key="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",
    )
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        stream=stream,
        stop=stop,
    )
    return completion.choices[0].message.content  # Access content directly


def chatbot():
    """Run the chatbot loop, allowing continuous interaction."""
    # Load initial configuration from chat.json
    config = load_config()
    messages = config["messages"]
    model = config["model"]
    temperature = config["temperature"]
    max_tokens = config["max_tokens"]
    top_p = config["top_p"]
    stream = config["stream"]
    stop = config["stop"]

    print("Hello! I'm here to help. Type 'exit' anytime to end the conversation.")
    # print("Type 'voice' to use voice input.")

    while True:
        # Get input from the user
        user_input = input("You: ")

        # Check if the user wants to end the conversation
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Take care.")
            break  # Exit the loop
#changes
        # if user_input.lower() == "voice":
        #     user_input = process_voice_input()
#changes

        # Add user's message to the messages list
        new_user_message = {"role": "user", "content": user_input}
        messages.append(new_user_message)

        # Make an API call to get the response
        assistant_response = get_response_from_api(
            messages, model, temperature, max_tokens, top_p, stream, stop
        )

        # Print the assistant's response
        print(f"Chatbot: {assistant_response}")

        # Add assistant's response to the messages list
        new_assistant_message = {"role": "assistant", "content": assistant_response}
        messages.append(new_assistant_message)

        # Update the chat.json file with the latest messages
        update_chat_json(messages)

# Run the chatbot
chatbot()