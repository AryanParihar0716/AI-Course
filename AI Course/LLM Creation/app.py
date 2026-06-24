import streamlit as st
st.title("Hello, Streamlit!")
st.title("_This is italic text_ :blue[This is blue text] :speech_balloon: :red[This is red text]")
st.title("$E=mc^2$")
with st.chat_message("AI"):
    st.write("Hello, Streamlit!")
prompt = st.chat_input("Ask me anything")
with st.chat_message("user"):
    st.write(prompt)