import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from app.agents import NotesAgent, ResearchAgent, PlannerAgent
from app.list_models import list_available_models

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.title("📚 Pocket School — AI Study Companion")
st.write("Your personal assistant for studying, research, and planning!")

mode = st.selectbox("Select Action:",
    ["Summarize Notes", "Research Topic", "Create Study Plan"]
)

user_input = st.text_area("Enter your text or topic:")

if st.sidebar.button("Show Available Models"):
    models = list_available_models()
    st.sidebar.write(models)

if st.button("Generate 🚀"):
    if not user_input.strip():
        st.warning("Please type something first 😄")
    else:
        if mode == "Summarize Notes":
            agent = NotesAgent(role="friendly academic summarizer")
            response = agent.summarize(user_input)

        elif mode == "Research Topic":
            agent = ResearchAgent(role="research assistant")
            response = agent.research(user_input)

        elif mode == "Create Study Plan":
            agent = PlannerAgent(role="smart study planner")
            response = agent.create_plan(user_input, 10)

        st.success(response)


