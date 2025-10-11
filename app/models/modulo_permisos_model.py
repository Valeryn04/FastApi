from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ModuloPermisoBase(BaseModel):
    id: Optional[int] = None
    id_modulo_fk: int
    id_permiso_fk: int
    nombre_funcionalidad: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
class ModuloPermisoUpdate(BaseModel):
    id: Optional[int] = None
    id_modulo_fk: Optional[int] = None
    id_permiso_fk: Optional[int] = None
    nombre_funcionalidad: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None