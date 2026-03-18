from fastapi import FastAPI
from app.routers import caminhao_router


app = FastAPI(title='api-caminhao')
app.include_router(caminhao_router.router, tags=['caminhoes'])


if __name__=='__main__':
    import uvicorn
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True, log_level='info')