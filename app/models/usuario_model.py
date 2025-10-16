from pydantic import BaseModel
from typing import Optional, List
from datetime import date, datetime
from app.models.usuarioatributo_model import UsuarioAtributoCreate

# --- NUEVO MODELO PARA ACTUALIZAR ATRIBUTOS ---
class AtributoUpdate(BaseModel):
    id_atributo: int
    valor: str


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
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    email: Optional[str] = None
    contrasena: Optional[str] = None
    tipo_documento: Optional[str] = None
    numero_documento: Optional[str] = None
    fecha_nacimiento: Optional[str] = None
    sexo: Optional[str] = None
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    id_rol: Optional[int] = None
    estado: Optional[bool] = None
    atributos: Optional[List[AtributoUpdate]] = None  # ✅ corregido tipo


class UsuarioCreateWithAtributos(BaseModel):
    usuario: str
    contrasena: str
    nombre: str
    apellido: str
    tipo_documento: str
    numero_documento: str
    fecha_nacimiento: date
    sexo: str
    telefono: str
    email: str
    direccion: str
    id_rol: int
    atributos: List[UsuarioAtributoCreate]
