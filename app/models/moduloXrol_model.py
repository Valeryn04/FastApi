from pydantic import BaseModel
from typing import Optional


class ModuloRolBase(BaseModel):
    idRol: int
    idModulo: int
    estado: Optional[int] = None
