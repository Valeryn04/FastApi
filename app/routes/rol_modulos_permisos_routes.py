from fastapi import APIRouter
from app.controllers.rol_modulo_permisos_controller import RolModuloPermisoController
from app.models.rol_modulo_permisos import RolModuloPermisoBase
from typing import Optional

router = APIRouter(prefix="/rol-permisos")
controller = RolModuloPermisoController()
pk_id = "id_asignacion"

@router.get("/")
async def obtener_asignaciones():
    return controller.get_all()

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