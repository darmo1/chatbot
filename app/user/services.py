from datetime import timedelta
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from app.common.database import SesssionDeep
from app.user.models import User
from sqlmodel import select
from app.auth.utils import create_access_token, hash_password, verify_password

#email: str, full_name: str | None = None, disabled: bool | None = None
def register_user(*args, db):
    user = User(
        email=args[0].email,
        full_name=args[0].full_name,
        hashed_password=args[0].password  # This should be hashed in a real application
    ) 
   
    statement = select(User).where(User.email == user.email)
    existing_user = db.exec(statement).first()

    if existing_user :
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    hashed_password = hash_password(user.hashed_password)
    user_to_save = User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password
    )

    db.add(user_to_save)
    db.commit()
    db.refresh(user_to_save)

    return user


def login_user(form_data, db):
 user = get_user_by_email(db, form_data.email)
 if not user or not verify_password(form_data.password, user.hashed_password):
     raise HTTPException(
         status_code=400,
         detail="Incorrect email or password"
     )
 
 access_token = create_access_token(data={"sub": user.email}, expires_delta=timedelta(minutes=30))
 response = JSONResponse(
     content={"access_token": access_token, "token_type": "bearer", "success": True})

 return response


def get_user_by_email(db: SesssionDeep, email: str):
    exisiting_user = db.exec(select(User).where(User.email == email)).first()
    return exisiting_user