from flask import Blueprint, jsonify, request
from app.gemini.utils import get_movies_from_description



main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({"message": "Welcome to your decision-making API!"})

    

@main.route('/api/searchMovieBasedOnDescriptionWithGemini', methods=['POST'])
def gemini_query():
    data = request.json
    user_query = data.get('query', '')

    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    try:
        movies = get_movies_from_description(user_query)
        
        # Ensure we return a JSON list
        return jsonify({"movies": movies}) if isinstance(movies, list) else jsonify({"error": movies}), 500
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500