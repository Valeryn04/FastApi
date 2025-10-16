from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
import mysql.connector
from app.config.db_config import get_db_connection
from app.routes.usuarios_routes import router as usuarios_router
from app.routes.roles_routes import router as rol_router
from app.routes.auth_routes import router as auth_router
from app.routes.atributos_routes import router as atributos_router
from app.routes.modulo_permisos_routes import router as moduloPermisos_router
from app.routes.rol_modulos_permisos_routes import router as rol_modulos_permisos_router

app = FastAPI(
    title="Clinica API - Test"
)

origins = [
    "http://localhost:8000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://fastapi-4-aqig.onrender.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_PREFIX = "/api"

app.include_router(usuarios_router, tags=["A. Usuarios"], prefix=API_PREFIX)
app.include_router(auth_router, tags=["B. Auth"], prefix=API_PREFIX)
app.include_router(rol_router, tags=["C. Roles"], prefix=API_PREFIX)
app.include_router(atributos_router, tags=["D. Atributos"], prefix=API_PREFIX)
app.include_router(moduloPermisos_router, tags=["E. Modelo-Permisos"], prefix=API_PREFIX)

# Ruta raíz
@app.get("/")
def read_root():
    return {"message": "API de la Clínica funcionando en v1."}

# Ruta para favicon.ico
@app.get("/favicon.ico")
async def favicon():
    return FileResponse(os.path.join("static", "favicon.ico"))

# Ruta de test para probar conexión a la BD
@app.get("/api/test-db")
def test_db_connection():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT NOW();")  # comando simple para comprobar que responde
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return {"message": "✅ Conexión exitosa a la base de datos", "server_time": result[0]}
    except mysql.connector.Error as err:
        return {"message": "❌ Error al conectar a la base de datos", "error": str(err)}
    except Exception as e:
        return {"message": "⚠️ Error inesperado", "error": str(e)}


# Ruta con prefijo '/api'
@app.get(API_PREFIX + "/")
def read_api_root():
    return {"message": "API de la Clínica funcionando en /api."}
