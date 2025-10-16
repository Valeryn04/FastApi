import mysql.connector
import re
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.usuario_model import UsuarioCreateWithAtributos, UsuarioUpdate
from datetime import datetime
from fastapi.encoders import jsonable_encoder
import bcrypt


class UsuarioController:

    def get_all(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios")
            data = cursor.fetchall()

            if not data:
                raise HTTPException(status_code=404, detail="No se encontraron usuarios")

            usuarios = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
            return {"resultado": jsonable_encoder(usuarios)}
        finally:
            conn.close()

    def get_by_id(self, id_usuario: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (id_usuario,))
            data = cursor.fetchone()

            if not data:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")

            return jsonable_encoder(dict(zip([col[0] for col in cursor.description], data)))
        finally:
            conn.close()

    def create(self, usuario: UsuarioCreateWithAtributos):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # VALIDACIONES BÁSICAS
            if not usuario.usuario or usuario.usuario.strip() == "":
                raise HTTPException(status_code=400, detail="El nombre de usuario es obligatorio")

            if not usuario.contrasena or len(usuario.contrasena.strip()) < 8:
                raise HTTPException(status_code=400, detail="La contraseña debe tener al menos 8 caracteres")
            if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", usuario.contrasena):
                raise HTTPException(status_code=400, detail="La contraseña debe incluir al menos un símbolo especial")

            if not usuario.email or usuario.email.strip() == "":
                raise HTTPException(status_code=400, detail="El correo electrónico es obligatorio")

            # VALIDAR DUPLICADOS
            cursor.execute("SELECT COUNT(*) FROM usuarios WHERE usuario = %s", (usuario.usuario,))
            if cursor.fetchone()[0] > 0:
                raise HTTPException(status_code=400, detail="El nombre de usuario ya está en uso")

            cursor.execute("SELECT COUNT(*) FROM usuarios WHERE email = %s", (usuario.email,))
            if cursor.fetchone()[0] > 0:
                raise HTTPException(status_code=400, detail="El correo electrónico ya está registrado")

            cursor.execute("SELECT COUNT(*) FROM usuarios WHERE numero_documento = %s", (usuario.numero_documento,))
            if cursor.fetchone()[0] > 0:
                raise HTTPException(status_code=400, detail="El número de documento ya está registrado")

            # VALIDAR QUE EL ROL EXISTA
            cursor.execute("SELECT COUNT(*) FROM roles WHERE id_rol = %s", (usuario.id_rol,))
            if cursor.fetchone()[0] == 0:
                raise HTTPException(status_code=400, detail="El rol asignado no existe")

            # Contraseña hasheada después de validar
            hashed_password = bcrypt.hashpw(usuario.contrasena.encode('utf-8'), bcrypt.gensalt())
            hashed_password = hashed_password.decode('utf-8')

            query = """
                INSERT INTO usuarios 
                (usuario, contrasena, nombre, apellido, tipo_documento, numero_documento, 
                fecha_nacimiento, sexo, telefono, email, direccion, id_rol, estado, create_date, update_date)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            values = (
                usuario.usuario, hashed_password, usuario.nombre, usuario.apellido,
                usuario.tipo_documento, usuario.numero_documento, usuario.fecha_nacimiento,
                usuario.sexo, usuario.telefono, usuario.email, usuario.direccion,
                usuario.id_rol, True, datetime.now(), datetime.now()
            )

            cursor.execute(query, values)
            conn.commit()

            # Obtener el id del usuario recién creado
            id_usuario = cursor.lastrowid

            # Insertar atributos asociados al usuario
            if usuario.atributos:
                for attr in usuario.atributos:
                    sql_attr = """
                        INSERT INTO usuarioatributo (id_usuario, id_atributo, valor, create_date)
                        VALUES (%s, %s, %s, NOW())
                    """
                    cursor.execute(sql_attr, (id_usuario, attr.id_atributo, attr.valor))

            conn.commit()
            return {"message": "Usuario y atributos creados correctamente", "id_usuario": id_usuario}

        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()

    def update(self, id_usuario: int, usuario: UsuarioUpdate):
        """
        Actualiza los datos del usuario y sus atributos personalizados (si se envían).
        Elimina los atributos que ya no están en la lista recibida.
        """
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            # Verificar si el usuario existe
            cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (id_usuario,))
            existente = cursor.fetchone()
            if not existente:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")

            # Separar campos básicos de los atributos personalizados
            data = usuario.dict(exclude_unset=True)
            atributos = data.pop("atributos", None)

            if not data and not atributos:
                return {"resultado": "No se enviaron datos para actualizar"}

            # --- ACTUALIZAR DATOS DEL USUARIO ---
            if data:
                campos = []
                valores = []

                # Validar contraseña (si viene)
                if "contrasena" in data:
                    if len(data["contrasena"].strip()) < 8:
                        raise HTTPException(status_code=400, detail="La contraseña debe tener al menos 8 caracteres")
                    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", data["contrasena"]):
                        raise HTTPException(status_code=400, detail="La contraseña debe incluir al menos un símbolo especial")

                    hashed_password = bcrypt.hashpw(data["contrasena"].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                    data["contrasena"] = hashed_password

                # Validar email único
                if "email" in data:
                    cursor.execute(
                        "SELECT COUNT(*) as total FROM usuarios WHERE email = %s AND id_usuario <> %s",
                        (data["email"], id_usuario)
                    )
                    if cursor.fetchone()["total"] > 0:
                        raise HTTPException(status_code=400, detail="El correo electrónico ya está en uso")

                # Validar rol existente
                if "id_rol" in data:
                    cursor.execute("SELECT COUNT(*) as total FROM roles WHERE id_rol = %s", (data["id_rol"],))
                    if cursor.fetchone()["total"] == 0:
                        raise HTTPException(status_code=400, detail="El rol asignado no existe")

                # Construir SQL dinámico
                for campo, valor in data.items():
                    campos.append(f"{campo}=%s")
                    valores.append(valor)

                campos.append("update_date=%s")
                valores.append(datetime.now())
                valores.append(id_usuario)

                sql = f"UPDATE usuarios SET {', '.join(campos)} WHERE id_usuario=%s"
                cursor.execute(sql, tuple(valores))

            # --- ACTUALIZAR ATRIBUTOS PERSONALIZADOS ---
            if atributos is not None:
                # Obtener los IDs actuales de los atributos del usuario
                cursor.execute("""
                    SELECT id_atributo FROM usuarioatributo WHERE id_usuario = %s
                """, (id_usuario,))
                actuales = {row["id_atributo"] for row in cursor.fetchall()}

                # Convertir los atributos recibidos a un set de IDs para facilitar la comparación
                nuevos = {attr["id_atributo"] for attr in atributos if isinstance(attr, dict) and "id_atributo" in attr}
                
                # 1️⃣ Eliminar los que ya no están en la nueva lista
                eliminar = actuales - nuevos
                if eliminar:
                    formato_in = ', '.join(['%s'] * len(eliminar))
                    cursor.execute(f"""
                        DELETE FROM usuarioatributo
                        WHERE id_usuario = %s AND id_atributo IN ({formato_in})
                    """, (id_usuario, *eliminar))

                # 2️⃣ Insertar o actualizar los atributos enviados
                for attr in atributos:
                    id_atributo = attr.get("id_atributo")
                    valor = attr.get("valor")
                    
                    if not id_atributo: continue # Saltar si falta el ID de atributo

                    cursor.execute("""
                        SELECT id_usuario_atributo 
                        FROM usuarioatributo 
                        WHERE id_usuario = %s AND id_atributo = %s
                    """, (id_usuario, id_atributo))
                    existente_attr = cursor.fetchone()

                    if existente_attr:
                        cursor.execute("""
                            UPDATE usuarioatributo
                            SET valor = %s, update_date = NOW()
                            WHERE id_usuario = %s AND id_atributo = %s
                        """, (valor, id_usuario, id_atributo))
                    else:
                        cursor.execute("""
                            INSERT INTO usuarioatributo (id_usuario, id_atributo, valor, create_date)
                            VALUES (%s, %s, %s, NOW())
                        """, (id_usuario, id_atributo, valor))

            conn.commit()
            return {"resultado": "Usuario y atributos actualizados correctamente"}

        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))

        finally:
            conn.close()


    def cambiar_estado(self, id_usuario: int, estado: bool):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Verificar que el usuario exista
            cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (id_usuario,))
            user = cursor.fetchone()
            if not user:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")

            # Actualizar el estado
            cursor.execute(
                "UPDATE usuarios SET estado = %s, update_date = %s WHERE id_usuario = %s",
                (estado, datetime.now(), id_usuario)
            )
            conn.commit()

            mensaje = "Usuario activado" if estado else "Usuario desactivado"
            return {"resultado": mensaje}

        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()