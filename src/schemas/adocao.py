from datetime import date, datetime
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field


class PedidoAdocaoSchema(BaseModel):
    data_pedido: date = date.today() 
    motivacao: str = Field(max_length=500)
    bio_adotante: str = Field(max_length=500)
    aceito_termos: bool = Field(default=True)
    em_aberto: bool = Field(default=True)
    deferido: bool = Field(default=False)

    class Config:
        arbitrary_types_allowed = False
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "motivacao": "Quero muito adotar este doguinho porque me identifiquei demais com ele e busco uma companhia para a vida toda. Prometo amá-lo e cuidar dele, na alegria, na tristeza, na saúde e na doença e sei que ele fará o mesmo por mim",
                "bio_adotante": "Sou extrovertida, adoro viajar (e pretendo levar o pet junto sempre), trabalho CLT homeoffice. Sou solteira, tenho 40 anos, sem filhos e não tenho outros pets. Moro em apartamento telado, de 40m",
                "aceito_termos": True
            }
        }
        
        
#upsert
class StatusAdocaoSchema(BaseModel):
    deferido: bool = Field(default=True)
    data_deferimento: datetime = datetime.now()
    
    class Config:
        arbitrary_types_allowed = False
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "deferido": True
            }
        }
        