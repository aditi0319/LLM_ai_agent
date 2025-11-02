# app/services/response_generator.py
import os
from dotenv import load_dotenv
import google.generativeai as genai  # official SDK

load_dotenv()  # loads .env in project root

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY missing — add it to your .env")

# configure SDK
genai.configure(api_key=GEMINI_API_KEY)

def generate_solution(category: str, query: str) -> str:
    """
    Uses Gemini to return a concise support-agent style answer.
    Falls back to a polite static message on error.
    """
    if not query or not query.strip():
        return "Invalid input: please provide the user's issue."

    prompt = (
        f"You are a helpful customer support assistant.\n"
        f"Category: {category}\n"
        f"User query: {query}\n\n"
        f"Write a short, polite, actionable solution (1-3 sentences)."
    )

    try:
        # choose a flash model (fast + free tier friendly)
        model = genai.GenerativeModel("models/gemini-2.0-flash")


        response = model.generate_content(prompt)
        # SDK returns an object; .text contains the generated text
        text = getattr(response, "text", None)
        if text:
            return text.strip()
        # fallback check
        return f"Unexpected API response: {response}"
    except Exception as e:
        # keep UI stable — return a sensible fallback
        return f"AI generation failed: {str(e)}"
