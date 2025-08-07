from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import timedelta, datetime, timezone

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(psw: str) -> str:
  return pwd_context.hash(psw)

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({""
    "exp": expire
    })
    return jwt.encode(to_encode, "secret", algorithm="HS256")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

