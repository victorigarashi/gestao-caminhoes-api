from typing import Optional
from pydantic import BaseModel as ScBaseModel
from pydantic import Field


class CaminhaoSchemas(ScBaseModel):
    id: Optional[int]
    modelo: str
    placa: str = Field(..., min_length=7, max_length=7)
    consumo: float = Field(..., gt=0)
    carga_total: float = Field(..., gt=0)
    tamanho: float = Field(..., gt=0)
    largura: float = Field(..., gt=0)
    
    class Config():
        orm_mode = True

    