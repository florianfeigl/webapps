# models.py

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Mare(Base):
    __tablename__ = "mares"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birth_year = Column(Integer)
    breed = Column(String)
    breedings = relationship("Breeding", back_populates="mare")

class Breeding(Base):
    __tablename__ = "breeding"
    id = Column(Integer, primary_key=True, index=True)
    mare_id = Column(Integer, ForeignKey('mares.id'))
    date = Column(Date)
    stallion = Column(String)
    offspring_name = Column(String)
    mare = relationship("Mare", back_populates="breedings")

class Stallion(Base):
    __tablename__ = "stallions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birth_year = Column(Integer)
    achievements = relationship("Achievements", back_populates="stallion")

class Achievements(Base):
    __tablename__ = "achievements"
    id = Column(Integer, primary_key=True, index=True)
    stallion_id = Column(Integer, ForeignKey('stallions.id'))
    date = Column(Date)
    achievement = Column(String)
    stallion = relationship("Stallion", back_populates="achievements")

