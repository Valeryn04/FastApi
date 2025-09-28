import mysql.connector
from fastapi import HTTPException
import bcrypt
from config.db_config import get_db_connection
from models.usuario_model import UsuarioBase
from fastapi.encoders import jsonable_encoder

class UsuarioController:

    def create_usuario(self, usuario: UsuarioBase):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute(
            "SELECT COUNT(*) FROM usuarios WHERE usuario = %s OR email = %s",
            (usuario.usuario, usuario.email)
            )
            
            if cursor.fetchone()[0] > 0:
                raise HTTPException(status_code=400, detail="El usuario o email ya existe")
            
            hashed_password = bcrypt.hashpw(usuario.contrasena.encode("utf-8"), bcrypt.gensalt())


            query = """
                INSERT INTO usuarios 
                (usuario, contrasena, nombreCompleto, tipoDocumento, numeroDocumento, 
                 fechaNacimiento, sexo, telefono, email, direccion, idRol, estado)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                usuario.usuario,
                hashed_password.decode("utf-8"),
                usuario.nombreCompleto,
                usuario.tipoDocumento,
                usuario.numeroDocumento,
                usuario.fechaNacimiento,
                usuario.sexo,
                usuario.telefono,
                usuario.email,
                usuario.direccion,
                usuario.idRol,
                usuario.estado
            )

            cursor.execute(query, values)
            conn.commit()
            usuario_id = cursor.lastrowid
            
            return {"resultado": "Usuario creado", "idUsuario": usuario_id}
        
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error al crear usuario: {str(err)}")
        finally:
            conn.close()

    def get_usuario(self, usuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE idUsuario = %s", (usuario_id,))
            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")

            content = {
                "id": result[0],
                "usuario": result[1],
                "contrasena": result[2],
                "nombreCompleto": result[3],
                "tipoDocumento": result[4],
                "numeroDocumento": result[5],
                "fechaNacimiento": result[6],
                "sexo": result[7],
                "telefono": result[8],
                "email": result[9],
                "direccion": result[10],
                "idRol": result[11],
                "estado": result[12],
            }

            return jsonable_encoder(content)

        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error al obtener usuario: {str(err)}")
        finally:
            conn.close()

    def get_usuarios(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios")
            results = cursor.fetchall()

            usuarios = []
            for data in results:
                usuarios.append({
                    "id": data[0],
                    "usuario": data[1],
                    "contrasena": data[2],
                    "nombreCompleto": data[3],
                    "tipoDocumento": data[4],
                    "numeroDocumento": data[5],
                    "fechaNacimiento": data[6],
                    "sexo": data[7],
                    "telefono": data[8],
                    "email": data[9],
                    "direccion": data[10],
                    "idRol": data[11],
                    "estado": data[12],
                })

            if not usuarios:
                raise HTTPException(status_code=404, detail="No hay usuarios registrados")

            return {"resultado": jsonable_encoder(usuarios)}

        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error al obtener usuarios: {str(err)}")
        finally:
            conn.close()
