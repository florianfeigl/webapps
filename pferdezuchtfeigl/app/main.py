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

@app.post("/horses/", response_model=schemas.Horse, status_code=status.HTTP_201_CREATED)
def create_horse(horse: schemas.HorseCreate, db: Session = Depends(get_db)):
	db_horse = crud.create_horse(db=db, horse=horse)
    return db_horse

@app.get("/horses/{horse_id}", response_model=schemas.HorseCreate)
def read_horse(horse_id: int, db: Session = Depends(get_db)):
	db_horse = crud.get_horse(db, horse_id=horse_id)
	if db_horse is None:
		raise HTTPException(status_code=404, detail="Horse not found.")
	return db_horse
