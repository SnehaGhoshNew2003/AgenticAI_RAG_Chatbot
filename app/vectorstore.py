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
