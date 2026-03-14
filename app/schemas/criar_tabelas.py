from app.core.configs import settings
from app.core.database import engine

async def create_table()-> None:
        import app.models.__all_models
        
        async with engine.begin() as conn:
            await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
            await conn.run_sync(settings.DBBaseModel.metadata.create_all)   

if __name__=='__main__' :
    import asyncio
    
    asyncio.run(create_table())