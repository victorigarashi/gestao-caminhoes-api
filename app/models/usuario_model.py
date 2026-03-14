from core.configs import settings
from sqlalchemy import Column, Integer, String

class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuarios'
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String, nullable=False)
    telefone: str = Column(String(20), nullable=False)
    email: str = Column(String, nullable=False, index=True, unique=True)
    cpf: str = Column(String, nullable=False)
    cidade: str = Column(String, nullable=False)
    
    
    