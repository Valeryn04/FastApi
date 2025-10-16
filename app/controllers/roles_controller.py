import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.roles_model import RolBase
from datetime import datetime
from fastapi.encoders import jsonable_encoder


class RolController:
    def get_all(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM roles")
            data = cursor.fetchall()

            if not data:
                raise HTTPException(status_code=404, detail="No se encontraron roles")

            roles = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
            return {"resultado": jsonable_encoder(roles)}
        finally:
            conn.close()

    def get_by_id(self, id_rol: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM roles WHERE id_rol = %s", (id_rol,))
            data = cursor.fetchone()

            if not data:
                raise HTTPException(status_code=404, detail="Rol no encontrado")

            return jsonable_encoder(dict(zip([col[0] for col in cursor.description], data)))
        finally:
            conn.close()

    def create(self, rol: RolBase):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # 🔹 Validación: nombre obligatorio
            if not rol.nombre_rol or rol.nombre_rol.strip() == "":
                raise HTTPException(status_code=400, detail="El nombre del rol es obligatorio")

            # 🔹 Validación: nombre único
            cursor.execute("SELECT COUNT(*) FROM roles WHERE nombre_rol = %s", (rol.nombre_rol,))
            existe = cursor.fetchone()[0]
            if existe > 0:
                raise HTTPException(status_code=400, detail="Ya existe un rol con ese nombre")

            # 🔹 Inserción
            cursor.execute(
                "INSERT INTO roles (nombre_rol, descripcion, create_date, update_date) VALUES (%s,%s,%s,%s)",
                (rol.nombre_rol, rol.descripcion, datetime.now(), datetime.now())
            )
            conn.commit()
            return {"resultado": "Rol creado correctamente"}

        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            conn.close()

    def update(self, id_rol: int, rol: RolBase):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # 🔹 Validar que el rol exista
            cursor.execute("SELECT * FROM roles WHERE id_rol = %s", (id_rol,))
            existente = cursor.fetchone()
            if not existente:
                raise HTTPException(status_code=404, detail="Rol no encontrado")

            campos = []
            valores = []

            # 🔹 Validar si viene nombre_rol
            if rol.nombre_rol is not None:
                if rol.nombre_rol.strip() == "":
                    raise HTTPException(status_code=400, detail="El nombre del rol no puede estar vacío")

                # Validar que no haya otro rol con el mismo nombre
                cursor.execute(
                    "SELECT COUNT(*) FROM roles WHERE nombre_rol = %s AND id_rol <> %s",
                    (rol.nombre_rol, id_rol)
                )
                if cursor.fetchone()[0] > 0:
                    raise HTTPException(status_code=400, detail="Ya existe otro rol con ese nombre")

                campos.append("nombre_rol=%s")
                valores.append(rol.nombre_rol)

            # 🔹 Si viene descripción
            if rol.descripcion is not None:
                campos.append("descripcion=%s")
                valores.append(rol.descripcion)

            # 🔹 Actualizar solo si hay campos
            if campos:
                campos.append("update_date=%s")
                valores.append(datetime.now())
                valores.append(id_rol)

                sql = f"UPDATE roles SET {', '.join(campos)} WHERE id_rol=%s"
                cursor.execute(sql, tuple(valores))
                conn.commit()
                return {"resultado": "Rol actualizado correctamente"}
            else:
                return {"resultado": "No se enviaron campos para actualizar"}

        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            conn.close()

    def eliminar(self, rol_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "DELETE FROM roles WHERE id_rol = %s"
            cursor.execute(query, (rol_id,))
            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Rol no encontrado")

            return {"message": "Rol eliminado correctamente"}

        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
