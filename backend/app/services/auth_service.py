from fastapi import HTTPException
from app.db.database import db
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token
)
from app.utils.logger import logger


# 🔐 REGISTER USER
async def register(user):
    # ✅ Check if user already exists
    existing_user = await db.users.find_one({"email": user.email})

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    # ✅ Hash password
    hashed_password = hash_password(user.password)

    # ✅ Save user
    await db.users.insert_one({
        "email": user.email,
        "hashed_password": hashed_password,
        "preferences": {}
    })

    logger.info(f"User registered: {user.email}")

    return {"msg": "User created successfully"}


# 🔐 LOGIN USER
async def login(user):
    # ✅ Find user
    db_user = await db.users.find_one({"email": user.email})

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # ✅ Verify password
    if not verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # ✅ Generate tokens
    access_token = create_access_token({"email": user.email})
    refresh_token = create_refresh_token({"email": user.email})

    logger.info(f"User login: {user.email}")

    return {
        "access": access_token,
        "refresh": refresh_token
    }