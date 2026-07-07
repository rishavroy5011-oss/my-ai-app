import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Multi-Tool Hub", layout="centered")

# --- SIDEBAR MEIN USER SE KEY MAANGNA ---
st.sidebar.title("🔑 Setup")
user_api_key = st.sidebar.text_input("Apni Gemini API Key yahan dalein:", type="password")

if not user_api_key:
    st.info("💡 App chalane ke liye please sidebar mein apni Gemini API Key dalein.")
    st.stop()  # Agar key nahi hai toh app yahi ruk jayega
else:
    genai.configure(api_key=user_api_key)  # User ki key se AI connect ho jayega

st.title("🚀 All-In-One AI Creator Hub")
# ... iske niche ka baaki poora code pehle jaisa hi rahega
