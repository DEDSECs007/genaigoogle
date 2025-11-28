import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # auto load

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

MODEL = "models/gemini-2.5-flash"

class Agent:
    def __init__(self, role, model=MODEL):
        self.role = role
        self.model = genai.GenerativeModel(model)

    def run(self, prompt):
        response = self.model.generate_content(f"You are {self.role}.\n\n{prompt}")
        return response.text

class NotesAgent(Agent):
    def summarize(self, text):
        return self.run(f"Summarize clearly in bullet points:\n{text}")

class ResearchAgent(Agent):
    def research(self, topic):
        return self.run(f"Research this topic and give structured notes:\n{topic}")

class PlannerAgent(Agent):
    def create_plan(self, subject, hours):
        return self.run(f"Create a {hours}-hour weekly study timetable for:\n{subject}")
