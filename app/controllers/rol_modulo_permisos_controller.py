import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.rol_modulo_permisos import RolModuloPermisoBase 
from datetime import datetime
from fastapi.encoders import jsonable_encoder


class RolModuloPermisoController:
    

    def get_all(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            query = """
                SELECT 
                    rmp.id, 
                    r.nombre_rol, 
                    mp.nombre_funcionalidad, 
                    rmp.created_at, 
                    rmp.updated_at
                FROM rol_modulo_permisos AS rmp
                JOIN roles AS r ON rmp.id_rol_fk = r.id_rol
                JOIN modulo_permisos AS mp ON rmp.id_modulo_permiso_fk = mp.id
            """
            cursor.execute(query)
            data = cursor.fetchall()

            if not data:
                raise HTTPException(status_code=404, detail="No se encontraron asignaciones de permisos a roles")

            # Mapea los resultados a una lista de diccionarios
            relaciones = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
            return {"resultado": jsonable_encoder(relaciones)}
        
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Error de base de datos: {str(err)}")
        finally:
            if conn.is_connected():
                conn.close()

    def get_by_id(self, id_relacion: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            query = "SELECT * FROM rol_modulo_permisos WHERE id = %s"
            cursor.execute(query, (id_relacion,))
            data = cursor.fetchone()

            if not data:
                raise HTTPException(status_code=404, detail="Asignación de permiso no encontrada")

            return jsonable_encoder(dict(zip([col[0] for col in cursor.description], data)))
        
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Error de base de datos: {str(err)}")
        finally:
            if conn.is_connected():
                conn.close()


    def create(self, relacion: RolModuloPermisoBase):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            # Validación: Evitar duplicados
            cursor.execute(
                "SELECT COUNT(*) FROM rol_modulo_permisos WHERE id_rol_fk = %s AND id_modulo_permiso_fk = %s",
                (relacion.id_rol_fk, relacion.id_modulo_permiso_fk)
            )
            if cursor.fetchone()[0] > 0:
                raise HTTPException(status_code=400, detail="Esta funcionalidad ya está asignada a este rol")

            # Inserción
            query = """
                INSERT INTO rol_modulo_permisos (id_rol_fk, id_modulo_permiso_fk, created_at, updated_at) 
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(
                query,
                (relacion.id_rol_fk, relacion.id_modulo_permiso_fk, datetime.now(), datetime.now())
            )
            conn.commit()
            
            return {"resultado": "Asignación de permiso creada correctamente"}

        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error al crear la asignación (Verifique FKs): {str(err)}")
        finally:
            if conn.is_connected():
                conn.close()
                

    def update(self, id_relacion: int, relacion: RolModuloPermisoBase):
        """Actualiza el rol o la funcionalidad asignada a una relación existente."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Validar que la asignación exista
            cursor.execute("SELECT * FROM rol_modulo_permisos WHERE id = %s", (id_relacion,))
            existente = cursor.fetchone()
            if not existente:
                raise HTTPException(status_code=404, detail="Asignación de permiso no encontrada")

            # Validación: Evitar duplicados después de la actualización
            cursor.execute(
                "SELECT COUNT(*) FROM rol_modulo_permisos WHERE id_rol_fk = %s AND id_modulo_permiso_fk = %s AND id <> %s",
                (relacion.id_rol_fk, relacion.id_modulo_permiso_fk, id_relacion)
            )
            if cursor.fetchone()[0] > 0:
                raise HTTPException(status_code=400, detail="Esta combinación de Rol y Funcionalidad ya existe en otra asignación.")

            query = """
                UPDATE rol_modulo_permisos SET 
                    id_rol_fk = %s, 
                    id_modulo_permiso_fk = %s, 
                    updated_at = %s 
                WHERE id = %s
            """
            cursor.execute(
                query, 
                (relacion.id_rol_fk, relacion.id_modulo_permiso_fk, datetime.now(), id_relacion)
            )
            conn.commit()

            return {"resultado": "Asignación de permiso actualizada correctamente"}

        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error al actualizar la asignación: {str(err)}")
        finally:
            if conn.is_connected():
                conn.close()


    def eliminar(self, id_relacion: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            query = "DELETE FROM rol_modulo_permisos WHERE id = %s"
            cursor.execute(query, (id_relacion,))
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Asignación de permiso no encontrada")

            return {"message": "Asignación de permiso eliminada correctamente"}

        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                conn.close()