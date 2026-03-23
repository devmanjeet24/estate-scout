import os

async def broker_node(state):

    for p in state.get("properties", []):

        title = str(p.get("title", "property")).replace(" ", "_")
        folder = f"data/{title}"

        os.makedirs(folder, exist_ok=True)

        # always create lease file
        lease_path = os.path.join(folder, "lease.txt")

        with open(lease_path, "w", encoding="utf-8") as f:
            f.write(f"""
Lease Agreement
Title: {p.get('title')}
Address: {p.get('address')}
Price: {p.get('price')}
""")

        p["folder"] = folder

    return state