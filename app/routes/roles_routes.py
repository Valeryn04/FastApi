from fastapi import APIRouter
from controllers.roles_controller import RolController
from models.roles_model import RolBase

router = APIRouter(prefix="/roles")
controller = RolController()
pk_id = "id_rol"


@router.get("/")
async def obtener_roles():
    return controller.get_all()

@router.get(f"/{{{pk_id}}}")
async def obtener_rol_id(id_rol: int):
    return controller.get_by_id(id_rol)

@router.post("/")
async def crear_rol(rol: RolBase):
    return controller.create(rol)

@router.patch(f"/{{{pk_id}}}")
async def actualizar_rol(id_rol: int,rol: RolBase):
    return controller.update(id_rol, rol)

@router.delete(f"/{{{pk_id}}}")
async def eliminar_rol(id_rol: int):
    return controller.eliminar(id_rol)

