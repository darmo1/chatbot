from fastapi import FastAPI
from app.auth.routes import auth_router
from app.chat.routes import chat_router
from app.common.database import create_all_tables

app = FastAPI()
create_all_tables()

#routes
app.include_router(auth_router)
app.include_router(chat_router)
@app.get("/")
def read_root():
    return {"Hello": "hi"}


