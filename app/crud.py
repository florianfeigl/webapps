# crud.py

from sqlalchemy.orm import Session
from . import models, schemas

def create_mare(db: Session, mare: schemas.MareCreate):
    db_mare = models.Mare(name=mare.name, birth_year=mare.birth_year, breed=mare.breed)
    db.add(db_mare)
    db.commit()
    db.refresh(db_mare)
    return db_mare
