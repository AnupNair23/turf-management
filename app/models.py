# app/models.py
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from enum import Enum

class TurfType(str, Enum):
    NATURAL = 'Natural'
    ARTIFICIAL = 'Artificial'
    HYBRID = 'Hybrid'

# Assuming PitchModel is already defined as shown in previous examples
class PitchModel(BaseModel):
    id: Optional[str] = Field(None)
    name: str = Field(...)
    location: str = Field(...)
    turf_type: TurfType = Field(...)
    last_maintenance_date: datetime = Field(default_factory=datetime.utcnow)
    next_scheduled_maintenance: Optional[datetime] = None
    current_condition: int = Field(default=10, ge=1, le=10)
    replacement_date: Optional[datetime] = None
    lat: Optional[int] = Field(None)
    long: Optional[int] = Field(None)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
# Define UpdatePitchModel for partial updates (making all the fields optional here)
class UpdatePitchModel(BaseModel):
    id: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    location: Optional[str] = Field(None)
    turf_type: Optional[TurfType] = Field(None)
    last_maintenance_date: Optional[datetime] = Field(default=None)
    next_scheduled_maintenance: Optional[datetime] = Field(default=None)
    current_condition: Optional[int] = Field(None, ge=1, le=10)
    replacement_date: Optional[datetime] = Field(default=None)
    lat: Optional[int] = Field(None)
    long: Optional[int] = Field(None)
    class Config:
        use_enum_values = True  # Ensures that enums are treated as their values
