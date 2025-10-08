import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from fastapi.encoders import jsonable_encoder

class UsuarioAtributoController:
    def get_all(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarioatributo")
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def get_by_id(self, usuario_atributo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarioatributo WHERE id_usuario_atributo = %s", (usuario_atributo_id,))
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Relación Usuario-Atributo no encontrada")
            return result
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def create(self, usuario_atributo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            data = jsonable_encoder(usuario_atributo)
            data.pop('id_usuario_atributo', None)
            
            columns = ", ".join(data.keys())
            placeholders = ", ".join(["%s"] * len(data))
            query = f"INSERT INTO usuarioatributo ({columns}) VALUES ({placeholders})"
            
            cursor.execute(query, list(data.values()))
            conn.commit()
            return {"id_usuario_atributo": cursor.lastrowid, **data}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def update(self, usuario_atributo_id: int, usuario_atributo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            data = jsonable_encoder(usuario_atributo)
            
            update_fields = ", ".join([f"{key} = %s" for key in data.keys()])
            query = f"UPDATE usuarioatributo SET {update_fields} WHERE id_usuario_atributo = %s"
            
            values = list(data.values()) + [usuario_atributo_id]
            cursor.execute(query, values)
            conn.commit()
            
            if cursor.rowcount == 0:
                 raise HTTPException(status_code=404, detail="Relación Usuario-Atributo no encontrada o datos sin cambios")
            
            return {"message": "Relación Usuario-Atributo actualizada correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def eliminar(self, usuario_atributo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "DELETE FROM usuarioatributo WHERE id_usuario_atributo = %s"
            cursor.execute(query, (usuario_atributo_id,))
            conn.commit()

            if cursor.rowcount == 0:
                 raise HTTPException(status_code=404, detail="Relación Usuario-Atributo no encontrada")

            return {"message": "Relación Usuario-Atributo eliminada correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()