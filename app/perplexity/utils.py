from openai import OpenAI
from typing import Dict
import json
import os
import re


# Load API key from environment variable
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")


def get_current_movies_in_cinemas_using_perplexity(pincode: str, date: str, radius: int) -> Dict:
    """
    Calls the Perplexity API to fetch movies currently playing in cinemas for the given pincode, date, and radius.
    Ensures a structured JSON response. If no movies are found, it returns {"cinemas": {}}.
    """
    if not PERPLEXITY_API_KEY:
        return {"error": "Missing API key"}

    # Initialize the Perplexity API client
    client = OpenAI(api_key=PERPLEXITY_API_KEY, base_url="https://api.perplexity.ai")

    # Define the prompt for the Perplexity API
    prompt = (
        f"Find movies currently playing in cinema halls on {date}, within a {radius}-mile radius of the area with pincode {pincode}. "
        "If no showtimes are available for the given date, return an empty JSON object: {'cinemas': {}}. "
        "Otherwise, structure the response with cinema halls as the primary key, listing movies, their show timings, and a source link. "
        "The JSON response should follow this exact structure: "
        '{"cinemas": {"Cinema Name": {"movies": [{"movie_name": "Movie Name", "show_timings": ["time1", "time2"], "source": "source_url"}]}}}'
    )

    try:
        # Call the Perplexity API
        response = client.chat.completions.create(
            model="sonar",
            messages=[
                {"role": "system", "content": "You are an AI that fetches real-time movie listings in cinemas."},
                {"role": "user", "content": prompt},
            ],
            stream=False,
        )

        # Extract the response content
        response_text = response.choices[0].message.content.strip()

        # Use regex to extract the JSON string from the response
        json_match = re.search(r"```json\n(.+?)\n```", response_text, re.DOTALL)
        if json_match:
            json_string = json_match.group(1).strip()
        else:
            # If no JSON block is found, assume the entire response is JSON
            json_string = response_text

        # Parse the JSON string
        try:
            movies_data = json.loads(json_string)
            return movies_data
        except json.JSONDecodeError as e:
            return {"error": f"Failed to parse JSON response: {str(e)}", "response": response_text}

    except Exception as e:
        return {"error": f"Perplexity API request failed: {str(e)}"}
