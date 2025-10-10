import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from fastapi.encoders import jsonable_encoder

class AtributoController:
    def get_all(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM atributo")
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def get_by_id(self, atributo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM atributo WHERE id_atributo = %s", (atributo_id,))
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Atributo no encontrado")
            return result
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def create(self, atributo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            data = jsonable_encoder(atributo)
            data.pop('id_atributo', None)
            
            columns = ", ".join(data.keys())
            placeholders = ", ".join(["%s"] * len(data))
            query = f"INSERT INTO atributo ({columns}) VALUES ({placeholders})"
            
            cursor.execute(query, list(data.values()))
            conn.commit()
            return {"id_atributo": cursor.lastrowid, **data}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def update(self, atributo_id: int, atributo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            data = jsonable_encoder(atributo)
            
            update_fields = ", ".join([f"{key} = %s" for key in data.keys()])
            query = f"UPDATE atributo SET {update_fields} WHERE id_atributo = %s"
            
            values = list(data.values()) + [atributo_id]
            cursor.execute(query, values)
            conn.commit()
            
            if cursor.rowcount == 0:
                 raise HTTPException(status_code=404, detail="Atributo no encontrado o datos sin cambios")
            
            return {"message": "Atributo actualizado correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def eliminar(self, atributo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "DELETE FROM atributo WHERE id_atributo = %s"
            cursor.execute(query, (atributo_id,))
            conn.commit()

            if cursor.rowcount == 0:
                 raise HTTPException(status_code=404, detail="Atributo no encontrado")

            return {"message": "Atributo eliminado correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()