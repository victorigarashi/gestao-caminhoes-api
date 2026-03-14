from fastapi import FastAPI
from app.routers import caminhao_router, usuario_router


app = FastAPI()
app.include_router(caminhao_router.router, tags=['caminhoes'])
app.include_router(usuario_router.router, tags=['usuarios'])


if __name__=='__main__':
    import uvicorn
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)