# routes/auth_routes.py
from fastapi import APIRouter
from app.schemas.login import LoginRequest, LoginResponse
from app.controllers.auth.auth_controller import login_usuario

router = APIRouter()

@router.post("/login", response_model=LoginResponse)
def login(datos: LoginRequest):
    return login_usuario(datos)
