from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PermisoBase(BaseModel):
    id_permiso: Optional[int] = None
    nombre_permiso: str
    descripcion: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
