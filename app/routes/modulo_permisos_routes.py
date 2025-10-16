from fastapi import APIRouter
from app.controllers.modulo_permisos_controller import ModuloPermisoController
from app.models.modulo_permisos_model import ModuloPermisoBase, ModuloPermisoUpdate

router = APIRouter(prefix="/modulos-permisos")
controller = ModuloPermisoController()
pk_id = "id_funcionalidad"


@router.get("/")
async def obtener_funcionalidades():
    return controller.get_all()

@router.get(f"/{{{pk_id}}}")
async def obtener_funcionalidad_id(id_funcionalidad: int):
    return controller.get_by_id(id_funcionalidad)

@router.post("/")
async def crear_funcionalidad(funcionalidad: ModuloPermisoBase):
    return controller.create(funcionalidad)

@router.patch(f"/{{{pk_id}}}")
async def actualizar_funcionalidad(id_funcionalidad: int, funcionalidad: ModuloPermisoUpdate):
    return controller.update(id_funcionalidad, funcionalidad)

@router.delete(f"/{{{pk_id}}}")
async def eliminar_funcionalidad(id_funcionalidad: int):
    return controller.eliminar(id_funcionalidad)