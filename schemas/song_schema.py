from pydantic import BaseModel, Field, validator
from typing import Optional


class SongSchema(BaseModel):
    """Schema for Song data validation"""
    name: str = Field(..., min_length=1, max_length=30)
    url: str = Field(..., min_length=1, max_length=200)
    plays: Optional[int] = Field(default=0, ge=0)

    model_config = {
        "from_attributes": True
    }


class SongUpdateSchema(BaseModel):
    """Schema for updating Song data"""
    name: Optional[str] = Field(None, min_length=1, max_length=30)
    url: Optional[str] = Field(None, min_length=1, max_length=200)

    model_config = {
        "from_attributes": True
    }


class SongResponseSchema(BaseModel):
    """Schema for Song response"""
    id: int
    name: str
    url: str
    plays: int

    model_config = {
        "from_attributes": True
    }
