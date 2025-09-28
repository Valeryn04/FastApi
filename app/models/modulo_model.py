from pydantic import BaseModel
from typing import Optional


class Modulo(BaseModel):
    idModulo: int
    nombre: str
    descripcion: Optional[str] = None