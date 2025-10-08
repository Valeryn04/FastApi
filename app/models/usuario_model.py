from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime

class UsuarioBase(BaseModel):
    id_usuario: Optional[int] = None
    usuario: str
    contrasena: str
    nombre: str
    apellido: str
    tipo_documento: str
    numero_documento: str
    fecha_nacimiento: date
    sexo: str
    telefono: Optional[str] = None
    email: Optional[str] = None
    direccion: Optional[str] = None
    estado: Optional[bool] = True
    id_rol: int
    create_date: Optional[datetime] = None
    update_date: Optional[datetime] = None
    
class UsuarioUpdate(BaseModel):
    usuario: Optional[str] = None
    contrasena: Optional[str] = None
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    tipo_documento: Optional[str] = None
    numero_documento: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    sexo: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    direccion: Optional[str] = None
    id_rol: Optional[int] = None
