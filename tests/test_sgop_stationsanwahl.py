import os
from playwright.sync_api import Page, expect

def test_sgop_stationsanwahl(page: Page) -> None:
    # Timeouts für langsame Login-/Redirect-Flows
    page.set_default_timeout(300_000)
    page.set_default_navigation_timeout(600_000)

    username = os.getenv("SGOP_USER")
    password = os.getenv("SGOP_PASSWORD")

    assert username, "Umgebungsvariable SGOP_USER fehlt"
    assert password, "Umgebungsvariable SGOP_PASSWORD fehlt"
    

    # Startseite / Login
    page.goto("http://core.test.sgop.cloud", wait_until="domcontentloaded")

    page.get_by_role("textbox", name="Username or email").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Sign In").click()
    

    # Suche / Station auswählen
    page.locator("div").filter(has_text="search").nth(2).click()
    page.get_by_role("textbox", name="Suche...").fill("Station 103")
    page.get_by_text("Station 103 - Aldi (cv86646)").click()

    # Erwartung + Aktion
    detail_button = page.get_by_role("button", name="Detailansicht")
    expect(detail_button).to_be_visible()
    detail_button.click()