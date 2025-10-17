from playwright.sync_api import sync_playwright

def test_admin_module():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/")
        page.fill('input[name="username"]', "Admin")
        page.fill('input[name="password"]', "admin123")
        page.click('button[type="submit"]')
        page.wait_for_selector("text=Dashboard")
        page.click("text=Admin")
        assert page.is_visible("text=User Management")
        browser.close()

test_admin_module()

