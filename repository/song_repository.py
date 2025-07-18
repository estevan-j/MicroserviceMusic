from config.database import db 
from schemas.song_schema import SongSchema, SongUpdateSchema
from models.song import Song
from typing import List, Optional


class SongRepository:
    """Repository for Song database operations"""

    @staticmethod
    def get_all_songs() -> List[Song]:
        """Retrieve all songs from the database"""
        return Song.query.all()
    
    @staticmethod
    def create_song(song_data: SongSchema) -> Song:
        """Create a new song in the database"""
        new_song = Song(
            name=song_data.name,
            url=song_data.url,
            plays=song_data.plays
        )
        db.session.add(new_song)
        db.session.commit()
        db.session.refresh(new_song)
        return new_song
    
    @staticmethod
    def update_song(song_id: int, song_data: SongUpdateSchema) -> Optional[Song]:
        """Update an existing song in the database"""
        song = Song.query.get(song_id)
        if not song:
            return None
        
        if song_data.name is not None:
            song.name = song_data.name
        if song_data.url is not None:
            song.url = song_data.url
        
        db.session.commit()
        return song
    
    @staticmethod
    def delete_song(song_id: int) -> bool:
        """Delete a song from the database"""
        song = Song.query.get(song_id)
        if not song:
            return False
        
        db.session.delete(song)
        db.session.commit()
        return True