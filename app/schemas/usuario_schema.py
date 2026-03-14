from typing import Optional
from pydantic import BaseModel as ScBaseModel


class usuarioSchemas(ScBaseModel):
    id: Optional[int]
    nome: str
    telefone: str
    email: str
    cpf: str
    cidade: str
    
    class Config():
        orm_mode = True