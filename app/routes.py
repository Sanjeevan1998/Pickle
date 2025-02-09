from flask import Blueprint, jsonify, request
from app.gemini.utils import *
from app.deepseek.utils import *
from app.openperplex.utils import *
from app.perplexity.utils import *




main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({"message": "Welcome to your decision-making API!"})

    

@main.route('/api/searchMovieBasedOnDescriptionWithGemini', methods=['POST'])
def searchMovieBasedOnDescriptionWithGemini():
    data = request.json
    user_query = data.get('query', '')
    exclude_list = data.get('exclude', '')


    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    try:
        movies = get_movies_from_description_using_gemini(user_query, exclude_list)
        
        # Ensure we return a JSON list
        if isinstance(movies, list):
            return jsonify({"movies": movies}), 200  # Explicitly return 200 for clarity
        else:
            return jsonify({"error": movies}), 500  # Return 500 only for errors

    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@main.route('/api/searchMovieBasedOnDescriptionWithDeepSeek', methods=['POST'])
def searchMovieBasedOnDescriptionWithDeepSeek():
    data = request.json
    user_query = data.get('query', '')
    exclude_list = data.get('exclude', '')


    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    try:
        movies = get_movies_from_description_using_deepseek(user_query,exclude_list)
        
        # Ensure we return a JSON list
        if isinstance(movies, list):
            return jsonify({"movies": movies}), 200  # Explicitly return 200 for clarity
        else:
            return jsonify({"error": movies}), 500  # Return 500 only for errors
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    



@main.route('/api/searchShowBasedOnDescriptionWithGemini', methods=['POST'])
def searchShowBasedOnDescriptionWithGemini():
    data = request.json
    user_query = data.get('query', '')
    exclude_list = data.get('exclude', '')


    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    try:
        shows = get_shows_from_description_using_gemini(user_query, exclude_list)
        
        # Ensure we return a JSON list
        if isinstance(shows, list):
            return jsonify({"shows": shows}), 200  # Explicitly return 200 for clarity
        else:
            return jsonify({"error": movies}), 500  # Return 500 only for errors

    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@main.route('/api/searchShowBasedOnDescriptionWithDeepSeek', methods=['POST'])
def searchShowBasedOnDescriptionWithDeepSeek():
    data = request.json
    user_query = data.get('query', '')
    exclude_list = data.get('exclude', '')


    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    try:
        shows = get_movies_from_description_using_deepseek(user_query, exclude_list)
        
        # Ensure we return a JSON list
        if isinstance(shows, list):
            return jsonify({"shows": shows}), 200  # Explicitly return 200 for clarity
        else:
            return jsonify({"error": shows}), 500  # Return 500 only for errors
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
    
    
    
@main.route('/api/searchAnimeBasedOnDescriptionWithGemini', methods=['POST'])
def searchAnimeBasedOnDescriptionWithGemini():
    data = request.json
    user_query = data.get('query', '')
    exclude_list = data.get('exclude', '')


    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    try:
        animes = get_animes_from_description_using_gemini(user_query, exclude_list)
        
        # Ensure we return a JSON list
        if isinstance(animes, list):
            return jsonify({"animes": animes}), 200  # Explicitly return 200 for clarity
        else:
            return jsonify({"error": animes}), 500  # Return 500 only for errors

    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@main.route('/api/searchAnimeBasedOnDescriptionWithDeepSeek', methods=['POST'])
def searchAnimeBasedOnDescriptionWithDeepSeek():
    data = request.json
    user_query = data.get('query', '')
    exclude_list = data.get('exclude', '')


    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    try:
        animes = get_animes_from_description_using_deepseek(user_query, exclude_list)
        
        # Ensure we return a JSON list
        if isinstance(animes, list):
            return jsonify({"animes": animes}), 200  # Explicitly return 200 for clarity
        else:
            return jsonify({"error": animes}), 500  # Return 500 only for errors
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
    
    
    
@main.route('/api/searchBookBasedOnDescriptionWithGemini', methods=['POST'])
def searchBookBasedOnDescriptionWithGemini():
    data = request.json
    user_query = data.get('query', '')
    exclude_list = data.get('exclude', '')


    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    try:
        books = get_books_from_description_using_gemini(user_query, exclude_list)
        
        # Ensure we return a JSON list
        if isinstance(books, list):
            return jsonify({"books": books}), 200  # Explicitly return 200 for clarity
        else:
            return jsonify({"error": books}), 500  # Return 500 only for errors

    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@main.route('/api/searchBookBasedOnDescriptionWithDeepSeek', methods=['POST'])
def searchBookBasedOnDescriptionWithDeepSeek():
    data = request.json
    user_query = data.get('query', '')
    exclude_list = data.get('exclude', '')


    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    try:
        books = get_books_from_description_using_deepseek(user_query, exclude_list)
        
        # Ensure we return a JSON list
        if isinstance(books, list):
            return jsonify({"books": books}), 200  # Explicitly return 200 for clarity
        else:
            return jsonify({"error": books}), 500  # Return 500 only for errors
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


@main.route('/api/searchCurrentMoviesInCinemasUsingOpenPerplex', methods=['POST'])
def searchCurrentMoviesInCinemasUsingOpenPerplex():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid or missing JSON payload"}), 400

    pincode = data.get('pincode', '')
    date = data.get('date', '')
    radius = data.get('radius', 10)  # Default to 10 miles if not provided

    if not pincode or not date:
        return jsonify({"error": "Pincode and date are required"}), 400

    try:
        movies_data = get_current_movies_in_cinemas_using_openperplex(pincode, date, radius)

        # Ensure movies_data is a dictionary
        if not isinstance(movies_data, dict):
            return jsonify({"error": "Invalid response format from OpenPerplex"}), 500

        # Check if no movies were found
        if movies_data.get("cinemas") == {}:
            return jsonify({"message": "No movies found for the given date and location"}), 200

        return jsonify(movies_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500



@main.route('/api/searchCurrentMoviesInCinemasUsingPerplexity', methods=['POST'])
def search_current_movies_in_cinemas_using_perplexity():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid or missing JSON payload"}), 400

    pincode = data.get('pincode', '')
    date = data.get('date', '')
    radius = data.get('radius', 10)  # Default to 10 miles if not provided

    if not pincode or not date:
        return jsonify({"error": "Pincode and date are required"}), 400

    try:
        movies_data = get_current_movies_in_cinemas_using_perplexity(pincode, date, radius)

        # Ensure movies_data is a dictionary
        if not isinstance(movies_data, dict) or movies_data.get("cinemas") == {}:
            return jsonify({"message": "No movies found for the given date and location"}), 200

        return jsonify(movies_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
		
@main.route('/api/generateTravelItineraryWithGemini', methods=['POST'])
def generate_travel_itinerary_gemini():
    data = request.json
    destination = data.get('destination')
    duration = data.get('duration')
    interests = data.get('interests')
    budget = data.get('budget')
    exclude = data.get('exclude', '')

    if not all([destination, duration, interests]):
        return jsonify({"error": "Missing required parameters"}), 400

    try:
        itinerary = generate_itinerary_using_gemini(
            destination=destination,
            duration=duration,
            interests=interests,
            budget=budget,
            exclude=exclude
        )
        return jsonify({"itinerary": itinerary}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main.route('/api/generateTravelItineraryWithDeepSeek', methods=['POST'])
def generate_travel_itinerary_deepseek():
    data = request.json
    destination = data.get('destination')
    duration = data.get('duration')
    interests = data.get('interests')
    budget = data.get('budget')
    exclude = data.get('exclude', '')

    if not all([destination, duration, interests]):
        return jsonify({"error": "Missing required parameters"}), 400

    try:
        itinerary = generate_itinerary_using_deepseek(
            destination=destination,
            duration=duration,
            interests=interests,
            budget=budget,
            exclude=exclude
        )
        if isinstance(itinerary, dict) and 'error' in itinerary:
            return jsonify(itinerary), 500
        return jsonify({"itinerary": itinerary}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500