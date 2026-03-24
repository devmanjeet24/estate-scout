# import asyncio
# import os
# from playwright.async_api import async_playwright


# async def inspector_node(state):
#     print("🟡 INSPECTOR STARTED")

#     properties = state.get("properties", [])

#     for p in properties:
#         try:
#             title = str(p.get("title", "property")).replace(" ", "_")
#             folder = f"data/{title}"

#             os.makedirs(folder, exist_ok=True)

#             async with async_playwright() as playwright:
#                 browser = await playwright.chromium.launch(headless=True)
#                 page = await browser.new_page()

#                 await page.goto("http://localhost:3000/map-simulator")

#                 await page.fill("#search", p.get("address"))
#                 await page.click("#search-btn")

#                 await page.wait_for_selector("#result img")

#                 path = os.path.join(folder, "view.png")

#                 await page.locator("#result").screenshot(path=path)

#                 await browser.close()

#             p["image"] = path
#             p["folder"] = folder

#         except Exception as e:
#             print("❌ INSPECTOR ERROR:", str(e))
#             p["image"] = None

#     return state