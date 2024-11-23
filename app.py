from flask import Flask, render_template, request, jsonify
from main import load_config, update_chat_json, get_response_from_api
import re
app = Flask(__name__)

# Load initial configuration from chat.json
config = load_config()
messages = config["messages"]
model = config["model"]
temperature = config["temperature"]
max_tokens = config["max_tokens"]
top_p = config["top_p"]
stream = config["stream"]
stop = config["stop"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["message"]
    new_user_message = {"role": "user", "content": user_input}
    messages.append(new_user_message)

    # Get the assistant's response
    assistant_response = get_response_from_api(
        messages, model, temperature, max_tokens, top_p, stream, stop
    )
    assistant_response = bold_text_in_response(assistant_response)
    # Replace newline characters with <br> for HTML display
    assistant_response = assistant_response.replace("\n", "<br>")

    new_assistant_message = {"role": "assistant", "content": assistant_response}
    messages.append(new_assistant_message)

    update_chat_json(messages)

    return jsonify({"response": assistant_response})

def bold_text_in_response(assistant_response):
    # Regular expression to find text between ** and replace with <strong> tags
    bold_pattern = r"\*\*(.*?)\*\*"  # This captures text between ** and **
    assistant_response = re.sub(bold_pattern, r"<strong>\1</strong>", assistant_response)

    return assistant_response

if __name__ == "__main__":
    app.run(debug=True)



# def chat():
#     user_input = request.form["message"]
#     new_user_message = {"role": "user", "content": user_input}
#     messages.append(new_user_message)
#
#     assistant_response = get_response_from_api(
#         messages, model, temperature, max_tokens, top_p, stream, stop
#     )
#
#     new_assistant_message = {"role": "assistant", "content": assistant_response}
#     messages.append(new_assistant_message)
#
#     update_chat_json(messages)
#
#     return jsonify({"response": assistant_response})



#
# // JavaScript function to handle message sending and receiving response
#         const chatLog = document.getElementById("chat-log");
#         const chatForm = document.getElementById("chat-form");
#         const messageInput = document.getElementById("message");
#
#         chatForm.addEventListener("submit", (e) => {
#             e.preventDefault(); // Prevent form from refreshing the page
#             const message = messageInput.value.trim(); // Get the message from input
#             if (message) {
#                 // Display user's message in chat
#                 const userMessage = document.createElement("div");
#                 userMessage.className = "user-message";
#                 userMessage.textContent = message;
#                 chatLog.appendChild(userMessage);
#
#                 // Clear input field
#                 messageInput.value = "";
#
#                 // Scroll to the latest message
#                 chatLog.scrollTop = chatLog.scrollHeight;
#
#                 // Send the message to the server and get the bot's response
#                 fetch("/chat", {
#                     method: "POST",
#                     headers: { "Content-Type": "application/x-www-form-urlencoded" },
#                     body: `message=${encodeURIComponent(message)}`
#                 })
#                 .then((response) => response.json())
#                 .then((data) => {
#                     const response = data.response;
#
#                     // Display bot's response in chat
#                     const botMessage = document.createElement("div");
#                     botMessage.className = "bot-message";
#                     botMessage.textContent = response;
#                     chatLog.appendChild(botMessage);
#
#                     // Scroll to the latest message
#                     chatLog.scrollTop = chatLog.scrollHeight;
#                 })
#                 .catch((error) => {
#                     console.error("Error:", error);
#                     const errorMessage = document.createElement("div");
#                     errorMessage.className = "bot-message";
#                     errorMessage.textContent = "Oops! Something went wrong. Please try again.";
#                     chatLog.appendChild(errorMessage);
#                     chatLog.scrollTop = chatLog.scrollHeight;
#                 });
#             }
#         });