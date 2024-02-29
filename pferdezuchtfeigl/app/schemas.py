# schemas.py

from pydantic import BaseModel
from typing import List, Optional

class BreedingBase(BaseModel):
    date: Optional[date] = None
    stallion: str
    offspring_name: str

class BreedingCreate(BreedingBase):
    pass

class Breeding(BreedingBase):
    id: int
    mare_id: int

    class Config:
        orm_mode = True

class MareBase(BaseModel):
    name: str
    birth_year: int
    breed: str

class MareCreate(MareBase):
    pass

class Mare(MareBase):
    id: int
    breedings: List[Breeding] = []

    class Config:
        orm_mode = True

