from typing import Optional
from pydantic import BaseModel as ScBaseModel


class caminhaoSchemas(ScBaseModel):
    id: Optional[int]
    modelo: str
    placa: str
    consumo: float
    carga_total: float
    tamanho: float
    largura: float
    
    class Config():
        orm_mode = True