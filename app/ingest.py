from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.vectorstore import get_vectorstore

def ingest_pdf(path: str):
    docs = PyPDFLoader(path).load()
    print(f"Loaded {len(docs)} pages from PDF")
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200,
        chunk_overlap=250,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    
    chunks = splitter.split_documents(docs)
    print(f"Created {len(chunks)} text chunks")
    
    for c in chunks:
        if "page" not in c.metadata:
            c.metadata["page"] = "unknown"
    
    db = get_vectorstore()
    db.add_documents(chunks)
    db.persist()
    
    print("Ebook fully ingested into vector database")

if __name__ == "__main__":

    ingest_pdf("Ebook.pdf")
