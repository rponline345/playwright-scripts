import os
import re
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
    page.goto("https://core.test.sgop.cloud")
    
    print("SGOP_USER gesetzt:", username)
    print("SGOP_PASSWORD gesetzt:", password)
    
    page.get_by_role("textbox", name="Username or email").fill(username)
    page.get_by_role("textbox", name="Username or email").press("Tab")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(15000) # 15 Sekunden
    page.get_by_role("textbox", name="Suche...").click()
    page.wait_for_timeout(15000) # 15 Sekunden
    page.get_by_role("textbox", name="Suche...").fill("Station 103")
    page.wait_for_timeout(15000) # 15 Sekunden
    page.get_by_text("Station 103 - Aldi (cv86646)•").click()
    page.wait_for_timeout(10000) # 10 Sekunden
    page.get_by_role("button", name="Detailansicht").click()
    

    # Erwartung + Aktion
    #detail_button = page.get_by_role("button", name="Detailansicht")
    #expect(detail_button).to_be_visible()
    #detail_button.click()

    # ---------------------
    page.wait_for_timeout(5000) # 5 Sekunden
    page.close()
