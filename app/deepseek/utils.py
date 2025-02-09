from openai import OpenAI
import json
from app.config import DEEPSEEK_API_KEY  # Load API key

def get_movies_from_description_using_deepseek(description, exclude_list):
    
    try:
        client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

        # Construct the prompt
        prompt = (
            f"Provide a JSON array of exactly 10 real movies that match this description: '{description}'. "
            "The movies must be real, well-known, and sourced from actual movie databases like IMDb. "
            "Each entry in the JSON array should include: "
            "1. 'movie': The exact title of the movie. "
            "2. 'release_date': The official release date in 'YYYY-MM-DD' format. "
            "3. 'intro': A short, one-sentence summary of the movie. "
            "Ensure the response contains only a valid JSON array, with no additional text, formatting, or explanations. "
            "Do not include any fictional or AI-generated movies—only widely recognized real films."
        )

        # Add exclusion list to the prompt only if it's not empty
        if exclude_list and exclude_list.strip():
            prompt += (
                f" **Important:** Do not include any of the following movies in the suggestions: {exclude_list}. "
                "If any of these movies match the description, exclude them and suggest other movies instead."
            )

        # Call the DeepSeek API
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a brilliant movie critic who likes to suggest movies to users."},
                {"role": "user", "content": prompt}
            ],
            stream=False
        )

        # Extract the response content
        response_text = response.choices[0].message.content.strip()

        # Remove Markdown-style code blocks (```json ... ```)
        if response_text.startswith("```json"):
            response_text = response_text.replace("```json", "").replace("```", "").strip()

        # Parse the response as JSON
        try:
            movies = json.loads(response_text)
            if isinstance(movies, list):
                # Validate the structure of each movie entry
                for movie in movies:
                    if not all(key in movie for key in ["movie", "release_date", "intro"]):
                        return {"error": "Invalid movie structure in DeepSeek response", "response": movies}
                return movies
            else:
                return {"error": "DeepSeek response is not a list", "response": movies}
        except json.JSONDecodeError:
            return {"error": "Failed to parse JSON from DeepSeek response", "response": response_text}

    except Exception as e:
        return {"error": str(e)}

def generate_itinerary_using_deepseek(destination, duration, interests, budget, exclude):
    try:
        # client = OpenAI(
        #     api_key=DEEPSEEK_API_KEY,
        #     base_url="https://api.deepseek.com/v1",
        #     timeout=30,
        #     default_headers={
        #         "User-Agent": "YourApp/1.0",
        #         "Accept": "application/json"
        #     }
        # )
        client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")


        print(f"API Key: {'valid' if DEEPSEEK_API_KEY.startswith('sk-') else 'invalid'} ({DEEPSEEK_API_KEY[:8]}...)")
        
        prompt = f"""
        [Role]: You are an expert travel planner.
        [Task] Create a {duration}-day itinerary for {destination} with:
        - Interests: {interests}
        - Budget: {budget or 'medium'}
        - Exclude: {exclude or 'no restrictions'}
        
        [Format] JSON array with daily details including:
        "day", "date", "activities", "area_to_stay", "transportation"
        
        [Instructions]:
        - For "area_to_stay", suggest the best neighborhood (3 at max), district, or area to stay in for that day, based on the activities planned.
        - Do not recommend specific hotels or accommodations—only general areas.
        - Ensure the areas suggested are safe, convenient, and align with the traveler's interests and budget.
        """
        
        print(f"\n=== DeepSeek Prompt ===\n{prompt}\n======================\n")
        
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a professional travel planner."},
                {"role": "user", "content": prompt}
            ]
        )
        
        response_text = response.choices[0].message.content.strip()
        if response_text.startswith("```json"):
            response_text = response_text.replace("```json", "").replace("```", "").strip()
            
        print(f"\n=== DeepSeek response ===\n{response_text}\n======================\n")

        itinerary = json.loads(response_text)
        if isinstance(itinerary, list):
            required_keys = ["day", "activities", "area_to_stay", "transportation"]
            for day_plan in itinerary:
                if not all(key in day_plan for key in required_keys):
                    return {"error": "Invalid itinerary structure"}
            return itinerary
        return {"error": "Response was not a list", "response": response_text}

    except Exception as e:
        return {"error": str(e)}
