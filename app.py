import streamlit as st
import os
from agent import run_agent_once

st.set_page_config(page_title="Tool-Using AI Agent", layout="wide")

st.title("🛠 Tool-Using AI Agent (Gemini)")

# -----------------------
# SIDEBAR — API SETTINGS
# -----------------------
st.sidebar.header("🔑 API Settings")

gemini_api_key = st.sidebar.text_input("Gemini API Key", type="password")

gmail_user = st.sidebar.text_input("Gmail (optional)")
gmail_app_password = st.sidebar.text_input("Gmail App Password", type="password")


# Inject values into os.environ so agent.py can see them
if gemini_api_key:
    os.environ["GEMINI_API_KEY"] = gemini_api_key

if gmail_user:
    os.environ["GMAIL_USER"] = gmail_user

if gmail_app_password:
    os.environ["GMAIL_APP_PASSWORD"] = gmail_app_password


# -----------------------
# MAIN CHAT INPUT
# -----------------------
st.subheader("💬 Ask the agent something...")

user_input = st.text_input(
    "Ask the agent something...",
    label_visibility="collapsed",
    placeholder="Type a command..."
)

if user_input:
    with st.spinner("Thinking..."):
        result = run_agent_once(user_input)

    st.write(result)
