from fastapi import APIRouter
from app.schemas.user_schema import UserCreate, UserLogin
from app.services.auth_service import register, login

router = APIRouter()

@router.post("/register")
async def register_user(user: UserCreate):
    await register(user)
    return {"msg": "created"}

@router.post("/login")
async def login_user(user: UserLogin):
    return await login(user)