'''from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from app.config import CHROMA_DIR, HF_EMBEDDING_MODEL


_embeddings = None


def get_embeddings():
    global _embeddings
    if _embeddings is None:
        _embeddings = HuggingFaceEmbeddings(
            model_name=HF_EMBEDDING_MODEL
        )
    return _embeddings


def get_vectorstore():
    return Chroma(
        collection_name="agentic_ai_ebook",
        persist_directory=CHROMA_DIR,
        embedding_function=get_embeddings()
    )
'''


from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from app.config import DB_PATH, EMBED_MODEL

embed = None

def get_embeddings():
    global embed
    if not embed:
        embed = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    return embed

def get_vectorstore():
    return Chroma(
        collection_name="ebook_db",
        persist_directory=DB_PATH,
        embedding_function=get_embeddings()
    )