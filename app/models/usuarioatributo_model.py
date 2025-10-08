from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UsuarioAtributoBase(BaseModel):
    id_usuario_atributo: Optional[int] = None
    id_usuario: int
    id_atributo: int
    valor: str
    create_date: Optional[datetime] = None
    update_date: Optional[datetime] = None
