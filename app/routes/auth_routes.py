# routes/auth_routes.py
from fastapi import APIRouter
from schemas.login import LoginRequest, LoginResponse
from controllers.auth.auth_controller import login_usuario

router = APIRouter()

@router.post("/login", response_model=LoginResponse)
async def login(datos: LoginRequest):
    return login_usuario(datos)
