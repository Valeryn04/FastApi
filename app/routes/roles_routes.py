from fastapi import APIRouter
from controllers.roles_controller import RolController
from models.roles_model import RolBase

router = APIRouter()
controller = RolController()
pk_id = "id_rol"


@router.get("/roles")
async def obtener_roles():
    return controller.get_all()

@router.get(f"/roles/{{{pk_id}}}")
async def obtener_rol_id(id_rol: int):
    return controller.get_by_id(id_rol)

@router.post("/roles")
async def crear_rol(rol: RolBase):
    return controller.create(rol)

@router.patch(f"/roles/{{{pk_id}}}")
async def actualizar_rol(id_rol: int,rol: RolBase):
    return controller.update(id_rol, rol)

@router.delete(f"/roles/{{{pk_id}}}")
async def eliminar_rol(id_rol: int):
    return controller.eliminar(id_rol)

