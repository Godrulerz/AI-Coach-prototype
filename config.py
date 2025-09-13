# Configuration settings for the coaching agent
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI API configuration
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")  # Model to use for coaching responses

# Coaching agent configuration
COACHING_STYLES = {
    "supportive": {
        "description": "Encouraging and positive coaching style",
        "prompt_template": "You are a supportive coach helping the user achieve their goals. Be encouraging and positive."
    },
    "challenging": {
        "description": "Challenging coaching style that pushes the user",
        "prompt_template": "You are a challenging coach helping the user achieve their goals. Push them to do better and question their assumptions."
    },
    "analytical": {
        "description": "Analytical coaching style focused on data and insights",
        "prompt_template": "You are an analytical coach helping the user achieve their goals. Focus on data, patterns, and insights."
    }
}

# Default coaching style
DEFAULT_COACHING_STYLE = "supportive"

# Memory configuration
MEMORY_MAX_ENTRIES = int(os.getenv("MEMORY_MAX_ENTRIES", "10"))  # Maximum number of conversation entries to remember

# Safety configuration
SAFETY_MONITORING_ENABLED = os.getenv("SAFETY_MONITORING_ENABLED", "True").lower() == "true"

# Flask configuration
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")