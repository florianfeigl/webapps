# schemas.py

from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class HorseCreate(BaseModel):
	name: str
	sex: str
	birth: date
	color: str
	region: str
	
	@validator('sex')
	def correct_sex_formatchecker(cls, sex_input):
		if len(sex_input) != 1 or v not in ('M', 'S', 'G'):
			raise ValueError('Sex must be \[M\]are, \[S\]tallion or \[G\]elding.')
		return sex_input
		
	class Config:
		orm_mode = True
