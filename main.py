import streamlit as st
from langchain_core.messages.base import BaseMessage
import LLM_agent


st.title("This is not a medical consultant, please take opinion as opinion not final verdict on your medical condition")
prompt = st.chat_input(
    "Say something and/or attach an image",
    accept_file=True,
    file_type=["jpg", "jpeg", "png"],
)
if prompt and prompt.text:
    st.markdown(prompt.text)
if prompt and prompt["files"]:
    st.image(prompt["files"][0])

LLM_response = LLM_agent.LLM_call(prompt.text)
text = LLM_response
st.chat_message("assistant").write(text)