import google.generativeai as genai
import json
from app.config import GEMINI_API_KEY


# Load the API key from environment variables
genai.configure(api_key=GEMINI_API_KEY)

def get_movies_from_description(description):
    """
    Uses Gemini to find the top 10 movies based on a given description.
    """
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")  # Using a valid model
        prompt = (
            f"Provide a JSON array of **exactly 10 real movies** that match this description: '{description}'. "
            "The movies **must be real and well-known, sourced from actual movie databases like IMDb**. "
            "Each entry should include: "
            "1. 'movie': The exact title of the movie. "
            "2. 'release_date': The official release date in 'YYYY-MM-DD' format. "
            "3. 'intro': A short, one-sentence summary of the movie. "
            "Ensure that the response contains **only a valid JSON array**, with no additional text, formatting, or explanations. "
            "Do not include any fictional or AI-generated movies—only widely recognized real films."
        )

        
        response = model.generate_content(prompt)

        # Extracting text response
        response_text = response.text.strip()

        # Remove Markdown-style code blocks (```json ... ```)
        if response_text.startswith("```json"):
            response_text = response_text.replace("```json", "").replace("```", "").strip()

        # Convert response to a Python list
        try:
            movies = json.loads(response_text)  # Parse as JSON
            if isinstance(movies, list):  
                return movies
            else:
                raise ValueError("Gemini response is not a list")
        except json.JSONDecodeError:
            return {"error": "Failed to parse JSON from Gemini response", "response": response_text}

    except Exception as e:
        return {"error": str(e)}  # Return error message