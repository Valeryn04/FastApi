import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.rol_modulo_permisos import RolModuloPermisoBase 
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
                
   # ----------------------------------------------------------------------
    # MÉTODOS DE PERMISOS POR ROL (CORREGIDOS)
    # ----------------------------------------------------------------------

    def get_modulos_por_rol_simple(self, id_rol: int):
        """
        🔹 Devuelve los módulos asignados a un rol, incluyendo su icono y URL.
        Ideal para construir el menú lateral (sidebar).
        """
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            query = """
                SELECT DISTINCT 
                    m.id_modulo,
                    m.nombre_modulo,
                    m.url,
                    m.icono
                FROM rol_modulo_permisos rmp
                JOIN modulo_permisos mp ON rmp.id_modulo_permiso_fk = mp.id
                JOIN modulos m ON mp.id_modulo_fk = m.id_modulo
                WHERE rmp.id_rol_fk = %s
                ORDER BY m.nombre_modulo;
            """
            cursor.execute(query, (id_rol,))
            data = cursor.fetchall()

            if not data:
                raise HTTPException(status_code=404, detail="El rol no tiene módulos asignados")

            return {"resultado": data}

        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Error de base de datos: {str(err)}")
        finally:
            if 'conn' in locals() and conn and conn.is_connected():
                conn.close()

    def get_modulos_por_rol(self, id_rol: int):
        """
        Devuelve los módulos y permisos asociados a un rol específico,
        agrupados por módulo.
        """
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            query = """
                SELECT
                    m.id_modulo,
                    m.nombre_modulo,
                    m.icono,
                    m.url,
                    mp.id AS id_modulo_permiso,
                    mp.nombre_funcionalidad,
                    p.nombre_permiso
                FROM rol_modulo_permisos rmp
                INNER JOIN modulo_permisos mp ON rmp.id_modulo_permiso_fk = mp.id
                INNER JOIN permisos p ON mp.id_permiso_fk = p.id_permiso
                INNER JOIN modulos m ON mp.id_modulo_fk = m.id_modulo
                WHERE rmp.id_rol_fk = %s
                ORDER BY m.nombre_modulo, mp.nombre_funcionalidad;
            """
            cursor.execute(query, (id_rol,))
            data = cursor.fetchall()

            if not data:
                return {"resultado": [], "mensaje": "El rol no tiene módulos asignados o no existen relaciones activas."}

            modulos = {}
            for row in data:
                id_modulo = row["id_modulo"]
                if id_modulo not in modulos:
                    modulos[id_modulo] = {
                        "id_modulo": id_modulo,
                        "nombre_modulo": row["nombre_modulo"],
                        "icono": row["icono"],
                        "url": row["url"],
                        "funcionalidades": []
                    }
                modulos[id_modulo]["funcionalidades"].append({
                    "id_modulo_permiso": row["id_modulo_permiso"],
                    "nombre_funcionalidad": row["nombre_funcionalidad"],
                    "permiso": row["nombre_permiso"]
                })

            return {"resultado": list(modulos.values())}

        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Error de base de datos: {str(err)}")
        finally:
            if 'conn' in locals() and conn and conn.is_connected():
                conn.close()
                
    def get_permisos_por_rol(id_rol: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            # Consulta para obtener los permisos del rol
            query = """
                SELECT 
                    m.nombre_modulo, 
                    p.nombre_permiso
                FROM rol_modulo_permisos rmp
                INNER JOIN modulo_permisos mp ON rmp.id_modulo_permiso_fk = mp.id
                INNER JOIN permisos p ON mp.id_permiso_fk = p.id_permiso
                INNER JOIN modulos m ON mp.id_modulo_fk = m.id_modulo
                WHERE rmp.id_rol_fk = %s
            """
            cursor.execute(query, (id_rol,))
            data = cursor.fetchall()

            # Verificamos si no hay permisos asignados
            if not data:
                return {"resultado": [], "mensaje": "Este rol no tiene permisos asignados."}

            # Estructuramos los permisos por módulo
            permisos = {}
            for row in data:
                modulo = row["nombre_modulo"]
                if modulo not in permisos:
                    permisos[modulo] = []
                permisos[modulo].append(row["nombre_permiso"])

            return {"resultado": permisos}

        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Error en la base de datos: {str(err)}")
        finally:
            if 'conn' in locals() and conn and conn.is_connected():
                conn.close()

    def get_todos_modulos_con_permisos(self):
        """
        Devuelve TODOS los módulos disponibles con TODOS sus permisos.
        """
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            query = """
                SELECT
                    m.id_modulo,
                    m.nombre_modulo,
                    p.id_permiso,
                    p.nombre_permiso
                FROM modulos m
                CROSS JOIN permisos p
                ORDER BY m.nombre_modulo, p.nombre_permiso
            """
            cursor.execute(query)
            data = cursor.fetchall()

            if not data:
                return {"resultado": []}

            # Agrupar por módulo
            modulos = {}
            for row in data:
                id_modulo = row["id_modulo"]
                if id_modulo not in modulos:
                    modulos[id_modulo] = {
                        "id_modulo": id_modulo,
                        "nombre_modulo": row["nombre_modulo"],
                        "permisos": []
                    }
                modulos[id_modulo]["permisos"].append({
                    "id_permiso": row["id_permiso"],
                    "nombre_permiso": row["nombre_permiso"]
                })

            return {"resultado": list(modulos.values())}

        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Error de base de datos: {str(err)}")
        finally:
            if 'conn' in locals() and conn and conn.is_connected():
                conn.close()
                
                
    def get_todos_modulos_con_permisos(self, id_rol: int):
        """
        Devuelve TODOS los módulos disponibles con TODOS sus permisos.
        Marca si el rol tiene asignado ese módulo/permiso.
        """
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            # Consulta todos los módulos y permisos disponibles
            query = """
                SELECT
                    m.id_modulo,
                    m.nombre_modulo,
                    p.id_permiso,
                    p.nombre_permiso
                FROM modulos m
                CROSS JOIN permisos p
                ORDER BY m.nombre_modulo, p.nombre_permiso
            """
            cursor.execute(query)
            data = cursor.fetchall()

            # Verificar si el rol tiene asignados estos permisos
            query_rol_permisos = """
                SELECT
                    m.id_modulo,
                    p.id_permiso
                FROM rol_modulo_permisos rmp
                INNER JOIN modulo_permisos mp ON rmp.id_modulo_permiso_fk = mp.id
                INNER JOIN permisos p ON mp.id_permiso_fk = p.id_permiso
                INNER JOIN modulos m ON mp.id_modulo_fk = m.id_modulo
                WHERE rmp.id_rol_fk = %s
            """
            cursor.execute(query_rol_permisos, (id_rol,))
            permisos_asignados = cursor.fetchall()

            # Crear un set de tuplas para comprobar los permisos asignados al rol
            permisos_asignados_set = set((permiso['id_modulo'], permiso['id_permiso']) for permiso in permisos_asignados)

            if not data:
                return {"resultado": []}

            # Agrupar por módulo y agregar el estado de asignación para cada permiso
            modulos = {}
            for row in data:
                id_modulo = row["id_modulo"]
                id_permiso = row["id_permiso"]

                if id_modulo not in modulos:
                    modulos[id_modulo] = {
                        "id_modulo": id_modulo,
                        "nombre_modulo": row["nombre_modulo"],
                        "icono": "bi bi-shield-lock",  # Puedes agregar iconos personalizados
                        "url": f"/admin/{row['nombre_modulo'].lower()}",  # Generación de URL de ejemplo
                        "permisos": []
                    }

                # Verificar si el rol tiene este permiso
                tiene_permiso = (id_modulo, id_permiso) in permisos_asignados_set

                modulos[id_modulo]["permisos"].append({
                    "id_permiso": id_permiso,
                    "nombre_permiso": row["nombre_permiso"],
                    "tiene_permiso": tiene_permiso  # Marca si tiene el permiso
                })

            return {"resultado": list(modulos.values())}

        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Error de base de datos: {str(err)}")
        finally:
            if 'conn' in locals() and conn and conn.is_connected():
                conn.close()
