import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from fastapi.encoders import jsonable_encoder

class PermisoController:
    def get_all(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM permisos")
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def get_by_id(self, permiso_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM permisos WHERE id_permiso = %s", (permiso_id,))
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Permiso no encontrado")
            return result
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def create(self, permiso):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            permiso_data = jsonable_encoder(permiso)
            permiso_data.pop('id_permiso', None)
            
            columns = ", ".join(permiso_data.keys())
            placeholders = ", ".join(["%s"] * len(permiso_data))
            query = f"INSERT INTO permisos ({columns}) VALUES ({placeholders})"
            
            cursor.execute(query, list(permiso_data.values()))
            conn.commit()
            return {"id_permiso": cursor.lastrowid, **permiso_data}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def update(self, permiso_id: int, permiso):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            permiso_data = jsonable_encoder(permiso)
            
            update_fields = ", ".join([f"{key} = %s" for key in permiso_data.keys()])
            query = f"UPDATE permisos SET {update_fields} WHERE id_permiso = %s"
            
            values = list(permiso_data.values()) + [permiso_id]
            cursor.execute(query, values)
            conn.commit()
            
            if cursor.rowcount == 0:
                 raise HTTPException(status_code=404, detail="Permiso no encontrado o datos sin cambios")
            
            return {"message": "Permiso actualizado correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def eliminar(self, permiso_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "DELETE FROM permisos WHERE id_permiso = %s"
            cursor.execute(query, (permiso_id,))
            conn.commit()

            if cursor.rowcount == 0:
                 raise HTTPException(status_code=404, detail="Permiso no encontrado")

            return {"message": "Permiso eliminado correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()