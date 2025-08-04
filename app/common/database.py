from sqlmodel import SQLModel, create_engine, Session
from fastapi import Depends
from typing import Annotated

engine = create_engine("sqlite:///./database.db", echo=True)

def create_all_tables():
    SQLModel.metadata.create_all(engine)


async def get_session():
    with Session(engine) as session:
        yield session

SesssionDeep = Annotated[Session, Depends(get_session)]