from fastapi import HTTPException, status
from pydantic import BaseModel, EmailStr, Field, validator
from bson import ObjectId


class UsuarioSchema(BaseModel):
    email: EmailStr = Field(unique=True, index=True)
    senha: str = Field(max_length=20)
    ativo: bool = Field(default=True)
    admin: bool = Field(default=False)
    
    @validator("senha")
    def password_validation(cls, v):
        if len(v) < 5 or len(v) > 15:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Senha deve ter entre 5 e 15 caracteres")
        return v

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