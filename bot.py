import openai
import streamlit as st

API_KEY = "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"

# Configure API key
openai.api_key = API_KEY

# Store chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

st.title("Anup-BOT 🤖")

# Show chat history
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).markdown(msg["content"])

# User input
if prompt := st.chat_input("Type your message..."):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    # Get response from OpenAI
    response = openai.chat.completions.create(
        model="gpt-4o-mini",  # Or gpt-3.5-turbo if you want
        messages=st.session_state["messages"],
        max_tokens=300,
        temperature=0.7
    )

    reply = response.choices[0].message.content
    st.session_state["messages"].append({"role": "assistant", "content": reply})
    st.chat_message("assistant").markdown(reply)
