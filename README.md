# Rasa Chatbot Application

This application provides a real-time conversational interface powered by a Rasa server. Key features include Voice Input, Text-to-Speech (TTS), and customizable UI themes.

## Features

- **Text-to-Speech (TTS):** Automated reading of bot responses, which can be toggled in settings.
- **Voice Input:** Integration for speech-to-text messaging.
- **UI Customization:** Options to modify themes (e.g., blue, dark-blue, green) and fonts (e.g., Helvetica, Arial, Courier New).
- **Rasa Integration:** Communicates with a local Rasa server to process user intents and generate responses.
- **Session Management:** Easy navigation back to the welcome screen to reset configurations.

## Requirements

Ensure all dependencies listed in `requirements.txt` are installed to avoid runtime errors.

## Installation and Setup

1. Clone or download the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Rasa server:
   ```bash
   rasa run
   ```
4. Launch the application:
   ```bash
   python main.py
   ```

## Application Workflow

1. **Welcome Screen:** Configure settings or start the chat.
2. **Chat Interface:** Interact via text or voice.
3. **Processing:** Messages are sent to `http://localhost:5005` for processing by Rasa.
4. **Response:** The bot's response is displayed and optionally read aloud.

## Important Considerations

- The Rasa server must be active before starting the application.
- Ensure microphone permissions are granted for voice input functionality.
