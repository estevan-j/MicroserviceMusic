from flask import Flask, jsonify
from flask_cors import CORS
from config.database import init_db, DatabaseConfig
from routes.song_routes import song_routes
import os


def create_app():
    """Factory pattern para crear la aplicación"""
    # Initialize Flask app
    app = Flask(__name__)

    # Configuración básica
    app.config['DEBUG'] = True

    # Configuración de base de datos
    app.config.from_object(DatabaseConfig)

    # Initialize extensions
    CORS(app)
    init_db(app)

    # Basic test route
    @app.route('/api/test', methods=['GET'])
    def test():
        """Test endpoint"""
        return jsonify({
            'status': 'success',
            'message': 'Flask API is working'
        })

    app.register_blueprint(song_routes)

    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not found'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500

    return app


# Crear la aplicación
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
