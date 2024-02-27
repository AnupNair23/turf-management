from fastapi import APIRouter, HTTPException, Path, Body, Depends
from typing import List
from app.db.database import get_db
from app.models import PitchModel, UpdatePitchModel
from app.crud.pitch import create_pitch, get_all_pitches, get_pitch, update_pitch, delete_pitch
router = APIRouter()


# add pitch
@router.post("/", response_model=UpdatePitchModel)
async def add_pitch(pitch: PitchModel):
    return create_pitch(pitch)

# get all the pitches
@router.get("/", response_model=List[PitchModel])
async def list_pitches():
    return get_all_pitches()

# get details of the pitch
@router.get("/{id}", response_model=PitchModel)
async def read_pitch(id: str = Path(..., title="The ID of the pitch to get")):
    pitch = get_pitch(id)
    if pitch:
        return pitch
    raise HTTPException(status_code=404, detail="Pitch not found")

# update pitch data
@router.patch("/{id}", response_model=PitchModel)
async def update_pitch_data(id: str, pitch: UpdatePitchModel = Body(...)):
    updated_pitch = update_pitch(id, pitch)
    if updated_pitch:
        return updated_pitch
    raise HTTPException(status_code=404, detail="Pitch not found")

# delete the pitch
@router.delete("/{id}", response_model=dict)
async def remove_pitch(id: str):
    if delete_pitch(id):
        return {"message": "Pitch successfully deleted"}
    raise HTTPException(status_code=404, detail="Pitch not found")
