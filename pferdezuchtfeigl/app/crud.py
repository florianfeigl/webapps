# crud.py

from sqlalchemy.orm import Session
from . import models, schemas

def create_horse(db: Session, horse: schemas.HorseCreate):
    db_horse = models.Horse(name=horse.name, sex=horse.sex, birth=horse.birth, color=horse.color, region=horse.region)
    db.add(db_horse)
    db.commit()
    db.refresh(db_horse)
    return db_horse
