# Rasa-bot
This little app connects to a Rasa server to give you real-time conversations with some cool features like Voice Input, Text-to-Speech, and the ability to customize the theme and font. Whether you're in the mood to text or want to talk to the bot like it's your new BFF, this chatbot has you covered. 😏

📦 Features
Text-to-Speech (TTS): Let the chatbot speak to you! It's enabled by default, but you can turn it off in the settings.

Voice Input: Type less, talk more! Just click the mic, and speak to your bot.

Theme and Font Customization: Personalize the look and feel of your app with multiple themes and fonts.

Rasa Integration: The chatbot communicates with a Rasa server (running locally) to process messages and return responses.

Back to Welcome Screen: Always have a way to reset and change settings.

🖥️ Requirements
Before running the chatbot, make sure everything as per requirements.txt to ensure there are no dependency errors
🔧 Setup Instructions
Clone or download this repository to your local machine.

Install all the required dependencies mentioned above.

Make sure you have a Rasa server running locally at http://localhost:5005.

You can start it with:
#rasa run
Run the chatbot app by executing:
python main.py
📝 How it Works
Once you launch the app, you will see a Welcome Screen with options to start chatting.

Click on Start Chatting, and you’ll enter the Chat Screen where you can type or speak to the bot.

Messages are sent to a local Rasa server for processing, and the bot's response is displayed in the chat window.

The Text-to-Speech feature will read out the bot’s responses (if enabled).

You can always change the theme and font through the app’s settings.

⚙️ Customization
Change the Theme: Choose between different color themes to match your vibe. Available themes: blue, dark-blue, green.

Change the Font: Pick from fonts like Helvetica, Arial, or Courier New with adjustable font sizes.

🚨 Important Notes
Make sure your Rasa server is up and running before launching the app.

You might want to make sure your microphone works well for voice input (you know, so your bot can actually hear you 🙄).

🤖 Bot Interactions
Bot Introduction: The bot will greet you with a friendly message and offer assistance.

Sending Messages: You can type a message and press enter or click Send.

Voice Input: Click the mic to speak your message instead of typing it.

Bot Response: The bot will process your input and respond accordingly. Text-to-Speech will read out the response if enabled.

