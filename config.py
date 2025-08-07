import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-3.5-turbo"

# Agent Configuration
AGENT_TIMEOUT = 30  # seconds
MAX_RETRIES = 3

# Evaluation Thresholds
GOOD_SCORE_THRESHOLD = 7.0  # out of 10
MIN_RESPONSE_LENGTH = 100  # characters
