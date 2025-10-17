from playwright.sync_api import sync_playwright

def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/")
        page.wait_for_selector('input[name="username"]')
        page.fill('input[name="username"]', "WrongUser")
        page.fill('input[name="password"]', "wrongpass")
        page.click('button[type="submit"]')
        page.wait_for_selector("text=Invalid credentials")
        assert page.locator("text=Invalid credentials").is_visible()
        print("✅ Invalid login test passed — error message displayed successfully!")
        browser.close()

test_invalid_login()