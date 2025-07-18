from flask import Blueprint, jsonify, request
from schemas.song_schema import SongSchema, SongUpdateSchema
from services.song_service import SongService
from pydantic import ValidationError

song_routes = Blueprint('song_routes', __name__, url_prefix='/api/songs')

songService = SongService()


@song_routes.route('/', methods=['GET'])
def get_all_songs():
    """Retrieve all songs"""
    try:
        songs_schemas = songService.get_all_songs()
        return jsonify([song.dict() for song in songs_schemas]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@song_routes.route('/', methods=['POST'])
def create_song():
    """Create a new song"""
    try:
        if not request.json:
            return jsonify({'error': 'Request body required'}), 400

        song_data = SongSchema(**request.json)

        new_song_schema = songService.create_song(song_data)
        return jsonify(new_song_schema.dict()), 201

    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@song_routes.route('/<int:song_id>', methods=['PUT'])
def update_song(song_id):
    """Update an existing song"""
    try:
        if not request.json:
            return jsonify({'error': 'Request body required'}), 400

        song_data = SongUpdateSchema(**request.json)

        updated_song_schema = songService.update_song(song_id, song_data)

        if updated_song_schema:
            return jsonify(updated_song_schema.dict()), 200
        else:
            return jsonify({'error': 'Song not found'}), 404

    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@song_routes.route('/<int:song_id>', methods=['DELETE'])
def delete_song(song_id):
    """Delete a song"""
    try:
        if songService.delete_song(song_id):
            return jsonify({'message': 'Song deleted successfully'}), 200
        else:
            return jsonify({'error': 'Song not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@song_routes.route('/search', methods=['GET'])
def search_songs():
    """Search songs"""
    try:
        name = request.args.get('name', '')
        min_plays = request.args.get('min_plays', 0, type=int)

        songs_schemas = songService.search_songs(
            name=name, min_plays=min_plays)
        return jsonify([song.dict() for song in songs_schemas]), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
