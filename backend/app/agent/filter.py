async def filter_node(state):
    prefs = state.get("user_preferences", {})
    budget = prefs.get("budget")

    filtered = []

    for p in state.get("properties", []):
        try:
            if budget and int(p["price"]) > int(budget):
                continue
            filtered.append(p)
        except:
            filtered.append(p)

    return {**state, "properties": filtered}