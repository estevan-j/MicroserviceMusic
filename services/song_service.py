from repository.song_repository import SongRepository
from schemas.song_schema import SongSchema, SongUpdateSchema, SongResponseSchema
from typing import List, Optional

class SongService:
    """Service for Song business logic operations"""

    def __init__(self):
        self.song_repository = SongRepository()


    def get_all_songs(self) -> List[SongResponseSchema]:
        songs = self.song_repository.get_all_songs()
        return [SongResponseSchema.from_orm(song) for song in songs]
    

    def create_song(self, song_data: SongSchema) -> SongResponseSchema:
        song = self.song_repository.create_song(song_data)
        return SongResponseSchema.from_orm(song)
    

    def update_song(self, song_id: int, song_data: SongUpdateSchema) -> Optional[SongResponseSchema]:
        song = self.song_repository.update_song(song_id, song_data)
        if song:
            return SongResponseSchema.from_orm(song)
        return None
    
    def delete_song(self, song_id: int) -> bool:
        return self.song_repository.delete_song(song_id)