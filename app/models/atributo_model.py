from pydantic import BaseModel
from typing import Optional


class AtributoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
