from sqlalchemy.orm import Session

import models, schemas


def get_note(db: Session, note_id: str):
    return db.query(models.Note).filter(models.Note.id == note_id).first()

def delete_note(db: Session, note_id: str):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    db.delete(db_note)
    db.commit()
    return {}

def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Note).order_by(models.Note.id).offset(skip).limit(limit).all()


def create_note(db: Session, note: schemas.NoteCreate):
    db_note = models.Note(text=note.text)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def update_note(db: Session, note: schemas.Note):   
    db_note = db.query(models.Note).filter(models.Note.id == note.id).first()
    db_note.text = note.text
    db_note.title = db_note.title
    db.commit()
    db.refresh(db_note)
    return db_note