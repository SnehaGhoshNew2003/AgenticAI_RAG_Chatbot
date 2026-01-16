import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
DB_PATH = os.getenv("CHROMA_DIR")
MODEL = os.getenv("LLM_MODEL")
EMBED_MODEL = os.getenv("HF_EMBEDDING_MODEL")