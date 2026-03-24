from bson import ObjectId
from app.db.database import db
from app.models.property_model import property_model

# ✅ ADD THIS FUNCTION
async def get_all_properties(user_email):
    properties = []

    async for p in db.properties.find({"created_by": user_email}):
        properties.append(property_model(p))

    return properties


async def get_property_by_id(property_id):
    p = await db.properties.find_one({"_id": ObjectId(property_id)})
    return property_model(p)


async def delete_property(property_id):
    await db.properties.delete_one({"_id": ObjectId(property_id)})
    return {"msg": "deleted"}


async def update_property(property_id, data):
    await db.properties.update_one(
        {"_id": ObjectId(property_id)},
        {"$set": data}
    )
    return {"msg": "updated"}