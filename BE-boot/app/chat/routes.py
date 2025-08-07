## Here agent routes
from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.responses import JSONResponse

from app.auth.dependencies import get_current_user
from app.chat.agent import get_agent_graph
from app.chat.model import ChatRequest


chat_router = APIRouter( prefix="/chat", tags=["agent"])

@chat_router.post("/")
async def chat(
    token: dict = Depends(get_current_user), 
    body : ChatRequest = ...):
    response_agent = get_agent_graph().invoke({"message": body.question })
    print(response_agent, '##########RESPONSE AGENT##########')
    return JSONResponse(content= response_agent)