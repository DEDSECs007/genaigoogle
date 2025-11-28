import os
import requests
from dotenv import load_dotenv
import streamlit as st

# Load local .env if running on PC
load_dotenv()

# First try .env → then fallback to Streamlit Secrets
API_KEY = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID") or st.secrets.get("SEARCH_ENGINE_ID")


def search_web(query):
    if not API_KEY or not SEARCH_ENGINE_ID:
        return "❌ Missing API Key or Search Engine ID. Add them to `.env` or Streamlit Secrets."

    url = (
        "https://www.googleapis.com/customsearch/v1?"
        f"key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}"
    )

    try:
        response = requests.get(url)
        data = response.json()

        results = data.get("items", [])

        if not results:
            return "🔍 No results found."

        extracted = [
            f"📌 **{item['title']}**\n🔗 {item['link']}"
            for item in results[:5]
        ]

        return "\n\n".join(extracted)

    except Exception as e:
        return f"⚠️ Search Error: {str(e)}"
