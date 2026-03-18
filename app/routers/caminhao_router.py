from fastapi import APIRouter
from fastapi import Response, HTTPException, status, Path, Query, Header, Depends
from app.models.caminhao_model import CaminhaoModel
from typing import Optional, Any, List, Dict
from app.schemas.caminhao_schema import CaminhaoSchemas
from app.core.deps import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


router = APIRouter()

@router.post('/app/v1/caminhoes',
          status_code=status.HTTP_201_CREATED,
          description='adiciona novo caminhao',
          summary='adiciona novo caminhao',
          response_model=CaminhaoSchemas)
async def post_caminhao(caminhao: CaminhaoSchemas, db: AsyncSession = Depends(get_session)):
    novo_caminhao = CaminhaoModel(**caminhao.dict())
    db.add(novo_caminhao)
    await db.commit()
    await db.refresh(novo_caminhao)
    
    return novo_caminhao



@router.get('/app/v1/caminhoes/{caminhao_id}',
            status_code=status.HTTP_200_OK,
            description='Busca caminhao por id',
            summary='busca caminhao por id',
             response_model=CaminhaoSchemas)
async def get_caminhao_by_id(caminhao_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CaminhaoModel).where(CaminhaoModel.id == caminhao_id)
        result = await session.execute(query)
        caminhao = result.scalar_one_or_none()
        
        if not caminhao:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='caminhao nao encontrado'
            )

        return caminhao
    


@router.get('/app/v1/caminhoes',
            status_code=status.HTTP_200_OK,
            description='mostra todos os camnhoes ou uma lista vazia',
            summary='lista todos os caminhoes cadastrados',
            response_model=List[CaminhaoSchemas])
async def get_list_caminhao(db: AsyncSession = Depends(get_session)):
    async with db as session:
        
        query = select(CaminhaoModel)
        result = await session.execute(query) 
        caminhoes: List[CaminhaoModel] = result.scalars().all()
        
        return caminhoes
    



@router.put('/app/v1/caminhoes/{caminhao_id}',
            status_code=status.HTTP_202_ACCEPTED,
            description='atualiza caminhao por id',
            summary='atualiza caminhao',
            response_model=CaminhaoSchemas)
async def put_caminhao( caminhao_id: int,
                       caminhao: CaminhaoSchemas,
                       db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CaminhaoModel).where(CaminhaoModel.id == caminhao_id)
        result = await session.execute(query)
        caminhao_up = result.scalar_one_or_none()
        
        if caminhao_up:
            caminhao_up.modelo = caminhao.modelo 
            caminhao_up.placa = caminhao.placa
            caminhao_up.consumo = caminhao.consumo
            caminhao_up.tamanho = caminhao.tamanho
            caminhao_up.largura = caminhao.largura
            caminhao_up.carga_total = caminhao.carga_total
            await session.commit()
            
            return caminhao_up
        else:
            raise HTTPException(detail='caminhao nao encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)
    


@router.delete('/app/v1/caminhoes/{caminhao_id}',
               status_code=status.HTTP_204_NO_CONTENT,
               description='deleta caminhao por id',
               summary='deleta caminhao',)
async def delete_caminhao( caminhao_id: int,
                       db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CaminhaoModel).where(CaminhaoModel.id == caminhao_id)
        result = await session.execute(query)
        caminhao_del = result.scalar_one_or_none()
        
        if caminhao_del:
            await session.delete(caminhao_del)
            await session.commit()
    
    
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='caminhao nao encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)