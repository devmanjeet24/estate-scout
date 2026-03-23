import os
from playwright.sync_api import sync_playwright

def take_screenshot_sync(address: str, folder: str):

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # load local map.html
        file_path = os.path.abspath("map.html")
        page.goto(f"file:///{file_path}")

        # type + click
        page.fill("#search", address)
        page.click("#search-btn")

        # WAIT FOR RESULT TO LOAD
        page.wait_for_selector("#result img")
        page.wait_for_timeout(1000)

        # ensure folder exists
        os.makedirs(folder, exist_ok=True)

        screenshot_path = os.path.join(folder, "view.png")

        # take screenshot of result section ONLY
        element = page.query_selector("#result")
        element.screenshot(path=screenshot_path)

        browser.close()

        return screenshot_path