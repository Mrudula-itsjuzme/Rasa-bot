# Rasa Chatbot Application

A desktop chatbot interface powered by a local Rasa server, with voice input, text-to-speech, and customizable UI themes.

This project demonstrates an end-to-end conversational AI workflow: user input, intent processing through Rasa, bot response generation, and optional voice output.

---

## Project links and evidence

| Item | Link / Note |
|---|---|
| Repository | https://github.com/Mrudula-itsjuzme/Rasa-bot |
| Paper / reference | Conversational-AI application project; no paper attached |
| Demo video | Not uploaded yet |
| Deployment | Local desktop + local Rasa server workflow; no hosted deployment |
| Dataset note | Uses Rasa NLU/training data when configured locally; add sample intents/stories in a future update |
| Result screenshots | Add chat interface screenshots, voice input demo GIFs, and sample conversation screenshots under `docs/` or `screenshots/` |

---

## Features

- Rasa server integration
- text chat interface
- voice input support
- text-to-speech output
- theme customization
- font customization
- session reset through welcome screen
- local API communication through `http://localhost:5005`

---

## Application flow

```text
User Input
    ↓
Desktop Chat UI
    ↓
Rasa Server
    ↓
Intent + Response Handling
    ↓
Chat Output / Text-to-Speech
```

---

## Requirements

- Python 3.8+
- Rasa
- microphone permissions for voice input
- dependencies listed in `requirements.txt`

---

## Quick start

```bash
git clone https://github.com/Mrudula-itsjuzme/Rasa-bot.git
cd Rasa-bot

pip install -r requirements.txt
```

Start the Rasa server:

```bash
rasa run
```

Launch the app:

```bash
python main.py
```

---

## Important notes

- The Rasa server must be running before the app is launched.
- Voice input requires microphone access.
- The app expects the Rasa endpoint at `http://localhost:5005`.

---

## Tech stack

- Python
- Rasa
- Speech-to-text workflow
- Text-to-speech workflow
- Desktop GUI development

---

## Future improvements

- add screenshots of the chat interface
- add sample intents and stories
- include training instructions for the Rasa model
- add Docker setup for easier local deployment
- improve error handling when the Rasa server is offline

---

## Author

Built by [Pedamallu Sai Mrudula](https://github.com/Mrudula-itsjuzme) as part of a conversational-AI and chatbot-development portfolio.
