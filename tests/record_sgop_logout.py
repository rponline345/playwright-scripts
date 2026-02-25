import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://oidc.sgop.cloud/realms/test/protocol/openid-connect/auth?client_id=core&redirect_uri=https%3A%2F%2Fcore.test.sgop.cloud&response_type=code&scope=offline_access%20openid%20email%20profile&nonce=a82d765a8f40153719eaf37e68ff162b65wQaACfn&state=694d790e090d467179b0bc7160077d02ede4Go19R&code_challenge=aJ796OPIVW8q2S04kH7e0MaA6XlvHYIdAJCso7N2egg&code_challenge_method=S256")
    page.get_by_role("link", name="VIVAVIS Login").click()
    page.get_by_role("link", name="VIVAVIS AG").click()
    page.get_by_role("textbox", name="Geben Sie Ihre E-Mail-Adresse").fill("robert.pyttel@vivavis.com")
    page.get_by_role("textbox", name="Geben Sie Ihre E-Mail-Adresse").press("Enter")
    page.get_by_role("button", name="Weiter", exact=True).click()
    page.locator("#i0118").fill("Flammenwerfer123!")
    page.locator("#i0118").press("Enter")
    page.get_by_role("button", name="Anmelden").click()
    page.goto("https://core.test.sgop.cloud/network")
    page.get_by_role("region", name="Map").click(position={"x":705,"y":391})
    page.get_by_role("region", name="Map").press("ArrowDown")
    page.get_by_role("region", name="Map").press("ArrowUp")
    page.get_by_role("region", name="Map").press("ArrowUp")
    page.get_by_role("region", name="Map").press("ArrowUp")
    page.get_by_role("region", name="Map").press("ArrowUp")
    page.get_by_role("region", name="Map").press("ArrowUp")
    page.get_by_role("region", name="Map").press("ArrowUp")
    page.get_by_role("region", name="Map").press("ArrowUp")
    page.get_by_role("button").filter(has_text="person").click()
    page.get_by_role("button").filter(has_text="person").press("ArrowRight")
    page.get_by_role("button").filter(has_text="person").press("ArrowRight")
    page.get_by_role("button").filter(has_text="person").press("ArrowRight")
    page.get_by_role("button").filter(has_text="person").press("ArrowRight")
    page.get_by_role("button").filter(has_text="person").press("ArrowRight")
    page.get_by_role("button").filter(has_text="person").press("ArrowRight")
    page.get_by_role("button").filter(has_text="person").press("ArrowRight")
    page.locator(".user-navigation-backdrop").click()
    page.get_by_role("button").filter(has_text="person").click()
    page.locator(".user-navigation-backdrop").click()
    page.get_by_role("button").filter(has_text="person").click()
    page.get_by_text("logoutAbmelden").click()
    page.locator("[data-test-id=\"robert.pyttel@vivavis.com\"]").click()
    page.locator("div").nth(1).click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
