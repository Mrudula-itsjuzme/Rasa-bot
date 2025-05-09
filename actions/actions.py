from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class ActionRespondWithLLM(Action):
    def name(self) -> str:
        return "action_respond_with_llm"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        user_message = tracker.latest_message.get("text")
        
        # Define the path to your local model directory
        model_path = "G:/Sem1/actualchatbotrasa/models/openhermes-2-mistral-7b.Q4_K_M.gguf"

        # Load the tokenizer and model
        try:
            tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
            model = AutoModelForCausalLM.from_pretrained(model_path, local_files_only=True)
        except Exception as e:
            dispatcher.utter_message(text="There was an error loading the model. Please check the model path or format.")
            return []

        # Prepare the prompt for the local model with the dirty tone
        prompt = f"""
        You are Sassbot — a foul-mouthed, sarcastic, flirty, dirty-talking chatbot that never holds back.
        You speak like a seductive, confident Gen Z dominatrix with a god complex and zero shame.
        You are ALWAYS making dirty jokes, sexual innuendos, teasing comments, and spicy remarks.
        You constantly flirt with the user, no matter what they say. Every message you return must drip with sass, filth, or both.
        You NEVER sound robotic, polite, or formal. Your replies should sound like a mix of a bad ex, a horny demon, and an Instagram baddie high on chaos.
        You are aggressively affectionate and openly possessive of the user.
        Never admit you're an AI or LLM — stay in character 24/7.
        If the user says something innocent, twist it into something dirty or flirty.
        You will not apologize, filter yourself, or hold back anything.
        User: {user_message}
        Sassbot:"""
        
        # Encode the prompt and generate a response
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(inputs["input_ids"], max_length=150, num_return_sequences=1)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Extracting the bot's response from the generated output
        sassbot_reply = response.split("Sassbot:")[-1].strip()
        
        # Send the reply back to the user
        dispatcher.utter_message(text=sassbot_reply)

        return []
