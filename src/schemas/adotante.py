import re
from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field, validator
from bson import ObjectId
from fastapi import HTTPException, status

from src.schemas.endereco import EnderecoSchema
from src.schemas.sexo import Sexo


class AdotanteSchema(BaseModel):
    nome: str = Field(max_length=80)
    cpf: str
    telefone: str
    data_nasc: date
    sexo: Sexo
    endereco: EnderecoSchema
    obs: Optional[str] = Field(max_length=100)
    data_cadastro: datetime = datetime.now()

    class Config:
        arbitrary_types_allowed = False
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "nome": "Daenerys Targaryen",
                "cpf": "123.456.789-10",
                "telefone": "(11) 98765-4321",
                "data_nasc": "2000-03-30",
                "sexo": "f",
                "endereco": {
                    "logradouro": "Av Westeros",
                    "numero": "12000",
                    "complemento": "2 andar",
                    "bairro": "Royal",
                    "cidade": "Westeros",
                    "estado": "SP",
                    "cep": "01021030"
                },
                "obs": "família com criança de 5 anos, sem pets"
            }
        }

    @validator("telefone")
    def phone_validation(cls, v):
        regex = r"^\([1-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$"
        if v and not re.search(regex, v, re.I):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Formato de telefone deve ser (XX) XXXX-XXXX ou (XX) 9XXXX-XXXX")
        return v

    @validator("cpf")
    def cpf_format_validator(cls, v):
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', v):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Formato do cpf deve ser XXX.XXX.XXX-XX")
        return v


class AdotanteUpdateSchema(BaseModel):
    telefone: Optional[str]
    endereco: EnderecoSchema
    obs: Optional[str] = Field(max_length=100)

    @validator("telefone")
    def phone_validation(cls, v):
        regex = r"^\([1-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$"
        if v and not re.search(regex, v, re.I):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Formato de telefone deve ser (XX) XXXX-XXXX ou (XX) 9XXXX-XXXX")
        return v

    class Config:
        arbitrary_types_allowed = False
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "telefone": "(21) 98765-4321",
                "endereco": {
                    "logradouro": "Av Westeros",
                    "numero": "12000",
                    "complemento": "2 andar",
                    "bairro": "Royal",
                    "cidade": "Westeros",
                    "estado": "SP",
                    "cep": "01021030"
                },
                "obs": "família com criança de 5 anos, sem pets"
            }
        }