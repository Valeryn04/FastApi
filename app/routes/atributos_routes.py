from fastapi import APIRouter, Body
from models.atributo_model import AtributoBase, AtributoUpdate
from controllers.atributo_controller import AtributoController


router = APIRouter(prefix="/atributos")
atributo_controller = AtributoController()

# Obtener todos los atributos
@router.get("/", response_model=dict)
async def get_all_atributos():
    rpta = atributo_controller.get_all()
    return rpta

# Obtener un atributo por ID
@router.get("/{atributo_id}", response_model=dict)
async def get_atributo_by_id(atributo_id: int):
    rpta = atributo_controller.get_by_id(atributo_id)
    return rpta

# Crear atributo
@router.post("/", response_model=dict)
async def create_atributo(atributo: AtributoBase):
    rpta = atributo_controller.create(atributo)
    return rpta

# Actualizar atributo
@router.patch("/{atributo_id}", response_model=dict)
async def update_atributo(atributo_id: int, atributo: AtributoUpdate):
    rpta = atributo_controller.update(atributo_id, atributo)
    return rpta

# Eliminar atributo
@router.delete("/{atributo_id}", response_model=dict)
async def delete_atributo(atributo_id: int):
    rpta = atributo_controller.eliminar(atributo_id)
    return rpta