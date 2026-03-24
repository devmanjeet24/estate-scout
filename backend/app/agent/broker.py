import os
import re


async def broker_node(state):
    print("🔵 BROKER STARTED")

    updated = []

    for p in state.get("properties", []):
        p["lease"] = f"Lease for {p.get('title')} at {p.get('price')}"
        updated.append(p)

    return {**state, "properties": updated}