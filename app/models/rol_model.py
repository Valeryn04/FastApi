from pydantic import BaseModel
from typing import Optional


class Rol(BaseModel):
    idRol: int
    nombre: str
    descripcion: Optional[str] = None
