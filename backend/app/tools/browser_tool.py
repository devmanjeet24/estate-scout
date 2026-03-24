# import os
# from playwright.async_api import async_playwright

# async def take_screenshot(address, folder):
#     async with async_playwright() as p:
#         browser = await p.chromium.launch()
#         page = await browser.new_page()

#         await page.goto("http://localhost:3000/map-simulator")
#         await page.fill("#search", address)
#         await page.click("#search-btn")

#         await page.wait_for_selector("#result img")

#         os.makedirs(folder, exist_ok=True)

#         path = os.path.join(folder, "view.png")
#         await page.locator("#result").screenshot(path=path)

#         await browser.close()

#         return path