# app/routes/note_routes.py
from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from datetime import datetime
from app.db.mongo import notes_collection
from app.models.note_model import NoteModel, NoteDBModel

router = APIRouter(prefix="/notes", tags=["notes"])

# GET all notes
@router.get("/", response_model=list[NoteDBModel])
async def get_notes():
    notes_cursor = notes_collection.find()
    notes = await notes_cursor.to_list(length=100)
    return notes

# GET note by ID
@router.get("/{note_id}", response_model=NoteDBModel)
async def get_note(note_id: str):
    if not ObjectId.is_valid(note_id):
        raise HTTPException(status_code=400, detail="Invalid note ID")
    note = await notes_collection.find_one({"_id": ObjectId(note_id)})
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

# POST create new note
@router.post("/", response_model=NoteDBModel, status_code=status.HTTP_201_CREATED)
async def create_note(note: NoteModel):
    note_data = note.dict()
    note_data["created_at"] = datetime.utcnow()
    note_data["updated_at"] = datetime.utcnow()
    result = await notes_collection.insert_one(note_data)
    new_note = await notes_collection.find_one({"_id": result.inserted_id})
    return new_note

# PUT update note
@router.put("/{note_id}", response_model=NoteDBModel)
async def update_note(note_id: str, note: NoteModel):
    if not ObjectId.is_valid(note_id):
        raise HTTPException(status_code=400, detail="Invalid note ID")
    note_data = note.dict()
    note_data["updated_at"] = datetime.utcnow()
    updated = await notes_collection.find_one_and_update(
        {"_id": ObjectId(note_id)},
        {"$set": note_data},
        return_document=True
    )
    if updated is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated

# DELETE note
@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(note_id: str):
    if not ObjectId.is_valid(note_id):
        raise HTTPException(status_code=400, detail="Invalid note ID")
    result = await notes_collection.delete_one({"_id": ObjectId(note_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")
    return
