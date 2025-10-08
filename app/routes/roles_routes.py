from fastapi import APIRouter
from controllers.rol_controller import RolController
from models.rol_model import RolBase

router = APIRouter()
controller = RolController()

@router.post("/roles")
async def crear_rol(rol: RolBase):
    return controller.create_rol(rol)

@router.get("/roles")
async def obtener_roles():
    return controller.get_roles()
