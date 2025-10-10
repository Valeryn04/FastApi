import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from fastapi.encoders import jsonable_encoder

class RolPermisoController:
    def get_all(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM rol_permisos")
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def get_by_id(self, rol_permiso_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM rol_permisos WHERE id_rol_permiso = %s", (rol_permiso_id,))
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Permiso de Rol no encontrado")
            return result
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def create(self, rol_permiso):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            data = jsonable_encoder(rol_permiso)
            data.pop('id_rol_permiso', None)
            
            columns = ", ".join(data.keys())
            placeholders = ", ".join(["%s"] * len(data))
            query = f"INSERT INTO rol_permisos ({columns}) VALUES ({placeholders})"
            
            cursor.execute(query, list(data.values()))
            conn.commit()
            return {"id_rol_permiso": cursor.lastrowid, **data}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def update(self, rol_permiso_id: int, rol_permiso):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            data = jsonable_encoder(rol_permiso)
            
            update_fields = ", ".join([f"{key} = %s" for key in data.keys()])
            query = f"UPDATE rol_permisos SET {update_fields} WHERE id_rol_permiso = %s"
            
            values = list(data.values()) + [rol_permiso_id]
            cursor.execute(query, values)
            conn.commit()
            
            if cursor.rowcount == 0:
                 raise HTTPException(status_code=404, detail="Permiso de Rol no encontrado o datos sin cambios")
            
            return {"message": "Permiso de Rol actualizado correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def eliminar(self, rol_permiso_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "DELETE FROM rol_permisos WHERE id_rol_permiso = %s"
            cursor.execute(query, (rol_permiso_id,))
            conn.commit()

            if cursor.rowcount == 0:
                 raise HTTPException(status_code=404, detail="Permiso de Rol no encontrado")

            return {"message": "Permiso de Rol eliminado correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()