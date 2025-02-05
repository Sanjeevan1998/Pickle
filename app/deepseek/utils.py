from openai import OpenAI
import json
from app.config import DEEPSEEK_API_KEY  # Load API key

def get_movies_from_description_using_deepseek(description):

    try:
        client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

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

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "system", "content": "You are a brilliant movie critic who likes to suggest movies to users."},
                      {"role": "user", "content": prompt}],
            stream=False
        )

        # Extracting text response
        response_text = response.choices[0].message.content.strip()

        # Remove Markdown-style code blocks (```json ... ```)
        if response_text.startswith("```json"):
            response_text = response_text.replace("```json", "").replace("```", "").strip()

        # Convert response to a Python list
        try:
            movies = json.loads(response_text)  # Parse as JSON
            if isinstance(movies, list):  
                return movies
            else:
                raise ValueError("DeepSeek response is not a list")
        except json.JSONDecodeError:
            return {"error": "Failed to parse JSON from DeepSeek response", "response": response_text}

    except Exception as e:
        return {"error": str(e)}  # Return error message
