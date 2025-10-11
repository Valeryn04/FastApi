# models/usuarioatributo_model.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UsuarioAtributoCreate(BaseModel):
    id_atributo: int
    valor: str

class UsuarioAtributoBase(UsuarioAtributoCreate):
    id_usuario_atributo: Optional[int] = None
    id_usuario: Optional[int] = None
    create_date: Optional[datetime] = None
    update_date: Optional[datetime] = None

