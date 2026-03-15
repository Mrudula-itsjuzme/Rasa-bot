import os
from typing import Any

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_PATH_ENV = "RASA_LOCAL_MODEL_PATH"
DEFAULT_MODEL_PATH = "models/openhermes-2-mistral-7b.Q4_K_M.gguf"


def _resolve_model_path() -> str:
    """Resolve local model path from environment with a repository-relative fallback."""
    return os.getenv(MODEL_PATH_ENV, DEFAULT_MODEL_PATH)


class ActionRespondWithLLM(Action):
    def name(self) -> str:
        return "action_respond_with_llm"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: dict[str, Any],
    ) -> list[dict[str, Any]]:
        user_message = tracker.latest_message.get("text", "")
        model_path = _resolve_model_path()

        try:
            tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
            model = AutoModelForCausalLM.from_pretrained(model_path, local_files_only=True)
        except Exception:
            dispatcher.utter_message(
                text=(
                    "There was an error loading the local model. "
                    "Set RASA_LOCAL_MODEL_PATH or verify model files."
                )
            )
            return []

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

        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(inputs["input_ids"], max_length=150, num_return_sequences=1)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        sassbot_reply = response.split("Sassbot:")[-1].strip()
        dispatcher.utter_message(text=sassbot_reply)

        return []