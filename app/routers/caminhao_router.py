from fastapi import APIRouter
from fastapi import Response, HTTPException, status, Path, Query, Header, Depends
from time import sleep
from app.models.caminhao_model import CaminhaoModel
from typing import Optional, Any, List, Dict


router = APIRouter()

@router.post('/app/v1/caminhoes',
          status_code=status.HTTP_201_CREATED,
          description='adiciona novo caminhao',
          summary='adiciona novo caminhao',
          response_model=CaminhaoModel)
async def post_caminhao():
    pass



@router.get('/app/v1/caminhoes/{caminhao_id}',
            status_code=status.HTTP_200_OK,
            description='Busca caminhao por id',
            summary='busca caminhao por id',
             response_model=CaminhaoModel)
async def get_caminhao_by_id():
    pass


@router.get('/app/v1/caminhoes',
            status_code=status.HTTP_200_OK,
            description='mostra todos os camnhoes ou uma lista vazia',
            summary='lista todos os caminhoes cadastrados',
            response_model=List[CaminhaoModel])
async def get_list_caminhao():
    pass



@router.put('/app/v1/caminhoes/{caminhao_id}',
            status_code=status.HTTP_200_OK,
            description='atualiza caminhao por id',
            summary='atualiza caminhao',
            response_model=CaminhaoModel)
async def put_caminhao():
    pass


@router.delete('/app/v1/caminhoes/{caminhao_id}',
               status_code=status.HTTP_204_NO_CONTENT,
               description='deleta caminhao por id',
               summary='deleta caminhao',
               response_model=CaminhaoModel)
async def delete_caminhao():
    pass
