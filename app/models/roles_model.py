from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RolBase(BaseModel):
    id_rol: Optional[int] = None
    nombre: str
    descripcion: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
