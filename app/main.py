# main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/mares/", response_model=schemas.Mare)
def create_mare(mare: schemas.MareCreate, db: Session = Depends(get_db)):
    return crud.create_mare(db=db, mare=mare)

# Weitere Routen hinzufügen

