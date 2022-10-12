from pydantic import BaseModel, EmailStr, Field, validator
from bson import ObjectId


class UsuarioSchema(BaseModel):
    email: EmailStr = Field(unique=True, index=True)
    senha: str = Field(max_length=20)
    ativo: bool = Field(default=True)
    admin: bool = Field(default=False)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "email": "khaleesi@dracarys.com",
                "senha": "motherOfDragons3",
                "ativo": True,
                "admin": False
            }
        }