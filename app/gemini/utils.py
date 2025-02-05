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
            f"Create a List of top 10 movies along with their release dates that match this description: '{description}'."
            "The ranking should be according to to IMDB. It is okay if the results are not perfect. But make sure to get 10 movies"
            "along with their release dates, and nothing more than that. In case a movie is mentioned in the description, do not add it again."
            "Return the result as a JSON array, with only the movie names, their release dates and a brief intro on the movie"
            " , no extra text or formatting."
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