from fastapi import APIRouter, HTTPException
from config.db_config import get_db_connection
from controllers.usuario_controller import UsuarioController
from models.usuario_model import UsuarioBase

router = APIRouter()

usuario_controller = UsuarioController()

# Crear usuario
@router.post("/usuarios", response_model=dict)
async def create_usuario(usuario: UsuarioBase):
    rpta = usuario_controller.create_usuario(usuario)
    return rpta


# Obtener un usuario por ID
@router.get("/usuarios/{usuario_id}", response_model=UsuarioBase)
async def get_usuario(usuario_id: int):
    rpta = usuario_controller.get_usuario(usuario_id)
    return rpta


# Obtener todos los usuarios
@router.get("/usuarios", response_model=dict)
async def get_usuarios():
    rpta = usuario_controller.get_usuarios()
    return rpta
