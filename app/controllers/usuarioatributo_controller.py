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
            raise HTTPException(status_code=500, detail=f"Error MySQL: {err}")
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
            raise HTTPException(status_code=500, detail=f"Error MySQL: {err}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    # ✅ NUEVO MÉTODO - Obtener atributos por ID de usuario
    def get_by_usuario(self, id_usuario: int):
        """Obtiene todos los atributos de un usuario específico con información del atributo"""
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            
            # Query con JOIN para obtener información completa del atributo
            query = """
                SELECT 
                    ua.id_usuario_atributo,
                    ua.id_usuario,
                    ua.id_atributo,
                    ua.valor,
                    a.nombre as nombre_atributo,
                    a.descripcion as descripcion_atributo
                FROM usuarioatributo ua
                INNER JOIN atributo a ON ua.id_atributo = a.id_atributo
                WHERE ua.id_usuario = %s
                ORDER BY a.nombre
            """
            
            cursor.execute(query, (id_usuario,))
            result = cursor.fetchall()
            
            # Retornar array vacío si no hay atributos (no es error)
            return result if result else []
            
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Error MySQL: {err}")
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
            raise HTTPException(status_code=500, detail=f"Error MySQL: {err}")
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
            raise HTTPException(status_code=500, detail=f"Error MySQL: {err}")
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
            raise HTTPException(status_code=500, detail=f"Error MySQL: {err}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()