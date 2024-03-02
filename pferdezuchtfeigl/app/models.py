# models.py

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Horse(Base):
    __tablename__ = "horses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    sex = Column(String)
    birth = Column(Date)
    color = Column(String)
    region = Column(String)
    # Beziehungen
    pedigree = relationship("Pedigree", back_populates="horse", uselist=False)
    breedings_as_dam = relationship("Breeding", back_populates="dam", foreign_keys='Breeding.dam_id')
    breedings_as_sire = relationship("Breeding", back_populates="sire", foreign_keys='Breeding.sire_id')

class Pedigree(Base):
    __tablename__ = "pedigree"
    id = Column(Integer, primary_key=True, index=True)
    horse_id = Column(Integer, ForeignKey('horses.id'))
    sire_id = Column(Integer, ForeignKey('horses.id'))
    dam_id = Column(Integer, ForeignKey('horses.id'))
    damsire_id = Column(Integer, ForeignKey('horses.id'))
    # Rückverweise
    horse = relationship("Horse", back_populates="pedigree")
    sire = relationship("Horse", foreign_keys=[sire_id])
    dam = relationship("Horse", foreign_keys=[dam_id])
    damsire = relationship("Horse", foreign_keys=[damsire_id])

class Breeding(Base):
    __tablename__ = "breeding"
    id = Column(Integer, primary_key=True, index=True)
    year = Column(Date)
    dam_id = Column(Integer, ForeignKey('horses.id'))
    sire_id = Column(Integer, ForeignKey('horses.id'))
    offspring_id = Column(Integer, ForeignKey('horses.id'))
    attribute = Column(String)
    # Beziehungen
    dam = relationship("Horse", back_populates="breedings_as_dam", foreign_keys=[dam_id])
    sire = relationship("Horse", back_populates="breedings_as_sire", foreign_keys=[sire_id])
    offspring = relationship("Horse", foreign_keys=[offspring_id])

