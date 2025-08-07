from fastapi import FastAPI
from app.auth.routes import auth_router
from app.chat.routes import chat_router
from app.common.database import create_all_tables
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
create_all_tables()

origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#routes
app.include_router(auth_router)
app.include_router(chat_router)
@app.get("/")
def read_root():
    return {"Hello": "hi"}


