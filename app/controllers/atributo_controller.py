import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from fastapi.encoders import jsonable_encoder

class AtributoController:
    
    
    def get_all(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM atributo")
            data = cursor.fetchall()
          
            if not data:
                raise HTTPException(status_code=404, detail="No se encontraron atributos")
        
            return {"resultado": data} 

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
            cursor = conn.cursor(dictionary=True)
            data = jsonable_encoder(atributo)
            data.pop('id_atributo', None)

            cursor.execute("SELECT * FROM atributo WHERE nombre = %s", (data["nombre"],))
            if cursor.fetchone():
                raise HTTPException(status_code=400, detail="El atributo ya existe")

            # Insertar nuevo atributo
            columns = ", ".join(data.keys())
            placeholders = ", ".join(["%s"] * len(data))
            query = f"INSERT INTO atributo ({columns}) VALUES ({placeholders})"
            cursor.execute(query, list(data.values()))
            conn.commit()
            new_id = cursor.lastrowid

            # Retornar el registro recién insertado
            cursor.execute("SELECT * FROM atributo WHERE id_atributo = %s", (new_id,))
            return cursor.fetchone()

        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()


    def update(self, atributo_id: int, atributo):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            data = jsonable_encoder(atributo) 
            
            update_data = {
                k: v for k, v in data.items() 
                if v is not None and k != 'id_atributo'
            }

            if not update_data:
                raise HTTPException(status_code=400, detail="No se enviaron datos válidos para actualizar")

            update_fields = ", ".join([f"{key} = %s" for key in update_data.keys()])
            
            query = f"UPDATE atributo SET {update_fields} WHERE id_atributo = %s"
            
            values = list(update_data.values()) + [atributo_id]
            
            cursor.execute(query, values)
            conn.commit()

            if cursor.rowcount == 0:
                cursor.execute("SELECT COUNT(*) FROM atributo WHERE id_atributo = %s", (atributo_id,))
                if cursor.fetchone()['COUNT(*)'] == 0:
                    raise HTTPException(status_code=404, detail="Atributo no encontrado")
                
                return {"resultado": "Atributo actualizado correctamente"}
                            
            cursor.execute("SELECT * FROM atributo WHERE id_atributo = %s", (atributo_id,))
            return cursor.fetchone()
            
        except mysql.connector.Error as err:
            if conn and conn.is_connected():
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

    def delete(self, atributo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("DELETE FROM atributo WHERE id_atributo = %s", (atributo_id,))
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
                
                
    def get_atributos_por_rol(self, rol_id: int):
        try:
            # Obtener los atributos correspondientes al rol desde el diccionario
            atributos = self.atributos_por_rol.get(rol_id)
            if not atributos:
                raise HTTPException(status_code=404, detail="No se encontraron atributos para este rol")
            
            return {"resultado": atributos}

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))