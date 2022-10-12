from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from schemas.adotante import AdotanteSchema
from schemas.pet import PetSchema


class AdocaoSchema(BaseModel):
    pet: PetSchema
    adotante: AdotanteSchema
    data_cadastro: Optional[datetime] = datetime.now()
    obs: str = Field(max_length=100)
