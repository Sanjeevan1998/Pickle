from flask import Blueprint, jsonify, request
from app.gemini.utils import get_movies_from_description_using_gemini
from app.deepseek.utils import get_movies_from_description_using_deepseek




main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({"message": "Welcome to your decision-making API!"})

    

@main.route('/api/searchMovieBasedOnDescriptionWithGemini', methods=['POST'])
def searchMovieBasedOnDescriptionWithGemini():
    data = request.json
    user_query = data.get('query', '')

    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    try:
        movies = get_movies_from_description_using_gemini(user_query)
        
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

    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    try:
        movies = get_movies_from_description_using_deepseek(user_query)
        
        # Ensure we return a JSON list
        if isinstance(movies, list):
            return jsonify({"movies": movies}), 200  # Explicitly return 200 for clarity
        else:
            return jsonify({"error": movies}), 500  # Return 500 only for errors
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500