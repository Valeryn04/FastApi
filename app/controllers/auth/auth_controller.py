from datetime import datetime, timedelta
from jose import jwt
import bcrypt
from fastapi import HTTPException

from app.config.db_config import get_db_connection

# Configuración del JWT
SECRET_KEY = "clave_super_secreta_cambiar"  # Usar variable de entorno luego
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def crear_token(data: dict):
    """Genera un JWT con expiración."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def login_usuario(datos):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        # Buscar usuario por nombre (se asume que en la tabla usuarios está id_rol)
        cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (datos.usuario,))
        usuario = cursor.fetchone()

        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        if not usuario["estado"]:
            raise HTTPException(status_code=403, detail="Usuario inactivo")

        if not bcrypt.checkpw(datos.contrasena.encode('utf-8'), usuario["contrasena"].encode('utf-8')):
            raise HTTPException(status_code=401, detail="Contraseña incorrecta")

        # Crear token con id_usuario y rol
        token_data = {
            "sub": str(usuario["id_usuario"]),
            "rol": usuario["id_rol"]
        }

        access_token = crear_token(token_data)

        return {
            "access_token": access_token,
        }
    finally:
        conn.close()
