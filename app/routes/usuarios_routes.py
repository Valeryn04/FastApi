from fastapi import APIRouter, Body, HTTPException
from models.usuario_model import UsuarioBase, UsuarioUpdate, UsuarioCreateWithAtributos
from controllers.usuario_controller import UsuarioController
from controllers.usuarioatributo_controller import UsuarioAtributoController
from typing import Optional, List


router = APIRouter()
usuario_controller = UsuarioController()
usuario_atributo_controller = UsuarioAtributoController()

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

# ✅ ACTUALIZAR USUARIO - Solo datos del usuario, sin atributos
@router.patch("/usuarios/{usuario_id}", response_model=dict)
async def update_usuario(usuario_id: int, usuario: UsuarioUpdate):
    """Actualiza los datos básicos del usuario"""
    rpta = usuario_controller.update(usuario_id, usuario)
    return rpta

# ✅ ALTERNATIVA - Si PATCH sigue fallando, usa PUT
@router.put("/usuarios/{usuario_id}", response_model=dict)
async def update_usuario_put(usuario_id: int, usuario: UsuarioUpdate):
    """Actualiza los datos básicos del usuario (alternativa con PUT)"""
    try:
        result = usuario_controller.update(usuario_id, usuario)
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

# Cambiar estado del usuario
@router.put("/usuarios/{usuario_id}/estado", response_model=dict)
async def cambiar_estado_usuario(usuario_id: int, estado: bool = Body(..., embed=True)):
    rpta = usuario_controller.cambiar_estado(usuario_id, estado)
    return rpta

# Obtener atributos de un usuario específico
@router.get("/usuarios/{id_usuario}/atributos")
def obtener_atributos_de_usuario(id_usuario: int):
    """Obtiene todos los atributos con valores de un usuario específico"""
    try:
        resultado = usuario_atributo_controller.get_by_usuario(id_usuario)
        return {
            "resultado": resultado,
            "total": len(resultado)
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")