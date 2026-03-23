from app.db.database import db
from app.models.property_model import property_model
from app.utils.logger import logger

async def create_property(property_data, user_email):
    try:
        data = property_data.dict()
        data["created_by"] = user_email

        result = await db.properties.insert_one(data)

        logger.info(f"Property created: {result.inserted_id}")

        return {"msg": "Property created"}

    except Exception as e:
        logger.error(f"Error creating property: {str(e)}")
        raise Exception("Failed to create property")


async def get_all_properties(user_email):
    try:
        properties = []

        async for p in db.properties.find({"created_by": user_email}):
            properties.append(property_model(p))

        return properties

    except Exception as e:
        logger.error(f"Error fetching properties: {str(e)}")
        raise Exception("Failed to fetch properties")


async def get_property_by_id(property_id):
    try:
        p = await db.properties.find_one({"_id": property_id})

        if not p:
            raise Exception("Property not found")

        return property_model(p)

    except Exception as e:
        logger.error(f"Error fetching property: {str(e)}")
        raise Exception("Error getting property")