# controllers/auth_controller.py
from datetime import datetime, timedelta
from jose import jwt
import bcrypt
from fastapi import HTTPException

from config.db_config import get_db_connection
    
# Configuración del JWT
SECRET_KEY = "clave_super_secreta_cambiar" #Usar variable de entorno luego
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def autenticar_usuario(usuario: str, contrasena: str):
    conn = get_db_connection()
    query = "SELECT id, contrasena FROM usuarios WHERE usuario = %s"
    result = conn.execute(query, (usuario,)).fetchone()
    if not result:
        return None
    
    if result[1] != contrasena:
        return None

    return result[0]

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
        # Buscar usuario por nombre
        cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (datos.usuario,))
        usuario = cursor.fetchone()

        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        # Verificar si está activo
        if not usuario["estado"]:
            raise HTTPException(status_code=403, detail="Usuario inactivo")

        # Verificar contraseña
        if not bcrypt.checkpw(datos.contrasena.encode('utf-8'), usuario["contrasena"].encode('utf-8')):
            raise HTTPException(status_code=401, detail="Contraseña incorrecta")

        # Crear token con los datos del usuario
        token_data = {
            "sub": str(usuario["id_usuario"]),
            }

        access_token = crear_token(token_data)

        # Retornar token y datos básicos
        return {
            "access_token": access_token,
        }
        #"token_type": "bearer",
    finally:
        conn.close()
