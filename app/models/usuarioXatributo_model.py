from pydantic import BaseModel
from typing import Optional


class UsuarioAtributoBase(BaseModel):
    idUsuario: int
    idAtributo: int
    valor: Optional[str] = None
