# initialize_db.py

from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import Base, Horse, Pedigree, Breeding

# Erstellen Sie alle Tabellen
Base.metadata.create_all(bind=engine)

# Neue Session erstellen
db = SessionLocal()

# Pferd erstellen
horse = Horse(name="Thunder", sex="M", birth=date(2010, 5, 17), color="Black", region="Bavaria")
db.add(horse)
db.commit()

# Abstammung erstellen
pedigree = Pedigree(horse_id=horse.id, sire_id=1, dam_id=2, damsire_id=3)  # Angenommen, diese IDs existieren bereits
db.add(pedigree)
db.commit()

# Zuchtinformation erstellen
breeding = Breeding(year=date(2020, 6, 15), dam_id=2, sire_id=horse.id, offspring_id=4, attribute="Winner")  # Angenommen, diese IDs existieren bereits
db.add(breeding)
db.commit()

# Session schließen
db.close()

