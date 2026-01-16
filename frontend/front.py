'''import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title="RAG AI Chatbot",
    layout="centered"
)

st.title("RAG AI Chatbot")
st.caption("Rag AI Chatbot based on the Ebook")

# chat history initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_query = st.chat_input("Ask a question from the Ebook...")

if user_query:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_query}
    )
    with st.chat_message("user"):
        st.markdown(user_query)

    # Call backend
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = requests.post(
                API_URL,
                json={"question": user_query},
                timeout=60
            )

            if response.status_code == 200:
                answer = response.json()["answer"]
            else:
                answer = "Error contacting backend"

            st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
'''


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