from fastapi import APIRouter, HTTPException, Response
from app.user.models import LoginRequest
from app.user.services import login_user, register_user
from app.common.database import SesssionDeep
from app.user.schemas import UserCreate

auth_router = APIRouter(prefix="/users");

@auth_router.post("/login")
async def login(form_data: LoginRequest, db: SesssionDeep):
    return login_user(form_data, db=db)

@auth_router.post("/register")
def register(user_data: UserCreate, db: SesssionDeep):
    if not user_data.email or not user_data.password:
        raise HTTPException(
            status_code=400, 
            detail="Email and password are required"
        )
    register_user(user_data, db=db) 
    return {"message": "User registered successfully"}