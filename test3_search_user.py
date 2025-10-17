from playwright.sync_api import sync_playwright

def test_search_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/")
        page.wait_for_selector('input[name="username"]')
        page.fill('input[name="username"]', "Admin")
        page.fill('input[name="password"]', "admin123")
        page.click('button[type="submit"]')
        page.wait_for_selector("text=Admin")
        page.click("text=Admin")
        page.wait_for_selector('input[placeholder="Username"]')
        page.fill('input[placeholder="Username"]', "Admin")
        page.click("button:has-text('Search')")
        page.wait_for_selector("text=Admin")
        assert page.locator("text=Admin").is_visible()
        print("✅ Search user test passed successfully!")
        browser.close()

test_search_user()