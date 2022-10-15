from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId
from enum import Enum

from src.schemas.sexo import Sexo


class Tipo(str, Enum):
    cachorro = "cachorro"
    gato = "gato"


class Porte(str, Enum):
    pequeno = "pequeno"
    medio = "medio"
    grande = "grande"


class PetSchema(BaseModel):
    nome: str = Field(max_length=20, unique=True)
    data_nasc: date
    data_cadastro: Optional[datetime] = datetime.now()
    sexo: Sexo
    raca: str = Field(max_length=20)
    porte: Porte
    cor: str = Field(max_length=20)
    tipo: Tipo
    pcd: bool = Field(default=False)
    foto: Optional[str]
    obs: Optional[str] = Field(max_length=200)
    adotado: bool = Field(default=False)

    class Config:
        arbitrary_types_allowed = False
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "nome": "khaleesi",
                "data_nasc": "2020-09-15",
                "sexo": "f",
                "raca": "srd",
                "porte": "medio",
                "cor": "caramelo e branco",
                "tipo": "cachorro",
                "pcd": False,
                "foto": "imgur.com/khaleesi.jpg",
                "obs": "brincalhona e sociável; foi resgatada grávida e teve três fihotes: drogo, viserion e rhaegal",
                "adotado": False
            }
        }


class PetUpdateSchema(BaseModel):
    pcd: Optional[bool] = Field(default=False)
    foto: Optional[str]
    obs: Optional[str] = Field(max_length=200)
    
    class Config:
        arbitrary_types_allowed = False
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "pcd": True,
                "foto": "imgur.com/khaleesi_update.jpg",
                "obs": "enxerga pouco no olho esquerdo"
            }
        }
