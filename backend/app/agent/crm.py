from app.db.database import db

async def crm_node(state):

    saved_properties = []

    for p in state["properties"]:
        result = await db.properties.insert_one(p)

        # attach id
        p["_id"] = str(result.inserted_id)

        saved_properties.append(p)

    return {**state, "properties": saved_properties}