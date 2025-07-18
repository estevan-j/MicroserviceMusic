from flask_sqlalchemy import SQLAlchemy
import os

# Instancia global de SQLAlchemy
db = SQLAlchemy()

class DatabaseConfig:
    """Configuración de base de datos"""
    
    # Configuración para desarrollo
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = os.environ.get('DB_ECHO', 'False').lower() == 'true'
    

def init_db(app):
    """Inicializa la base de datos con la app Flask"""
    db.init_app(app)
    
    with app.app_context():
        # Crear todas las tablas
        db.create_all()
        print("✅ Base de datos inicializada correctamente")

def get_db():
    """Retorna la instancia de base de datos"""
    return db