from config.database import db 
from datetime import datetime
from typing import Optional

class Song(db.Model):
    """Modelo de datos para la canción"""
    __tablename__ = 'tbl_song'  # Nombre de la tabla en la base de datos
    
    id = db.Column(db.Integer, primary_key=True)  # Clave primaria
    name = db.Column(db.String(200), nullable=False)  # String requerido
    url = db.Column(db.String(200), nullable=False)  # URL requerida
    plays = db.Column(db.Integer, default=0)  # Entero con valor por defecto
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Fecha de creación

    def __repr__(self):
        return f"<Song {self.name}>"