from fastapi import APIRouter, Depends
from app.db.database import db
from app.core.dependencies import get_current_user

router = APIRouter()

@router.get("/preferences")
async def get_preferences(user=Depends(get_current_user)):
    db_user = await db.users.find_one({"email": user["email"]})
    return db_user.get("preferences", {})


@router.put("/preferences")
async def update_preferences(data: dict, user=Depends(get_current_user)):
    await db.users.update_one(
        {"email": user["email"]},
        {"$set": {"preferences": data}}
    )
    return {"msg": "updated"}