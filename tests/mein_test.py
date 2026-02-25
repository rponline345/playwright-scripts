import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://oidc.sgop.cloud/realms/test/protocol/openid-connect/auth?client_id=core&redirect_uri=https%3A%2F%2Fcore.test.sgop.cloud&response_type=code&scope=offline_access%20openid%20email%20profile&nonce=21e43586002faf18268c54fedd80059dd9LmJtrL1&state=2127893d67ea85971d17370f8f1cc4c93aawFTiQJ&code_challenge=sgIpUapnHj3UHnXsSiCG-wy-LUMuVeohJqwjLNbFc44&code_challenge_method=S256")
    page.locator("div").nth(1).click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
