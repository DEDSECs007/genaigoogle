import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv(r"X:\000 PocketSchool\app\.env")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print("\n📌 Available Gemini Models in YOUR account:\n")
for m in genai.list_models():
    print("  ✔", m.name)
