from flask import Flask, request, render_template
import json

app = Flask(__name__)

# Load or initialize the chatbot's knowledge base
try:
    with open("chatbot_knowledge.json", "r") as f:
        knowledge_base = json.load(f)
except FileNotFoundError:
    knowledge_base = {}

# Global variable to track if we're waiting for a teaching response
teaching_mode = {"active": False, "last_message": ""}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    global teaching_mode
    user_message = request.json['message'].strip().lower()

    if user_message == "exit":
        response = "Goodbye!"
        teaching_mode = {"active": False, "last_message": ""}
    elif teaching_mode["active"]:
        # User is teaching the bot a response
        knowledge_base[teaching_mode["last_message"]] = user_message
        with open("chatbot_knowledge.json", "w") as f:
            json.dump(knowledge_base, f, indent=4)
        response = "Thanks for teaching me! I’ll remember that."
        teaching_mode = {"active": False, "last_message": ""}
    elif user_message in knowledge_base and knowledge_base[user_message]:
        response = knowledge_base[user_message]
    else:
        # New message, ask to teach
        knowledge_base[user_message] = ""  # Add to knowledge base with no response yet
        with open("chatbot_knowledge.json", "w") as f:
            json.dump(knowledge_base, f, indent=4)
        teaching_mode = {"active": True, "last_message": user_message}
        response = "I don’t know that yet. What should I say?"

    return {'response': response}

if __name__ == '__main__':
    app.run(debug=True)