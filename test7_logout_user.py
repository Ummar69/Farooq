from playwright.sync_api import sync_playwright

def test_logout_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/")
        page.wait_for_selector('input[name="username"]')
        page.fill('input[name="username"]', "Admin")
        page.fill('input[name="password"]', "admin123")
        page.click('button[type="submit"]')
        page.wait_for_selector("img.oxd-userdropdown-img")
        page.click("img.oxd-userdropdown-img")
        page.wait_for_selector("text=Logout")
        page.click("text=Logout")
        page.wait_for_selector('input[name="username"]')
        assert page.locator('text=Login').is_visible()
        print("✅ Logout functionality test passed successfully!")
        browser.close()

test_logout_user()