from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ModuloRolBase(BaseModel):
    id_modulo_rol: Optional[int] = None
    id_modulo: int
    id_rol: int
    estado: Optional[bool] = True
    create_date: Optional[datetime] = None
    update_date: Optional[datetime] = None
