'''from fastapi import FastAPI
from pydantic import BaseModel
from app.graph import chat_graph

app = FastAPI(title="RAG AI Chatbot")

#req-res model
class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str


#health check
@app.get("/")
def health():
    return {"status": "Backend running"}


#endpoint
@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    result = chat_graph.invoke({
        "question": req.question,
        "context": None,
        "answer": None,
        "route": None
    })

    return ChatResponse(answer=result["answer"])
'''

from fastapi import FastAPI
from pydantic import BaseModel
from app.graph import chat_graph

api = FastAPI(title="RAG AI Chatbot")

class Query(BaseModel):
    question: str

class Reply(BaseModel):
    answer: str

@api.get("/")
def status():
    return {"status": "Backend running"}

@api.post("/chat", response_model=Reply)
def chat(q: Query):
    res = chat_graph.invoke({
        "question": q.question,
        "context": None,
        "answer": None,
        "route": None
    })
    return Reply(answer=res["answer"])

app = api