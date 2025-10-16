import mysql.connector
import os

# Cargar variables de entorno
from dotenv import load_dotenv
load_dotenv()

# Usar variables de entorno para la configuración de la base de datos
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

def get_db_connection():
    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
