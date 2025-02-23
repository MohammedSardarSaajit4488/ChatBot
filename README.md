# Use and Learn Chatbot

![Chatbot interface showing a conversation](https://github.com/MohammedSardarSaajit4488/ChatBot/blob/main/chatbot%20project/image.png) <!-- Add a screenshot if you have one -->

A simple, web-based chatbot built with Flask that learns responses from users dynamically. Featuring a modern UI with gradients, animations, and a clean aesthetic, this chatbot is perfect for educational purposes or casual interaction.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Interactive Chat**: Real-time text-based conversation with a sleek interface.
- **Dynamic Learning**: Teaches itself new responses when encountering unknown messages.
- **Persistent Storage**: Saves learned responses in a JSON file (`chatbot_knowledge.json`).
- **Modern UI**: Gradient backgrounds, fade-in animations, and custom scrollbars.
- **User-Friendly**: Supports Enter key and button clicks for sending messages, with visual feedback (e.g., thinking dots).

## Prerequisites
- **Python**: Version 3.6 or higher (`python --version` to check).
- **Flask**: Python web framework (`pip install flask`).
- **Web Browser**: Chrome, Firefox, or any modern browser.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/use-and-learn-chatbot.git
   cd use-and-learn-chatbot
   Install Dependencies:

### Install Dependencies:

-pip install flask
Verify Setup: Ensure app.py and the templates folder with index.html are in the root directory.

### Usage

   -Run the Application:
   -python app.py
   -The server starts at http://127.0.0.1:5000.
   -Open your browser and navigate to this URL.

## Interact with the Chatbot:

   -Type a message (e.g., "hi") and press Enter or click "Send".
   -If the bot doesn’t know a response, it will ask, "I don’t know that yet. What should I say?"
   -Teach it by typing a response (e.g., "Hello there!").
   -The bot will confirm with "Thanks for teaching me!" and remember the response.
   -Type "exit" to end the conversation.

## Check the Knowledge Base:

Learned responses are saved in chatbot_knowledge.json in the project root.

### Project Structure

   -use-and-learn-chatbot/
   ├── app.py                # Flask backend and chatbot logic
   ├── templates/
   │   └── index.html        # HTML with embedded CSS and JavaScript
   ├── chatbot_knowledge.json # Persistent storage for learned responses (auto-generated)
   └── README.md             # This file
   -Contributing
   -Fork the repository.

## Create a feature branch:

   -git checkout -b feature/your-feature
## Commit your changes:

   -git commit -m "Add your feature"

## Push to the branch:
   -git push origin feature/your-feature
   -Open a pull request.
   -Feel free to suggest improvements, such as:
   - Multi-user support
   -Advanced learning algorithms
   -Additional UI themes

## License

   -This project is licensed under the MIT License. See the LICENSE file for details. <!-- Add a LICENSE file if you choose to include one -->

Developed by: Mohammed Sardar Saajit

Last Updated: February 23, 2025
