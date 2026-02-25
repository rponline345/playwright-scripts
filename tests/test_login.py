def test_login(page):
    page.goto("https://google.com")
    page.get_by_role("button", name="Sign In").click()