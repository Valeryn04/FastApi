from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AtributoBase(BaseModel):
    id_atributo: Optional[int] = None
    nombre: str
    descripcion: Optional[str] = None
    create_date: Optional[datetime] = None
    update_date: Optional[datetime] = None
