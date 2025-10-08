import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.rol_model import RolBase
from fastapi.encoders import jsonable_encoder
from datetime import datetime

class RolController:

    def create_rol(self, rol: RolBase):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO roles (nombre, descripcion, created_at, updated_at)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (rol.nombre, rol.descripcion, datetime.now(), datetime.now()))
            conn.commit()
            return {"resultado": "Rol creado correctamente", "idRol": cursor.lastrowid}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error al crear rol: {str(err)}")
        finally:
            conn.close()

    def get_roles(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM roles")
            roles = cursor.fetchall()
            data = []
            for r in roles:
                data.append({
                    "idRol": r[0],
                    "nombre": r[1],
                    "descripcion": r[2],
                    "created_at": r[3],
                    "updated_at": r[4]
                })
            return {"resultado": jsonable_encoder(data)}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Error al obtener roles: {str(err)}")
        finally:
            conn.close()
