# controllers/modulo_rol_controller.py

import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from fastapi.encoders import jsonable_encoder

class ModuloRolController:
    def get_all(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM clinica_der_modulorol")
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def get_by_id(self, modulo_rol_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM clinica_der_modulorol WHERE id_modulo_rol = %s", (modulo_rol_id,))
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Relación Módulo-Rol no encontrada")
            return result
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def create(self, modulo_rol):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            data = jsonable_encoder(modulo_rol)
            data.pop('id_modulo_rol', None)
            
            columns = ", ".join(data.keys())
            placeholders = ", ".join(["%s"] * len(data))
            query = f"INSERT INTO modulorol ({columns}) VALUES ({placeholders})"
            
            cursor.execute(query, list(data.values()))
            conn.commit()
            return {"id_modulo_rol": cursor.lastrowid, **data}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def update(self, modulo_rol_id: int, modulo_rol):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            data = jsonable_encoder(modulo_rol)
            
            update_fields = ", ".join([f"{key} = %s" for key in data.keys()])
            query = f"UPDATE modulorol SET {update_fields} WHERE id_modulo_rol = %s"
            
            values = list(data.values()) + [modulo_rol_id]
            cursor.execute(query, values)
            conn.commit()
            
            if cursor.rowcount == 0:
                 raise HTTPException(status_code=404, detail="Relación Módulo-Rol no encontrada o datos sin cambios")
            
            return {"message": "Relación Módulo-Rol actualizada correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def desactivar(self, modulo_rol_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "UPDATE modulorol SET estado = 0 WHERE id_modulo_rol = %s"
            cursor.execute(query, (modulo_rol_id,))
            conn.commit()

            if cursor.rowcount == 0:
                 raise HTTPException(status_code=404, detail="Relación Módulo-Rol no encontrada")

            return {"message": "Relación Módulo-Rol desactivada correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()