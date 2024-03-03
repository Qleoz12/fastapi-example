from typing import List, Optional
from pydantic import BaseModel


class NoteBase(BaseModel):
    title: str =""
    text: str


class NoteCreate(NoteBase):
    pass


class Note(BaseModel):
    id: str
    text: str

    class Config:
        orm_mode = True


class NoteResponse(NoteBase):
    id: str
