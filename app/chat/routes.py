## Here agent routes
from fastapi import APIRouter
from fastapi.params import Depends

from app.auth.dependencies import get_current_user


chat_router = APIRouter( prefix="/chat", tags=["agent"])

@chat_router.get("/")
async def chat(token: dict = Depends(get_current_user)):
    return { "message": "Hello, this is the agent"}