from fastapi import APIRouter
from fastapi import Response, HTTPException, status, Path, Query, Header, Depends
from app.models.usuario_model import UsuarioModel

router = APIRouter()


@router.post('/app/v1/usuarios',
             status_code=status.HTTP_201_CREATED,
             description='cadastra novo caminhao',
             summary='cadastra caminhao',
             response_model=UsuarioModel)
async def post_usuario():
    pass



@router.get('/api/v1/usuarios',
            status_code=status.HTTP_200_OK,
            description='busca todos usuarios ou uma lista vazia',
            summary='lista todos os usuarios cadastrados',
            response_model=list[UsuarioModel])
async def get_usuarios():
    pass



@router.get('/app/v1/usuarios/{usuario_id}',
            status_code=status.HTTP_200_OK,
            description='busca usuario por id',
            summary='busca de usuario por id',
            response_model=UsuarioModel)
async def get_usuario_by_id(usuario_id: int):
    pass


@router.put('/app/v1/usuario/{usuario_id}',
            status_code=status.HTTP_200_OK,
            description='atualiza usuario por id',
            summary='atualiza usuario',
            response_model=UsuarioModel)
async def put_usuario(usuario_id: int):
    pass


@router.delete('/app/v1/usuarios/{usuario_id}',
               status_code=status.HTTP_204_NO_CONTENT,
               description='deleteta usuario por id',
               summary='deleta usuario',
               response_model=UsuarioModel)
async def delete_usuario(usuario_id: int):
    pass
