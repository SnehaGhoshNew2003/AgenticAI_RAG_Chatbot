import streamlit as st
import requests

URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="RAG AI Chatbot", layout="centered")
st.title("RAG AI Chatbot")
st.caption("Rag AI Chatbot based on the Ebook")

if "history" not in st.session_state:
    st.session_state.history = []

for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

query = st.chat_input("Ask a question from the Ebook...")

if query:
    st.session_state.history.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            resp = requests.post(URL, json={"question": query}, timeout=60)
            ans = resp.json()["answer"] if resp.status_code == 200 else "Error contacting backend"
            st.markdown(ans)
    

    st.session_state.history.append({"role": "assistant", "content": ans})
