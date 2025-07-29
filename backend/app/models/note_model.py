# app/models/note_model.py
from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId
import datetime

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, field):  # <-- accept 2 arguments
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return str(v)

# Base Note schema (for creating/updating)
class NoteModel(BaseModel):
    title: str
    content: str
    tags: Optional[List[str]] = []

# Schema returned from DB (includes _id, timestamps)
class NoteDBModel(NoteModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
        orm_mode = True
