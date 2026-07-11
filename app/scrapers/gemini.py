import os
from google import genai
from google.genai import types

def generate_digest_with_gemini(article_text):
    # Initialize the client. It automatically picks up GEMINI_API_KEY from your environment.
    client = genai.Client()

    prompt = f"Summarize the following article for a news digest:\n\n{article_text}"

    try:
        # Gemini 2.5 Flash is the recommended default for text tasks (fast and cost-effective)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        return response.text
        
    except Exception as e:
        print(f"Error generating digest with Gemini: {e}")
        return None