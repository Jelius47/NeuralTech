# chat_insight/analyzer.py
import json
from openai import OpenAI
from .formatter import format_chat
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def analyze_chat(chat_transcript):
    """Use LLM to analyze a chat transcript."""
    prompt = f"""
    Analyze the following chat and determine:
    1. If the customer is struggling.
    2. What are they struggling with?
    3. Overall sentiment (positive, neutral, negative).
    4. Summary of the conversation.

    Chat:
    {chat_transcript}

    Return a JSON with: is_struggling (bool), struggle_reason (str), sentiment (str), summary (str).
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo-2024-04-09",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"Error analyzing chat: {e}")
        return {
            "is_struggling": None,
            "struggle_reason": None,
            "sentiment": None,
            "summary": None
        }
