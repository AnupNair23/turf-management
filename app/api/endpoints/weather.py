from fastapi import APIRouter, HTTPException, Path, Body, Depends
from typing import List
from app.db.database import get_db
from app.models import PitchModel, UpdatePitchModel
from app.crud.weather import get_geo
router = APIRouter()

# get all the pitches
@router.get("/{query}", response_model=List[PitchModel])
async def get_geo_location(query: str):
    return get_geo(query)
