from app.db.database import db
from app.core.llm import get_llm


async def crm_node(state):

    print("🟣 CRM STARTED")

    user_email = state.get("user_email")
    query = state.get("query")

    llm = get_llm()

    # ✅ extract preferences from chat
    prompt = f"""
Extract user preferences from this:
"{query}"

Return JSON like:
{{"pet": true, "parking": true, "budget": 20000}}
"""

    try:
        ai_res = llm.invoke(prompt).content
        prefs = eval(ai_res) if ai_res else {}
    except:
        prefs = {}

    # ✅ save preferences
    if prefs:
        await db.users.update_one(
            {"email": user_email},
            {"$set": {"preferences": prefs}}
        )

    saved = []

    for p in state.get("properties", []):
        p["created_by"] = user_email
        result = await db.properties.insert_one(p)
        p["_id"] = str(result.inserted_id)
        saved.append(p)

    return {**state, "properties": saved}