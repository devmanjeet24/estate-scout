from app.tools.search_tool import search_properties

async def scout_node(state):
    print("🟢 SCOUT STARTED")
    query = state["query"]

    raw_results = search_properties(query)

    properties = []

    for r in raw_results:
        properties.append({
            "title": r.get("title"),
            "address": r.get("address"),
            "description": r.get("description", "")[:150],  # trim
            "price": "20000"
        })

        print("🟢 SCOUT OUTPUT:", properties)

    return {**state, "properties": properties}