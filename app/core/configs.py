from typing import List
from pydantic import AnyHttpUrl, BaseSettings
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://projeto:fast@localhost:5432/facul"
    DBBaseModel = declarative_base()
    
    
    class config:
        case_sensitive = True
    
    
    
    
settings = Settings()