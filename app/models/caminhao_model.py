from typing import Optional
from app.core.configs import settings
from sqlalchemy import Column, Integer, String, Float


class CaminhaoModel(settings.DBBaseModel):
    __tablename__ = 'caminhoes'
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    modelo: str = Column(String(50),  nullable=False)
    placa: str = Column(String(7), unique=True, index=True, nullable=False)
    consumo: float = Column(Float,  nullable=False)
    carga_total: float = Column(Float, nullable=False)
    tamanho: float = Column(Float, nullable=False)
    largura: Optional[Float] = Column(Float, nullable=True)

    class config:
        from_attributes = True

