import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    context.set_default_timeout(60_000)  # 60 Sekunden
    page = context.new_page()
    page.locator("body").click()
    page.goto("http://core.test.sgop.cloud")
    page.get_by_role("textbox", name="Username or email").fill("test-admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("5H~~9*#6f-2.014D|u~b873l}K<LxYoR")
    page.get_by_role("button", name="Sign In").click()
    page.locator("div").filter(has_text="search").nth(2).click()
    page.get_by_role("textbox", name="Suche...").fill("Station 103")
    page.get_by_text("Station 103 - Aldi (cv86646)").click()
    page.get_by_role("button", name="Detailansicht").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
