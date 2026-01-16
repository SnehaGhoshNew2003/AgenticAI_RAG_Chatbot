'''from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import LLM_MODEL, GOOGLE_API_KEY

def get_llm():
    return ChatGoogleGenerativeAI(
        model=LLM_MODEL,
        google_api_key=GOOGLE_API_KEY,
        temperature=2
    )
'''


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