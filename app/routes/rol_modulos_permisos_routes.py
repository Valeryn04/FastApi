from fastapi import APIRouter
from app.controllers.rol_modulo_permisos_controller import RolModuloPermisoController
from app.models.rol_modulo_permisos import RolModuloPermisoBase
from typing import Optional

router = APIRouter(prefix="/rol-permisos")
controller = RolModuloPermisoController()
pk_id = "id_asignacion"


# 🔹 Obtener todas las asignaciones
@router.get("/")
async def obtener_asignaciones():
    return controller.get_all()

# 🔹 Obtener módulos y permisos por ID de rol (sin autenticación)
@router.get("/modulos-usuario/{id_rol}", summary="Obtener módulos y permisos de un rol específico (sin token)")
async def obtener_modulos_por_rol(id_rol: int):
    """
    Devuelve los módulos y funcionalidades asignadas al rol indicado por su ID.
    Ideal para pruebas o consultas sin necesidad de JWT.
    """
    return controller.get_modulos_por_rol(id_rol)



@router.get(f"/{{{pk_id}}}")
async def obtener_asignacion_id(id_asignacion: int):
    return controller.get_by_id(id_asignacion)

@router.post("/")
async def crear_asignacion(relacion: RolModuloPermisoBase):
    return controller.create(relacion)

@router.patch(f"/{{{pk_id}}}")
async def actualizar_asignacion(id_asignacion: int, relacion: RolModuloPermisoBase):
    """Actualiza una asignación existente (cambiar el rol o la funcionalidad)."""
    return controller.update(id_asignacion, relacion)

@router.delete(f"/{{{pk_id}}}")
async def eliminar_asignacion(id_asignacion: int):
    return controller.eliminar(id_asignacion)