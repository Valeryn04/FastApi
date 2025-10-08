from fastapi import HTTPException
from config.db_config import get_db_connection
from models.usuario_model import UsuarioBase
from datetime import datetime
from fastapi.encoders import jsonable_encoder

class UsuarioController:
    
    def get_all(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios")
            data = cursor.fetchall()
            if not data:
                raise HTTPException(status_code=404, detail="No se encontraron usuarios")
            usuarios = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
            return {"resultado": jsonable_encoder(usuarios)}
        finally:
            conn.close()

    def get_by_id(self, id_usuario: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (id_usuario,))
            data = cursor.fetchone()
            if not data:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")
            return jsonable_encoder(dict(zip([col[0] for col in cursor.description], data)))
        finally:
            conn.close()

    def create(self, usuario: UsuarioBase):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = """INSERT INTO usuarios 
                       (usuario, contrasena, nombre, apellido, tipo_documento, numero_documento, 
                        fecha_nacimiento, sexo, telefono, email, direccion, id_rol, estado, create_date, update_date)
                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            values = (
                usuario.usuario, usuario.contrasena, usuario.nombre, usuario.apellido,
                usuario.tipo_documento, usuario.numero_documento, usuario.fecha_nacimiento,
                usuario.sexo, usuario.telefono, usuario.email, usuario.direccion,
                usuario.id_rol, True, datetime.now(), datetime.now()
            )
            cursor.execute(query, values)
            conn.commit()
            return {"resultado": "Usuario creado correctamente"}
        finally:
            conn.close()

    def update(self, id_usuario: int, usuario: UsuarioBase):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = """UPDATE usuarios SET nombre=%s, apellido=$%s, telefono=%s, email=%s, direccion=%s, 
                       id_rol=%s, update_date=%s WHERE id_usuario=%s"""
            cursor.execute(query, (usuario.nombre, usuario.apellido, usuario.telefono, usuario.email,
                                   usuario.direccion, usuario.id_rol, datetime.now(), id_usuario))
            conn.commit()
            return {"resultado": "Usuario actualizado correctamente"}
        finally:
            conn.close()

    def deactivate(self, id_usuario: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE usuarios SET estado = FALSE, update_date = %s WHERE id_usuario = %s",
                           (datetime.now(), id_usuario))
            conn.commit()
            return {"resultado": "Usuario desactivado"}
        finally:
            conn.close()
