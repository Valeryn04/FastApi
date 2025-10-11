from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ModuloBase(BaseModel):
    id_modulo: Optional[int] = None
    nombre_modulo: str
    descripcion: Optional[str] = None
    create_date: Optional[datetime] = None
    update_date: Optional[datetime] = None