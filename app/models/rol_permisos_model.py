from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RolPermisoBase(BaseModel):
    id_rol_permiso: Optional[int] = None
    id_modulo_rol: int
    id_permiso: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
