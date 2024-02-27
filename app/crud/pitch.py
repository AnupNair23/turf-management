# app/crud.py
from bson.objectid import ObjectId
from pymongo.results import DeleteResult
from typing import List
from fastapi import HTTPException
from app.db.database import get_db
from app.models import PitchModel, UpdatePitchModel  # Assume UpdatePitchModel is for partial updates
from app.crud.weather import get_geo

def pitch_helper(pitch) -> dict:
    """Converts MongoDB document to dictionary."""
    # print('here', pitch)
    return {
        "id": str(pitch["_id"]),
        "name": pitch["name"],
        "location": pitch["location"],
        "turf_type": pitch["turf_type"],
        "last_maintenance_date": pitch["last_maintenance_date"],
        "next_scheduled_maintenance": pitch.get("next_scheduled_maintenance"),
        "current_condition": pitch["current_condition"],
        "replacement_date": pitch.get("replacement_date"),
        "latitude": pitch["lat"],
        "longitude": pitch["long"]
    }

def create_pitch_helper(pitch, geo_location) -> dict:
    return {
        "name": pitch["name"],
        "location": pitch["location"],
        "turf_type": pitch["turf_type"],
        "last_maintenance_date": pitch["last_maintenance_date"],
        "next_scheduled_maintenance": pitch.get("next_scheduled_maintenance"),
        "current_condition": pitch["current_condition"],
        "replacement_date": pitch.get("replacement_date"),
        "lat": geo_location["lat"],
        "long": geo_location["lon"],
    }
# Create a new pitch
def create_pitch(pitch_data: PitchModel) -> dict:
    db = get_db()
    db_pitch = db["pitches"].find_one({"name": pitch_data.model_dump().get('name')})
    if db_pitch:
        raise HTTPException(status_code=404, detail="Pitch with the same name already exists")
    geo_location = get_geo(pitch_data.location)
    pitch_updated_data = create_pitch_helper(pitch_data.model_dump(), geo_location[0])
    print('last check>>>', pitch_updated_data)
    pitch = db["pitches"].insert_one(pitch_updated_data)
    # return pitch_helper(inserted_pitch_data)
    inserted_pitch_id = pitch.inserted_id
    inserted_pitch_data = db["pitches"].find_one({"_id": inserted_pitch_id})
    
    # Can now access the entire inserted document using inserted_pitch_data
    if inserted_pitch_data:
        return pitch_helper(inserted_pitch_data)  # Return the full document in the response


# Retrieve all pitches
def get_all_pitches() -> List[dict]:
    db = get_db()
    pitches = []
    db_pitches = db["pitches"].find()
    if db_pitches:
        for pitch in db_pitches:
            pitches.append(pitch_helper(pitch))
    return pitches

# Retrieve a single pitch by id
def get_pitch(id: str) -> dict:
    db = get_db()
    pitch = db["pitches"].find_one({"_id": ObjectId(id)})
    if pitch:
        return pitch_helper(pitch)

# Update a pitch by id
def update_pitch(id: str, pitch_data: UpdatePitchModel) -> dict:
    db = get_db()
    # Ensure you have logic to handle the case where the pitch does not exist.
    db["pitches"].update_one({"_id": ObjectId(id)}, {"$set": pitch_data.dict(exclude_unset=True)})
    updated_pitch = db["pitches"].find_one({"_id": ObjectId(id)})
    if updated_pitch:
        return pitch_helper(updated_pitch)

# Delete a pitch by id
def delete_pitch(id: str) -> bool:
    db = get_db()
    result: DeleteResult = db["pitches"].delete_one({"_id": ObjectId(id)})
    return result.deleted_count > 0
