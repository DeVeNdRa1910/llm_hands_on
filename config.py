from dotenv import load_dotenv
import os

load_dotenv()

class ENV_CONFIG():
    OPEN_API_KEY = os.getenv("OPEN_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GROK_API_KEY = os.getenv("GROK_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    LLM_MODEL = os.getenv("LLM_MODEL")