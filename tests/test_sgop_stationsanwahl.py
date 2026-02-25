import os
from playwright.sync_api import Page, expect

def test_sgop_stationsanwahl(page: Page) -> None:
    # Timeouts für langsame Login-/Redirect-Flows
    page.set_default_timeout(60_000)
    page.set_default_navigation_timeout(120_000)


    # Startseite / Login
    page.goto("http://core.test.sgop.cloud", wait_until="domcontentloaded")

    page.get_by_role("textbox", name="Username or email").fill("test-admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("5H~~9*#6f-2.014D|u~b873l}K<LxYoR")
    page.get_by_role("button", name="Sign In").click()
    

    # Suche / Station auswählen
    page.locator("div").filter(has_text="search").nth(2).click()
    page.get_by_role("textbox", name="Suche...").fill("Station 103")
    page.get_by_text("Station 103 - Aldi (cv86646)").click()

    # Erwartung + Aktion
    detail_button = page.get_by_role("button", name="Detailansicht")
    expect(detail_button).to_be_visible()
    detail_button.click()