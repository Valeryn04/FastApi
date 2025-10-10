from fastapi import APIRouter, Body
from models.atributo_model import AtributoBase, AtributoUpdate
from controllers.atributo_controller import AtributoController

router = APIRouter()
atributo_controller = AtributoController()

# Obtener todos los atributos
@router.get("/atributos", response_model=dict)
async def get_all_atributos():
    rpta = atributo_controller.get_all()
    return rpta

# Obtener un atributo por ID
@router.get("/atributos/{atributo_id}", response_model=dict)
async def get_atributo_by_id(atributo_id: int):
    rpta = atributo_controller.get_by_id(atributo_id)
    return rpta

# Crear atributo
@router.post("/atributos", response_model=dict)
async def create_atributo(atributo: AtributoBase):
    rpta = atributo_controller.create(atributo)
    return rpta

# Actualizar atributo
@router.patch("/atributos/{atributo_id}", response_model=dict)
async def update_atributo(atributo_id: int, atributo: AtributoUpdate):
    rpta = atributo_controller.update(atributo_id, atributo)
    return rpta

# Eliminar atributo
@router.delete("/atributos/{atributo_id}", response_model=dict)
async def delete_atributo(atributo_id: int):
    rpta = atributo_controller.eliminar(atributo_id)
    return rpta

# Ruta para obtener los atributos por rol
@router.get("/atributos/rol/{rol_id}")
def obtener_atributos_por_rol(rol_id: int):
    atributo_controller = AtributoController()
    return atributo_controller.get_atributos_por_rol(rol_id)