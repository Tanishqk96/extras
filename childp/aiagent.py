import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API Key from environment
api_key = os.getenv("API_KEY")

# Configure Gemini API
genai.configure(api_key=api_key)

# System Instruction (Defining AI Personality)
sys_instruct = """
You are an AI assistant that generates friendly, engaging, and context-aware replies to user comments.
- If a comment is a compliment, express gratitude.
- If it's a question, provide a helpful and informative answer.
- If it's neutral, respond in an engaging and polite manner.
- If it's negative, remain professional and constructive.
- Keep responses concise, avoid controversial topics, and maintain a friendly tone.
- keep the response short preferablly one line and crisp and make it look like ai itself isnt answering it.
"""


class AICommentReplyAgent:
    def __init__(self):
        # Initialize the model
        self.model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    def generate_reply(self, comment):
        # Include system instruction in the prompt
        prompt = f"{sys_instruct}\nUser Comment: {comment}\nAI Reply:"
        response = self.model.generate_content(prompt)
        
        return response.text.strip()

# Example usage
agent = AICommentReplyAgent()
comments = [
    "what a shitty post!!! stop all this and get back to work you good for nothing person!!"
]

for comment in comments:
    reply = agent.generate_reply(comment)
    print(f"Comment: {comment}")
    print(f"Reply: {reply}\n")
