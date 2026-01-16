from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import MODEL, API_KEY

model = None

def get_llm():
    global model
    if not model:
        model = ChatGoogleGenerativeAI(
            model=MODEL,
            google_api_key=API_KEY,
            temperature=0.2
        )

    return model
