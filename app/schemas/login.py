from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    usuario: str
    contrasena: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
