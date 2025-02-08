from openperplex import OpenperplexSync
import json

from app.config import OPENPERPLEX_API_KEY



client_sync = OpenperplexSync(OPENPERPLEX_API_KEY)

def get_current_movies_in_cinemas_using_openperplex(pincode, date, radius):

    try:
        query = (
            f"Find me movies that are currently playing in cinema halls on the date {date} "
            f"around a {radius} mile radius in the area with pincode {pincode}. "
            f"If the movie is present in multiple cinema halls, list it repeatedly. "
            f"Give me just the movie name, cinema location, and timing for each movie. "
            f"Give me the response in JSON format only, nothing else is needed."
        )

        result = client_sync.search(
            query=query,
            date_context=date,
            location="us",  # Adjust based on region if necessary
            pro_mode=False,
            response_language="en",
            answer_type="text",
            verbose_mode=False,
            search_type="general",
            return_citations=False,
            return_sources=False,
            return_images=False,
            recency_filter="past_week"  # Prioritize recent showtimes
        )
        
        print(result["llm_response"])

        if "llm_response" in result and result["llm_response"]:
            try:
                movies_data = json.loads(result["llm_response"].strip())
                return movies_data
            except json.JSONDecodeError:
                return "Error: Received data is not in valid JSON format."
        
        return "No relevant results found."

    except Exception as e:
        return f"Error fetching movie data: {str(e)}"
