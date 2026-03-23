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
    try:
        # ✅ Check if user already exists
        existing_user = await db.users.find_one({"email": user.email})
        if existing_user:
            raise Exception("User already exists")

        # ✅ Ensure password is string (IMPORTANT FIX)
        password_str = str(user.password)

        # ✅ Hash password safely
        hashed_password = hash_password(password_str)

        # ✅ Save user
        await db.users.insert_one({
            "email": user.email,
            "hashed_password": hashed_password,
            "preferences": {}
        })

        logger.info(f"User registered: {user.email}")

        return {"msg": "User created successfully"}

    except Exception as e:
        logger.error(f"Register error: {str(e)}")
        raise Exception(str(e))


# 🔐 LOGIN USER
async def login(user):
    try:
        # ✅ Find user
        db_user = await db.users.find_one({"email": user.email})

        if not db_user:
            raise Exception("User not found")

        # ✅ Ensure password is string
        password_str = str(user.password)

        # ✅ Verify password
        if not verify_password(password_str, db_user["hashed_password"]):
            raise Exception("Invalid credentials")

        # ✅ Generate tokens
        access_token = create_access_token({"email": user.email})
        refresh_token = create_refresh_token({"email": user.email})

        logger.info(f"User login: {user.email}")

        return {
            "access": access_token,
            "refresh": refresh_token
        }

    except Exception as e:
        logger.error(f"Login error: {str(e)}")
        raise Exception(str(e))