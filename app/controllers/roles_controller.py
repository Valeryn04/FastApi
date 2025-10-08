import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.roles_model import RolBase
from datetime import datetime
from fastapi.encoders import jsonable_encoder

class RolController:
    def get_all(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM roles")
            data = cursor.fetchall()
            if not data:
                raise HTTPException(status_code=404, detail="No se encontraron roles")
            roles = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
            return {"resultado": jsonable_encoder(roles)}
        finally:
            conn.close()

    def get_by_id(self, id_rol: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM roles WHERE id_rol = %s", (id_rol,))
            data = cursor.fetchone()
            if not data:
                raise HTTPException(status_code=404, detail="Rol no encontrado")
            return jsonable_encoder(dict(zip([col[0] for col in cursor.description], data)))
        finally:
            conn.close()

    def create(self, rol: RolBase):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO roles (nombre_rol, descripcion, create_date, update_date) VALUES (%s,%s,%s,%s)",
                (rol.nombre_rol, rol.descripcion, datetime.now(), datetime.now())
            )
            conn.commit()
            return {"resultado": "Rol creado correctamente"}
        finally:
            conn.close()

    def update(self, id_rol: int, rol: RolBase):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE roles SET nombre_rol=%s, descripcion=%s, update_date=%s WHERE id_rol=%s",
                (rol.nombre_rol, rol.descripcion, datetime.now(), id_rol)
            )
            conn.commit()
            return {"resultado": "Rol actualizado correctamente"}
        finally:
            conn.close()

    def eliminar(self, rol_id: int):
            try:
                conn = get_db_connection()
                cursor = conn.cursor()
                query = "DELETE FROM roles WHERE id_rol = %s"
                cursor.execute(query, (rol_id,))
                conn.commit()

                if cursor.rowcount == 0:
                    raise HTTPException(status_code=404, detail="Rol no encontrado")

                return {"message": "Rol eliminado correctamente"}
            except mysql.connector.Error as err:
                conn.rollback()
                raise HTTPException(status_code=500, detail=str(err))
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()
