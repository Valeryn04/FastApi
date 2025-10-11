from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RolModuloPermisoBase(BaseModel):
    id: Optional[int] = None   
    id_rol_fk: int   
    id_modulo_permiso_fk: int    
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None