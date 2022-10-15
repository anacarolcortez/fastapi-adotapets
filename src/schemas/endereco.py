from pydantic import BaseModel, EmailStr, Field
from bson import ObjectId


class EnderecoSchema(BaseModel):
    logradouro: str = Field(max_length=80)
    numero: int
    complemento: str = Field(max_length=10)
    bairro: str = Field(max_length=20)
    cidade: str = Field(max_length=40)
    estado: str = Field(max_length=2)
    cep: str = Field(max_length=8)  
    
    class Config:
        arbitrary_types_allowed = False
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "logradouro": "Av Westeros",
                "numero": "12000",
                "complemento": "2 andar",
                "bairro": "Royal",
                "cidade": "Westeros",
                "estado": "SP",
                "cep": "01021030"
            }
        }
        
class EnderecoAdotanteSchema(BaseModel):
    adotante: EmailStr = Field(unique=True)
    logradouro: str = Field(max_length=80)
    numero: int
    complemento: str = Field(max_length=10)
    bairro: str = Field(max_length=20)
    cidade: str = Field(max_length=40)
    estado: str = Field(max_length=2)
    cep: str = Field(max_length=8)  