from langgraph.graph import StateGraph, END
from typing import TypedDict, Optional
from app.vectorstore import get_vectorstore
from app.llm import get_llm

store = get_vectorstore()
model = get_llm()

class State(TypedDict):
    question: str
    context: Optional[str]
    answer: Optional[str]
    route: Optional[str]

def classify(state: State):
    query = state["question"].lower().strip()
    
    greets = {"hi", "hello", "hey", "hii", "good morning", "good afternoon", "good evening", "good night"}
    
    if query in greets:
        return {"route": "greet"}
    if "summar" in query:
        return {"route": "summarize"}
    return {"route": "rag"}

def fetch(state: State):
    results = store.similarity_search(state["question"], k=15)
    
    if not results:
        return {"context": None}
    
    ctx = "\n\n".join(f"[Page {d.metadata.get('page', 'N/A')}]\n{d.page_content}" for d in results)
    return {"context": ctx}

def respond(state: State):
    if state["route"] == "greet":
        return {"answer": "Hey.. I can answer detailed questions and summarize content from the Agentic AI Ebook."}
    
    if state["route"] == "summarize" and state["context"]:
        prompt = f"You are an expert technical summarizer.\n\nSummarize the following ebook content clearly, accurately, and concisely.\nPreserve key concepts, steps, and terminology.\nUse ONLY the provided content.\n\nContent:\n{state['context']}"
        return {"answer": model.invoke(prompt).content}
    
    if state["context"]:
        prompt = f"You are an expert AI assistant answering STRICTLY from the Agentic AI Ebook.\n\nINSTRUCTIONS:\n- Use ONLY the provided context.\n- Combine information from multiple sections if needed.\n- Answer in detail with clear explanations.\n- If the answer is not explicitly present, respond exactly with:\n  \"Sorry, this question is not covered in the Agentic AI Ebook.\"\n\nContext:\n{state['context']}\n\nQuestion:\n{state['question']}"
        return {"answer": model.invoke(prompt).content}
    
    return {"answer": "Sorry, this question is not covered in the Agentic AI Ebook."}

workflow = StateGraph(State)
workflow.add_node("classify", classify)
workflow.add_node("fetch", fetch)
workflow.add_node("respond", respond)

workflow.set_entry_point("classify")
workflow.add_edge("classify", "fetch")
workflow.add_edge("fetch", "respond")
workflow.add_edge("respond", END)


chat_graph = workflow.compile()
