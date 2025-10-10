import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from fastapi.encoders import jsonable_encoder

class ModuloController:
    def get_all(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM modulos")
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def get_by_id(self, modulo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * modulos WHERE id_modulo = %s", (modulo_id,))
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Módulo no encontrado")
            return result
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def create(self, modulo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            modulo_data = jsonable_encoder(modulo)
            modulo_data.pop('id_modulo', None)
            
            columns = ", ".join(modulo_data.keys())
            placeholders = ", ".join(["%s"] * len(modulo_data))
            query = f"INSERT INTO modulos ({columns}) VALUES ({placeholders})"
            
            cursor.execute(query, list(modulo_data.values()))
            conn.commit()
            return {"id_modulo": cursor.lastrowid, **modulo_data}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def update(self, modulo_id: int, modulo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            modulo_data = jsonable_encoder(modulo)
            
            update_fields = ", ".join([f"{key} = %s" for key in modulo_data.keys()])
            query = f"UPDATE modulos SET {update_fields} WHERE id_modulo = %s"
            
            values = list(modulo_data.values()) + [modulo_id]
            cursor.execute(query, values)
            conn.commit()
            
            if cursor.rowcount == 0:
                 raise HTTPException(status_code=404, detail="Módulo no encontrado o datos sin cambios")
            
            return {"message": "Módulo actualizado correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def eliminar(self, modulo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "DELETE FROM modulos WHERE id_modulo = %s"
            cursor.execute(query, (modulo_id,))
            conn.commit()

            if cursor.rowcount == 0:
                 raise HTTPException(status_code=404, detail="Módulo no encontrado")

            return {"message": "Módulo eliminado correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()