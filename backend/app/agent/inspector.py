import asyncio
import os
from app.tools.browser_tool import take_screenshot_sync

async def inspector_node(state):
    print("🟡 INSPECTOR STARTED")

    properties = state.get("properties", [])
    loop = asyncio.get_event_loop()

    for p in properties:

        title = str(p.get("title", "property")).replace(" ", "_")
        folder = f"data/{title}"

        try:
            print("➡️ Taking screenshot for:", p.get("address"))

            screenshot_path = await loop.run_in_executor(
                None,
                take_screenshot_sync,
                p.get("address"),
                folder
            )

            print("✅ Screenshot saved:", screenshot_path)

            p["image"] = screenshot_path
            p["folder"] = folder

        except Exception as e:
            print("❌ ERROR:", e)
            p["image"] = "failed.png"

    return state