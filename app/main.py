from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.db_config import get_db_connection

from routes.usuarios_routes import router as usuarios_router
from routes.roles_routes import router as rol_router
from routes.auth_routes import router as auth_router
from routes.atributos_routes import router as atributos_router
from routes.modulo_permisos_routes import router as moduloPermisos_router
from routes.rol_modulos_permisos_routes import router as rol_modulos_permisos_router

app = FastAPI(
    title="Clinica API - Test"
)

origins = [
    "http://localhost:8000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",

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

# Ruta de bienvenida
@app.get(API_PREFIX + "/")
def read_root():
    return {"message": "API de la Clínica funcionando en v1."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)