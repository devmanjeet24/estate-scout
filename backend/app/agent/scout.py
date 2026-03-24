from app.tools.search_tool import search_properties
from app.core.llm import get_llm


async def scout_node(state):
    print("🟢 SCOUT STARTED")

    query = state["query"]
    prefs = state.get("user_preferences", {})

    llm = get_llm()

    # ✅ AI enhancement
    enhanced_query = f"""
User wants: {query}
Preferences: {prefs}

Generate better search query for real estate:
"""

    ai_query = llm.invoke(enhanced_query).content

    raw_results = search_properties(ai_query)

    properties = []

    for r in raw_results:
        properties.append({
            "title": r.get("title"),
            "address": r.get("title"),
            "description": r.get("description", "")[:150],
            "price": "20000",
            "image": "/assets/images/streetview.webp"
        })

    return {**state, "properties": properties}