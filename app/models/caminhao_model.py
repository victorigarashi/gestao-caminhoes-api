from typing import Optional
from core.configs import settings
from sqlalchemy import Column, Integer, String, Float


class CaminhaoModel(settings.DBBaseModel):
    __tablename__ = 'caminhoes'
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    modelo: str = Column(String(50),  nullable=False)
    placa: str = Column(String(7), unique=True, index=True, nullable=False)
    consumo: float = Column((float),  nullable=False)
    carga_total: float = Column((Float), nullable=False)
    tamanho: float = Column((float), nullable=False)
    largura: Optional[float] = Column(Float, nullable=True)



