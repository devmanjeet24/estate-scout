from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import HTTPException
from app.core.config import settings

# ✅ Optimized bcrypt (faster but still secure)
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
    bcrypt__rounds=10   # 🔥 performance boost (default 12 → slow)
)

# 🔐 HASH PASSWORD
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


# 🔐 VERIFY PASSWORD
def verify_password(plain: str, hashed: str) -> bool:
    try:
        return pwd_context.verify(plain, hashed)
    except Exception:
        return False


# 🔑 CREATE ACCESS TOKEN
def create_access_token(data: dict) -> str:
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire,
        "type": "access"
    })

    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")


# 🔑 CREATE REFRESH TOKEN
def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    to_encode.update({
        "exp": expire,
        "type": "refresh"
    })

    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")


# 🔓 DECODE TOKEN (NEW - IMPORTANT)
def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        return payload

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")