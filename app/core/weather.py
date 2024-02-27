from fastapi import APIRouter, HTTPException, Path, Body
from typing import List

from app.models import PitchModel, UpdatePitchModel
router = APIRouter()