# agents.py

import google.generativeai as genai
from config import API_KEY, MODEL

# Configure GenAI client
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(MODEL)

class Agent:
    def __init__(self, name, role_prompt):
        self.name = name
        self.role_prompt = role_prompt

    def respond(self, message):
        """
        Generate a response from the Gemini model, given the agent's role and a message.
        """
        # Combine the role instruction and the user message into one prompt string.
        prompt = f"Role: {self.role_prompt}\n\nTask: {message}"
        response = model.generate_content(prompt)
        return response.text
