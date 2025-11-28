import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st

# Load .env locally
load_dotenv()

# Fallback: Use Streamlit Secrets in cloud
api_key = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("❌ No API key found! Add it to .env or Streamlit Secrets.")

genai.configure(api_key=api_key)

def list_available_models():
    return [m.name for m in genai.list_models()]

if __name__ == "__main__":
    print("\n📌 Available Gemini Models in YOUR account:\n")
    for name in list_available_models():
        print("  ✔", name)
