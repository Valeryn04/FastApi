import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection 
from app.models.modulo_permisos_model import ModuloPermisoBase 
from datetime import datetime
from fastapi.encoders import jsonable_encoder

# Recordatorio de columnas: id, id_modulo_fk, id_permiso_fk, nombre_funcionalidad, created_at, updated_at

class ModuloPermisoController:
    

    def get_all(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            query = """
                SELECT 
                    mp.id, 
                    m.nombre_modulo, 
                    p.nombre_permiso, 
                    mp.nombre_funcionalidad,
                    mp.created_at, 
                    mp.updated_at
                FROM modulo_permisos AS mp
                JOIN modulos AS m ON mp.id_modulo_fk = m.id_modulo
                JOIN permisos AS p ON mp.id_permiso_fk = p.id_permiso
            """
            cursor.execute(query)
            data = cursor.fetchall()

            if not data:
                raise HTTPException(status_code=404, detail="No se encontraron funcionalidades (Módulo-Permiso)")

            # Mapea los resultados a una lista de diccionarios
            funcionalidades = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
            return {"resultado": jsonable_encoder(funcionalidades)}
        
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Error de base de datos: {str(err)}")
        finally:
            if conn.is_connected():
                conn.close()


    def get_by_id(self, id_funcionalidad: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            query = "SELECT * FROM modulo_permisos WHERE id = %s"
            cursor.execute(query, (id_funcionalidad,))
            data = cursor.fetchone()

            if not data:
                raise HTTPException(status_code=404, detail="Funcionalidad no encontrada")

            return jsonable_encoder(dict(zip([col[0] for col in cursor.description], data)))
        
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Error de base de datos: {str(err)}")
        finally:
            if conn.is_connected():
                conn.close()

    def create(self, funcionalidad: ModuloPermisoBase):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            # Validación: nombre obligatorio
            if not funcionalidad.nombre_funcionalidad or funcionalidad.nombre_funcionalidad.strip() == "":
                raise HTTPException(status_code=400, detail="El nombre de la funcionalidad es obligatorio")

            # Validación: Evitar duplicados
            cursor.execute(
                "SELECT COUNT(*) FROM modulo_permisos WHERE id_modulo_fk = %s AND id_permiso_fk = %s",
                (funcionalidad.id_modulo_fk, funcionalidad.id_permiso_fk)
            )
            if cursor.fetchone()[0] > 0:
                raise HTTPException(status_code=400, detail="Esta combinación Módulo-Permiso ya existe como funcionalidad")


            query = """
                INSERT INTO modulo_permisos (id_modulo_fk, id_permiso_fk, nombre_funcionalidad, created_at, updated_at) 
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(
                query,
                (
                    funcionalidad.id_modulo_fk, 
                    funcionalidad.id_permiso_fk, 
                    funcionalidad.nombre_funcionalidad, 
                    datetime.now(), 
                    datetime.now()
                )
            )
            conn.commit()
            
            return {"resultado": "Funcionalidad creada correctamente"}

        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error al crear la funcionalidad (Verifique FKs): {str(err)}")
        finally:
            if conn.is_connected():
                conn.close()
                

    def update(self, id_funcionalidad: int, funcionalidad: ModuloPermisoBase):
        """Actualiza el nombre, módulo o permiso de una funcionalidad existente."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM modulo_permisos WHERE id = %s", (id_funcionalidad,))
            existente = cursor.fetchone()
            if not existente:
                raise HTTPException(status_code=404, detail="Funcionalidad no encontrada")

            campos = []
            valores = []
            
            if funcionalidad.nombre_funcionalidad is not None:
                if funcionalidad.nombre_funcionalidad.strip() == "":
                    raise HTTPException(status_code=400, detail="El nombre de la funcionalidad no puede estar vacío")
                
                campos.append("nombre_funcionalidad=%s")
                valores.append(funcionalidad.nombre_funcionalidad)

            if funcionalidad.id_modulo_fk is not None:
                campos.append("id_modulo_fk=%s")
                valores.append(funcionalidad.id_modulo_fk)

            if funcionalidad.id_permiso_fk is not None:
                campos.append("id_permiso_fk=%s")
                valores.append(funcionalidad.id_permiso_fk)
            
            # Actualizar solo si hay campos
            if campos:
                
                if funcionalidad.id_modulo_fk is not None or funcionalidad.id_permiso_fk is not None:
                    
                    # Usamos los valores propuestos o los valores existentes
                    new_module_id = funcionalidad.id_modulo_fk if funcionalidad.id_modulo_fk is not None else existente[1] # [1] es id_modulo_fk
                    new_permiso_id = funcionalidad.id_permiso_fk if funcionalidad.id_permiso_fk is not None else existente[2] # [2] es id_permiso_fk

                    cursor.execute(
                        "SELECT COUNT(*) FROM modulo_permisos WHERE id_modulo_fk = %s AND id_permiso_fk = %s AND id <> %s",
                        (new_module_id, new_permiso_id, id_funcionalidad)
                    )
                    if cursor.fetchone()[0] > 0:
                        raise HTTPException(status_code=400, detail="Esa combinación Módulo-Permiso ya está registrada en otra funcionalidad.")


                campos.append("updated_at=%s")
                valores.append(datetime.now())
                valores.append(id_funcionalidad)

                sql = f"UPDATE modulo_permisos SET {', '.join(campos)} WHERE id=%s"
                cursor.execute(sql, tuple(valores))
                conn.commit()
                return {"resultado": "Funcionalidad actualizada correctamente"}
            else:
                return {"resultado": "No se enviaron campos para actualizar"}

        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error al actualizar la funcionalidad: {str(err)}")
        finally:
            if conn.is_connected():
                conn.close()

    def eliminar(self, id_funcionalidad: int):
        """Elimina una funcionalidad por su ID."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            query = "DELETE FROM modulo_permisos WHERE id = %s"
            cursor.execute(query, (id_funcionalidad,))
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Funcionalidad no encontrada")

            return {"message": "Funcionalidad eliminada correctamente"}

        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error al eliminar (Verifique dependencias en roles): {str(err)}")
        finally:
            if conn.is_connected():
                conn.close()