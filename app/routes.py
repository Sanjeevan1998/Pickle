from flask import Blueprint, jsonify, request
from app.gemini.utils import *
from app.deepseek.utils import *




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