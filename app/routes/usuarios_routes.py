from fastapi import APIRouter
from fastapi import Body
from models.usuario_model import UsuarioBase, UsuarioUpdate, UsuarioCreateWithAtributos
from controllers.usuario_controller import UsuarioController

router = APIRouter()
usuario_controller = UsuarioController()

# Obtener todos los usuarios
@router.get("/usuarios", response_model=dict)
async def get_all_usuarios():
    rpta = usuario_controller.get_all()
    return rpta

# Obtener un usuario por ID
@router.get("/usuarios/{usuario_id}", response_model=dict)
async def get_usuario_by_id(usuario_id: int):
    rpta = usuario_controller.get_by_id(usuario_id)
    return rpta

# Crear usuario
@router.post("/usuarios", response_model=dict)
async def create_usuario(usuario: UsuarioCreateWithAtributos):
    rpta = usuario_controller.create(usuario)
    return rpta

# Actualizar usuario
@router.patch("/usuarios/{usuario_id}", response_model=dict)
async def update_usuario(usuario_id: int, usuario: UsuarioUpdate):
    rpta = usuario_controller.update(usuario_id, usuario)
    return rpta

# Desactivar usuario (Soft Delete)
@router.put("/usuarios/{usuario_id}/estado", response_model=dict)
async def cambiar_estado_usuario(usuario_id: int, estado: bool = Body(..., embed=True)):
    rpta = usuario_controller.cambiar_estado(usuario_id, estado)
    return rpta