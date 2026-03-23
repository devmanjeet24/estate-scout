from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt
from app.core.config import settings

security = HTTPBearer()

def get_current_user(token=Depends(security)):
    try:
        payload = jwt.decode(token.credentials, settings.SECRET_KEY, algorithms=["HS256"])

        if payload.get("type") != "access":
            raise Exception()

        return payload

    except:
        raise HTTPException(status_code=401, detail="Unauthorized")