from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime


class UsuarioBase(BaseModel):
    usuario: str
    contrasena: str
    nombreCompleto: str
    tipoDocumento: Optional[str] = None
    numeroDocumento: Optional[str] = None
    fechaNacimiento: Optional[date] = None
    sexo: Optional[str] = None   # varchar(1), ej: 'M', 'F', 'O'
    telefono: Optional[str] = None
    email: Optional[EmailStr] = None
    direccion: Optional[str] = None
    idRol: int
    estado: Optional[int] = 1 # 1 = Activo | 0 = Inactivo